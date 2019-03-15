from django.db import models
import datetime as dt
from django.db.models import Q

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

    # def del_editor(self):
    #     self.delete()

    def display_editors():
        Editor.objects.all()

    def update_editor(self):
        Editor.objects.filter(self).update(self)

    class Meta:
        ordering = ['first_name']

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_cat(self):
        self.save()

    def del_cat(self):
        self.delete()

    # def display_tags():
    #     tags.objects.all()

    def update_cat(self):
        Category.objects.filter(self).update(self)

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_loc(self):
        self.save()

    def del_loc(self):
        self.delete()

    # def display_tags():
    #     tags.objects.all()

    def update_loc(self):
        Location.objects.filter(self).update(self)


class Image(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length =60)
    description = models.TextField()
    editor = models.ForeignKey(Editor)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to = 'image/',default='SOME STRING')

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    # def display_artis():
    #     image.objects.all()

    # def update_arti(self):
    #     image.objects.filter(self).update(self)

    @classmethod
    def todays_image(cls):
        today = dt.date.today()
        image = cls.objects.filter(pub_date__date = today)
        return image

    @classmethod
    def days_image(cls,date):
        image = cls.objects.filter(pub_date__date = date)
        return image

    @classmethod
    def image_details(cls,image_id):
        image = cls.objects.get(pk = image_id)
        return image

    # @classmethod
    # def get_image_by_id(cls,search_id):
    #     image = cls.objects.filter(id__icontains=search_id)
    #     return image

    @classmethod
    def search_image(cls,search_cat,search_loc):
        image = cls.objects.filter(
        Q(category__name__icontains=search_cat) |
        Q(location__name__icontains=search_loc)
        )
        return image

    # @classmethod
    # def filter_by_location(cls,search_loc):
    #     image = cls.objects.filter(location__name__icontains=search_loc)
    #     return image
