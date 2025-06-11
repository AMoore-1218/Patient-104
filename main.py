def play_again():
  print("\n" + "="*50)
  choice = input("Would you like to play again? (y/n):").lower()
  if choice == 'y' or choice == "yes":
    print("\n" + "="*50)
    start_game()

def bad_ending():
  print("You should've just minded your business, keep a low cover. Now, you're being dragged into a dark, cold room by two men dressed in all white lab coats, never to be seen again.")
  print("You've got the bad ending. Would you like to play again to get a new ending?")
  play_again()

def good_ending():
  print("You managed to get out of the hospital with everything you came in with…give or take. Maybe next time avoid random places advertising free cream cheese bagels.")
  print("You got the good ending. Would you like to play again to get a new ending?")
  play_again()

def secrets_ending():
  print("You found a book of all sorts of twisted documents, detailing all the terrible things these people came up with in here. Who knows how many more they'll be going after! It's time to tell the world what you saw…")
  print("You've got the secrets ending. Would you like to play again to get a new ending?")
  play_again()

def traitor_ending():
  print("You're really willing to give up your morals just to save your own hide, huh? Not like you can change it, you're one of them now, meaning there's no way things will be the same again.")
  print("You've got the traitor ending. Would you like to play again to get a new ending?")
  play_again()

def start_game():
  name = input("Enter your name:")
  print("Welcome, " + name + "!")
  print(name + ", you are in a dark room, lying in bed. There is a door to your left and a window to your right, what do you choose?")
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

  elif choice == '2':
    print("You move over to the window and notice that it's a relatively full parking lot down below. Perhaps you're in a hospital? While looking out the window, you hear noises from the hallway, what do you do?")
    print("1. Go to the door")
    print("2. Go back to bed and pretend to sleep.")
    print("3. Try to hide")
    choice = input("Enter '1', '2', or '3':")    
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
      print("You kept your head against the pillow and heard a noise from the hallway, what do you do?")
      print("1. Try to hide")
      print("2. Check it out")
      print("3. Close your eyes and pretend to sleep")
      choice = input("Enter '1', '2', or '3':")
start_game()