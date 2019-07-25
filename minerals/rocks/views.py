from django.http import Http404
from django.shortcuts import render

from .models import Mineral


def mineral_list(request):
    """View to show the mineral list using Paginator to limit 45 per page."""
    minerals = Mineral.objects.filter(name__startswith='A')
    return render(request, 'rocks/mineral_list.html', {'minerals': minerals})


def letter_search(request, letter=None):
    minerals = Mineral.objects.filter(name__startswith=letter)
    return render(request, 'rocks/mineral_list.html', {'minerals': minerals})


def mineral_detail(request, pk):
    """View to show detail of mineral and to show 404 if does not exist"""
    if Mineral.objects.filter(pk=pk).exists():
        mineral = Mineral.objects.filter(pk=pk).values()
        main_details_dict = {}
        important_details_dict = {}
        other_details_dict = {}
        for elements in mineral:
            for key, value in elements.items():
                if key != 'id':
                    if (key == 'name' or key == 'image_filename' or
                            key == 'image_caption'):
                        main_details_dict.update({key: value})
                    elif (key == 'category' or key == 'group'):
                        important_details_dict.update({key: value})
                    else:
                        if value:
                            other_details_dict.update({key: value})
        return render(request, 'rocks/mineral_detail.html',
                      {'main': main_details_dict,
                       'important': important_details_dict,
                       'other': other_details_dict})
    else:
        raise Http404('Mineral does not exist.')


def search(request):
    main_details_dict = {}
    important_details_dict = {}
    other_details_dict = {}
    term = request.GET.get('q')
    mineral = Mineral.objects.filter(
        name__icontains=term
    ).values()
    for elements in mineral:
        for key, value in elements.items():
            if key != 'id':
                if (key == 'name' or key == 'image_filename' or
                        key == 'image_caption'):
                    main_details_dict.update({key: value})
                elif (key == 'category' or key == 'group'):
                    important_details_dict.update({key: value})
                else:
                    if value:
                        other_details_dict.update({key: value})
    return render(request, 'rocks/mineral_detail.html',
                  {'main': main_details_dict,
                   'important': important_details_dict,
                   'other': other_details_dict})
