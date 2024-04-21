from django.db import models

# Create your models here.


class Banner(models.Model):
    banner_images = models.ImageField(upload_to='banner_img/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    blog_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    blog_images = models.ImageField(upload_to='blog_images/')    
    title = models.CharField(max_length=255)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    
    
class Newsletter(models.Model):
    email = models.CharField(max_length=255)
    is_submit =  models.BooleanField(default=False) 


class BlogNewsletter(models.Model):
    news_images = models.ImageField(upload_to="newsletter_img/", null=True, blank=True)  
    description = models.TextField(null=True, blank=True) 
    

class RecipePost(models.Model):
    
    labels = (
        ("BEGGINERS", "BEGGINERS"),
        ("INTERMEDIATE", "INTERMEDIATE"),
        ("EXPERT", "EXPERT"),
    )
    
    title = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    preparation_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    yield_items = models.PositiveIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    recipe_label = models.CharField(choices=labels, default='BEGGINERS', max_length=30)
    recipe_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_best_recipe = models.BooleanField(default=False) 


class RecipeImage(models.Model):
    recipe_post = models.ForeignKey(RecipePost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='recipe_img/')


class RecipeContentSection(models.Model):
    post = models.ForeignKey(RecipePost, on_delete=models.CASCADE,related_name='recipe_description')
    content = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
    

class Ingredient(models.Model):
    post = models.ForeignKey(RecipePost, on_delete=models.CASCADE,null=True ,blank=True, related_name='recipe_ingredient')
    name = models.CharField(max_length=100, null=True ,blank=True)

    class Meta:
        ordering = ['name']


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    
    