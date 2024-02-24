import random

map = ['☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','\n',
       '☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','\n',
       '☐ ','☐ ','☐ ','☐ ','⊕ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','\n',
       '☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','\n',
       '☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','\n',
       '☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','\n',
       '☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','\n',
       '☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','\n',
       '☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','\n',
       '☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','☐ ','\n',]

#stats Player----------------------------------------------------
MaxHP = 100
HP = 100
ATK = 1000000000
Maxmama = 100
Mama = 100

level = 1
FULLEXP = 50
EXP = 0

List_item = ['Dack book','Sword of freedom','Gun','Money','Rock','Friendly armor']
Nember_item = 0

#Level up++---------------------------------------------------------
ATKUP = 2
HPUP = 10
MAMAUP = 20

Gameover = False
textgameover = '''
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   '''

#Monster-------------------------------------------------------

GotoFight = True

Monstername = ''
Monsterlevel = 0
MonsterMaxHP = 0
MonsterHP = 0
MonsterATK = 0
MonsterCheck = ''
MonsterEXP = 0

Batbatart = ["""                                                                     
                                                                                             
                                  █ █                             █                                 
                                   ████    █            █    ██ ██                                  
                                    █  ███                 ███ ██                                   
                                       ███               ████  █                                    
                                       ██████         ███████ █                                     
                                        █ ████       █████ █                                        
                                       █ ██  ██████████  ██ ██                                      
                                     ██  ██ ████    █████ █  ███                                    
                           ███            ████        ████            ███                           
                      ███  ████                                      █████████                      
                   ██     ██████     ██    ███ █ ██   ███   ███     ██████     ██                   
                  █      ████   ███ ██████████        ██████████ ███  █████     ██                  
                           ██    █   ████████████  ████████████  ██   ███                           
                            ██████    ████████████████████████ █████████     █                      
                      █     █████████████             █   ██████████████     █                      
                            █████████████   ████████████  ██████████████                            
                             ███████████                  █████████████                             
                             ██████████████           █████████████████                             
                             ██████████████████  █   ██████████████████                             
                             █████████        █████████████   █████████                             
                            █   ███████   █   █            █  █████   █                             
                                  █████████  ██         █  ██████                                   
                                         ████████  ████████                                         
                                           ██          ██                                           
                                            ████████████                                            """]
Batbatname = 'Batbat'
Batbatlevel = 5
BatbatMaxHP = 50
BatbatHP = 50
BatbatATK = 10
BatbatCheck = 'It looks ilke Batman but It is Bat.'
BatbatEXP = 10

