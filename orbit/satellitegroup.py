
from . import satellite,tle

class satellitegroup:
    def __init__(self,groupname):
        satellitetle = tle.getgroup(groupname)
        self.satellite = []
        for rawtle in satellitetle:
            s = satellite(None,rawtle)
            self.satellite += [ s ]




