from django.shortcuts import render,get_object_or_404
from .models import post, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.

# def post_list(request):
#     posts =post.objects.all()
#     return render(request,'book/list.html',{"posts":posts})



# def post_detail(request,year,month):
#     post = get_object_or_404(post,slug = post,publish_year = publish)  
#     return render (request ,'book/detail.html',{'post:post'})


####### For Train ######

def LikeView(request, pk):
    _post = get_object_or_404(post, id=request.POST.get('post_id'))
    liked = False
    if _post.likes.filter(id=request.user.id).exists():
        _post.likes.remove(request.user)
        liked = False
    else:
        _post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-ditail', args=[str(pk)]))


class HomeView(ListView):
    model = post
    template_name = 'list.html'
    ordering = ['-upadated']

    

def CategoryListView(request):
    cat_menu_list = post.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})



def CategoryView(request, cats):
    category_posts = post.objects.filter(category = cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model = post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all();
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context



class AddPostView(CreateView):
    model = post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'body')


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    # fields = ('title', 'body')


class UpdatePostView(UpdateView):
    model = post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('list')