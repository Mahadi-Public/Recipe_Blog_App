from django.shortcuts import render,redirect
from recipe.models import Banner,BlogPost,Category,BlogNewsletter,RecipePost,RecipeContentSection,Ingredient,RecipeImage
from recipe.forms import NewsletterForm,ContactForm
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models.functions import TruncMonth

# Create your views here.

def HomePage(request):
    
    context = {
        'BANNERS' : Banner.objects.all().order_by('-create_at')[:3],
        'RECIPE_POSTS': RecipePost.objects.all(),
        'RATTING_RANGE' : range(0,5), # Create a range for the stars
        'BEST_RECIPE' : RecipePost.objects.filter(is_best_recipe=True)
    }
    
    return render(request, 'recipe/home.html',context)


def RecipePostDetails(request, id):
    
    queryset =  RecipePost.objects.get(id=id)
    rating = int(queryset.rating)
    
    context = {
        'RECIPE_DETAILS' : queryset,
        'RATTING_RANGE' : range(rating),
        'EMPTY_RATING_RANGE': range(5 - max(min(rating, 5), 0)) 
    }
    
    return render(request, 'recipe/receipe-post.html', context)


def RecipePostList(request):
    search_query = request.GET.get('recipe_category')
    category_id = request.GET.get('select_category')
    queryset = RecipePost.objects.all()
    
    if category_id and category_id != '1':  # Check if a category is selected
        queryset = queryset.filter(recipe_category__id=category_id) 
    if search_query:
        queryset = queryset.filter(title__icontains=search_query)    
    
    context = {
        'RECIPE_LIST' : queryset,
        'RATTING_RANGE' : range(0,5), # Create a range for the stars
        'RECIPE_CATEGORY' : Category.objects.all(),
    }    
    
    return render(request, 'recipe/all-recipe-list.html', context)


def BlogPostList(request):
    
    distinct_dates = BlogPost.objects.annotate(month=TruncMonth('create_at')).values('month').annotate(count=Count('id'))
    queryset = BlogPost.objects.all()
    category = request.GET.get('category')
    if category:
        queryset = queryset.filter(blog_category__name = category)
    paginator = Paginator(queryset, 3)  # Show 3 queryset per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
        
    context = {
        'BLOG_LIST' : page_obj,
        'BLOG_CATEGORY' : Category.objects.all(),
        'BLOG_NEWSLETTER' : BlogNewsletter.objects.all().order_by('-id'),
        'PAGE_OBJECT' : page_obj,
        'DISTINCT_DATES' : distinct_dates
    }    
    
    return render(request, 'recipe/blog-post.html', context)



def BlogPostDetail(request, id):
    
    context = {
        'BLOGDETAILS' : BlogPost.objects.get(id=id)
    }
    
    return render(request, 'recipe/blog-post-details.html',context)




def ContactPage(request):
    return render(request, 'recipe/contact.html')

def AboutUs(request):
    return render(request, 'recipe/about.html')