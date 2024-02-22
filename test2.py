map = ['☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','\n',
       '☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','\n',
       '☐ ','☐ ','☐ ','☐ ','⊕ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','\n',
       '☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','\n',]

floor = '☐ '
Player = '⊕ '

print('floor is',floor)
print('Player is',Player)

xend = True
x = 0
y = 0
px = 0
py = 0
allo = 0
xse = 0
po = 0

nop = 0

while True:

    for i in map:
        if i == Player:
         px = x
        if i != "\n" and xend == True:
         x += 1
        elif i == "\n":
         x = 0
        if xse < x:
          xse = x
    
    for i in range(xse): #Top nember
      print(i,end=' ')
    print('\n')

    for i in map:
       if i != "\n" and xend == True:
         x += 1
       elif i == "\n":
         y += 1
         xend = False

       if i == Player:
          py = y + 1
    
    y = 0

    for i in map:
       if i == "\n":
          y += 1

       print(i ,end='')
    moveX = input("moveX : ")
    moveY = input("moveY : ")

    moveX = int(moveX)
    moveY = int(moveY)

    if moveX < 0 or moveX > xse - 1:
      pass

    elif moveY < 1 or moveY > y:
      pass

    else:
      if moveY > 1:
        po = (moveY - 1) * 10 + (moveY - 1) * 3 + moveX 
      else :
        po = moveX
      print('moveto ',po)
      nop = -1
      for i in map:
        nop += 1
        if i == Player:
          map[nop] = floor
      map[po] = Player