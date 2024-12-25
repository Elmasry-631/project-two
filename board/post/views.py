from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def homepage(request):
    home = Board.objects.all()
    return render(request,'home.html',{'home':home})
def boards(request, post_id):
    board_list = get_object_or_404(Board,pk=post_id)
    return render(request,'boards.html',{'board_list':board_list, 'post_id':post_id})
def posts(request,post_id):
    post_list = get_object_or_404(Post, pk=post_id)
    return render(request,'boards.html',{'post_list':post_list, 'post_id':post_id})
def new_post(request, post_id):
    post_new = get_object_or_404(Board, pk=post_id)if post_id else None
    
    return render(request,'newboards.html',{'post_new':post_new,'post_id':post_id})


