"""

"""

from datetime import date
import os.path
from Weather import Weather

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

# Main function is starting from here.



months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# building a dictionary with year as key and each value against key is
# again a dictionary with month name as key. and in against month key
# there is a list of weather objects

data = {year: {month : read_data_of_a_month('lahore_weather_'+repr(year)+'_'+month) for month in months} for year in range(1996,2012)}

print (data[1997]['Jan'][0])

