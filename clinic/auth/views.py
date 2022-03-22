from django.shortcuts import render

def signup(request):
    '''
    View for creating a new user.
    '''
    
    return render(request, 'signup.html')
    
def signin(request):
    '''
    View for signing a user in.
    '''
    
def logout(request):
    '''
    View for logging a user out.
    '''