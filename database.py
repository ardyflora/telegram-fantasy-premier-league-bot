
import sqlite3


def create_points(c):
    c.execute('''CREATE TABLE Points
              (Rank integer, PartialLink text, Team text, Manager text,RoundScore integer, TotalScore integer)''')

def latestPoints(c):
	c.execute('''CREATE TABLE LatestPoints
              (Manager text, Points integer)''')
def playerInfo(c):
    c.execute('''CREATE table playerInfo
                 (PlayerTitle text, StatusOfPlayer text, ManagerID integer, ManagerName text, PlayerName text, Team text, Points text) ''')


def init_database():
    conn = sqlite3.connect('points.db')
    c = conn.cursor()
    create_points(c)
    latestPoints(c)
    playerInfo(c)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_database()
