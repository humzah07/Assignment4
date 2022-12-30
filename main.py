import csv
from Airport import *
from Flight import *

allAirports = []
allFlights = {}
# ---------------------------------------------------------------------------------------------------------------------
list = []
listTwo = []
originList = []
flightObjects = ''

def loadData(airportFile, flightFile):
    try:
        airportObject = ''
        # this segment of code extracts all the info from the two files and stores into the two lists
        with open(airportFile, 'r', encoding='utf8') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                list.append(row)
        for i in list:
            airportObject = Airport(i[0], i[2], i[1])
            allAirports.append(airportObject)
            allFlights[airportObject._code] = []
        with open(flightFile, 'r', encoding='utf8') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                listTwo.append(row)
        # ------------------------------------------------------------------------------------
        originObject = ''
        destinationObject = ''
        for i in allAirports:
            for a in listTwo:
                if i._code in a[1]:
                    originList.append(a)
        for i in originList:
            for a in allAirports:
                if i[1] in a._code:
                    originObject = a
                if i[2] in a._code:
                    destinationObject = a
                    flightObject = Flight(i[0], originObject, destinationObject)
                    flightObjects = flightObject
                    for b in allFlights:
                        if originObject._code in b:
                            allFlights[b].append(flightObject)
    except FileNotFoundError:
        print("File doesn't exist")
    except TypeError as e:
        print("the origin and destination must be airport objects")

def getAirportByCode(code):
    airport = ''
    city = ''
    country = ''
    flight = Airport(code, '', '')
    for i in allAirports:
        if code in i._code:
            city = i._city
            country = i._country
    flight = Airport(code, city, country)
    print(flight)

def findAllCityFlights(city):
    allCityFlights = []
    for i in flightObjects:
        if city == i._origin:
            allCityFlights.append(i)
        if city == i._destination:
            allCityFlights.append(i)
    print(allCityFlights)

def findAllCountryFlights(country):
    allCountries = []
    for i in flightObjects:
        if country == i._originTwo:
            allCountries.append(i)
        if country == i._destinationTwo:
            allCountries.append(i)
    print(allCountries)

def findFlightBetween(origAirport, destAirport):
    print(origAirport)
    print(destAirport)
    for i in allAirports:
        5==5
        if origAirport == i:
            5 ==5

def findReturnFlight(firstFlight):
    originCity = firstFlight._origin
    destinationCity = firstFlight._destination
    originCity2 = ''
    destinationCity2 = ''
    yesOrNo = ''
    print(originCity)
    print(destinationCity)
    for i in allFlights.values():
        for a in i:
            if originCity == a._destination and destinationCity2 == a._origin:
                print(a)
            else:
               yesOrNo = -1
    print(yesOrNo)


loadData("airports.txt", "flights.txt")
getAirportByCode("LHR")
findAllCityFlights("Toronto")
findFlightBetween(getAirportByCode("PVG"), getAirportByCode("YOW"))
flight = Flight("BCS101", Airport("ABQ", "Toronto", "United States"), Airport("OMA", "Omaha", "United States"))
