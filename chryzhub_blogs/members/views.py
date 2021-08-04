from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

from blog_app.models import UserProfile, Category, Post
from .forms import SignUpForm, EditAccountForm, PasswordChangingForm, ProfileUpdateForm

# Create your views here.
class EditProfilePageView(generic.UpdateView):
    model = UserProfile
    form_class= ProfileUpdateForm
    template_name = 'registration/edit_profile_page.html'

class ShowProfilePageView(DetailView):
    model = UserProfile
    template_name= 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        user = self.request.user
        user_posts = Post.objects.filter(author= user).order_by('-post_date')
        context['page_user'] = page_user
        context['user_posts'] = user_posts
        return context

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def  password_success(request):
    return render(request, 'registration/password_success.html', {})



class CreateAccount(generic.CreateView):
    form_class= SignUpForm
    template_name='registration/register.html'
    success_url= reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        all_category = Category.objects.all()
        context = super(CreateAccount, self).get_context_data(*args, **kwargs)
        context['all_category'] = all_category
        return context

class UpdateAccount(generic.UpdateView):
    model = UserProfile
    form_class= EditAccountForm
    template_name='registration/edit_profile.html'
    success_url= reverse_lazy('blog_list')

    def get_object(self):
        return self.request.user

class CreateProfilePageView(CreateView):
    model = UserProfile
    form_class= ProfileUpdateForm
    template_name = 'registration/create_user_profile_page.html'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
