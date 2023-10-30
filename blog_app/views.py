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

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
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

def DeleteComment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'GET':
        comment.delete()
        return redirect('blog_detail', pk=comment.post_id)
    return render(request, 'delete_comment.html')


class BlogDetail(DetailView):
    model = Post
    template_name = 'blog_detail.html'

    def get_context_data(self, **kwargs):
       context = super(BlogDetail, self).get_context_data(**kwargs)

       stuff = get_object_or_404(Post, id=self.kwargs['pk'])
       total_likes = stuff.total_likes()

       liked = False 
       if stuff.likes.filter(id=self.request.user.id).exists():
           liked = True
       context['commentform'] = CommentForm()
       context['total_likes'] = total_likes
       context['liked'] = liked
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
    login_url = 'login'
    model = Post
    form_class= PostForm
    template_name= 'create_blog.html'
    success_url= reverse_lazy('blog_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditBlog(LoginRequiredMixin, UpdateView):
    model = Post
    template_name= 'edit_blog.html'
    form_class= EditPostForm


class DeleteBlog(LoginRequiredMixin, DeleteView):
    model= Post
    template_name='delete_blog.html'
    success_url = reverse_lazy('blog_list')




class AddCategory (CreateView):
    model = Category
    form_class= CategoryForm
    template_name= 'add_category.html'
    success_url= reverse_lazy('blog_list')


def CategoryView(request, category):
    blog_category = Post.objects.filter(category__name=category.replace('-', ' '))
    return render(request, 'categories.html', {'category':category.title().replace('-', ' '), 'blog_category':blog_category})




class CategoryList(ListView):
    model= Category
    template_name='category_list.html'


class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__icontains=query) | Q(category__name__icontains=query) | Q(snippet__icontains= query))
        return object_list
