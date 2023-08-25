from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def index(requset):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(requset, 'index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    # if, else 둘다 사용하는 context
    context = {
        'form': form,
    }
    return render(request, 'form.html', context) # 'form.html': 'create.html'

def detail(request, id):
    article = Article.objects.get(id=id)
    comment_form = CommentForm()

    # comment 목록
    # 첫 번째 방법
    # comment_list = Comment.objects.filter(article=article)

    # 두 번째 방법
    # comment_list = article.comment_set.all()

    # 세 번째 방법
    # detail.html 코드에서 article.comment_set.all

    context = {
        'article': article,
        'comment_form': comment_form,
        # 'comment_list': comment_list,  ###
    }
    return render(request, 'detail.html', context)

def comment_create(request, article_id):
    comment_form = CommentForm(request.POST) # 사용자가 입력한 정보를 form에 입력
    if comment_form.is_valid():             # 유효성 검사
        comment = comment_form.save(commit=False) # 추가 데이터를 넣기 위해, 아직 저장하지 않음

        # # 첫 번째 방법 (객체 오브젝트)
        # article = Article.objects.get(id=article_id) # article_id를 기준으로 objects를 가져옴
        # comment.article = article                   # article 컬럼에 추가

        # 두 번째 방법 (id를 직접 입력)
        comment.article_id = article_id

        comment.save()                      # 저장
    
        return redirect('articles:detail', id=article_id)

def comment_delete(request, article_id, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('articles:detail', id=article_id)

