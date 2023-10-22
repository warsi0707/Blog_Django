from django.shortcuts import render,redirect, HttpResponse, HttpResponseRedirect
from blog_app .models import Post, contactUs, Comment
from .forms import contactForm
# from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth import authenticate, login as auth_login
# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {'posts':posts})

def comment(request):
    comments = Comment.objects.all()
    return render(request, 'home.html', {'comments':comments})

# def add_comment(request):
#     if request.method == 'POST':
#         n = request.POST['name']
#         c = request.POST['comment']

#         comm = Comment(
#             name = n,
#             text = c
#         )
#         comm.save()
#         return HttpResponseRedirect('home_page')

def detail(request, id):
    context ={}
    context['data'] = Post.objects.get(id = id)
    return render(request, 'detail.html', context)


def addtemp(request):
    return render(request, "create.html")

def create(request):
    if request.method == 'POST':
        t = request.POST['title']
        c = request.POST['caption']
        co = request.POST['content']
        img = request.POST['image']

        data = Post(
            title = t,
            caption = c,
            content = co,
        )
        data.save()
        return redirect('home_page')





def delete(request, id):
    posts = Post.objects.get(id=id)
    posts.delete()
    return redirect('home_page')



def contact_us(request):
    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "success.html")
    
    form = contactForm()
    context = {'form':form}

    return render(request, 'contact_us.html')



def privacy(request):
    return render(request, 'privacy.html')

def follow(request):
    return render(request,'follow.html')


# def signup(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']

#         myuser = User.objects.create_user(username, email, pass1)
#         myuser.first_name = fname
#         myuser.last_name = lname
#         myuser.save()

#         messages.success(request, "Your account has been created please login ")
#         return redirect('login')
#     return render(request, "signup.html")


# def login(request):
#     if request.method =='POST':
#         user = authenticate(
#             username = request.POST['username'],
#             pass1 = request.POST['pass1']
#         )
#         if user is not None:
#             login(request, user)
#             return render(request, 'home_page')

#         else:
#             messages.error(request, "Bad Credentials!")
#             return redirect('login')
#     return render(request, 'login.html')


