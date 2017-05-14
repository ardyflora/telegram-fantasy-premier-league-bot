from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unicodedata,json,os
import re,sqlite3,time


playingXIDict = []
teamList = ["SOU","MID","STK","HUL","LEI","CHE","LIV","WBA","TOT","EVE","BOU","BUR","SWA","MUN","WHU","SUN","WAT","CRY","MCI","ARS"]

driver = webdriver.Chrome()
#driver = webdriver.Chrome('/Users/ripudamanflora/Downloads/chromedriver')

# To distinguish between who is the captain, vice-captain
# and who are regular playing in playingXI
def findPlayerTitle(spn):
    # playerTitle elements in detail: 0 = Regular, 1 = Vice-Captain, 2 = Captain
    playerTitle=[0,1,2] 
    if str(spn.get_attribute("title")) == "Captain":
        return "Captain"
    elif str(spn.get_attribute("title")) == "Vice-Captain":
        return "Vice-captain"
    else:
        return "Regular"

def checkPlayerName(name1,name2,name3,name4):
    if name2 not in teamList:
        return name1+name2,name3,name4
    else:
        return name1,name2,name3

def scrapePlayersInfo(managerID, xpathParm, tagName, statusOfPlayers,managerName):
    elements = driver.find_element_by_xpath(xpathParm)
    elementList = elements.find_elements_by_tag_name(tagName)
    for elem in elementList[1:]:
        for spn in elem.find_elements_by_tag_name("span"):
            data = {}
            splitString = unicodedata.normalize('NFKD', elem.text).encode('ascii','ignore').split()

            playerInf = checkPlayerName(splitString[0],splitString[1],splitString[2],splitString[3])
            if re.search('[a-zA-Z]', splitString[0]):
                if re.search('[a-zA-Z]', splitString[1]) and splitString[1] not in teamList:
                    playerTitle = findPlayerTitle(spn)
                    c.execute("insert into playerInfo (PlayerTitle, StatusOfPlayer, ManagerID, ManagerName, PlayerName, Team, Points) values (?,?,?,?,?,?,?)", [
                               playerTitle, statusOfPlayers, managerID, managerName, playerInf[0],playerInf[1],playerInf[2]])

                else:
                    playerTitle = findPlayerTitle(spn)
                    c.execute("insert into playerInfo (PlayerTitle, StatusOfPlayer, ManagerID, ManagerName, PlayerName, Team, Points) values (?,?,?,?,?,?,?)", [
                               playerTitle, statusOfPlayers, managerID, managerName, playerInf[0],playerInf[1],playerInf[2]])

conn = sqlite3.connect('points.db')
c = conn.cursor()

#Delete all records 
c.execute("delete from playerInfo")

listOfPartialLink = c.execute('Select Rank,PartialLink,Manager from Points')

for elem in listOfPartialLink.fetchall():
    managerID = elem[0]
    managerName = elem[2]
    print "Manager id: ", managerID
    print "Manager name: ",managerName
    driver.get(elem[1])
    time.sleep(2)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'List View')))

    driver.find_element_by_partial_link_text('List View').click()

    #Pulling PlayingXI info and parsing it into json file
    scrapePlayersInfo(managerID, "//*[@id=\"ismr-detail\"]/div/div[1]/div","tr","playingXI",managerName)

    #Pulling Bench info and parsing it into json file
    scrapePlayersInfo(managerID, "//*[@id=\"ismr-detail\"]/div/div[2]/div","tr","bench",managerName)

    #Clearing the list 
    #playingXIDict[:] = []
conn.commit()
conn.close()

driver.quit()