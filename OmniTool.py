import random
import time
import os
import json

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
    return

#Utility Function for printing the word on the Screen
def Initiate(word):
    length = len(word)
    print("\n")
    while length > 0:
        print("_ " , end='')
        length = length - 1
    print(end = '\n')

#Function to Play the HangMan game    
def Hangman():
    print("Welcome to Hangman\n")
    while(True):
        print("Which Category would you like to play?\n")
        print("1)Sports\n2)Games\n3)Countries\n4)Exit\n")
        print("Enter the Number of the category you would like to play.")
        cat = input()
        time.sleep(1)
        with open("words\\Hangman.txt") as HG:
            words = json.load(HG)
        
        clear()
        n = random.randint(0,7)
        if cat == "1":
            print("\nYou chose the category Sports.\n")
            word = words["words"]["sports"][n]
            print(word)
            Initiate(word)
        elif cat == "2":
            print("\nYou chose the category Video Games.\n")
            word = words["words"]["games"][n]
            Initiate(word)
        elif cat == "3":
            print("\nYou choose the category Countries.\n")
            word = words["words"]["countries"][n]
            Initiate(word)
        elif cat == "4":
            print("\nClosing Application\n")
            time.sleep(1)
            clear()
            break
        else:
            print("Please pick a number from 1-4")

        #Prints and Playes the Game screen
        lives = 10
        length = 0
        guesses = ""
        while lives>0:
            wrong = 0
            print(f"\nYou have {lives} lives left")
            print("\nGuess a Letter")
            guess = input().lower()
            print("\n")
            guesses = guesses + guess
            if guess not in word:
                print("Wrong\n")
                lives = lives - 1
                if lives<1:
                    clear()
                    print("You loose\n")
                    print(f"The word was {word}.\n")
                    print("Would you like to play again? (Y/N)")
                    yn = input().lower()
                    if yn == 'y':
                        time.sleep(1)
                        clear()
                        continue
                    elif yn == 'n':
                        print("Closing Application")
                        time.sleep(1)
                        clear()
                        return
            clear()
            for char in word:
                if char in guesses:
                    print(char , end="")
                else:
                    print("_ ", end="")
                    wrong = wrong + 1
            if wrong == 0:
                print(f"\n\nYou won\n\nThe word was {word}\n")
                time.sleep(1)
                print("Would you like to play again?(Y/N)")
                YN = input().lower()
                if YN == 'y':
                    clear()
                    break
                elif YN == 'n':
                    clear()
                    return
                else:
                    print("Please pick either Y(yes) or N(no)\n")

#Function to Play the Rock, Paper, Scissors game.
def RockPaperScissors():
    print("Welcome to Rock Paper Scissors.")
    cho = ["Rock","Paper","Scissors"]
    while (1==1):
        print("\n1)Rock\n2)Paper\n3)Scissors\n")
        print("Enter the number of the hand you would like to play\n")
        Pla = cho[int(input())]
        Com = cho[random.randint(0,2)]
        time.sleep(0.5)
        if(Pla == Com):
            print(Pla+" vs "+Com)
            print("\nIts a Tie\n")
        elif(Pla == "Rock" and Com == "Scissors"):
            print(Pla+" vs "+Com)
            print("\nYou win\n")
        elif(Pla == "Paper" and Com == "Rock"):
            print(Pla+" vs "+Com)
            print("\nYou Win\n")
        elif(Pla == "Scissors" and Com == "Paper"):
            print(Pla+" vs "+Com)
            print("\nYou win\n")
        else:
            print(Pla+" vs "+Com)
            print("You lose Better luck Next time.\n")
        time.sleep(1)
        print("Would you like to play again? (Y/N)")
        yn = input().lower()
        if yn == 'y':
            clear()
            continue
        elif yn == 'n':
            print("\nClosing Application")
            time.sleep(1)
            clear()
            break
        else:
            print("Please type either (Y/N)")
            break            
        print("Closing Application")
        time.sleep(1)
    return

