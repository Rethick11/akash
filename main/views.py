from django.shortcuts import render # type: ignore

def home(request):
    return render(request, 'main/home.html', {'show_footer': True})

def login_register(request, action):
    if action == 'login':
        title = "Login"
        is_login = True
    else:
        title = "Register"
        is_login = False
    return render(request, 'main/login-register.html', {'title': title, 'is_login': is_login, 'show_footer': False})
