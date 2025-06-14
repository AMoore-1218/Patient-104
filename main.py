from fasthtml.common import *
from fasthtml import RedirectResponse

app, rt = fast_app()

# Store game state in a simple session-like structure
game_states = {}

def get_game_state(session_id):
    if session_id not in game_states:
        game_states[session_id] = {
            'current_step': 'start',
            'player_name': '',
            'choices': []
        }
    return game_states[session_id]

def reset_game_state(session_id):
    game_states[session_id] = {
        'current_step': 'start',
        'player_name': '',
        'choices': []
    }

@rt("/")
def get():
    return Titled("Patient 104",
        Div(
            H1("Welcome to Patient 104"),
            P("A thrilling text-based adventure game"),
            Form(
                Input(type="text", name="player_name", placeholder="Enter your name", required=True),
                Button("Start Game", type="submit"),
                method="post", action="/start"
            ),
            style="max-width: 600px; margin: 0 auto; padding: 20px; text-align: center;"
        )
    )

@rt("/start")
def post(player_name: str):
    session_id = "default"  # In a real app, you'd use proper session management
    state = get_game_state(session_id)
    state['player_name'] = player_name
    state['current_step'] = 'initial_choice'

    return Titled("Patient 104",
        Div(
            H2(f"Welcome, {player_name} to Patient 104!"),
            P("You are in a dark room, lying in bed. There is a door to your left and a window to your right, what do you choose?"),
            Form(
                Div(
                    Input(type="radio", name="choice", value="1", id="choice1"),
                    Label("Go to the door on the left", _for="choice1"),
                    Br(),
                    Input(type="radio", name="choice", value="2", id="choice2"),
                    Label("Look out the window on the right", _for="choice2"),
                    Br(),
                    Input(type="radio", name="choice", value="3", id="choice3"),
                    Label("Remain in bed", _for="choice3"),
                    Br(), Br(),
                    Button("Make Choice", type="submit")
                ),
                method="post", action="/choice"
            ),
            style="max-width: 600px; margin: 0 auto; padding: 20px;"
        )
    )

@rt("/choice")
def post(choice: str):
    session_id = "default"
    state = get_game_state(session_id)

    # Handle the choice logic
    if state['current_step'] == 'initial_choice':
        if choice == '1':
            return door_choice()
        elif choice == '2':
            return window_choice()
        elif choice == '3':
            return bed_choice()

    # Add more choice handling logic here for different game states
    return RedirectResponse("/")

def door_choice():
    return Titled("Patient 104",
        Div(
            P("You walk over to the door. It doesn't seem to be locked, as far as you can tell. Do you want to open it?"),
            Form(
                Div(
                    Input(type="radio", name="choice", value="1", id="choice1"),
                    Label("Try opening the door", _for="choice1"),
                    Br(),
                    Input(type="radio", name="choice", value="2", id="choice2"),
                    Label("Go back to bed", _for="choice2"),
                    Br(),
                    Input(type="radio", name="choice", value="3", id="choice3"),
                    Label("Look around the room", _for="choice3"),
                    Br(),
                    Input(type="radio", name="choice", value="4", id="choice4"),
                    Label("Go to the window", _for="choice4"),
                    Br(), Br(),
                    Button("Make Choice", type="submit")
                ),
                method="post", action="/door-action"
            ),
            style="max-width: 600px; margin: 0 auto; padding: 20px;"
        )
    )

def window_choice():
    return Titled("Patient 104",
        Div(
            P("You move over to the window and notice that it's a relatively full parking lot down below. 'Am I in a hospital?' You think to yourself. While looking out the window, you hear noises from the hallway."),
            Form(
                Div(
                    Input(type="radio", name="choice", value="1", id="choice1"),
                    Label("Go over to the door", _for="choice1"),
                    Br(),
                    Input(type="radio", name="choice", value="2", id="choice2"),
                    Label("Go to bed and pretend to sleep", _for="choice2"),
                    Br(),
                    Input(type="radio", name="choice", value="3", id="choice3"),
                    Label("Try to hide", _for="choice3"),
                    Br(), Br(),
                    Button("Make Choice", type="submit")
                ),
                method="post", action="/window-action"
            ),
            style="max-width: 600px; margin: 0 auto; padding: 20px;"
        )
    )

