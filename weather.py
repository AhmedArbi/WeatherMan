"""
This class is to store weather data.
it contains all variables that are in weather file are data members here.
"""


class Weather:

    def __init__(self, d, maxT, meanT, minT, dewPoint,
                 meanD, minD, maxH, meanH, minH):
        self.date = d
        self.maxTemperature = maxT
        self.meanTemperature = meanT
        self.minTemperature = minT
        self.dewPoint = dewPoint
        self.meanDewPoint = meanD
        self.minDewPoint = minD
        self.maxHumadity = maxH
        self.meanHumadity = meanH
        self.minHumadity = minH