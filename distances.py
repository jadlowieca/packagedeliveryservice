import csv
class Distances:
    def __init__(self, file_path):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            distanceHash = {}
            hubNames = []

            for i, row in enumerate(reader):
                if i < 8:
                    if i == 7:
                        for name in row[2:]:
                            holder = name.strip().split('\n')
                            hubName = '4001 South 700 East' if holder[1] == 'HUB' else holder[1].strip(", ")
                            hubNames.append(hubName)
                    continue

                if len(row) >= len(hubNames) + 2:
                    hubDistances = {}
                    for j in range(len(hubNames)):
                        distance_str = row[j + 2].strip()
                        if distance_str:
                            hubDistances[hubNames[j]] = float(distance_str)
                        else:
                            hubDistances[hubNames[j]] = None
                    distance_key = row[1].strip().split('\n')[0].strip(", ")
                    if distance_key == 'HUB':
                        distance_key = '4001 South 700 East'
                    if distance_key == '5383 S 900 East #104':
                        distance_key = '5383 South 900 East #104'
                    if distance_key == '3575 W Valley Central Station bus Loop':
                        distance_key = '3575 W Valley Central Sta bus Loop'
                    distanceHash[distance_key] = hubDistances

        self.distances = distanceHash

    def distance_finder(self, point_a, point_b):
        distance = self.distances.get(point_a).get(point_b)
        if distance is None:
            distance = self.distances.get(point_b).get(point_a)
        if distance is None:
            print("the distance could not be found")
            print(point_a, point_b)
        return distance

Distances("Data/WGUPS Distance Table.csv")
