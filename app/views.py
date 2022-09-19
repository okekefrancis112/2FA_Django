from django.shortcuts import render,redirect
from app.forms import CustomUserCreationForm, ReportForm
from app.models import CustomUser,Report
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django_otp.decorators import otp_required
from two_factor.views import LoginView
# from cryptography.fernet import Fernet


@login_required
def home_view(request):
    reports = Report.objects.filter(user=request.user)
    
    context = {
        'reports':reports,
    }
    return render(request,'app/home.html',context)

@login_required
def create_report(request):
    form = ReportForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            # title = form.cleaned_data[b'title']
            # description = form.cleaned_data[b'description']
            # key = Fernet.generate_key()
            # crypt = Fernet(key) 
            # entitle = crypt.encrypt(title)
            # endescription = crypt.decrypt(description)
            report = form.save(commit=False)
            
            report.user = request.user
            report.save()
            return redirect('home')
            
    context = {
        'form':form,
    }
    return render(request,'app/report-form.html',context)



def register_user(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User was created successfully.')
            
            return redirect('two_factor:login')
           
        else:
            messages.error(request, 'An error has occurred during registration.')
    context = {
        'form':form,
    }
    return render(request,'app/register.html',context)




def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = CustomUser.objects.get(username=username)
        except:
            messages.error(request, 'Username Does not exist')
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Successfully logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is incorrect.')
    return render(request,'app/login.html')

class CustomLoginView(LoginView):
    template_name = 'app/customlogin.html'


def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('login')





    