#Function to play the Scramble Game.
def Scramble():
    print("Welcome to Scramble\n")
    while(1==1):
        print("What category would you like to play?\n")
        print("1)Games\n2)Movies\n3)Companies\n4)Super Heroes\n5)Back\n")
        cat = input()
        with open("words\\Scramble.txt") as SC:
            words = json.load(SC)
        word = ""
        if cat == "1":
            word = " ".join(random.choices(words["word"]["games"]))
            shuffle = random.sample(word,len(word))
            shuffle = " ".join(shuffle)                                   
        elif cat == "2":
            word = " ".join(random.choices(words["word"]["movies"]))
            shuffle = random.sample(word,len(word))
            shuffle = " ".join(shuffle)           
        elif cat == "3":
            word = " ".join(random.choices(words["word"]["companies"]))
            shuffle = random.sample(word,len(word))
            shuffle = " ".join(shuffle)           
        elif cat == "4":
            word = " ".join(random.choices(words["word"]["superhero"]))
            shuffle = random.sample(word,len(word))
            shuffle = " ".join(shuffle)            
        elif cat == "5":
            print("Closing Application")
            time.sleep(1)
            clear()
            return
        else:
            print("Choose a number between 1-4")
        
        #Prints the Scramble Game Screen
        lives = 3
        while lives>0:
            print(f"You need to unscramble {shuffle}")
            print("\nYou think the word is : ")
            guess = input().lower()
            if guess == word:
                print("\nThat is the word")
                print("\nYou Win")
                time.sleep(0.5)
                print("\nWould you like to play again? (Y/N)")
                yn = input().lower()
                if yn == 'y':
                    time.sleep(0.9)
                    clear()
                    break
                elif yn == 'n':
                    print("\nReturning")
                    time.sleep(1)
                    clear()
                    return             
            else:
                print("\nWrong")
                print("\nTry again")
                lives = lives - 1
                clear()
                print(f"\nYou have {lives} lives left")
                if lives == 0:
                    print("\nYou loose")
                    print("\nThe Word was "+word)
                    print("\nWould you like to play again? (Y/N)")
                    yn = input().lower()
                    if yn == 'y':
                        time.sleep(0.9)
                        clear()
                        break
                    elif yn == 'n':
                        print("\nReturning")
                        time.sleep(0.7)
                        clear()
                        return


#Utility function to print the cards in hand
def printCards(cards):
    category = ['♣','♦','♥','♠']
    random_category = category[random.randint(0,3)]
    for card in cards:
        print(f"{card} {random_category} ,",end='')
    return


#Function to play the game BlackJack
def BlackJack():
    print("Welcome to BlackJack")
    cards = [1,2,3,4,5,6,7,8,9,10]
    while (1==1):
        player = []
        computer = []
        player_sum = 0
        computer_sum = 0
        n = 0
        while (1==1):
            random_card = cards[random.randint(0,9)]
            player.append(random_card)
            random_card = cards[random.randint(0,9)]
            computer.append(random_card)
            player_sum = sum(player)
            computer_sum = sum(computer)
            print("\nYou have the Cards")
            printCards(player)
            print("\nYour Total is = "+str(player_sum))
            if player_sum > 21:
                print("\nYou loose")
                print("\nThe Computer had ")
                printCards(computer)
                print(f"\nSum = {computer_sum}")
                break
            print("\nThe Computer has")
            printCards(computer)
            print("\nWould you like to \n1)Hit\n2)Stand")
            player_Choice = input().lower()
            if player_Choice == '1' or player_Choice == 'hit':
                if computer_sum > 21:
                    print("\nYou Win")
                    print("\nThe Computer had ")
                    printCards(computer)
                    print(f"\nSum = {computer_sum}")
                    break
                clear()
                continue
            elif player_Choice == '2':
                if player_sum<=21 and player_sum>computer_sum:
                    print("\nYou Win")
                    print("\nThe Computer had ")
                    printCards(computer)
                    print(f"\nSum = {computer_sum}")
                    break
                elif player_sum == 21 and computer_sum == 21:
                    print("\n Its a Draw")
                    print("You had :")
                    printCards(player)
                    print("\nThe Computer had :")
                    printCards(computer)
                    break
                elif computer_sum > 21:
                    print("\nYou Win")
                    print("\nThe Computer had ")
                    printCards(computer)
                    print(f"\nSum = {computer_sum}")
                    break
                else:
                    print("\nYou Loose")
                    print("\nThe Computer had ")
                    printCards(computer)
                    print(f"\nSum = {computer_sum}")
                    break
        print("Would you like to play again?")
        yn = input().lower()
        if yn == 'y':
            clear()
            continue
        elif yn == 'n':
            clear()
            return

        
