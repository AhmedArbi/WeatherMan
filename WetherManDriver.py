"""
This file include WeatherManDriver class which have 5 functions and a main portion.
In main portion data is readed from files and saved in a dictionary. And the in 5
functions 1st is to read data against each month and other 4 areone for each task
including bonus task
"""

from datetime import date
from statistics import mean
import os.path
import sys
import csv
from termcolor import colored

from Weather import Weather

class WeatherManDriver:

    def _read_data_of_a_month(name):
        days = []
        if os.path.exists(sys.argv[3]+ '/' + name +'.txt'):
            with open(sys.argv[3] + '/' + name + '.txt', 'r') as f:
                reader = csv.reader(f)
                for i, line in enumerate(reader):
                    if i>1 and line[0][0] != '<':
                        date_string = line[0]
                        date_in_list_form = date_string.split('-')
                        date_obj = date(year=int(date_in_list_form[0]), month=int(date_in_list_form[1]), day=int(date_in_list_form[2]))
                        max_t = line[1]
                        mean_t = line[2]
                        min_t = line[3]
                        dew_point = line[4]
                        mean_dew = line[5]
                        min_dew = line[6]
                        max_humadity = line[7]
                        mean_humadity = line[8]
                        min_humadity = line[9]
                        weather = Weather(date_obj, max_t, mean_t,min_t, dew_point, mean_dew, min_dew, max_humadity, mean_humadity, min_humadity)
                        days.append(weather)
        else:
            print ('Searched File:'+sys.argv[3]+ '/' + name +'.txt')
            print("Error: Data file related to your query doesn\'t exists ..")
            exit()
        return days


    # This function is to display Highest tmperature, Lowest Temperature
    # and most humid day with humidity against some given year (Task 1)
    @staticmethod
    def display_high_temper_low_temper_most_humidity(year):
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        given_year_data = {month :WeatherManDriver._read_data_of_a_month('lahore_weather_'+repr(year)+'_'+month) for month in months }

        # initialize each with 1st day of the year
        max_temp_day, min_temp_day, max_humid_day = given_year_data['Jan'][0], given_year_data['Jan'][0], given_year_data['Jan'][0]

        for m in months:
            for this_day in given_year_data[m]:
                if max_temp_day.maxTemperature < this_day.maxTemperature:
                    max_temp_day = this_day

                if this_day.minTemperature and min_temp_day.minTemperature > this_day.minTemperature:
                    min_temp_day = this_day

                if max_humid_day.maxHumadity < this_day.maxHumadity:
                    max_humid_day = this_day

        print (date.strftime( max_temp_day.date, '%B %d'))
        print ('Highest: {0}C on {1}'.format(max_temp_day.maxTemperature, date.strftime( max_temp_day.date, '%B %d')))
        print ('Lowest: {0}C on {1}'.format(min_temp_day.minTemperature, date.strftime( min_temp_day.date, '%B %d')))
        print ('Humid: {0}% on {1}'.format(max_humid_day.maxHumadity,  date.strftime( max_humid_day.date, '%B %d')))



    # This function is to print hightest average lowest average temperatures and average humadity (Task 2)
    @staticmethod
    def display_averages_of_given_month(year,month):
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        data_of_given_month = WeatherManDriver._read_data_of_a_month('lahore_weather_'+repr(year)+ '_'+ months[month-1])

        h_temps = [int(hT.maxTemperature) for hT in data_of_given_month]
        l_temps = [int(lT.minTemperature) for lT in data_of_given_month]
        hum = [int(hm.maxHumadity) for hm in data_of_given_month]

        print('Highest Average: {0:.2f}C '.format(mean(h_temps)))
        print('Lowest: {0:.2f}C'.format(mean(l_temps)))
        print('Humid: {0:.2f}%'.format(mean(hum)))


    # This function is to  draw two horizontal bar charts on the
    # console for the highest and lowest temperature on each day.
    #  Highest in red and lowest in blue  For a given month(Task 3)
    @staticmethod
    def draw_two_bar_charts_for_given_month(year,month):
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        data_of_given_month = WeatherManDriver._read_data_of_a_month(
            'lahore_weather_' + repr(year) + '_' + months[month - 1])

        for this_day in data_of_given_month:
            minTbar = colored('+' * int(this_day.minTemperature), 'blue')
            maxTbar = colored('+' * int(this_day.maxTemperature), 'red')
            print(str(this_day.date.day) + ':' +  maxTbar + '{0}C'.format(this_day. maxTemperature))
            print(str(this_day.date.day) + ':' + minTbar + '{0}C'.format(this_day.minTemperature))


    # This functio is to draw one horizontal bar chart on the
    # console for the highest and lowest temperature on each day.
    # Highest in red and lowest in blue  BONUS TASK
    @staticmethod
    def draw_one_bar_chart_for_given_month(year,month):
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        data_of_given_month = WeatherManDriver._read_data_of_a_month(
            'lahore_weather_' + repr(year) + '_' + months[month - 1])

        for this_day in data_of_given_month:
            minTbar = colored('+' * int(this_day.minTemperature), 'blue')
            maxTbar = colored('+' * int(this_day.maxTemperature),'red')
            print (str(this_day.date.day) + ':' + minTbar+maxTbar+'{0}C-{1}C'.format(this_day.minTemperature, this_day.maxTemperature))



def main(arg):
    if arg.__len__() < 4:
        print ("Error: Arguments are not complete 3 arguments are required..")
        exit()

    task = arg[1]
    if task == '-e':
        WeatherManDriver.display_high_temper_low_temper_most_humidity(int(arg[2]))
    elif task == '-a':
        dateStr = str(arg[2])
        date_actual = dateStr.split('/')
        WeatherManDriver.display_averages_of_given_month(int(date_actual[0]), int(date_actual[1]))
    elif task == '-c':
        dateStr = str(arg[2])
        date_actual = dateStr.split('/')
        WeatherManDriver.draw_two_bar_charts_for_given_month(int(date_actual[0]), int(date_actual[1]))
    elif task == '-d':
        dateStr = str(arg[2])
        date_actual = dateStr.split('/')
        WeatherManDriver.draw_one_bar_chart_for_given_month(int(date_actual[0]), int(date_actual[1]))
    else:
        print("Error: Task name is not correct ..")
        exit()

if __name__ == '__main__':
    main(sys.argv)