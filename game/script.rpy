
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
define gs1 = Character("Silver Guard")
define itl1 = Character("Investigation Team #1 Leader")

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene castle bedroom
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show Narrator static with dissolve
    # These display lines of dialogue.
    n "It is a warm morning in the Bronze Kingdom."
    n "The King is planning wars."
    n "The queen is gaming."
    hide Narrator static with dissolve
    show Queen happy with dissolve
    q "It looks nice outside."
    hide Queen happy with dissolve
    show King happy at midleft
    k "I agree."
    show Phone ring at midright
    p "*ringing*"
    show King confused
    k "Huh?"
    hide King confused with dissolve
    hide Phone ring with dissolve
    show King busy with dissolve
    k "Hello?"
    hide King busy with dissolve
    show King concerened with dissolve
    k "I did not authorise them."
    k "I will check it out."
    k "Goodbye."
    hide King concerened with dissolve
    show King concerened at midleft with dissolve
    show Queen concerened at midright with dissolve
    q "What happened?"
    k "One of the pawns went rouge."
    q "Oh no!"
    q "Do we hnow where they are?"
    k "No."
    q "Let's send a search team."
    hide Queen with dissolve
    hide King with dissolve
    show King at midleft with dissolve
    show Mic at midright with dissolve
    k "Activate code 17 section A subsection C. This is not a drill."
    hide Mic with dissolve
    hide King with dissolve
    show King with dissolve
    n "Alarms start."
    hide King with dissolve
    show King at midleft with dissolve
    show Pawn Leader at midright with dissolve
    pl "Where did the incident happen?"
    k "Silver Kingdom."
    pl "I will send the best teams out."
    k "Good luck."
    hide King with dissolve
    hide Pawn Leader with dissolve
    scene Outside
    label menu1:
    menu:
        "Where should we go?"
        "Left":
            pl "It's blocked!"
            jump menu1
        "Right":
            jump right1
    label right1:
    show Pawn Leader happy with dissolve
    pl "I see footsteps!"
    hide Pawn Leader with dissolve
    menu: 
        "What should we do?"
        "Ask guards":
            show Pawn Leader idea
            pl "Let's go ask the guards."
            scene Castle Entrance
            hide Pawn Leader with dissolve
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
            hide Guard Bronze with dissolve
            jump next1
        "Continue":
            show Pawn Leader idea with dissolve
            pl "Let's continue."
            hide Pawn Leader with dissolve
            jump next1
    label next1:
        scene blank
        show text "You go down the path" at truecenter
        with dissolve
        pause 5
        hide text
        with dissolve
        scene Silver Entrance
        show Pawn Leader
        n "Your group knoks on the door."
        n "The silver guards awnser."
        gs1 "Who is there?"
        pl "The Bronze pawn team #002"
        hide Pawn Leader
        show Pawn Leader at midleft
        show Silver Guard 1 at midright
        gs1 "You may enter."
        pl "Can you direct us to the crime scene?"
        gs1 "Sure."
        hide Pawn Leader
        hide Silver Guard 1
        scene blank
        show text "You go down the path." at truecenter
        with dissolve
        pause 5
        hide text
        with dissolve
        scene crime
        show Pawn Leader at midleft
        show Silver Guard 1 at midright
        gs1 "Here is the crime scene."
        pl "Were any injuries reported?"
        gs1 "No."
        pl "What do you think they were trying to do?"
        gs1 "It looks like they were trying to kill the king."
        pl "Oh no!"
        pl "I can confirm that we did not authorise this."
        gs1 "Alright."
        pl "You should put them in your prison while we send out an escort team to get them."
        gs1 "Okay."
        pl "Is that all?"
        gs1 "Yes."
        hide Pawn Leader
        hide Silver Guard 1
        scene blank
        show text "You go down the path." at truecenter
        with dissolve
        pause 5
        hide text
        with dissolve
        scene Bronze Entrance

        n "The pawns knock on the door."
        show Pawn Leader
        gb1 "Who is it?"
        pl "Pawn group #002."
        gb1 "You may enter."
        pl "Thanks."
        hide Pawn Leader
        show Pawn Leader at midleft
        show Bronze Guard 1 at midright
        pl "Were there any major developments in the case?"
        gb1 "Not that I have heard of yet."
        gb1 "You should ask the investigation team."
        pl "Alright."
        hide Pawn Leader
        hide Bronze Guard 1

        scene blank
        show text "You go down the path." at truecenter
        with dissolve
        pause 6
        hide text
        with dissolve
        scene Investigation Building Bronze
        
        show Investigation Team 1 Leader
        itl1 "Hello?"
        pl "Hello!"
        itl1 "Did you find anything out?"
        pl "No."
        pl "What about you?"
        itl1 "Not yet. We have some DNA from the crime scene, but that can't help."
        pl "Why?"
        itl1 "Because we have no DNA t compare it with."
        pl "Oh yeah, I forgot."
    # This ends the game.

    return
