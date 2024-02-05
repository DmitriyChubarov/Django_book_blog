from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'detail_post.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['body', 'title']
    template_name = 'edit_post.html'

class BlogDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'delete_post.html'

class BlogLogoutView(TemplateView):
    template_name = 'registration/logout.html'

