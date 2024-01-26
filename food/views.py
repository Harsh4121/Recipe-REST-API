from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Receipe, UserProfile 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import UserProfile
from .forms import UserRegistrationForm
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            
            # Redirect to the main page (change 'receipes' to match your URL pattern)
            return redirect('receipes')

        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'login.html')



@login_required
def user_profile(request):
    # Try to get the UserProfile for the current user
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    context = {'user_profile': user_profile}
    return render(request, 'user_profile.html', context)

@login_required


def receipes(request):
    receipes_list = Receipe.objects.all()
    paginator = Paginator(receipes_list, 12)

    page = request.GET.get('page')
    try:
        receipes = paginator.page(page)
    except PageNotAnInteger:
        receipes = paginator.page(1)
    except EmptyPage:
        receipes = paginator.page(paginator.num_pages)

    context = {'receipes': receipes}

    # Add the following line to check if the user is authenticated
    context['user_authenticated'] = request.user.is_authenticated

    return render(request, 'receipes.html', context)
def add_receipe(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_discription = data.get('receipe_discription')

        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_discription=receipe_discription,
        )

        return redirect('/')

    return render(request, 'add_receipe.html')

def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_discription = data.get('receipe_discription')

        if receipe_discription:
            queryset.receipe_discription = receipe_discription

        queryset.receipe_name = receipe_name

        if 'receipe_image' in request.FILES:
            receipe_image = request.FILES['receipe_image']
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/')

    context = {'receipe': queryset}
    return render(request, 'update_receipes.html', context)

def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/')

def recipe_details(request, recipe_id):
    recipe = Receipe.objects.get(id=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'receipe_details.html', context)

@csrf_protect

def registration_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            
            # Redirect to the login page
            return redirect('login')
        else:
            # Print errors to console for debugging
            print("Form is not valid:")
            for field, errors in form.errors.items():
                print(f"{field}: {', '.join(errors)}")
            
            # Render the form with errors
            return render(request, 'registration.html', {'form': form, 'error': 'Form submission failed. Please check the form for errors.'})
    else:
        form = UserRegistrationForm()

    return render(request, 'registration.html', {'form': form})