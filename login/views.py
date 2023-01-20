from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

def is_user_valid(user):
    # Returns True if user is valid, False if not
    return not user is None


def get_username_and_password(request):
    # returns username, password from the form data
    return request.POST['username'], request.POST['password']

def get_user(username, password):
    # this returns a user object, and None if authentication failed
    return authenticate(username=username, password=password)

def log_user_in(request, user):
    # this logs the user in, so that the site cookies can register that this user is logged in
    login(request, user)

def login_failure():
    # run this method if login fails
    return HttpResponseRedirect(reverse('auth_task:login'))


def login_success():
    # run this method if login succeeds
    return HttpResponseRedirect(reverse('auth_task:show_user'))

# Create your views here.
def index(request):
    # Render your HTML for logging in here
    return render(request, "login.html")
    # pass

def authenticate_user(request):
    """
    For this part, you will need to use the following methods:
       - login_success()
       - login_failure()
       - log_user_in(request, user)
       - get_user(username, password)
       - get_username_and_password(request)
       - is_user_valid(user)
    """
    # TODO: Authenticate user for logging in
    # Get username and password from form data contained in request
    
    # get user with username and password
    
    # If user is valid, log them in and redirect them to login_success
    
    # Otherwise, redirect them to login_failure
    pass # This line can be removed once the method has been filled in
    

def get_username_and_password_from_session(request):
    return request.user.username, request.user.password

def render_user_details(request, username, password):
    # Returns the view for showing the user details
    return render(request, 'user_details.html', {
        'username': username,
        'password': password
    })

def show_user(request):
    """
    For this view, you will need the following methods:
        - get_username_and_password_from_session(request)
        - render_user_details(request, username, password)
    """
    # TODO: Display user details
    pass # This line can be removed once the method has been filled in