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
print()

# Let's write a function to filter out only items that meet the condition
# Hint: condition will be associated with an anonymous function, e.x., lamdbda x: max(x)
def filter(condition, dict_list):
    temps = []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps


# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    tmp = []
    for item in dict_list:
        tmp.append(item[aggregation_key])
    return aggregation_function(tmp)


# Print the average temperature of all the cities

print("Average temp of all cities:")
aggregate_list = aggregate("temperature", lambda x: sum(map(float, x))/max(len(x),1), cities)
print(aggregate_list)
print()


# Print all cities in Germany

print("All cities in Germany:")
filtered_list = filter(lambda x: x["country"] == "Germany", cities)
print(filtered_list)
print()


# Print all cities in Spain with a temperature above 12°C

print("All cities in Spain with temp above 12°C:")
filtered_list = filter(lambda x: x["country"] == "Spain" and float(x["temperature"]) > 12, cities)
print(filtered_list)
print()


# Count the number of unique countries

print("Count the number of unique countries:")
aggregate_list = aggregate("country", lambda x: len(set(x)), cities)
print(aggregate_list)
print()


# Print the average temperature for all the cities in Germany

print("Average temp for cities in Germany:")
filtered_list = filter(lambda x: x["country"] == "Germany", cities)
aggregate_list = aggregate("temperature", lambda x: sum(map(float, x))/max(len(x), 1), filtered_list)
print(aggregate_list)
print()


# Print the max temperature for all the cities in Italy

print("Max temp for all cities in Italy:")
filtered_list = filter(lambda x: x["country"] == "Italy" , cities)
aggregate_list = aggregate("temperature", lambda x: max(x), filtered_list)
print(aggregate_list)
print()
