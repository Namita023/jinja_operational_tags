from django.shortcuts import render

# Create your views here.

d={'name':'Namita', 'age':21 ,'gender':'female'}

def age_group(request):
    return render(request,'age_group.html',context=d)