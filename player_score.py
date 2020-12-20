import requests
import re
from bs4 import BeautifulSoup

# Return the players Overall winrate
def winRate(content):
    return content.find('div', class_='Text').text
# Return Level
def getLevel(content):
    return content.find('span', class_='Level').text
# Return rank
def getRank(content):
    return content.find('div', class_='sub-tier__rank-tier').text
# Return LP
def getLP(content):
    return content.find('div', class_='sub-tier__league-point').text
# Return amount of wins 
def amountOfWins(content):
    return content.find('span', class_="win").text
# Return amount of losses
def amountOfLosses(content):
    return content.find('span', class_="lose").text
# Return amount of games
def amountOfGames(content):
    return content.find('span', class_="total").text
# Return kd ratio
def getKdRatio(content):
    return content.find('span', class_="KDARatio").text


# Returns Win rates of all champions played in current season  
def championWinrates(name):
    result = dict()
    names  = []
    ratios = []
    count  = 0
    link = "https://na.op.gg/summoner/champions/userName=" + name
    page = requests.get(link) 
    soup = BeautifulSoup(page.content, 'html.parser')

    for champion in soup.div.find_all('td', class_='ChampionName Cell'):
        names.append(champion.text)
        count = count + 1
    for ratio in soup.div.find_all('span', class_='WinRatio'):
        ratios.append(ratio.text)
    i = 0
    while i < count:
        result[names[i]] = ratios[i]
        i = i + 1
    return result
# Return 5 most played with friends
def friendList(content):
    friends = []
    for friend in content.div.find_all('td', class_='SummonerName Cell left_select_played_with_summoner'):
        friends.append(friend.text)
    return friends





