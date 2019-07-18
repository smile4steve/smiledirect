from django.test import TestCase
from ..api_lookup import LaunchPad
from ..models import LaunchPad as ModelLaunchPad
from ..datasource import DataSource

import logging
log = logging.getLogger(__name__)


# Create your tests here.
class APILookupTest(TestCase):
    '''
    test the apilookup class
    '''

    log.info('APILookupTest started')

    def test_get_object(self):
        mode = DataSource.api_mode

        if not mode:
            ds = DataSource.factory(mode)
            obj = ModelLaunchPad
            self.assertIsInstance(ds, obj )

        if mode:
            ds = DataSource.factory(mode )
            obj = LaunchPad
            self.assertIsInstance(ds, obj )
        #
        # interesting... can I use this syntax?
        # AssertionError: <LaunchPad: LaunchPad object (None)> is not an instance of <class 'launchpad.api_lookup.LaunchPad'>


    def test_get_data(self):
        # api = LaunchPad()
        api = DataSource.factory(1)
        self.assertIsNotNone(api.data, 'we have data')

    def test_get_id(self):
        # api = LaunchPad()
        api = DataSource.factory(1)
        rec = []
        rec = api.lp_id('kwajalein_atoll')
        log.debug('test_get_id for kwajalein_atoll: %s' % (rec) )

        self.assertEqual(rec[0]['lp_name'], 'Kwajalein Atoll Omelek Island')
        self.assertEqual(rec[0]['lp_status'], 'retired')
        self.assertEqual(rec[0]['lp_id'], 'kwajalein_atoll')

    '''
    {'id': 'kwajalein_atoll', 'full_name': 'Kwajalein Atoll Omelek Island', 'status': 'retired'}
    '''

    def test_get_one_lp(self):
        # api = LaunchPad()
        api = DataSource.factory(1)
        rec = []
        rec = api.get_lp_by_id(3)

        for k in rec[0].keys():
            self.assertIn(k, api.allowed_lp_keys, "valid key found")


    def test_bad_get_one_lp(self):
        # api = LaunchPad()
        api = DataSource.factory(1)
        rec = []
        try:
            rec = api.get_lp_by_id(333)
        except :
            log.debug('ERROR: we expected an error: %s' % Exception )
            print('ERROR: we expected an error: %s' % Exception )


    def test_get_all_lp(self):
        api  = DataSource.factory(1)  # just to be sure we are testing the right object
        data = api.get_all_lp()
        self.assertGreaterEqual( len(data), 5, 'did we get all the records' )
