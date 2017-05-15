# telegram-fantasy-premier-league-bot

> A Telegram bot that gives you the latest fantasy premier league scores for the league.

Some of the cool features:
* **/whohas** <_playername_> - List all the manager who have a certain player
* **/points** - display latest point table
* **/captains** - display all the captain in the league

Please refer to screenshots below to see `telegram-fantasy-premier-league-bot` in action:

###### `/captains` in action
<img src="https://snag.gy/LCMoPv.jpg" width="400">

###### `/points` in action
<img src="https://snag.gy/CZFKLv.jpg" width="400">

## Benefits
* You don't have to browse through the *fantasy premier league website* to find the latest points for each manager, with just one command you will get the immediate update.
* whohas makes it easy for the user to just simply use one command `/whohas <playerName>` instead of going through on each and every manager page one by one which is very time consuming and frustrating. In a smaller league with 10 Manager that will probably take about 7 minutes but with this feature, output will be in seconds. 
* `/captains` again is an amazing feature that gives you list of all the captains with one command 


## Features to be added
* `/benchpoints` - will give a list of manager with total bench points

## Installation
* You will need to install python telegram bot
  * Please follow the link:  
    https://github.com/python-telegram-bot/python-telegram-bot
* PrettyTable - Which is used to display the result as shown in the **telegram Ipl cricket score bot screenshot** above
   * To install PrettyTable, Please follow: https://pypi.python.org/pypi/PrettyTable
* selenium - which is used to scrape premierleague website
   * To install selenium, Please follow: http://selenium-python.readthedocs.io/installation.html

## How to Execute?
* Execute in following order:
  
  `python database.py` - This will create the *points.db* file. 

  `python leagueTable.py` - This will insert iplPoint Table into points.db

  `python latestPoints.py` - This will insert points Tables into points.db'
  
  `python playerInfo.py` - This will insert playerInfo Table into points.db

  `python interface.py` - Once this is running, you can go to telegram and open **Fantasypremierleague bot** where you can type `/start` to start the telegram bot, it should return *_I'm a bot, please talk to me!_*. Once you can see  that, you can run any of the the commands specified above such as  `/points`, `/whohas <playerName>` or `/captains`

## Release History
* 0.0.1
    * Work in progress

## Meta

Ardy Flora – flora_ripudaman@hotmail.com

Distributed under the MIT license. See ``LICENSE.txt`` for more information.

[https://github.com/ardyflora/telegram-fantasy-premier-league-bot](https://github.com/ardyflora/)

## Contributing

1. Fork it (<https://github.com/ardyflora/telegram-fantasy-premier-league-bot>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
