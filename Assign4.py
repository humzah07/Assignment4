# Course: CS 1026
# Date created: 22/11/22
# Date last modified: 12/12/22
# Name: Humzah Zahid Malik
# Description: Assignment 4 - Air Travel

"""In the Assign4.py, the following functions are used to extract all the info from airports.txt and flights.txt, and then
    the info is used to create class objects and is also used to find specific info as required in some functions. """


import csv
from Airport import *
from Flight import *

# allAirports holds all the Airport objects and allFlights holds all the Flight objects
allAirports = []
allFlights = {}

# these lists are used in the loadData functions to temporarily hold the info for 'airports.txt' and 'flights.txt' before creating class objects
oneList = []
list2 = []
list3 = []
originList = []
flightObjects = ''

# this functions extracts the data from the two .txt files and creates Airport or Flight objects
def loadData(airportFile, flightFile):
    try:
        airportObject = ''
        # this segment of code extracts all the info from the airport file and stores into a temporary list
        with open(airportFile, 'r', encoding='utf8') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                oneList.append(row)
            # this for loop removes all whitespaces from each line in the .txt file before creating Airport objects
            for item in oneList:
                for i in item:
                    list2.append(i.split(","))
                item[0], item[1], item[2] = item[0].strip(), item[1].strip(), item[2].strip()
                # the stripped line is then created into a airport object
                allAirports.append(Airport(item[0], item[2], item[1]))
                allFlights[item[0]] = []
        x = oneList.clear()
        x = list2.clear()
        # this segment of code extracts all the info from the airport file and stores into a temporary list
        with open(flightFile, 'r', encoding='utf8') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                oneList.append(row)
            # this for loop removes all whitespaces from each line in the .txt file before creating Flight objects
            for item in oneList:
                for i in item:
                    list2.append(i.split(","))
                item[0], item[1], item[2] = item[0].strip(), item[1].strip(), item[2].strip()
                x = item[0], item[1], item[2]
                list3.append(x)
        # in the following code, flight objects are created using the given Airport objects
        originObject = ''
        destinationObject = ''
        # the for loop iterates over each object in the list, finds the airport code, and appends to a temporary list
        for i in allAirports:
            for a in list3:
                if i._code in a[1]:
                    originList.append(a)
        # then this for loop is used to create flight objects by using the allAirports and the temporary lists.
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
        return True
    except:
        return False

# this functions returns the Airport object by the given code
def getAirportByCode(code):
    city = ''
    country = ''
    # this for loop iterates over each airport object and checks if the given code is in the airport code of the airport object
    for i in allAirports:
        # the airport object is returned if the given code is in the airport code
        if code in i._code:
            city = i._city
            country = i._country
    return Airport(code, city, country)


# this function returns all the city flights that have the given city in them
def findAllCityFlights(city):
    allCities = []
    # the for loop iterates over each flight object and checks if the given city parameter is in either or both origin and destination airport objects
    for key, value in allFlights.items():
        for i in range(len(value)):
            originCity = value[i]._origin
            destCity = value[i]._destination
            # if the city is in either or both, origin and destination airports, the flight object is appended to the list
            if originCity == city:
                allCities.append(value[i])
            if destCity == city:
                allCities.append(value[i])
    return allCities

# this function returns all the country flights that have the given city in them
def findAllCountryFlights(country):
    allCountries = []
    # the for loop iterates over each flight object and checks if the given country parameter is in either or both origin and destination airport objects
    for i in allFlights.values():
        for a in i:
            # if the country is in either or both, origin and destination airports, the flight object is appended to the list
            if country == a._originTwo:
                allCountries.append(a)
            if country == a._destinationTwo:
                allCountries.append(a)
    return allCountries


# this function returns if there is a direct flight between the origin and destination airports
def findFlightBetween(origAirport, destAirport):
    # these lists and variables are used to temporarily hold specific values throughout the following code
    directFLight = ''
    city = ''
    cityTwo = ''
    originFlights = []
    originFlightsTwo = []
    destinationFlights = []
    originX = []
    destinationX = []
    yesOrNO = ''
    finalList = []
    flightSet = []
    # the following code checks if there is a direct flight between the two given Airport objects

    # this for loop checks if the origin and destination cities of the given Airport objects are in the airport objects
    for i in allFlights:
        if origAirport._code == i:
            for i in allAirports:
                if origAirport._code == i._code:
                    city = i.getCity()
                if destAirport._code == i._code:
                    cityTwo = i.getCity()
    # this for loops iterates over each allFlights values, and checks if the origin and destination cities are in the flight object
    # if they are, then a statement is returned stating that there is a direct flight
    for i in allFlights.values():
        for a in i:
            if city in a._origin and cityTwo in a._destination:
                originFlights.append(a)
                directFLight = "Direct Flight: " + origAirport._code + " to " + destAirport._code
                return directFLight
    # if there is no direct flight, then the following code is implemented
    # the following code checks if there are any other airports that that can be used a stop between the origin and destination airports
    if originFlights == []:
        # the for loop checks for the all 'X' airports that could be used as connecting airports between the two origin and destination airports
        for i in allFlights.values():
            for a in i:
                if city in a._origin:
                    originX.append(a._destination)
                if cityTwo in a._destination:
                    destinationX.append(a._origin)
        # this for loop appends all the 'X' airports to a temporary list
        for i in originX:
            for a in destinationX:
                if i == a:
                    finalList.append(i)
        # this for loop appends all the 'X' airports code to a new list, and then converts the new list into a set
        for i in finalList:
            for a in allAirports:
                if i in a._city:
                    flightSet.append(a._code)
        xCodes = set(flightSet)
    # if there is no direct flight AND no connecting airport, then -1 is returned
    if finalList == []:
        return -1
    else:
        return xCodes

# this function finds the return flight
def findReturnFlight(firstFlight):
    originCity = firstFlight._origin
    destCity = firstFlight._destination
    int = ''
    yesOrNo = []
    # this for loop checks if there is any return flight from destination airport back to the origin airport
    for i in allFlights.values():
        for a in i:
            # if there is any flight, then flightobject is appended to a list
            if originCity == a._destination and destCity == a._origin:
                yesOrNo.append(a)

    # if there is no return flight, then the following code is implemented
    if yesOrNo == []:
        return -1
    else:
        return yesOrNo[0]

loadData("airports.txt", "flights.txt")
print(allFlights)
