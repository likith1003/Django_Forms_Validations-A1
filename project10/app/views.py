from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     ESFO = SkoolForm()
#     d = {'ESFO': ESFO}
#     if request.method == 'POST':
#         sname = request.POST.get('sname')
#         princy = request.POST.get('princy')
#         pno = request.POST.get('pno')
#         add = request.POST.get('add')
#         SO = Skool(sname=sname, princy=princy, pno=pno, add=add)
#         SO.save()
#         return HttpResponse('Done.....')
#     return render(request, 'home.html', d)



def home(request):
    ESFO = SkoolForm()
    d = {'ESFO': ESFO}
    if request.method == 'POST':
        SFO = SkoolForm(request.POST)
        if SFO.is_valid():
            sname = SFO.cleaned_data.get('sname')
            princy = SFO.cleaned_data.get('princy')
            pno = SFO.cleaned_data.get('pno')
            add = SFO.cleaned_data.get('add')
            SO = Skool(sname=sname, pno=pno, add=add, princy=princy)
            SO.save()
            return HttpResponse('Done......')
        return HttpResponse('Invalid Data')
    return render(request, 'home.html', d)