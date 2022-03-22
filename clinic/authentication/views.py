from django.shortcuts import render

def signup(request):
    '''
    View for creating a new user.
    '''
    if request.method == "GET":
        return render(request, 'signup.html')
    
    elif request.method == "POST":
        pass
    
def signin(request):
    '''
    View for signing a user in.
    '''
    
def signout(request):
    '''
    View for signing a user out.
    '''