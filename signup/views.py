from django.shortcuts import render, redirect
from .forms import SignupModelForm
from home.models import MyUser
from django.contrib import messages



def get_signup(request):
    form = SignupModelForm(request.POST or request.FILES or None)
    if form .is_valid():
        instance = form.save(commit=False)
<<<<<<< HEAD
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
=======
        # Signup fields
>>>>>>> e94b0c35046f04a1ca04b3fab1b21d59d59fb29b
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        user = MyUser(
            username=username,
            phone_number=phone_number,
            password=password
        )

        user.set_password(password)
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Registration successfully complete')
        return redirect('login')
    return render(request, 'signup.html', {"form": form})
