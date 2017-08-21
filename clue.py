# Initialize variables
per = ['Mustard', 'Plum', 'Green', 'Peacock', 'Scarlet', 'White']
wea = ['Knife', 'Candlestick', 'Pistol', 'Poison', 'Trophy', 'Rope', \
       'Bat', 'Ax', 'Dumbbell']
roo = ['Hall', 'Dining', 'Kitchen', 'Patio', 'Observatory', 'Theater', \
       'Living', 'Spa', 'Guest']
allcards = per + wea + roo
allcardsnc = per + wea + roo

rumours = []
poolcards = []

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
        if self.shown == '0':
            self.rumour = p + ' accused ' + g \
                          + ' of killing someone with the ' + w \
                          + ' in the ' + r + ' and was shown a ' \
                          + 'card by ' + players[int(sb)].name
        else:
            self.rumour = p + ' accused ' + g + \
                          ' of killing someone with the ' + w + \
                          ' in the ' + r

def Error():
    print()
    print('Error')
    print()

def MainMenu():
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
    action = input('Action: ')
    print()
    if action == '0':
        YourCards()
    elif action == '1':
        InfoSheet()
    elif action == '2':
        LogRumour()
    elif action == '3':
        PlayerInfo()
    else:
        Error()

def YourCards():
    print('====================')
    print('     Your Cards')
    print('====================')
    print()
    print(str(players[0].cards))

def InfoSheet():
    print('===================')
    print('    Info Sheet')
    print('===================')
    print()
    print('Cards:')
    for i in range(0, len(allcardsnc)):
        for k in range(0, len(players)):
            if allcardsnc[i] in players[k].cards:
                owner = players[k].name
                break
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

def LogRumour():
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
    print()
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
            if guest not in players[0].cards:
                print('0: ' + guest)
            if weapon not in players[0].cards:
                print('1: ' + weapon)
            if room not in players[0].cards:
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
    # Analize rumour
    if shown == '0':
        players[int(shownby)].rumoursa.append(rumour.rumour)
    if guest in players[int(playern)].cards and weapon in players[int(playern)].cards and shown == '0':
        rgw = room
    elif weapon in players[int(playern)].cards and room in players[int(playern)].cards and shown == '0':
        rgw = guest
    elif guest in players[int(playern)].cards and room in players[int(playern)].cards and shown == '0':
        rgw = weapon
    else:
        rgw = ''
    if playern == '0':
        if guest not in players[0].cards and shown == '1':
            if guest not in poolcards:
                poolcards.append(guest)
        if weapon not in players[0].cards and shown == '1':
            if weapon not in poolcards:
                poolcards.append(weapon)
        if room not in players[0].cards and shown == '1':
            if room not in poolcards:
                poolcards.append(room)
    else:
        if guest not in allcards and guest not in players[int(playern)].cards and shown == '1':
            if guest not in poolcards:
                poolcards.append(guest)
        if weapon not in allcards and weapon not in players[int(playern)].cards and shown =='1':
            if weapon not in poolcards:
                poolcards.append(weapon)
        if room not in allcards and room not in players[int(playern)].cards and shown == '1':
            if room not in poolcards:
                poolcards.append(room)
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
    for i in range(0, len(players[int(player)].cards)):
        print(players[int(player)].cards[i])
    print('===========')
    print()
    print('Accusations:')
    print('============')
    for i in range(0, len(players[int(player)].rumoursd)):
        print(players[int(player)].rumoursd[i])
    print('============')
    print()
    print('Accusations Answered:')
    print('=====================')
    for i in range(0, len(players[int(player)].rumoursa)):
        print(players[int(player)].rumoursa[i])
    print('=====================')

# Main program
# Get players
print('===========================================')
print('             Enter player name')
print('*Enter a blank line to stop entering names*')
print('===========================================')

players = []
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

# Main loop
while True:
    if len(allcards) == 3:
        poolcards = allcards
    if len(poolcards) == 3:
        print()
        print('Go to the pool. Cards are: ' + poolcards[0] + ', ' + poolcards[1] + ', ' + poolcards[2])
    MainMenu()
