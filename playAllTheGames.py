"""
Randomizes which steam game to play based on a list of games unplayed
"""
import re
import random
import urllib2
import bs4
from config import SteamAPIKey
from xml.dom import minidom
import json

usernameURL = "https://steamcommunity.com/id/%s/?xml=1"
gamesURL = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=%s&steamid=%s&format=json"
def getcommunityid(username):

    sanuser = re.sub(r'\W+', '', username)
    dom = minidom.parse(urllib2.urlopen(usernameURL % sanuser))
    return dom.getElementsByTagName("steamID64")[0].firstChild.data


def randomunplayedgame(communityid):
    sancommunityid = re.sub(r'\W+', '', communityid)
    url = gamesURL % (SteamAPIKey, sancommunityid)
    data = urllib2.urlopen(url)
    games = json.loads(data.read())
    unplayed = []
    for game in games['response']['games']:
        if game['playtime_forever'] == 0:
            unplayed.append(game['appid'])
    randgameid = random.choice(unplayed)
    # Hacky way to pull the game name, i couldnt find a way to do it with the API
    # TODO: Fix this, importing another lib for this task makes me sad :(
    title = bs4.BeautifulSoup(urllib2.urlopen('https://steamcommunity.com/app/%s' % randgameid)).html.title
    return str(title).split(':: ')[1].split('<')[0]


if __name__ == "__main__":
    username = "r3cursive"
    communityID = getcommunityid(username)
    print randomunplayedgame(communityID)