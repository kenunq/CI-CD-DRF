from django.test import TestCase

from SimpleApp.models import SimpleModel

# Create your tests here.


class SimpleTest(TestCase):
    def test_first_in_bd(self):
        result = SimpleModel.objects.get(pk=1).SimpleText
        self.assertEqual(result, "Text 1")

    def test_second_in_bd(self):
        result = SimpleModel.objects.get(pk=2).SimpleText
        self.assertEqual(result, "Text 3")
