from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

# ModelForm: 해당 모델에 맞는 input태그들을 생성해줌
# Meta : 원 자료 외 정보 등을 기입하는 클래스

class CommentForm(forms.ModelForm):
    class Meta:
        model =Comment
        # fields: 추가할 필드 이름 목록 / exclude: 제외
        # fields = '__all__' # 모든 게시물
        # fields = ('content', ) # 게시물 선택 없음
        exclude = ('article', )