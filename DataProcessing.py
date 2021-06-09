def readFileToData(data, path):
    names = []
    year = getYear(path)
    with open(path, mode='r') as csvFile:
        for i, line in enumerate(csvFile):
            if i == 0:
                names = line.split(",")
            else:
                row = {}
                for j, val in enumerate(line.split(",")):
                    try:
                        row[names[j]] = val
                    except IndexError:
                        print(line)
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

def allCountriesForRegion(data, region):
    countries = set()
    filteredData = filter(lambda row: row["Region"] == region, data)
    for row in filteredData:
        countries.add(row["Country"])
    return list(countries)

data = []
readFileToData(data, 'Assets/2015.csv')
readFileToData(data, 'Assets/2016.csv')
print(allCountriesForRegion(data, "Southeastern Asia"))
#print(getYear('Assets/2015.csv'))
