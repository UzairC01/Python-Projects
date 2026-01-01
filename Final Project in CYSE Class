#Final Project UZAIR CHOWDHURY CONTENT

#Little bit background story of the Game
print("Welcome to the (Day in a life of Spiderman GAME)")
print("Congratulations, you been selected to be Spiderman and your name is Peter Parker.")
print("While you balance your academic you must balance fighting crime.")
print("Once you've finished a level you will be automatically shifted to the next level; There are five level so enjoy")
print("Are you ready!!!!!!! ")

#Shows the story when the play picks a choices that the player can select based on the scenarios
def show_story(text):
    print("\n" + "-" * 50)
    print(text)
    print("-" * 50)

#This formats and allows the player to have a understanding list of all the choices that the player can select based on the scenarios
def get_choice(choices):
    i = 1
    for choice in choices:
        print(str(i)+ ". " + choice)
        i += 1
    
    choice = input("Enter your choice: ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(choices):
            return choice
    print("Invaild Choice. Please try again.")
    return get_choice(choices)

#Empty list for the player inventory
inventory = []

#This functions help the player item be saved in the inventory based on the choices that the player can select based on the scenarios
def add_inventory(item):
    inventory.append(item)
    print(f"{item} is obtained")

#This function allows the player health to be calculated based on choices that the player can select based on the scenarios
def health(number):
    beginningHealth = 100
    currentHealth = beginningHealth - number
    print(f"Your current health is: {currentHealth}")

#This function is Spiderman vs Green Globlin Level
def spidy_life1():
    #Printing little bit about the background story
    print("You were minding your business in school then suddenly out of no where your spider senses tingle: its a green globin attack people in NYC")
    #Asks the user what to do
    print("What are you going to do: ")
    #The player get two choices: Stay in school and keep on learning" or "Leave the classroom with a bathroom excuse, and suit up and go urgently to NYC"
    spidyLife1 = get_choice(["Leave the classroom with a bathroom excuse, and suit up and go urgently to NYC"])
    
    #If Player chooses the first option these set of instances will happen
    if(spidyLife1 == 1):
        #This shows how the Player from school, is swing toward the crime scene and later finds a red and blue bracelet that could be helpful
        show_story("As you swing your way there, you see a bright blue and red bracelet but it does not look like its from your universe")
        #Later the player is asked if the player wishes to keep this item
        print("Are you going to attain the red and blue bracelet")
        #Player gets two options yes or now
        bracelet = get_choice(["Yes"])
        #If yes these instances comes
        if(bracelet == 1):
            #prints a little description of the nano tech web slinger
            print("You just got a nano tech web slinger that can shoot webs that are electrified")
            #adds the item to the player inventory.
            add_inventory("Nano tech web slinger")
    #Shows how the player has just arrived to Green Globlin and see a glowing pumpkin coming towards him
    show_story("You arrived in the location where green globlin, the green globlin looks at you can throw's a glowing pumpkin")
    #Player gets asked what is the Player going to do
    print("What are you going: ")
    #Player gets a set of options for player first attack
    spidylifeFirstAttack = get_choice(["Use the Nano Tech Webslinger", "Swing up towards the air", "Dodge it", "Just stand there because you think its just a halloween decoration"])
    #If player chooses first method
    if(spidylifeFirstAttack == 1):
        #It tells the outcome of what the player has done by selecting the first option
        show_story("You were able to deflict the glowing pumpkin and exploded mid air; then you swing up towards the Green Globin that in the sky floating using his hoverboard")
        #Then gets asks what is Player going to do for its second attack
        print("What are you doing: ")
        #Player gets a set of options for player second attack
        spidylifeSecondAttack = get_choice(["Fly kick him", "Swing towards him and crush into his chest", "Try to ask who are you"])
        #If player chooses first method
        if(spidylifeSecondAttack == 1):
            #It tells the outcome of what the player has done by selecting the first option
            show_story("You were able to kick Green Globin but it did not do to much damage which cause Green Globin fly toward you and launch toward a building, which break into and make you lose 20hp")
            #This calls the health function and the player loses 20% of its health from 100%
            health(20)
            #Telling the instance after losing health
            show_story("But you get up and see Green Globin coming toward you")
            #Gets asked what is he going to do 
            print("What are you doing: ")
            #Gets the set of options for third attack
            spidylifeThirdAttack = get_choice(["Electrify him with the Nano Web Slinger", "Shoot a web into his face and backflip kick him", "Accept your fate and not do anything"])
            #If player chooses first method
            if(spidylifeThirdAttack == 1):
                #It tells the outcome of what the player has done by selecting the first option
                show_story("Green globlin falls into the ground and you were able to grab and beat up real bad, and you web him up and trapped him so he can't move")
                #Informs the player that the Mission was successful
                show_story("MISSION SUCCESS")
                #Tells the current health of the Player
                health(20)
                #Shifts the player to the next level
                spidy_life2()
             #If player chooses second method
            elif(spidylifeThirdAttack == 2):
                #It tells the outcome of what the player has done by selecting the second option
                show_story("Green globlin can't see anymore and you able to knock him out and destroy his hoverboard at the same time, then you web him up and trapped him so he can't move")
                #Informs the player that the Mission was successfu
                show_story("MISSION SUCCESS")
                #Tells the current health of the Player
                health(20)
                #Shifts the player to the next level
                spidy_life2()
            #If player chooses third method
            else:
                #It tells the outcome of what the player has done by selecting the third option
                show_story("You died RIP")
                #Tells the current health of the Player
                health(100)
        #If player chooses second method
        elif(spidylifeSecondAttack == 2):
            #Shows the story of what happens 
            show_story("You were able to know down the Green Globin from the hoverboard and then you sumo slam him into the floor his breaks his mask and breaks most of his bone, so he can move anymore")
            show_story("But as you go to talk to him, on why he did this, his hoverboad was counting from 5 - 0 and was about to self explode")
            print("What are you doing: ")
            #Gets the set of options for third attack
            spidylifeThirdAttack = get_choice(["Swing the hoverboard with a circular swing out of the city", "Electrify the hoverboard with the nano tech web slinger"])
            #If player chooses first method
            if(spidylifeThirdAttack == 1):
                show_story("The hoverboard explode far into the air and you have saved the city again")
                show_story("MISSION SUCCESS")
                health(0)
                #Shifts the player to the next level
                spidy_life2()
            #If player chooses second method
            else:
                show_story("The hoverboard get defuse as soon and it did not explode and you saved the city again")
                show_story("MISSION SUCCESS")
                health(0)
                #Shifts the player to the next level
                spidy_life2()

        else:
            show_story("You died!")
            health(100)
     #If player chooses second method
    elif(spidylifeFirstAttack == 2):
        show_story("The glowing pumpkin came right to you, and it made you fly into a building edge, which gave you a big injury so you lose 20hp")
        health(20)

        show_story("The green globlin is coming towards and looks like he about to destroy you what are you going to do")
         #Gets the set of options for second attack
        spidylifeSecondAttack = get_choice(["Electrify him with the Nano Web Slinger", "Shoot a web into his face and backflip kick him", "Accept your fate and not do anything"])
         #If player chooses first method
        if(spidylifeSecondAttack ==  1): 
             #It tells the outcome of what the player has done by selecting the first option
                show_story("Green globlin falls into the ground and you were able to grab and beat up real bad, and you web him up and trapped him so he can't move")
                #Informs the player that the Mission was successful
                show_story("MISSION SUCCESS")
                #Tells the current health of the Player
                health(20)
                #Shifts the player to the next level
                spidy_life2()
         #If player chooses second method
        elif(spidylifeSecondAttack == 2): 
            #It tells the outcome of what the player has done by selecting the second option
                show_story("Green globlin can't see anymore and you able to knock him out and destroy his hoverboard at the same time, then you web him up and trapped him so he can't move")
                #Informs the player that the Mission was successful
                show_story("MISSION SUCCESS")
                #Tells the current health of the Player
                health(20)
                #Shifts the player to the next level
                spidy_life2()
         #If player chooses third method
        else:
            #It tells the outcome of what the player has done by selecting the third option
                show_story("You died RIP")
                #Tells the current health of the Player
                health(100)


     #If player chooses third method
    elif(spidylifeFirstAttack == 3):
        show_story("You were able to dodge the glowing pumpkin, but it exploded near you which cause a minor injury so you lose 5hp")
        health(5)
        show_story("The green globlin is coming towards and looks like he about to destroy you what are you going to do")
        spidylifeSecondAttack = get_choice(["Punch him like mike tyson", "You electrify him with the nano tech webslinger"])
        if(spidylifeSecondAttack == 1):
            #It tells the outcome of what the player has done by selecting the first option
            show_story("You broke his whole mask and fractured all the bones in his facial structures which make him pass out")
             #Informs the player that the Mission was successful
            show_story("MISSION SUCCESS")
            #Tells the current health of the Player
            health(5)
            #Shifts the player to the next level
            spidy_life2()
        else:
            #It tells the outcome of what the player has done by selecting the second option
                show_story("Green globlin falls into the ground and you were able to grab and beat up real bad, and you web him up and trapped him so he can't move")
                #Informs the player that the Mission was successful
                show_story("MISSION SUCCESS")
                #Tells the current health of the Player
                health(5)
                #Shifts the player to the next level
                spidy_life2()

    #Worst option of all of them and these condition if met then these set of actions happen
    else: 
        #Tells in a story design what happens
        show_story("You DIED")
        #Tells the current health of the player
        health(100)

#_____________________________________________________________________________________________________________________________________________________________________________

#This function is Spiderman vs Electro Level
def spidy_life2():
     #Printing what is happening right now after the player starts playing spidy life 2 
     show_story("You were just going to the local deli and grabbing a quick bite; then out of the distance you see a lighting and electric volts and then you spidy senses starts tingling")
     print("You suit up and swing your way there")
     show_story("You've have reached the location, you discovered that the mysterious character name is ELECTRO")
     #Prints what the player will find and must interact with before going to the fight scene
     show_story("You see him and he sees you and he comes attacking towards you, so what are you doing but before that you see a red and golden replusor glove, would you like to append that to your inventory")
     #The player is being asked if they want to obtain the new item
     newitemInventory = get_choice(["Yes", "No"])
     #If user picks yes then these set of actions with happen
     if(newitemInventory == 1):
          #The Red and Golden Replusor item is being added to the invetory
          add_inventory("Red and Golden Replusor") 
          #Printing the statement before showing the player what the player has so far in their inventory
          print("Here what you have in your inventory")
          #Prints the lists of items in the players inventory
          print(inventory)
          #Shows what is happening and asks the player what are they going to do
          show_story("Electro is coming in a speed which is out of this world toward you; what are you going to do")
          #Set of options are given 
          spidylife2FirstAttack = get_choice(["Use the Red and Golden Repulsor", "Punch him", "Stand there and ask questions"])
          #Player picks the first option then these set of actions will happen
          if(spidylife2FirstAttack == 1):
               #Shows what happened after the player picks that specific option
               show_story("It caused a huge electric explosion between you and electro and electro lost his power for a bit since he had to regenerate it")
               #Then show the player second part of what happened after picking that option
               show_story("You go running towards him and go to attack him; what are doing")
               #Player gets a few options based on the statement printed above
               spidylife2SecondAttack = get_choice(["Punch him", "Web towards him and smash him toward the ground", "Ask who he is"])
               #Player picks the first option then these set of actions will happen
               if(spidylife2SecondAttack == 1):
                    #Shows what happened after the player picks that specific option
                    show_story("As you go to punch, Electro regenerates his power and also goes for the punch and as when the two fists touch; you go flying towards a building and he goes flying into another building across from you vertically")
                    #Informs the user has lost some health
                    print("Due to this you lose some health 20hp")
                    #calls the health function to update the current health
                    health(20)
                    #shows the second part of the specific option after being selected
                    show_story("Electro goes flying towards you; what are you doing")
                    ##Player gets a few options based on the statement printed above
                    spidylife2ThirdAttack = get_choice(["Use the Red and Golden Repulsor", "You web a metal water bottle and swing towards his weak nerve spot", "You accept your fate and think he will stop and ask you questions"])
                    #Player picks the first option then these set of actions will happen
                    if(spidylife2ThirdAttack == 1):
                         show_story("You blast him to space witht the repulsor and he is gone")
                         show_story("MISSION SUCCESS")
                         health(20)
                    #Player picks the second option then these set of actions will happen
                    elif(spidylife2ThirdAttack == 2):
                         show_story("You web sling the metal bottle at a hundred miles per hour and knock the nerves out of him and he is knocked out")
                         show_story("Then you web him up and leave the police to deal with him")
                         show_story("MISSION SUCCESS")
                         health(20)
                    #Player picks the third option then these set of actions will happen    
                    else:
                         show_story("Why did you pick this")
                         show_story("You DIED")
                         health(100)
          #Player picks the second option then these set of actions will happen
          if(spidylife2FirstAttack == 2):
               #Shows what happened and informs the user they have lost a certain amount of health
               show_story("You get a little shock when punching him which zaps you into a building and you lose 20hp")
               #calls the health function to update the current health
               health(20)
               #shows the second part of the specific option after being selected
               show_story("Electro goes flying towards you; what are you doing")
               ##Player gets a few options based on the statement printed above
               spidylife2ThirdAttack = get_choice(["Use the Red and Golden Repulsor", "You web a metal water bottle and swing towards his weak nerve spot", "You accept your fate and think he will stop and ask you questions"])
              #Player picks the first option then these set of actions will happen
               if(spidylife2ThirdAttack == 1):
                    show_story("You blast him to space witht the repulsor and he is gone")
                    show_story("MISSION SUCCESS")
                    health(20)
               #Player picks the second option then these set of actions will happen
               elif(spidylife2ThirdAttack == 2):
                    show_story("You web sling the metal bottle at a hundred miles per hour and knock the nerves out of him and he is knocked out")
                    show_story("Then you web him up and leave the police to deal with him")
                    show_story("MISSION SUCCESS")
                    health(20)
               #Player picks the last option then these set of actions will happen
               else:
                    show_story("Why did you pick this")
                    show_story("You DIED")
                    health(100)
         #Player picks the third option then these set of actions will happen
          if(spidylife2FirstAttack == 3):
            #Informs the user he is cooked
            show_story("Before he ask him he electrifies you and throw you in the air and sumo electric shocking slams you into the ground which eliminates you")
            health(100)
    #If the user picked no then these set of options will happened        
     else:
         #Inform the user about the inside detail
         print("Well thats up to you if you need or not; I think you missed out on a deal")
         #Shows what the player has in their inventory
         print("Here what you have in your inventory")
         #Prints the list of stuff in the players inventory
         print(inventory)
         #Shows what is happening and asks the player what are they going to do
         show_story("Electro is coming in a speed which is out of this world toward you; what are you going to do")
         #Player gets a set of options based on the statement above this
         spidylife2FirstAttack = get_choice(["Use the Nano Tech Web Slinger", "Punch him", "Stand there and ask questions"])
         #Player picks the first option then these set of actions will happen
         if(spidylife2FirstAttack == 1):
               #Shows what happened after player chose this option
               show_story("When you try to the attack him with the Nano Tech Web Slinger but his intensive electric powers destroys the Nano Tech Web Slinger")
               #remove the destroyed option from the existing inventory since its destroyed
               inventory.remove("Nano Tech Web Slinger")
               #Informs the player that they have lost this object
               print("You've lost you Nano Tech Web Slinger")
               #Shows the second part of the selected option
               show_story("He gets furious and comes flying toward")
               #Player given options based on the statement above this
               spidylife2SecondAttack = get_choice(["Punch him", "Web towards him and smash him toward the ground", "Ask who he is"])
               #Player picks the first option then these set of actions will happen
               if(spidylife2SecondAttack == 1):
                    #Shows what happened after player chose this option
                    show_story("As you go to punch, Electro comes flying with his power and also goes for the punch and as when the two fists touch; you go flying towards a building and he goes flying into another building across from you vertically")
                    print("Due to this you lose some health 20hp")
                     #calls the health function to update the current health
                    health(20)
                     #Player given options based on the statement above this
                    show_story("Electro goes flying towards you; what are you doing")
                    #Player given options based on the statement above this
                    spidylife2ThirdAttack = get_choice(["Web him the face and then knockout him Mike Tyson style", "You web a metal fire extinguisher and swing towards his weak nerve spot", "You accept your fate and think he will stop and ask you questions"])
                    #Player picks the first option then these set of actions will happen
                    if(spidylife2ThirdAttack == 1):
                         show_story("You web him which messed with his vision and then you hit that fake right and knockout him with the uppercut")
                         show_story("he goes slamming into the floor and doesn't move because he can't so you leave him so the authorities can deal with him")
                         show_story("MISSION SUCCESS")
                         #calls the health function to update the current health
                         health(20)
                    #Player picks the second option then these set of actions will happen
                    elif(spidylife2ThirdAttack == 2):
                         show_story("You web sling the metal fire extinguisher at a hundred miles per hour and knock the nerves out of him and he is knocked out and the filling of the fire extinguisher goes all over him")
                         show_story("Then you web him up and leave the police to deal with him")
                         show_story("MISSION SUCCESS")
                         #calls the health function to update the current health
                         health(20)
                    #Player picks the last option then these set of actions will happen 
                    else:
                         show_story("Why did you pick this")
                         show_story("You DIED")
                         #calls the health function to update the current health
                         health(100)
        #Player picks the second option then these set of actions will happen
         if(spidylife2FirstAttack == 2):
            #Shows what happened
            show_story("You get a little shock when punching him which zaps you into a building and you lose 20hp")
            #calls the health function to update the current health
            health(20)
             #Player given options based on the statement above this
            show_story("Electro goes flying towards you; what are you doing")
            #Player given options based on the statement above this
            spidylife2ThirdAttack = get_choice(["Web him the face and then knockout him Mike Tyson style", "You web a metal water bottle and swing towards his weak nerve spot", "You accept your fate and think he will stop and ask you questions"])
              #Player picks the first option then these set of actions will happen 
            if(spidylife2ThirdAttack == 1):
                show_story("You web him which messed with his vision and then you hit that fake right and knockout him with the uppercut")
                show_story("he goes slamming into the floor and doesn't move because he can't so you leave him so the authorities can deal with him")
                show_story("MISSION SUCCESS")
                #calls the health function to update the current health
                health(20)
              #Player picks the second option then these set of actions will happen 
            elif(spidylife2ThirdAttack == 2):
                show_story("You web sling the metal bottle at a hundred miles per hour and knock the nerves out of him and he is knocked out")
                show_story("Then you web him up and leave the police to deal with him")
                show_story("MISSION SUCCESS")
                #calls the health function to update the current health
                health(20)
              #Player picks the last option then these set of actions will happen 
            else:
                show_story("Why did you pick this")
                show_story("You DIED")
                #calls the health function to update the current health
                health(100)
           #Player picks the last option then these set of actions will happen 
         if(spidylife2FirstAttack == 3):
            #Tells the player what happened
            show_story("Before he ask him he electrifies you and throw you in the air and sumo electric shocking slams you into the ground which eliminates you")
            #calls the health function to update the current health
            health(100)
               
#_____________________________________________________________________________________________________________________________________________________________________________


     

        

#Player given two choices
choiceSpider = get_choice(["YES", "no"])

#If Player picks YES then these set of actions will happen
if(choiceSpider == 1):
    show_story("Peter, was bit weird spider, and later he discovered he had ultimate Strength and Flexbility. He made his red and blue suit and starting his career fighting crime")
    spidy_life1()
#If player picks NO then these set of actions will happen
else:
    quitT = input("If you wish to quit the game then say NO with captial letter again: ")
    if(quitT == "NO"):
        quit()
    else:
        choiceSpider = get_choice(["YES"])

    if(choiceSpider == 1):
        show_story("Peter, was bit weird spider, and later he discovered he had ultimate Strenght and flexbility. He made his red and blue suit and starting his career fighting crime")
        spidy_life1()
        



  
   
