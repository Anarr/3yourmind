from django.shortcuts import render
from django.http import JsonResponse
from .services import *
from django.conf import settings
from .utils import output, modify_api_result
# Create your views here.

def index(request, tag = None):
    """
    get cats by tag

    Args:
        tag: display cat category

    Returns:
        Json
    """

    limit = request.GET.get('limit') or settings.LIMIT
    cats = CatService()
    data = cats.get_cats(tag, limit)
    result = output(modify_api_result(data))
    return JsonResponse(result, safe=False)

def categories(request):
    """
    get available categoreis for /api/cats/:tag API

    Returns:
        Json
    """
    limit = request.GET.get('limit') or settings.LIMIT
    cats = CatService()
    data = cats.get_categories(limit)
    result = output(data)
    return JsonResponse(result, safe=False)