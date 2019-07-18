# simple factory to handle creation
"""
•	Design the solution in such a way that that a database can later be used to replace the SpaceX REST API which
incurs as little re-work/re-factor as possible.

"""
from .models import LaunchPad
from .api_lookup import LaunchPad as APILaunchPad

class DataSource(object):

    api_mode = 1

    def factory(mode=api_mode):
        # need a simple way to switch between api lookup and database lookup
        if mode:
            obj = APILaunchPad()
        else:
            obj = LaunchPad()
        return obj


    def factory_serializer(mode=api_mode):
        pass



