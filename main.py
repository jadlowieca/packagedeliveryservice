# Student ID: 011561882
# NOTE: Please run from pythonProject directory
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


# Function to determine the package status at a given time
def get_package_status(package, query_time):
    if query_time < package.departure_time:
        return PackageStatus.ATHUB.value
    elif package.departure_time <= query_time < package.arrival_time:
        return PackageStatus.ENROUTE.value
    else:
        return PackageStatus.DELIVERED.value


# Menu option 1: Print all packages status and total mileage
def print_all_package_status():
    print("\nAll Packages Status and Total Mileage:")
    print(f"Total Mileage: {total_mileage_all_trucks:.2f} miles")
    print("------------------------------------------------------")
    print(f"{'PackageID':<10} {'Address':<35} {'City':<15} {'State':<10} {'ZIP':<10} {'Deadline':<12} {'Weight (kg)':<10} {'Status':<15} {'Delivery Time':<15}")
    print("-" * 130)
    for package_id in range(1, 41):
        package = packages.lookup(str(package_id))
        if package:
            status = get_package_status(package, datetime.now())
            delivery_time = package.arrival_time.strftime('%I:%M %p') if package.arrival_time else "N/A"
            print(f"{package.id:<10} {package.address:<35} {package.city:<15} {package.state:<10} {package.zip:<10} {package.deadline:<12} {package.weight:<10} {status:<15} {delivery_time:<15}")


# Menu option 2: Get single package status with a time
def get_single_package_status():
    package_id = input("Enter the Package ID: ").strip()
    time_input = input("Enter the Time (HH:MM AM/PM): ").strip()

    try:
        query_time = datetime.strptime(time_input, "%I:%M %p")
    except ValueError:
        print("Invalid time format. Please use HH:MM AM/PM.")
        return

    package = packages.lookup(package_id)
    if package:
        status = get_package_status(package, query_time)
        delivery_time = package.arrival_time.strftime('%I:%M %p') if package.arrival_time else "N/A"
        print("\nPackage Details:")
        print(f"{'PackageID':<10} {'Address':<35} {'City':<15} {'State':<10} {'ZIP':<10} {'Deadline':<12} {'Weight (kg)':<10} {'Status':<15} {'Delivery Time':<15}")
        print("-" * 130)
        print(f"{package.id:<10} {package.address:<35} {package.city:<15} {package.state:<10} {package.zip:<10} {package.deadline:<12} {package.weight:<10} {status:<15} {delivery_time:<15}")
    else:
        print("Package not found.")


# Menu option 3: Get all package status with a time
def get_all_package_status():
    time_input = input("Enter the Time (HH:MM AM/PM): ").strip()

    try:
        query_time = datetime.strptime(time_input, "%I:%M %p")
    except ValueError:
        print("Invalid time format. Please use HH:MM AM/PM.")
        return

    print(f"\nPackage Status Report at {query_time.strftime('%I:%M %p')}")
    print("------------------------------------------------------")
    print(f"{'PackageID':<10} {'Address':<35} {'City':<15} {'State':<10} {'ZIP':<10} {'Deadline':<12} {'Weight (kg)':<10} {'Status':<15} {'Delivery Time':<15}")
    print("-" * 130)
    for package_id in range(1, 41):  # Assuming package IDs range from 1 to 40
        package = packages.lookup(str(package_id))
        if package:
            status = get_package_status(package, query_time)
            delivery_time = package.arrival_time.strftime('%I:%M %p') if package.arrival_time else "N/A"
            print(f"{package.id:<10} {package.address:<35} {package.city:<15} {package.state:<10} {package.zip:<10} {package.deadline:<12} {package.weight:<10} {status:<15} {delivery_time:<15}")


# Execute the route for each truck and calculate total mileage
total_mileage_all_trucks = 0.0
total_mileage_all_trucks += truck1.truck_route(packages, distances)
total_mileage_all_trucks += truck2.truck_route(packages, distances)
total_mileage_all_trucks += truck3.truck_route(packages, distances)

while True:
    print("\n**************************************")
    print("WGUPS Package Delivery System")
    print("1. Print All Package Status and Total Mileage")
    print("2. Get a Single Package Status with a Time")
    print("3. Get All Package Status with a Time")
    print("4. Exit the Program")
    print("**************************************")
    option = input("Enter your choice (1-4): ").strip()

    if option == "1":
        print_all_package_status()
    elif option == "2":
        get_single_package_status()
    elif option == "3":
        get_all_package_status()
    elif option == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")