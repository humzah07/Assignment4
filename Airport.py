""" In Airport.py, a class is made to create the Airport objects for the airports.txt  """

class Airport:
    # the class is initialized through the instance variables through the function parameters in the following code
    def __init__(self, code, city, country):
        _code = ""
        _city = ""
        _country = ""
        self._code = code
        self._city = city
        self._country = country

    # this function returns the representation of the given airport object
    def __repr__(self):
        rep = self._code + ' (' + self._city + ', ' + self._country + ")"
        return rep

    # this function returns the Airport code for the given airport object
    def getCode(self):
        return f"{self._code}"

    # this function returns the city for the given airport object
    def getCity(self):
        return f"{self._city}"

    # this function returns the country for the given airport object
    def getCountry(self):
        return f"{self._country}"

    # this function updates the city for the given airport object
    def setCity(self, city):
        self._city = city

    # this function updates the country for the given airport object
    def setCountry(self, country):
        self._country = country
