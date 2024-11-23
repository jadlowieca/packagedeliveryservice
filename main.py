# Student ID: 011561882
# NOTE please run from pythonProject directory
# cd pythonProject 
from distances import Distances
from packageclass import load_packages, PackageStatus
from truckclass import Truck
from datetime import datetime, timedelta

# Initialize trucks with departure times and package loads
departure_time_truck1 = datetime.strptime("8:00 AM", "%I:%M %p")
truck1 = Truck(1, 16, 18, None, [1, 13, 14, 15, 19, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
               departure_time_truck1)

departure_time_truck2 = datetime.strptime("9:05 AM", "%I:%M %p")
truck2 = Truck(2, 16, 18, None, [2, 3, 4, 5, 6, 7, 8, 10, 18, 23, 25, 26, 27, 28, 36, 38], 0.0, "4001 South 700 East",
               departure_time_truck2)

departure_time_truck3 = datetime.strptime("12:30 PM", "%I:%M %p")
truck3 = Truck(3, 16, 18, None, [9, 11, 12, 17, 21, 22, 24, 32, 33, 35, 39], 0.0, "4001 South 700 East",
               departure_time_truck3)

# Load packages and distances
packages = load_packages("Data/WGUPS Package File.csv")
distances = Distances("Data/WGUPS Distance Table.csv")


# Function to query package statuses at a specific time
def query_package_status(query_time):
    print(f"\nPackage Status Report at {query_time.strftime('%I:%M %p')}")
    print("------------------------------------------------------")
    for package_id in range(1, 41):  # Assuming package IDs range from 1 to 40
        package = packages.lookup(str(package_id))
        if package:
            if query_time < package.departure_time:
                status = PackageStatus.ATHUB.value
            elif package.departure_time <= query_time < package.arrival_time:
                status = PackageStatus.ENROUTE.value
            else:
                status = PackageStatus.DELIVERED.value

            print(
                f"Package {package.id}: {status}, Delivery Time: {package.arrival_time.strftime('%I:%M %p')}")


# Execute the route for each truck and calculate total mileage
total_mileage_all_trucks = 0.0
total_mileage_all_trucks += truck1.truck_route(packages, distances)
total_mileage_all_trucks += truck2.truck_route(packages, distances)
total_mileage_all_trucks += truck3.truck_route(packages, distances)

# Print total mileage for all trucks
print(f"\nTotal mileage for all trucks: {total_mileage_all_trucks:.2f} miles.")

# Query package statuses at specific times for the required screenshots
query_times = [
    datetime.strptime("9:00 AM", "%I:%M %p"),
    datetime.strptime("10:00 AM", "%I:%M %p"),
    datetime.strptime("1:00 PM", "%I:%M %p"),
]

# Generate status reports for the requested times
for query_time in query_times:
    query_package_status(query_time)