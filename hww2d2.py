# 1. Python Sets Adventure
# Task 1: Flight Route Comparison
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

same_destinations = our_routes.intersection(competitor_routes)
print(same_destinations) #Destinations that both airlines fly to.

different_destinations = our_routes.difference(competitor_routes)
print(different_destinations) #Destinations unique to your airline.

unique_destinations = our_routes.symmetric_difference(competitor_routes)
print(unique_destinations)

# 2. Set Operations in Data Analysis
# Task 1: Duplicate Entries Cleanup
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

no_dups = {num for num in customer_ids}
print(no_dups)

# 3. Music Festival Playlist Organization
# Task 1: Artist Lineup Compilation
artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()

for artist in artist_names:
    unique_artists.add(artist)
print(unique_artists)