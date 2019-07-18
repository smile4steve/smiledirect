import requests
from pprint import pprint

import logging
log = logging.getLogger(__name__)

from spacex_api import settings


'''
get the data from the external SpaceX api
'''


class LaunchPad():

    def __init__(self):
        self.data = []

        # map the api principle keys to the future db column names.
        self.api_keys_to_cols = {'id': 'lp_id', 'full_name': 'lp_name', 'status': 'lp_status'}

        # self.allowed_keys = ['id', 'full_name', 'status']
        self.allowed_api_keys = self.api_keys_to_cols.keys();
        self.allowed_lp_keys  = self.api_keys_to_cols.values();

        res       = requests.get(settings.SPACEX_SOURCE_API_URL, data={'status':'active'}, headers={"Content-Type": "application/json"})
        self.data = res.json()
        log.debug('hows the data look: %s' % self.data )
        self.data = self.reduce_data()


    def reduce_data(self):
        '''
        API solution should have the following attributes only...
        :return: data list of dicts
        '''
        myapi = []
        for rec in self.data:
            myrecord = {}
            for (key,val) in self.api_keys_to_cols.items():
                myrecord[val] = rec[key]
            myapi.append(myrecord)
        return myapi


    def get_lp_by_id(self, pk=0):
        '''
        fake the pk lookup, ie, get data by index in the list

        :param pk: integer for the sequence in our data list
        :return: list with one dict
        '''
        pk = int(pk)
        if (pk <= len(self.data)):
            return [self.data[pk]]
        else:
            log.debug("Input invalid, use a number less than %d" % (len(self.data)) )
            return []


    def get_all_lp(self):
        # get all the data.
        return self.data


    def search_by(self, key_name, key_val):
        '''
        Search the external API data using any of their keys, return the one (or more) record where the key matches your key_val
        :param key_name: one of the acceptable keys
        :param key_val: value to search for
        :return: record(s) matching the key_val of the key_name
        '''
        data = self.data
        # return [ row for row in data if row[key_name] == key_val ]

        # by design, key_name is one of the following: id, full_name, status
        # need data validation key_name.lower()
        try:
            key_name.lower() in self.allowed_lp_keys
        except:
            log.warning('invalid user entry of %s' % key_name.lower() )
            return 'Invalid key to search_by()'

        record = list(filter(lambda tt: tt[key_name] == key_val, data))
        log.debug('looking for %s of %s found: %s' % (key_name, key_val, record) )

        return record


    def lp_id(self, key_val):
        return self.search_by('lp_id', key_val)

    def lp_name(self, key_val):
        return self.search_by('lp_name', key_val)

    def lp_status(self, key_val):
        return self.search_by('lp_status', key_val)


