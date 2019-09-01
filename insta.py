from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import glob
import os
import json
import sys


if __name__ == '__main__':

	hastags = [str(argument) for argument in sys.argv[1:]]
	
	if len(hastags) == 0:
		print("Please import hashtags!")
		sys.exit(1)
	
	print(hastags)

	# Get working directory
	current_directory = os.getcwd()

	# Get your instagram credentials from the .json file
	with open(current_directory + '/credentials.json', 'r') as f:
		credentials_dict = json.load(f)

	for key,val in credentials_dict.items():
		exec(key + '=val')

	# Set the chrome webdriver
	chromedriver_path = current_directory + '/chromedriver.exe'
	webdriver = webdriver.Chrome(executable_path=chromedriver_path)
	sleep(2)

	# Log in to instagram
	webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
	sleep(3)
	username = webdriver.find_element_by_name('username')
	username.send_keys(instagram_username)
	password = webdriver.find_element_by_name('password')
	password.send_keys(instagram_password)
	password.send_keys(Keys.ENTER)
	sleep(3)

	# In case you get a pop up asking you about notifications, use the next two lines, otherwise comment them out
	notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
	notnow.click()

	sleep(2)
	# Close the chrome webdriver
	webdriver.quit()

