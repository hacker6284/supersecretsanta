import urllib.request as requests
import urllib.parse as parse
from random import shuffle
import random

#define method of contacting people
def ifttt(name, value1, value2, value3, key):
    payload = parse.urlencode({ 'value1' : value1,
                              'value2' : value2,
                              'value3' : value3}).encode()
    requests.urlopen(requests.Request("https://maker.ifttt.com/trigger/%s/with/key/%s"%(name, key), data=payload))

#dictionary of iFTTT trigger names and the corresponding plain text
names = {
'zoogs' 	: 'Zoogs (Zach)',
'spoopy' 	: 'Spoopy (Carlos)',
'snek' 		: 'Tex (Jake)',
'datebra' 	: "Date Bra (It's Cute) [Brianna]",
'iverson' 	: 'White Iverson (Ivy)',
'buzz' 		: 'Buzz Lightyear (Tim)',
'steve' 	: 'Kardigan (Kurtis)',
'garbandra' : 'Garbandra (Cassandra)',
'wolf' 		: 'Wolf Quest (Elise)',
'zepps' 	: 'Led Zeppelin (Tannor)'
}

#randomize the order of the cards
namesList = list(names.keys())
shuffle(namesList)

#choose a random shift
x = random.randint(1, len(namesList) - 1)

#duplicate the list
getList = list(namesList)

#shift second list by random shift amount
for y in range (0, x):
	getList.insert(0, getList.pop())

#honor Elise's request not to interact with Kurtis because you love her
if (getList[namesList.index('wolf')] == 'steve' or getList[namesList.index('steve')] == 'wolf' or getList[namesList.index('zoogs')] == 'zoogs'):
	getList.insert(0, getList.pop())

#send messages to all groups
for x in range(0, len(namesList)):
	#ifttt(namesList[x], names[getList[x]], "nothing", "nothing", "n1eehkzp81qCiI7RvdbnC3ixTJDOo-vuK915uujBA1D")
	ifttt('zoogs', names[namesList[x]] + names[getList[x]], "nothing", "nothing", "secret key")
