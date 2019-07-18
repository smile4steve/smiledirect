from django.db import models

import datetime
import logging
log = logging.getLogger(__name__)


class LaunchPad(models.Model):
    '''
    SpaceX.LaunchPad
    for future reference, some place to start the process
    '''
    lp_id     = models.IntegerField()
    lp_name   = models.CharField(max_length=255)
    lp_status = models.CharField(max_length=100)

    '''
    # okay, getting off track again... 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=10)  # login id? 
    updated_by = models.CharField(max_length=10)
    '''

    def __unicode__(self):
        return self.lp_name


    def get_lp_by_id(self, pk=0):
        # the pk lookup, ie, get data by index in the table
        # incomplete, untested
        # postpone for now.
        lp = []
        pk = int(pk)
        lp = self.objects.get(pk=pk)
        return lp


    def get_all_lp(self):
        # get all data
        # incomplete, untested
        # postpone for now.
        lp = []
        lp = self.objects.all()
        return lp

