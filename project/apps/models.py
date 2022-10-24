from email.policy import default
from hashlib import blake2b
from pyexpat import model
from random import choices
from tabnanny import verbose
from urllib import request
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=120)
    email = models.EmailField(max_length=120, unique=True)
    password = models.CharField(max_length=120)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Ulanyjy'
        verbose_name_plural = 'Ulanyjylar'
    
    def __str__(self):
        return self.email


class Category(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="category", null=True, blank=True)
    total_questions = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Kategoriýalar'
        verbose_name_plural = 'Kategoriýalar'

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="sub_category")
    cat_id = models.ForeignKey(Category, related_name='category_id', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Bölümler'
        verbose_name_plural = 'Bölümler'

    def __str__(self):
        return self.title

class Questions(models.Model):
    OPTIONS = (
        ('answer1', 'answer1'),
        ('answer2', 'answer2'),
        ('answer3', 'answer3'),
        ('answer4', 'answer4'),
    )
    title = models.TextField(null=True, blank=True)
    answer1 = models.CharField(max_length=150)
    answer2 = models.CharField(max_length=150)
    answer3 = models.CharField(max_length=150)
    answer4 = models.CharField(max_length=150)
    correct_answer = models.CharField(max_length=255,  default='answer1')
    sub_question = models.ForeignKey(SubCategory, related_name='sub_question', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Soraglar'
        verbose_name_plural = 'Soraglar'

    def __str__(self):
        return self.title



class CategoryUser(models.Model):
    user_id = models.ForeignKey(User, related_name='cat_user', on_delete=models.CASCADE)
    sub_category_id = models.ForeignKey(SubCategory, related_name='user_cat', on_delete=models.CASCADE, blank=True, null=True)
    dogry_jogap = models.CharField(max_length=100)
    yalnysh_jogap = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Dogry jogaplar'
        verbose_name_plural = 'Dogry jogaplar'

    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    mobile_number = models.CharField(max_length=10)
    email = models.CharField(max_length=25)
    state_region = models.CharField(max_length=35)
    avatar = models.ImageField(upload_to="avatars")

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    def __str__(self):
        return self.name




    
