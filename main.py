import phonenumbers
from phonenumbers import geocoder, carrier, timezone

number = input("Enter your phone number with +__: ")
phone = phonenumbers.parse(number)

country_name = phonenumbers.parse(number, "CN")
service_provider_name = phonenumbers.parse(number, "SP")
time = phonenumbers.parse(number, "TZ")

print(phone)
print(geocoder.description_for_number(country_name, "en"))
print(carrier.name_for_number(service_provider_name, "en"))
print(timezone.time_zones_for_number(time))
