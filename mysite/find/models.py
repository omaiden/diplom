from django.db import models
import os

def get_image_missings_path(instance, filename):
    return os.path.join('images/missings', str(instance.id), filename)

def get_image_victims_path(instance, filename):
    return os.path.join('images/victims', str(instance.id), filename)



    
