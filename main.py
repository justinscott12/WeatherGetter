# Based off of code from :
# https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/

# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required module
import requests
import sys
import RPi.GPIO as GPIO
import time
from RPLCD import CharLCD
from RPi import GPIO

# Enter your API key here 
api_key = "f7a73ffed4960413a86a299bc089559f"

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name 
city_name = input('')

# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

# get method of requests module 
# return response object 
response = requests.get(complete_url) 

# json method of response object 
x = response.json() 

# Now x contains list of nested dictionaries  
# city is not found 
if x["cod"] != "404": 

	# store the value of "main"  
	y = x["main"] 

	# store the value corresponding 
	current_temperature = int((y["temp"] -273) * (9/5) + 32)

	# store the value corresponding  
	current_humidity = y["humidity"] 

	# store the value of "weather"
	z = x["weather"] 

	# store the value corresponding 
	weather_description = z[0]["description"]
	if weather_description == 'scattered clouds' or 'overcast clouds':weather_description = 'cloudy'
        

	# print corresponding values
	print(" Temperature (in farenheight) = " +
					str(current_temperature) +
		"\n Humidity (in %) = " +
					str(current_humidity) +
		"\n Description = " +
					str(weather_description)) 

else: 
	print(" City Not Found ")
	

GPIO.setwarnings(False)

lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
lcd.cursor_pos = (0, 0) 
lcd.write_string('Temp:' + str(current_temperature) + '°')
lcd.cursor_pos = (0, 9)
lcd.write_string('Hum:' + str(current_humidity) + '%')
lcd.cursor_pos = (1, 0)
lcd.write_string('State:' + str(weather_description))