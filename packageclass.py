from enum import Enum
from hash import HashMap
import csv

class PackageStatus(str, Enum):
    ATHUB = "At the WGU Hub"
    ENROUTE = "ENROUTE"
    DELIVERED = "Package delivered"

class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight ):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = PackageStatus.ATHUB
        self.departure_time = None
        self.arrival_time = None

    def package_formatted(self):
        formatted_address = (
            f"\n{self.address}, \n{self.city}, {self.state} {self.zip}"
        )
        return formatted_address

    def get_status(self):
        return self.status

    def setstatus(self, status:PackageStatus):
        self.status = status

    def __str__(self):
        return f'Package {self.id}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.deadline}, {self.arrival_time}, {self.weight}, {self.status.value}'

def load_packages(file_path):
    package_map = HashMap()

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        for i in range(8):
            next(reader)

        for row in reader:
            if row:
                package_id = row[0].strip()
                address = row[1].strip()
                if address == "3575 W Valley Central Station bus Loop":
                    address = "3575 W Valley Central Sta bus Loop"
                elif address == "5383 S 900 East #104":
                    address = "5383 South 900 East #104"
                elif address == "HUB":
                    address = "4001 South 700 East"
                city = row[2].strip()
                state = row[3].strip()
                zip_code = row[4].strip()
                deadline = row[5].strip()
                weight = row[6].strip()

                package = Package(package_id, address, city, state, zip_code, deadline, weight)

                package_map.insert(package_id, package)
                print(package)
    return package_map


#load_packages("C:\\Users\\Cindy\\PythonStuff\\WGUPS Package File.csv")