def readFile(path):
    names = []
    data = []
    year = getYear(path)
    with open(path, mode='r') as csvFile:
        for i, line in enumerate(csvFile):
            if i == 0:
                names = line.split(",")
            else:
                row = {}
                for j, val in enumerate(line.split(",")):
                    row[names[j]] = val
                row["Year"] = year
                data.append(row)
    return data

def getYear(path):
    return path.replace("/", ".").replace("\\", ".").split(".")[-2]

def allRegions(data):
    regions = set()
    for row in data:
        regions.add(row["Region"])
    return list(regions)

print(readFile('Assets/2016.csv'))
#print(getYear('Assets/2015.csv'))
