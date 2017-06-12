"""
This file include 5 functions and a main portion. In main portion data
is readed from files and saved in a dictionary. And the in 5 functions
1st is to read data against each month and other 4 areone for each task
 including bonus task
"""

from datetime import date
from statistics import mean
import os.path
from termcolor import colored, cprint

from Weather import Weather

# This function take name of file actually that is data of a month.
# Return list of the weather object of this particular month

def read_data_of_a_month(name):
    days = []

    if os.path.exists('weatherdata/'+ name +'.txt'):
        print(name + " is processing ...")
        for line in open('weatherdata/'+ name +'.txt', 'r'):
            line_in_list_form = line.split(',')
            date_string = line_in_list_form[0]
            date_in_list_form = date_string.split('-')

            if date_in_list_form[0] not in ('PKT', 'PKST', '\n' , '<!'): # because 1st two lines and last line of file are not valid
                date_obj = date(year=int(date_in_list_form[0]), month=int(date_in_list_form[1]), day=int(date_in_list_form[2]))
                max_t = line_in_list_form[1]
                mean_t = line_in_list_form[2]
                min_t = line_in_list_form[3]
                dew_point = line_in_list_form[4]
                mean_dew = line_in_list_form[5]
                min_dew = line_in_list_form[6]
                max_humadity = line_in_list_form[7]
                mean_humadity = line_in_list_form[8]
                min_humadity = line_in_list_form[9]

                weather = Weather(date_obj, max_t, mean_t,min_t, dew_point, mean_dew, min_dew
                                  , max_humadity, mean_humadity, min_humadity)
                days.append(weather)

    return days


# This function is to display Highest tmperature, Lowest Temperature
# and most humid day with humidity against some given year (Task 1)
def display_high_temper_low_temper_most_humidity(year):

    global data     # make use of the data we had prepared in our main section
    global months   # make use of the months list we we had prepared in our main section
    given_year_data = data[year]

    # initialize each with 1st day of the year
    max_temp_day, min_temp_day, max_humid_day = data[year]['Jan'][0], data[year]['Jan'][0], data[year]['Jan'][0]

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



# This function is to print hightest average lowest average temperatures and average humadity
def display_averages_of_given_month(year,month):
    global data  # make use of the data we had prepared in our main section
    global months  # make use of the months list we we had prepared in our main section
    data_of_given_month = data[year][months[month-1]] # month - 1, because user will give numeric input and key in dictionary is like 'Jan'
    h_temps = [int(hT.maxTemperature) for hT in data_of_given_month]
    l_temps = [int(lT.minTemperature) for lT in data_of_given_month]
    hum = [int(hm.maxHumadity) for hm in data_of_given_month]

    print('Highest Average: {0}C '.format(mean(h_temps)))
    print('Lowest: {0}C'.format(mean(l_temps)))
    print('Humid: {0}%'.format(mean(hum)))


# This function is to  draw two horizontal bar charts on the
# console for the highest and lowest temperature on each day.
#  Highest in red and lowest in blue  For a given month(Task 3)
def draw_two_bar_charts_for_given_month(year,month):
    global data  # make use of the data we had prepared in our main section
    global months  # make use of the months list we we had prepared in our main section
    data_of_given_month = data[year][ months[month - 1]]  # month - 1, because user will give numeric input and key in dictionary is like 'Jan'

    for this_day in data_of_given_month:
        minTbar = colored('+' * int(this_day.minTemperature), 'blue')
        maxTbar = colored('+' * int(this_day.maxTemperature), 'red')
        print(str(this_day.date.day) + ':' +  maxTbar + '{0}C'.format(this_day.minTemperature))
        print(str(this_day.date.day) + ':' + minTbar + '{0}C'.format(this_day.minTemperature))


# This functio is to draw one horizontal bar chart on the
# console for the highest and lowest temperature on each day.
# Highest in red and lowest in blue  BONUS TASK
def draw_one_bar_chart_for_given_month(year,month):
    global data  # make use of the data we had prepared in our main section
    global months  # make use of the months list we we had prepared in our main section
    data_of_given_month = data[year][
        months[month - 1]]  # month - 1, because user will give numeric input and key in dictionary is like 'Jan'

    for this_day in data_of_given_month:
        minTbar = colored('+' * int(this_day.minTemperature), 'blue')
        maxTbar = colored('+' * int(this_day.maxTemperature),'red')
        print (str(this_day.date.day) + ':' + minTbar+maxTbar+'{0}C-{1}C'.format(this_day.minTemperature, this_day.maxTemperature))



# Main function is starting from here.
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# building a dictionary with year as key and each value against key is
# again a dictionary with month name as key. and in against month key
# there is a list of weather objects of that particular month
data = {year: {month : read_data_of_a_month('lahore_weather_'+repr(year)+'_'+month) for month in months} for year in range(1996,2012)}



print('\nTask 1:')
year = input("Please Enter Year: ")
display_high_temper_low_temper_most_humidity(int(year))




print('\nTask 2:')
year = input("Please Enter Year: ")
month = input("Please Enter Month (1,2,3): ")
display_averages_of_given_month(int(year), int(month))

print('\nTask 3:')
year = input("Please Enter Year: ")
month = input("Please Enter Month (1,2,3): ")
draw_two_bar_charts_for_given_month(int(year), int(month))

print('\nBONUS:')
year = input("Please Enter Year: ")
month = input("Please Enter Month (1,2,3): ")
draw_one_bar_chart_for_given_month(int(year),int(month))