#Function to roll a die     
def Roll():
    print("\nWelcome to Roll The Dice")
    while(1==1):
        print("\nRolling the Dice")
        dice = random.randint(1,6)
        time.sleep(2)
        print(f"\nThe Dice says {dice}")
        while(True):
            print("\nWould you like to roll again?")
            print("1) Yes\n2) No")
            yn = input().lower()
            if yn == '1':
                clear()
                break
            elif yn == '2':
                clear()
                return
            else:
                print("Pick a number from 1(Yes) and 2(No)")
                time.sleep(1)
                clear()
                continue


#Function to Flip a Coin
def Flip():
    print("\nWelcome to Flip a Coin")
    while(1==1):
        print("\nFlipping a Coin")
        coin = random.randint(0,1)
        time.sleep(1)
        if coin == 0:
            print("The coin landed on HEADS")
        else:
            print("The coin landed on TAILS")
        while(True):
            print("\nWould you like to Flip again?")
            print("1) Yes\n2) No")
            yn = input().lower()
            if yn == '1':
                clear()
                break
            elif yn == '2':
                clear()
                return
            else:
                print("Pick either 1(YES) or 2(NO)")
                time.sleep(0.5)
                clear()
                continue


def Calculator():
    print("\nWelcome to Calculator")    
    res = 0
    n = 0
    while (1==1):
        print("\nWhat would you Like to do?")
        print("\n1)Addition \n2)Subtraction \n3)Multiplication \n4)Division \n5)Exit")
        opr = input()
        if opr == '5':
            print("\nClosing Program")
            time.sleep(1)
            return
        else:
            print("\nEnter a Variable 'a'")
            varA = int(input())
            print("\nEnter a Variable 'b'")
            varB = int(input())
            if(opr == '1'):
                res = varA + varB
            elif(opr == '2'):
                res = varA - varB
            elif(opr == '3'):
                res = varA * varB
            elif(opr == '4'):
                res = varA / varB
            else:
                print("\nChoose a operation from 1-4")
        print("\nResult = "+str(res))
        time.sleep(1)
        print("\nWould you like to try again? (Y/N)")
        yn = input().lower()
        if yn == 'y':
            continue
        elif yn == 'n':
            print("\nClosing Application")
            time.sleep(1)
            break
    return

        
def StopWatch():
    def Converter(sec):
        sec = int(sec)
        mins = sec//60
        hr = mins//60
        sec = str(sec)
        mins = str(mins)
        hr = str(hr)
        print(hr+" hours : "+mins+" minutes : "+sec+" seconds has passed")
        time.sleep(2)
        return
    print("\nWelcome to StopWatch")
    while (1==1):
        print("\nPress Enter to Start")
        input()
        print("\nStarting StopWatch")
        start = time.time()
        print("\nPress Enter to Stop")
        input()
        print("\nStopping StopWatch\n")
        pause = time.time()
        time_spent = pause - start
        Converter(time_spent)
        print("\nWould you like to time again? (Y/N)")
        yn = input().lower()
        if yn == 'y':
            clear()
            continue
        elif yn == 'n':
            print("\nClosing Application")
            time.sleep(1)
            clear()
            break
        return

  
