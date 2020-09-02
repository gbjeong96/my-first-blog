from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html',{})

#post_list 함수는 request(요청)을 받아서 render함수를 호출한다. render함수는 blog/post_list.html 템플릿을 보여준다.