from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date') #posts는 querry set의 이름이다.
    return render(request, 'blog/post_list.html',{'posts': posts}) #request는 사용자가 요청한 모든것을 의미한다.

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    

#post_list 함수는 request(요청)을 받아서 render함수를 호출한다. render함수는 blog/post_list.html 템플릿을 보여준다.