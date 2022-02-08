
from django.test import TestCase
from data_view.models import data_view

class ModelTesting(TestCase):
 def setUp(self):
  self.data_view = data_view.objects.create(id_lot='django', nb_piece='django')


def test_post_model(self):
        d = self.data_view
        self.assertTrue(isinstance(d, data_view))
        self.assertEqual(str(d, 'django'))

class ModelTesting(TestCase):
    @classmethod
    def setUpTestmodel(cls):
        data_view.objects.create(id_lot="48_4_GardenCity-Inten'City_Bouygues", typologie="Appartemente")

    def test_id_lot_label(self):
        immo = data_view.objects.get(id=1)
        field_label = immo._meta.get_field('id_lot').verbose_name
        self.assertEqual(field_label, 'id_lot')

    def test_date_extraction_label(self):
        immo = data_view.objects.get(id=1)
        field_label = immo._meta.get_field('date_extraction').verbose_name
        self.assertEqual(field_label, 'date_extraction')

    def test_id_lot_max_length(self):
        immo = data_view.objects.get(id=1)
        max_length = immo._meta.get_field('id_lot').max_length
        self.assertEqual(max_length, 255)

    def test_object_name_is_id_lot_Appartement_commae(self):
        immo = data_view.objects.get(id=1)
        expected_object_name = f'{immo.id_lot}, {immo.Appartemente}'
        self.assertEqual(str(immo), expected_object_name)