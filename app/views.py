from django.shortcuts import render

# Create your views here.
def statement(request):
    d = {'a':10000,'b':5000, 'c':3000}
    return render(request,'statement.html',context=d)

def loops(request):
    d = {'name':'satya'}
    return render(request,'loops.html',d)