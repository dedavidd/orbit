from math import degrees

from . import tle, utilities

class satellite:
    def __init__(self,catnr,rawtle=None):
        if (rawtle is None):
            self.tle_raw = tle.get(catnr)
        else:
            self.tle_raw = rawtle
        self.tle_parsed = tle.parse(self.tle_raw[0], self.tle_raw[1], self.tle_raw[2])
    
    def name(self):
        return self.tle_raw[0].strip()
        
    def catalog_number(self):
        return self.tle_raw[1][2:7]
        
    def elsat_classification(self):
        return self.tle_raw[1][7]
        
    def launch_year(self):
        return utilities.calc_year(self.tle_raw[1][9:11])
        
    def tle(self):
        return [self.tle_raw[0], self.tle_raw[1], self.tle_raw[2]]
    
    def lat(self):
        return degrees(self.tle_parsed.sublat)
    
    def long(self):
        return degrees(self.tle_parsed.sublong)
    
    def next_pass(self,observer):
        return observer.next_pass(self.tle_parsed)
        
    def compute(self,observer):
        return self.tle_parsed.compute(observer)
        
    def elevation(self):
        return self.tle_parsed.elevation
        
    def eclipsed(self):
        return self.tle_parsed.eclipsed
