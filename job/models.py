from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.



class Job(models.Model):
    Type_Of_Job = (

    ('Part Time','Part Time'),
    ('Full Time','Full_Time'),
    )

    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    #location
    job_type = models.CharField(max_length=20,choices=Type_Of_Job)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=0)
    salary = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    category = models.ForeignKey('Category',on_delete = models.CASCADE)
    image = models.ImageField(upload_to='jobs')
    slug = models.SlugField(null = True,blank = True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args,**kwargs)

    def __str__(self):
        return (self.title)


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class ApplyJob(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE,max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.CharField(max_length=100)
    apply_file = models.FileField(upload_to='apply_jobs/')
    comment = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
