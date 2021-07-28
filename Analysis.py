import DataProcessing as DP
import functools as FT

def getMaxRowByColumn(data, column):
    return (FT.reduce(lambda max, current: current if float(current[column]) > float(max[column]) else max, data))

def getMinRowByColumn(data, column):
    return (FT.reduce(lambda min, current: current if float(current[column]) < float(min[column]) else min, data))

def allValuesOfCountryByRange(data, country, startYear, endYear, column):
    dic = {}
    contryByYearRange = (DP.allRowsForCountry(DP.allRowsByYearRange(data, startYear, endYear), country))
    for row in contryByYearRange:
        dic[row[DP.YEAR]] = row[column]
    return dic

def avgValueOfCountryByRange(data, country, startYear, endYear, column):
    contryByYearRange = (DP.allRowsForCountry(DP.allRowsByYearRange(data, startYear, endYear), country))
    return FT.reduce(lambda a, b: a + float(b[column]), contryByYearRange, 0.0) / len(contryByYearRange)

def allAvgValuesOfRegionByRange(data, region, startYear, endYear, column):
    dic = {}
    regionByYearRange = DP.allRowsForRegion(DP.allRowsByYearRange(data, startYear, endYear), region)
    for year in range(startYear, endYear + 1):
        allCountries = list(filter(lambda x: int(x[DP.YEAR]) == year and x[column], regionByYearRange))
        dic[year] = FT.reduce(lambda a, b: a + float(b[column]), allCountries, 0.0) / len(allCountries)
    return dic

def avgValueOfRegionByRange(data, region, startYear, endYear, column):
    regionByYearRange = (DP.allRowsForRegion(DP.allRowsByYearRange(data, startYear, endYear), region))
    return FT.reduce(lambda a, b: a if not b[column] else a + float(b[column]), regionByYearRange, 0.0) / len(regionByYearRange)

data = []
for i in range(2008, 2022):
    DP.readFileToData(data, "Assets/" + str(i) + ".csv")
column = "Trust (Government Corruption)"
"""print(avgValueOfRegionByRange(data, "Southeast Asia", 2008, 2018, column))
print(allAvgValuesOfRegionByRange(data, "Southeast Asia", 2008, 2018, column))
print("Malaysia average", avgValueOfCountryByRange(data, "Malaysia", 2008, 2018, column))
print("Singapore average", avgValueOfCountryByRange(data, "Singapore", 2008, 2018, column))
print("Malaysia", allValuesOfCountryByRange(data, "Malaysia", 2008, 2009, column))
print("Singapore", allValuesOfCountryByRange(data, "Singapore", 2008, 2009, column))
print("Government Trust Max:", getMaxRowByColumn(data, "Trust (Government Corruption)"), "\n")
print("Government Trust Min:", getMinRowByColumn(data, "Trust (Government Corruption)"), "\n")
print("Family Max:", getMaxRowByColumn(data, "Family"), "\n")
print("Family Min:", getMinRowByColumn(data, "Family"), "\n")
print("Health (Life Expectancy) Max:", getMaxRowByColumn(data, "Health (Life Expectancy)"), "\n")
print("Health (Life Expectancy) Min:", getMinRowByColumn(data, "Health (Life Expectancy)"), "\n")
print("Freedom Max:", getMaxRowByColumn(data, "Freedom"), "\n")
print("Freedom Min:", getMinRowByColumn(data, "Freedom"), "\n")"""
