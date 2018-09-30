from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class LocationTestClass(TestCase):
    # Set Up Method
    def setUp(self):
        self.nairobi = Location(pic_location='Nairobi')
        self.nairobi.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))
    
    def test_updating_location(self):
        location = Location.get_location(self.nairobi.id)
        location.update_location('Mombasa')
        location = Location.get_location(self.nairobi.id)
        self.assertTrue(location.pic_location == 'Mombasa')
    
    def tearDown(self):
        self.nairobi.delete_location()
    
class CategoryTestClass(TestCase):
    # Set Up Method
    def setUp(self):
        self.Food=Category(pic_category='Food')
        self.Food.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.Food,Category))
    
    def tearDown(self):
        self.Food.delete_category()
    
    def test_updating_category(self):
        category = Category.get_category(self.Food.id)
        category.update_category('food1')
        category = Category.get_category(self.Food.id)
        self.assertTrue(category.pic_category == 'food1')
    
class ImageTestCase(TestCase):
    # Set Up Method
    def setUp(self):
        self.Food = Category(pic_category='Food')
        self.Food.save_category()

        self.nairobi = Location(pic_location='Nairobi')
        self.nairobi.save_location()

        self.image = Image(name='Delicious', description='Best Meals in town', location=self.nairobi, category=self.Food)
        self.image.save_image()
    
    def tearDown(self):
        self.image.delete_image()
        self.Food.delete_category()
        self.nairobi.delete_location()
    
    def test_get_images(self):
        images = Image.get_images()
        self.assertTrue(len(images)>0)
    
    def test_get_image(self):
        images = Image.get_image(self.image.id)
        self.assertTrue(images == self.image)

    def test_search_image(self):
        images = Image.search_image('Food')
        self.assertTrue(len(images)>0)
    
    def test_filter_by_location(self):
        images = Image.filter_by_location('Nairobi')
        self.assertTrue(len(images)>0)