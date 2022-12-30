from django.shortcuts import render

# Create your views here.
def filters(request):
    d={'data':'hi PythON HOw Are YoU','c':0}

    return render(request,'filters.html',d)


def userdefinedfilters(request):
    d={'data':'hi PythON HOw Are YoU'}
    return render(request,'userdefinedfilters.html',d)