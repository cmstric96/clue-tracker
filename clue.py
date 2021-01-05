# Initialize variables
per = ['Mustard', 'Plum', 'Green', 'Peacock', 'Scarlet', 'White']
wea = ['Knife', 'Candlestick', 'Pistol', 'Poison', 'Trophy', 'Rope', \
       'Bat', 'Ax', 'Dumbbell']
roo = ['Hall', 'Dining', 'Kitchen', 'Patio', 'Observatory', 'Theater', \
       'Living', 'Spa', 'Guest']
allcards = per + wea + roo
allcardsnc = per + wea + roo

global poolcards
rumours = []
poolcards = []
notowned = []
players = []

# Initialize classes and functions
class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.rumoursd = []
        self.rumoursa = []

class Rumour():
    def __init__(self, p, g, w, r, s, sb):
        self.shown = s
        self.person = p
        self.guest = g
        self.weapon = w
        self.room = r
        self.shownby = sb
        if self.shown == '0':
            self.rumour = p + ' started a rumour that ' + g \
                          + ' killed someone with the ' + w \
                          + ' in the ' + r + ' and was shown a ' \
                          + 'card by ' + players[int(sb)].name
        else:
            self.rumour = p + ' started the rumour that ' + g + \
                          ' killed someone with the ' + w + \
                          ' in the ' + r

# Main loop
def MainLoop():
    global poolcards
    while True:
        tempnum = 0
        for i in range(0, len(per)):
            if per[i] in allcards:
                tempnum += 1
        if tempnum == 1:
            for i in range(0, len(per)):
                if per[i] in allcards:
                    poolcards.append(per[i])
                    allcards.remove(per[i])
        tempnum = 0
        for i in range(0, len(wea)):
            if wea[i] in allcards:
                tempnum += 1
        if tempnum == 1:
            for i in range(0, len(wea)):
                if wea[i] in allcards:
                    poolcards.append(wea[i])
                    allcards.remove(wea[i])
        tempnum = 0
        for i in range(0, len(roo)):
            if roo[i] in allcards:
                tempnum += 1
        if tempnum == 1:
            for i in range(0, len(roo)):
                if roo[i] in allcards:
                    poolcards.append(roo[i])
                    allcards.remove(roo[i])
        if len(allcards) == 3:
            poolcards = allcards
        if len(poolcards) == 3:
            print()
            print('Go to the pool. Cards are: ' + poolcards[0] + ', ' + poolcards[1] + ', ' + poolcards[2])
        MainMenu()
                
def Error():
    print()
    print('Error')
    print()

def AddCards():
    try:
        for i in range(0, len(players)):
            print(str(i) + ': ' + players[i].name)
        print(str(len(players)) + ': Free card')
        addingplayer = input('Player: ')
        for i in range(0, len(allcards)):
            print(str(i) + ': ' + allcards[i])
        addingcard = input('Card: ')
        if int(addingplayer) == len(players):
            notowned.append(allcards[int(addingcard)])
        else:
            players[int(addingplayer)].cards.append(allcards[int(addingcard)])
        allcards.remove(allcards[int(addingcard)])
    except:
        MainLoop()
    
    
def MainMenu():
    # Load initial menu screen
    print()
    print('===================')
    print('     Main Menu')
    print('===================')
    print()
    # Get menu actions
    print('0: Your cards')
    print('1: Info sheet')
    print('2: Log rumour')
    print('3: Player info')
    print('4: Eliminate card')
    print('5: Make pool card')
    print('6: Card Statistics')
    action = input('Action: ')
    print()
    try:
        if action == '0':
            YourCards()
        elif action == '1':
            InfoSheet()
        elif action == '2':
            LogRumour()
        elif action == '3':
            PlayerInfo()
        elif action == '4':
            AddCards()
        elif action == '5':
            PoolizeCard()
        elif action == '6':
            PrintStatistics()
        else:
            Error()
    except:
        Error()
def YourCards():
    print('====================')
    print('     Your Cards')
    print('====================')
    print()
    print(str(players[0].cards))

def InfoSheet():
    playern = 0
    print('===================')
    print('    Info Sheet')
    print('===================')
    print()
    print('Cards:')
    for i in range(0, len(allcardsnc)):
        if i == 0:
            print('')
            print('Guests')
            print('===================')
        elif i == 6:
            print('')
            print('Weapons')
            print('===================')
        elif i == 15:
            print('')
            print('Rooms')
            print('===================')
        for k in range(0, len(players)):
                if allcardsnc[i] in players[k].cards:
                    owner = players[k].name
                    break
                elif allcardsnc[i] in notowned:
                    owner = 'Free Card'
                elif allcardsnc[i] in poolcards:
                    owner = 'Pool Card'
                else:
                    owner = ''
        print(str(i) + ': ' + allcardsnc[i] + ' - ' + owner)
    print()
    print('Rumours:')
    for i in range(0, len(rumours)):
        print(rumours[i].rumour)
    print()
    print('Pool Cards:')
    for i in range(0, len(poolcards)):
        print(poolcards[i])

