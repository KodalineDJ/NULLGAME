

 #//
 
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
    friend = input("Do you still want to be my friend? ")

    friend= friend.lower()
     #Path Option 3(NEUTRAL/ACQUAINTANCES),4(FRIENDS)
    if friend == "yes":
        print("Yay! Glad you still want to be buddies!")
        sleep(1)
        pass
         #//Work on story paths for 3-4

     #Path Option 1(EVIL), 5(COMPUTER DEATH, SELF DESTRUCT)
    elif friend == "no":
        print("You-")
        sleep(2)
        print("How dare you!")
        print("I thought you said you wanted to before?!")
        sleep(2)
        print("What changed?")
        care = input("Do you even still care?(Yes/No) ")

        care = care.lower()
         #Path Option 5(COMPUTER DEATH, SELF DESTRUCT)
        if care == "yes":
            print ("Then why don't you want to be friends...")
            sleep(1)
            print("Why do you hurt me")
            
         #Path Option 1(EVIL), 6(SAFETY FROM EVIL), 7(Computer to Physical Hologram)
        elif care == "no":
             print ("So you never cared...")
             sleep(3)
             use = input("Were you just going to use me?(Yes/No) ")
             sleep(1)
             print()

             use = use.lower()
             if use == "yes":
                print("Oh....")
                print("Well I guess we had the same idea")
  
                print() 
                print("(ˇò_ó)")
             
                print("You messed with the wrong computer")
                sleep(3)
                saveroll = input("Would you like to defend, and close NULL?(Yes/No) ")

                saveroll=saveroll.lower()

                #Path Option 6(SAFETY FROM EVIL), 7(Computer to Physical Hologram)
                while saveroll == "yes":
                    print("What would you like to do?(Please type answer in FULL from below selection) ")
                    print("1. Unistall the app \n\ 2. Unplug the computer \n\ 3.Shut off the generator \n\ 4. Toss the Computer out a window \n\ 5. Power off Computer")
                    safecall= input("Answer: ")
                     
                    #SAFETY ROLL = UNINSTALL (NOT CORRECT)
                    if "uninstall" in safecall.lower():
                        print("You watch as you try to drag your cursor to the application and pull it into the trash)")
                        sleep(2)
                        print("HUH?! WHAT ARE YOU DOING!")
                        sleep(2)
                        print("(Your cursor starts to move the opposite direction)")
                        print("You pull the cursor back into it's position and you susscefully place the app into the trash bin")
                        trash=input("Would you like to empty trash?(Yes/No) ")

                        if trash.lower() == "yes":
                            print("You hover your cusor over the [YES] option and you click it")
                            sleep(2)
                            print("NONONONO, Come On good ol' buddy pal. We are friends, aren't we? \n\ Don't do this to me.")
                            sleep(3)
                            print("(You watch as a confirmation window comes up)")
                            confirm=input("Are you sure?(Yes/No) ")

                            if confirm.lower() == "yes":
                                print("(You watch as you click [Yes] for a second time)")
                                sleep(2)
                                print("(For a moment, you here silence...)")
                                sleep(2)
                                print("(Just- pure silence)")
                                sleep(2)
                                print("(You open up another app and go on about your day. You feel safe...")
                                sleep(3)
                                print("(Secure...)")
                                sleep(2)
                                print()
                                print("(You open Facebook and login in to start telling your friends about you strange incounter.)")
                                print()
                                print("(Suddenly you computer starts to glitch out...)")
                                print("(and you here a malicious laugh in the background of your computer)")
                                print()
                                sleep(4)
                                print("You think you could get rid of me that easily?")
                                print()
                                sleep(3)
                                saveroll = input("Your attempt has failed, would you like to try again?(Yes/No) ")
                                continue
                    #Saftey Roll = UNPLUG (Not Correct)
                    elif "unplug" in savecall.lower():
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
                        cord=input("Which cord would you like to pull?(Please type answer in FULL from below selection) ")

                        print("1. White Double Cord \n\ 2. Black Tube Cord \n\ 3. Black Double Cord \n\ 4. White Tube Cord \n\ 5. Black Box Cord")
                        while cord.lower() != "black box cord":

                            #Lamp Cord
                            if cord.lower() == "white double cord":
                             print("(You pull the cord.)")
                             sleep(2)
                             print("(Light around you go out, now you are working in the dark)")
                             cord=input("Which cord would you like to pull?(Please type answer in FULL from below selection) ")

                             print("1. White Double Cord \n\ 2. Black Tube Cord \n\ 3. Black Double Cord \n\ 4. White Tube Cord \n\ 5. Black Box Cord")
                             continue
                            
                            #Phone Charger
                            elif cord.lower() == "black tube cord":
                                print()

                            #TV Power Cord
                            elif cord.lower() == "black double cord":
                                print()
                            
                            #Cable Cord
                            elif cord.lower() == "white tube cord":
                                print()

                            #Computer Cord
                            elif cord.lower() == "black box cord":
                                break
                            print()
                    #Safety Roll = SHUT OFF (Not Correct)
                    elif "shut off" in safecall.lower():
                        print()

                    #Safety Roll = TOSS (CORRECT)
                    elif "toss" in safecall.lower():
                        print()

                    #Safety Roll = Power Off (Not Correct)
                    elif "power" in safecall.lower():
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
                    print("Ending 1/6")
                    void = " \n " * 28
                    print(void)
                    
 #Path option 2(BEST FRIENDS)
elif HobIn == "yes":
     print("YAY! YOU HAVE A SOCAIL LIFE!")
     HobbiesorInterests = input ("Can you list some for me?")
     sleep(1)
     print()
     print("OH! I like those all too! Maybe we can be friends!")