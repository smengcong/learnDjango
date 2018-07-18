from django.shortcuts import render,HttpResponse,redirect
from video import models

# Create your views here.
def index(request,*args,**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        temp = int(v)
        kwargs[k] = temp
    class_list = models.Level.objects.all()
    type_list = models.Type.objects.all()
    direction_list = models.Direction.objects.all()

    video_list = models.Video.objects.filter(
        level_id=kwargs['level_id'],
        type=models.Type.objects.get(id=kwargs['type_id']),
        direction=models.Direction.objects.get(id=kwargs['direction_id']),
    )
    print(video_list)
    return render(
        request,
        'videoIndex.html',
        {
            'level_list':class_list,
            'type_list':type_list,
            'direction_list':direction_list,
            'kwargs':kwargs
        }
    )