def bed_choice():
    return Titled("Patient 104",
        Div(
            P("You remained in bed and suddenly hear something beeping in your ear. Will you investigate?"),
            Form(
                Div(
                    Input(type="radio", name="choice", value="1", id="choice1"),
                    Label("Yes", _for="choice1"),
                    Br(),
                    Input(type="radio", name="choice", value="2", id="choice2"),
                    Label("No", _for="choice2"),
                    Br(), Br(),
                    Button("Make Choice", type="submit")
                ),
                method="post", action="/bed-action"
            ),
            style="max-width: 600px; margin: 0 auto; padding: 20px;"
        )
    )

@rt("/door-action")
def post(choice: str):
    if choice == "1":
        return hallway_choice()
    elif choice == "2":
        return delusion_ending()
    # Add more door action logic here
    return RedirectResponse("/")

@rt("/window-action")
def post(choice: str):
    if choice == "3":
        return hiding_choice()
    # Add more window action logic here
    return RedirectResponse("/")

@rt("/bed-action") 
def post(choice: str):
    if choice == "2":
        return delusion_ending()
    # Add more bed action logic here
    return RedirectResponse("/")

def hallway_choice():
    return Titled("Patient 104",
        Div(
            P("You open the door, entering out into the hallway. You hear some noises, though it's unclear just where it's coming from."),
            Form(
                Div(
                    Input(type="radio", name="choice", value="1", id="choice1"),
                    Label("Left hallway. The lights are on, so someone's probably doing something down there", _for="choice1"),
                    Br(),
                    Input(type="radio", name="choice", value="2", id="choice2"),
                    Label("The room across from you. Someone's definitely in there", _for="choice2"),
                    Br(),
                    Input(type="radio", name="choice", value="3", id="choice3"),
                    Label("Right hallway. Maybe someone left something on", _for="choice3"),
                    Br(), Br(),
                    Button("Make Choice", type="submit")
                ),
                method="post", action="/hallway-action"
            ),
            style="max-width: 600px; margin: 0 auto; padding: 20px;"
        )
    )

def hiding_choice():
    return Titled("Patient 104",
        Div(
            P("There's really only three places to hide: the closet, under the bed, and behind the curtain. Which way?"),
            Form(
                Div(
                    Input(type="radio", name="choice", value="1", id="choice1"),
                    Label("The closet, seems smart", _for="choice1"),
                    Br(),
                    Input(type="radio", name="choice", value="2", id="choice2"),
                    Label("Under the bed, though it'll be a tight squeeze", _for="choice2"),
                    Br(),
                    Input(type="radio", name="choice", value="3", id="choice3"),
                    Label("Behind the curtain, though it's pretty risky", _for="choice3"),
                    Br(),
                    Input(type="radio", name="choice", value="4", id="choice4"),
                    Label("Stand brave, you're not scared of anything!", _for="choice4"),
                    Br(), Br(),
                    Button("Make Choice", type="submit")
                ),
                method="post", action="/hiding-action"
            ),
            style="max-width: 600px; margin: 0 auto; padding: 20px;"
        )
    )

@rt("/hallway-action")
def post(choice: str):
    if choice == "1":
        return bad_ending()
    elif choice == "3":
        return right_hallway_choice()
    # Add more hallway logic here
    return RedirectResponse("/")

@rt("/hiding-action")
def post(choice: str):
    if choice == "1":
        return closet_choice()
    elif choice == "4":
        return bad_ending()
    # Add more hiding logic here
    return RedirectResponse("/")

def closet_choice():
    return Titled("Patient 104",
        Div(
            P("There's little space, but you can just barely fit in. You hear things getting pushed around, as well as some angered comments. Eventually, the room grows quiet. What now?"),
            Form(
                Div(
                    Input(type="radio", name="choice", value="1", id="choice1"),
                    Label("Stay in place", _for="choice1"),
                    Br(),
                    Input(type="radio", name="choice", value="2", id="choice2"),
                    Label("Get out and look around", _for="choice2"),
                    Br(), Br(),
                    Button("Make Choice", type="submit")
                ),
                method="post", action="/closet-action"
            ),
            style="max-width: 600px; margin: 0 auto; padding: 20px;"
        )
    )

