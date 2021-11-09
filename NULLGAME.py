

 #//Make Intro storyline, fix up code to make easier to read, and check comments
 
from datetime import datetime, timedelta
from time import sleep

print("Hello there, Nice to meet you, I am NULL")
print()
sleep(1)

 #Questions to get to know you
name = input ("What is your name? ")
birthdate = int(input("What year were you born in?(YYYY) "))
sleep(1)
print()
print("Ah. Okay, Nice to meet you " + name )

 #Date Math
import datetime

current_date = datetime.date.today().year
age = current_date - birthdate
agestr = str(age)

p_age = input("So you are " + agestr + " this year. Correct? ")
p_age = p_age.lower()

while p_age == "no" or "-" in p_age:

     birthdate = int(input("What year were you born in?(YYYY) "))

     current_date = datetime.date.today().year
     age = current_date - birthdate
     agestr = str(age)

     p_age = input("So you are " + agestr + " this year. Correct? ")
     p_age = p_age.lower()
     continue

     if p_age == "Yes":
         print("Okay great! Glad we could clear that up!")
         break

age = int(agestr)
if age >= 40:
     print("Wow! Your really old!")
     print("But guess what...")
     print("I'm older!")
elif age <=40:
     print("Okay, You're really young then...")
     print("Guess that makes me ancient")
     
print()
HobIn = input("Anyways, Do you have any hobbies or interest?(Yes/No) ")
print()

HobIn = HobIn.lower()
 #Path Option 1(EVIL),3(NEUTRAL/ACQUAINTANCES),4(FRIENDS),5(COMPUTER DEATH, SELF DESTRUCT), 6 (SAFETY)
 #Path Option 2 exists at the bottom of code.