def PrintStatistics():
    print('====================')
    print('     Card Statistics')
    print('====================')
    print('0: Guests')
    print('1: Weapons')
    print('2: Rooms')
    print('3: All Cards')
    action = input('Action: ')
    print()
    print('Card       |Owner      |Rumours    |Probs      |')
    print('-----------|-----------|-----------|-----------|')
    for i in range(0, len(allcardsnc)):
        Rumour = 0
        if allcardsnc[i] in per:
            Rumour = sum(p.guest == allcardsnc[i] and p.shown == '0' for p in rumours)
        elif allcardsnc[i] in wea:
            Rumour = sum(p.weapon == allcardsnc[i] and p.shown == '0' for p in rumours)
        elif allcardsnc[i] in roo:
            Rumour = sum(p.room == allcardsnc[i] and p.shown == '0' for p in rumours)
        for k in range(0, len(players)):
            if allcardsnc[i] in players[k].cards:
                owner = players[k].name
                Prob = 0
                break
            elif allcardsnc[i] in poolcards:
                owner = 'Pool Card'
                Prob = 1
            else:
                owner = ''
                if allcardsnc[i] in per:
                    Prob = round(1/(sum(el in per for el in allcards)),5)
                elif allcardsnc[i] in wea:
                    Prob = round(1/(sum(el in wea for el in allcards)),5)
                elif allcardsnc[i] in roo:
                    Prob = round(1/(sum(el in roo for el in allcards)),5)
        #print(f'{allcardsnc[i]:11}|{owner:11}|{Rumour:11}|{Prob:11}|')
        if action == '0':
            if allcardsnc[i] in per:
                print(f'{allcardsnc[i]:11}|{owner:11}|{Rumour:11}|{Prob:11}|')
        elif action == '1':
            if allcardsnc[i] in wea:
                print(f'{allcardsnc[i]:11}|{owner:11}|{Rumour:11}|{Prob:11}|')
        elif action == '2':
            if allcardsnc[i] in roo:
                print(f'{allcardsnc[i]:11}|{owner:11}|{Rumour:11}|{Prob:11}|')
        elif action == '3':
            print(f'{allcardsnc[i]:11}|{owner:11}|{Rumour:11}|{Prob:11}|')
        else:
            error()

def LogRumour():
    numcardsbefore = len(players[0].cards)
    print('====================')
    print('     Log Rumour')
    print('====================')
    print()
    # Player making the rumour
    playernum = 0
    for i in range(0, len(players)):
        print(str(playernum) + ': ' + players[playernum].name)
        playernum += 1
    playern = input('Player: ')
    while int(playern) not in range(0, len(players)):
        Error()
        playernum = 0
        for i in range(0, len(players)):
            print(str(playernum) + ': ' + players[playernum].name)
            playernum += 1
        playern = input('Player: ')
    player = players[int(playern)].name
    print()
    # Guest in the rumour
    cardnum = 0
    for i in range(0, len(per)):
        print(str(cardnum) + ': ' + per[cardnum])
        cardnum += 1
    guest = input('Guest: ')
    while int(guest) not in range(0, len(per)):
        Error()
        for i in range(0, len(per)):
            print(str(cardnum) + ': ' + per[cardnum])
            cardnum += 1
        guest = input('Guest: ')
    guest = per[int(guest)]
    print()
    # Weapon in the rumour
    cardnum = 0
    for i in range(0, len(wea)):
        print(str(cardnum) + ': ' + wea[cardnum])
        cardnum += 1
    weapon = input('Weapon: ')
    while int(weapon) not in range(0, len(wea)):
        Error()
        cardnum = 0
        for i in range(0, len(wea)):
            print(str(cardnum) + ': ' + wea[cardnum])
            cardnum += 1
        weapon = input('Weapon: ')
    weapon = wea[int(weapon)]
    # Room in the rumour
    cardnum = 0
    for i in range(0, len(roo)):
        print(str(cardnum) + ': ' + roo[cardnum])
        cardnum += 1
    room = input('Room: ')
    while int(room) not in range(0, len(roo)):
        Error()
        cardnum = 0
        for i in range(0, len(roo)):
            print(str(cardnum) + ': ' + roo[cardnum])
            cardnum += 1
        room = input('Room: ')
    room = roo[int(room)]
    # Was player?
    if playern == '0':
        print()
        print('0: Yes')
        print('1: No')
        shown = input('Were you shown a card? ')
        # Shown card?
        if shown == '0':
            print()
            for i in range(1, len(players)):
                print(str(i) + ': ' + players[i].name)
            shownby = input('Who showed you the card? ')
            print()
            if guest in allcards:
                print('0: ' + guest)
            if weapon in allcards:
                print('1: ' + weapon)
            if room in allcards:
                print('2: ' + room)
            card = input('What card did they show you? ')
            if card == '0':
                card = guest
            elif card == '1':
                card = weapon
            elif card == '2':
                card = room

            players[int(shownby)].cards.append(card)
            allcards.remove(card)
        else:
            shownby = 0
    else:
        print()
        print('0: Yes')
        print('1: No')
        shown = input('Were they shown a card? ')
        if shown == '0':
            print()
            for i in range(0, len(players)):
                print(str(i) + ': ' + players[i].name)
            shownby = input('Who showed the card? ')
        else:
            shownby = 0
    rumour = Rumour(player, guest, weapon, room, shown, shownby)
    rumours.append(rumour)
    players[int(playern)].rumoursd.append(rumour.rumour)
    print()
    print('0: Yes')
    print('1: No')
    submit = input('Are you sure you want to go through with this rumour? ')
    if submit == '1':
        MainMenu()
    # Analyze rumour
    if len(players[0].cards) == numcardsbefore:
        if shown == '0':
            players[int(shownby)].rumoursa.append(rumour.rumour)
        if guest in players[int(playern)].cards and weapon in players[int(playern)].cards and shown == '0':
            rgw = room
        elif weapon in players[int(playern)].cards and room in players[int(playern)].cards and shown == '0':
            rgw = guest
        elif guest in players[int(playern)].cards and room not in players[int(playern)].cards and shown == '0':
            rgw = weapon
        else:
            rgw = ''
    ##    for i in range(0, len(rumours)):
    ##        if 
        if guest not in allcards and weapon not in allcards and shown == '1':
            if room not in poolcards:
                poolcards.append(room)
                allcards.remove(room)
        elif weapon not in allcards and room not in allcards and shown == '1':
            if guest not in poolcards:
                poolcards.append(guest)
                allcards.remove(guest)
        elif guest not in allcards and room not in allcards and shown == '1':
            if weapon not in poolcards:
                poolcards.append(weapon)
                allcards.remove(weapon)
        if rgw not in players[int(shownby)].cards and rgw != '':
            players[int(shownby)].cards.append(rgw)

