print('''
ESCAPE GAME

Find the KEY and get out of the House 
Avoid the monsters!

Commands:
  go direction
  get item
''')

def Status():
  print('You are in the ' + currentRoom)
  print("Inventory : " + str(inventory))
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
inventory = []
rooms = {

            'Hall' : { 'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'north' : 'Living Room',
                  'west'  : 'Bedroom'
                },        

            'Kitchen' : { 'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Living Room' : { 'east' : 'Store Room',
                  'south' : 'Hall'
                },
            'Store Room' : { 'item' : 'monster',
                   'west' : 'Living Room'
                },
            'Bedroom' : { 'west' : 'Bathroom',
                   'east' : 'Hall'
                },
            'Bathroom' : { 'item' : 'key',
                   'east' : 'Bedroom'
                },
                   
            'Dining Room' : { 'west'  : 'Hall',
                  'south' : 'Garden'
                },
                
            'Garden' : { 'north' : 'Dining Room',
                  'west'  : 'Kitchen'
                },

         }

currentRoom = 'Hall'
while True:

  Status()


  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()

  if move[0] == 'go':
    if move[1] in rooms[currentRoom]:
      currentRoom = rooms[currentRoom][move[1]]
    else:
      print('You can\'t go that way!')

  if move[0] == 'get' :
    if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      inventory += [move[1]]
      print(move[1] + ' got!')
      del rooms[currentRoom]['item']
    else:
      print('Can\'t get ' + move[1] + '!')

  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break

  if currentRoom == 'Garden' and 'key' in inventory:
    print('You escaped the house... YOU WIN!')
    break
