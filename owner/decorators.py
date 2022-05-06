from django.shortcuts import redirect

def owner_permission_required(fun):
    def wrapper(request,*args,**kwargs):
        if request.user.is_superuser:
            return fun(request,*args,**kwargs)
        else:
            return redirect("signin")
    return wrapper