def PlayerInfo():
    print('=====================')
    print('     Player Info     ')
    print('=====================')
    print()
    for i in range(0, len(players)):
        print(str(i) + ': ' + players[i].name)
    player = input('Player: ')
    print()
    print('Cards:')
    print('===========')
    print('Guests')
    print('------------')
    for i in range(0, len(players[int(player)].cards)):
        if(players[int(player)].cards[i]) in per:
            print(players[int(player)].cards[i])
    print('Weapons')
    print('------------')
    for i in range(0, len(players[int(player)].cards)):
        if(players[int(player)].cards[i]) in wea:
            print(players[int(player)].cards[i])
    print('Rooms')
    print('------------')
    for i in range(0, len(players[int(player)].cards)):
        if(players[int(player)].cards[i]) in roo:
            print(players[int(player)].cards[i])  
    print('===========')
    print()
    print('Rumours Started:')
    print('============')
    for i in range(0, len(players[int(player)].rumoursd)):
        print(players[int(player)].rumoursd[i])
    print('============')
    print()
    print('Rumours Answered:')
    print('=====================')
    for i in range(0, len(players[int(player)].rumoursa)):
        print(players[int(player)].rumoursa[i])
    print('=====================')

def PoolizeCard():
    for i in range(0, len(allcards)):
        print(str(i) + ': ' + allcards[i])
    poolizingcard = input('Card: ')
    poolcards.append(allcards[int(poolizingcard)])
    allcards.remove(allcards[int(poolizingcard)])

print('===========================================')
print('             Enter player name')
print('*Enter a blank line to stop entering names*')
print('===========================================')

playernum = 0
while True:
    name = input('Player #' + str(playernum) + ' (You are player 0): ')
    if name == '':
        if len(players) > 1:
            break
        else:
            print()
            print('You need at least two players to play!')
            print()
    else:
        player = Player(name)
        players.append(player)
    playernum += 1

# Get cards
print()
print('===========================================')
print('             Enter card number')
print('*Enter a blank line to stop entering cards*')
print('===========================================')
while True:
    cardnum = 0
    for i in range(0, len(allcards)):
        print(str(cardnum) + ': ' + allcards[cardnum])
        cardnum += 1
    print()
    print('Your cards: ' + str(players[0].cards))
    card = input('Card: ')
    if card == '':
        break
    elif int(card) >= 0 and int(card) <= len(allcards) - 1:
        players[0].cards.append(allcards[int(card)])
        allcards.remove(allcards[int(card)])
    else:
        Error()

MainLoop()