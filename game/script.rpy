# The script of the game goes in this file.
#midleft pos
transform midleft:
    xalign 0.3
#Midright pos
transform midright:
    xalign 0.7
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")
define q = Character("Queen")
define k = Character("King")
define p = Character("Phone")
define m = Character("Microphone")
define pl = Character("Pawn Leader")
define gb1 = Character("Bronze Guard")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene castle bedroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Narrator static
    # These display lines of dialogue.

    n "It is a warm morning in the Bronze Kingdom."

    n "The King is planning wars."

    n "The queen is gaming."
    hide Narrator static
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

    q "Let's send a search team."

    hide Queen
    hide King
    show King at midleft
    show Mic at midright

    k "Activate code 17 section A subsection C. This is not a drill."
    hide Mic
    hide King

    show King
    n "Alarms start."
    hide King
    show King at midleft
    show Pawn Leader at midright

    pl "Where did the incident happen?"
    
    k "Silver Kingdom."

    pl "I will send the best teams out."

    k "Good luck."

    hide King
    hide Pawn Leader
    scene Outside

    menu:
        "Where should we go?"
        "Left":
            pl "It's blocked!"
            jump right1
        "Right":
            jump right1
    
    label right1
    show Pawn Leader happy
    pl "I see footsteps!"
    hide Pawn Leader
    menu: 
        "What should we do?"
        "Ask guards":
            show Pawn Leader idea
            pl "Let's go ask the guards."
            scene Castle Entrance
            hide Pawn Leader
            show Guard Bronze 1
            pl "When did theese footsteps appear?"
            gb1 "Last night."
            pl "Did you hear anything?"
            gb1 "No, but I saw a pawn silloete."
            pl "How many?"
            gb1 "2."
            pl "Alright."
            pl "Did they come back?"
            gb1 "No."
            pl "Thanks."
            hide Guard Bronze
            jump next1
        "Continue":
            show Pawn Leader idea
            pl "Let's continue."
            hide Pawn Leader
            jump next1
    label next1
    # This ends the game.

    return
