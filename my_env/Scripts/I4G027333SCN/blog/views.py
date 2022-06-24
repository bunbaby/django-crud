from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from models import Post
class PostListView():
    model = Post

class  PostCreateView():
    model = Post

    fields =  "__all_"

    success_url = reverse_lazy("blog: all")

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post

    fields = "__all__"

    success_url = reverse_lazy("blog: all")

class PostDeleteView(PostUpdateView):
    model = Post

    fields = "__all__"

    success_url = reverse_lazy("blog: all")




    # Create your views here.
