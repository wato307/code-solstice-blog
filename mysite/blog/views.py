from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
import json

from django.views.decorators.csrf import csrf_exempt

from .models import Artical, NewFavorite

# Create your views here.
def index(request):
    artical_list = Artical.objects.all()
    context = {"artical_list": artical_list}
    return render(request, "blog/index.html", context)

def detail(request, artical_id):
    artical = get_object_or_404(Artical, pk=artical_id) # pk: primary-key which is identical to id
    context = {'artical': artical}
    return render(request, "blog/detail.html", context)

@csrf_exempt
def favorite(request, artical_id, obj_type, auor):
    user = request.user
    ret = {"status": 0, "msg":""}
    c = ContentType.objects.get(model=obj_type)

    param = dict(content_type=c, object_id=artical_id, author=auor)
    try:
        new_favorite = NewFavorite.objects.get(**param)
        ret["msg"] = "已经点过赞了，不能再点赞了."
    except NewFavorite.DoesNotExist:
        new_favorite = NewFavorite(**param)
        ret["msg"] = "Create a new NewFavorite instance."
        new_favorite.save()    

        newFavs = NewFavorite.objects.filter(content_type=c, object_id=artical_id)
        ret["favorite_count"] = newFavs.count()
        ret["status"] = 1

    # try:
    #     newFavs = NewFavorite.objects.filter(content_type=c, object_id=artical_id)
    #     ret["favorite_count"] = newFavs.count()
    #     ret["status"] = 1
    # except:
    #     ret["msg"] = "except on NewFavorite.objects.filter(context_type=c, object_id=artical_id)"
       

    return HttpResponse(json.dumps(ret), content_type="application/json")

