#Helper file imports
from player_score import *
#Librarys
import requests
from bs4 import BeautifulSoup

#Global values
#used to send to helper values to get data
summonerName = ""

#
def scrape(name):
  summonerName = name
  link = 'https://na.op.gg/summoner/userName=' + summonerName
  # scrape page content with created link
  page = requests.get(link) 
  soup = BeautifulSoup(page.content, 'html.parser')
  return soup

#Queries
def setSummonerName(name): #Client chooses summoner name
  return scrape(name)

#Used to see everything about a player
def summonerReview(name):
  data = scrape(name)
  winRatio = winRate(data)
  championStats = championWinrates(name)
  kda = getKdRatio(data)
  print(name + "'s Statistics:")
  print("Win Ratio: " + winRatio)
  print("Kill Death Ratio: " + kda)
  print("Champion Statistics: " )
  print(championStats)
