import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany

print("All cities in Germany:")

# temp = []
# for city in cities:
#     if city["country"] == "Germany":
#         temp.append(city)

# print(city)
# print()

temp = [city["city"] for city in cities if city["country"] == "Germany"]
print(temp)
print()

# Print all cities in Spain with a temperature above 12°C

print("Cities in Spain with a temp above 12°C:")

temps = []
for city_data in cities:
    city = city_data["city"]
    country = city_data["country"]
    temp = float(city_data["temperature"])

    if country == "Spain" and temp > 12:
        temps.append(city)

print(city)
print()


# Count the number of unique countries

print("Count the number of unique countries")

country = [city["country"] for city in cities]
print(len(set(country)))
print()

# Print the average temperature for all the cities in Germany

print("Avg temp for all cities in Germany:")

temps = [float(city["temperature"]) for city in cities if city["country"] == "Germany"]

print(sum(temps)/len(temps))
print()


# Print the max temperature for all the cities in Italy

print("Max temp for all cities in Italy:")

temps = [float(city["temperature"]) for city in cities if city["country"] == "Italy"]

print(max(temps))
print()
