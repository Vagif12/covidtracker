from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import requests,urllib


def index(request):
    return render(request,'search_results.html',{})

@require_http_methods(['GET'])
def search(request):
    q = request.GET.get('q')
    area = request.GET.get('area')
    v = request.GET.get('king')
    latl = request.GET.get('latlng1')
    latl2 = request.GET.get('latlng2')
    iphone = request.GET.get('iphone')
    ask = request.GET.get('ask')
    a = ''
    b = ''
    z1 = ''
    z2 = ''
    print(iphone)
    z1 = ''
    if q and area:
        if v == '':
            a = ''
            b = ''
        else:
            v = v + ' ireland'
            x = urllib.parse.quote_plus(v)
            res = requests.get('https://eu1.locationiq.com/v1/search.php?key=63a7a1cc5a7398&q={}&format=json'.format(x))
            try:
                a = res.json()[0]['lat']
                b = res.json()[0]['lon']
            except:
                a = ''
                b = ''

    if iphone == '':
        pass
    else:
        z = iphone + ' ireland'
        zz = urllib.parse.quote_plus(z)
        res1 = requests.get('https://eu1.locationiq.com/v1/search.php?key=63a7a1cc5a7398&q={}&format=json'.format(zz))
        try:
            z1 = res1.json()[0]['lat']
            z2 = res1.json()[0]['lon']
        except:
            z1 = ''
            z2 = ''
            print(z1)
        q = z1
        area = z2
        latl = z1
        latl2 = z2
    return render(request, 'search_results.html', {'z1':z1,'z2':z2,'iphone':iphone,'q':q, 'area':area,'a':a,'b':b,'latl':latl,'latl2':latl2})

# from django.shortcuts import render,redirect
# from django.views.decorators.http import require_http_methods
# from django.contrib import messages
# import requests,urllib


# def index(request):
#     return render(request,'search_results.html',{})

# @require_http_methods(['GET'])
# def search(request):
#     q = request.GET.get('q')
#     area = request.GET.get('area')
#     v = request.GET.get('king')
#     latl = request.GET.get('latlng1')
#     latl2 = request.GET.get('latlng2')
#     iphone = request.GET.get('iphone')
#     z1 = ''
#     z2 = ''
#     print(iphone)
#     z1 = ''
#     if q and area:
#         if v == '':
#             a = ''
#             b = ''
#         else:
#             v = v + ' ireland'
#             x = urllib.parse.quote_plus(v)
#             res = requests.get('https://eu1.locationiq.com/v1/search.php?key=63a7a1cc5a7398&q={}&format=json'.format(x))
#             try:
#                 a = res.json()[0]['lat']
#                 b = res.json()[0]['lon']
#             except:
#                 a = ''
#                 b = ''

#     if iphone == '':
#         pass
#     else:
#         z = iphone + ' ireland'
#         zz = urllib.parse.quote_plus(z)
#         res1 = requests.get('https://eu1.locationiq.com/v1/search.php?key=63a7a1cc5a7398&q={}&format=json'.format(zz))
#         try:
#             z1 = res1.json()[0]['lat']
#             z2 = res1.json()[0]['lon']
#         except:
#             z1 = ''
#             z2 = ''
#             print(z1)
#         q = z1
#         area = z2
#         latl = z1
#         latl2 = z2
#     return render(request, 'search_results.html', {'z1':z1,'z2':z2,'iphone':iphone,'q':q, 'area':area,'a':a,'b':b,'latl':latl,'latl2':latl2})
