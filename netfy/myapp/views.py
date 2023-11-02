from django.shortcuts import render ,HttpResponse , render , redirect ,get_object_or_404
from django.contrib.auth.models import User , auth 
from .models import Video , Comment , UserDetails , Catogory_movie , Catogory_anime , Catogory_new_release , Cart
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from django.contrib import messages
from django.db.models import Q




# Create your views here.
def demo(request):
    return render(request,'demo.html')

def home(request):
    return render(request,'index.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        data = User.objects.create_user(username=username,email=email,password=password1)
        data.save()
        return redirect('login')

    return render(request,'signpage.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request , "Logout Successful ! , Please complete the further procedure to enjoy our services .")
            return redirect('part1')
        
        else:
            messages.error(request , "Login Failed ! Please or a valid username and password . if you don't have an acccunt please go to the sign in page ")
            return redirect('login')
        

    return render(request,'loginpage.html')

def userlogout(request):
    logout(request)
    return render(request,'loginpage.html')

def part1(request):
    # if request.method == 'POST':
    userposts = UserDetails.objects.all()
    context = {'userposts':userposts}
    return render(request,'next/part1.html',context)

def part2(request):
    if request.method == 'POST':
        user_name = request.POST['myname']
        user_age = request.POST['myage']
        user_choice = request.POST['choice']
        user_image = request.POST['profileimmage']
        user = request.user
        if user_name:
            mydata = UserDetails.objects.create(user=user, user_name=user_name,user_age=user_age, user_choice= user_choice,user_image=user_image)
            mydata.save()
            return redirect('moviepage')
        
    return render(request,'next/part2.html')

def moviepage(request):
    allPosts = Video.objects.all()
    randompost = Video.objects.order_by('?').first()

    context = {'allPosts': allPosts , 'randompost':randompost}
    return render(request,'next/moviepage.html',context)

def fmovie(request):
    return render(request,'playmovie/playmovie.html')

# def allmovie(request,post_slug):
#     post = get_object_or_404(Video , slug=post_slug)
#     # context = {'post': post}
#     comments = Comment.objects.filter(video=post).order_by('-created_at')
    
#     context = {'post': post, 'comments': comments}
    
#     return render(request,'playmovie/allmovie.html',context)


def moviedetails(request , post_slug):

    # allPosts = Video.objects.all()
    # contextes = {'allPosts': allPosts}

    post = get_object_or_404(Video , slug=post_slug)

    mychoice = post.category
    myreferances = Video.objects.filter(category=mychoice)
    # print(mychoice)
    context = {'post': post, 'myreferances':myreferances }

    return render(request,'next/moviedetails.html',context )


def allmovie(request, post_slug):
    post = get_object_or_404(Video, slug=post_slug)
    comments = Comment.objects.filter(video=post).order_by('-created_at')

    if request.method == 'POST':
        content = request.POST.get('content')
        user = request.user  # Assuming you have user authentication

        if content:
            Comment.objects.create(video=post, user=user, content=content)

        return redirect('allmovie', post_slug=post_slug)

    context = {'post': post, 'comments': comments}
    return render(request, 'playmovie/allmovie.html', context)

def moviepageshow(request):
    allPosts = Catogory_movie.objects.all()
    allAnime = Catogory_anime.objects.all()
    allNewRelease =  Catogory_new_release.objects.all()
    context = {'allPosts': allPosts , 'allAnime':allAnime , 'allNewRelease':allNewRelease }

    return render(request, 'movielist/movieshowpage.html', context)

# def searchpage(request,query=None):
#     results = Video.objects.filter(title__icontains=query)
#     return render(request, 'searchpage.html',{'results': results, 'query': query})

def searchpage(request):
    query = request.GET.get('q')  # Get the search query from the request
    results = Video.objects.filter(title__icontains=query) if query else None
    return render(request, 'searchpage.html', {'results': results, 'query': query})


def addtomylist(request):
    user = request.user
    video_id = request.GET.get('post_id')
    video = Video.objects.get(id=video_id)
    Cart(user=user ,movie=video).save()
    return redirect('/mylist')

def mylist(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    return render(request, 'movielist/mylist.html',{'carts':cart})
    
def remove_mylist(request):
    if request.method == 'GET':
        prod_id = request.GET.get('post_id')
        try:
            cart_item = Cart.objects.get(user=request.user, movie_id=prod_id)
            cart_item.delete()
            return redirect('/mylist')
        except Cart.DoesNotExist:
            return JsonResponse({'message': 'Item not found in your cart'}, status=404)


# Building the aisearch section

# def aisearch(request):
#     user_input = request.POST.get('user_input', '')

#     # Print the user's input to the terminal
#     print("User input:", user_input)

#     if user_input:
#         # Split the user's input into keywords
#         keywords = user_input.split()

#         # Query the database to find movies with descriptions that match the user's input
#         suggested_movies = Video.objects.filter(desc__icontains=keywords[0])

#         for keyword in keywords[1:]:
#             suggested_movies = suggested_movies.filter(desc__icontains=keyword)

#         # Sort suggested_movies by relevance (you may need to define a relevance metric)
#         # For simplicity, this example sorts by the number of matched keywords
#         suggested_movies = sorted(suggested_movies, key=lambda video: sum(keyword in video.desc for keyword in keywords), reverse=True)

#     else:
#         suggested_movies = []

#     return render(request, 'aisearch/aisearch.html', {'suggested_movies': suggested_movies, 'user_input': user_input})
#     # return render(request, 'aisearch/aisearch.html')
    

def aisearch(request):
    user_input = request.POST.get('user_input', '')

    if user_input:
        # Split the user's input into keywords
        keywords = user_input.split()

        # Initialize variables to keep track of the best-matching movie
        best_matching_movie = None
        best_matching_score = 0

        # Loop through all movies and calculate relevance scores
        for movie in Video.objects.all():
            relevance_score = 0
            for keyword in keywords:
                if keyword in movie.desc:
                    relevance_score += 1

            # Update the best-matching movie if the current movie has a higher score
            if relevance_score > best_matching_score:
                best_matching_movie = movie
                best_matching_score = relevance_score

        suggested_movies = [best_matching_movie] if best_matching_movie else []
        

    else:
        suggested_movies = []
        print(suggested_movies)

    return render(request, 'aisearch/aisearch.html', {'suggested_movies': suggested_movies, 'user_input': user_input})

