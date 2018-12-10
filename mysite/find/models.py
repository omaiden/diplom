from django.db import models
import os

def get_image_missings_path(instance, filename):
    return os.path.join('images/missings', str(instance.id), filename)

def get_image_victims_path(instance, filename):
    return os.path.join('images/victims', str(instance.id), filename)


class Customer(models.Model):
    fullname = models.CharField(max_length=50)
    telephone = models.CharField(max_length=12)
    email = models.EmailField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname


class Post_type(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name

    
class Post(models.Model):
    text = models.TextField()
    time = models.DateTimeField()
    found = models.BooleanField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    post_type = models.ForeignKey(Post_type, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Adress(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    home = models.CharField(max_length=20)

    def __str__(self):
        return name


class Relative(models.Model):
    relation = models.CharField(max_length=20)
    fullname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    birthday = models.DateField()
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=12)
    position = models.CharField(max_length=30)
    
    
class Missing_person(models.Model):
    fullname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=20)
    birthday = models.DateField()
    missing_place = models.ForeignKey(Adress, on_delete=models.CASCADE)
    missing_time = models.DateField()
    status = models.CharField(max_length=20)
    relatives = models.ForeignKey(Relative, on_delete=models.CASCADE)

    def __str__(self):
        return fullname


class Images(models.Model):
    person = models.ForeignKey(Missing_person, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_missings_path, default = 'images/non.png')


class Victim(models.Model):
    date = models.DateField()
    place = models.ForeignKey(Adress, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_victims_path, default = 'images/non.png')
    additional_information = models.CharField(max_length=50)



    
