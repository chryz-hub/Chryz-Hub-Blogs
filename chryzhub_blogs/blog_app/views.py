from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.http import HttpResponseRedirect

from .models import Post, Category, Comment
from .forms import PostForm, CategoryForm, SignUpForm, CommentForm, EditPostForm

class LoginToBlog(generic.CreateView):
    form_class= SignUpForm
    template_name='registration/register.html'
    success_url= reverse_lazy('create_blog')

    def get_context_data(self, *args, **kwargs):
        all_category = Category.objects.all()
        context = super(LoginToBlog, self).get_context_data(*args, **kwargs)
        context['all_category'] = all_category
        return context

def LikeView(request, pk):
    post =get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))

class BlogList(ListView):
    model = Post
    template_name= 'blog_list.html'
    ordering=['-post_date']

    def get_context_data(self, *args, **kwargs):
        all_category = Category.objects.all()
        context = super(BlogList, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post)
        total_likes = stuff.total_likes()

        context['all_category'] = all_category
        context['total_likes'] = total_likes
        return context


class  BlogDetail(DetailView):
    model = Post
    template_name='blog_detail.html'

    def get_context_data(self, *args, **kwargs):
        all_category = Category.objects.all()
        context = super(BlogDetail, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['all_category'] = all_category
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class AddComment(LoginRequiredMixin, CreateView):
    model = Comment
    form_class= CommentForm
    template_name= 'add_comment.html'
    success_url= reverse_lazy('blog_list')


    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Post
    form_class= PostForm
    template_name= 'create_blog.html'
    success_url= reverse_lazy('blog_list')
    #fields=['title', 'author', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        all_category = Category.objects.all()
        context = super(CreateBlog, self).get_context_data(*args, **kwargs)
        context['all_category'] = all_category
        return context


class EditBlog(LoginRequiredMixin, UpdateView):
    model = Post
    template_name= 'edit_blog.html'
    form_class= EditPostForm
    #success_url = reverse_lazy('blog_detail', Post.pk)
    #fields=['title', 'body']

    def get_context_data(self, *args, **kwargs):
        all_category = Category.objects.all()
        context = super(EditBlog, self).get_context_data(*args, **kwargs)
        context['all_category'] = all_category
        return context


class DeleteBlog(LoginRequiredMixin, DeleteView):
    model= Post
    template_name='delete_blog.html'
    success_url = reverse_lazy('blog_list')

    def get_context_data(self, *args, **kwargs):
        all_category = Category.objects.all()
        context = super(DeleteBlog, self).get_context_data(*args, **kwargs)
        context['all_category'] = all_category
        return context

class AddCategory(LoginRequiredMixin, CreateView):
    model = Category
    form_class= CategoryForm
    template_name= 'add_category.html'
    #fields= ('category')
    success_url= reverse_lazy('category_list')

    def get_context_data(self, *args, **kwargs):
        all_category = Category.objects.all()
        context = super(AddCategory, self).get_context_data(*args, **kwargs)
        context['all_category'] = all_category
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def CategoryView(request, category):
    blog_category = Post.objects.filter(category=category.replace('-', ' '))
    return render(request, 'categories.html', {'category':category.title().replace('-', ' '), 'blog_category':blog_category})

    def get_context_data(self, *args, **kwargs):
        all_category = Category.objects.all()
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        context['all_category'] = all_category
        return context


class CategoryList(ListView):
    model= Category
    template_name='category_list.html'

    def get_context_data(self, *args, **kwargs):
        all_category = Category.objects.all()
        context = super(CategoryList, self).get_context_data(*args, **kwargs)
        context['all_category'] = all_category
        return context
