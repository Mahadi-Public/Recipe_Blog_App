from django.urls import path
from recipe.views import HomePage,RecipePostDetails,ContactPage,AboutUs,BlogPostList,BlogPostDetail,RecipePostList

urlpatterns = [
    path('', HomePage, name="HomePage"),
    path('recipe-post-list/', RecipePostList, name="RecipePostList"),
    path('recipe-post/<int:id>/', RecipePostDetails, name="RecipePost"),
    path('contact/', ContactPage, name="ContactPage"),
    path('about/', AboutUs, name="AboutUs"),
    path('blog-post/', BlogPostList, name="BlogPost"),
    path('blog-list-detail/<int:id>/', BlogPostDetail, name="BlogPostDetails")
]
