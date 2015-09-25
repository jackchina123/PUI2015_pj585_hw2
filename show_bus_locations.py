import json
import sys
import urllib2

#ab1fa649-f976-4c81-9742-fa2091862d0d
#http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=ab1fa649-f976-4c81-9742-fa2091862d0d&VehicleMonitoringDetailLevel=calls&LineRef=B52

if __name__=='__main__':
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())
    act = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    print 'Bus Line:', act[0]['MonitoredVehicleJourney']['PublishedLineName']
    print 'Number of Active Buses:', len(act)
    num = 0
    for s in act:
        lat  = s['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lon  = s['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print 'Bus %d is at latitude %s and %s' % (num, lat, lon)  
        num += 1
 
