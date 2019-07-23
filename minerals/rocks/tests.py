from django.urls import reverse
from django.test import TestCase

from .models import Mineral


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name='A',
            image_filename='mineralx.jpg',
            image_caption='this is the mineral x',
            category='xyz',
            formula='X<sub>42</sub>Y<sub>32</sub>',
            strunz_classification='15.XY.57',
            color='red',
            crystal_system='crystal',
            unit_cell='x = 8.508 \y00z5',
            crystal_symmetry='group xyz',
            cleavage='probable',
            mohs_scale_hardness='2\u20133',
            luster='sub crystal',
            streak='yellow',
            diaphaneity='Semitransparent',
            optical_properties='not sure',
            refractive_index='x\y03c9 = 1.597',
            crystal_habit='Forms crust-like aggregates',
            specific_gravity='34.20 - 18.22',
            group='sulphites'
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'rocks/mineral_list.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('detail',
                                       kwargs={'pk': self.mineral.pk}))
        main_dict = {'name': 'A', 'image_filename': 'mineralx.jpg',
                     'image_caption': 'this is the mineral x'}
        important_dict = {'category': 'xyz', 'group': 'sulphites'}
        other_dict = {'formula': 'X<sub>42</sub>Y<sub>32</sub>',
                      'strunz_classification': '15.XY.57',
                      'color': 'red',
                      'crystal_system': 'crystal',
                      'unit_cell': 'x = 8.508 \y00z5',
                      'crystal_symmetry': 'group xyz',
                      'cleavage': 'probable',
                      'mohs_scale_hardness': '2\u20133',
                      'luster': 'sub crystal',
                      'streak': 'yellow',
                      'diaphaneity': 'Semitransparent',
                      'optical_properties': 'not sure',
                      'refractive_index': 'x\y03c9 = 1.597',
                      'crystal_habit': 'Forms crust-like aggregates',
                      'specific_gravity': '34.20 - 18.22'}
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(main_dict, resp.context['main'])
        self.assertEqual(important_dict, resp.context['important'])
        self.assertEqual(other_dict, resp.context['other'])
        self.assertTemplateUsed(resp, 'rocks/mineral_detail.html')
