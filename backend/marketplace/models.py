from django.db import models
# from django.contrib.auth.models import User

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    username = models.CharField("Username", max_length=200, default='Unknown')
    email = models.EmailField()
    image = models.ImageField()
    # registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return self.user

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Item(models.Model):
    # CATEGORY = (('Painting'), ('Ceramics'), ('Knitting and Crocheting'), ('Illustration and Drawing'), ('Embroidery'), ('Sculpture'))
    name = models.CharField("Name", max_length=50)
    description = models.TextField("Description", null=True,blank=True)
    image = models.ImageField()
    condition = models.CharField(max_length=50, default='Unknown') 
    category = models.CharField(max_length=50, default='Uncategorized')    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    reserved = models.BooleanField(default=False) 

    class Meta:
        ordering = ['reserved']
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)