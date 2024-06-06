import phonenumbers
#from test import number
from phonenumbers import geocoder
from api_key import key # api key from opencage
import folium

number = input("Enter Number with country code: ")
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)


from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
location = str(number_location)
results = geocoder.geocode(location)
# print(results)
latitude = results[0]['geometry']['lat']
longitude = results[0]['geometry']['lng']
print(latitude, longitude)
map_location = folium.Map(location=[latitude, longitude], zoom_start=9)
folium.Marker([latitude, longitude], popup=number_location).add_to(map_location)
map_location.save("mobile_location.html")
