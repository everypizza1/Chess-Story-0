# The script of the game goes in this file.
#midleft pos
transform midleft:
    xalign 0.3
#Midright pos
transform midright:
    xalign 0.7
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Narrator")
define q = Character("Queen")
define k = Character("King")
define p = Character("Phone")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg castle

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    "It is a warm morning in the Bronze Kingdom."

    "The King is planning wars."

    "The queen is gaming."

    show Queen happy

    q "It looks nice outside."

    hide Queen happy

    show King happy at midleft

    k "I agree."

    show Phone ring at midright

    p "*ringing*"

    show King confused

    k "Huh?"

    hide King confused
    hide Phone ring

    show King busy
    k "Hello?"
    hide King busy
    show King concerened
    k "I did not authorise them."

    k "I will check it out."

    k "Goodbye."
    hide King concerened
    show King concerened at midleft
    show Queen concerened at midright
    q "What happened?"

    k "One of the pawns went rouge."

    q "Oh no!"

    q "Do we hnow where they are?"

    k "No."
    # This ends the game.

    return
