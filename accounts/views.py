from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserDetails,Cart,Entry
from django.contrib.auth.hashers import make_password,check_password
from email_validator import validate_email
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import validate_email
from django.http import HttpResponse
from django.shortcuts import render
from .models import UserDetails,ProductCategory,Products
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib.messages import get_messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required






def home(request):
    storage = get_messages(request)
    products = Products.objects.select_related('category').all()
    categorys = ProductCategory.objects.all()
    product_Image ={}
    for product in products:
        category_name = product.category.name
        product_image = product.productimage
  
        category_id = product.category.id
        
        # Check if the category has already been displayed
        if category_name not in product_Image:
            product_Image[category_name] = {'image_url': product_image, 'category_id': category_id}

    messages_list = list(storage)
    # print(category_id)
    return render(request, 'home.html',{'messages': messages_list,'products':product_Image,'categorys': categorys})
def Form(request):
    if request.method == 'POST':
        Name = request.POST['name']
        Email = request.POST['email']
        Password = request.POST['password']
        print(Password)
            
        
        # Validate email format
        try:
            validate_email(Email)
        except ValidationError:
            return HttpResponse("Invalid email format")

        # Check if a user with the same name or email already exists
        existing_users_name = UserDetails.objects.filter(Name=Name)
        existing_users_email = UserDetails.objects.filter(email=Email)

        if existing_users_name.exists():
            messages.error( request,"User with this name already exists")
            return render(request, 'Form.html')

        if existing_users_email.exists():
            messages.error(request,"User with this email already exists")
            return render(request, 'Form.html')
        # If the user doesn't exist, create a new one
        encrypted_password = make_password(Password)
        data = UserDetails(Name=Name, email=Email, password=encrypted_password)
        data.save()
        messages.success(request, 'Form submitted successfully.')
        return render(request, 'Form.html')
    else:
        return render(request, 'Form.html')
def sign(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        password = request.POST['password']
        
        try:
            user = UserDetails.objects.get(Name=Name)
            stored_password = user.password  
            check = check_password(password, stored_password)
            if check:
                messages.success(request, f'Login is successful for {Name}')
                return render(request, "Product.html")
            else:
                messages.warning(request, 'Wrong password')
                return render(request, ".html")
        except UserDetails.DoesNotExist:
            messages.warning(request, "The user does not exist")
            return render(request, "Form.html")

    return render(request, "home.html")
def products(request): 
    categories = ProductCategory.objects.all()
    print(categories)
    context ={'categories':categories}
    if request.method == 'POST':
        Pname = request.POST['productName']
        ProductDescription = request.POST['ProductDescription']
        category= request.POST.get('category')
        Brand = request.POST['Brand']
        price = request.POST['price']
        is_available = request.POST.get('checkbox', False)
        
        upload = request.FILES['upload']
        
        try:
            
            category1 = ProductCategory.objects.get(pk=category)
            data = Products(name=Pname, ProductDescription=ProductDescription, category=category1, Brand=Brand, price=price, is_available=is_available,productimage=upload)
             
            if data:
                data.is_available = True
                data.save()
                messages.success(request,"Successfull!!!!")
                return redirect("/")
            else:
                messages.error(request, "Failed to save the data")
               
        except ProductCategory.DoesNotExist:
            messages.error(request, "Please Enter the Category")
       
    # else:
    #     messages.error( request,"Cannot Upload in the Database")
    return render(request,"Product.html",context)


def Cloth(request,category_id): 
    if(ProductCategory.objects.filter(pk = category_id)):
        products =Products.objects.filter(category__id = category_id)
        product_category=ProductCategory.objects.filter(pk = category_id)
        context = {'products':products,
                   'products_category':product_category}
        return render(request,"Cloth.html",context)
    else:
        messages.warning("sorry")
def detail(request,pk):
    Products_Detail = Products.objects.get(pk=pk) 
    
    return render(request,"Detail.html",{'products':Products_Detail})
    

@login_required(login_url='sign')  # Specify your login URL
def addToCart(request):
    if request.method == 'GET':
        current_val = request.GET.get('currentVal')
        print(current_val)

    # Rest of your view logic

    return render(request, "Detail.html")