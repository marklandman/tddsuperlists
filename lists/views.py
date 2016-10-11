from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item,List

# Create your views here.
def home_page(request):
    #print("HOMEPAGE")
    return render(request,'home.html')
    #return render(request,'home.html')

def view_list(request,list_id):
    #print("VIEWLIST {}".format(list_id))

    list_ = List.objects.get(id=list_id)
    return render(request,'list.html', {'list':list_})

def new_list(request):
    #print("NEWLIST ")

    list_ = List.objects.create()
    #print("created list id %d" %(list_.id,))
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect('/lists/%d/' % (list_.id,))

def add_item(request,list_id ):
    #print("ADDITEM {}".format(list_id))
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect('/lists/%d/' % (list_.id,))
