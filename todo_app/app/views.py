from django.shortcuts import render,redirect
from django.views.generic import View
from .models import TaskModel
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm,TodoForm
from django.views.generic.edit import UpdateView


class HomePage(View):

    def get(self,request):

        task=TaskModel.objects.all()

        return render(request,'Home/index.html',{'task_list':task})



class AddTask(View):

    def get(self,request):

        form=TodoForm()

        return render(request,'Home/add.html',{'form':form})

    def post(self,request):
        form=TodoForm(data=request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            user.user=self.request.user
            user.save()

            return redirect('home')
        
        return render(request,'Home/add.html',{'form':form})



class updateTask(UpdateView):

    model=TaskModel
    fields=['name','description']
    template_name='Home/add.html'
    success_url='/'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = TaskModel.objects.get(id=self.kwargs['pk']).user
        user=self.request.user

        return context
    

@login_required
def DeletePage(request,pk):

    if request.method=='GET':
        obj=TaskModel.objects.get(id=pk)
        obj.delete()
        obj.save()


        return redirect('home')


@login_required
def DonePage(request,pk):

    if request.method=='GET':
        obj=TaskModel.objects.get(id=pk)
        
        if obj.is_done is True:
            obj.is_done=False
            obj.save()

            return redirect('home')
            

        obj.is_done=True
        obj.save()
        return redirect('home')

        

        


    
# Authenitcation 

class LoginPage(View):


    def get(self,request):

        form=AuthenticationForm()

        return render(request,'Account/login.html',{'form':form})


    def post(self,request):


        form=AuthenticationForm(data=request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']


            user=authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                print('user login successfully ')
                return redirect('home')                
            
        return render(request,'Account/login.html',{'form':form})


class Signuppage(View):

    def get(self,request):

        form=SignupForm()

        return render(request,'Account/register.html',{'form':form})

    
    def post(self,request):


        form=SignupForm(data=request.POST)

        if form.is_valid():
            login(request,form.save())
            
            return redirect('home')
        
        return render(request,'Account/register.html',{'form':form})



@login_required
def LogoutPage(request):

    logout(request)

    return redirect('home')
