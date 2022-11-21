from django.shortcuts import render
from django.http import HttpResponse
from .models import article

# Create your views here.
def news(request):
    news = article.objects.all()
    context = {
        'news': news,
    }
    return render(request, 'news.html', context)

def view_news_item(request, news_id):
    news = article.objects.get(pk=news_id)
    return render(request, 'view_news_item.html', {'news_item': news})