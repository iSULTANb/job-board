from django.db import models

# Create your models here.



class Job(models.Model):

    Type_Of_Job = (

    ('Part Time','Part Time'),
    ('Full Time','Full_Time'),

    )

    title = models.CharField(max_length=200)
    #location
    job_type = models.CharField(max_length=20,choices=Type_Of_Job)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=0)
    salary = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    category = models.ForeignKey('Category',on_delete = models.CASCADE,)
    image = models.ImageField(upload_to='jobs')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
