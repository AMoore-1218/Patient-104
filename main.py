from fasthtml.common import *
def play_again():
  print("\n" + "=" * 50)
  choice = input("Would you like to play again? (y/n):").lower()
  if choice == 'y' or choice == "yes":
     print("\n" + "=" * 50)
     start_game()
  else:
     print("Thank you for playing!")
def bad_ending():
  print(
        "You should've just minded your business, keep a low cover. Now, you're being dragged into a dark, cold room by two men dressed in all white lab coats, never to be seen again."
  )
  print(
        "You've got the bad ending. Would you like to play again to get a new ending?"
  )
  play_again()
def good_ending():
  print(
        "You managed to get out of the hospital with everything you came in with…give or take. Maybe next time avoid random places advertising free cream cheese bagels."
  )
  print(
        "You got the good ending. Would you like to play again to get a new ending?"
  )
  play_again()
def secrets_ending():
  print(
        "You found a book of all sorts of twisted documents, detailing all the terrible things these people came up with in here. Who knows how many more they'll be going after! It's time to tell the world what you saw…"
  )
  print(
        "You've got the secrets ending. Would you like to play again to get a new ending?"
  )
  play_again()
def traitor_ending():
  print(
        "You're really willing to give up your morals just to save your own hide, huh? Not like you can change it, you're one of them now, meaning there's no way things will be the same again."
  )
  print(
        "You've got the traitor ending. Would you like to play again to get a new ending?"
  )
  play_again()
def delusion_ending():
  print(
        "You wake up in bed, a person hovering over you while writing stuff down. At your side, your family is there, wanting to make sure that you're alright. Your head's pounding like crazy, so maybe that has something to do with it. Man, you've really gotta start reading labels before just eating stuff."
  )
  print(
        "You've got the delusion ending. Would you like to play again to get a new ending?"
  )
  play_again()
