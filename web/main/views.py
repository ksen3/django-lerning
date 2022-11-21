from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    siteInfo = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sapien ipsum, imperdiet in est vel, vehicula malesuada diam. Integer tristique justo accumsan finibus consectetur. Ut eu dui lorem. Etiam porta dui sit amet quam mollis, ut pulvinar ipsum tincidunt. Nullam eget tempor ipsum. Maecenas aliquet, lorem faucibus luctus pharetra, ex metus accumsan justo, scelerisque aliquam lacus magna at mauris. Donec quis lacus placerat, laoreet lorem nec, condimentum sem. Ut suscipit in diam nec aliquam. Sed ornare velit eget risus scelerisque, a condimentum est varius. Nulla neque elit, mollis eget tellus sed, dictum ullamcorper mauris. Sed non lectus sit amet tellus varius tristique. Donec rutrum elit vel sem facilisis interdum. Maecenas laoreet iaculis massa quis volutpat. Pellentesque commodo ac erat at luctus. Donec sit amet turpis varius nulla tincidunt sodales.'

    info = {
        'siteTitle': 'Блог',
        'siteInfo': siteInfo,
    }
    return render(request, 'index.html', info)

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')
