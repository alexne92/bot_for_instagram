from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import glob
import os
import json
import sys
from datetime import date


def open_browser(current_directory, instagram_username, instagram_password):
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
    pass

if __name__ == '__main__':
    #Retrieve the hashtags
    hashtags = [str(argument) for argument in sys.argv[1:]]
    if len(hashtags) == 0:
        print("Please import hashtags!")
        sys.exit(1)
    print("You have imported the following hashtags:")
    for hashtag in hashtags:
        print(hashtag)
    today = date.today()
    date = today.strftime("%d/%m/%Y")
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
    # Go to Instagram feed
    open_browser(current_directory, instagram_username, instagram_password)
	# read the file with data from previous imports
    if not os.path.exists("data"):
        os.makedirs("data")
        print("New directory for data has been created!")
    csv_dir = "data/insta_data.csv"
    if not os.path.isfile(csv_dir):
        empty_df = pd.DataFrame(columns=['id', 'user', 'date_of_load'])
        empty_df.to_csv(current_directory + "/" + csv_dir, index=False)
        print("Csv file has been created!")
    else:
        print("Scan found previous data")
    df = pd.read_csv(current_directory + "/" + csv_dir, delimiter=',')
    # Retrieve the previous users
    prev_user_list = list(df['user'])
    # Find the last id
    prev_id = list(df['id'])
    if len(prev_id) == 0:
        new_id = 0
    else:
        new_id = prev_id[-1] + 1
    # Initiate values for followers and likes
    new_followed = []
    likes = 0	
    for hashtag in hashtags:
        webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag + '/')
        sleep(5)
        first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
        first_thumbnail.click()
        try:
            for x in range(1,30):
                sleep(randint(3,4))
                user = webdriver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text
                # If the user is not in the previous user list and he hasn't uploaded something more than once
                if user not in prev_user_list and user not in new_followed:
                    if webdriver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                        webdriver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                        sleep(2)
                        # Like the content
                        button_like = webdriver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')
                        button_like.click()
                        likes += 1
                        new_followed.append(user)
                        df = df.append({'id' : new_id , 'user' : user, 'date_of_load': date} , ignore_index=True)
                        new_id += 1
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(2,4))
        except Exception as e:
            print("The following error occured:")
            print(e)
            continue
    sleep(2)
    df.to_csv(current_directory + "/" + csv_dir, index=False)
    print('Followed {} new people.'.format(len(new_followed)))
    print('Liked {} photos.'.format(likes))
    # Close the chrome webdriver
    webdriver.quit()

