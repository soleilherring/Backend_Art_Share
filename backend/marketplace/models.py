from django.db import models


class User(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    password = models.CharField(max_length=200, default='Unknown')

    def __str__(self):
        return self.name

class Category(models.Model):
    CATEGORY_CHOICES = (
        ('Painting', 'Painting'),
        ('Ceramics', 'Ceramics'),
        ('Yarn and Needlework', 'Yarn and Needlework'),
        ('Illustration and Drawing', 'Illustration and Drawing'),
        ('Sculpture', 'Sculpture'),
        ('Printmaking', 'Printmaking'),
        ('Photography', 'Photography'),
        ('Calligraphy', 'Calligraphy'),
        ('Textiles', 'Textiles'),
    )
    name = models.CharField(max_length=200, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField("Name", max_length=50)
    description = models.TextField("Description", null=True,blank=True)
    image = models.ImageField(upload_to='images/')
    condition = models.CharField(max_length=50, default='Unknown') 
    category = models.ManyToManyField(Category, related_name="items")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # postId = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="items",blank=True, null=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField("Title", max_length=50, null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name="posts", blank=True)
    # itemId = models.ForeignKey(Item, on_delete=models.CASCADE,null=True,blank=True)
    location = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    reserved = models.BooleanField(default=False) 

    class Meta:
        ordering = ['reserved']

class Review(models.Model):
    reviewer = models.ForeignKey(User, related_name='reviewer', on_delete=models.CASCADE,  null=True,blank=True)
    reviewed_user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True,blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)