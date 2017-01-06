# coding: utf-8

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Photo

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