Sales_leaderart = ['''
=+==========================~~+++-~~~~~~~~===~~~======================== 
 ====================~~~~~~-~-++=+++--++++-~~=~^~======================+= 
 ====================~++++*+^++=====~.   :=*~=~~~==========~============= 
 ==================~~++=++=~==~~-:   >%%)  --~~~~~========+~+============ 
 ===================*++==^~++==<~ .@@>~@@@(  ++**~===========+=========== 
 ==================~-++:==--~~+  @@       @@ --~=-===============++====== 
 ===================~++~:.*{^-~ @@@#@@.^+  @ >><=+*~~~~===============+== 
 ===================~--.((      @  @@ .-  @{ --=.=:+**=================~= 
 ==================~~+~@->@@{[@: @%     ~@@  .~ :^++-~~~===============+= 
 ==================~+==-:   @@ ~~   ]@@@[  >[@@([*+-.:*-~~===+=========== 
 ================~~-+~=>^=+. @  *@@@@@@@@ -     **>*]-..~-=======+======= 
 ======+========~-+~:--~~^+^.@@=@  -@  @.@#% .-^>]~.+)#@~  ~============= 
 ============~~~-(=-]} -=-.~ (#>@  (@  @ @-@(:=   ~=:   ^@  ~============ 
 =========~.     -:<~}{-  -~ > ~@ )@@( @+  @ . @@ >}[  ~  @ ~~=========== 
 ========~  @@@@  .~: .}#@([@@= @ :@   @ >       @  )@[   . +~=========== 
 ========  @+   @@= :)   @    > @      @ @# ~@ @ +@   @@@@@   .~========= 
 =======- @:      @[  ]@@+ @^% -@@@@@@{@< @=      @ *  @   #@@ :========= 
 =======. @  @+*  ^@ )> @# # >  @   {@ @@] @#   @@    @+ .*  @]:========= 
 =======.~@  +(@@#)@ @   @@^    @~~+@@ @ @-  *@=  @@@+>  >  ~@ .~~======= 
 ==+====: @=      @. @ .<(@ ]@@ @ -@[@ @ @@@-@  (   [  -)@@@> .=+*~====== 
 =======~  @@+> @@  @%   @@ }<  @  @#@ @ * @@ ( >  {@  {@}<  -++=+===+=== 
 ========~    * @   @ - =@ <@>  @ <<[@ @@@{@# @@@@* @{  * . ~++~+~~====== 
 =========~ @   @@ @] ~ ]@  %@  @ ^*%@ %@# @ @      @+@@>   ==++--~====== 
 ======~=~~ @ @@ ] @ +-# @  @.  @^=>@@  @@ @ @{:- >@}  @@{@  @ ~++*~===== 
 =======+=~ @@   @ +  <:@@ .    @   @}  >@ @ { -^:  >@    @  >(:+++~===== 
 ===~~~~~=~ @ .= @ @  @  @  @ } @ . @=][ < @   @@*@>@^^..@@( @ .--*~===== 
 ===~***~== @ -+ @ @  @  @[ @  ~@   @    @<@    @ @@(>@... #@=+.+~~~===== 
 ===~~=~~~~ @ -+ @ @  @  @ +@ ^}] @@@@@@@@@@@@+@@ +@ @@    [@># -~======= 
 ========~* @ +- @ @  @  @ =@+^=% @   @:     @ @@~ @>@.%@@@<(.@ =~======= 
 =+======~- @ =  @ @  @  @        @(    ::^: @   @ @ . %@ +   @ -~===+=== 
 =========- @ + >@ @  @ @@@@@@@@@@@< +~~~=*- @@@-@ @+*  @ { = @} ~===~=== 
 ========~- @ = @@ @  @ @*  @+ @= =@ ==+^~== @   @ @ =  @ ] - +{ ~===~++= 
 =========*     @+ @  @ @( .   @@ {@ -+===== @~ ]% @  :)@^(+*  ].+~=+==== 
 ========~~ #@   :  @ @ @] ~-+ %@ @@ ~~-++++ @> @% @  ^@   * ]#*:+~====== 
 ==+=======  @ =.@  @ @ @+ =~- @@ ~) ~=~~~-+ @- @% @  *@ + @.{@--+~====== 
 ========== :@ -    @ @ @=.==~ @% ::-==+==~~:.  @  @  (@ +   {@ =~~====== 
 ========== >@ =~~~ @     -=+~   :============~ : .::-   ~~=:  .=~======= 
 ==========-   ====   ~==============+=========~~~====+==================''']
Sales_leadername = 'Sales leader'
Sales_leaderlevel = 10
Sales_leaderMaxHP = 100
Sales_leaderHP = 100
Sales_leaderATK = 10
Sales_leaderCheck = 'These politicians look powerful but they are just pieces of meat.'
Sales_leaderEXP = 50

