from django.db import models, migrations

# Create your models here.


class Mineral(models.Model):
    name = models.CharField(max_length=100)
    image_filename = models.TextField()
    image_caption = models.TextField(blank=True, default='')
    category = models.TextField(blank=True, default='')
    formula = models.TextField(blank=True, default='')
    strunz_classification = models.TextField(blank=True, default='')
    color = models.TextField(blank=True, default='')
    crystal_system = models.TextField(blank=True, default='')
    unit_cell = models.TextField(blank=True, default='')
    crystal_symmetry = models.TextField(blank=True, default='')
    cleavage = models.TextField(blank=True, default='')
    mohs_scale_hardness = models.TextField(blank=True, default='')
    luster = models.TextField(blank=True, default='')
    streak = models.TextField(blank=True, default='')
    diaphaneity = models.TextField(blank=True, default='')
    optical_properties = models.TextField(blank=True, default='')
    refractive_index = models.TextField(blank=True, default='')
    crystal_habit = models.TextField(blank=True, default='')
    specific_gravity = models.TextField(blank=True, default='')
    group = models.CharField(max_length=100, default='')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
