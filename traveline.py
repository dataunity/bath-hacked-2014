# Parser for traveline data
from xml.dom import minidom
import csv


def parsefiles():
    print "Parsing files..."
    file_path = "/home/normal/Projects/OpenData/Travelline/SW/swe_30-7-A-y10-1.xml"


    xmldoc = minidom.parse(file_path)

    annot_stoppoints = xmldoc.getElementsByTagName('AnnotatedStopPointRef')
    print "annot_stoppoints"
    print len(annot_stoppoints) 

    with open('data/AnnotatedStopPointRef.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile)
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

    # route_section = xmldoc.getElementsByTagName('RouteSection')
    # with open('RouteSection.csv', 'wb') as csvfile:
    #     csv_writer = csv.writer(csvfile)
    #     for s in route_section:
    #         route_links = s.getElementsByTagName('RouteLink')

    #         csv_writer.writerow([stop_point_ref, common_name, locality_name, locality_qualifier])

        


if __name__ == "__main__":
    parsefiles()