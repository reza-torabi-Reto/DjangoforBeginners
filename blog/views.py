from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment
# Create your views here.

# class BlogListView(ListView):
#     model = Post
#     template_name = 'blog/home.html'
#     context_object_name = 'all_posts'

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class DetailPost(DetailView):
    model =Post
    template_name = 'blog/post.html'
    def get_object(self):
        pk = self.kwargs.get('pk')
        object = get_object_or_404(Post.objects.all(), id = pk)
        ip_address = self.request.user.ip_address
        if ip_address not in object.hits.all():
            object.hits.add(ip_address)
        return object


    # def post(self, request, *args, **kwargs):
    #     new_comment = Comment(comment= request.Post.get('comment'),
    #         post = request.Post.get('post'),
    #         author = self.request.user
    #     )
    










class CreatePost(LoginRequiredMixin ,CreateView):
    model = Post
    template_name = 'blog/create.html'
    fields = ['title',  'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post
    template_name = 'blog/update.html'
    fields = ['title', 'body',]
    # success_url = reverse_lazy('blog:home')
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class DeletePost(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url =reverse_lazy('blog:home')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


