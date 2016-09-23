# -*- coding: utf-8 -*-

import json
#from pprint import pprint

#read the source data file and work with it
with open ("parkscheinautomaten_raw_data.json", "r", encoding="utf-8") as myfile:
    full = json.load(myfile)
    result = full['result']
    records = result['records']
    #pprint(full)

    #begin to count with 0
    i=0

    #make an empty list
    automaten = []

    #run this loop until every Parkautomat is done
    while i < len(records):
        data = records[i]

        bis = data['Abschnitt bis']
        von = data['Abschnitt von']
        ort = data['Aufstellort']
        bezirk = data['Bezirk/Gebiet']
        gebuehr = data[u'Geb\u00fchr je 20 Minuten']
        zeit = data[u'Geb\u00fchrenzeit']
        dauer = data[u'H\u00f6chstparkdauer in Std.']
        plaetze = data[u'Stellpl\u00e4tze']
        tag = data[u'Tagesgeb\u00fchr 4,00 \u20ac']
        handy = data['Handyparkzone']
        y = data['GeoKoordinateNord'].replace(",",".")
        x = data['GeoKoordinateOst'].replace(",",".")
        
        i=i+1
        
        #check if there is a "Tagesgebühr" in the "Parkscheinautomat", if not then "Nein"
        if tag == "": 
            tag = "Nein"
        else:
            pass

        #add all Parkautomat informations to the empty park list
        park = []
        park.append(bezirk) #Bezirk/Gebiet: 
        park.append(ort) #Aufstellort: 
        park.append(von) #Abschnitt von
        park.append(bis) #Abschnitt bis
        park.append(gebuehr) #Gebühr je 20 Minuten: 
        park.append(tag) #Tagesgebühr 4,00 €
        park.append(zeit) #Gebührenzeit: 
        park.append(dauer) #Höchstparkdauer in Std.
        park.append(handy) #Handyparkzone: 
        park.append(plaetze) #Stellplätze
        park.append(y) # Y-Koordinaten
        park.append(x) # X-Koordinaten

        #add the park list (containing one Parkautomat) to the automaten list
        automaten.append(park)


#write everything in a json file
with open('parkschein.json', 'w') as outfile:
    json.dump(automaten, outfile)

