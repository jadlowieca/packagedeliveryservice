import csv
with open("C:\\Users\\Cindy\\PythonStuff\\WGUPS Distance Table.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    distanceHash = {}
    hubNames = []

    for i, row in enumerate(reader):
        if i < 8:
            if i == 7:
                hubNames = [name.strip() for name in row[2:] if name.strip()]
            continue

        if len(row) >= len(hubNames) + 2:
            hubDistances = {}
            for j in range(len(hubNames)):
                distance_str = row[j + 2].strip()
                if distance_str:
                    hubDistances[hubNames[j]] = float(distance_str)
                else:
                    hubDistances[hubNames[j]] = None
            distanceHash[row[0].strip()] = hubDistances
    print(distanceHash[9])

    def truck_route(self, packages:HashMap, distances:Distances):
        mileage=0
        for i in range(len(self.packages)):
            shortest_length = sys.maxsize
            distance = distances.distance_finder(self.location, packages.lookup(i).package_formatted())
            if distances < distance:
                shortest_length = distance
                self.location = self.packages[i].package_formatted()
            mileage += shortest_length
        time = self.speed
        return mileage