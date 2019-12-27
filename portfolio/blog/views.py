from django.shortcuts import render,get_object_or_404
from .models import Blog
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy

# Create your views here.
# def allblogs(request):
#     blogs = Blog.objects
#     return render(request, 'blog/allblogs.html', {'blogs':blogs})

class PostListView(ListView):
    model = Blog
    template_name = 'blog/allblogs.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'blogs'




#
# def detail(request, blog_id):
#     detailBlog = get_object_or_404(Blog, pk = blog_id)
#     return render(request, 'blog/blog_detail.html', {'blog':detailBlog})

class PostDetailView(DetailView):
    model = Blog

class PostCreateView(CreateView):
    model = Blog
    fields = ['title', 'body','image']

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    success_url =reverse_lazy('allblogs')

class PostUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'body','image']
    template_name = 'blog/blog_update.html'
    success_url =reverse_lazy('allblogs')

class PostDeleteView(DeleteView):
    model = Blog
    # success_url = 'allblogs'
    success_url =reverse_lazy('allblogs')






