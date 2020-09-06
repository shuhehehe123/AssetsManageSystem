from django.shortcuts import render,get_object_or_404,redirect

from .models import Asset
# Create your views here.
def index(request):
    #下面这一段是选填的，但是可能会危
    '''
     if request.session.get('is_login', None):
        # 不允许重复登录
        return redirect('/')
        #ddd
    #dd
    '''
    asset_list=Asset.objects.all().order_by('-asset_buyin_time')
    
    return render(request,'asset/index.html',context={'asset_list':asset_list})
def article(request,pk):
    asset = get_object_or_404(Asset,pk=pk)
    return render(request, 'asset/article.html', context={'asset': asset})
