import math

from lxml import html
import requests
import requests_cache
import ephem

from . import utilities

requests_cache.install_cache(expire_after=86400)

def get(catnr):
    page = html.fromstring(requests.get('http://www.celestrak.com/NORAD/elements/gp.php?CATNR=%s' % catnr).text)
    tle = page.xpath('//p/text()')[0].split('\n')
    return tle[0].strip(), tle[1].strip(), tle[2].strip()
    
def getgroup(groupname):
    page = html.fromstring(requests.get('http://www.celestrak.com/NORAD/elements/gp.php?GROUP=%s&FORMAT=tle' % groupname).text)
    praw = page.xpath('//p/text()')[0].strip().split('\n')
    tlegroup = []
    pres = tuple(praw[x:x + 3]
       for x in range(0, len(praw), 3))
    for tle in pres:
        tlegroup += [ [ tle[0].strip(), tle[1].strip(), tle[2].strip()] ]
    return tlegroup

def parsegroup(group):
    tle_rec_group = []
    for tle in group:
        tle_rec = ephem.readtle(tle)
        tle_rec.compute()
        tle_rec_group += tle_rec
    return tle_rec_group
        
    
def parse(name, line1, line2):
    tle_rec = ephem.readtle(name, line1, line2)
    tle_rec.compute()
    return tle_rec
