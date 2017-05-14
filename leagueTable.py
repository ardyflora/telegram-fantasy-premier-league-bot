
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unicodedata,json,os
import re
import sqlite3

conn = sqlite3.connect('points.db')
c = conn.cursor()

driver = webdriver.Chrome()
driver.get("https://fantasy.premierleague.com/a/leagues/standings/123712/classic")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'ismr-classic-standings')))

leagueInfo = driver.find_elements_by_xpath("//*[@id=\"ismr-classic-standings\"]/div/div/table/tbody")

for player in leagueInfo:
	elements = player.find_elements_by_tag_name("tr")
	for elem in elements:
		empList = []
		for td in elem.find_elements_by_tag_name("td"):
			links = [am.get_attribute('href') for am in td.find_elements_by_tag_name('a') ]
			if links !=[]:
				empList.append(links[0])
			empList.append(td.text)

		c.execute("insert into Points (Rank, PartialLink, Team, Manager, RoundScore, TotalScore) values (?,?,?,?,?,?)", [
			empList[0],empList[1],empList[2].split('\n')[0],empList[2].split('\n')[1],empList[3],empList[4]])
            
            
conn.commit()
conn.close()
