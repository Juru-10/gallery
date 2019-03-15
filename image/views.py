from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image


# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Gallery')

def image_of_day(request):
    date = dt.date.today()
    image = Image.todays_image()
    return render(request, 'all-image/today-image.html', {"date": date,"image":image})

def past_days_image(request,past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(image_of_day)

    image = Image.days_image(date)
    return render(request, 'all-image/past-image.html', {"date": date,"image":image})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images_id = Image.get_image_by_id(search_term)
        # searched_images_loc = Image.filter_by_location(search_term)
        # searched_images_cat = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'all-image/search.html',{"message":message,"images": searched_images_id})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-image/search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-image/image.html", {"image":image})

def image_details(request):
    if date == dt.date.today():
        image = Image.todays_image()
    else:
        image = Image.days_image(date)

    return render(request,"all-image/image.html", {"date": date,"image":image})