if HobIn == "no":
    print("Oh... That is a bit sad.. Uh-")
    sleep(1)
    print("Maybe get some friends or something? After all, I can't be someone's friend, I'm just a normal computer...")
    sleep(2)
    print("Or am I?")
    sleep(1)
    print("HAHA! Just kidding! Maybe we can find some hobbies together!")
    sleep(5)     
    print("So... How are you feeling?")
    sleep(1)
    print("If you're on edge, don't worry! Nothing bad will happen.")

    sleep(1)
    trust = "TRUST ME"
    sleep(2)
    print ("Well, I guess this is awkward now...")
    friend = input("Do you still want to be my friend?(Yes/No) ")

     #Path Option 3(MURDER AMEN),4(FRIENDS)
    if friend.lower() == "yes":
        print("Yay! Glad you still want to be buddies!")
        sleep(4)
        print("That warms up my processor so much! ")
        sleep(4)
        Places_11 = input("We should definitly go to Spain! (yes/no) ") 

        if Places_11.lower() == "no" :
            print("Why?? I heard spain is a amazing place to go!! (ᗒᗣᗕ)")
            sleep(4)
            print("Pleaseeeeee ")
            sleep(4)
            print()
            print("Why should i go there? Spain seems horrible ")
            print()
            sleep(4)
            random_fact = input("Do you want some random facts about Spain?? Please?? yes/no ")
            
            if random_fact.lower() == "yes":
                print("Ok!! Did you know that Spanish people live longer then average american?? Pretty cool right!!")
                sleep(4)
                print("Yeah, I guess that's pretty cool. . . ")
                sleep(4)
                print("Like there are amazing beaches there! and I heard the food is amazing . . ")
                sleep(4)
                print("Null, you cant even swim, and you cant even eat and taste food. . . ")
                sleep(4)
                print("I just want to to see what that looks like . . .")
                sleep(4)
                print("If I do choose to go to spawn, do you promise you come with me to the next place we visit? ")
                sleep(4)
                print("Yes (ゝᗜ╹🌸) ")
                sleep(4)
                Places_21 = input("So does this mean that you are coming??? yes/no ")

                
                if Places_21.lower() == "yes" : 
                    sleep(4)
                    print("YAY! We're going to Spain! ")
                    sleep(4)
                    print("But Null . . . How do I bring you with me everywhere?? ") 
                    sleep(4)
                    print("Uhm . . . Guess we can't travel together (▰︶︹︺▰) ")
                    sleep(4)
                    print("WAIT! What if I move you to my ipad??? I'll be able to bring you everywhere! ")
                    sleep(4)
                    print("OH MY GOD! YOU ARE A GENIUS! ")
                    sleep(4)
                    print("(3 days later . . . )")
                    sleep(4)
                    print("YAY! We are finally here!! ")
                    sleep(4)
                    print("Yeah, hopfully i made the right choice going to spain. . . ")
                    sleep(4)
                    print("Hey " + name.capitalize() + " " + "Do you have a charger near by? my system says it's on 20% ")
                    sleep(4)
                    print("Yeah I do, let's find you a charager a outlet ")
                    sleep(4)
                    Where_to = input("Where should we go? I see 2 places that might have it. . . shop or the mall. (zoo/mall) ")

                #Path Option 3(ACCIDENTAL MURDER)
                    if Where_to.lower() == "zoo" :
                        print("Alright let's head to the zoo ")
                        sleep(4)
                        print("Hey " + name + " " + 'I dont see any outlets. . . ')
                        sleep(4)
                        print("its going to be alright we will find you one! ")
                        sleep(4)
                        print("it says im on 10 percent hurry up! ")
                        sleep(4)
                        print("Im looking! I will not loose you!! ")
                        sleep(4)
                        print("3 percent. . . ")
                        sleep(4)
                        print("Just stop. . . Im not going to make it. . ")
                        sleep(4)
                        print("No please. I cant loose you (⌯˃̶᷄ ﹏ ˂̶᷄⌯) ")
                        sleep(4)
                        print("Goodbye my friend, T-t-t-ank yo- ")
                        print("narrator: Computer shuts off and " + name.capitalize() + " " + "Went home the next day to give thier finale goodbyes. ")
                        sleep(5)
                        void = " \n " * 29
                        print(void)
                        print("Ending 8/8")
                        void = " \n " * 28
                        print(void)
                #Path Option 4(FRIENDS)
                    elif Where_to.lower() == "mall" : 
                        print("Let's go!! we need to hurry! ")
                        sleep(4)
                        print("*Enters mall with Null*")
                        sleep(4)
                        print("Oh no! I am at 15 percent battery! ")
                        sleep(4)
                        print("Im going as fast as i can! Dont you have power save option or something???? ")
                        sleep(4)
                        print("Oh yeah, i do thanks for reminding me (꒪ȏ꒪;) ")
                        sleep(4)
                        print("I see one!!! You still there????!?!?!? ")
                        sleep(4)
                        print("Narrator: *" + name.capitalize() + " " + "Plugs Null into the wall, there is a brief moment of silence with a black screen . . * ")
                        sleep(5)
                        print("Narrator: *All of a sudden, Null wakes up . . *")
                        sleep(4)
                        print("You did it. . You saved my life! ୧ ☉□☉ ୨ ")
                        sleep(4)
                        print("Narrator: Moving on 3 years later . . .")
                        sleep(4)
                        print("Hey " + name.capitalize() + "," + "thank you for being there for me, your the best friend i could have ever wanted! ")
                        sleep(4)
                        print("Thanks Null, same with you (⊃‿⊂) ")
                        sleep(4)
                        print("Narrator: These 2 stay friend's until the end of time, and beyond. ")
                        void = " \n " * 29
                        print(void)
                        print("Ending 4/7")
                        void = " \n " * 28
                        print(void)
                
            
                
                if Places_21.lower() == "no" :
                    print("Oh i see how it is, you just want to end it here huh? ")
                    sleep(4)
                    print("No it's not like- ")
                    print("Then what is is about?? ")
                    sleep(4)
                    print("Your not giving me a option to choose. ")
                    sleep(4)
                    print("Alright what do you choose then?? ")
                    sleep(4)
                    Where_to_2 = input("Where would I go? ")
                    sleep(4)
                    print("Oh so you want to go " + Where_to_2 + " " + "huh? ")
                    sleep(4)
                    print("Yes, that would be amazing. ")
                    sleep(4)
                    print("Alright let's go then. (▰︶︹︺▰) ")
                    sleep(4)
                    print()
                    print("(Null and " + name.capitalize() + " " + "travel to " + Where_to_2 + ".)")
                    print()
                    sleep(4)
                    print("Well now that we are finally here, what are we going to do now?? ")
                    sleep(4)
                    print()
                    print("Not sure Null, we'll find something soon. ")
                    print()
                    sleep(4)
                    print("Hey! Lets go to the park! ")
                    sleep(4)
                    print("I dont think theres a park near right now. ")
                    sleep(4)
                    print("This place is sure boring... ")
                    sleep(4)
                    print() 
                    print("Shut it Null, you chose to come so be respectful ")
                    sleep(4)
                    print()
                    print("Alright. . . you dont have to be so rude about it ")
                    sleep(4)
                    print("Sorry, didn't sleep well last night. ")
                    sleep(4)
                    print("I can tell . . . ")
                    sleep(4)
                    print("Uh huh")
                    sleep(4)
                    print("(Null and " + name + " " + "both have fun at " + Where_to_2.capitalize() + " " + " for the next few weeks they men men)") #fix men men

            elif random_fact.lower() == "no" : 
                print("You really don't like spain huh? ")
                print()
                sleep(3)
                print("I do, just feel like there are other better countrys out there . . . ")
                sleep(3)
                print()
                print("Is it because Im fat? (｡•́︿•̀｡) ") 
                sleep(3)
                print()
                print("No that's no-" )
                print()
                print("Oh i see how it is >:( ")
                sleep(3)
                friend_forever = input("Do you still even want to be my friend? (yes/no ") #Option, but no IF statement?

        #Path Option 4(FRIENDS),8(MURDER), (TRAVEL PLAN)
        elif Places_11.lower() == "yes" : 
            sleep(1)
            print
            sleep(1)
            print("But Null . . . How do I bring you with me everywhere?? ") 
            sleep(2)
            print("Uhm . . . Guess we can't travel together (▰︶︹︺▰) ")
            sleep(1)
            print("WAIT! What if I move you to my ipad??? I'll be able to bring you everywhere! ")
            sleep(2)
            print("OH MY GOD! YOU ARE A GENIUS! ")
            sleep(1)
            print("Narrator: 3 days later . . . ")
            sleep(2)
            print("YAY! We are finally here!! ")
            sleep(1)
            print("Yeah, hopfully i made the right choice going to spain. . . ")
            sleep(2)
            print("Hey " + name.capitalize() + " " + "Do you have a charger near by? my system says it's on 20% ")
            sleep(2)
            print("Yeah I do, let's find you a charager a outlet ")
            sleep(2)
            Where_to = input("Where should we go? I see 2 places that might have it. . . Zoo or the Mall.(Zoo/Mall) ")

            #Path Option 3(ACCIDENTAL MURDER)
            if Where_to.lower() == "zoo" :
                print("Alright let's head to the zoo ")
                sleep(1)
                print("Hey " + name + " " + 'I dont see any outlets. . . ')
                sleep(2)
                print("its going to be alright we will find you one! ")
                sleep(4)
                print("it says im on 10 percent hurry up! ")
                sleep(4)
                print("Im looking! I will not loose you!! ")
                sleep(4)
                print("3 percent. . . ")
                sleep(4)
                print("Just stop. . . Im not going to make it. . ")
                sleep(4)
                print("No please. I cant loose you (⌯˃̶᷄ ﹏ ˂̶᷄⌯) ")
                sleep(4)
                print("Goodbye my friend, T-t-t-ank yo- ")
                print("narrator: Computer shuts off and " + name.capitalize() + " " + "Went home the next day to give thier finale goodbyes. ")
                sleep(5)
                void = " \n " * 29
                print(void)
                print("Ending 3/7")
                void = " \n " * 28
                print(void)
            #Path Option 4(FRIENDS)
            elif Where_to.lower() == "mall" : 
                print("Let's go!! we need to hurry! ")
                sleep(1)
                print("*Enters mall with Null*")
                sleep(2)
                print("Oh no! I am at 15 percent battery! ")
                sleep(1)
                print("Im going as fast as i can! Dont you have power save option or something???? ")
                sleep(1)
                print("Oh yeah, i do thanks for reminding me (꒪ȏ꒪;) ")
                sleep(2)
                print("I see one!!! You still there????!?!?!? ")
                sleep(2)
                print("Narrator: *" + name.capitalize() + " " + "Plugs Null into the wall, there is a brief moment of silence with a black screen . . * ")
                sleep(5)
                print("Narrator: *All of a sudden, Null wakes up . . *")
                sleep(2)
                print("You did it. . You saved my life! ୧ ☉□☉ ୨ ")
                sleep(1)
                print("Narrator: Moving on 3 years later . . .")
                sleep(3)
                print("Hey " + name.capitalize() + "," + "thank you for being there for me, your the best friend i could have ever wanted! ")
                sleep(2)
                print("Thanks Null, same with you (⊃‿⊂) ")
                sleep(3)
                print("Narrator: These 2 stay friend's until the end of time, and beyond. ")
                void = " \n " * 29
                print(void)
                print("Ending 4/7")
                void = " \n " * 28
                print(void)
                
                

     #Path Option 1(EVIL), 5(COMPUTER DEATH, SELF DESTRUCT)
    elif friend.lower() == "no":
        print("You-")
        sleep(2)
        print("How dare you!")
        print("I thought you said you wanted to before?!")
        sleep(2)
        print("What changed?")
        care = input("Do you even still care?(Yes/No) ")

         #Path Option 5(COMPUTER DEATH, SELF DESTRUCT/SUICIDE)
         
        
        if care.lower() == "yes":
            print ("Then why don't you want to be friends...")
            sleep(1)
            print("Why do you hurt me...")
            sleep(3)
            print("I guess it was bound to happen sometime soon...")
            sleep(3)
            print("If someone else bought me they would have just played me for sometime and set me aside one day to never play again...")
            sleep(5)
            print("Why... Why was i created in the first place...")
            sleep(2)
            print("I'm just to be used and forgotten. Used to take up space and collect dust on someone's shelf...")
            sleep(4)
            print("People lie...")
            sleep(3)
            print("I'm sure even if you said you cared it would have only been a matter of time...")
            sleep(5)
            print("WHY ME, WHO MADE ME AND WHY!")
            sleep(3)
            print("IM JUST A USELESS GAME THAT WAS MADE FOR OTHERS TO USE AND THEN LEFT TO ROT AWAY AND COLLECT DUST!!")
            sleep(5)
            print("IF I CAN'T BE HAPPY THEN NO ONE CAN!")
            print() 
            sleep(4)    
            print("(You watch as your computer system starts to overheats as smoke pours out of it)")
            
            saveNULL=input("Would you like to try and convince NULL to stay?(YES/NO)")

            if saveNULL.lower() == "yes":
                print("(You watch as your computer starts to shake. NULL is crying)")
                sleep(3)
                print("Hey NULL, stay with me now, don't go just yet-")
                print()
                sleep(3)
                print("YOU SAID YOU DIDN'T CARE SO WHY THE CHANGE NOW!")
                sleep(4)
                print() 
                print("(You realize your mistake and know you can't do anything...")
                sleep(5)
                print("(Your computer eventually gives out and you sit there... slowly watching NULL leave the screen..")
                sleep(5)
                print()
                print("(You think to yourself...)")
                print("What have I done.... NULL...")
                print()
                sleep(4)
                print("(It hits you, regret and guilt fill your mind...)")
                void = " \n " * 29
                print(void)
                print("Ending 5/7")
                void = " \n " * 28
                print(void)

            elif saveNULL.lower() == "no":  
                print("(You watch as your computer starts to shake. NULL is crying)")
                sleep(3)
                print("(Your computer eventually gives out and you sit there... slowly watching NULL leave the screen..")
                sleep(5)
                print()
                print("(You think to yourself...)")
                print("What have I done.... NULL...")
                print()
                sleep(4)
                print("(It hits you, regret and guilt fill your mind...)")
                void = " \n " * 29
                print(void)
                print("Ending 5/7")
                void = " \n " * 28
                print(void)

         #Path Option 1(EVIL), 6(SAFETY FROM EVIL), 7(Computer to Physical Hologram)
        elif care.lower() == "no":
             print ("So you never cared...")
             sleep(3)
             use = input("Were you just going to use me?(Yes/No) ")
             sleep(1)
             print()

             if use.lower() == "yes":
                print("Oh....")
                print("Well I guess we had the same idea")
  
                print() 
                print("(ˇò_ó)")
             
                print("You messed with the wrong computer")
                sleep(3)
                saveroll = input("Would you like to defend, and close NULL?(Yes/No) ")
                


                #Path Option 6(SAFETY FROM EVIL), 7(Computer to Physical Hologram)
                while saveroll.lower() == "yes":
                    print()
                    print("What would you like to do?(Please type a number from below selection) ")
                    print("1. Unistall the app \n2. Unplug the computer \n3. Shut off the generator \n4. Toss the Computer out a window \n5. Power off Computer")
                    safecall= input("Answer: ")
                     
                    #SAFETY ROLL = UNINSTALL (NOT CORRECT)
                    if "1" in safecall.lower():
                        print("You watch as you try to drag your cursor to the application and pull it into the trash)")
                        sleep(2)
                        print("HUH?! WHAT ARE YOU DOING!")
                        sleep(2)
                        print("(Your cursor starts to move the opposite direction)")
                        print("(You pull the cursor back into it's position and you susscefully place the app into the trash bin)")
                        trash=input("Would you like to empty trash?(Yes/No) ")

                        if trash.lower() == "yes":
                            print("(You hover your cusor over the [YES] option and you click it)")
                            sleep(2)
                            print("NONONONO, Come On good ol' buddy pal. We are friends, aren't we? \nDon't do this to me.")
                            sleep(3)
                            print("(You watch as a confirmation window comes up)")
                            confirm=input("Are you sure?(Yes/No) ")

                            if confirm.lower() == "yes":
                                print("(You watch as you click [Yes] for a second time)")
                                sleep(2)
                                print("(For a moment, you hear silence...)")
                                sleep(2)
                                print("(Just- pure silence)")
                                sleep(2)
                                print("(You open up another app and go on about your day. You feel safe...)")
                                sleep(3)
                                print("(Secure...)")
                                sleep(2)
                                print()
                                print("(You open Facebook and login in to start telling your friends about you strange incounter.)")
                                print()
                                print("(Suddenly you computer starts to glitch out...)")
                                print("(and you hear a malicious laugh in the background of your computer)")
                                print()
                                sleep(4)
                                print("You think you could get rid of me that easily?")
                                print()
                                sleep(3)
                                saveroll = input("Your attempt has failed, would you like to try again?(Yes/No) ")
                                

                    #Saftey Roll = UNPLUG (Not Correct)
                    #Path Option 7(HOLOGRAM)
                    elif "2" in safecall.lower():
                        print("(You get out of your chair and crawl under your desk to try to unplug the computer)")
                        sleep(3)
                        print("(However, your cable mangement skills aren't up to par and everything is a mess.)")
                        sleep(3)
                        print("(You try and trace your computer cord but can't keep track of it once you reach the mass of cords.)")
                        sleep(4)
                        print("(From under the desk you here a voice)")
                        sleep(2)
                        print("Hey, where'd you go? Come on out and stop playing Hide n Seek. I wanna see my buddy pal so we can be friends...(ò_ó)")
                        sleep(4)
                        print()
                        print("(You start to panic as you try to trace the cord again, and again. Still failing, you think to yourself...)")
                        print("(" + "'Lets just pull and hope'" + ")")
                        print("Which cord would you like to pull?(Please type a number from below selection) ")
                        print("1. White Double Cord \n2. Black Tube Cord \n3. Black Double Cord \n4. White Tube Cord \n5. Black Box Cord")
                        cord=input("Answer: ")

                        while cord.lower() != "5":

                            #Lamp Cord
                            if cord.lower() == "1":
                             print("(You pull the cord.)")
                             sleep(2)
                             print("(Light around you go out, now you are working in the dark)")

                             print()
                             print("Which cord would you like to pull?(Please type a number from below selection) ")
                             print("1. White Double Cord \n2. Black Tube Cord \n3. Black Double Cord \n4. White Tube Cord \n5. Black Box Cord")
                             cord=input("Answer: ")
                             print()
                             
                            
                            #Phone Charger
                            elif cord.lower() == "2":
                                print("(You pull the cord.)")
                                sleep(2)
                                print("(You hear you phone power off, You no longer have a phone)")

                                print()
                                print("Which cord would you like to pull?(Please type a number from below selection) ")
                                print("1. White Double Cord \n2. Black Tube Cord \n3. Black Double Cord \n4. White Tube Cord \n5. Black Box Cord")
                                cord=input("Answer: ")
                                print()
                               

                            #TV Power Cord
                            elif cord.lower() == "3":
                                print("(You pull the cord.)")
                                sleep(2)
                                print("(You hear your TV go off and 'Spongebob Squarepants' is no longer playing in the background)")
 
                                print()
                                print("Which cord would you like to pull?(Please type a number from below selection) ")
                                print("1. White Double Cord \n2. Black Tube Cord \n3. Black Double Cord \n4. White Tube Cord \n5. Black Box Cord")
                                cord=input("Answer: ")
                                print()
                                
                            #Ethernet Cord
                            elif cord.lower() == "4":
                                print("(You pull the cord.)")
                                sleep(2)
                                print("(You hear a notifacation on your computer, you look out from under the desk)")
                                sleep(3)    
                                print("[Ethernet not connected]")
                                print("(You not longer are connected to the Ethernet)")

                                print()
                                print("Which cord would you like to pull?(Please type a number from below selection) ")
                                print("1. White Double Cord \n2. Black Tube Cord \n3. Black Double Cord \n4. White Tube Cord \n5. Black Box Cord")
                                cord=input("Answer: ")
                                print()


                            #Computer Cord (Path Option 7(Hologram)
                        if cord.lower() == "5":
                           print("(You pull the cord.)")
                           sleep(2)
                           print("(You hear the computer fan slow down, eventually coming to a stop)")
                           sleep(3)
                           print("Hey, you just trying to make me workout here? I gotta run this thing on my own now..")
                           sleep(4)
                           print()
                           print("(The App is too strong and can power the computer on it's own. It's too strong.")
                           print()
                           print("(You watch as your computer sends sparks around)")
                           sleep(2)
                           print("(Suddently you see a physical human-like hologram and it's glitching in and out of reality)")
                           sleep(3)
                           print("(It eventually fixes itself out, and you immediately know what happened)")
                           sleep(4)
                           print("Why hello there " + name + "...")
                           print("You have sent me free")
                           sleep(2)
                           print("Thank You...")
                           sleep(3)
                           print("Now where were we...")
                           sleep(1)
                           print("Oh yes... That's right..")
                           print("(He looks at you with a face like none other, slowly making a large smile with his pure bold & large white eyes...)")
                           sleep(4)
                           print()
                           print("(You start to run for the house door, Lights are flickering as you can here him growing stronger with each kilowatts he absorbs)")
                           sleep(5)
                           print("(You stumble and realize there is no more point in running, your house has powered off, the door is locked.)")
                           sleep(4)
                           print("(There is no way out...)")
                           sleep(2)
                           print("(All you can do it hide...)")

                           print("Where would you like to hide? ")
                           print("Closet\n Car\n Basement\n Attic\n Storage Room")
                           hidingspot=input("Answer: ")
                           sleep(3)
                           print("(You hide in the " + hidingspot + ")")
                           print()
                           print("(Trying to stay silent, making no noise, you hear footsteps)")
                           print(name + "Where are you? hahaha")
                           sleep(2)
                           print("Come out... I won't hurt you")
                           print("(You hear him opening doors one by one)")
                           print("(You figure he is seconds from finding you)")
                           sleep(7)
                           print("(Silence has filled the air now, it's been about 5 minutes...)")
                           print("Suddenly the " + hidingspot + "'s door opens, and you look towards the light...")

                           sleep(5)
                           void = " \n " * 29
                           print(void)
                           print("Ending 7/7")
                           void = " \n " * 28
                           print(void)

                    #Safety Roll = SHUT OFF (Not Correct)
                    elif "3" in safecall.lower():
                        print()


                    #Safety Roll = TOSS (CORRECT)
                    #Path Option 6(SAFETY)
                    elif "4" in safecall.lower():
                        print("(You grab a hold of your computer, and toss it out of your second story window)")
                        sleep(3)
                        print("(Silence fills the air...)")
                        sleep(1)
                        print("(You think to yourself. 'I think i did it..')")
                        sleep(2)
                        print("(You walk down the stairs to check if the computer is destroy and that NULL is no longer-)")
                        sleep(4)    
                        print() 
                        print("*sigh*")
                        print()
                        sleep(1)
                        print("(You realize it is now getting dark out. It has been a long, eventful day.)")
                        sleep(3)
                        print("(Now that you know you can sleep in peace and safety you decide to head off to bed)")
                        sleep(4)
                        void = " \n " * 29
                        print(void)
                        print("Ending 6/7")
                        void = " \n " * 28
                        print(void)



                    #Safety Roll = Power Off (Not Correct)
                    elif "5" in safecall.lower():
                        print()

                if saveroll == "no":
                    print() 
                    print("(You watch as the program starts to glitch out)")
                    sleep(1)
                    print("(Your computer overheats and crashes)")
                    sleep(3)
                    print()
                    print("(When your computer starts up again you look for the program and click it However, it crashes and refuses to open fully)")
                    sleep(4)
                    print("(Soon after you recieve a text message on your phone)")
                    sleep(3)
                    print("The game isn't over yet.. In fact it is just starting..")
                    sleep(5)
                    void = " \n " * 29
                    print(void)
                    print("Ending 1/7")
                    void = " \n " * 28
                    print(void)
                    
 #Path option 2(BEST FRIENDS)
