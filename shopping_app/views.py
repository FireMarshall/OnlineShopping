from django.shortcuts import render
import datetime
from shopping_app.forms import ProductForm, SignInForm, SignUpForm
from shopping_app.models import CartItem, Product, User

# Create your views here.
is_logged_in = False
current_username = ''
categories = ['', 'Men', 'Women', 'Kids', 'Cosmetics', 'Bags', 'Watches']
# sort_by = ['', "New Arrival", "Discount", "Low-to-High", "High-to-Low"]

def signin(request):
    global is_logged_in, current_username
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
    if is_logged_in == False:
        return signin(request)

    if request.method == "POST":
        product_name = request.POST.get('product_name')
        category = categories[int(request.POST.get('category'))]
        price = int(request.POST.get('price'))
        discount = int(request.POST.get('discount'))
        quantity_available = int(request.POST.get('quantity_available'))

        product = Product(
            product_name=product_name,
            category=category,
            price=price,
            discount=discount,
            quantity_available=quantity_available,
            selling_price = price - price*discount/100,
            date_added=datetime.datetime.now()
        )
        product.save()
        message = 'Added Successfully'
        product_form = ProductForm()
        return render(request, 'shopping_app/add_product.html', {'product_form': product_form, 'message': message})
    product_form = ProductForm()
    return render(request, 'shopping_app/add_product.html', {'product_form': product_form})


def homepage(request):
    products = Product.objects.all()
    return render(request, 'shopping_app/homepage.html', {'products': products})


def new_arrival(request):
    if is_logged_in == False:
        return signin(request)
    products = Product.objects.all()
    return render(request, 'shopping_app/homepage.html', {'products': products})


def sort_by_discount(request):
    if is_logged_in == False:
        return signin(request)
    products = Product.objects.all()
    return render(request, 'shopping_app/homepage.html', {'products': products})


def sort_high_to_low(request):
    if is_logged_in == False:
        return signin(request)
    products = Product.objects.all()
    return render(request, 'shopping_app/homepage.html', {'products': products})


def sort_low_to_high(request):
    if is_logged_in == False:
        return signin(request)
    products = Product.objects.all()
    return render(request, 'shopping_app/homepage.html', {'products': products})


def add_to_cart(request, item_name):
    if is_logged_in == False:
        return signin(request)
    if request.method == "POST":
        quantity = request.POST.get(item_name)
        product = Product.objects.filter(product_name=item_name)[0]
        cart_item = CartItem(
            username=current_username,
            product_name=product.product_name,
            category=product.category,
            price=product.selling_price,
            discount=product.discount,
            quantity_added=quantity
        )
        cart_item.save()
        product.quantity_available -= int(quantity)
        product.save()
    return homepage(request)


def view_cart(request):
    if is_logged_in == False:
        return signin(request)
    cart_items = CartItem.objects.filter(username=current_username)
    return render(request, 'shopping_app/cart.html', {'cart_items': cart_items})


def remove_item(request, item_id):
    if is_logged_in == False:
        return signin(request)

    return view_cart(request)


def logout(request):

    is_logged_in = False
    current_username = ''
    return signin(request)