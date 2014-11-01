# Parser for traveline data
from xml.dom import minidom
import csv
from os import listdir
from os.path import isfile, join


def parsefiles():
    data_path = "/home/normal/Projects/OpenData/Travelline/SW"
    data_files = [ f for f in listdir(data_path) if isfile(join(data_path,f)) ]
    print "Parsing files..."

    # Prepare csv writers
    with open('data/AnnotatedStopPointRef.csv', 'wb') as stops_csvfile:
        stops_csv_writer = csv.writer(stops_csvfile)
        stops_csv_writer.writerow(["StopPointRef", "CommonName", "LocalityName", "LocalityQualifier"])

        with open('data/RouteSection.csv', 'wb') as routes_csvfile:
            routes_csv_writer = csv.writer(routes_csvfile)
            routes_csv_writer.writerow(["RouteSectionId", "RouteLinkId", "From", "To"])

            # Parse files
            for data_file in data_files:
                file_path = join(data_path, data_file)
                print file_path
                parsefile(file_path, stops_csv_writer, routes_csv_writer)

    

def parsefile(file_path, stops_csv_writer, routes_csv_writer):
    xmldoc = minidom.parse(file_path)

    annot_stoppoints = xmldoc.getElementsByTagName('AnnotatedStopPointRef')
    for s in annot_stoppoints:
        stop_point_ref = s.getElementsByTagName('StopPointRef')[0].childNodes[0].nodeValue
        common_name = s.getElementsByTagName('CommonName')[0].childNodes[0].nodeValue
        locality_name = s.getElementsByTagName('LocalityName')[0].childNodes[0].nodeValue
        locality_qualifier = s.getElementsByTagName('LocalityQualifier')[0].childNodes[0].nodeValue
        
        stops_csv_writer.writerow([stop_point_ref, common_name, locality_name, locality_qualifier])

    route_section = xmldoc.getElementsByTagName('RouteSection')
    for rs in route_section:
        route_links = rs.getElementsByTagName('RouteLink')
        route_section_id = rs.getElementsByTagName('RouteLink').attributes['id'].value

        for rl in route_links:
            route_link_id = rl.attributes['id'].value
            #print route_link_id
            from_stop = rl.getElementsByTagName('From')[0] \
                .getElementsByTagName('StopPointRef')[0] \
                .childNodes[0].nodeValue
            to_stop = rl.getElementsByTagName('To')[0] \
                .getElementsByTagName('StopPointRef')[0] \
                .childNodes[0].nodeValue

            routes_csv_writer.writerow([route_section_id, route_link_id, from_stop, to_stop])

        


if __name__ == "__main__":
    parsefiles()