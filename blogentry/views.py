from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.views.generic.dates import YearArchiveView
from .models import BlogEntry, Likes
from .forms import BlogForm

# Create your views here.

class BlogYearArchiveView(YearArchiveView):
    queryset = BlogEntry.objects.all()
    template_name = 'home.html'
    date_field = "published_date"
    model = BlogEntry
    make_object_list = True
    allow_future = True
	
def home(request):
	blog = BlogEntry.objects.all()
	paginator = Paginator(blog,4) 
	page = request.GET.get('page')
	try:
	    blogs = paginator.page(page)
	except PageNotAnInteger:
	    blogs = paginator.page(1)  
	except EmptyPage:
         blogs = paginator.page(paginator.num_pages)
	context = {
				"blog" : blog,
				"blogs" : blogs,
				}
	return render(request, "home.html", context)
	
def blog_detail(request,slug):
	try:
		obj = BlogEntry.objects.get(slug=slug) 
		context = {
					"obj" : obj,
					}
		return render(request, "blog_detail.html", context)
	except:
		raise Http404

def blog_post(request):
	if request.method == "POST":
		form = BlogForm(request.POST)
		if form.is_valid():
            
			title = form.cleaned_data['title']
			description = form.cleaned_data['description']
			instance = form.save(commit=False)
			instance.title = title
			instance.description=description
			instance.save()
			return redirect('/')
	else:
		form = BlogForm()
	context = {
				"form" : form,
				}
	return render(request, "blogpost.html", context)
	
def likes(request, slug):
		object = BlogEntry.objects.get(slug=slug)
		likes_count = objects.likes_set.all().count()
		context = {
					"object" : object,
					"likes_count" : likes_count,
					}
		return render(request, "like_blog.html", context)

""""def paginate(request):
    blog_list = BlogEntry.objects.all()
    paginator = Paginator(blog_list, 2) 
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)
    return render(request, "blog_list.html", {"blogs": blogs})		
	"""