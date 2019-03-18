from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image
# from .forms import SearchForm


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

        search_cat = request.GET.get("image")
        search_loc = request.GET.get("image")
        # search_id = request.GET.get("image")

        searched_images_cat = Image.search_image(search_cat,search_loc)
        message = f"{search_cat}"
        return render(request, 'all-image/search.html',{"message":message,"images":searched_images_cat})

        # elif search_loc == request.GET.get("image"):
        #     searched_images_loc = Image.filter_by_location(search_loc)
        #     message = f"{search_loc}"
        #     return render(request, 'all-image/search.html',{"message":message,"images":searched_images_loc})

        # elif search_id == request.GET.get("image"):
        #     searched_images_id = Image.get_image_by_id(search_id)
        #     message = f"{search_id}"
        #     return render(request, 'all-image/search.html',{"message":message,"images": searched_images_id})


    else:
        message = "You haven't searched for any term"
        return render(request, 'all-image/search.html',{"message":message})

# def image_details(request,image_id):
#     try:
#         image = Image.objects.get(id = image_id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request,"all-image/image.html", {"image":image},image_id)

def image_details(request):
    # pk=Image.id
    image = Image.objects.get(id)
    image=Image.image_details(id)
    return render(request,"all-image/image.html", {"image":image})

def all_images(request):
    image=Image.objects.all()
    date=dt.date.today()
    # if date == dt.date.today():
    #     image = Image.todays_image()
    # else:
    #     image = Image.days_image(date)

    return render(request,"all-image/today-image.html", {"date": date,"image":image})

# def form():
#     form=SearchForm()
#     if form.is_valid():
#
#         return render('all-image/search.html')

# def search_lctn(request):
#     if 'image' in request.GET and request.GET["image"]:
#         search_loc = request.GET.get("image")
#         searched_images_loc = Image.filter_by_location(search_loc)
#         message = f"{search_loc}"
#         return render(request, 'all-image/search.html',{"message":message,"images":searched_images_loc})
#
#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'all-image/search.html',{"message":message})
