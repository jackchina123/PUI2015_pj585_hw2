import json
import csv
import sys
import urllib2

#ab1fa649-f976-4c81-9742-fa2091862d0d
#http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=ab1fa649-f976-4c81-9742-fa2091862d0d&VehicleMonitoringDetailLevel=calls&LineRef=B52

if __name__=='__main__':

    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())


    with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['SAMPLE OUTPUT CONTENTS OF %s:' % (sys.argv[3])]
        headers2 = ['Latitude','Longitude','Stop Name','Stop Status']
        writer.writerow(headers)
        writer.writerow(headers2)
        act = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
        for s in act:
            lat  = s['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            lon  = s['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
           
            if 'StopPointName' in s['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]:
                sname = s['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
            else:
                sname = 'N/A'
            
            if 'PresentableDistance' in s['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']:
                status = s['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
            else:
                status = 'N/A'

            writer.writerow([lat, lon, sname, status])         
            
 


