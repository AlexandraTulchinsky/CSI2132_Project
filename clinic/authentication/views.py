from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import create_user, get_user_password, get_all_user_data
from django.db import connection

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
            user_info = get_user_password(username)
            request.session["user_id"] = user_info[1]
            request.session["user_type"] = user_info[2]
            
        except Exception as e:
            print(str(e))
            error = "There was an issue creating your account."
        
        # keep use on signup page if there was an error creating the account
        if error:
            return render(request, 'signup.html', {"error": error})
        
        else:
                            
            if user_info[2] != "Patient":
                return redirect('/auth/createemployee')
            else:
                
                if request.session["user_type"] == "Receptionist":
                    return redirect('/Receptionist/menu')
                
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
                request.session["user_type"] = user_info[2]
                
                if request.session["user_type"] == "Receptionist":
                    return redirect('/Receptionist/menu')
                
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
        if request.session.get("user_type", None) != None:
            request.session.pop("user_type")
        
        return redirect('/auth/signin')

def login_required(view):
    '''
    Decorator for redirecting if user is not logged in.
    '''
    def wrapper(*args, **kwargs):
        
        if type(args[0]) == int or args[0].session.get("user_id", None) == None:
            return redirect('/auth/signin')
        else:
            return view(*args, **kwargs)
        
    return wrapper

@login_required
def create_employee(request):
    '''
    View for creating an employee
    '''
    if request.method == "GET":
        return render(request, 'create_employee.html')
    
    if request.method == "POST":
        # query user data
        user_id = request.session.get("user_id")

        user_data = get_all_user_data(user_id)
        email = user_data[1]
        username = user_data[2]
        password = user_data[3]
        user_type = user_data[5]
        
        SSN = request.POST["ssn"]
        first = request.POST["first_name"]
        last = request.POST["last_name"]
        salary = request.POST["salary"]
        title = request.POST["title"]
        
        error = None
        
        try: 
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO "Employee" VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', [user_id, email, username, password, 0, user_type, user_id, SSN, first, last, user_type, salary, title])
            
        except Exception as e:
            print(str(e))
            error = "There was an issue creating your employee account."
        
        # keep use on signup page if there was an error creating the account
        if error:
            return render(request, 'create_employee.html', {"error": error})
        
        else:
            return redirect('/')
        