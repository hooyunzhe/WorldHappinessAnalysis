import DataProcessing as DP
import functools as FT

def getMaxRowByColumn(data, column):
    return (FT.reduce(lambda max, current: current if float(current[column]) > float(max[column]) else max, data))

def getMinRowByColumn(data, column):
    return (FT.reduce(lambda min, current: current if float(current[column]) < float(min[column]) else min, data))

data = []
DP.readFileToData(data, 'Assets/2015.csv')
print("Government Trust Max:", getMaxRowByColumn(data, "Trust (Government Corruption)"), "\n")
print("Government Trust Min:", getMinRowByColumn(data, "Trust (Government Corruption)"), "\n")
print("Family Max:", getMaxRowByColumn(data, "Family"), "\n")
print("Family Min:", getMinRowByColumn(data, "Family"), "\n")
print("Health (Life Expectancy) Max:", getMaxRowByColumn(data, "Health (Life Expectancy)"), "\n")
print("Health (Life Expectancy) Min:", getMinRowByColumn(data, "Health (Life Expectancy)"), "\n")
print("Freedom Max:", getMaxRowByColumn(data, "Freedom"), "\n")
print("Freedom Min:", getMinRowByColumn(data, "Freedom"), "\n")
