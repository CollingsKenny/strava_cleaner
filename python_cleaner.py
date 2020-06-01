import xmltodict


docname = "uncleanride.gpx"
THRESH = 0.01

with open("uncleanride.gpx") as fd:
    doc = xmltodict.parse(fd.read())

firsttrkpnt = False
prevLon = 0
for trackpoint in doc['gpx']['trk']['trkseg']['trkpt']:
    if('@lon' in trackpoint):
        if(not firsttrkpnt): # Set basecase compare value
            prevLon = trackpoint['@lon']
            firsttrkpnt = True
        else:
            curLon = trackpoint['@lon']
            diff = abs(float(prevLon) - float(curLon))
            if (diff > THRESH):
                print(curLon)
            prevLon = curLon
# xmltodict.parse(docname, item_depth=2, item_callback=handle_trackpoint)

