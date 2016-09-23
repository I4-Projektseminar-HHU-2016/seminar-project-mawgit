# -*- coding: utf-8 -*-

import json
#from pprint import pprint

#read the source data file and work with it
with open ("busparkplaetze_raw_data.json", "r", encoding="utf-8") as myfile:
    full = json.load(myfile)
    features = full['features']
    #attributes = features['attributes']
    #geo = features['geometry']
    #pprint(features)

    #make an empty list
    automaten = []

    #begin to count with 0
    i=0

    #run this loop until every Busparklatz is done
    while i < len(features):   
        data = features[i]

        attr = data['attributes']
        bezeichnung = attr[u'BEZEICHNUN']
        gebuehren = attr[u'GEBUEHREN']
        nutzen = attr['NUTZUNGSART']

        geometry = data['geometry']
        geo = geometry['rings']

        i=i+1

        #begin to count with 0
        n=0

        #run this loop until every geo-location is done
        while n < len(geo[0]):
            y = geo[0][n][1]
            x = geo[0][n][0]

            n = n+1

            #add all Busparkplatz informations to the empty automat list
            automat = []
            automat.append(nutzen) #NUTZUNGSART
            automat.append(bezeichnung) #BEZEICHNUN
            automat.append(gebuehren) #GEBUEHREN
            automat.append(y) # Y-Koordinaten
            automat.append(x) # X-Koordinatens

            #add the automat list (containing one Busparkplatz) to the automaten list
            automaten.append(automat)

	
#write everything in a json file
with open('busparkplaetze.json', 'w') as outfile:
    json.dump(automaten, outfile)



