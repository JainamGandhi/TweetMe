from django.shortcuts import render
from django.views import View

from .models import HashTag


class HashTagView(View):
    def get(self,request,hashtag,*args,**kwargs):
        obj,created = HashTag.object.get_or_create(tag=hashtag)
        return render(request,'hashtags/tag_view.html',{"obj":obj})

# Create your views here.