def start_game():
  name = input("Enter your name:")
  print("Welcome, " + name + " to Patient 104!\nYou are in a dark room, lying in bed. There is a door to your left and a window to your right, what do you choose?")
  print("1. Go to the door on the left")
  print("2. Look out the window on the right")
  print("3. Remain in bed")
  choice = input("Enter '1', '2',or '3':")
  if choice == '1':
     print("You walk over to the door. It doesn't seem to be locked, as far as you can tell. Do you want to open it?")
     print("1. Try opening the door")
     print("2. Go back to bed")
     print("3. Look around the room")
     print("4. Go to the window")
     choice = input("Enter '1', '2', '3', or '4':")
     if choice == '1':
          print("You open the door, entering out into the hallway. You hear some noises, though it's unclear just where it's coming from.")
          print("1. Left hallway. The lights are on, so someone's probably doing something down there")
          print("2. The room across from you. Someone's definitely in there")
          print("3. Right hallway. Maybe someone left something on")
          choice = input("Enter '1', '2', or '3':")
          if choice == '1':
                print("As you turned to make your way down the hallway, a hand completely covered your face, making it incredibly hard to breathe. As you tried struggling against it, it somehow managed to pull you backwards, eventually making you stumble backwards.")
                bad_ending()
          elif choice == '2':
                print("You were surprised to see that the room was empty, save for the equipment that any room would have. A door leading to, what could potentially be a bathroom, was slightly ajar. On the contrary, the window was wide open, a cool breeze hitting your face. What do you do?")
                print("1. Go to the bathroom")
                print("2. Look out the window")
                choice = input("Enter '1' or '2':")
                if choice == '1':
                     print("You walk towards the bathroom, tiptoeing across the tiled flooring of the room. As you entered, the room suddenly went pitch black. You fumbled for the switch, only to be met with electricity coursing throughout your body. You fell to the ground, your body shaking uncontrollably.")
                     delusion_ending()
                elif choice == '2':
                     print("You walk over to the window, looking out into the parking lot. You see a few cars, but nothing too out of the ordinary. In the distance, a line of trees bordered the edge of the parking lot.")
                     print("1. Go over to the bathroom")
                     print("2. Exit through the window")
                     print("3. Go back out of the room")
                     choice = input("Enter '1', '2', or '3':")
                     if choice == '1':
                          print("You walk towards the bathroom, tiptoeing across the tiled flooring of the room. As you entered, the room suddenly went pitch black. You fumbled for the switch, only to be met with electricity coursing throughout your body.")
                          delusion_ending()
                     elif choice == '2':
                          print("You fall out of the window, falling onto the concrete below you. You land pretty hard, unable to move around from the immense pain. A hand grasps at your ankle, beginning to drag you back into the building. As you tried kicking at the person, you quickly realized that the effort wouldn't be enough to escape.")
                          bad_ending()
                     elif choice == '3':
                          print("You've really only got two options: the bright left hallway or the dark right hallway. Which way?")
                          print("1. Left hallway")
                          print("2. Right hallway")
                          choice = input("Enter '1' or '2':")
                          if choice == '1':
                                print("As you turned the corner, your face was suddenly met with an intense force. Through your blurry vision, you could just barely make out a person holding onto something large and mettalic. You'd fight back if you could, but it'd be no use.")
                                bad_ending()
                          elif choice == '2':
                                print("You continue walking, making it to the end of the hallway. In front of you is a pair of glass doors, and a slightly ajar wooden door to the left of it. Which way?")
                                print("1. The exit. Home sweet home!")
                                print("2. The wooden door. Maybe there's something cool in there")
                                choice = input("Enter '1' or '2':")
                                if choice == '1':
                                     print("You walk out, taking a second to breathe in the air. It'd be a lot nicer had the sound of someone yelling, followed by aggressive barking come out of nowhere. As you ran away, you couldn't keep yourself from wondering how'd you even get into this place to begin with.")
                                     good_ending()
                                elif choice == '2':
                                     print("You walk in the room, taking in the immediate sight of a huge book on a table. Carefully flipping through the pages, your eyes were only met with some of the most sickening things known to man: inhumane experiments, overly detailed notes...and terrible penmanship! Good God, if you're gonna be evil, at least try to make it look good!\nA sudden noise comes from the hallway...")
                                     print("1. Leave the book and run")
                                     print("2. Take the book and run")
                                     print("3. Investigate the noise")
                                     choice = input("Enter '1', '2', or '3':")
                                     if choice == '1':
                                          print("You toss the book to the ground and run out, having to push someone away from you. You kept going, even with a sudden aching pain growing throughout your body. Eventually, you fell into the middle of the road, just barely being saved by grace when a car stopped after seeing you fall in front of them.")
                                          good_ending()
                                     elif choice == '2':
                                          print("You slam the book shut and sprint out, just barely dodging someone trying to hit you with something. Your heart pounds in your chest, threatening to burst out of your chest at any moment. You ran until you couldn't anymore, your legs giving out from under you. You fell in the middle of the road, face first into the asphalt. Ow...")
                                          secrets_ending()
                                     elif choice == '3':
                                          print("You walk towards the sound, only to be met with a person holding onto something large and metallic. You'd fight back if you could, but it'd be no use. They were already pinning you down and calling people over.")
                                          bad_ending()
          elif choice == '3':
                print("As you walk down the hallway, you couldn't help but feel scared. It was pretty dark, and the noises seemed to persist. As you're walking, you notice that a door has began to open, followed by the sound of someone sniffling.")
                print("1. Someone needs help, go check it out")
                print("2. Nope, keep it pushing")
                choice = input("Enter '1' or '2':")
                if choice == '1':
                     print("As you make your way towards the sound, you find the room. Entering it, you notice a woman in a chair, sobbing in her hands. As you drew closer, the woman suddenly grabbed onto you, pulling you close enough to keep you from moving anywhere. As you tried fighting back, a doctor came in, already prepared with a strait jacket.")
                     bad_ending()
                elif choice == '2':
                  print("You make your way down the hallway, taking in all the rotting wallpaper and poorly maintained floors, a strange smell constantly permeating through the air.\nA pair of glass doors come into view, and a slightly ajar wooden door to the left of it. Which way?")
                  print("1. Out the glass doors, you can find help out there")
                  print("2. The wooden door, perhaps you can find answers")
                  choice = input("Enter '1' or '2':")
                  if choice == '1':
                        print("You walk through the doors, the cool night air rushing into your face. It was relieving, especially given the stuffy air from inside. As you continued to walk, you took in everything around you with a new sense of appreciation.")
                        good_ending()
                  elif choice == '2':
                        print("You walk inside, picking up the book on the table. It's pretty big, so you take a second look in it. Before you could really process the things you saw, a noise came from the hallway, forcing you to run out of the building in a hurry. Once you were safe in the nearby forest, you opened the book again, reading everything in more detail...")
                        secrets_ending()
     elif choice == '2':
         print("You decide to lay back down, feeling a bit nauseous as you did. Laying there was pretty uncomfortable, but was better than nothing. Noticing that the door was slowly beginning to open, you suddenly close your eyes shut, though soon fall into a deep sleep.")
         delusion_ending() [done]
     elif choice == '3':
          print("You look around, noticing two main things: a heart monitor and papers clipped to your bed. You can faintly hear something coming closer to the door, so maybe you should make some quick choices.")
          print("1. Hide in the closet")
          print("2. Quickly read the papers")
          print("3. Go check out the noises")
          choice = input("Enter '1', '2', or '3':")
          if choice == '1': 
                print("You slip into the closet, the door closing behind you. You hear things getting pushed around, as well as some angered comments. Eventually, the room grows quiet. It only makes sense to...")
                print("1. Get out and head out into the hallway")
                print("2. Head over to the window")
                print("3. Go back to looking around")
                print("4. Lay down in bed")
                choice = input("Enter '1', '2', '3', or '4':")
                if choice == '1':
                     print("Before you could even exit the room, you were suddenly pulled out of the room, the back of your head being hit hard by something while the front violently met the floor. You were in an unreasonable amount of pain, yet you couldn't do nor say a thing about it.")
                     bad_ending()
                elif choice == '2':
                     print("Going out into the hallway would be stupid, so you head back over to the window. There's only one way out of here, and it's this window. You could potentially escape, but you could also potentially get caught if you're not careful. A little risk and reward, if you will. What do you do?")
                     print("1. Climb out the window and go left")
                     print("2. Climb out the window and go right")
                     print("3. Stay in the room, it's safer")
                     choice = input("Enter '1', '2', or '3':")
                     if choice == '1':
                          print("You climbed out, trying your hardest to cling to the wall. However, with the insufficent amount of foot space, you end up slipping and falling, landing on the concrete below you. The fall was pretty bad, enough to nearly knock you unconcious. It didn't help that a doctor was exiting their car, almost like you were a free pay raise for them.")
                          bad_ending()
                     elif choice == '2':
                          print("You climbed out, carefully placing your feet on whatever brick you could reach first. Before long, you were running away from the place, reaching a river. Above it was a bridge, a place that you could easily hide under or cross if you truly wanted to. But that's for tomorrow you to worry about. For now, you're just glad to be out of there.")
                          good_ending()
                     elif choice == '3':
                          print("You stay inside of the room, taking in the fresh air. That is, until a cloth was suddenly placed over your face, making it incredibly hard to breathe. As you tried struggling against it, it somehow managed to pull you backwards, eventually making you stumble backwards. It wasn't long before you were being dragged out of the room, in pain, and all while practically choking to death by some random cloth!")
                          bad_ending()
                elif choice == '3':
                     print("All your poking and proding created enough noise to get you caught, as a couple nearby doctors realized that you were in fact still in the room. Returning to the room with haste, they dragged you out of the room, fastening you into a strait jacket as they led you off somewhere")
                     bad_ending()
                elif choice == '4':
                     print("Crawling into the bed, you curled up into a ball, feeling safer than ever, as ironic as that is. Closing your eyes, it felt like it was the best sleep you'd probably ever have in your entire life.")
                     delusion_ending()
          elif choice == '2':
                print("You flipped through the pages, seeing that they were all about you. A sharp pain suddenly filled your body, completely paralyzing you. As you held tightly onto the papers, you curled up into a ball, your body shaking uncontrollably as everything blurred into darkness.")
                delusion_ending() 
          elif choice == '3':
                print("You walk out towards the door, only to have it suddenl open. The force sends you into the wall, the pain from the impact sending you to the ground. As you tried getting up, a man firmly grabs hold of your arms, dragging you out of the room with more force than what was probably necessary for someone like yourself.")
                bad_ending() 
     elif choice == '4':
        print("It's dark out and it's hard to see much of anything outside, but you could make out a few cars out in the parking lot...and a loose brick in the wall. Maybe you could climb out and use it?")
        print("1. No way, that's just stupid!")
        print("2. What's the worst that could happen?")
        choice = input("Enter '1' or '2':")
        if choice  == '1':
             print("Well, you've gotta do something! Maybe you could go out into the hallway, or maybe look around the room some more. Going to bed is always an option as well.")
             print("1. Out of the room")
             print("2. Explore some more")
             print("3. Go back to bed")
             choice = input("Enter '1', '2', or '3':")
             if choice == '1':
                  print("You exit the room, now being met with even more options...great. You've got the left hallway, the right hallway, and the room across from you. Which way?")
                  print("1. Left hallway, the lights must be something good")
                  print("2. Right hallway, maybe you can escape")
                  print("3. The room across from you, maybe someone's in there")
                  choice = input("Enter '1', '2', or '3':")
                  if choice == '1':
                        print("Going down the hallway, you hear a couple screams coming from a room next to you. The sudden sounds distract you, leading to you getting caught by two doctors down the hallway. They managed to make quick work of you, already getting you ready to be taken away.")
                        bad_ending()
                  elif choice == '2':
                        print("As you made your way down the hallway, you were finally met with the glorious sign of the exit doors. At the same time, you were met with the sight of a room next to the doors.")
                        print("1. Go through the doors, don't be stupid!")
                        print("2. Check out the room, something's just gotta be in there")
                        choice = input("Enter '1' or '2':")
                        if choice == '1':
                             print("You exit the building, your heart pounding in your chest. You ran until you couldn't anymore, your legs giving out from under you as you entered the forest area bordering the edge of the hospital's parking lot. You were out of the hospital, free from whatever was going on in there.")
                             good_ending()
                        elif choice == '2':
                            print("You walk into the room and notice a book on a table. It's relatively large compared to most you've seen in your life, so something's gotta be in it, right?")
                            print("1. Nope, no way, heading back out now.")
                            print("2. Open the book and read it, there's just gotta be answers")
                            choice = input("Enter '1' or '2':")
                            if choice == '1':
                                 print("Walking away is better. Can't be guilty for something you didn't know about, can you?")
                                 good_ending()
                            elif choice == '2':
                                 print("You open the book and are immediately disgusted by what you see inside of it. Gruesome didn't even begin to describe it. You can't help but feel sick to your stomach, but you didn't know what to do with it.\nFlipping through the pages, you're eyes catch sight of someone entering, a doctor more specifically.")
                                 print("1. Run past her with the book")
                                 print("2. Use the book as a weapon")
                                 print("3. Explain that you were just looking at patient notes")
                                 choice = input("Enter '1', '2', or '3':")
                                 if choice == '1':
                                      print("You run past her, the book held tightly in your hand. You didn't know where you were going, but you knew you were out of there. You ran until you couldn't anymore, your heart pounding in your chest.")
                                      secrets_ending()
                                 elif choice == '2':
                                      print("You struck her upside the head several times with the book, the sharp edges leaving major bruising and stains. As you ran out, the book fell out of your hands, landing on the floor, though that was the least of your worries. For now, you needed to worry about getting back home.")
                                      good_ending()
                                 elif choice == '3':
                                      print("The woman seem to buy it just enough to let you go, though not without her scolding you about wasting company time. She grabs your arm, pulling you towards a room full of all sorts of equipment and uniforms. You threw one on, only to be led to a chair and told to take notes on their latest experiment.")
                                      traitor_ending()
                  elif choice == '3':
                        print("As you open the door to enter the room, a person lunges out at you, their hands grabbing onto your wrists. You tried fighting back, but it was no use. You were pulled back into the room just long enough for a couple other people to come in a strap you down to a stretcher.")
                        bad_ending()
             elif choice == '2':
                  print("As you're taking small peeks at stuff, you eventually enter the bathroom. Taking in the scenery, you hadn't noticed someone walking in until it was too late. They grabbed onto you, pulling you close enough to keep you from going anywhere that they wouldn't want you to. Fighting back is useless, the woman being far stronger than you.")
                  bad_ending()
             elif choice == '3':
                  print("As you lay down, you couldn't help but feel a bit queasy. You closed your eyes, trying to sleep, though it was quite the struggle to do so. As your last traces of consciousness faded away, you fell into a deep sleep.")
                  delusion_ending()
        elif choice == '2':
             print("You make your way out of the window, taking care to climb out. The second your foot touched the grass beneath you, you were out of there, the air hitting against your skin in harsh lashes. Running until you couldn't, you made sure not to be seen anywhere near that place!")
             good_ending() 
  elif choice == '2':
        print("You move over to the window and notice that it's a relatively full parking lot down below. 'Am I in a hospital?' You think to yourself. While looking out the window, you hear noises from the hallway.")
        print("1. Go over to the door")
        print("2. Go to bed and pretend to sleep")
        print("3. Try to hide")
        choice = input("Enter '1', '2', or '3':")
        if choice == '1':
             print("You walked over to the door, ready to open it, when someone suddenly bursts in. The sudden impact knocks you to the ground, and you can't help but feel a lot of pain as they grab ahold of you. As you tried to fight back, your efforts only proved to be useless as the person easily dragged you out of the room.")
             bad_ending()
        elif choice == '2':
             print("Lying down in the bed and closing your eyes, you pretend to sleep. As you lay there, you couldn't help but feel a bit queasy. You closed your eyes, trying to sleep, though it was quite the struggle to do so. As your last traces of consciousness faded, it was comforting in a way.")
             delusion_ending()
        elif choice == '3':
             print("There's really only three places to hide: the closet, under the bed, and behind the curtain. Which way?")
             print("1. The closet, seems smart")
             print("2. Under the bed, though it'll be a tight squeeze")
             print("3. Behind the curtain, though it's pretty risky")
             print("4. Stand brave, you're not scared of anything!")
             choice = input("Enter '1', '2', '3', or '4':")
             if choice == '1':
                     print("There's little space, but you can just barely fit in. You hear things getting pushed around, as well as some angered comments. Eventually, the room grows quiet. What now?")
                     print("1. Stay in place")
                     print("2. Get out and look around")
                     choice = input("Enter '1' or '2':")
                     --if choice == '1':
                        print("You look around the space and notice a letter on the ground. It's a letter from someone's family, asking about their father and why they hadn't heard anything from him in a while. You can't help but feel sorry for them. With the letter, you can either...")
                        print("1. Keep it to read later and exit the closet")
                        print("2. Leave it there and exit the closet")
                        print("3. Keep it and exit the closet to try finding the person")
                        choice = input("Enter '1', '2', or '3':")
                        if choice == '1':
                          print("You exit the closet, letter held tightly in your hand. As you're stepping out into the hallway, you suddenly hear a noise coming from the right hallway. What do you do?")
                          print("1. Go check it out, maybe someone needs help!")
                          print("2. No way, going the other way!")
                          choice = input("Enter '1' or '2':")
                          if choice == '1':
                            print("You walked towards the sound, keeping your ears open for any it. As you turned the corner, you were suddenly met with a person holding onto something large and metallic. You'd fight back if you could, but it'd be no use. They were already pinning you down and calling some others for backup.")
                            bad_ending()
                          elif choice == '2':
                            print("You walked into the much darker hallway, carefully avoiding any sharp objects. Eventually, you reached the end of the hallway, the exit doors in sight. To your left, you saw a door slowly open, just barely enough room for you to slip inside. What do you do?")
                            print("1. Go to the door, maybe you can find something to help you")
                            print("2. Go out the doors, at least you know that there's going to be help out there")
                            choice = input("Enter '1' or '2':")
                            if choice == '1':
                               print("You walked over to the room, entering. On a table, there's a relatively large book. As you walked closer, you noticed that it was open to a page that looked poorly written. Regardless, you could still make out that it was some pretty gruesome stuff. You suddenly hear a noise in the hallway, forcing you to make a decision quickly.")
                               print("1. Take the book and run")
                               print("2. Leave it, you don't have time for it")
                               choice = input("Enter '1' or '2':")
                               if choice == '1':
                                    print("You hold onto the book tightly, running out of the building. You ran until you couldn't anymore, your heart pounding in your chest. You didn't fully know where you were just yet, but as long as you're not in there, it didn't really matter. Something's gotta be done about this place, even if it's the last thing you do.")
                                    secrets_ending()
                               elif choice == '2':
                                    print("You toss the book aside, making a break for the exit. You ran until you couldn't anymore, your heart pounding in your chest. You didn't fully know where you were just yet, but as long as you're not in there, it didn't really matter.")
                                    good_ending()
                            elif choice == '2':
                                 print("You exit the building, your heart pounding in your chest. You ran until you couldn't anymore, your legs giving out from under you as you entered the forest area bordering the edge of the hospital's parking lot. You were out of the hospital, meaning it'd take a whole lot more work on their end to find you again.")
                                 good_ending()
                        elif choice == '2':
                             print("You left it. It's not yours, so why bother it anymore? Exiting the closet, you hear some sounds coming from outside, more specifically from the right side. What do you do?")
                             print("1. Check it out, maybe someone can explain what's going on")
                             print("2. Uh uh, stay inside the room, it's none of your business")
                             print("3. What about somewhere else?")
                             choice = input("Enter '1', '2', or '3':")
                             if choice == '1':
                                  print("As you're walking towards the sound, you feel your arm suddenly snag on something. At first, you thought it was nothing, perhaps a door handle, so you pulled pretty hard to loosen yourself. The sharp sting forced you to look back, revealing that it'd had snag on a broken hook from an IV rack, and a sharp hook at that.")
                                  print("1. Crap! Maybe someone around here can help")
                                  print("2. Just keep walking, it'll figure itself out")
                                  print("What about the room next to you? Maybe it'll have something for it")
                                  choice = input("Enter '1', '2', or '3':")
                                  if choice == '1':
                                       print("You tried looking around, moving about aimlessly until you had bumped into a person. Looking up, it was a large burly man, one that didn't seem all to pleased with you bumping into him. He grabbed you by the neck, taking you out of the dark hallway.")
                                       bad_ending()
                                  elif choice == '2':
                                       print("You walked slowly down the hallway, blood slightly trailing behind you. The sense of dread from earlier persisted, though a newfound desperation emerged as well. Your head was beginning to hurt, but the end of the hallway was in sight. What do you do?")
                                       print("1. Keep moving, you can't stop now")
                                       print("2. Stop, there's no way you can keep going")
                                       choice = input("Enter '1' or '2':")
                                       if choice == '1':
                                            print("You keep pushing yourself, the headache causing your whole body to ache in utter pain. You'd finally reached the end of the hallway, the door in sight. To your left, you saw a door slowly open, just barely enough room for you to slip inside. On one hand, you could leave and find help, but on the other, you could stay and potentially find out what's going on. What do you do?")
                                            print("1. Go to the door, maybe you can find something to help you")
                                            print("2. Go out the doors, at least you know that there's going to be help out there")
                                            choice = input("Enter '1' or '2':")
                                            if choice == '1':
                                                 print("You slip into the room, your head still throbbing. You notice on the table that there is a book, and it appeared as though someone had been reading it before suddenly dumping it there. You can either...")
                                                 print("1. Open the book and read it, something's gotta be in there")
                                                 print("2. Leave it, it's not yours to read")
                                                 choice = input("Enter '1' or '2':")
                                                 if choice == '1':
                                                      print("You opened it and almost immediately felt sick to your stomach. Inside the book, you find all sorts of horrific notes, stripping people of their humanity, treating them like mere objects to test on and throw away. The signatures were amateur cursive, but you knew that it was definitely real.\nHearing a noise in the hallway, you tuck the book under your arm and make a break for it. You ran until you couldn't anymore, your heart pounding in your chest...")
                                                      secrets_ending()
                                                 elif choice == '2':
                                                      print("You decide to leave the book alone, not wanting to waste any time on it. As you left the building, you managed to notice one of the cars was on, the soft humming filling the air. Against your good concious, you walked over and, sure enough, the keys were still inside. Taking the car and going on your way, you couldn't help but feel like you probably should've taken that book anyways.")
                                                      good_ending()
                                            elif choice == '2':
                                                 print("Exiting the building, you walked until you couldn't anymore. You'd made it surprisingly far, managing to get to an old gas station. The owner had let you in, though only for tonight, his words exactly.")
                                                 good_ending()
                                       elif choice == '2':
                                            print("The pain in your head is growing, feeling as if your body was being split apart from the head down. Finally, the heavy feeling in your chest leaves as you vomit, only to collapse right after. A doctor just so happens to find you lying there in your own mess, grabbing you by the leg to drag you away.")
                                            bad_ending()
                                  elif choice == '3':
                                       print("Walking into the room, it wasn't hard to see that it was a generic waiting room. What was harder to understand, however, was seeing a child standing in front of you: Jeremy. He looked at you, that same toothy smile that you'd come to know. But you knew it wasn't real, he'd been gone for a while now. Closing your eyes, you tried to make the hallucination go away...")
                                       delusion_ending()
                             elif choice == '2':
                                  print("Okay, keep it cool. It's probably nothing. On the bed, there seems to be some clipboard. At the same time, the window is just slightly open. What sounds better?")
                                  print("1. The clipboard, surely something important is on it")
                                  print("2. The window, maybe you can escape")
                                  choice = input("Enter '1' or '2':")
                                  if choice == '1':
                                       print("Reading the papers, you see that they're all about you. A sharp pain suddenly filled your body, completely paralyzing you. As you held tightly onto the papers, you curled up into a ball, your body shaking uncontrollably as everything")
                                       delusion_ending()
                                  elif choice == '2':
                                       print("On the way out, you made sure to take extra care to avoid slipping. The second you touched the groun, you were gone, running until your legs gave out from under you. Falling into the river, you could just barely keep yourself afloat.")
                                       good_ending()
                             elif choice == '3':
                                  print("Okay, so you've got two options: the room across from yours and the left hallway. Which way?")
                                  print("1. The room across from you, maybe someone's in there")
                                  print("2. The left hallway, the lights on must mean something good, right?")
                                  choice = input("Enter '1' or '2':")
                                  if choice == '1':
                                       print("You walk into the room, taking in the sight of a person in a chair. From the door, it was unclear who it was, though, as you walked closer, the sight was shocking: it was your mom! She looked up at you with those familiar eyes, holding out a hand to you. Hesitant, you take her hand, feeling a sudden rush of shock move throughout you. The shock managed to have your heart racing to the point of giving out, causing you to collapse to the ground.")
                                       delusion_ending()
                                  elif choice == '2':
                                       print("Just as you turned the corner, you were suddenly met with a person holding onto something large and metallic. You'd fight back if you could, but it'd be no use. They were already pinning you down and calling people over.")
                                       bad_ending()
                        elif choice == '3':
                             print("As you're walking towards the sound, you feel something grab onto your arm. Turning around, you see a man in a lab coat, his eyes locked onto you. As you tried pulling back, he suddenly landed a punch square in the face, knocking you out cold.")
                             bad_ending()
                     elif choice == '2':
                        print("You exit the closet and take a look around the room. You notice that they'd left behind a clipboard with some papers on it. At the same time, the door's been left open, but you also have a chance to look out the window for a moment. What would you like to do?")
                        print("1. Look out the window")
                        print("2. Look at the clipboard")
                        print("3. Go out the door")
                        choice = input("Enter '1', '2', or '3':")
                        if choice == '1':
                          print(
                                "You look out the window and notice a stretcher had been left outside in the parking lot. It seems that something is covered up, but you can't quite make it out. Do you want to..."
                          )
                          print("1. Try to find your way down to it")
                          print("2. Leave it be, it's none of your business")
                          choice = input("Enter '1' or '2':")
                          if choice == '1':
                             print(
                                  "You head out of the room and have two options: the left hallway or the right hallway. Which way?"
                             )
                             print("1. Down the left hallway, the lights will make it easier to see, so you might get there faster")
                             print("2. Down the right hallway, no one will see you, but it'll be hard to move around")
                             print("3. The room across from you might have something useful")
                             choice = input("Enter '1', '2', or '3':")
                             if choice == '1':
                                print("Walking down the hallway, you couldn't help but be bothered by the occasional sounds of agonizing screams and extreme discomfort coming from the closed off rooms. At the end of the hallway, you see a woman talking to a man in a lab coat. What do you do?")
                             print("1. Go back. Maybe you're better off going down the darker hallway")
                             print("2. Walk up and ask them some questions")
                             print("3. Slip into the slightly open door to the side of you")
                             choice = input("Enter '1', '2', or '3':")
                          elif choice == '2':
                             print(
                                  "You're probably better off ignoring it. Walking away from the window, you realize that it'll probably be a while before anyone shows up again. The clipboard is still sitting there, but the door is open, a chance of escaping. What do you do?"
                             )
                             print("1. Look at the clipboard")
                             print("2. Go out the door")
                             print("3. What about the window?")
                             choice = input("Enter '1', '2', or '3':")
                             if choice == '1':
                                print(
                                     "You walk over to the clipboard and notice that there are a few papers on it. You can either..."
                                )
                             elif choice == '2':
                                print(
                                     "You exit the door, and notice two hallways: one has lights and the other is dark. At the same time, there's a room across from you, likely occupied by another person in the same situation. Which way will you go?"
                                )
                             elif choice == '3':
                                print(
                                     "You walk back over to the window and realize that it's unlocked. Pulling up a few times, a sudden rush of air hits your face. Now's the time to choose..."
                                )
                                print(
                                     "1. Climb out the window, but it's a long way down if you slip"
                                )
                                print(
                                     "2. Stay inside, only crazy people try climbing out windows at night"
                                )
                                choice = input("Enter '1' or '2':")
                                if choice == '1':
                                  print(
                                        "You climb out the window, but end up slipping and falling. At the very least the stretcher acts like a cushion, but you're still hurt. You're able to get up and walk away, though. You've made it out of the hospital, but you're not sure where you are. You're just glad to be out of there."
                                  )
                                  good_ending()
                                elif choice == '2':
                                  print(
                                        "Trying to stay safe is probably the best way to go right now. There's a good bit you could do right now. There's always that stupid clipboard, the door, and just laying back down."
                                  )
                                  print("1. Look at the clipboard, maybe kill some time")
                                  print("2. Go out the door, maybe you could find help")
                                  print("3. Lay down, this is becoming too stressful!")
                                  choice = input("Enter '1', '2', or '3':")
                                  if choice == '1':
                                     print(
                                          "You walk over to the clipboard and notice that there are a few papers on it. You can either..."
                                     )
                                     print(
                                          "1. Look at the papers, something has to be on there"
                                     )
                                     print("2. They're probably fakes, just leave them be")
                                     choice = input("Enter '1' or '2':")
                                     if choice == '1':
                                        print(
                                             "You pick up the papers and begin to read them. They're all about one thing: you. It was insane! Surely this wasn't true, but you couldn't help but feel a little sick to your stomach. You can either..."
                                        )
                                        print("1. Keep reading, maybe it'll help you")
                                        print("2. Throw them away, it's too much!")
                                        print(
                                             "3. Shove them into your pocket, you might need them later"
                                        )
                                        choice = input("Enter '1', '2', or '3':")
                                        if choice == '1':
                                          print(
                                                "You continue to read until you suddenly feel lightheaded. You stumble for a moment, trying to catch onto something, suddenly, you fell over and everything goes black."
                                          )
                                          delusion_ending()
                                        elif choice == '2':
                                          print(
                                                "You ball the papers up and toss them into the trash can, quickly exiting the room right after, feeling a bit queasy after reading the documents. Upon exiting the room, you notice three things: a well-lit hallway to your left, a dark one to your right, and a room straight ahead. Which do you choose?"
                                          )
                                          print(
                                                "1. To the left, maybe you'll find something, and it'll be easy with all those lights"
                                          )
                                          print(
                                                "2. To the right, maybe you can escape, but finding an exit will be much harder"
                                          )
                                          print(
                                                "3. Straight ahead, maybe you'll find someone who can help you"
                                          )
                                          choice = input("Enter '1', '2', or '3':")
                                  elif choice == '2':
                                     print(
                                          "You exit the room and notice that there are two different hallways; the left has working lights while the right is nearly pitch black. You also notice that there's a room across from you, likely occupied by another person in the same situation. Which way will you go?"
                                     )
                                     print(
                                          "1. Down the left hallway, though the lights might give you away, so be cautious"
                                     )
                                     print(
                                          "2. Go down the right hallway, though it'll be hard to see, you might be able to escape"
                                     )
                                     print(
                                          "3. The room ahead, something or someone useful just has to be in there"
                                     )
                                     choice = input("Enter '1', '2', or '3':")
                                     if choice == '1':
                                        print(
                                             "Walking down the hallway, an orchestra of screams and moans fill your ears. You can't help but feel a bit sorry for them. At the end of the hallway, you see a woman talking to a man in a lab coat, seemingly frustrated about something. What do you do?"
                                        )
                                        print(
                                             "1. Try talking to them, maybe they know what's going on"
                                        )
                                        print("2. Turn around, and be quick with it!")
                                        print(
                                             "3. Slip into the room next to you. Maybe you can listen in from there"
                                        )
                                        choice = input("Enter '1', '2', or '3':")
                                     elif choice == '2':
                                        print(
                                             "Walking down the hallway, you felt a constant sense of dread, almost like you're being watched. In your moment of distraction, the worst happened: your foot was cut pretty badly by stray glass on the ground, a pool of blood already forming."
                                        )
                                        print(
                                             "1. Shoot! Maybe try finding someone to help you")
                                        print(
                                             "2. Keep moving, you can try finding someone once you're out of here"
                                        )
                                        print(
                                             "3. Stop and clean the wound, you can't keep moving with this much blood, it'll make a trail"
                                        )
                                        choice = input("Enter '1', '2', or '3':")
                                        if choice == '1':
                                          print(
                                                "You tried looking around, moving about aimlessly until you had bumped into a person. Looking up, it was a large burly man, one that didn't seem all to pleased with you bumping into him. He took in the sight of you, then your wound, then locked eyes again. What do you do?"
                                          )
                                          print(
                                                "1. Try to explain yourself, maybe he'll understand"
                                          )
                                          print(
                                                "2. Quick, run away! His size will probably weigh him down"
                                          )
                                          print(
                                                "3. Try pushing past him, maybe you can find help elsewhere"
                                          )
                                          choice = input("Enter '1', '2', or '3':")
                                        elif choice == '2':
                                          print(
                                                "You limped down the hallway, blood slightly trailing behind you. The sense of dread from earlier persisted, though a newfound desperation emerged as well. Your head was beginning to hurt, but the end of the hallway was in sight. What do you do?"
                                          )
                                          print("1. Keep moving, you can't stop now")
                                          print("2. Stop, there's no way you can keep going")
                                          choice = input("Enter '1' or '2':")
                                          if choice == '1':
                                               print("You keep pushing yourself, the headache causing your whole body to ache in utter pain. You'd finally reached the end of the hallway, the door in sight. To your left, you saw a door slowly open, just barely enough room for you to slip inside. On one hand, you could leave and find help, but on the other, you could stay and potentially find out what's going on. What do you do?")
                                          print("1. Go to the door, maybe you can find something to help you")
                                          print("2. Go out the doors, at least you know that there's going to be help out there")
                                          choice = input("Enter '1' or '2':")
                                          if choice == '1':
                                             print(
                                                  "You slip into the room, your head still throbbing. You notice on the table that there is a book, and it appeared as though someone had been reading it before suddenly dumping it there. You can either..."
                                             )
                                             print(
                                                  "1. Open the book and read it, something's gotta be in there"
                                             )
                                             print("2. Leave it, it's not yours to read")
                                             choice = input("Enter '1' or '2':")
                                             if choice == '1':
                                                print(
                                                     "Inside the book, you find all sorts of horrific notes, stripping people of their humanity, treating them like mere objects to test on and throw away. The signatures were amateur cursive, but you knew that it was real. It didn't help that it looked like one of the pages had your name, meaning you'd probably just gotten here. What now?"
                                                )
                                                print("1. Put it down, it's not yours!")
                                                print(
                                                     "2. Take the book and run, you have to reveal the truth!"
                                                )
                                                choice = input("Enter '1' or '2':")
                                                if choice == '1':
                                                  print(
                                                        "You leave the book alone before leaving the room, rushing out the glass doors before anyone could spot you. You ran until your legs gave out from under you. Despite being in the middle of a forest, you felt secure. Perhaps it was the fact that you were out of the hospital, or perhaps it was the amazing sight above you."
                                                  )
                                                  good_ending()
                                                elif choice == '2':
                                                  print(
                                                        "You snatch it up and rush out, not even bothering to look back. It wasn't until you had ran out to the edge of an interstate did you finally stop in your tracks. A truck slowed down, allowing you to hop inside so long as they could drop you off somewhere. During the entire ride, you remained silent, your mind racing with the thoughts of what you'd just seen."
                                                  )
                                                  secrets_ending()
                                             elif choice == '2':
                                                print(
                                                     "You decide to leave the book alone, not wanting to waste any time on it. Just as you had reached the door, a sudden surge of pain struck you, causing you to fall to the ground. You couldn't help but feel like you were being attacked from the inside out. Turning around, you see a woman towering over you, a metal object in hand being the last thing you see before blacking out."
                                                )
                                                bad_ending()
                                          elif choice == '2':
                                             print(
                                                  "You limp your way towards the door, finally getting out of there. You notice a stretcher, and walk over to it. However, just as you were about to lift up the cloth, you hear a sudden noise, making you jump and flee the area."
                                             )
                                             good_ending()
                                          elif choice == '2':
                                             print("You made an abrupt stop, nearly falling over. You held onto your head, trying to keep it together. Somehow, the pain hurt more just by standing there. There's no way you can keep going, not unless you're really crazy enough to do so.")
                                             print("1. Crazy's your middle name, now move")
                                             print("2. You're not crazy, you just need to rest")
                                             choice = input("Enter '1' or '2':")
                                             if choice == '1':
                                                print("Finally, you reach the end of the hallway. You hear a small sniffling sound coming from your left, but there's also a glass double door to your right. You can almost taste freedom...")
                                                print("1. Someone needs help, go to the left")
                                                print("2. It's none of your business, go to the right")
                                                choice = input("Enter '1' or '2':")
                                                if choice == '1':
                                                  print("Upon entering a room, you notice a wooden table. Walking closer, you see...a tape recorder?! Whipping around, a man is already behind you, his baton striking you in the head. He was followed by a woman with a strait jacket, her hands moving quickly to lock you inside it.")
                                                  bad_ending()
                                                elif choice == '2':
                                                  print("You walk towards the doors, your hand shakily reaching out towards it. Out the corner of your eye, you see a slightly ajar wooden door, but freedom is right in sight. Well, that, and a stretcher with something on it outside. But there's a door, maybe something cool's in there!")
                                                  print("1. What are you, ten? Go out the door!")
                                                  print("2. Go check it out, who can resist cool stuff behind mysterious doors?")
                                                  choice = input("Enter '1' or '2':")
                                                  if choice == '1':
                                                     print("You exit the building, your head still throbbing. The second you can find a bus, you're heading to the hospital, that much is clear. You walked over to the stretcher, carefully picking up the cloth, only to find a body underneath. While expected, it was still frightening, causing you to book it out of there.")
                                                     good_ending()
                                                  elif choice == '2':
                                                     print("You walk over to the door, careful not to make too much noise. Upon entering, you notice a large book on a table. You can either...")
                                                     print("1. Open the book and read it, something's gotta be in there")
                                                     print("2. Leave it be, you're not crazy enough to read random books")
                                                     choice = input("Enter '1' or '2':")
                                                     if choice == '1':
                                                        print("You open the book and begin to read. It was filled to the brim with sick and twisted ideas, treating people as though they're mere objects to test on and throw away! And the signatures, talk about amateur cursive!")
                                                        print("1. Put it down, it's not yours!")
                                                        print("2. Take the book and run, you have to reveal the truth!")
                                                        print("3. Wait, read on...something's sticking out a couple pages in!")
                                                        choice = input("Enter '1', '2', or '3':")
                                                        if choice == '1':
                                                          print("You put down the book. After all, stealing's not right, regardless of the situation. You sneak over to the double doors, exiting before anyone really noticed. You rushed out, though you couldn't help but feel a bit guilty.\nYou know what's happening here, yet you've left the evidence. Yeah, it's not your job to expose them, but you can't help but feel like you should've done something.")
                                                          good_ending()
                                                        elif choice == '2':
                                                          print("You took the book and rushed out, your heart pounding in your chest. You can't help but feel like you're doing the right thing, but you can't help but feel guilty as well. You know what's happening here, and you have proof, but what if everyone else is just like them? What if they just call you crazy? As you continue running away from the place, the feeling continues to grow, unwilling to budge.")
                                                          secrets_ending()
                                                        elif choice == '3':
                                                          print("Quickly flipping through the pages, you reach the note. It was another letter, a mother asking what had happened to her son. It's sickening, considering you'd just seen a page about him, a gruesome thing.\nWhile reading, you hear footsteps, followed by the sound of a door opening. Turning around, you see a man in a lab coat, his eyes locked onto you. What do you do?")
                                                          print("1. Push him over, then try to run")
                                                          print("2. Try to explain yourself, maybe he'll understand")
                                                          print("3. Throw the book at him, maybe it'll distract him")
                                                          print("4. Shove the book into your pocket and dip!")
                                                          choice = input("Enter '1', '2', '3' or '4':")
                                                          if choice == '1':
                                                             print("Not sure why you'd even try that in the first place, as he managed to block your attack before you could even fully place your hands on him. Tackling you to the ground, there wasn't enough time to react as he'd suddenly tased you, leaving you unconscious.")
                                                             bad_ending()
                                                          elif choice == '2':
                                                             print("You tried explaining, but you kept fumbling over your words, only making things worse. He grabbed you, his grip tightening around your neck. You tried to scream, but you couldn't make a sound. You continued to struggle, but it was no use. You were taken away, never to be seen again")
                                                             bad_ending()
                                                          elif choice == '3':
                                                             print("The pain from the sudden impact distracts him just long enough for you to slip past and get out of there! You ran until you couldn't run anymore, your heart pounding in your chest. You didn't fully know where you were just yet, but as long as you're not in there, it didn't really matter.")
                                                             good_ending()
                                                          elif choice == '4':
                                                             print("You shove the book into your pocket and make a break for it. Thankfully, the man was just disoriented enough by all your movement that you could slip past and burst through the doors. You didn't know where you were, but you knew you were out of there. As far as you're concerned, something's going to be done about this place, even if it's the last thing you do."\)
                                                             secrets_ending()
                                                     elif choice == '2':
                                                        print("You put the book down, deciding it's not worth you time, and head out the room. However, just as you exited, three people were waiting outside, all of them ready to pin you down in a second. What do you do?")
                                                        print("1. Fight back, you're not going down without a fight")
                                                        print("2. Lie and say it's your first day and that you need a uniform")
                                                        print("3. Hurry, sprint past them! They can't all lunge at once!")
                                                        choice = input("Enter '1', '2', or '3':")
                                                        if choice == '1':
                                                          print("You tried to fight back, but you were no match for them. They were all too strong, too many. You were pinned down, and you couldn't move. You tried to scream, but you couldn't make a sound. You continued to struggle, but it was no use. You were taken away, never to be seen again.")
                                                          bad_ending()
                                                        elif choice == '2':
                                                          print("You lied, right through your teeth, and they somehow believed you. Taking you by the arm, they led you to a room, where you were given a uniform, only to be ushered around through each room, made to take notes. The whole time, you couldn't help but think about the things you saw.")
                                                          traitor_ending()
                                                        elif choice == '3':
                                                          print("You sprinted past them, your heart pounding in your chest. You didn't look back, didn't care what happened to you. You just kept running, until you finally made it out of the building. You were out of the hospital, but you were still in danger. You knew, no matter what, you were never going to truly be safe. At the very least, you didn't have to worry about them tonight.")
                                                          good_ending()
                                             elif choice == '2':
                                                print("The pain in your head is growing, feeling as if your body was being split apart from the head down. Finally, the heavy feeling in your chest leaves as you vomit, only to collapse right after. The world around you slowly fades to black...")
                                                delusion_ending()
                                  elif choice == '3':
                                     print("You lay down, a pain in your head beginning to grow rapidly. Still, the soft surface of the pillow is comforting, almost erasing the pain for a moment. Closing your eyes, you slowly drift off to sleep...")
                                     delusion_ending()
                        elif choice == '2':
                          print("As you draw closer to it, the name on it is more apparent...it looks like yours. Do you dare to read further?")
                          print("1. Yes, maybe it'll help me")
                          print("2. No, it must be fake")
                          choice = input("Enter '1' or '2':")
                          if choice == '1':
                              print("Flipping through the pages, you see that they're all about you. A sharp pain suddenly filled your body, completely paralyzing you. As you held tightly onto the papers, you curled up into a ball, your body shaking uncontrollably as everything")
                              delusion_ending()
                          elif choice == '2':
                             print("The papers were probably fakes anyways, so no point in entertaining them. You walk out the door and notice two hallways: one has lights and the other is dark. Which way?")
                             print("1. Down the left hallway, the lights make it easier to see")
                             print("2. Down the right hallway, the darkness could cover you")
                             print("3. The room across from you, someone might be in there")
                             choice = input("Enter '1', '2', or '3':")
                             if choice == '1':
                                 print("Walking through the bright hallway, a bulb had suddenly fell in front of you, causing you to jump back into someone. The woman let out an agitated sound before wrapping her hands around your neck, choking you out as a couple other people came to check out what all the noise was for...")
                                 bad_ending()
                             elif choice == '2':
                                 print("The darkness made it incredibly difficult to see, everything blending in with each other. As you were walking, you slip on something, falling to the ground. A sharp pain radiates through your body as you realize that something on the floor must've punctured")
                                 print("1. Try to get up and keep moving")
                                 print("2. Oh God, this is it, it's the end for me! (dramatic much...)")
                                 choice = input("Enter '1' or '2':")
                                 if choice == '1':
                                     print("You manage to get up, albeit with some difficulty. You keep moving, your head throbbing in pain. Eventually, you reach the end of the hallway, the door in sight. To your left, you see a door slowly open, just barely enough room for you to slip inside. On one hand, you could leave and find help, but on the other, you could stay and potentially find out what's going on. What do you do?")
                                     print("1. Out the exit")
                                     print("2. The room next to you")
                                     choice = input("Enter '1' or '2':")
                                 elif choice == '2':
                                     print("Seriously? You're just gonna lay there? Well, it's not like you've got a choice now, as a doctor walked out of the room next to you andd just noticed you lying there like a little kid in the middle of a tantrum. Rolling his eyes, he grabbed onto your legs and began pulling...")
                                     bad_ending()
                             elif choice == '3':
                                 print("Walking into the room, you saw someone sitting in the bed: your mother. She was dazed for a moment, trying to take in your shadowed figure. Once she could tell it was you, she ran over and wrapped you in a warm embrace. You closed your eyes, the warmth of it allowing you to sink into it...")
                                 delusion_ending()
                        elif choice == '3':
                          print("You exit the door, and notice two hallways: one has lights and the other is dark. At the same time, there's a room across from you, likely occupied by another person in the same situation. Which way will you go?")
                          print("1. Down the left hallway, the lights make it easier to see")
                          print("2. Down the right hallway, the darkness could cover you")
                          print("3. The room across from you, maybe someone's in there after all")
                          choice = input("Enter '1', '2', or '3':")
                          if choice == '1':
                                print("Walking down the left hallway, it was filled to the brim with an ochestra of medical equipment and screaming. It was both sad and somewhat irritating, the sounds messing with your already aching head. At the end of the hallway, you see a woman talking to a man in a lab coat, seemingly frustrated about something. What do you do?")
                                print("1. Try talking to them, maybe they know what's going on")
                                print("2. Turn around and go the other way")
                                print("3. Slip into the room next to you")
                                choice = input("Enter '1', '2', or '3':")
                                if choice == '1':
                                     print("You walk up to them, trying to get their attention. They look up at you, their eyes filled with a sense of frustration. Once they'd registered that you were, in fact, not a doctor, they pulled out their tasers, the both of them striking you down to the ground. Honestly, it was a bit of an overkill reaction.")
                                     bad_ending()
                                elif choice == '2':
                                     print("You made your way down the hallway, careful to avoid everything around you as a putrid smell invaded your nostrils. Eventually, you made your way towards a pair of glass doors, along with a wooden door to the left of them. Which will you choose?")
                                     print("1. The glass doors, let's get out of here")
                                     print("2. The wooden door, maybe there's something cool in there")
                                     choice = input("Enter '1' or '2':")
                                     if choice == '1':
                                         print("You walk out of the building, surprisingly feeling a lot calmer than before. Eventually, you made your way to a bus stop, sitting down on the bench to wait on the bus. While wating, your thoughts finally had time to run buck wild throughout your head, causing you to nearly miss the bus when it did arrive.")
                                         good_ending()
                                     elif choice == '2':
                                         print("You walk into the room, noticing almost immediately that a book was sitting on a table admist the cluttered mess that made up the room. Walking closer, it was open to a page that looked poorly written. Regardless, you could still make out that it was some pretty gruesome stuff.")
                                         print("1. Take the book and run")
                                         print("2. Leave it, it's not yours")
                                         choice = input("Enter '1' or '2':")
                                         if choice == '1':
                                             print("Well, you don't really need to run right now. It seems like nobody was dwn here at the moment, so you had time to walk. Well, that was until a car began pulling into the parking lot, the driver locking eyes with you. Almost immediately, you ran away, ending up under a bridge by the time you tired out.")
                                             secrets_ending()
                                         elif choice == '2':
                                             print("You left the book alone, no longer interested. However, just as you were walking out of the building, someone was walking in. The man constantly kept pushing you while asking a million questions per second, eventually causing you to fall over. Before you could really fight with him, he was already calling people over...")
                                             bad_ending()
                                elif choice == '3':
                                     print("Slipping into the room, your eyes fell onto the figure standing next to you. You couldnt believe it: your father was just standing next to you like everything was normal. He looked at you, noticing your slightly disheveled appearance. As he placed a hand onto your shoulder, you suddenly fell over, the last thing you see being your father's distressed expression.")
                                     delusion_ending()
                          elif choice == '2':
                                print("Walking down the right hallway, you felt a constant sense of dread, almost like you're being watched. In your moment of distraction, the worst happened: your foot was cut pretty badly by stray glass on the ground, a pool of blood already forming")
                                print("1. Find someone to help, there's clearly doctors here")
                                print("2. Just keep walking, it'll heal itself...hopefully")
                                print("3. Stop to clean up")
                                choice = input("Enter '1', '2', or '3':")
                                if choice == '1':
                                     print("As you try looking for someone, you bumped into a wall. Feeling your way around, you felt something soft. Opening your eyes, it was the lab coat of a pretty tall guy, who was now frustrated with you touching him. He snatched you up, deciding to dispose of you somewhere.")
                                     bad_ending()
                                elif choice == '2': 
                                     print("After a long while of dragging your foot along, the pain being much more impactful than you thought it'd be, you finally reached the end of the hallway. You see a door to your left, and a pair of glass doors in front of you. Which way?")
                                     print("1. Glass doors, let's head home")
                                     print("2. Door to the left of you")
                                     choice = input("Enter '1' or '2':")
                                     if choice == '1':
                                          print("You exit the building, your head still throbbing. The second you can find a bus, you're heading to the hospital, that much is clear. You walked over to the stretcher, carefully picking up the cloth, only to find a body underneath. While expected, it was still frightening, causing you to book it out of there.")
                                          good_ending()
                                     elif choice == '2':
                                          print("You walk into the room, noticing almost immediately that a book was sitting on a table admist the cluttered mess that made up the room. Walking closer, it was open to a page that looked poorly written. Regardless, you could still make out that it was some pretty gruesome stuff.")
                                          print("1. Take the book and run")
                                          print("2. Leave it, it's not yours")
                                          choice = input("Enter '1' or '2':")
                                          if choice == '1':
                                                print("You tuck it under your arm and run out, running until your foot finally gave out from under you, causing you to fall into a puddle. It was a pain like no other...and was definitely going to get infected sooner or later...")
                                                secrets_ending()
                                          elif choice == '2':
                                                print("You leave the book alone, deciding that it's not worth your time. Exiting the building, you decided to sneak along the edge of the building until you reached the edge of the parking lot, running off into the forest afterwards.")
                                                good_ending()
                                elif choice == '3':
                                     print("Trying to find something, you end up taking your shirt off, a desperate attempt to stop the bleeding. Dabbing at it was a pain in the rear end, though that was quickly replaced by a violent surge of electricity coursing throughout your body. You fell to the ground, your body shaking uncontrollably as you looked back and saw two women looking down at you. Taking ahold of you, they began to drag you out of the dark hallway.")
                                     bad_ending()
                          elif choice == '3':
                                print("You walk over to the room, taking in the sight of a person in a chair. From the door, it was unclear who it was, though, as you walked closer, the sight was shocking: it was your mom! She looked up at you with those familiar eyes, holding out a hand to you. Hesitant, you take her hand, feeling a sudden rush of shock move throughout you. The shock managed to have your heart racing to the point of giving out, causing you to collapse to the ground.")
                                delusion_ending()
             elif choice == '2':
                  print("It's an unbearbly tight squeeze, pressing down hard on you, but you keep quiet anyways. Things are knocked around and you hear some angry comments. Suddenly, the footsteps grow closer. What do you do?")
                  print("1. Stay in place")
                  print("2. Get out and fight back")
                  print("3. Hop out and run")
                  choice = input("Enter '1', '2', or '3':")
                  if choice == '1':
                          print("You remained under the bed, your breathing beginning to grow heavier from the lack of oxygen. It's incredibly hard to stay still, and the footsteps only seem to be getting closer. Just as they began lifting the bed, you faint.")
                          delusion_ending()
                  elif choice == '2':
                          print("You squeeze out of the bed, ready to fight back. However, because of how long it took you to get out from under there, they easily overpowerd you, laughing like it was some inside joke you weren't apart of. Well, you are, but as the joke.")
                          bad_ending()
                  elif choice == '3':
                          print("Squeezing out from under the bed took a lot out of you, disorienting you slightly. As you tried to make a break for it, one of the doctors held a foot out, tripping you up and sending you crashing into the wall, nearly knocking you unconcious from the impact.")
                          bad_ending()
             elif choice == '3':
                  print("The first place they looked was behind the sheer fabric of the curtain. They bombard you with questions, but don't seem to be the brightest of the bunch. You can either...")
                  print("1. Fight back")
                  print("2. Lie and say you were looking for a patient")
                  print("3. Ask what's happening and why you're here")
                  print("4. Quickly run past them")
                  choice = input("Enter '1', '2', '3', or '4':")
                  if choice == '1':
                       print("Alright," + name + ", wannabe Tommy Tough Knuckles, they might not be the the brightest of the bunch, but they're still pretty strong. They land a good couple of punches on you, knocking you to the floor long enough that they could drag you out with no problem. Real smart, bud.")
                       bad_ending()
                  elif choice == '2':
                          print("Even if didn't want to, you allowed yourself to lie straight through your teeth, creating some long elaborate story about how you were just a new employee, and that you were looking for a patient. They seemed to buy it, leading you to a room where you were given a uniform, making comments about how ridiculous you looked in your current attire.")
                          traitor_ending()
                  elif choice == '3':
                          print("You ask them some questions, but they just look at you like you've gone mad. Eventually, the two grab you by your arms, taking you out of the room.")
                          bad_ending()
                  elif choice == '4':
                          print("You run out and, without thinking, run into the room right across from yours. Inside is what looks to be another person and a slightly ajar window. You could potentially escape out of the window, but you could also investigate the possible person.")
                          print("1. Jump out the window, surely there'll be something to break your fall")
                          print("2. Find out if it's a body or just a terrible sleeper")
                          choice = input("Enter '1' or '2':'")
                          if choice == '1': 
                              print("Why in your right mind did you just jump out of a window? Yeah, your fall was broken, but by a tree. As you tried fighting your way out of the limbs of the tree, a group of hands were suddenly pulling you down, only for you to be dragged off to who knows where.")
                              bad_ending() 
                          elif choice == '2':
                                print("You slowly crept over to the person, careful not to make too much noise in case they truly were sleeping. Lifting the cover away, you're met with the sight of fully opened eyes staring up at you. Just as you were about to scream, their hand grabbed onto your wrist, pulling you close enough to hear them scream at you to wake up, repeating themselves until you'd closed your eyes shut.")
                                delusion_ending()     
             elif choice == '4':
                  print("That was pretty dumb, as the people just looked at you like you were a total idiot. Tasing you to the ground, they dragged you out of the room, never to be seen again.")
                  bad_ending()
             
  elif choice == '3':
     print("You remained in bed and suddenly hear something beeping in your ear. Will you investigate?")
     print("1. Yes")
     print("2. No")
     choice = input("Enter '1' or '2':")
     if choice == '1':
        print("You looked around the room and saw a heart monitor next to you. You must be in a hospital. You hear a noise from the hallway, what do you do?")
        print("1. Check it out")
        print("2. Hide somewhere")
        choice = input("Enter '1' or '2':")
        if choice == '1':
          bad_ending()
        elif choice == '2':
          print("You've got a couple choices, but not a lot of time. Quick, choose!")
          print("1. The closet, seems smart")
          print("2. Under the bed, though it'll be a tight squeeze")
          print("3. Behind the curtain, though it's pretty risky")
          print("4. Stand brave, you're not scared of anything!")
          choice = input("Enter '1', '2', '3', or '4':")
          if choice == '1':
             print("There's little space, but you can just barely fit in. You hear things getting pushed around, as well as some angered comments. Eventually, the room grows quiet. What now?")
             print("1. Stay in place")
             print("2. Get out and look around")
             choice = input("Enter '1' or '2':")
             --if choice == '1':
                print("You look around the space and notice a letter on the ground. It's a letter from someone's family, asking about their father and why they hadn't heard anything from him in a while. You can't help but feel sorry for them. With the letter, you can either...")
                print("1. Keep it to read later and exit the closet")
                print("2. Leave it there and exit the closet")
                print("3. Keep it and exit the closet to try finding the person")
                choice = input("Enter '1', '2', or '3':")
                if choice == '1':
                  print("You exit the closet, letter held tightly in your hand. As you're stepping out into the hallway, you suddenly hear a noise coming from the right hallway. What do you do?")
                  print("1. Go check it out, maybe someone needs help!")
                  print("2. No way, going the other way!")
                  choice = input("Enter '1' or '2':")
                  if choice == '1':
                    print("You walked towards the sound, keeping your ears open for any it. As you turned the corner, you were suddenly met with a person holding onto something large and metallic. You'd fight back if you could, but it'd be no use. They were already pinning you down and calling some others for backup.")
                    bad_ending()
                  elif choice == '2':
                    print("You walked into the much darker hallway, carefully avoiding any sharp objects. Eventually, you reached the end of the hallway, the exit doors in sight. To your left, you saw a door slowly open, just barely enough room for you to slip inside. What do you do?")
                    print("1. Go to the door, maybe you can find something to help you")
                    print("2. Go out the doors, at least you know that there's going to be help out there")
                    choice = input("Enter '1' or '2':")
                    if choice == '1':
                       print("You walked over to the room, entering. On a table, there's a relatively large book. As you walked closer, you noticed that it was open to a page that looked poorly written. Regardless, you could still make out that it was some pretty gruesome stuff. You suddenly hear a noise in the hallway, forcing you to make a decision quickly.")
                       print("1. Take the book and run")
                       print("2. Leave it, you don't have time for it")
                       choice = input("Enter '1' or '2':")
                       if choice == '1':
                            print("You hold onto the book tightly, running out of the building. You ran until you couldn't anymore, your heart pounding in your chest. You didn't fully know where you were just yet, but as long as you're not in there, it didn't really matter. Something's gotta be done about this place, even if it's the last thing you do.")
                            secrets_ending()
                       elif choice == '2':
                            print("You toss the book aside, making a break for the exit. You ran until you couldn't anymore, your heart pounding in your chest. You didn't fully know where you were just yet, but as long as you're not in there, it didn't really matter.")
                            good_ending()
                    elif choice == '2':
                         print("You exit the building, your heart pounding in your chest. You ran until you couldn't anymore, your legs giving out from under you as you entered the forest area bordering the edge of the hospital's parking lot. You were out of the hospital, meaning it'd take a whole lot more work on their end to find you again.")
                         good_ending()
                elif choice == '2':
                     print("You left it. It's not yours, so why bother it anymore? Exiting the closet, you hear some sounds coming from outside, more specifically from the right side. What do you do?")
                     print("1. Check it out, maybe someone can explain what's going on")
                     print("2. Uh uh, stay inside the room, it's none of your business")
                     print("3. What about somewhere else?")
                     choice = input("Enter '1', '2', or '3':")
                     if choice == '1':
                          print("As you're walking towards the sound, you feel your arm suddenly snag on something. At first, you thought it was nothing, perhaps a door handle, so you pulled pretty hard to loosen yourself. The sharp sting forced you to look back, revealing that it'd had snag on a broken hook from an IV rack, and a sharp hook at that.")
                          print("1. Crap! Maybe someone around here can help")
                          print("2. Just keep walking, it'll figure itself out")
                          print("What about the room next to you? Maybe it'll have something for it")
                          choice = input("Enter '1', '2', or '3':")
                          if choice == '1':
                               print("You tried looking around, moving about aimlessly until you had bumped into a person. Looking up, it was a large burly man, one that didn't seem all to pleased with you bumping into him. He grabbed you by the neck, taking you out of the dark hallway.")
                               bad_ending()
                          elif choice == '2':
                               print("You walked slowly down the hallway, blood slightly trailing behind you. The sense of dread from earlier persisted, though a newfound desperation emerged as well. Your head was beginning to hurt, but the end of the hallway was in sight. What do you do?")
                               print("1. Keep moving, you can't stop now")
                               print("2. Stop, there's no way you can keep going")
                               choice = input("Enter '1' or '2':")
                               if choice == '1':
                                    print("You keep pushing yourself, the headache causing your whole body to ache in utter pain. You'd finally reached the end of the hallway, the door in sight. To your left, you saw a door slowly open, just barely enough room for you to slip inside. On one hand, you could leave and find help, but on the other, you could stay and potentially find out what's going on. What do you do?")
                                    print("1. Go to the door, maybe you can find something to help you")
                                    print("2. Go out the doors, at least you know that there's going to be help out there")
                                    choice = input("Enter '1' or '2':")
                                    if choice == '1':
                                         print("You slip into the room, your head still throbbing. You notice on the table that there is a book, and it appeared as though someone had been reading it before suddenly dumping it there. You can either...")
                                         print("1. Open the book and read it, something's gotta be in there")
                                         print("2. Leave it, it's not yours to read")
                                         choice = input("Enter '1' or '2':")
                                         if choice == '1':
                                              print("You opened it and almost immediately felt sick to your stomach. Inside the book, you find all sorts of horrific notes, stripping people of their humanity, treating them like mere objects to test on and throw away. The signatures were amateur cursive, but you knew that it was definitely real.\nHearing a noise in the hallway, you tuck the book under your arm and make a break for it. You ran until you couldn't anymore, your heart pounding in your chest...")
                                              secrets_ending()
                                         elif choice == '2':
                                              print("You decide to leave the book alone, not wanting to waste any time on it. As you left the building, you managed to notice one of the cars was on, the soft humming filling the air. Against your good concious, you walked over and, sure enough, the keys were still inside. Taking the car and going on your way, you couldn't help but feel like you probably should've taken that book anyways.")
                                              good_ending()
                                    elif choice == '2':
                                         print("Exiting the building, you walked until you couldn't anymore. You'd made it surprisingly far, managing to get to an old gas station. The owner had let you in, though only for tonight, his words exactly.")
                                         good_ending()
                               elif choice == '2':
                                    print("The pain in your head is growing, feeling as if your body was being split apart from the head down. Finally, the heavy feeling in your chest leaves as you vomit, only to collapse right after. A doctor just so happens to find you lying there in your own mess, grabbing you by the leg to drag you away.")
                                    bad_ending()
                          elif choice == '3':
                               print("Walking into the room, it wasn't hard to see that it was a generic waiting room. What was harder to understand, however, was seeing a child standing in front of you: Jeremy. He looked at you, that same toothy smile that you'd come to know. But you knew it wasn't real, he'd been gone for a while now. Closing your eyes, you tried to make the hallucination go away...")
                               delusion_ending()
                     elif choice == '2':
                          print("Okay, keep it cool. It's probably nothing. On the bed, there seems to be some clipboard. At the same time, the window is just slightly open. What sounds better?")
                          print("1. The clipboard, surely something important is on it")
                          print("2. The window, maybe you can escape")
                          choice = input("Enter '1' or '2':")
                          if choice == '1':
                               print("Reading the papers, you see that they're all about you. A sharp pain suddenly filled your body, completely paralyzing you. As you held tightly onto the papers, you curled up into a ball, your body shaking uncontrollably as everything")
                               delusion_ending()
                          elif choice == '2':
                               print("On the way out, you made sure to take extra care to avoid slipping. The second you touched the groun, you were gone, running until your legs gave out from under you. Falling into the river, you could just barely keep yourself afloat.")
                               good_ending()
                     elif choice == '3':
                          print("Okay, so you've got two options: the room across from yours and the left hallway. Which way?")
                          print("1. The room across from you, maybe someone's in there")
                          print("2. The left hallway, the lights on must mean something good, right?")
                          choice = input("Enter '1' or '2':")
                          if choice == '1':
                               print("You walk into the room, taking in the sight of a person in a chair. From the door, it was unclear who it was, though, as you walked closer, the sight was shocking: it was your mom! She looked up at you with those familiar eyes, holding out a hand to you. Hesitant, you take her hand, feeling a sudden rush of shock move throughout you. The shock managed to have your heart racing to the point of giving out, causing you to collapse to the ground.")
                               delusion_ending()
                          elif choice == '2':
                               print("Just as you turned the corner, you were suddenly met with a person holding onto something large and metallic. You'd fight back if you could, but it'd be no use. They were already pinning you down and calling people over.")
                               bad_ending()
                elif choice == '3':
                     print("As you're walking towards the sound, you feel something grab onto your arm. Turning around, you see a man in a lab coat, his eyes locked onto you. As you tried pulling back, he suddenly landed a punch square in the face, knocking you out cold.")
                     bad_ending()
             elif choice == '2':
                print("You exit the closet and take a look around the room. You notice that they'd left behind a clipboard with some papers on it. At the same time, the door's been left open, but you also have a chance to look out the window for a moment. What would you like to do?")
                print("1. Look out the window")
                print("2. Look at the clipboard")
                print("3. Go out the door")
                choice = input("Enter '1', '2', or '3':")
                if choice == '1':
                  print(
                        "You look out the window and notice a stretcher had been left outside in the parking lot. It seems that something is covered up, but you can't quite make it out. Do you want to..."
                  )
                  print("1. Try to find your way down to it")
                  print("2. Leave it be, it's none of your business")
                  choice = input("Enter '1' or '2':")
                  if choice == '1':
                     print(
                          "You head out of the room and have two options: the left hallway or the right hallway. Which way?"
                     )
                     print("1. Down the left hallway, the lights will make it easier to see, so you might get there faster")
                     print("2. Down the right hallway, no one will see you, but it'll be hard to move around")
                     print("3. The room across from you might have something useful")
                     choice = input("Enter '1', '2', or '3':")
                     if choice == '1':
                        print("Walking down the hallway, you couldn't help but be bothered by the occasional sounds of agonizing screams and extreme discomfort coming from the closed off rooms. At the end of the hallway, you see a woman talking to a man in a lab coat. What do you do?")
                     print("1. Go back. Maybe you're better off going down the darker hallway")
                     print("2. Walk up and ask them some questions")
                     print("3. Slip into the slightly open door to the side of you")
                     choice = input("Enter '1', '2', or '3':")
                  elif choice == '2':
                     print(
                          "You're probably better off ignoring it. Walking away from the window, you realize that it'll probably be a while before anyone shows up again. The clipboard is still sitting there, but the door is open, a chance of escaping. What do you do?"
                     )
                     print("1. Look at the clipboard")
                     print("2. Go out the door")
                     print("3. What about the window?")
                     choice = input("Enter '1', '2', or '3':")
                     if choice == '1':
                        print(
                             "You walk over to the clipboard and notice that there are a few papers on it. You can either..."
                        )
                     elif choice == '2':
                        print(
                             "You exit the door, and notice two hallways: one has lights and the other is dark. At the same time, there's a room across from you, likely occupied by another person in the same situation. Which way will you go?"
                        )
                     elif choice == '3':
                        print(
                             "You walk back over to the window and realize that it's unlocked. Pulling up a few times, a sudden rush of air hits your face. Now's the time to choose..."
                        )
                        print(
                             "1. Climb out the window, but it's a long way down if you slip"
                        )
                        print(
                             "2. Stay inside, only crazy people try climbing out windows at night"
                        )
                        choice = input("Enter '1' or '2':")
                        if choice == '1':
                          print(
                                "You climb out the window, but end up slipping and falling. At the very least the stretcher acts like a cushion, but you're still hurt. You're able to get up and walk away, though. You've made it out of the hospital, but you're not sure where you are. You're just glad to be out of there."
                          )
                          good_ending()
                        elif choice == '2':
                          print(
                                "Trying to stay safe is probably the best way to go right now. There's a good bit you could do right now. There's always that stupid clipboard, the door, and just laying back down."
                          )
                          print("1. Look at the clipboard, maybe kill some time")
                          print("2. Go out the door, maybe you could find help")
                          print("3. Lay down, this is becoming too stressful!")
                          choice = input("Enter '1', '2', or '3':")
                          if choice == '1':
                             print(
                                  "You walk over to the clipboard and notice that there are a few papers on it. You can either..."
                             )
                             print(
                                  "1. Look at the papers, something has to be on there"
                             )
                             print("2. They're probably fakes, just leave them be")
                             choice = input("Enter '1' or '2':")
                             if choice == '1':
                                print(
                                     "You pick up the papers and begin to read them. They're all about one thing: you. It was insane! Surely this wasn't true, but you couldn't help but feel a little sick to your stomach. You can either..."
                                )
                                print("1. Keep reading, maybe it'll help you")
                                print("2. Throw them away, it's too much!")
                                print(
                                     "3. Shove them into your pocket, you might need them later"
                                )
                                choice = input("Enter '1', '2', or '3':")
                                if choice == '1':
                                  print(
                                        "You continue to read until you suddenly feel lightheaded. You stumble for a moment, trying to catch onto something, suddenly, you fell over and everything goes black."
                                  )
                                  delusion_ending()
                                elif choice == '2':
                                  print(
                                        "You ball the papers up and toss them into the trash can, quickly exiting the room right after, feeling a bit queasy after reading the documents. Upon exiting the room, you notice three things: a well-lit hallway to your left, a dark one to your right, and a room straight ahead. Which do you choose?"
                                  )
                                  print(
                                        "1. To the left, maybe you'll find something, and it'll be easy with all those lights"
                                  )
                                  print(
                                        "2. To the right, maybe you can escape, but finding an exit will be much harder"
                                  )
                                  print(
                                        "3. Straight ahead, maybe you'll find someone who can help you"
                                  )
                                  choice = input("Enter '1', '2', or '3':")
                          elif choice == '2':
                             print(
                                  "You exit the room and notice that there are two different hallways; the left has working lights while the right is nearly pitch black. You also notice that there's a room across from you, likely occupied by another person in the same situation. Which way will you go?"
                             )
                             print(
                                  "1. Down the left hallway, though the lights might give you away, so be cautious"
                             )
                             print(
                                  "2. Go down the right hallway, though it'll be hard to see, you might be able to escape"
                             )
                             print(
                                  "3. The room ahead, something or someone useful just has to be in there"
                             )
                             choice = input("Enter '1', '2', or '3':")
                             if choice == '1':
                                print(
                                     "Walking down the hallway, an orchestra of screams and moans fill your ears. You can't help but feel a bit sorry for them. At the end of the hallway, you see a woman talking to a man in a lab coat, seemingly frustrated about something. What do you do?"
                                )
                                print(
                                     "1. Try talking to them, maybe they know what's going on"
                                )
                                print("2. Turn around, and be quick with it!")
                                print(
                                     "3. Slip into the room next to you. Maybe you can listen in from there"
                                )
                                choice = input("Enter '1', '2', or '3':")
                             elif choice == '2':
                                print(
                                     "Walking down the hallway, you felt a constant sense of dread, almost like you're being watched. In your moment of distraction, the worst happened: your foot was cut pretty badly by stray glass on the ground, a pool of blood already forming."
                                )
                                print(
                                     "1. Shoot! Maybe try finding someone to help you")
                                print(
                                     "2. Keep moving, you can try finding someone once you're out of here"
                                )
                                print(
                                     "3. Stop and clean the wound, you can't keep moving with this much blood, it'll make a trail"
                                )
                                choice = input("Enter '1', '2', or '3':")
                                if choice == '1':
                                  print(
                                        "You tried looking around, moving about aimlessly until you had bumped into a person. Looking up, it was a large burly man, one that didn't seem all to pleased with you bumping into him. He took in the sight of you, then your wound, then locked eyes again. What do you do?"
                                  )
                                  print(
                                        "1. Try to explain yourself, maybe he'll understand"
                                  )
                                  print(
                                        "2. Quick, run away! His size will probably weigh him down"
                                  )
                                  print(
                                        "3. Try pushing past him, maybe you can find help elsewhere"
                                  )
                                  choice = input("Enter '1', '2', or '3':")
                                elif choice == '2':
                                  print(
                                        "You limped down the hallway, blood slightly trailing behind you. The sense of dread from earlier persisted, though a newfound desperation emerged as well. Your head was beginning to hurt, but the end of the hallway was in sight. What do you do?"
                                  )
                                  print("1. Keep moving, you can't stop now")
                                  print("2. Stop, there's no way you can keep going")
                                  choice = input("Enter '1' or '2':")
                                  if choice == '1':
                                       print("You keep pushing yourself, the headache causing your whole body to ache in utter pain. You'd finally reached the end of the hallway, the door in sight. To your left, you saw a door slowly open, just barely enough room for you to slip inside. On one hand, you could leave and find help, but on the other, you could stay and potentially find out what's going on. What do you do?")
                                  print("1. Go to the door, maybe you can find something to help you")
                                  print("2. Go out the doors, at least you know that there's going to be help out there")
                                  choice = input("Enter '1' or '2':")
                                  if choice == '1':
                                     print(
                                          "You slip into the room, your head still throbbing. You notice on the table that there is a book, and it appeared as though someone had been reading it before suddenly dumping it there. You can either..."
                                     )
                                     print(
                                          "1. Open the book and read it, something's gotta be in there"
                                     )
                                     print("2. Leave it, it's not yours to read")
                                     choice = input("Enter '1' or '2':")
                                     if choice == '1':
                                        print(
                                             "Inside the book, you find all sorts of horrific notes, stripping people of their humanity, treating them like mere objects to test on and throw away. The signatures were amateur cursive, but you knew that it was real. It didn't help that it looked like one of the pages had your name, meaning you'd probably just gotten here. What now?"
                                        )
                                        print("1. Put it down, it's not yours!")
                                        print(
                                             "2. Take the book and run, you have to reveal the truth!"
                                        )
                                        choice = input("Enter '1' or '2':")
                                        if choice == '1':
                                          print(
                                                "You leave the book alone before leaving the room, rushing out the glass doors before anyone could spot you. You ran until your legs gave out from under you. Despite being in the middle of a forest, you felt secure. Perhaps it was the fact that you were out of the hospital, or perhaps it was the amazing sight above you."
                                          )
                                          good_ending()
                                        elif choice == '2':
                                          print(
                                                "You snatch it up and rush out, not even bothering to look back. It wasn't until you had ran out to the edge of an interstate did you finally stop in your tracks. A truck slowed down, allowing you to hop inside so long as they could drop you off somewhere. During the entire ride, you remained silent, your mind racing with the thoughts of what you'd just seen."
                                          )
                                          secrets_ending()
                                     elif choice == '2':
                                        print(
                                             "You decide to leave the book alone, not wanting to waste any time on it. Just as you had reached the door, a sudden surge of pain struck you, causing you to fall to the ground. You couldn't help but feel like you were being attacked from the inside out. Turning around, you see a woman towering over you, a metal object in hand being the last thing you see before blacking out."
                                        )
                                        bad_ending()
                                  elif choice == '2':
                                     print(
                                          "You limp your way towards the door, finally getting out of there. You notice a stretcher, and walk over to it. However, just as you were about to lift up the cloth, you hear a sudden noise, making you jump and flee the area."
                                     )
                                     good_ending()
                                  elif choice == '2':
                                     print("You made an abrupt stop, nearly falling over. You held onto your head, trying to keep it together. Somehow, the pain hurt more just by standing there. There's no way you can keep going, not unless you're really crazy enough to do so.")
                                     print("1. Crazy's your middle name, now move")
                                     print("2. You're not crazy, you just need to rest")
                                     choice = input("Enter '1' or '2':")
                                     if choice == '1':
                                        print("Finally, you reach the end of the hallway. You hear a small sniffling sound coming from your left, but there's also a glass double door to your right. You can almost taste freedom...")
                                        print("1. Someone needs help, go to the left")
                                        print("2. It's none of your business, go to the right")
                                        choice = input("Enter '1' or '2':")
                                        if choice == '1':
                                          print("Upon entering a room, you notice a wooden table. Walking closer, you see...a tape recorder?! Whipping around, a man is already behind you, his baton striking you in the head. He was followed by a woman with a strait jacket, her hands moving quickly to lock you inside it.")
                                          bad_ending()
                                        elif choice == '2':
                                          print("You walk towards the doors, your hand shakily reaching out towards it. Out the corner of your eye, you see a slightly ajar wooden door, but freedom is right in sight. Well, that, and a stretcher with something on it outside. But there's a door, maybe something cool's in there!")
                                          print("1. What are you, ten? Go out the door!")
                                          print("2. Go check it out, who can resist cool stuff behind mysterious doors?")
                                          choice = input("Enter '1' or '2':")
                                          if choice == '1':
                                             print("You exit the building, your head still throbbing. The second you can find a bus, you're heading to the hospital, that much is clear. You walked over to the stretcher, carefully picking up the cloth, only to find a body underneath. While expected, it was still frightening, causing you to book it out of there.")
                                             good_ending()
                                          elif choice == '2':
                                             print("You walk over to the door, careful not to make too much noise. Upon entering, you notice a large book on a table. You can either...")
                                             print("1. Open the book and read it, something's gotta be in there")
                                             print("2. Leave it be, you're not crazy enough to read random books")
                                             choice = input("Enter '1' or '2':")
                                             if choice == '1':
                                                print("You open the book and begin to read. It was filled to the brim with sick and twisted ideas, treating people as though they're mere objects to test on and throw away! And the signatures, talk about amateur cursive!")
                                                print("1. Put it down, it's not yours!")
                                                print("2. Take the book and run, you have to reveal the truth!")
                                                print("3. Wait, read on...something's sticking out a couple pages in!")
                                                choice = input("Enter '1', '2', or '3':")
                                                if choice == '1':
                                                  print("You put down the book. After all, stealing's not right, regardless of the situation. You sneak over to the double doors, exiting before anyone really noticed. You rushed out, though you couldn't help but feel a bit guilty.\nYou know what's happening here, yet you've left the evidence. Yeah, it's not your job to expose them, but you can't help but feel like you should've done something.")
                                                  good_ending()
                                                elif choice == '2':
                                                  print("You took the book and rushed out, your heart pounding in your chest. You can't help but feel like you're doing the right thing, but you can't help but feel guilty as well. You know what's happening here, and you have proof, but what if everyone else is just like them? What if they just call you crazy? As you continue running away from the place, the feeling continues to grow, unwilling to budge.")
                                                  secrets_ending()
                                                elif choice == '3':
                                                  print("Quickly flipping through the pages, you reach the note. It was another letter, a mother asking what had happened to her son. It's sickening, considering you'd just seen a page about him, a gruesome thing.\nWhile reading, you hear footsteps, followed by the sound of a door opening. Turning around, you see a man in a lab coat, his eyes locked onto you. What do you do?")
                                                  print("1. Push him over, then try to run")
                                                  print("2. Try to explain yourself, maybe he'll understand")
                                                  print("3. Throw the book at him, maybe it'll distract him")
                                                  print("4. Shove the book into your pocket and dip!")
                                                  choice = input("Enter '1', '2', '3' or '4':")
                                                  if choice == '1':
                                                     print("Not sure why you'd even try that in the first place, as he managed to block your attack before you could even fully place your hands on him. Tackling you to the ground, there wasn't enough time to react as he'd suddenly tased you, leaving you unconscious.")
                                                     bad_ending()
                                                  elif choice == '2':
                                                     print("You tried explaining, but you kept fumbling over your words, only making things worse. He grabbed you, his grip tightening around your neck. You tried to scream, but you couldn't make a sound. You continued to struggle, but it was no use. You were taken away, never to be seen again")
                                                     bad_ending()
                                                  elif choice == '3':
                                                     print("The pain from the sudden impact distracts him just long enough for you to slip past and get out of there! You ran until you couldn't run anymore, your heart pounding in your chest. You didn't fully know where you were just yet, but as long as you're not in there, it didn't really matter.")
                                                     good_ending()
                                                  elif choice == '4':
                                                     print("You shove the book into your pocket and make a break for it. Thankfully, the man was just disoriented enough by all your movement that you could slip past and burst through the doors. You didn't know where you were, but you knew you were out of there. As far as you're concerned, something's going to be done about this place, even if it's the last thing you do."\)
                                                     secrets_ending()
                                             elif choice == '2':
                                                print("You put the book down, deciding it's not worth you time, and head out the room. However, just as you exited, three people were waiting outside, all of them ready to pin you down in a second. What do you do?")
                                                print("1. Fight back, you're not going down without a fight")
                                                print("2. Lie and say it's your first day and that you need a uniform")
                                                print("3. Hurry, sprint past them! They can't all lunge at once!")
                                                choice = input("Enter '1', '2', or '3':")
                                                if choice == '1':
                                                  print("You tried to fight back, but you were no match for them. They were all too strong, too many. You were pinned down, and you couldn't move. You tried to scream, but you couldn't make a sound. You continued to struggle, but it was no use. You were taken away, never to be seen again.")
                                                  bad_ending()
                                                elif choice == '2':
                                                  print("You lied, right through your teeth, and they somehow believed you. Taking you by the arm, they led you to a room, where you were given a uniform, only to be ushered around through each room, made to take notes. The whole time, you couldn't help but think about the things you saw.")
                                                  traitor_ending()
                                                elif choice == '3':
                                                  print("You sprinted past them, your heart pounding in your chest. You didn't look back, didn't care what happened to you. You just kept running, until you finally made it out of the building. You were out of the hospital, but you were still in danger. You knew, no matter what, you were never going to truly be safe. At the very least, you didn't have to worry about them tonight.")
                                                  good_ending()
                                     elif choice == '2':
                                        print("The pain in your head is growing, feeling as if your body was being split apart from the head down. Finally, the heavy feeling in your chest leaves as you vomit, only to collapse right after. The world around you slowly fades to black...")
                                        delusion_ending()
                          elif choice == '3':
                             print("You lay down, a pain in your head beginning to grow rapidly. Still, the soft surface of the pillow is comforting, almost erasing the pain for a moment. Closing your eyes, you slowly drift off to sleep...")
                             delusion_ending()
                elif choice == '2':
                  print("As you draw closer to it, the name on it is more apparent...it looks like yours. Do you dare to read further?")
                  print("1. Yes, maybe it'll help me")
                  print("2. No, it must be fake")
                  choice = input("Enter '1' or '2':")
                  if choice == '1':
                      print("Flipping through the pages, you see that they're all about you. A sharp pain suddenly filled your body, completely paralyzing you. As you held tightly onto the papers, you curled up into a ball, your body shaking uncontrollably as everything")
                      delusion_ending()
                  elif choice == '2':
                     print("The papers were probably fakes anyways, so no point in entertaining them. You walk out the door and notice two hallways: one has lights and the other is dark. Which way?")
                     print("1. Down the left hallway, the lights make it easier to see")
                     print("2. Down the right hallway, the darkness could cover you")
                     print("3. The room across from you, someone might be in there")
                     choice = input("Enter '1', '2', or '3':")
                     if choice == '1':
                         print("Walking through the bright hallway, a bulb had suddenly fell in front of you, causing you to jump back into someone. The woman let out an agitated sound before wrapping her hands around your neck, choking you out as a couple other people came to check out what all the noise was for...")
                         bad_ending()
                     elif choice == '2':
                         print("The darkness made it incredibly difficult to see, everything blending in with each other. As you were walking, you slip on something, falling to the ground. A sharp pain radiates through your body as you realize that something on the floor must've punctured")
                         print("1. Try to get up and keep moving")
                         print("2. Oh God, this is it, it's the end for me! (dramatic much...)")
                         choice = input("Enter '1' or '2':")
                         if choice == '1':
                             print("You manage to get up, albeit with some difficulty. You keep moving, your head throbbing in pain. Eventually, you reach the end of the hallway, the door in sight. To your left, you see a door slowly open, just barely enough room for you to slip inside. On one hand, you could leave and find help, but on the other, you could stay and potentially find out what's going on. What do you do?")
                             print("1. Out the exit")
                             print("2. The room next to you")
                             choice = input("Enter '1' or '2':")
                         elif choice == '2':
                             print("Seriously? You're just gonna lay there? Well, it's not like you've got a choice now, as a doctor walked out of the room next to you andd just noticed you lying there like a little kid in the middle of a tantrum. Rolling his eyes, he grabbed onto your legs and began pulling...")
                             bad_ending()
                     elif choice == '3':
                         print("Walking into the room, you saw someone sitting in the bed: your mother. She was dazed for a moment, trying to take in your shadowed figure. Once she could tell it was you, she ran over and wrapped you in a warm embrace. You closed your eyes, the warmth of it allowing you to sink into it...")
                         delusion_ending()
                elif choice == '3':
                  print("You exit the door, and notice two hallways: one has lights and the other is dark. At the same time, there's a room across from you, likely occupied by another person in the same situation. Which way will you go?")
                  print("1. Down the left hallway, the lights make it easier to see")
                  print("2. Down the right hallway, the darkness could cover you")
                  print("3. The room across from you, maybe someone's in there after all")
                  choice = input("Enter '1', '2', or '3':")
                  if choice == '1':
                        print("Walking down the left hallway, it was filled to the brim with an ochestra of medical equipment and screaming. It was both sad and somewhat irritating, the sounds messing with your already aching head. At the end of the hallway, you see a woman talking to a man in a lab coat, seemingly frustrated about something. What do you do?")
                        print("1. Try talking to them, maybe they know what's going on")
                        print("2. Turn around and go the other way")
                        print("3. Slip into the room next to you")
                        choice = input("Enter '1', '2', or '3':")
                        if choice == '1':
                             print("You walk up to them, trying to get their attention. They look up at you, their eyes filled with a sense of frustration. Once they'd registered that you were, in fact, not a doctor, they pulled out their tasers, the both of them striking you down to the ground. Honestly, it was a bit of an overkill reaction.")
                             bad_ending()
                        elif choice == '2':
                             print("You made your way down the hallway, careful to avoid everything around you as a putrid smell invaded your nostrils. Eventually, you made your way towards a pair of glass doors, along with a wooden door to the left of them. Which will you choose?")
                             print("1. The glass doors, let's get out of here")
                             print("2. The wooden door, maybe there's something cool in there")
                             choice = input("Enter '1' or '2':")
                             if choice == '1':
                                 print("You walk out of the building, surprisingly feeling a lot calmer than before. Eventually, you made your way to a bus stop, sitting down on the bench to wait on the bus. While wating, your thoughts finally had time to run buck wild throughout your head, causing you to nearly miss the bus when it did arrive.")
                                 good_ending()
                             elif choice == '2':
                                 print("You walk into the room, noticing almost immediately that a book was sitting on a table admist the cluttered mess that made up the room. Walking closer, it was open to a page that looked poorly written. Regardless, you could still make out that it was some pretty gruesome stuff.")
                                 print("1. Take the book and run")
                                 print("2. Leave it, it's not yours")
                                 choice = input("Enter '1' or '2':")
                                 if choice == '1':
                                     print("Well, you don't really need to run right now. It seems like nobody was dwn here at the moment, so you had time to walk. Well, that was until a car began pulling into the parking lot, the driver locking eyes with you. Almost immediately, you ran away, ending up under a bridge by the time you tired out.")
                                     secrets_ending()
                                 elif choice == '2':
                                     print("You left the book alone, no longer interested. However, just as you were walking out of the building, someone was walking in. The man constantly kept pushing you while asking a million questions per second, eventually causing you to fall over. Before you could really fight with him, he was already calling people over...")
                                     bad_ending()
                        elif choice == '3':
                             print("Slipping into the room, your eyes fell onto the figure standing next to you. You couldnt believe it: your father was just standing next to you like everything was normal. He looked at you, noticing your slightly disheveled appearance. As he placed a hand onto your shoulder, you suddenly fell over, the last thing you see being your father's distressed expression.")
                             delusion_ending()
                  elif choice == '2':
                        print("Walking down the right hallway, you felt a constant sense of dread, almost like you're being watched. In your moment of distraction, the worst happened: your foot was cut pretty badly by stray glass on the ground, a pool of blood already forming")
                        print("1. Find someone to help, there's clearly doctors here")
                        print("2. Just keep walking, it'll heal itself...hopefully")
                        print("3. Stop to clean up")
                        choice = input("Enter '1', '2', or '3':")
                        if choice == '1':
                             print("As you try looking for someone, you bumped into a wall. Feeling your way around, you felt something soft. Opening your eyes, it was the lab coat of a pretty tall guy, who was now frustrated with you touching him. He snatched you up, deciding to dispose of you somewhere.")
                             bad_ending()
                        elif choice == '2': 
                             print("After a long while of dragging your foot along, the pain being much more impactful than you thought it'd be, you finally reached the end of the hallway. You see a door to your left, and a pair of glass doors in front of you. Which way?")
                             print("1. Glass doors, let's head home")
                             print("2. Door to the left of you")
                             choice = input("Enter '1' or '2':")
                             if choice == '1':
                                  print("You exit the building, your head still throbbing. The second you can find a bus, you're heading to the hospital, that much is clear. You walked over to the stretcher, carefully picking up the cloth, only to find a body underneath. While expected, it was still frightening, causing you to book it out of there.")
                                  good_ending()
                             elif choice == '2':
                                  print("You walk into the room, noticing almost immediately that a book was sitting on a table admist the cluttered mess that made up the room. Walking closer, it was open to a page that looked poorly written. Regardless, you could still make out that it was some pretty gruesome stuff.")
                                  print("1. Take the book and run")
                                  print("2. Leave it, it's not yours")
                                  choice = input("Enter '1' or '2':")
                                  if choice == '1':
                                        print("You tuck it under your arm and run out, running until your foot finally gave out from under you, causing you to fall into a puddle. It was a pain like no other...and was definitely going to get infected sooner or later...")
                                        secrets_ending()
                                  elif choice == '2':
                                        print("You leave the book alone, deciding that it's not worth your time. Exiting the building, you decided to sneak along the edge of the building until you reached the edge of the parking lot, running off into the forest afterwards.")
                                        good_ending()
                        elif choice == '3':
                             print("Trying to find something, you end up taking your shirt off, a desperate attempt to stop the bleeding. Dabbing at it was a pain in the rear end, though that was quickly replaced by a violent surge of electricity coursing throughout your body. You fell to the ground, your body shaking uncontrollably as you looked back and saw two women looking down at you. Taking ahold of you, they began to drag you out of the dark hallway.")
                             bad_ending()
                  elif choice == '3':
                        print("You walk over to the room, taking in the sight of a person in a chair. From the door, it was unclear who it was, though, as you walked closer, the sight was shocking: it was your mom! She looked up at you with those familiar eyes, holding out a hand to you. Hesitant, you take her hand, feeling a sudden rush of shock move throughout you. The shock managed to have your heart racing to the point of giving out, causing you to collapse to the ground.")
                        delusion_ending()
          elif choice == '2':
             print("It's an unbearbly tight squeeze, pressing down hard on you, but you keep quiet anyways. Things are knocked around and you hear some angry comments. Suddenly, the footsteps grow closer. What do you do?")
             print("1. Stay in place")
             print("2. Get out and fight back")
             print("3. Hop out and run")
             choice = input("Enter '1', '2', or '3':")
             if choice == '1':
                     print("You remained under the bed, your breathing beginning to grow heavier from the lack of oxygen. It's incredibly hard to stay still, and the footsteps only seem to be getting closer. Just as they began lifting the bed, you faint.")
                     delusion_ending()
             elif choice == '2':
                     print("You squeeze out of the bed, ready to fight back. However, because of how long it took you to get out from under there, they easily overpowerd you, laughing like it was some inside joke you weren't apart of. Well, you are, but as the joke.")
                     bad_ending()
             elif choice == '3':
                     print("Squeezing out from under the bed took a lot out of you, disorienting you slightly. As you tried to make a break for it, one of the doctors held a foot out, tripping you up and sending you crashing into the wall, nearly knocking you unconcious from the impact.")
                     bad_ending()
          elif choice == '3':
             print("The first place they looked was behind the sheer fabric of the curtain. They bombard you with questions, but don't seem to be the brightest of the bunch. You can either...")
             print("1. Fight back")
             print("2. Lie and say you were looking for a patient")
             print("3. Ask what's happening and why you're here")
             print("4. Quickly run past them")
             choice = input("Enter '1', '2', '3', or '4':")
             if choice == '1':
                  print("Alright," + name + ", wannabe Tommy Tough Knuckles, they might not be the the brightest of the bunch, but they're still pretty strong. They land a good couple of punches on you, knocking you to the floor long enough that they could drag you out with no problem. Real smart, bud.")
                  bad_ending()
             elif choice == '2':
                  print("Even if didn't want to, you allowed yourself to lie straight through your teeth, creating some long elaborate story about how you were just a new employee, and that you were looking for a patient. They seemed to buy it, leading you to a room where you were given a uniform, making comments about how ridiculous you looked in your current attire.")
                  traitor_ending()
             elif choice == '3':
                  print("You ask them some questions, but they just look at you like you've gone mad. Eventually, the two grab you by your arms, taking you out of the room.")
                  bad_ending()
             elif choice == '4':
                  print("You run out and, without thinking, run into the room right across from yours. Inside is what looks to be another person and a slightly ajar window. You could potentially escape out of the window, but you could also investigate the possible person.")
                  print("1. Jump out the window, surely there'll be something to break your fall")
                  print("2. Find out if it's a body or just a terrible sleeper")
                  choice = input("Enter '1' or '2':'")
                  if choice == '1': 
                      print("Why in your right mind did you just jump out of a window? Yeah, your fall was broken, but by a tree. As you tried fighting your way out of the limbs of the tree, a group of hands were suddenly pulling you down, only for you to be dragged off to who knows where.")
                      bad_ending() 
                  elif choice == '2':
                        print("You slowly crept over to the person, careful not to make too much noise in case they truly were sleeping. Lifting the cover away, you're met with the sight of fully opened eyes staring up at you. Just as you were about to scream, their hand grabbed onto your wrist, pulling you close enough to hear them scream at you to wake up, repeating themselves until you'd closed your eyes shut.")
                        delusion_ending()     
          elif choice == '4':
                print("Yeah, okay, Dangerous Dan, you end up just getting tased to the ground, your constantly shaking and jerking body being dragged out of the room by two doctors.")
                bad_ending() 
     elif choice == '2':
          print("No point in checking stuff out, huh? As you continued to lay there, you couldn't help but feel drowsy. Your eyes fluttered for a moment, trying their hardest to remain open, but it was no use. It wasn't long before you fell into a deep sleep...")
          delusion_ending()
start_game()
