# import factory
# from factory.faker import Faker; 
# import factory.fuzzy
from faker import Faker; 
from faker.factory import Factory
import factory.fuzzy

from .models import *

class PostFactory(factory.Factory):

    class Meta: 
        model = Post

    title = factory.Faker("name")
    description = factory.Faker("sentence")
    published = factory.fuzzy.FuzzyChoice(choices=[True, True, True, False])
    image = factory.Faker("image_url")