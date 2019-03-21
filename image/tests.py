from django.test import TestCase
from .models import Editor,Image,Location,Category
import datetime as dt
# from django.db.models import Q

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    # def test_del_editor(self):
    #     self.james.del_editor()
    #     editors = Editor.objects.all()
    #     self.assertTrue(len(editors) == 0)

    # def test_display_editors():
    #     Editor.objects.display_editors()
    #     editors = Editor.objects.all()
    #     self.assertTrue(len(editors) > 0)
    #
    # def test_update_editor(self):
    #     Editor.objects.update_editor(self)
    #     editors = Editor.objects.all()
    #     self.assertTrue(len(editors) > 0)

# class tagsTestClass(TestCase):

    # def test_save_tag(self):
    #     self.james.save_editor()
    #     tags = tags.objects.all()
    #     self.assertTrue(len(tags) > 0)

#     def test_del_tag(self):
#         self.james.del_editor()
#         tags = tags.objects.all()
#         self.assertTrue(len(tags) == 0)
#
#     def test_display_tags():
#         tags.objects.display_tags()
#         tags = tags.objects.all()
#         self.assertTrue(len(tags) > 0)
#
#     def test_update_tag(self):
#         tags.objects.update_tagss(self)
#         Tags = tags.objects.all()
#         self.assertTrue(len(Tags) > 0)
#
#
class ImageTestClass(TestCase):
    def setUp(self):
        # Creating a new editor and saving it
        self.assumpta= Editor(first_name = 'Assumpta', last_name ='Uwanyirijuru', email ='jurassu10@gmail.com')
        self.assumpta.save_editor()

        # Creating a new tag and saving it
        self.new_cat = Category(name = 'testing')
        self.new_cat.save()

        self.new_loc = Location(name = 'testing')
        self.new_loc.save()

        self.new_image= Image(name = 'Test Image',description = 'This is a random test Post',editor = self.assumpta,location = self.new_loc,category = self.new_cat)
        self.new_image.save()

        # self.new_image.location.save(self.new_loc)
        # self.new_image.category.save(self.new_cat)

    def tearDown(self):
        Editor.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    def test_get_image_today(self):
        today_image = Image.todays_image()
        self.assertTrue(len(today_image)>0)

    def test_get_image_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        image_by_date = Image.days_image(date)
        self.assertTrue(len(image_by_date) == 0)


    # def test_get_image_by_id(self):
    #     image_by_id = Image.get_image_by_id()
    #     self.assertTrue(len(image_by_id)>0)

    # def test_search_image(self):
    #     search_cat =
    #     search_loc =
    #     search_image = Image.search_image(search_cat,search_loc)
    #     self.assertTrue(len(search_image)>0)

    # def test_filter_by_location(self):
    #     filter_by_location = Image.filter_by_location()
    #     self.assertTrue(len(filter_by_location)>0)
