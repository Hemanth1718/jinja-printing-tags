from django.shortcuts import render

# Create your views here.

def data_render(request):
    data='this data is our assumption'
    d={'assumption':data}
    return render(request,'data_render1.html',context=d)    
