from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
import requests,urllib

def index(request):
    return render(request,'search_results.html',{})

@require_http_methods(['GET'])
def search(request):
    q = request.GET.get('q')
    area = request.GET.get('area')
    v = request.GET.get('king')
    print(q)
    if not q and not area:
        messages.set_level(request, messages.ERROR)
        messages.error(request,'Please fill in at least one box!')
        return redirect(request.META.get('HTTP_REFERER', request.path_info))
    if q and area:
        v = v + ' ireland'
        x = urllib.parse.quote_plus(v)
        res = requests.get('https://eu1.locationiq.com/v1/search.php?key=63a7a1cc5a7398&q={}&format=json'.format(x))
        try:
            a = res.json()[0]['lat']
            b = res.json()[0]['lon']
        except:
            a = ''
            b = ''
    return render(request, 'search_results.html', {'q':q, 'area':area,'a':a,'b':b})
