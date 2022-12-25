from orbit import satellite,satellitegroup
import ephem


def showobserverinfo(obs,sat):
    nextpass = obs.next_pass(sat.tle_parsed)
    print("risetime, azimuth: %s, %s\nmax altitude at:   %s, %s\nset time, azimuth: %s, %s" % nextpass)
    return nextpass

def showinfo(sat):
    # Get the proper name of the satellite
    name = sat.name()
    print("name: %s" % name)

    # Get the current lat/long of the satellite
    current_latitude = sat.lat()
    print("current_latitude: %s" % current_latitude)
    current_longitude = sat.long()
    print("current_longitude: %s" % current_longitude)

    # Get the elsat classificiation of the satellite
    elsat_classification = sat.elsat_classification()
    print("elsat_classification: %s" % elsat_classification)

    # Get the year the satellite launched
    launch_year = sat.launch_year()
    print("launch_year: %s" % launch_year)

    # Get the current TLE for the satellite
    tle = sat.tle()
    print("tle: %s" % tle)

    # Get the current elevation of the satellite
    elevation = sat.elevation()
    print("elevation: %s" % elevation)

    # True if the satellite is currently in the earth's shadow
    eclipsed = sat.eclipsed()
    print("eclipsed: %s" % eclipsed)




iridium = satellitegroup.satellitegroup("iridium-NEXT")

hongkong = ephem.city("Hong Kong")
miami = ephem.city("Miami")
now = ephem.now()


obs = miami
obs.horizon = '7:30'
visible = []
predict = []
for s in iridium.satellite:
    s.compute(obs)
    nextpass = s.next_pass(obs)
    nextpass = [ nextpass ]
    nextpass += [s]
    predict += [ nextpass ]
    if (s.tle_parsed.alt>0.12):
        visible += [s]

print(now)
print("currently %s satelites visible" % len(visible))
obs.date = now - ephem.hour
for s in visible:
    print("---------------------------------")
    showinfo(s)
    nextpass = showobserverinfo(obs,s)
print("\ncurrently %s satelites visible" % len(visible))
for s in visible:
    settime = s.next_pass(obs)[4]
    print("%s: %s, %s visible for another %s" % (s.name(),s.tle_parsed.alt,s.tle_parsed.az,86400*(settime-now)))

def getrisetime(elem):
    return(elem[0][0])

predict.sort(key=getrisetime)

obs.date = now

print("\n\nnext in view\n")

for i in range(0,5):
    print("---------------------------------")
    transit = predict[i]
    s = transit[1]
    print("%s" % s.name())
    showobserverinfo(obs,s)




