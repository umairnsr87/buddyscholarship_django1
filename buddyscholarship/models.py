
from django.urls import reverse
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
    slug = models.SlugField( max_length=200, unique=True)
    blog_type = models.CharField( max_length=50, choices=STATUS_CHOICES, default="scholarship" )
    blog_author_name=models.CharField(max_length=200)
    blog_content=models.CharField(max_length=5000)
    publish_date=models.DateField()

    def get_absolute_url(self):
        return reverse( 'post_detail', kwargs={'slug': self.slug} )

    def __str__(self):
        return self.blog_title+" by "+str(self.blog_author_name)+" on "+str(self.publish_date)




class cities(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class college(models.Model):
    scholarship_choices=(('yes','Yes'),
                         ('no','No'))

    college_name=models.CharField(max_length=400)
    college_url=models.URLField()
    college_scholarship_status=models.CharField(max_length=20,choices=scholarship_choices,default='---')
    college_city=models.ForeignKey(cities,on_delete=models.PROTECT)


