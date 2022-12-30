""" In Flight.py, a class is made to create the flight objects from the given airport objects from
  Airport.py, and from flights.txt"""
\

from Airport import *

class Flight:
    def __init__(self, flightNo, origin, destination):
        _flightNo = ""
        _origin = ""
        _destination = ""
        sameCountry = ""
        diffCountry = ""
        # the following code checks if the given 'origin' and 'destinations' parameters are Airport objects
        if isinstance(origin, Airport) and isinstance(destination, Airport):
            # if the parameters are airport objects, the class is initialized through the instance variables
            self._flightNo = flightNo
            self._origin = origin.getCity()     # this variable gets the origin city from the airport object
            self._destination = destination.getCity()   # this variable gets the destination city from the airport object
            self._originTwo = origin.getCountry()   # this variable gets the origin country from the airport object
            self._destinationTwo = destination.getCountry()    # this variable gets the destination country from the airport object
            self._originThree = origin.getCode()    # this variable gets the origin airport code from the airport object
            self._destinationThree = origin.getCode()    # this variable gets the destination airport code from the airport object
        else:
            # if the origin and destination are not airport objects, then TypeError is raised
            raise TypeError("The origin and destination must be Airport objects")

    # this function returns the representation of the given airport object
    def __repr__(self):
        # if the flight is domestic, the following representation is returned
        if self.isDomesticFlight() == True:
            rep = "Flight: " + self._flightNo + ' from ' + self._origin + ' to ' + self._destination + " {Domestic}"
            return rep
        # if the flight is international, the following representation is returned
        if self.isDomesticFlight() == False:
            rep = "Flight: " + self._flightNo + ' from ' + self._origin + ' to ' + self._destination + " {International}"
            return rep
    # this function checks if 'other' object and the flight object are the same flight
    def __eq__(self, other):
        # the isinstance checks if the 'other' and 'Flight' are flight objects
        if isinstance(other, Flight):
            # this if statement checks if the origin and destination cities for both of these objects are same or not
            if self._origin == other._origin and self._destination == other._destination:
                return "yes"
            else:
                print("They are not the same flights")
        else:
            print("False")

    # this function returns the flight number for the given flight object
    def getFlightNumber(self):
        return f"{self._flightNo}"

    # this function returns the origin city for the given flight object
    def getOrigin(self):
        return f"{self._origin}"

    # this function returns the destination city for the given flight object
    def getDestination(self):
        return f"{self._destination}"

    def isDomesticFlight(self):
        if self._originTwo == self._destinationTwo:
            sameCountry = "{Domestic}"
            return True
        else:
            diffCountry = "{International}"
            return False

    # this function returns the flight Origin for the given flight object
    def setOrigin(self, origin):
        self._origin = origin

    # this function returns the flight Destination for the given flight object
    def setDestination(self, destination):
        self._destionation = destination
