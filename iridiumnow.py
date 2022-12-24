from orbit import satellite,satellitegroup
import ephem



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

for i in iridium.satellite:
    print("---------------------------------")
    showinfo(i)


