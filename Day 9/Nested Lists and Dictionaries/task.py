capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested list in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }

# print(travel_log["France"][1])

# Nested list
nested_list = ["A", "B", ["C", "D"]]

# print(nested_list[2][1])

travel_log = {
    "France": {
        "total_visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "total_visits": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    }
}

print(travel_log["Germany"]["cities_visited"][2])