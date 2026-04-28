from functools import wraps
from django.shortcuts import redirect


def editorial_login_required(view_func):
    """Redirect to editorial login if not authenticated."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('editorial:login')
        # Only users with editor, admin role OR staff/superuser can access
        if not (
            request.user.role in ('editor', 'admin')
            or request.user.is_staff
            or request.user.is_superuser
        ):
            return redirect('editorial:login')
        return view_func(request, *args, **kwargs)
    return wrapper


def admin_required(view_func):
    """Restrict view to admin role or superuser."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('editorial:login')
        if not (
            request.user.role == 'admin'
            or request.user.is_staff
            or request.user.is_superuser
        ):
            return redirect('editorial:dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper
