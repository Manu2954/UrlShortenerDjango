from multiprocessing import context
from django.shortcuts import render,redirect,HttpResponse
import uuid
from .models import Linkk
# Create your views here.

def index(request):
    if request.method == 'POST':
        urlInp=request.POST['linkInp']
        uid=str(uuid.uuid4())[:5]
        if urlInp[:5]=='https':
            urlInp=urlInp[8:]
        new_url = Linkk(linkkk=urlInp,uuid=uid)
        new_url.save()    
        context={
            "urlD":new_url,
        }
        return render(request,'index.html',context)

    return render(request,'index.html')

def go(request,pk):
    urlDet = Linkk.objects.get(uuid=pk)
    return redirect('https://'+urlDet.linkkk)