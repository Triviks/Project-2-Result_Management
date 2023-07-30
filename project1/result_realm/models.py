from django.db import models

# Create your models here.

class profile(models.Model):
    # user=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    DOB = models.PositiveBigIntegerField()
    register_no = models.PositiveBigIntegerField()
    branch = models.CharField(max_length=30,)
    enrollment_no = models.PositiveBigIntegerField()
    blood = models.CharField(max_length=4,)
    gender = models.CharField(max_length=10,)
    mobile = models.PositiveBigIntegerField()
    alternative_mobile = models.PositiveBigIntegerField()
    parents_email = models.EmailField(max_length=30,)
    father_name = models.CharField(max_length=20,)
    mother_name = models.CharField(max_length=20,)
    father_occupation = models.CharField(max_length=20,)
    mother_occupation = models.CharField(max_length=20,)
    father_mobile = models.PositiveBigIntegerField()
    mother_mobile = models.PositiveBigIntegerField()
    premanent_address = models.CharField(max_length=50,)
    current_address = models.CharField(max_length=50,)
    local_guardian_address = models.CharField(max_length=50,)
    images = models.ImageField(upload_to="pics")
    
    def _str_(self):
        return self.name
    
class result(models.Model):
    name = models.CharField(max_length=30)
    register_no = models.PositiveBigIntegerField()
    branch = models.CharField(max_length=30)
    
    oosm = models.IntegerField()
    webm = models.IntegerField()
    phpm = models.IntegerField()
    crptom = models.IntegerField()
    oem = models.IntegerField()
    
    oosc = models.IntegerField()
    webc = models.IntegerField()
    phpc = models.IntegerField()
    crptoc = models.IntegerField()
    oec = models.IntegerField()
    
    oosg = models.CharField(max_length=30,)
    webg = models.CharField(max_length=30,)
    phpg = models.CharField(max_length=30,)
    crptog = models.CharField(max_length=30,)
    oeg = models.CharField(max_length=30,)
    
    credits_earned = models.IntegerField()
    GPA = models.FloatField()
    CGPA = models.FloatField()
    
    def _str_(self):
        return self.name