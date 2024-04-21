from django.contrib import admin
from recipe.models import Banner, Category, BlogPost, Newsletter, BlogNewsletter, RecipePost, Ingredient, RecipeContentSection, RecipeImage ,Contact

class RecipeContentSectionInline(admin.TabularInline):
    model = RecipeContentSection
    extra = 1

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 2

@admin.register(RecipePost)
class RecipePostAdmin(admin.ModelAdmin):
    inlines = [RecipeContentSectionInline, IngredientInline, RecipeImageInline]

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogNewsletter)
class BlogNewsletterAdmin(admin.ModelAdmin):
    pass

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass

@admin.register(RecipeContentSection)
class RecipeContentSectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass