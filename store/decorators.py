from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticatedUser(view_func):
    # restricting logged in user to see loginpage again through decorator
    def wrapper_func_unauth(request, *args, **kwargs):
        if request.user.is_authenticated:
         return redirect('store')
        else:
          return view_func(request, *args, **kwargs)
    return wrapper_func_unauth

# allowing users as per theier roles , be it admin , customer etc
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func_allowed_users(request,*args,**kwargs):
            print("in wrapper func_above group")
            group = None
            if request.user.groups.exists():
                print("in request.user.groups.exists()")
                group=request.user.groups.all()[0].name
                print(group)

            if group in allowed_roles:
                print("in group in allowed_roles")
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse("You are not authorized to view this page")
                       
        return wrapper_func_allowed_users
    return decorator


def admin_only(view_func):
    def wrapper_func_admin(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        
        if group =='customer':
            return redirect('user-page')
        
        if group =='admin':
            return view_func(request,*args,**kwargs)
        else:
            return HttpResponse("You are not authorized to view this page")  
        
    return wrapper_func_admin
