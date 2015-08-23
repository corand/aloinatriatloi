from django.shortcuts import render
from django.views.generic import DetailView,ListView
from bloga.models import Post



class PostList(ListView):
    template_name = "blog.html"
    context_object_name = 'posts'
    paginate_by = 5
    def get_queryset(self):
        return Post.objects.all().order_by('-data')

class PostView(DetailView):
    slug_field = 'slug'
    model = Post
    context_object_name = "post"
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['postak'] = Post.objects.all().order_by('data')[:3]
        return context