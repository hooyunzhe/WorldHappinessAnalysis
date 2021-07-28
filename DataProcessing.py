YEAR = "Year"
COUNTRY = "Country"
REGION = "Region"

def readFileToData(data, path):
    names = []
    year = getYearFromFileName(path)
    with open(path, mode='r') as csvFile:
        for i, line in enumerate(csvFile):
            if i == 0:
                names = line.split(",")
            else:
                row = {}
                for j, val in enumerate(line.split(",")):
                    try:
                        row[names[j].strip()] = val.strip()
                    except IndexError:
                        print(line)
                row["Year"] = year
                data.append(row)
    return data

def getYearFromFileName(path):
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
        countries.add(row[COUNTRY])
    return list(countries)

def allRowsByYearRange(data, startYear, endYear):
    return (list(filter(lambda x: int(x[YEAR]) in range(startYear, endYear+1), data)))

def allYears(data):
    year = set()
    for i in data:
        year.add(i[YEAR])
    return year

def allCols(data):
    cols = set()
    years = set()
    for i in data:
        if i[YEAR] not in years:
            years.add(i[YEAR])
            for collums in i.keys():
                cols.add(collums)
    cols.remove(YEAR)
    return cols

def allRowsForCountry(data, country):
    return (list(filter(lambda x: x[COUNTRY] == country, data)))

def allRowsForRegion(data, region):
    return (list(filter(lambda x: x[REGION] == region, data)))

"""data = []
for i in range(2008, 2022):
    readFileToData(data, "Assets/" + str(i) + ".csv")
print(allRowsByYearRange(data, 2008, 2009))"""

#readFileToData(data, 'Assets/2016.csv')
#print(allRowsForCountry(data, "Malaysia"))
#list of dictionary [{Country: "", etc}]
#print(allCountriesForRegion(data, "Southeastern Asia"))
#print(getYear('Assets/2015.csv'))