def right_hallway_choice():
    return Titled("Patient 104",
        Div(
            P("You continue walking, making it to the end of the hallway. In front of you is a pair of glass doors, and a slightly ajar wooden door to the left of it. Which way?"),
            Form(
                Div(
                    Input(type="radio", name="choice", value="1", id="choice1"),
                    Label("The exit. Home sweet home!", _for="choice1"),
                    Br(),
                    Input(type="radio", name="choice", value="2", id="choice2"),
                    Label("The wooden door. Maybe there's something cool in there", _for="choice2"),
                    Br(), Br(),
                    Button("Make Choice", type="submit")
                ),
                method="post", action="/exit-choice"
            ),
            style="max-width: 600px; margin: 0 auto; padding: 20px;"
        )
    )

@rt("/closet-action")
def post(choice: str):
    # Add closet action logic
    return RedirectResponse("/")

@rt("/exit-choice")
def post(choice: str):
    if choice == "1":
        return good_ending()
    elif choice == "2":
        return book_choice()
    return RedirectResponse("/")

def book_choice():
    return Titled("Patient 104",
        Div(
            P("You walk in the room, taking in the immediate sight of a huge book on a table. Carefully flipping through the pages, your eyes were only met with some of the most sickening things known to man: inhumane experiments, overly detailed notes...and terrible penmanship! A sudden noise comes from the hallway..."),
            Form(
                Div(
                    Input(type="radio", name="choice", value="1", id="choice1"),
                    Label("Leave the book and run", _for="choice1"),
                    Br(),
                    Input(type="radio", name="choice", value="2", id="choice2"),
                    Label("Take the book and run", _for="choice2"),
                    Br(),
                    Input(type="radio", name="choice", value="3", id="choice3"),
                    Label("Investigate the noise", _for="choice3"),
                    Br(), Br(),
                    Button("Make Choice", type="submit")
                ),
                method="post", action="/book-action"
            ),
            style="max-width: 600px; margin: 0 auto; padding: 20px;"
        )
    )

@rt("/book-action")
def post(choice: str):
    if choice == "1":
        return good_ending()
    elif choice == "2":
        return secrets_ending()
    elif choice == "3":
        return bad_ending()
    return RedirectResponse("/")

# Ending functions
def bad_ending():
    return ending_template(
        "Bad Ending",
        "You should've just minded your business, keep a low cover. Now, you're being dragged into a dark, cold room by two men dressed in all white lab coats, never to be seen again.",
        "You've got the bad ending. Would you like to play again to get a new ending?"
    )

def good_ending():
    return ending_template(
        "Good Ending", 
        "You managed to get out of the hospital with everything you came in with…give or take. Maybe next time avoid random places advertising free cream cheese bagels.",
        "You got the good ending. Would you like to play again to get a new ending?"
    )

def secrets_ending():
    return ending_template(
        "Secrets Ending",
        "You found a book of all sorts of twisted documents, detailing all the terrible things these people came up with in here. Who knows how many more they'll be going after! It's time to tell the world what you saw…",
        "You've got the secrets ending. Would you like to play again to get a new ending?"
    )

def traitor_ending():
    return ending_template(
        "Traitor Ending",
        "You're really willing to give up your morals just to save your own hide, huh? Not like you can change it, you're one of them now, meaning there's no way things will be the same again.",
        "You've got the traitor ending. Would you like to play again to get a new ending?"
    )

def delusion_ending():
    return ending_template(
        "Delusion Ending",
        "You wake up in bed, a person hovering over you while writing stuff down. At your side, your family is there, wanting to make sure that you're alright. Your head's pounding like crazy, so maybe that has something to do with it. Man, you've really gotta start reading labels before just eating stuff.",
        "You've got the delusion ending. Would you like to play again to get a new ending?"
    )

def ending_template(title, description, message):
    return Titled("Patient 104",
        Div(
            H2(title, style="color: #d32f2f;"),
            P(description, style="font-size: 18px; line-height: 1.6;"),
            P(message, style="font-weight: bold;"),
            Div(
                A("Play Again", href="/", style="background-color: #1976d2; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin: 10px;"),
                style="text-align: center; margin-top: 30px;"
            ),
            style="max-width: 600px; margin: 0 auto; padding: 20px; text-align: center;"
        )
    )

if __name__ == "__main__":
    serve(host="0.0.0.0", port=5000)