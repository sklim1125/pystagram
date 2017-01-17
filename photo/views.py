# coding: utf-8

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from photo.models import Photo
from photo.forms import PhotoEditForm

# Create your views here.
def single_photo(request, photo_id):
#    try:
#        photo = Photo.objects.get(pk=photo_id)
#    except Photo.DoesNotExist:
#        return HttpResponse("사진이 없습니다.")

    photo = get_object_or_404(Photo, pk=photo_id)
    response_text = '<p>{photo_id}번 사진을 보여줍니다.</p>'
    response_text += '<p>{photo_url}</p>'
    response_text += '<p><img src="{photo_url}" /></p>'

    return HttpResponse(response_text.format(photo_id=photo_id, photo_url=photo.image_file.url))

def new_photo(request):
    if request.method == "GET":
        edit_form = PhotoEditForm()
    elif request.method == "POST":
        edit_form = PhotoEditForm(request.POST, request.FILES)

        if edit_form.is_valid():
            new_photo = edit_form.save()
            return redirect(new_photo.get_absolute_url())

    return render(request, 'new_photo.html', {'form':edit_form,})
