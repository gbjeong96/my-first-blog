from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date') #posts는 querry set의 이름이다.
    return render(request, 'blog/post_list.html',{'posts': posts}) #request는 사용자가 요청한 모든것을 의미한다.

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk) #post_detail은 우리가 이동해야할 view이다.
    else:
        form = PostForm() #Post 폼을 추가하기 위해 PostForm() 함수를 호출하도록 하여 탬플릿에 넘깁니다.
    return render(request, 'blog/post_edit.html', {'form':form}) #html template를 호출하고 받아온 정보는 request가 가지고 있다.

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

#post_list 함수는 request(요청)을 받아서 render함수를 호출한다. render함수는 blog/post_list.html 템플릿을 보여준다.