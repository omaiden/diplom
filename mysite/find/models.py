from django.db import models
import os
import datetime
from django.contrib.auth.models import User

def get_image_missings_path(instance, filename):
    return os.path.join('images/missings', str(instance.id), filename)

def get_image_victims_path(instance, filename):
    return os.path.join('images/victims', str(instance.id), filename)



# class Customer(models.Model):
#     fullname = models.CharField(max_length=50)
#     telephone = models.CharField(max_length=12)
#     email = models.EmailField()
#     username = models.CharField(max_length=30)
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.fullname


class Post_type(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name

    class Admin: pass


class Relative(models.Model):
    fullname = models.CharField(max_length=50)
    adress = models.CharField(max_length=100, null=True)
    telephone = models.CharField(max_length=12)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.relation

    class Admin: pass


class Missing_person(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=20, null=True)
    birthday = models.DateField()
    missing_place = models.CharField(max_length=100)
    missing_time = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return fullname

    class Admin: pass


class Image(models.Model):
    person_id = models.ForeignKey(Missing_person, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_missings_path, default = 'images/non.png')


class Victim(models.Model):
    date = models.DateField()
    place = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_image_victims_path, default = 'images/non.png')
    additional_information = models.CharField(max_length=50, null=True)

    class Admin: pass

    
class Post(models.Model):
    text = models.TextField()
    time = models.DateTimeField(default = datetime.datetime.now())
    found = models.BooleanField(default=False)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE, default='000')
    post_type_id = models.ForeignKey(Post_type, on_delete=models.CASCADE, default='000')
    relative_id = models.ForeignKey(Relative, on_delete=models.CASCADE, default='000')
    missing_person_id = models.ForeignKey(Missing_person, on_delete=models.CASCADE, default='000')
    victim_id = models.ForeignKey(Victim, on_delete=models.CASCADE, default='000')

    def __str__(self):
        return self.text

    class Admin: pass


# class Adress(models.Model):
#     name = models.CharField(max_length=50)
#     country = models.CharField(max_length=20)
#     city = models.CharField(max_length=20)
#     street = models.CharField(max_length=20)
#     home = models.CharField(max_length=20)

#     def __str__(self):
#         return name

#     class Admin: pass





    
