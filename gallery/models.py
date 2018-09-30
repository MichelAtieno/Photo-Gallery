from django.db import models

# Create your models here.
class Location(models.Model):
    pic_location = models.CharField(max_length=50)

    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()

    def update_location(self, update):
        self.pic_location = update
        self.save()

    @classmethod
    def get_location(cls, id):
        the_location = Location.objects.get(id=id)
        return the_location

    def __str__(self):
        return self.pic_location

class Category(models.Model):
    pic_category= models.CharField(max_length=50)

    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()
    
    def update_category(self, update):
        self.pic_category = update
        self.save()

    @classmethod
    def get_category(cls, id):
        category = Category.objects.get(id=id)
        return category

    def __str__(self):
        return self.pic_category   

class Image(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to = 'pictures/', default=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    class Meta:
        ordering = ('-id',)

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def __str__(self):
        return self.name

    @classmethod
    def get_image(cls,id):
        one_image = Image.objects.get(id=id)
        return one_image

    @classmethod
    def get_images(cls):
        all_images = Image.objects.all()
        return all_images
    
    @classmethod
    def search_image(cls,search_category):
        image_category = Image.objects.filter(category__pic_category__icontains=search_category)
        return image_category

    @classmethod
    def filter_by_location(cls, filter_location):
        image_location = Image.objects.filter(location__id=filter_location)
        return image_location   

