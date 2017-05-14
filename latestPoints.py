from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unicodedata,json,os
import re
import sqlite3,time


conn = sqlite3.connect('points.db')
c = conn.cursor()


driver = webdriver.Chrome()

#Delete all records 
c.execute("delete from LatestPoints")

listOfPartialLink = c.execute('Select Manager,PartialLink from Points')

for elem in listOfPartialLink.fetchall():
	print "elem first: ",elem[0]
	print "elem second: ",elem[1]
	driver.get(elem[1])
	time.sleep(2)
	latestPoints = driver.find_element_by_xpath("//*[@id=\"ismr-scoreboard\"]/div/div[2]/div[1]/div[1]/div")
	c.execute("insert into LatestPoints (Manager, Points) values (?,?)", [
			elem[0],latestPoints.text.split('Reload')[0]])

	time.sleep(2)

conn.commit()
conn.close()

