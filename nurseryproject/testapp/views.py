from django.shortcuts import render
import datetime

# Create your views here.
def visit(request):
    date=datetime.datetime.now()
    name='sunny'
    my_dict={'date':date,'guest':name,'time':date}
    return render(request,'testapp/wish.html',context=my_dict)
