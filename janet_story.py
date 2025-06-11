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
    elif choice == '2':
      print("You kept your head against the pillow and heard a noise from the hallway, what do you do?")
start_game()