from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from elasticapp.documents import PostDocument, BanksDocument


def search(request):
    bankname = request.GET.get('q')
    if bankname:
        posts = BanksDocument.search().query("match", name=bankname)
    else:
        posts = ''
    return render(request, 'search/search.html', {'posts': posts})