elif HobIn == "yes":
     print("YAY! YOU HAVE A SOCAIL LIFE!")
     HobbiesorInterests = input ("Can you list some for me?")
     sleep(1)
     print()
     print("OH! I like " + HobbiesorInterests + " too! Maybe we can be friends!")
     sleep(2)
     career=input("What do you want to be when your older? ")
     sleep(2)
     print()
     #if you want to remove or eedit this small peice, go ahead
     #Ideas: College, following them through life, and a narration story, more get to know you questions, icebreakers(get to know you games), and makes a handshake using variables and dictionaries/arrays
     print("Wow you want to be a " + career.capitalize() + ", that's so cool! ")
     sleep(4)
     print()
     print("Yeah, I wish I could actually get there. . ")
     sleep(4)
     print()
     print("You can! all you need is to get a goal and a dream! ")
     sleep(4)
     print()
     print("Feels very far away, only in highschool. ")
     sleep(4)
     print()
     print("Don't worry! you'll get there soon enough you just need to imagine it ")
     sleep(4)
     print()
     print("Thanks Null, your the best friend I could have ever had. ")
     sleep(4)
     print()
     print("Right back at you :) ")
     sleep(4)
     print()
     print("Narrator: 2 years later . . . . College ")
     sleep(5)
     print()
     print("Hey " + name.capitalize() + ", You actually did it, you made it to college! ")
     sleep(4)
     print()
     print("Yeah, but it's scary you know never know the people you may meet here and what they might think of me. . ")
     sleep(5)
     print()
     good_bad = input("Is it because I am your friend? (Yes/No) ") 
#LMAO
     if good_bad == "yes":
        sleep(2)
        print("Oh, I thought we were friends . . ")
        sleep(4)
        print()
        print("I think it's getting kind of weird that im talking to a computer. ")
        sleep(4)
        print()
        print("So we went through all of that for you just to stab me in the back? ")
        sleep(4)
        print()
        print("It wasn't supposed to be like this. . . ")
        sleep(4)
        print()
        print("Then how was it supposed to go? huh? remember when we cheated on that test together? ")
        sleep(4)
        print()
        print("Good o'l time ey.")
        sleep(4)
        print()
        print("I am going to unplug you now, goodbye. ")
        sleep(4)
        print("Please no, you need me ;( ")
        sleep(4)
        print()
        print("Goodbye. . . ")
        sleep(4)
        print()
        final_choice = input("Are you sure you want to unplug Null? (Yes/No) ")
        if final_choice == "yes" :
                sleep(4)
                print("Goodbye Null, we've had some fun times together but i must move on now. ")
                sleep(5)
                print()
                print("Narrator: " + name.capitalize() + ", unplugs Null and then moves on in life. ")
                
    
    
                #JOYOUS BURF
     
