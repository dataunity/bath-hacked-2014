# Parser for traveline data
from xml.dom import minidom
import csv
from os import listdir
from os.path import isfile, join


def parsefiles():
    data_path = "/home/normal/Projects/OpenData/Travelline/SW"
    data_files = [ f for f in listdir(data_path) if isfile(join(data_path,f)) ]
    print "Parsing files..."
    #file_path = "/home/normal/Projects/OpenData/Travelline/SW/swe_30-7-A-y10-1.xml"
    for data_file in data_files:
        print data_file

    

def parsefile(file_path)
    xmldoc = minidom.parse(file_path)

    annot_stoppoints = xmldoc.getElementsByTagName('AnnotatedStopPointRef')
    print "annot_stoppoints"
    print len(annot_stoppoints) 

    with open('data/AnnotatedStopPointRef.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["StopPointRef", "CommonName", "LocalityName", "LocalityQualifier"])
        for s in annot_stoppoints:
            stop_point_ref = s.getElementsByTagName('StopPointRef')[0].childNodes[0].nodeValue
            common_name = s.getElementsByTagName('CommonName')[0].childNodes[0].nodeValue
            locality_name = s.getElementsByTagName('LocalityName')[0].childNodes[0].nodeValue
            locality_qualifier = s.getElementsByTagName('LocalityQualifier')[0].childNodes[0].nodeValue

            # print stop_point_ref
            # print common_name
            # print locality_name
            # print locality_qualifier

            csv_writer.writerow([stop_point_ref, common_name, locality_name, locality_qualifier])

    route_section = xmldoc.getElementsByTagName('RouteSection')
    with open('data/RouteSection.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["RouteLinkId", "From", "To"])
        for s in route_section:
            route_links = s.getElementsByTagName('RouteLink')

            for rl in route_links:
                route_link_id = rl.attributes['id'].value
                #print route_link_id
                from_stop = rl.getElementsByTagName('From')[0] \
                    .getElementsByTagName('StopPointRef')[0] \
                    .childNodes[0].nodeValue
                to_stop = rl.getElementsByTagName('To')[0] \
                    .getElementsByTagName('StopPointRef')[0] \
                    .childNodes[0].nodeValue

                csv_writer.writerow([route_link_id, from_stop, to_stop])

        


if __name__ == "__main__":
    parsefiles()