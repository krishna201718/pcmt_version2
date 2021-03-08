from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse


def unauthenticated_user(view_func):
    def wraper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("college:student_data_view")
        else:
            return redirect("college:login")

    return wraper_func


def allowed_users(allowed_roles=[]):
    def decorator_used(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                if (('student' in allowed_roles) and (request.user.is_student ))or \
                        (('staff' in allowed_roles) and (request.user.is_teacher)) \
                        or (('admin' in allowed_roles) and (request.user.is_admin)) :
                    print("yes")
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse("You are not authorized to view this page <h1> <a href=" + "{%url 'college:login'%}" + ">return to login</a><h/1>")
            else:
                return redirect("college:login")
        return wrapper_func

    return decorator_used
