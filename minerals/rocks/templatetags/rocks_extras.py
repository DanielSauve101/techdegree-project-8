from django import template

import random

from rocks.models import Mineral


register = template.Library()


@register.simple_tag
def random_mineral():
    """Generates a random mineral from the list of all minerals."""
    mineral_count = Mineral.objects.all().count()
    return random.randint(1, mineral_count)


@register.filter('name_modifier')
def name_modifier(str):
    """Replaces the '_' with a blank space in a string."""
    return str.replace('_', ' ')
