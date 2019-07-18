from django.test import TestCase
from ..models import LaunchPad


# Create your tests here.
class LaunchPadTest(TestCase):
    '''
    test the launchpad model
    '''

    def setUp(self) -> None:
        LaunchPad.objects.create(lp_id=90, lp_name='Sample SpaceX mission full_name', lp_status='active')
        LaunchPad.objects.create(lp_id=91, lp_name='Another sample spacex mission full_name', lp_status='retired')


    def test_get_names(self):
        lp_obj = LaunchPad.objects.get(lp_id=90)
        self.assertEqual(lp_obj.lp_name, 'Sample SpaceX mission full_name')
        self.assertEqual(lp_obj.lp_status, 'active')




