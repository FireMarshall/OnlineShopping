from django.shortcuts import render

from shopping_app.forms import ProductForm, SignInForm, SignUpForm
from shopping_app.models import CartItem, Product, User

# Create your views here.
is_logged_in = False
current_username = ''

def signin(request):
    if request.method == "POST":
        form_data = SignInForm(request.POST)
        if form_data.is_valid():
            name = request.POST.get('name').strip()
            password = request.POST.get('password').strip()
            user_model = User.objects.filter(name=name)
            print(user_model)
            if user_model:
                if user_model[0].password == password:
                    is_logged_in = False
                    current_username = name
                    return render(request, 'shopping_app/homepage.html')
                else:
                    error_message = "Wrong Password"
                    return render(request, 'shopping_app/signin.html', {
                        'signin_form': form_data, 
                        'error_message': error_message
                    })
    signin_form = SignInForm()
    return render(request, 'shopping_app/signin.html', {'signin_form': signin_form})


def signup(request):
    if request.method == "POST":
        form_data = SignUpForm(request.POST)
        if form_data.is_valid():
            name = request.POST.get('name')
            password = request.POST.get('password')
            mobile = request.POST.get('mobile')
            user_model = User(name=name, password=password, mobile=mobile)
            user_model.save()
            return render(request, 'shopping_app/homepage.html')
        else:
            return render(request, 'shopping_app/signup.html', {'signup_form': form_data})
    signup_form = SignUpForm()
    return render(request, 'shopping_app/signup.html', {'signup_form': signup_form})


def add_product(request):
    product_form = ProductForm()
    return render(request, 'shopping_app/add_product.html', {'product_form': product_form})


def view_cart(request):

    return render(request, 'shopping_app/cart.html')


def homepage(request):

    return render(request, 'shopping_app/homepage.html')

def remove_item(request, item_id):

    return view_cart(request)


def logout(request):

    is_logged_in = False
    current_username = ''
    return signin(request)