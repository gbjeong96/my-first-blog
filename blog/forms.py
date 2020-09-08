from django import forms

from .models import Post

class PostForm(forms.ModelForm): #우리가 만들 form의 이름은 PostFrom이고 그 form이 Modelfrom이라는것을 파라미터로 알려준다.

    class Meta: 
        model = Post #Form을 만들기 위해 우리가 어던 model이 쓰여야 하는지 장고에게 알려준다. #Post는 model.py에서 만들어주었다.
        fields = ('title', 'text',) #form에 title과 text가 보여지게 해준다.