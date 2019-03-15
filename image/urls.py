from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.image_of_day,name='imageToday'),
    url(r'^$',views.all_images,name='all_images'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_image,name = 'pastImage'),
    url(r'^search/', views.search_results, name='search_results'),
    # url(r'^image/',views.image_details,name ='image_details'),
    url(r'^image/(\d+)',views.image,name ='image')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
