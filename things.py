import csv
from packageclass import Package

packageList = []
addressList = []
with open("C:\\Users\\Cindy\\PythonStuff\\WGUPS Package File.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    i=0
    for row in reader:
        if i < 8:
            i+=1
            continue
        else:
            packageList.append(Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            addressList.append(row[1])


import distances

def load_distance_hash(file_path):
    distance_hash = {}
    hub_names = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i < 8:
                if i == 7:
                    hub_names = [name.strip() for name in row[2:] if name.strip()]
                continue

            if len(row) >= len(hub_names) + 2:
                hub_distances = {}
                for j in range(len(hub_names)):
                    distance_str = row[j + 2].strip()
                    if distance_str:
                        hub_distances[hub_names[j]] = float(distance_str)
                    else:
                        hub_distances[hub_names[j]] = None
                distance_hash[row[0].strip()] = hub_distances

    return distance_hash