def Timer():
    
    def CD(t):
        while t:
            sec = t%60
            mins = t//60
            hours = mins//60
            timer = ' {} : {} : {}'.format(hours,mins,sec)
            time.sleep(1)
            print(timer)
            t = t-1
        time.sleep(0.7)
        print("Times up")
        time.sleep(1)
    print("\nWelcome to Timer")
    while(1==1):
        print("\nEnter your time in Seconds")
        tim = int(input())
        print("\n")
        CD(tim)
        print("\nWould you like to try again? (Y/N)")
        yn = input().lower()
        if yn == 'y':
            continue
        elif yn == 'n':
            print("\nClosing Application")
            time.sleep(1)
            break
    return


def Vguide():
    print("Welcome to Valorant Guide")
    while(1==1):
        print("\nWho's Information would you like to access?")
        print("\n1)Breach\n2)Brimstone\n3)Cypher\n4)Jett\n5)Killjoy\n6)Omen\n7)Phoenix\n8)Raze\n9)Reyna\n10)Sage\n11)Sova\n12)Skye\n13)Viper\n14)Go Back")
        print("\nEnter the Number of the Character you would like to access.")
        vchoice = str(input())
        if vchoice == '1':
            print("\nBreach is a Swedish cyborg who fires powerful, targeted kinetic blasts to aggressively clear a path through enemy ground.\nThe damage and disruption he inflicts ensures no fight is ever fair.\n")
            print("Abilities:\n\n1)AfterShock(Basic):\nCost: 100 Credits\nDescription: Equip a fusion charge. Fire the charge to set a slow-acting burst through the wall. The burst does heavy damage to anyone caught in its area.\n\n2)FlashPoint(Basic):\nCost: 200 Credits\nDescription: Equip a blinding charge. Fire the charge to set a fast-acting burst through the wall. The charge detonates to blind all players looking at it.\n\n3)Fault Line(Signature):\nCost: Free\nDescription: Equip a seismic blast. Hold Fire to increase the distance. Release to set off the quake, dazing all players in its zone and in a line up to the zone.\n\n4)Rolling Thunder(Ultimate):\nPoints: 7\nDescription: Equip a seismic charge. Fire to send a cascading quake through all terrain in a large cone. The quake dazes and knocks up anyone caught in it.\n")
            print("\nPress Enter to Continue")
            input()
        elif vchoice == '2':
            print("\nBrimstone is a powerful American comander with his orbital arsenal that ensures his squad always has the advantage\n")
            print("Abilities:\n\n1)Incendiary(Basic):\nCost: 300 Credits\nDescription: Equip an Incendiary grenade launcher. Fire to launch a grenade that detonates as it comes to a rest on the floor, creating a lingering fire zone that damages players.\n\n2)Stim Beacon(Basic):\nCost: 100 Credits\nDescription: Equip a Stim Beacon. Fire to toss the stim beacon in front of Brimstone. Upon landing, the stim beacon will create a field that grants players RapidFire.(RapidFire increases fire rate, reload speed, weapon swap speed, and recoil recovery by 15%.)\n\n3)Sky Smoke(Signature):\nCost: 100 Credits\nDescription: Equip a tactical map. Fire to set locations where Brimstone's smoke clouds will land. Alternate Fire to confirm, launching long-lasting smoke clouds that block vision in the selected area.\n\n4)Orbital Strike(Ultimate):\nPoints: 7\nDescription: Equip a tactical map. Fire to launch a lingering orbital strike laser at the selected location, which deals heavy damage over-time to players in the area.\n")
            print("\nPress Enter to Continue")
            input()
        elif vchoice == '3':
            print("\nCypher is a Moroccan information broker who keeps tabs on the enemy’s every move. No secret is safe. No maneuver goes unseen\n")
            print("Abilities:\n\n1)Tripwire(Basic):\nCost: 100 Credits\nDescription: Equip a trapwire that spans between the placed location and the wall opposite. Enemy players who cross a tripwire will be tethered, revealed, and dazed after a short period if they do not destroy the device in time.\n\n3)Cyber Cage(Basic):\nCost: 100 Credits\nDescription:  Instantly toss a cyber cage in front of Cypher. Activate from any distance to create a temporary zone that blocks vision.\n\n3)Spycam(Signature):\nCost: Free\nDescrpition: Equip a spycam ire to place the spycam at the targeted location. REUSE this ability to take control of the camera's view. While in control of the camera, Fire to shoot a tracking dart. The dart is removable and will periodically reveal the location of the enemy hit. It can be destroyed by shooting it once with any gun.\n\n4)Neural Theft(Ultimate):\nPoints: 7\nDescription: Use on a fresh enemy corpse to throw Cypher's hat. After a brief delay, all enemy players' locations will be revealed once.\n")
            print("\nPress Enter to Continue")
            input()
        elif vchoice == '4':
            print("\nJett is a Korean fighter who prioritizes movement over everything, Jett is one of the few Agents with a passive ability. Holding the jump key while in the air will allow Jett to slow her descent\n")
            print("Abilities:\n\n1)Cloudburst(Basic):\nCost: 100 Credits\nDescription:  Instantly throw a projectile that expands into a brief vision cloud on impact with a surface. Hold the ability key to curve the cloud in the direction of your crosshair.\n\n2)Updraft(Basic):\nCost: 100 Credits\nDescription: Instantly propel Jett high into the air.\n\n3)Tailwin(Signature):\nCost: Free\nDescription:Instantly propel in the direction she is moving. If Jett is standing still, she will propel forward.\n\n4)Blade Storm(Ultimate):\nPoints: 6\nDescription:  Equip a set of 5 highly accurate throwing knives. Fire to throw a single knife. Alternative Fire to throw all remaining daggers at once. Restocks upon killing an enemy.\n")
            print("\nPress Enter to Continue")
            input()
        elif vchoice == '5':
            print("\nKilljoy is The genius of Germany, Killjoy secures the battlefield with ease using her arsenal of inventions. If the damage from her gear doesn't stop her enemies, her robots debuff will help make short work of them.\n")
            print("Abilities:\n\n1)Alarmbot(Basic):\nCost: 200 Credits\nDescription:EQUIP a covert Alarmbot. FIRE to deploy a bot that hunts down enemies that get in range. After reaching its target, the bot explodes, applying Vulnerable.\n\n2)Nanoswarm(Basic):\nCost: 200 Credits\nDescription:  EQUIP a Nanoswarm grenade. FIRE to throw the grenade. Upon landing, the Nanoswarm goes covert. ACTIVATE the Nanoswarm to deploy a damaging swarm of nanobots.\n3)Turret(Signature):\nCost: Free\nDescription:  EQUIP a Turret. FIRE to deploy a turret that fires at enemies in a 180 degree cone that deals 11 damage per burst\n\n4)Lockdown(Ultimate):\nPoints: 7\nDescription: EQUIP the Lockdown device, After a long windup, the device Detains all enemies caught in the radius, Enemies detained by the ultimate can neither shoot nor use any abilities for 8 seconds\n")
            print("\nPress Enter to Continue")
            input()
        elif vchoice == '6':
            print("\nOmen is described as a shadow hunter, whose origins are completely unknown. Omen hunts in the shadows. He renders enemies blind, teleports across the field, then lets paranoia take hold as his foe scrambles to learn where he might strike next\n")
            print("Abilities:\n\n1)Shrouded Step(Basic):\nCost: 100 Credits\nDescription: Equip a shadow walk ability and see its range indicator. Fire to begin a brief channel, then teleport to the marked location. Enemies can hear a sound cue at your original location.\n\n2)Paranoia(Basic):\nCost: 200 Credits\nDescription: Instantly fire a shadow projectile forward, briefly reducing the vision range of all players it touches. This projectile can pass through walls.\n\n3)Dark Cover(Signature):\nCost: Free\nDescription:  Equip a shadow orb and see its range indicator. Fire to throw the shadow orb to the marked location, creating a long-lasting shadow sphere that blocks vision. Hold Alternate Fire while targeting to move the marker further away. Hold the ability key with targeting to move the market closer.\n\n4)From the Shadows(Ultimate):\nPoints: 7\nDescription: Equip a tactical map. Fire to begin teleporting to the selected location. While teleporting, Omen will appear as a Shade that can be destroyed by an enemy to cancel his teleport.\n")
            print("\nPress Enter to Continue")
            input()
        elif vchoice == '7':
            print("\nPhoenix is a fiery Brit that can wield the power of flame to essentially reshape the battlefield into how he sees fit.\n")
            print("Abilities:\n\n1)Blaze(Basic):\nCost: 200 Credits\nDescription: Equip a flame wall. Fire to create a line of flames that moves forward creating a wall that blocks vision and damages players passing through it. Hold Fire to bend the wall in the direction of your crosshair.\n\n2)Curveball(Basic):\nCost: 200 Credits\nDescription: Equip a flare orb that takes a curving path and detonates shortly after throwing, impairing vision. Fire to curve the flare orb to the left, detonating and blinding any player who sees the orb. Alternate fire to curve the flare orb to the right.\n\n3)Hot Hands(Signature):\nCost: Free\nDescription: Equip a fireball. Fire to throw a fireball that explodes after a set amount of time or upon hitting the ground, creating a lingering fire zone that damages enemies.\n\n4)Run it Back(Ultimate):\nPoints: 6\nDescription:  Instantly place a marker at Phoenix's location. When this ability is active, if you die or if the time expires, the ability ends and sends Phoenix back to the starting location.\n")
            print("\nPress Enter to Continue")
            input()
        elif vchoice == '8':
            print("\nRaze is a Brazilian who loves explosions With her blunt-force-trauma playstyle, she excels at flushing entrenched enemies and clearing tight spaces with a generous dose of 'boom'.\n")
            print("Abilities:\n\n1)Boom Bot(Basic):\nCost: 200 Credits\nDescription:  Equip a Boom Bot. The Boom Bot will lock on to any enemies in its frontal cone and chase them, exploding for heavy damage if it reaches them.\n\n2)Blast Pack(Basic):\nCost: 200 Credits\nDescription:  Instantly throw a Blast Pack that will stick to surfaces. Re-use to detonate, damaging and knocking back anything hit. Blast Pack will not damage Raze, but she can still suffer fall damage.\n\n3)Paint Shells(Signature):\nCost: Free\nDescription: Equip a cluster grenade. Fire to throw the grenade, which deals damage and creates sub-munitions, each exploding and dealing further damage\n\n4)Showstopper(Ultimate):\nPoints: 7\nDescription:  Equip a single-use Rocket Launcher and light its fuse which travels in a straight line and explodes on contact, dealing high damage to enemies caught in its blast radius.\n")
            print("\nPress Enter to Continue")
            input()
        elif vchoice == '9':
            print("\nReyna is a Mexican who dominates single combat, popping off with each kill she scores. Her capability is only limited by her raw skill, making her highly dependent on performance\n")
            print("Abilities:\n\n1)Leer(Basic)\nCost: 200 Credits\nDescription: Equip an ethereal eye The eye will Nearsight all enemies who can see it. The eye will disappear either after two seconds or receiving any bullet damage.\n\n2)Devour(Basic):\nCost: 100 Credits\nDescription: Instantly consume a nearby Soul Orb, disabling Reyna's ability to fire for 1 second and creating a tether between Reyna and the Soul Orb whilst rapidly healing for 100 health over 3 seconds.\n\n3)Dismiss(Signature):\nCost: 100 Credits\nDescription: Instantly consume a nearby Soul Orb, becoming intangible for 2 seconds and gaining a burst of movement speed for the first second of the duration.\n\n4)Empress(Ultimate):\nPoints: 6\nDescription:  Enter a frenzy for 30 seconds, increasing firing, equip and reload speeds by 15%. Grants infinite charges of Soul Harvest abilities. Scoring a kill fully refreshes the duration.\n")
            print("\nPress Enter to Continue")
            input()
        elif vchoice == '10':
            print("\nSage is a Chinese Healer who  creates safety for herself and her team wherever she goes. Able to revive fallen friends and stave off forceful assaults, she provides a calm center to a hellish battlefield.\n")
            print("Abilities:\n\n1)Barrier Orb(Basic):\nCost: 400 Credits\nDescription:  Equip a barrier orb. Fire places a solid wall. Alternate fire rotates the targeter.\n\n2)Slow Orb(Basic):\nCost: 100 Credits\nDescription: Equip a Slowing Orb. Fire to launch the Orb, which expands upon hitting the ground, creating a zone that slows players who walk on it.\n\n3)Healing Orb(Signature):\nCost: Free\nDescription:  Equip a healing orbFire with your crosshairs over a damaged ally to activate a heal-over-time on them. Alternate fire while Sage is damaged to activate a self heal-over-time. The heal will stop upon taking damage.\n\n4)Resurrection(Ultimate):\nPoints: 7\nDescription:  Equip a resurrection ability. Fire with your crosshairs placed over an ally's corpse to begin resurrecting them. After a brief channel, the ally will be brought back to life with full health.\n")
            print("\nPress Enter to Continue")
            input()
        elif vchoice == '11':
            print("\nSova is a Russian Hunter who  tracks, finds, and eliminates enemies with ruthless efficiency and precision. His custom bow and incredible scouting abilities ensure that even if you run, you cannot hide.\n")
            print("Abilities:\n\n1)Shock Bolt:\nCost: 100 Credits\nDescription: Equip a bow with shock bolt. Fire to send the explosive bolt forward detonating upon collision and damaging players nearby. Hold Fire to extend the range of the projectile. Alternate Fire to add up to two bounces to this arrow.\n\n2)Owl Drone(Basic):\nCost: 300 Credits\nDescription: Equip an owl drone. Fire to deploy and take control of movement of the drone. While in control of the drone, Fire to shoot a marking dart. This dart will periodically reveal the location of its target.\n\n3)Recon Bolt(Signature):\nCost: Free\nDescription: Equip a bow with recon bolt, activating upon collision and revealing the location of nearby enemies caught in the line of sight of the bolt.\n\n4)Hunter's Fury(Ultimate):\nPoints: 7\nDescription: Equip a bow with three long-range, wall-piercing energy blasts. Fire to release an blast in a line in front of Sova dealing damage and revealing the location of enemies caught in the line.\n")
            print("\nPress Enter to Continue")
            input()
        elif vchoice == '12':
            print("\nSkye is an Australian wild-life user, she and her band of beasts trail-blaze the way through hostile territory. With her creations hampering the enemy, and her power to heal others, the team is strongest and safest by Skye's side.\n")
            print("Abilities:\n\n1)Regrowth(Basic):\nCost: 200 Credits\nDescription:  EQUIP a healing trinket. HOLD FIRE to channel, healing allies in range and line of sight. Can be reused until her healing pool is depleted. Skye cannot heal herself.\n\n2)Trailblazer(Basic):\nCost: 200 Credits\nDescription: EQUIP a Tasmanian tiger trinket. FIRE to send out and take control of the predator. While in control, FIRE to leap forward, exploding in a concussive blast and damaging directly hit enemies.\n\n3)Guiding Light(Signature):\nCost: Free\nDescription: EQUIP a hawk trinket. FIRE to send it forward. HOLD FIRE to guide the hawk in the direction of your crosshair. RE-USE while the hawk is in flight to transform it into a flash that plays a hit confirm if an enemy was within range and line of sight.\n\n4)Seekers(Ultimate):\nPoints: 6\nDescription: EQUIP a Seeker trinket. FIRE to send out three Seekers to track down the three closest enemies. If a Seeker reaches its target, it nearsights them.\n")
            print("\nPress Enter to Continue")
            input()
        elif vchoice == '13':
            print("\nViper is an American toxicologist who deploys an array of poisonous chemical devices to control the battlefield and cripple the enemy’s vision. If the toxins don’t kill her prey, her mind games surely will\n")
            print("Abilities:\n\n1)Snake Bite(Basic):\nCost: 100 Credits\nDescription: Equip a chemical launcher. Fire to launch a canister that shatters upon hitting the floor, creating a lingering chemical zone that damages enemies (24 dps) and applies Vulnerable, doubling incoming damage\n\n2)Posion Cloud:\nCost: 200 Credits\nDescription: Equip a gas emitter. Fire to throw the emitter that perpetually remains throughout the round. Re-use the ability to create a toxic gas cloud at the cost of fuel. This ability can be re-used more than once and can be picked up to be redeployed.\n\n3)Toxic Screen(Signature):\nCost: Free\nDescription: Equip a gas emitter launcher. Fire to deploy a long line of gas emitters. Re-use the ability to create a tall wall of toxic gas at the cost of fuel. This ability can be re-used more than once.\n\n4)Viper's Pit(Ultimate):\nPoints: 7\nDescription: Equip a chemical sprayer. Fire to spray a chemical cloud in all directions around Viper, creating a large cloud that reduces the vision range of players and maximum health of enemies inside of it. Hold the ability key to disperse the cloud early.\n ")
            print("\nPress Enter to Continue")
            input()
        elif vchoice == '14':
            print("Returning")
            time.sleep(1)
            return
        else:
            print("Please select a number between 1-14")
            continue
        

