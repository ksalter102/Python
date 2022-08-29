# list in dictionary
# dict in dict

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"],"total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#nesting dict in list

travel_log = [
{
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
},
{
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
},
]

#adding to a key

def add_new_country(country_visited, times_visited,
                    cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities_visited"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#             country  times visited  cities visited


