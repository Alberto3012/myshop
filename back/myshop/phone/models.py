from django.db import models

# Create your models here.
class Brand(models.Model):
    brand = models.CharField(max_length=50)

    class Meta:
        db_table = 'brand' 
    
    def __str__(self):
        return self.brand
        
class Color(models.Model):
    color = models.CharField(max_length=50)
    color_hex = models.CharField(max_length=50)

    class Meta:
        db_table = 'color'  

    def __str__(self):
        return self.color

class So(models.Model):
    so = models.CharField(max_length=50)
    firmware = models.CharField(max_length=50)

    class Meta:
        db_table = 'so' 
    
    def __str__(self):
        return self.so + ', ' + self.firmware

class Screen_resolution(models.Model):
    resolution = models.CharField(max_length=20)

    class Meta:
        db_table = 'screen_resolution' 

    def __str__(self):
        return self.resolution
        
class Camera(models.Model):
    camera_name = models.CharField(max_length=50)
    resolution = models.DecimalField(max_digits=4, decimal_places=1) 
    aperture = models.CharField(max_length=10) 
    sensor_type = models.CharField(max_length=50)
    flash = models.CharField(max_length=50)
    features = models.TextField() 
    video_resolution = models.CharField(max_length=20)
    number_of_cameras = models.IntegerField()

    class Meta:
        db_table = 'camera'
    
    def __str__(self):
        return self.camera_name

class Phone(models.Model):
    identifier = models.CharField(max_length=50, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    battery = models.CharField(max_length=100)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    screen_resolution = models.ForeignKey(Screen_resolution, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)  # mm
    width = models.DecimalField(max_digits=5, decimal_places=2)   # mm
    depth = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    storage = models.CharField(max_length=100)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    so = models.ForeignKey(So, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'phone' 
        

