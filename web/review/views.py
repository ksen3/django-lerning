from django.shortcuts import render, redirect
from .models import review
from .forms import reviewForm

def post_review(request):
    error=''
    if request.method == 'POST':
        form = reviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'


    form = reviewForm()
    return render(request, 'post_review.html', {'form': form, 'error': error})

def read_review(request):
    reviews = review.objects.all()
    return render(request, 'read_review.html', {'reviews': reviews})
