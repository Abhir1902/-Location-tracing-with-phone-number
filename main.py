import phonenumbers
from phonenumbers import geocoder
number = str(input("Enter your mobile number : "))
key = 'db9a378a2e864d159b12c1d6581e1153' #The key needs to be constantly udpated. 
ch_number = phonenumbers.parse(number, "ch")
yourlocation  = geocoder.description_for_number(ch_number,"en")
print("Your location is : ",yourlocation,sep = "")

from phonenumbers import carrier
service_number = phonenumbers.parse(number,"RO")
print("Your service providers is : ",carrier.name_for_number(service_number,"en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(yourlocation)
result = geocoder.geocode(query)
lat = result[0]['geometry']['lat']
lng  = result[0]['geometry']['lng']
print("Latitude : ", lat,sep = "")
print("Longitude : ", lat,sep = "")