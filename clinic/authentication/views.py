from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import create_user, get_user_password

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
    if request.method == "GET":
        
        if request.session.get("user_id", None) != None:
            return redirect('/')
        
        return render(request, 'signin.html')
    
    elif request.method == "POST":
        
        username = request.POST["username"]
                
        error = None
        
        try:
            # attempt to signin
            user_info = get_user_password(username) # returns tuple
            if check_password(request.POST["password"], user_info[0]):
                request.session["user_id"] = user_info[1]
                return redirect('/')
            else:
                print("fail")
            
        except Exception as e:
            print(str(e))
            error = "Your username or password is incorrect."
        
        return render(request, 'signin.html', {"error": error})
    
def signout(request):
    '''
    View for signing a user out.
    '''
    if request.method == "GET":
        if request.session.get("user_id", None) != None:
            request.session.pop("user_id")
        
        return redirect('/auth/signin')
    
def login_required(view):
    '''
    Decorator for redirecting if user is not logged in.
    '''
    def wrapper(*args, **kwargs):
        if args[0].session.get("user_id", None) == None:
            return redirect('auth/signin')
        else:
            return view(*args, **kwargs)
        
    return wrapper