from django import forms

class SignUpForm(forms.Form):

    name = forms.CharField(
        max_length=25,
        label="Username"
    )
    password = forms.CharField(
        max_length=12,
        label="Password"
    )
    mobile = forms.IntegerField(
        label="Mobile Number"
    )


class SignInForm(forms.Form):

    name = forms.CharField(
        max_length=25,
        label="Username"
    )
    password = forms.CharField(
        max_length=12,
        label="Password"
    )


class ProductForm(forms.Form):

    product_name = forms.CharField(
        max_length=30, 
        label="Product Name"
    )
    category = forms.CharField(
        max_length=30,
        label="Category"
    )
    price = forms.IntegerField(
        label="Price"
    )
    discount = forms.IntegerField(
        label="Discount"
    )
    quantity_available = forms.IntegerField(
        label="Quantity"
    )
