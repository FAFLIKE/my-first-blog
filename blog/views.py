from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
import vk_api

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    vk = vk_api.VkApi(token="80f8b7bc46d3e6eda2bcb6e7cf302d8028bdc0a68ef8b07639c6a7a42b57ec344693e7ac1981e801e1c13") # авторизация через токен (желательно)
    user = vk.method("users.get", {"user_ids": 475532308, "fields": 'status'})
    get_status = user[0]['status']
    return render(request, 'blog/post_list.html', {'posts': posts, 'status': get_status})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})