from django.db import models






class Contact(models.Model):


    name = models.CharField(max_length = 200)
    email = models.EmailField()
    phone = models.CharField(max_length = 200)
    subject = models.TextField()

    def __str__(self):
        return self.name





class Post(models.Model):


    Title = models.CharField(max_length = 200)
    Content = models.CharField(max_length = 1000)
    Link = models.CharField(max_length = 200)





    def __str__(self):

        return self.Title