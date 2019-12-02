from django.db import models
# Create your models here.

class blog(models.Model):
    STATUS_CHOICES=(
        ("scholarship","Scholarship"),
            ("examination","Examination"),
            ("career","Career"),
            ("fellowship","Fellowship")
            )
    blog_image=models.ImageField(upload_to='blog_media',default="")
    blog_title=models.CharField(max_length=300)
    blog_type = models.CharField( max_length=50, choices=STATUS_CHOICES, default="scholarship" )
    blog_author_name=models.CharField(max_length=200)
    blog_content=models.CharField(max_length=5000)
    publish_date=models.DateField()

    def __str__(self):
        return self.blog_title+" by "+str(self.blog_author_name)+" on "+str(self.publish_date)