Super_Rockart = ['''                                                        
                        ..:::-----=--==-:                       
                     .:::::----=-=====-:-==:                    
                   .::::::---=-=====-::=+=====:                 
                 .::::::::---======-:=++++==+===:               
                .:::::::---======-:=++++==++++-+++-             
              .:::::::::--=====::=+++*+==++==++***++:           
            .:::::::::--==---:=++++==+**+***********+=.         
           :::::::::---:-=-:=***+*****++*########*****+.        
         .::::::::-:::===:=******####*############*****=        
        ::::::::--:-===-+***##+*###*###########*******++.       
       :::::::--:-====-***##**####*###*###*********++++=.       
      :::::::-::===+==****##*####*###********++++++++++=        
      :::::--:==+++==****##***##********+*++++++++++===:        
     .:::---:=+++*+-***##*+********+**+++++*++++++++==:         
     .:----.=+++++==******+***++++++++++++++++**++++=.          
      :---:-=+=++=-++++++==+++=++++++++++**+******+:            
      .--:---====::=+++=--==+==+++++++++*****###*:              
       .::--:--=-:-====--===+=+++++*****######*:............    
          :-:----:-=======+++++****########*=---------==========
            .:--::===++=++****########%######***+++++++++++====-
            .:-=+*+**############################****++==---::::
           ..:-=++*##########################**+==---:::::......
              ...::--===+++++++++++++===---::::::..........     
                        ...........................             ''']
Super_Rockname = 'Super power Rock!!!!!!!!!!'
Super_Rocklevel = 9999999999
Super_RockMaxHP = 10
Super_RockHP = 10
Super_RockATK = 0
Super_RockCheck = 'It is incredibly terrifying! Its strength is like that of a professional wrestler. It is powerful and fast like a rock. Time cannot destroy it. The longer it exists on this earth, the more powerful it becomes, to the point of being uncontrollable.'
Super_RockEXP = 1

#---------------------------------------------------------------

floor = '☐ '
Player = '⊕ '

xend = True
x = 0
y = 0
px = 0
py = 0
allo = 0
xse = 0
po = 0

nop = 0

endfor = False

#rate%---------------------------------------------------------
rate_spawn = 5
nember_spawn = 0
rate_list = []

#--------------------------------------------------------------
play = True

print('''
▄█      ███        ▄████████                         
███  ▀█████████▄   ███    ███                         
███▌    ▀███▀▀██   ███    █▀                          
███▌     ███   ▀   ███                                
███▌     ███     ▀███████████                         
███      ███              ███                         
███      ███        ▄█    ███                         
█▀      ▄████▀    ▄████████▀                          
   ▄██████▄     ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████
  ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███
  ███    █▀    ███    ███ ███   ███   ███   ███    █▀ 
 ▄███          ███    ███ ███   ███   ███  ▄███▄▄▄    
▀▀███ ████▄  ▀███████████ ███   ███   ███ ▀▀███▀▀▀    
  ███    ███   ███    ███ ███   ███   ███   ███    █▄ 
  ███    ███   ███    ███ ███   ███   ███   ███    ███
  ████████▀    ███    █▀   ▀█   ███   █▀    ██████████
   ▄████████    ▄███████▄    ▄██████▄                 
  ███    ███   ███    ███   ███    ███                
  ███    ███   ███    ███   ███    █▀                 
 ▄███▄▄▄▄██▀   ███    ███  ▄███                       
▀▀███▀▀▀▀▀   ▀█████████▀  ▀▀███ ████▄                 
▀███████████   ███          ███    ███                
  ███    ███   ███          ███    ███                
  ███    ███  ▄████▀        ████████▀                 
  ███    ███                                          ''')
readyplay = str(input('Are you ready for play(Y/N) : '))

if readyplay == "Y" or readyplay == "y":
  play = True
  print('floor is',floor)
  print('Player is',Player)
else:
  play = False
  for i in range(5):
    print(textgameover)

#def------------------------------------------------------------

while play == True and Gameover == False:
    HP = MaxHP
    Mama = Maxmama
    y = 0

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


    for i in map:
       if i != "\n" and xend == True:
         x += 1
       elif i == "\n":
         y += 1
         xend = False

       if i == Player:
          py = y + 1

    print("size:",xse-1,"x",y)

    for i in map: #---------gen_map
       if i == "\n":
          y += 1

       print(i ,end='')
    print('Stats:','HP:',str(HP) + '/' + str(MaxHP),"ATK:",str(ATK),"Mama:",str(Mama) + '/' + str(Maxmama))
    print('Level:',level,'EXP:',str(EXP) + '/' + str(FULLEXP),'Monster spawn rate(%):',str(rate_spawn)+'%')

