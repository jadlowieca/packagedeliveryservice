#Student ID 011561882
from distances import Distances
from packageclass import load_packages
from truckclass import Truck
from datetime import datetime
# Initialize trucks
departure_time_truck1 = datetime.strptime("8:00 AM", "%I:%M %p")
truck1 = Truck( 1,16, 18, None, [1, 13, 14, 15, 19, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East", departure_time_truck1)

departure_time_truck2 = datetime.strptime("9:05 AM", "%I:%M %p")
truck2 = Truck(2,16, 18, None, [2, 3, 4, 5, 6, 7, 8, 10, 18, 23, 25, 26, 27, 28, 36, 38], 0.0, "4001 South 700 East", departure_time_truck2)

departure_time_truck3 = datetime.strptime("12:30 PM", "%I:%M %p")
truck3 = Truck(3, 16, 18, None, [9, 11, 12, 17, 21, 22, 24, 32, 33, 35, 39], 0.0, "4001 South 700 East", departure_time_truck3)

# Load packages and distances
packages = load_packages("C:\\Users\\Cindy\\PythonStuff\\WGUPS Package File.csv")
distances = Distances("C:\\Users\\Cindy\\PythonStuff\\WGUPS Distance Table.csv")

# Track total mileage for all trucks
total_mileage_all_trucks = 0.0

# Execute the route for each truck and accumulate mileage
total_mileage_all_trucks += truck1.truck_route(packages, distances)
total_mileage_all_trucks += truck2.truck_route(packages, distances)
total_mileage_all_trucks += truck3.truck_route(packages, distances)

# Display the total mileage for all trucks
print(f"\nTotal mileage for all trucks: {total_mileage_all_trucks} miles.")