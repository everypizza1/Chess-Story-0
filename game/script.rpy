# Functions
#midleft pos
# e.x. show character at pos
transform midleft:
    xalign 0.3
#Midright pos
transform midright:
    xalign 0.7
transform topright:
    xalign 0.7
    yalign 0.7
# Declare characters used by this game. The color argument colorizes the
# name of the character.
# shows title of character
define n = Character("Narrator")
define q = Character("Queen")
define k = Character("King")
define p = Character("Phone")
define m = Character("Microphone")
define pl = Character("Bronze Pawn Leader")
define gb1 = Character("Bronze Guard")
define gs1 = Character("Silver Guard")
define itl1 = Character("Investigation Team #1 Leader")
# Actual code

label start:
    scene blank
        show text "Act I" at truecenter
        with dissolve
        pause 5
        hide text
        with dissolve
    # Show a background. Here it is /images/castle bedroom.png
    #FIX BEFORE RELEASE
    scene castle bedroom
    # This shows a character sprite. here it will show /images/Narrator static.png
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
    hide King confuse
    hide Phone rin
    show King bus
    k "Hello?"
    hide King bus
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
    label menu1:
    menu:
        "Where should we go?"
        "Left":
            pl "It's blocked!"
            jump menu1
        "Right":
            jump right1
    label right1:
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
            hide Guard Bron
            jump next1
        "Continue":
            show Pawn Leader idea
            pl "Let's continue."
            hide Pawn Leader
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
        show Investigation Team 1 Leader at midleft
        show Pawn Leader at midright
        itl1 "Hello?"
        pl "Hello!"
        itl1 "Did you find anything out?"
        pl "No."
        pl "What about you?"
        itl1 "Not yet. We have some DNA from the crime scene, but that can't help."
        pl "Why?"
        itl1 "Because we have no DNA to compare it with."
        pl "Oh yeah, I forgot."
        pl "The disadvantage of not spying on our citizens."
        itl1 "Hear me out..."
        hide Pawn Leader
        show Pawn Leader annoyed at midright
        pl "No, I'm not hearing you out!"
        pl "How many times do I need to tell you this?"
        itl1 "Tell me what?"
        pl "WE AREN'T SPING ON OUR CITZENS?"
        itl1 "But why?"
        pl "Because we're just better than the other countries!"
        itl1 "Alright, fine."
        itl1 "We won't spy on them."
        hide Pawn Leader
        hide Investigation Team 1 Leader
        scene blank
        show text "The next morining..." at truecenter
        with dissolve
        pause 6
        hide text
        with dissolve
        scene silver horizon 1
        show text "Silver Kingdom" at topright
        with dissolve
        pause 5
        hide text
        with dissolve
        show Pawn Leader Silver

    # This ends the game.
    return