from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="wazeyes") # Nome do seu aplicativo
location = geolocator.geocode("1222, Lins de Vasconcelos, Sao Paulo, SP")
print(location.address)
print((location.latitude, location.longitude)) 


