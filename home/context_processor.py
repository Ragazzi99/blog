from . models import *

def category(request):
    newscat = Category.objects.all()
    trendsongs = Blog_Post.objects.filter(trendsongs=True)
    mostviewed = Blog_Post.objects.filter(mostviewed=True)

    context = {
        'newscat':newscat,
        'trendsongs':trendsongs,
        'mostviewed':mostviewed,
    }

    return context 