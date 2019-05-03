from django import forms

class SignUpForm(forms.Form):

    name = forms.CharField(
        max_length=25,
        label="Username"
    )
    password = forms.CharField(
        max_length=12,
        widget=forms.PasswordInput,
        label="Password",

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
        label="Password",
        widget=forms.PasswordInput(),

    )


class ProductForm(forms.Form):

    product_name = forms.CharField(
        max_length=30, 
        label="Product Name"
    )
    category = forms.ChoiceField(
        label="Category",
        choices=[
            (1, 'Men'),
            (2, 'Women'),
            (3, 'Kids'),
            (4, 'Cosmetics'),
            (5, 'Bags'),
            (6, 'Watches')
        ]
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
    img_link = forms.URLField(
        label="Product Image URL"
    )

class FilterForm(forms.Form):

    category = forms.ChoiceField(
        label='Category',
        choices=[
            (0, 'All'),
            (1, 'Men'),
            (2, 'Women'),
            (3, 'Kids'),
            (4, 'Cosmetics'),
            (5, 'Bags'),
            (6, 'Watches')
        ]
    )
    sort_by = forms.ChoiceField(
        label='Sort By',
        choices=[
            (0, 'New Arrival'),
            (1, 'Discount'),
            (2, 'Low to High'),
            (3, 'High to Low'),
        ]
    )
