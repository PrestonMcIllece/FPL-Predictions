from unittest import TestCase
from . import views
from . import connect_to_api

# Create your tests here.
class TestFPL(TestCase):
    '''Removes accents and lowercases names'''
    def test_format_name(self):
        self.assertEqual(views.format_name('TAMMY ABRAHAM'), 'tammy abraham') #lowercases names
        self.assertEqual(views.format_name('raúl jiménez'), 'raul jimenez') #removes accents
        self.assertEqual(views.format_name('José Ángel Esmorís Tasende'), 'jose angel esmoris tasende') #removes accents and lowercases names
        self.assertEqual(views.format_name("N'Golo Kanté"), "n'golo kante") #doesn't affect apostraphes in names

    def test_get_form():
        pass
    def test_compare_players():
        pass
    def test_parse_players():
        pass
    def test_run_model():
        pass