#choice----------------------------------------------------------------------------------------------
       
    moveX = int(input("moveX : "))
    moveY = int(input("moveY : "))

    if moveX < 0 or moveX > xse - 1:
      pass

    elif moveY < 1 or moveY > y:
      pass

    else:
      if moveY > 1:
        po = (moveY - 1) * 10 + (moveY - 1) * 2 + moveX 
      else :
        po = moveX
      nop = -1
      for i in map:
        nop += 1
        if i == Player:
          map[nop] = floor
      if po > nop:
        continue
      else:
        map[po] = Player
        for i in range(rate_spawn):
          add_rate = random.randint(0,rate_spawn)
          rate_list.append(add_rate)
        nember_spawn = random.randint(0,rate_spawn)
        GotoFight = False
        for i in rate_list:
          if i == nember_spawn:
            GotoFight = True

        if GotoFight == True:
          for i in range(5):
            print('\n')
          print('Oh? You are approaching me? Instead of running away, you are coming right to me?')
    
          Gameover = False
#----------------------------------------------------------------------------------------------------------          
          MonsterRamdom = random.randint(1,3)
          if MonsterRamdom == 1:
            for i in Batbatart:
              print(i)
            Monstername = Batbatname
            Monsterlevel = Batbatlevel
            MonsterMaxHP = BatbatMaxHP
            MonsterHP = BatbatHP
            MonsterATK = BatbatATK
            MonsterCheck = BatbatCheck
            MonsterEXP = BatbatEXP
          elif MonsterRamdom == 2:
            for i in Super_Rockart:
              print(i)
            Monstername = Super_Rockname
            Monsterlevel = Super_Rocklevel
            MonsterMaxHP = Super_RockMaxHP
            MonsterHP = Super_RockHP
            MonsterATK = Super_RockATK
            MonsterCheck = Super_RockCheck
            MonsterEXP = Super_RockEXP
          elif MonsterRamdom == 3:
            for i in Sales_leaderart:
              print(i)
            Monstername = Sales_leadername
            Monsterlevel = Sales_leaderlevel
            MonsterMaxHP = Sales_leaderMaxHP
            MonsterHP = Sales_leaderHP
            MonsterATK = Sales_leaderATK
            MonsterCheck = Sales_leaderCheck
            MonsterEXP = Sales_leaderEXP
