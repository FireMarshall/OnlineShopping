from django.shortcuts import render
import datetime
from shopping_app.forms import ProductForm, SignInForm, SignUpForm, FilterForm
from shopping_app.models import CartItem, Product, User

# Create your views here.
is_logged_in = False
is_admin = False
current_username = ''
categories = ['All', 'Men', 'Women', 'Kids', 'Cosmetics', 'Bags', 'Watches']
sort_type = ["date_added", "discount", "Low-to-High", "High-to-Low"]


def signin(request):
    global is_logged_in, current_username, is_admin
    if request.method == "POST":
        form_data = SignInForm(request.POST)
        if form_data.is_valid():
            name = request.POST.get('name').strip()
            password = request.POST.get('password').strip()
            user_model = User.objects.filter(name=name)
            print(user_model)
            if user_model:
                if user_model[0].password == password:
                    is_logged_in = True
                    current_username = 'admin'
                    is_admin = name == 'admin'
                    if is_admin:
                        product_form = ProductForm()
                        return render(request, 'shopping_app/add_product.html', {'product_form': product_form})
                    current_username = request.POST.get('name')
                    return homepage(request)
                else:
                    error_message = "Wrong Password"
                    return render(request, 'shopping_app/signin.html', {
                        'signin_form': form_data, 
                        'error_message': error_message
                    })
    signin_form = SignInForm()
    return render(request, 'shopping_app/signin.html', {'signin_form': signin_form})


def signup(request):
    global is_logged_in, current_username
    if request.method == "POST":
        form_data = SignUpForm(request.POST)
        if form_data.is_valid():
            is_logged_in = True
            name = request.POST.get('name')
            current_username = request.POST.get('name')
            password = request.POST.get('password')
            mobile = request.POST.get('mobile')
            user_model = User(name=name, password=password, mobile=mobile)
            user_model.save()
            return homepage(request)
        else:
            return render(request, 'shopping_app/signup.html', {'signup_form': form_data})
    signup_form = SignUpForm()
    return render(request, 'shopping_app/signup.html', {'signup_form': signup_form})


def add_product(request):
    if is_admin == False:
        signin_form = SignInForm()
        error_message = "You must sign in as admin to add product"
        return render(request, 'shopping_app/signin.html', {
                        'signin_form': signin_form,
                        'error_message': error_message
                    })
    if is_logged_in == False or current_username == '':
        return signin(request)
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        category = categories[int(request.POST.get('category'))]
        price = int(request.POST.get('price'))
        discount = int(request.POST.get('discount'))
        quantity_available = int(request.POST.get('quantity_available'))
        img_link = request.POST.get('img_url')
        product = Product(
            product_name=product_name,
            category=category,
            price=price,
            discount=discount,
            quantity_available=quantity_available,
            selling_price = price - price*discount/100,
            date_added=datetime.datetime.now(),
            img_link=img_link
        )
        product.save()
        message = 'Added Successfully'
        product_form = ProductForm()
        return render(request, 'shopping_app/add_product.html', {'product_form': product_form, 'message': message})
    product_form = ProductForm()
    return render(request, 'shopping_app/add_product.html', {'product_form': product_form})


def homepage(request):
    if is_logged_in == False or current_username == '':
        return signin(request)
    if request.method == "POST":
        filter_form = FilterForm(request.POST)
        if filter_form.is_valid():
            filter_by = categories[int(request.POST.get('category')[0])]
            sort_by = int(request.POST.get('sort_by')[0])
            print(sort_by,filter_by)
            if sort_by == 0:
                param = 'date_added'
            elif sort_by == 1:
                param = '-discount'
            elif sort_by == 2:
                param = 'selling_price'
            else:
                param = '-selling_price'

            if filter_by == 'All':
                products = Product.objects.order_by(param)
            else:
                products = Product.objects.filter(category=filter_by).order_by(param)

            return render(request, 'shopping_app/homepage.html', {'products': products, 'filter_form': filter_form})
    products = Product.objects.all()
    filter_form = FilterForm()
    return render(request, 'shopping_app/homepage.html', {'products': products, 'filter_form': filter_form})


def add_to_cart(request, item_name):
    if is_logged_in == False or current_username == '':
        return signin(request)
    if request.method == "POST":
        quantity = int(request.POST.get(item_name))
        product = Product.objects.filter(product_name=item_name)[0]
        cart_item = CartItem(
            username=current_username,
            product_name=product.product_name,
            category=product.category,
            price=product.price,
            selling_price=product.selling_price,
            discount=product.discount,
            total_price=product.selling_price*quantity,
            quantity_added=quantity
        )
        cart_item.save()
        product.quantity_available -= int(quantity)
        product.save()
    return homepage(request)


def view_cart(request):
    if is_logged_in == False or current_username == '':
        return signin(request)
    cart_items = CartItem.objects.filter(username=current_username)
    items = CartItem.objects.filter(username=current_username)
    if items:
        total = sum(map(lambda item: item.total_price, items))
    else:
        total = 0
    return render(request, 'shopping_app/cart.html', {'cart_items': cart_items, 'total': total})


def remove_item(request, item_name):
    if is_logged_in == False or current_username == '':
        return signin(request)
    cart_item = CartItem.objects.filter(username=current_username, product_name=item_name)[0]
    product = Product.objects.filter(product_name=item_name)[0]
    product.quantity_available += cart_item.quantity_added
    product.save()
    cart_item.delete()
    return view_cart(request)


def logout(request):
    is_logged_in = False
    current_username = ''
    return signin(request)