def Arcade():
    print("Welcome to the Arcade\n")
    while(1==1):
        print("What would you like to play today\n")
        print("1)Hangman\n2)Rock,Paper,Scissors\n3)Scramble\n4)BlackJack\n5)Exit\n")
        achoice = input()
        if achoice == '1':
            print("\nLaunching Hangman\n")
            time.sleep(1)
            clear()
            Hangman()
        elif achoice == '2':
            print("\nLaunching Rock Paper Scissors\n")
            time.sleep(1)
            clear()
            RockPaperScissors()
        elif achoice == '3':
            print("\nLaunching Scramble\n")
            time.sleep(1)
            clear()
            Scramble()
        elif achoice == '4':
            print("\nLaunching BlackJack\n")
            time.sleep(1)
            clear()
            BlackJack()
        elif achoice == '5':
            print("Exiting Application\n")
            time.sleep(1)
            clear()
            return
        else:
            print("Choose between 1-5")
            time.sleep(1)
            clear()


def Tools():
    print("Welcome to Tools")
    while (1 == 1):
        print("\nWhat would you like to use\n\n1.Roll The Dice \n2.Flip a Coin \n3.Calculator \n4.Stop Watch \n5.Timer \n6.Exit\n")
        bchoice = input()
        if bchoice == '1':
            print("\nLaunching Roll The Dice")
            time.sleep(1)
            clear()
            Roll()
        elif bchoice == '2':
            print("\nLaunching Flip a Coin")
            time.sleep(1)
            clear()
            Flip()
        elif bchoice == '3':
            print("\nLaunching Calculator")
            time.sleep(1)
            clear()
            Calculator()
        elif bchoice == '4':
            print("\nLaunching Stop Watch")
            time.sleep(1)
            clear()
            StopWatch()
        elif bchoice == '5':
            print("\nLaunching Timer")
            time.sleep(1)
            clear()
            Timer()
        elif bchoice == '6':
            clear()
            return            
        else:
            print("Choose between 1-6")
            time.sleep(1)
            clear()

#main
if __name__ == "__main__":    
    print("\nHello\n")
    print("Launching Omni-Tool\n")
    while(1==1):
        print("What would you like to access")
        print("\n1)Arcade \n2)Tools \n3)Valorant Character Guide \n4)Exit\n")
        print("Enter the number you want to access.")
        choice = input()
        if choice == '1':
            print("\nLaunching Arcade\n")
            clear()
            Arcade()
        elif choice == '2':
            print("\nLaunching Tools\n")
            clear()
            Tools()
        elif choice == '3':
            print("\nLaunching Valorant Character Guide\n")
            clear()
            Vguide()
        elif choice == '4':
            print('\nShutting Down\n')
            clear()
            exit()