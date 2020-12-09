from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from random import randrange
from time import sleep


print("Welcome to Ehouse's Yolo Spammer!")
link = input("Link to yolo:")
numOfMs = input("Number of messages(Defualt is 150):")
Ms = input("Message:")

print("Starting chrome...")
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options = options)

if numOfMs == '':
    numOfMs = 150

def spammer():
    global link, numOfMs, Ms
    print("Loading in...")
    driver.get(link)
    sleep(1)
    print("Starting spams...")
    for i in range(int(numOfMs)):
        driver.find_element_by_xpath('/html/body/div[4]/form/textarea').click()
        driver.find_element_by_xpath('/html/body/div[4]/form/textarea').send_keys(Ms)
        driver.find_element_by_xpath('/html/body/div[4]/form/div[1]').click()
        sleep(1)
        driver.get(link)
        sleep(0.5)
        print(f"Spam number {i} complete")
print("Spams complete. See you next time!")
spammer()