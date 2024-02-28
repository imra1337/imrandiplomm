from django.db import models


class Course(models.Model):
    name = models.CharField(max_length = 40 , null = False)
    slug = models.CharField(max_length = 50 , null = False, unique = True)
    description = models.CharField(max_length = 250 , null = True)
    price = models.IntegerField(null = False, default = 499)
    discount = models.IntegerField(null = False, default = 0)
    active = models.BooleanField(default = False)
    thumbnail = models.ImageField(upload_to= "flies/tumbnail")
    date = models.DateTimeField(auto_now_add=True)
    resourse = models.FileField(upload_to= "flies/resourse")
    length = models.IntegerField(null = False)

    def __str__(self):
        return self.name

class CourseProperty(models.Model):
    description = models.CharField(max_length = 30, null = False)
    course = models.ForeignKey(Course, null = False, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Tag(CourseProperty):
    pass

class Prerequisite(CourseProperty):
    pass


class Learning(CourseProperty):
    pass    

class CouponCode(models.Model):
    code = models.CharField(max_length = 1000)
    course = models.ForeignKey(Course, on_delete= models.CASCADE, related_name = "coupon")
    discount = models.IntegerField(default = 0)


