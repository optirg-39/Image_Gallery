from django.shortcuts import render
from . models import Tag, PhotoImage
from PIL import Image as PilImage
from django.db.models import Q
import os
from django.core.paginator import Paginator
# Create your views here.

def addPhoto(request):

	if request.method == 'POST':
		myDict = dict(request.POST.lists())
		img = request.FILES.getlist('imagefiles')
		li = myDict['new_tags'].pop().replace(' ','').split(',')
		t = myDict['input_tags']

		# first make image instanc
		for ig in img:
			PhotoImage_inst, created = PhotoImage.objects.get_or_create(
                # tag=tag,
                description=myDict['description'],
                address=ig,
            )

			# input_tags
			for tg in t:
				tg_inst = Tag.objects.get(id = tg)
				PhotoImage_inst.tag.add(tg_inst)
				
			# #  new tags
			for ntg in li:
				ntg_inst, created = Tag.objects.get_or_create(name = ntg)
				PhotoImage_inst.tag.add(ntg_inst)

	tags = Tag.objects.all()
	return render(request,'app/addphoto.html',{'tags':tags})

def albumgallery(request):

	if request.method == 'POST':
		myDict = dict(request.POST.lists())
		search_tags = myDict['search_tags']
		if search_tags:
			querySet=PhotoImage.objects.all()
			for i in search_tags:
				querySet = querySet.filter(tag__name=i)
			tags = Tag.objects.filter(name__in = search_tags)
		elif search_tags is None:
			tags = Tag.objects.all()
			querySet =PhotoImage.objects.all() 
	else:
		tags = Tag.objects.all()
		querySet =PhotoImage.objects.all() 

	# pagination
	querySet=querySet.order_by('id')
	paginator = Paginator(querySet, 8, orphans=1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {'tags':tags, 'page_obj':page_obj}
	return render(request,'app/gallery.html',context)
	
def albumphoto(request, pk):
	photo_image = PhotoImage.objects.get(id = pk)
	tag = Tag.objects.filter(photo__id = pk)
	return render(request,'app/photo.html',{'image':photo_image, 'tag': tag})
