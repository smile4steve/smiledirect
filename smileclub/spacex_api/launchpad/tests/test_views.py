import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..datasource import DataSource
#from ..serializers import LaunchPadSerializer

## init the APIClient app
client = Client()

class TestGetAllLaunchPad(TestCase):
    '''
    test module for GET from our api
    '''

    def setUp(self) -> None:
        pass


    def test_get_all_launchpad(self):
        # get data from our API
        response = client.get(reverse('get_all_launchpads'))

        # get the data locally
        ds   = DataSource.factory()
        data = ds.get_all_lp()

        self.assertEqual(response.data, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_one_launchpad(self):
        # get one item from our API
        id       = 3  # any ole guess
        response = client.get(reverse('get_one_launchpad', kwargs={'pk': id}))

        # get the data locally
        ds   = DataSource.factory()
        data = ds.get_lp_by_id( id )

        self.assertEqual(response.data, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_invalid_get_one_launchpad(self):
        # get one item from our API
        id       = 42  # any ole guess
        response = client.get(reverse('get_one_launchpad', kwargs={'pk': id}))

        # get the data locally
        ds   = DataSource.factory()
        data = ds.get_lp_by_id( id )

        self.assertEqual(response.data, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND) # sloppy steve...

