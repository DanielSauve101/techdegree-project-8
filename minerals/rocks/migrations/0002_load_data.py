from django.db import migrations

import json


def load_data(apps, schema_editor):
    """Function loads the initial data from the json file into the database"""
    Mineral = apps.get_model('rocks', 'Mineral')
    with open('data/minerals.json', encoding='utf-8') as file:
        minerals = json.load(file)
        for mineral in minerals:
            Mineral.objects.create(
                name=mineral.get('name', ''),
                image_filename=mineral.get('image_filename', ''),
                image_caption=mineral.get('image_caption', ''),
                category=mineral.get('category', ''),
                formula=mineral.get('formula', ''),
                strunz_classification=mineral.get('strunz_classification', ''),
                color=mineral.get('color', ''),
                crystal_system=mineral.get('crystal_system', ''),
                unit_cell=mineral.get('unit_cell', ''),
                crystal_symmetry=mineral.get('crystal_symmetry', ''),
                cleavage=mineral.get('cleavage', ''),
                mohs_scale_hardness=mineral.get('mohs_scale_hardness', ''),
                luster=mineral.get('luster', ''),
                streak=mineral.get('streak', ''),
                diaphaneity=mineral.get('diaphaneity', ''),
                optical_properties=mineral.get('optical_properties', ''),
                refractive_index=mineral.get('refractive_index', ''),
                crystal_habit=mineral.get('crystal_habit', ''),
                specific_gravity=mineral.get('specific_gravity', ''),
                group=mineral.get('group', '')
            )


class Migration(migrations.Migration):

    dependencies = [
        ('rocks', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]
