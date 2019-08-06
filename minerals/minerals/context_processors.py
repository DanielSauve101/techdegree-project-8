from rocks.models import Mineral

def custom_proc(request):
    """A context processor that provides groups."""
    groups = Mineral.objects.order_by('group').values_list('group', flat=True).distinct()
    return {
        'groups': groups
    }