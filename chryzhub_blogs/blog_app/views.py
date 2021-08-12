from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.http import HttpResponseRedirect
from django.db.models import Q 
from django.contrib.auth.models import User


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

# def LikeView(request, pk):
#     post =get_object_or_404(Post, id=request.POST.get('post_id'))
#     liked = False
#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user)
#         liked = False
#     else:
#         post.likes.add(request.user)
#         liked = True
#     return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))

class BlogList(ListView):
    model = Post
    template_name= 'blog_list.html'
    ordering=['-post_date']

    def get_context_data(self, *args, **kwargs):
        all_category = Category.objects.all()
        context = super(BlogList, self).get_context_data(*args, **kwargs)
        context['all_category'] = all_category

        return context

def DeleteComment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'GET':
        comment.delete()
        return redirect('blog_detail', pk=comment.post_id)
    return render(request, 'delete_comment.html')


class BlogDetail(DetailView):
    model = Post
    template_name = 'blog_detail.html'

    def like(request):
        post = get_object_or_404(Post, pk=pk)
        is_liked = False
        if post.likes.filter(id=request.user.id).exists():
            is_liked = True
        else:
            is_liked = False
        context[' is_liked'] =  is_liked
        return render(request, 'blog_detail.html', context)


    def get_context_data(self, **kwargs):
       context = super(BlogDetail, self).get_context_data(**kwargs)
       context['commentform'] = CommentForm()
       return context

    def post(self, request, pk):
       post = get_object_or_404(Post, pk=pk)
       form = CommentForm(request.POST)
     
       if form.is_valid():
           obj  = form.save(commit=False)
           obj.post = post
           obj.name = self.request.user
           obj.save()
           return redirect('blog_detail', post.pk)


def EditComment(request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        form = CommentForm(instance=comment)
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('blog_detail', pk=comment.post_id)
        context = {'form':form}
        return render(request, 'edit_comment.html', context)


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Post
    form_class= PostForm
    template_name= 'create_blog.html'
    success_url= reverse_lazy('blog_list')
    #fields=['title', 'author', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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

class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__icontains=query) | Q(category__icontains=query) | Q(snippet__icontains= query))
        return object_list