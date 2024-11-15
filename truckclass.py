from datetime import datetime, timedelta
from distances import Distances
from hash import HashMap
from packageclass import PackageStatus


class Truck:
    def __init__(self, id, capacity, speed, load, packages, mileage, address, depart_time):
        self.id=id
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time
        self.location = "4001 South 700 East"


    def __str__(self):
        return f'{self.capacity},{self.speed},{self.load},{self.packages},{self.mileage},{self.address},{self.depart_time}'

    def truck_route(self, packages: HashMap, distances: Distances):
        total_mileage = 0.0
        current_location = self.location
        undelivered_packages = [str(pkg_id) for pkg_id in self.packages]
        for package_key in undelivered_packages:
            my_package=packages.lookup(package_key)
            my_package.status=PackageStatus.ENROUTE
            my_package.departure_time = self.time

        # While there are still undelivered packages
        while undelivered_packages:
            shortest_distance = float('inf')
            nearest_package = None
            address_change_time = datetime.strptime("10:20 AM", "%I:%M %p")

            if self.time >= address_change_time:
                if packages['9'].address == "300 State St":  # Check if address hasn't been updated
                    packages['9'].address = "410 S State St"
                    print("Address for Package 9 has been updated to 410 S. State St.")

            # Find the nearest package from the current location
            for package_id in undelivered_packages:
                package = packages.lookup(package_id)
                if package is None:
                    continue
                distance = distances.distance_finder(current_location, package.address)

                if distance is not None and distance < shortest_distance:
                    shortest_distance = distance
                    nearest_package = package

            # Deliver the nearest package
            if nearest_package:
                travel_time = timedelta(hours=shortest_distance / self.speed)

                # Update truck's current time and location
                self.time += travel_time
                total_mileage += shortest_distance
                current_location = nearest_package.address

                # Mark package as delivered with delivery time
                nearest_package.arrival_time = self.time
                undelivered_packages.remove(nearest_package.id)

                # Set package to Delivered
                nearest_package.status = PackageStatus.DELIVERED

                # Print out the package delivery info
                print(
                    f"Truck {self.id} Delivered Package {nearest_package.id} to {nearest_package.address} at {self.time.strftime('%I:%M %p')}.")

        # Final report on the truck's route
        self.mileage = total_mileage
        print(f"Total mileage for route: {total_mileage} miles.")
        return total_mileage