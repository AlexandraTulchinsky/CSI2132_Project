from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import create_user

def signup(request):
    '''
    View for creating a new user.
    '''
    if request.method == "GET":
        return render(request, 'signup.html')
    
    elif request.method == "POST":
        
        email = request.POST["email"]
        username = request.POST["username"]
        pass_hash = make_password(request.POST["password"]) # create password hash
        type = request.POST.get("type")
        error = None
        
        # attempt to create the new user
        try:
            create_user(email, username, pass_hash, type)
            
        except Exception as e:
            print(str(e))
            error = "There was an issue creating your account."
        
        # keep use on signup page if there was an error creating the account
        if error:
            return render(request, 'signup.html', {"error": error})
        
        else:
            return redirect('/')
        
    
def signin(request):
    '''
    View for signing a user in.
    '''
    
    
def signout(request):
    '''
    View for signing a user out.
    '''