#----------------------------------------------------------------------------------------------------------
            
          while GotoFight == True:
              if GotoFight == False or Gameover == True or MonsterHP <= 0 or HP <= 0:
                break
              print(Monstername,'Level:',Monsterlevel,'HP:',str(MonsterHP) + '/' + str(MonsterMaxHP),'ATK:',str(MonsterATK))
              print('\n')
              print('Stats:','HP:',str(HP) + '/' + str(MaxHP),"ATK:",str(ATK),"Mama:",str(Mama) + '/' + str(Maxmama))
              print('''
              1.Attack
              2.Skills
              3.Check
              4.Item
              5.Run''')
              ChoosePlayer = input('You choose: ')
              if ChoosePlayer == 1 or ChoosePlayer == '1':
                AttackMonster = ATK - random.randint(0,5)
                print(Monstername,'attacked',str(AttackMonster),'HP')
                MonsterHP -= AttackMonster
                print(Monstername,'Level:',Monsterlevel,'HP:',str(MonsterHP) + '/' + str(MonsterMaxHP),'ATK:',str(MonsterATK))
              elif ChoosePlayer == 2 or ChoosePlayer == '2':
                print('''
              1.Heal -10 mama +10-15HP
              2.Water ball -50 mama 30ATK ''')
                ChooseSkill = input('You choose: ')
                if ChooseSkill == 1 or ChooseSkill == '1':
                  if Mama < 10:
                    print('NO Mama')
                  else:
                    HealHP = 10 + random.randint(0,5)
                    HP += HealHP
                    print('Heal','+' + str(HealHP),'Mama','-10')
                    Mama -= 10

                elif ChooseSkill == 2 or ChooseSkill == '2':
                  AttackMonster = 30
                  if ATK > 0:
                    print('Mama','-30')
                    if Mama < 30:
                      print('NO Mama')
                    else:
                      Mama -= 30
                      print(Monstername,'attacked',str(AttackMonster),'HP')
                      MonsterHP -= AttackMonster
                      print(Monstername,'Level:',Monsterlevel,'HP:',str(MonsterHP) + '/' + str(MonsterMaxHP),'ATK:',str(MonsterATK))

              elif ChoosePlayer == 3 or ChoosePlayer == '3':
                  print(MonsterCheck)
                  print('\n')

              elif ChoosePlayer == 4 or ChoosePlayer == '4':
                  Nember_item = 0
                  for i in List_item:
                    Nember_item += 1
                    print(str(Nember_item)+".",end=' ')
                    print(i)
                  Itme_Choose = int(input('You choose: '))
                  Yes_Itme =List_item[Itme_Choose - 1]
                  if Yes_Itme == 'Dack book':
                    print('Dack book BY Dack. MAKE BY Dack. WRITE BY Dack. Why do you use it?')
                  elif Yes_Itme == 'Sword of freedom':
                    print('It kill you because freedom.')
                    print('Sword of freedom : Goodbye my master.')
                    HP = 0
                  elif Yes_Itme == 'Money': 
                    if Monstername == 'Sales leader':
                      print('Thank you for buying.')
                      print('You got Dack book.')
                      List_item.append('Dack book')
                      break
                    else:
                      print('Why do you use it?')
                  elif Yes_Itme == 'Gun':
                    if Monstername != 'Super power Rock!!!!!!!!!!':
                      if ATK > 0:
                        print('You kill ',end='')
                        print(Monstername ,end=' ')
                        print('BY gun.')
                        MonsterHP = 0
                      else:
                        print('Now Why do you use it?')
                    else:
                      print('Why do you use it?')
                  if Yes_Itme == 'Rock':
                    print('Rock is Best weapon in the world.')
                    if ATK > 0:
                      MonsterHP -= 9999999999999999999999999999999999999999
                      print(Monstername,'attacked',str(9999999999999999999999999999999999999999),'HP')
                      print(Monstername,'Level:',Monsterlevel,'HP:',str(MonsterHP) + '/' + str(MonsterMaxHP),'ATK:',str(MonsterATK))
                  if Yes_Itme == 'Friendly armor':
                    print('You can not hurt anyone right now because you are too Friendly.')
                    ATK = 0

              elif ChoosePlayer == 5 or ChoosePlayer == '5':
                  print('You run form',Monstername)
                  GotoFight = False
                  endfor = True
                  break
              else:
                print('OK')
              if MonsterHP <= 0:
                print('You won',Monstername)
                print('You get',str(MonsterEXP),'EXP')
                EXP += MonsterEXP
                HP = MaxHP
                if EXP >= FULLEXP:
                  level += 1
                  print('Level UP!')
                  print('Level:',str(level))
                  print('HP+:',str(HPUP))
                  print('ATK+:',str(ATKUP))
                  print('MAMA+:',str(MAMAUP))
                  MaxHP += HPUP
                  ATK += ATKUP
                  EXP -= FULLEXP
                  Maxmama += MAMAUP
                GotoFight = False
                endfor = True
                break
              Monsterattack = MonsterATK + random.randint(0,Monsterlevel)
              HP -= Monsterattack
              print('Player attacked',str(Monsterattack),'HP')
              print('Player:','HP:',str(HP) + '/' + str(MaxHP),"ATK:",str(ATK),"Mama:",str(Mama) + '/' + str(Maxmama))
              if HP <= 0:
                Gameover = True
                print(textgameover)
                GotoFight = False
                endfor = True
                break

        if HP <= 0:
          break
        