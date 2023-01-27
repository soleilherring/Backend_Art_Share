from django.db import models
# from cloudinary.models import CloudinaryField
# from cloudinary.uploader import upload

# uploaded_image = upload(file_path)
# item = Item.objects.create(name=name, description=description, image=uploaded_image, condition=condition, owner=owner)
# from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    password = models.CharField(max_length=200, default='Unknown')
    # image = models.ImageField()
    # registrationDate = models.DateField("Registration Date", auto_now_add=True)

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
    # name = models.CharField(max_length=200)
    # description = models.TextField()
    # item  = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField("Name", max_length=50)
    description = models.TextField("Description", null=True,blank=True)
    image = models.FileField(upload_to='media/')
    # image = models.ImageField('image', null=True, blank=True)

    # image = CloudinaryField('image')
    condition = models.CharField(max_length=50, default='Unknown') 
    # category = models.CharField(max_length=50, default='Uncategorized')    
    category = models.ManyToManyField(Category, related_name="items")
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