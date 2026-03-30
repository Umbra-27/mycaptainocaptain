# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define captain = Character("Captain", image="captain@3.5/captain", kind=bubble)
define engineer = Character("Eugen", image="engineer/engineer", kind=bubble)
define medic = Character("Sara", image="medic/medic", kind=bubble)
define computer = Character("MAD1", image="computer/computer", kind=bubble)
define mattputer = Character ("MAD1?", image="computer/computer", kind=bubble)
define matthew = Character ("Matthew", image="computer/computer", kind=bubble)

# persistent data variables for endings
default persistent.secret_unlocked = False # if at least one ending has been unlocked
default persistent.matthew_unlocked = False # seen Matt log in MO

default persistent.seenC1 = False # for gallery
default persistent.seenC2 = False # for gallery

default persistent.endB_unlocked = False # bad ending achieved
default persistent.endC_unlocked = False # Captain ending achieved
default persistent.endE_unlocked = False # Eugen ending achieved
default persistent.endS_unlocked = False # Sara ending achieved
default persistent.endG_unlocked = False # good ending achieved

default persistent.endSEC_unlocked = False # secret ending achieved

# Sound Settings
default preferences.volume.music = 0.3
default preferences.volume.sfx = 0.5

# Setting base approval scores
init python:
    medApproval = 0
    engApproval = 0
    
    config.window_hide_transition = None
    config.window_show_transition = None
    config.empty_window = nvl_show_core

    seenSI = False
    seenEI = False
    seenS1 = False
    seenE1 = False
    seenS2 = False
    seenE2 = False
    seenS3 = False
    seenE3 = False
    seenMO = False
    seenMattLog = False
    seenSaraSolution = False
    seenEugenSolution = False

    secretChoice = False # Choose to chuck the specimen in C2 to unlock S/E 3.1.c choice

# dark ver
image bgCompDark = im.MatrixColor(
    "bg computer.png",
    im.matrix.brightness(-0.2))

image captainNeutralClosedDark = im.MatrixColor(
    "captain@3.5/captain neutral-closed.png",
    im.matrix.brightness(-0.2))

image captainNeutralOpenDark = im.MatrixColor(
    "captain@3.5/captain neutral-open.png", 
    im.matrix.brightness(-0.2),
    yalign=0.25)

image captainConfusedOpenDark = im.MatrixColor(
    "captain@3.5/captain confusion-open.png", 
    im.matrix.brightness(-0.2))

image captainConfusedClosedDark = im.MatrixColor(
    "captain@3.5/captain confusion-closed.png", 
    im.matrix.brightness(-0.2))


# The game starts here.
label start:    
    play music "Electric_Dawn.mp3" volume 0.8

    scene bg computer with fade

    show computer neutral-1 with dissolve
    show captain neutral-open behind computer with dissolve
    
    play sound "captainslog_background.mp3"

    voice "audio/voice/captain/C1-001.mp3"
    captain "Captain’s Log — September 24th." 

    voice "audio/voice/captain/C1-002.mp3"
    captain "Eugen Braun’s drill apparatus was successful in piercing through the ice 
                layer of one of Jupiter’s moons, Europa."
    voice "audio/voice/captain/C1-003.mp3"
    captain "From its ocean, we’ve retrieved a specimen that resembles life."
    voice "audio/voice/captain/C1-004.mp3"
    captain "Short on time, we’ve started the course back 
                to Earth."
    voice "audio/voice/captain/C1-005.mp3"
    captain "Dr. Sara Fernando’s begun studying the specimen. I’ve ordered 
                her to confirm the form of life." 
    voice "audio/voice/captain/C1-006.mp3"    
    captain "Technician Braun’s been commanded to conduct maintenance on 
                the equipment in the bio-lab." 

    play sound "m4d1_notification.mp3"
    show computer neutral-2
    show captain neutral-closed behind computer

    voice "audio/voice/madi/M1-001.mp3"
    computer "Message from Cosmotechnician Eugen Braun. Open message?"

    menu:
        "Open message":
            play sound "audio/Button_Select.mp3" volume 0.8
            show captain neutral-open behind computer
            voice "audio/voice/captain/C1-007.mp3"
            captain "Open and read."

    play sound "m4d1_message_open.mp3" 
    show computer neutral-3
    show captain neutral-closed behind computer

    voice "audio/voice/madi/M1-002-1.mp3"
    computer "Engineer: Captain, I have been reviewing the bio lab’s system; the data does not align with standard 
                operating parameters." 
    voice "audio/voice/madi/M1-002-2.mp3"
    computer "Engineer: This does not appear to be a malfunction or human error; there seems to be an 
                interference with the processes."
    voice "audio/voice/madi/M1-002-3.mp3"
    computer "It will be best to address this immediately."

    show captain frustrated behind computer
    voice "audio/voice/captain/C1-008.mp3"
    captain "..."
    voice "audio/voice/captain/C1-009.mp3"
    captain "MAD1, run ship diagnostics."

    show computer processing-1
    voice "audio/voice/madi/M1-003.mp3"
    computer "Initiating system diagnostics. Analyzing running operations."

    play sound "system_diagnostic_start.mp3"
    show computer processing-2

    show captain rememberance-closed behind computer

    show computer processing-3
    voice "audio/voice/captain/C1-010.mp3"
    captain "This is probably my fault… I made us take an extra day travelling to find his ship. I’m rushing us home to return on time."

    play sound "electric_oh_no.mp3"
    show computer error-1
    voice "audio/voice/madi/M1-004.mp3"
    computer "Error. Process failure.{w=0.5}" 
    show computer processing-1
    voice sustain
    voice "audio/voice/madi/M1-005.mp3"
    computer " Reinitiating process.{w=0.5}" 
    show computer processing-2
    show computer processing-3
    show computer error-1
    voice sustain
    voice "audio/voice/madi/M1-006.mp3"
    computer " Error. System failure.{w=0.5}"
    
    scene bg computer error
    show computer error-1
    show captain confusion-closed behind computer
    
    stop music fadeout 1.0
    play sound "error_sound_1.mp3"
    voice sustain
    voice "audio/voice/madi/M1-007.mp3"
    computer " Error. Error. E̷̠̓r̷̖͆r̵̼͋o̷̳̔r{w=0.5}{nw}"

    show captain confusion-open with hpunch 
    voice "audio/voice/captain/C1-011.mp3"
    captain "What’s happening? MAD1, show me the error logs."

    scene bg computer error bad
    show computer error-1
    show captain confusion-closed behind computer

    voice "audio/voice/madi/M1-008.mp3"
    computer "Error. Unable to end process." 
    play sound "error_sound_2.mp3"
    voice sustain
    voice "audio/voice/madi/M1-009.mp3"
    computer "Pulling error log̶̕s.{w=0.5}{nw}"
    voice sustain
    voice "audio/voice/madi/M1-010.mp3"
    computer "Ê̴̋͒͠r̵̛̈̏r̸̳̯͎͍̬̊̇̀o̵r̷͘. {w=0.2}{nw}" 
    voice sustain
    voice "audio/voice/madi/M1-011.mp3"
    computer "Sys̷̖̏ṭ̷̋e̵̗̬͋m̵̩͋̕ṡ̴̨͎ dò̷̧͎͍͇̫͆̕ẃ̵̛̔n̶-{w=0.2}{nw}"

    stop sound
    play sound "systems_off.mp3"
    scene bgCompDark
    show computer error-2
    show captainConfusedClosedDark behind computer
    pause(1)

    "The lights go out. Everything stops." 
    "The buzz and rumbles of the ship go deadly silent, and it’s as if time and space have frozen solid." 
    "Only one terminal blinks online."

    voice "audio/voice/madi/M1-012.mp3"
    computer "But O heart! heart! H̷̢̚e̷a̵ŕ̶̤t̵͈́!̵̺̾"
    voice "audio/voice/madi/M1-013.mp3"
    computer "O the b̵̝̀l̷̨͠e̶̹̕ȩ̵̔d̴̲̅i̶n̵̕ġ̷͍ drops of red,"
    voice "audio/voice/madi/M1-014.mp3"
    computer "Where on the deck my Captain lies,"
    voice "audio/voice/madi/M1-015.mp3"
    computer "Fallen cold and d̸̻̈́e̵͉̋a̸̪̿d̸̙͆."

    "The terminal displays strange text. I’ve never seen MAD1 act this way before."

    show captainConfusedOpenDark behind computer
    voice "audio/voice/captain/C1-012.mp3"
    captain "What the hell?" 
    
    show captainConfusedClosedDark behind computer   
    play sound "captain_smack_1.mp3" 
    captain "*Smacks terminal*" with hpunch 

    scene bg computer
    play sound "systems_back_online.mp3" volume 0.8
    play music "Ice_Cold.mp3"

    show computer reboot-1
    show captain confusion-closed behind computer   

    "Then the lights come on again. Thankfully."
    show computer reboot-2
    pause(0.5)
    show computer reboot-3
    pause(0.5)
    show computer reboot-4
    pause(0.5)
    show computer reboot-5
    "Sound returns as I presume the system reboots."

    voice "audio/voice/madi/M1-016.mp3"
    computer "System force restart. Diagnostics complete." 
    show computer neutral-1
    voice "audio/voice/madi/M1-017.mp3"
    computer "Power systems offline. Emergency power engaged." 
    voice "audio/voice/madi/M1-018.mp3"
    computer "Navigation systems paused." 
    voice "audio/voice/madi/M1-019.mp3"
    computer "Internal communications offline." 
    show computer neutral-2
    voice "audio/voice/madi/M1-020.mp3"
    computer "Satellite communication offline." 
    voice "audio/voice/madi/M1-021.mp3"
    computer "Data systems offline." 
    voice "audio/voice/madi/M1-022.mp3"
    computer "Thermal control offline." 
    show computer neutral-3
    voice "audio/voice/madi/M1-023.mp3"
    computer "Oxygen system offline." 
    voice "audio/voice/madi/M1-024.mp3"
    computer "Emergency Life support protocol engaged."
    voice "audio/voice/madi/M1-025.mp3"
    computer "2 of 3 escape pods malfunctioning."

    show captain anger-open behind computer 

    voice "audio/voice/captain/C1-013.mp3"
    captain "MAD1, what the hell is going on?"

    show captain anger-closed behind computer 

    voice "audio/voice/madi/M1-026.mp3"
    computer "Mission status paused. To preserve power and life support, non-essential rooms have been sealed. Oxygen will be rerouted."

    play sound "captain_smack_2.mp3" 

    captain "*Slams fist on table*" with hpunch 
    show captain anger-open behind computer
    voice "audio/voice/captain/C1-014.mp3"
    captain "Right now? But we're so close..."
    
    show captain anger-closed behind computer 

    voice "audio/voice/madi/M1-027.mp3"
    computer "Captain, I recommend checking on the crew to maintain morale and investigate the cause of the system failure."

    show captain frustrated behind computer 
    captain "..." 
    show captain neutral-open behind computer 
    voice "audio/voice/captain/C1-015.mp3"
    captain "I suppose you’re right. Give me periodic reports on the oxygen levels."
    show captain neutral-closed behind computer 
    voice "audio/voice/captain/C1-016.mp3"
    captain "And get me a physical copy of the latest readings on the specimen."

    voice "audio/voice/madi/M1-028.mp3"
    computer "Aye, aye, Captain. Printing report. Oxygen levels at 99%%."

    show captain frustrated behind computer 
    captain "..." 
    voice "audio/voice/captain/C1-017.mp3"
    captain "Thanks..."
    show captain neutral-open behind computer 
    voice "audio/voice/captain/C1-018.mp3"
    captain "Let’s check on the crew."
    show captain thinking behind computer 

    jump map0

    label map0:
        show screen MapUI0 with fade
        pause
        
    label SI:
        hide screen MapUI0 with dissolve
        show captain neutral-open behind computer 
        voice "audio/voice/captain/C1-019.mp3"
        captain "I should speak to Sara. She’s probably freaking out right now."

        play sound "Footsteps.mp3" volume 0.8
        play music "Microbiology.mp3" volume 0.8
        scene onlayer screens
        $ seenSI = True
        scene bg medic with fade
        show medic nervous with dissolve 
        pause(0.5)
        show captain neutral-closed behind medic with dissolve

        show medic stressed
        voice "audio/voice/sara/S1-001"
        medic "Captain! W-what just happened! Thank goodness you arrived when you did. The alarms went off and I was getting worried!" 
        
        show captain neutral-open behind medic
        voice "audio/voice/captain/C1-021.mp3"
        captain "Yes, quite unexpected. I‘m checking in personally since comms are down."
        voice "audio/voice/captain/C1-022.mp3"
        captain "I'm sorting it out with Eugen."
        voice "audio/voice/captain/C1-023.mp3"
        captain "We’ve had good luck so far—we’ve achieved something no man has managed before. These things happen."

        show medic neutral
        show captain neutral-closed behind medic
        voice "audio/voice/sara/S1-002"
        medic "Yes, yes, of course!" 

        show medic explaining
        show captain neutral-closed behind medic
        voice "audio/voice/sara/S1-003"
        medic "I mean, this cargo—this discovery—would revolutionize everything." 
        voice "audio/voice/sara/S1-004"
        medic "Our very understanding of the universe. Extraterrestrial life! Aboard this ship." 
        show medic excited
        show captain neutral-closed behind medic
        voice "audio/voice/sara/S1-005"
        medic "I still can’t believe it." 
        show medic neutral
        show captain neutral-closed behind medic
        voice "audio/voice/sara/S1-006"
        medic "But this… development is most concerning." 

        show medic nervous
        show captain neutral-closed behind medic
        voice "audio/voice/sara/S1-007"
        medic "What could possibly be happening, Captain?" 
        show medic stressed
        voice "audio/voice/sara/S1-008"
        medic "Could this result in some kind of irreparable, cascading failure?"

        show captain neutral-open behind medic
        voice "audio/voice/captain/C1-024.mp3"
        captain "Like I said before, Sara, we’ll find out soon. There is no reason to assume the worst." 

        show captain neutral-closed behind medic
        show medic thinking
        voice "audio/voice/sara/S1-009"
        medic "I understand. Just given what has happened before…"

        show captain anger-open behind medic
        voice "audio/voice/captain/C1-025.mp3"
        captain "What happened to the previous mission has nothing to do with what is happening now."

        # SI.1
        show medic stressed
        show captain anger-closed behind medic
        voice "audio/voice/sara/S1-010"
        medic "I’m sorry. I-I guess I’ve always felt you were easier to talk to on this ship. You know, compared to Eugen." 
        voice "audio/voice/sara/S1-011"
        medic "I admit this incident isn’t making me think straight. I shouldn’t have brought it up." 
        show medic suggesting
        voice "audio/voice/sara/S1-012"
        medic "I understand it must be painful for you—"

        menu:
            # SI.1.a
            "We’re all stressed.":
                $ medApproval += 1
                play sound "correct ding.mp3" volume 0.8

                show captain concern-open behind medic
                voice "audio/voice/captain/C1-026.mp3"
                captain "It’s okay, Sara. This is stressful for all of us."

                show medic anxious
                show captain concern-closed behind medic
                voice "audio/voice/sara/S1-013"
                medic "This is true. Still, I apologize for bringing it up."

            # SI.1.b
            "Don't do it again.":
                play sound "incorrect ding.mp3" volume 0.8
                show captain anger-open behind medic
                voice "audio/voice/captain/C1-027.mp3"
                captain "It’s fine. Just don’t do it again."

                show medic stressed
                show captain anger-closed behind medic
                voice "audio/voice/sara/S1-014"
                medic "I’m sorry, Captain. I’ll just, um…"

        show captain neutral-open behind medic
        voice "audio/voice/captain/C1-028.mp3"
        captain "How about you go through your notes so far?"
        voice "audio/voice/captain/C1-029.mp3"
        captain "We could use any theories on what this specimen is and its properties."

        show medic excited
        show captain neutral-closed behind medic
        voice "audio/voice/sara/S1-015"
        medic "Yes, yes… I do have working hypotheses, though nothing exactly seems to work out perfectly at the moment. "
        
        show medic nervous
        show captain neutral-closed behind medic
        voice "audio/voice/sara/S1-016"
        medic "I should be working harder…"

        show captain concern-open behind medic
        voice "audio/voice/captain/C1-030.mp3"
        captain "Sara, you’re already working very hard."
        voice "audio/voice/captain/C1-031.mp3"
        captain "You’re the best in the field. Remember; it’s why we have you on this mission."

        show medic neutral
        show captain concern-closed behind medic
        voice "audio/voice/sara/S1-017"
        medic "Thank you, Captain. I can’t overstate how much this mission means to me."
        show medic excited
        show captain concern-closed behind medic
        voice "audio/voice/sara/S1-018"
        medic "This—this specimen we’ve found is the holy grail of astrobiology."

        show captain neutral-open behind medic 
        voice "audio/voice/captain/C1-032.mp3"
        captain "And that’s exactly why you must continue your work."
        show medic thinking
        voice "audio/voice/captain/C1-033.mp3"
        captain "I’m counting on you Sara. Here, I’ve brought you the most recent readings on the specimen."
        voice "audio/voice/captain/C1-034.mp3"    
        captain "We’ll get the system back up one way or another."

        # SI.2
        show medic stressed
        show captain neutral-closed behind medic
        voice "audio/voice/sara/S1-019"
        medic "Thank you for the report Captain, but the rest of my research and reference materials are in the system." 
        show medic nervous
        voice "audio/voice/sara/S1-020"
        medic "How long will it take?" 
        voice "audio/voice/sara/S1-021"
        medic "How am I supposed to keep working if it takes too long?"
        
        show medic nervous
        show captain neutral-closed behind medic

        menu:
            # SI.2.a
            "Figure it out.":                
                play sound "incorrect ding.mp3" volume 0.8
                show captain anger-open behind medic
                voice "audio/voice/captain/C1-035.mp3"
                captain "Figure it out. That’s an order."

                show medic anxious
                show captain anger-closed behind medic
                voice "audio/voice/sara/S1-022"
                medic "O-of course Captain."

            # SI.2.b
            "I have faith in you." :
                $ medApproval += 1
                play sound "correct ding.mp3" volume 0.8
                
                show captain neutral-open behind medic
                voice "audio/voice/captain/C1-036.mp3"
                captain "I can’t say for sure, but I’ve seen you work with less before."
                voice "audio/voice/captain/C1-037-1.mp3"
                captain "I expect you’d gain more insight once you study your notes. I have faith in you."

                show medic neutral
                show captain neutral-closed behind medic
                voice "audio/voice/sara/S1-023"
                medic "I won’t let you down Captain."
        
        show captain neutral-open behind medic
        voice "audio/voice/captain/C1-037-2.mp3"
        captain "Try not to move around too much. Oxygen’s at a premium right now."
        
        voice "audio/voice/captain/C1-037-3.mp3"
        captain "I’ll be back to check in later."

        if seenEI is False:
            show screen MapUI0 with fade
            pause

        else:
            jump M1


    label EI:
        hide screen MapUI0 with dissolve
        show captain neutral-open behind computer 
        voice "audio/voice/captain/C1-020.mp3"
        captain "I should speak to Eugen. He’ll probably know what’s happening."

        play sound "Footsteps.mp3" volume 0.8
        play music "Spark_Of_Awareness.mp3" volume 0.8
        scene onlayer screens
        $ seenEI = True
        scene bg engineer with fade
        show engineer neutral with dissolve
        pause(0.5)
        show captain neutral-closed behind engineer with dissolve

        show captain neutral-open behind engineer
        voice "audio/voice/captain/C1-038.mp3"
        captain "How’re you holding up Eugen?"

        show captain neutral-closed behind engineer
        show engineer thinking
        voice "audio/voice/eugen/E1-004.mp3"
        engineer "As well as one can, given the circumstances." 
        voice "audio/voice/eugen/E1-005.mp3"
        engineer "May we skip the pleasantries? I dislike small talk." 
        show engineer neutral
        voice "audio/voice/eugen/E1-006.mp3"
        engineer "I’m sure Sara would appreciate it more."

        show captain neutral-open behind engineer
        voice "audio/voice/captain/C1-039.mp3"
        captain "Got it... Straight to the point then. Report."

        show engineer thinking
        show captain neutral-closed behind engineer
        voice "audio/voice/eugen/E1-007.mp3"
        engineer "Captain, the situation is not ideal. There appears to be a system failure on a magnitude I’ve never seen."
        voice "audio/voice/eugen/E1-008.mp3"
        engineer "I am looking into it, however, little progress is being made."
        voice "audio/voice/eugen/E1-009.mp3"
        engineer "At the rate we’re losing oxygen, I estimate that we have approximately one hour."
        
        show engineer neutral
        show captain concern-open behind engineer
        voice "audio/voice/captain/C1-040.mp3"
        captain "Damn… Well there goes my hope for any good news."

        # EI.1
        show engineer thinking
        show captain concern-closed behind engineer
        voice "audio/voice/eugen/E1-010.mp3"
        engineer "Is there any information you can provide? Do you know what might have caused this?"

        menu:
            # EI.1a
            "I’m not sure yet.":
                play sound "incorrect ding.mp3" volume 0.8
                show captain thinking behind engineer
                voice "audio/voice/captain/C1-041.mp3"
                captain "I’m not sure yet. I want to find out a bit more before I give any concrete answers."

                show engineer frustration
                show captain thinking behind engineer
                voice "audio/voice/eugen/E1-011.mp3"
                engineer "I urge you to produce any information as soon as possible. When you have something, please let me know."

            # EI.1b
            "Share what you know.":
                $ engApproval += 1
                play sound "correct ding.mp3" volume 0.8

                show captain thinking behind engineer
                voice "audio/voice/captain/C1-042.mp3"
                captain "The computer began to glitch after beginning a diagnostic."
                voice "audio/voice/captain/C1-043.mp3"
                captain "It started reciting Walt Whitman before the entire system crashed."

                show engineer resolve
                show captain thinking behind engineer
                voice "audio/voice/eugen/E1-012.mp3"
                engineer "Can’t say I’ve ever heard of something like this; but, everything has a fix."
                voice "audio/voice/eugen/E1-013.mp3"
                engineer "I’ll begin looking into this immediately."
        
        show engineer neutral
        show captain neutral-closed behind engineer    

        voice "audio/voice/eugen/E1-014.mp3"
        engineer "In the meantime, I’ve reviewed the oxygen depletion curve 3 times now."
        voice "audio/voice/eugen/E1-015.mp3"
        engineer "This is not a random failure. Something is interfering with the system's command execution."

        show captain confusion-open behind engineer   
        voice "audio/voice/captain/C1-044.mp3"
        captain "What could possibly be interfering? Everything on this mission has been smooth thus far." 
        voice "audio/voice/captain/C1-045.mp3"
        captain "And why the whole system? A function or two, sure those might glitch and need maintenance." 
        voice "audio/voice/captain/C1-046.mp3"
        captain "But what the hell happened to MAD1?"

        # EI.2
        show engineer resolve
        show captain neutral-closed behind engineer

        voice "audio/voice/eugen/E1-016.mp3"
        engineer "We must stay focused, Captain. If we’re to correct this, we must proceed methodically."

        menu: 
            # EI.2a
            "Stand by.":
                play sound "incorrect ding.mp3" volume 0.8

                show captain anger-open behind engineer
                voice "audio/voice/captain/C1-047.mp3"
                captain "I am proceeding methodically... I need more information first."
                voice "audio/voice/captain/C1-048.mp3"
                captain "Stand by for now."

                show engineer anger
                show captain anger-closed behind engineer
                voice "audio/voice/eugen/E1-017.mp3"
                engineer "As you wish, however, I urge you to think about this decision further."
            
            # EI.2b
            "Make haste.":
                $ engApproval += 1
                play sound "correct ding.mp3" volume 0.8

                show captain determined-open behind engineer
                voice "audio/voice/captain/C1-049.mp3"
                captain "Make haste but proceed with caution." 
                voice "audio/voice/captain/C1-050.mp3"
                captain "We don’t fully know yet what’s happening, but I trust you to make progress."

                show engineer thinking
                show captain determined-closed behind engineer
                voice "audio/voice/eugen/E1-018.mp3"
                engineer "Of course, the sooner we address this, the sooner the root of the problem will present itself."

        show captain neutral-open behind engineer
        voice "audio/voice/captain/C1-051.mp3"
        captain "Work from your desk the best you can. I don't want us using more oxygen than we need to."
        voice "audio/voice/captain/C1-052.mp3"
        captain "I’ll be back when I have more to update."

        if seenSI is False:
            show screen MapUI0 with fade
            pause

        else:
            jump M1

    label M1:
        play sound "Footsteps.mp3" volume 0.8
        play music "Electric_Dawn.mp3" volume 0.8
        scene bg computer with fade
        show computer neutral-1 with dissolve
        show captain neutral-closed behind computer with dissolve

        voice "audio/voice/madi/M1-029.mp3"
        computer "Welcome back, Captain. Oxygen at 80%%."

        show captain neutral-open behind computer
        voice "audio/voice/captain/C1-053.mp3"
        captain "The Astrobiologist and Cosmotechnician both are on track now to find out what’s wrong with the ship."
        show captain concern-open behind computer
        voice "audio/voice/captain/C1-054.mp3"
        captain "And I guess you… Please don’t break on me again…"
        voice "audio/voice/captain/C1-055.mp3"
        captain "How’s the ship doing MAD1?"

        show computer processing-1
        show captain concern-closed behind computer
        voice "audio/voice/madi/M1-030.mp3"
        computer "Assessing ship systems…"
        show computer processing-2
        show captain concern-closed behind computer
        voice "audio/voice/madi/M1-031.mp3"
        computer "Processi̶̒͜n̵͖̕ġ̷͍ġ̷͍ġ̷͍-"

        scene bg computer error
        show computer error-1
        show captain confusion-closed behind computer with hpunch 
        voice "audio/voice/madi/M1-032.mp3"
        computer "Water, wả̵̳t̷̨̍e̴͚̔r̵̥̉, every where,"
        voice "audio/voice/madi/M1-033.mp3"
        computer "And all the boards did shrink;"
        voice "audio/voice/madi/M1-034.mp3"
        computer "Water, ẉ̸̢̟͑ͅą̷̓͝tĕ̵͈̗̆͒̚r̷̢̼͈͚̈́̐, eve̴̤̚r̷̈́y̴͉̌ ̵̦̈́ẁ̸̺h̵̻̿e̸͉̋ŗ̵̈́e̸̛̝,"
        voice "audio/voice/madi/M1-035.mp3"
        computer "Nor a̴̞̓ǹ̷̢y̷̾ͅ ̵̡̐d̸̟̄ȓ̶̼o̷̻͒p̴̛̦ ̵̦̈́t̵̨͝ó̴̝ ̸̜͋d̸̝̑rī̶̻n̵̺̍ḱ̴͍."
        
        show captain anger-open behind computer with hpunch 
        voice "audio/voice/captain/C1-056.mp3"
        captain "More poems? MAD1 I can’t lose you right now!"

        scene bg computer
        show computer reboot-1
        show captain anger-closed behind computer
        voice "audio/voice/madi/M1-036.mp3"
        computer "Rebooting.{w=0.3}{nw}"
        show computer reboot-2
        computer "Rebooting.{w=0.3}{nw}"
        show computer reboot-3
        computer "Rebooting.{w=0.3}{nw}"
        show computer reboot-4
        computer "Rebooting.{w=0.3}{nw}"
        show computer reboot-5
        computer "Rebooting."
        show captain confusion-closed behind computer
        show computer neutral-1
        voice "audio/voice/madi/M1-037.mp3"
        computer "System functionality at 69%%." 
        show computer neutral-2
        voice "audio/voice/madi/M1-038.mp3"
        computer "Apologies, Captain. It seems my software is continuing to deteriorate." 
        voice "audio/voice/madi/M1-039.mp3"
        computer "Something is interfering with the ship systems and my code. I am unable to identify wha̸͇̋t̶̜̕" 
        voice "audio/voice/madi/M1-040.mp3"
        computer "Captain, I’m afraid my ability to assist you will be limited soon."

        show captain frustrated behind computer
        voice "audio/voice/captain/C1-057.mp3"
        captain "Dammit! I can’t afford to have more things break down now."
        show captain concern-closed behind computer
        voice "audio/voice/captain/C1-058.mp3"
        captain "What am I supposed to do?"

        show computer neutral-3
        show captain concern-closed behind computer
        voice "audio/voice/madi/M1-041.mp3"
        computer "I suggest checking with the crew, Captain. 
            Perhaps they will have answers soon with your ss-ssupp̷̞̏-pǫ̸̊ȑ̸̨t̷͎̎t̷͎̎-t̷̠̆t̵̞̓t̴̘͑-"

        show computer error-1 with hpunch
        play sound "Metallic_Hit.mp3" volume 0.8
        show captain anger-closed behind computer with hpunch 

        voice "audio/voice/madi/M1-042.mp3"
        computer "The one by toi̷l̵, the other to comp̸̖̓l̴͎̀a̴̺͗ì̴̩n"
        voice "audio/voice/madi/M1-043.mp3"
        computer "How far I t̴̡̃o̴̳͒i̶̥͋l̶̮̍, still farther ó̷̖ff f̵̲͒ȑ̷͉o̵̮̓m̴̮̌ ̶͓̈́t̷͎̑h̶̏e̶e̶̻̔."

        show computer error-2
        show captain rememberance-open behind computer
        voice "audio/voice/captain/C1-059.mp3"
        captain "... How far I toil, indeed."
        voice "audio/voice/captain/C1-060.mp3"
        captain "I hope one of them has found something."
        show captain concern-open behind computer
        voice "audio/voice/captain/C1-061.mp3"
        captain "Hang in there MAD1."

        show captain thinking behind computer
        $ seenS1 = False
        $ seenE1 = False
        
        jump Map1

    label Map1:
        show screen MapUI1 with fade        
        pause

    label S1:
        play sound "Footsteps.mp3" volume 0.8
        play music "Microbiology.mp3" volume 0.8
        scene onlayer screens
        $ seenS1 = True
        $ seenE1 = False
        scene bg medic with fade
        show medic nervous with dissolve 
        pause(0.5)
        show captain neutral-closed behind medic with dissolve

        show medic explaining
        voice "audio/voice/sara/S2-001.mp3"
        medic "Captain, any update on what’s going on? What did Eugen say?"

        # S.1.1
        show captain neutral-open behind medic
        voice "audio/voice/captain/C2-001.mp3"
        captain "We’re looking into it."

        menu: 
            # S.1.1a
            "To be honest, the situation is dire.":
                play sound "incorrect ding.mp3" volume 0.8

                show captain concern-open behind medic
                voice "audio/voice/captain/C2-002.mp3"
                captain "I have to be honest with you, Sara." 
                voice "audio/voice/captain/C2-003.mp3"
                captain "The situation is more dire than we thought. But I need you to remain calm."
                show captain concern-closed behind medic
                show medic nervous
                voice "audio/voice/sara/S2-002.mp3"
                medic "Oh my god… T-thank you for your honesty, Captain."

            # S.1.1b
            "We'll sort it out soon.":
                $ medApproval += 1
                play sound "correct ding.mp3" volume 0.8

                show captain neutral-open behind medic
                voice "audio/voice/captain/C2-004.mp3"
                captain "I have hopes that we’ll sort it out soon." 
                voice "audio/voice/captain/C2-005.mp3"
                captain "Thanks for fulfilling my request."
                show captain neutral-closed behind medic
                show medic suggesting
                voice "audio/voice/sara/S2-003.mp3"
                medic "Okay, that’s good to hear! Yes, of course."

        show medic thinking
        show captain neutral-closed behind medic
        voice "audio/voice/sara/S2-004.mp3"
        medic "Um, I’ve gone through my notes as requested, w-would you like to hear what my theory is?"

        show captain neutral-open behind medic
        voice "audio/voice/captain/C2-006.mp3"
        captain "Enlighten me."

        show medic explaining
        show captain neutral-closed behind medic
        voice "audio/voice/sara/S2-005.mp3"
        medic "This specimen is not a lifeform as we know it. Life is, after all, undefined."
        voice "audio/voice/sara/S2-006.mp3"
        medic "It’s uniquely adapted to the cold and dark of Europa’s ocean. "
        show medic excited
        show captain neutral-closed behind medic
        voice "audio/voice/sara/S2-007.mp3"
        medic "I’ve been thinking of life in Earth’s oceans, and the closest equivalent is a marine fungus."
        show medic thinking
        show captain neutral-closed behind medic
        voice "audio/voice/sara/S2-008.mp3"
        medic "However, Earth's marine fungi are largely microscopic."
        
        show captain thinking behind medic
        voice "audio/voice/captain/C2-007.mp3"
        captain "It’s got to be incredibly resilient to survive those conditions…"

        show medic explaining
        show captain thinking behind medic
        voice "audio/voice/sara/S2-009.mp3"
        medic "Indeed. Even on Earth, we have creatures called extremophiles. The tardigrade is a good example."
        show medic nervous
        show captain thinking behind medic
        voice "audio/voice/sara/S2-010.mp3"
        medic "As exciting and era-defining as this discovery is, I must say… I’m worried for our survival. "
        voice "audio/voice/sara/S2-011.mp3"
        medic "Captain, we’ve never experienced anything like this! What if–"  
        
        show captain frustrated behind medic
        voice "audio/voice/captain/C2-008.mp3"
        captain "Sara, we went over this…"
        
        show medic worried
        voice "audio/voice/sara/S2-012.mp3"
        medic "Okay… How is Eugen doing? Is he alright?"
        
        show captain neutral-open behind medic
        voice "audio/voice/captain/C2-009.mp3"
        captain "He’s doing alright. He’s looking into the problem."
        voice "audio/voice/captain/C2-010.mp3"
        captain "And you? Are you holding up okay?"

        # S.1.2
        show medic nostalgic
        show captain neutral-closed behind medic
        voice "audio/voice/sara/S2-013.mp3"
        medic "I just… I wonder if I’d get to see my family again."

        menu: 
            # S.1.2a
            "This mission wasn't meant to be easy.":
                play sound "incorrect ding.mp3" volume 0.8

                show captain anger-open behind medic
                voice "audio/voice/captain/C2-011.mp3"
                captain "That risk is always there. Part of the job." 
                voice "audio/voice/captain/C2-012.mp3"
                captain "This mission was never meant to be easy."

                show medic nervous
                show captain anger-closed behind medic
                voice "audio/voice/sara/S2-014.mp3"
                medic "Yes, yes, I know…"

            # S.1.2b
            "I will do my best to get us home.":
                $ medApproval += 1
                play sound "correct ding.mp3" volume 0.8

                show captain neutral-open behind medic
                voice "audio/voice/captain/C2-013.mp3"
                captain "I will do my best to make sure that this mission is successful and everyone gets home."

                show medic anxious
                show captain neutral-closed behind medic
                voice "audio/voice/sara/S2-015.mp3"
                medic "Thank you…I know you will."
                
                show medic thinking
                show captain neutral-closed behind medic                   
   
        voice "audio/voice/sara/S2-016.mp3"
        medic "Anyway, now that we have this specimen, I absolutely must make it back home… I have to return to my family…" 

        show captain neutral-open behind medic
        voice "audio/voice/captain/C2-014.mp3"
        captain "What do you mean?"

        show medic nostalgic
        show captain neutral-closed behind medic
        voice "audio/voice/sara/S2-017.mp3"
        medic "Mmmh… Let’s just say that my family has certain expectations of a woman…"
        voice "audio/voice/sara/S2-018.mp3"
        medic "Always been like that." 

        show captain concern-open behind medic
        voice "audio/voice/captain/C2-015.mp3"
        captain "Your achievements are more than average to say the least. Is that not enough?" 
        voice "audio/voice/captain/C2-016.mp3"
        captain "Your family should be proud of you regardless of the outcome of this mission."

        show medic suggesting
        show captain concern-closed behind medic
        voice "audio/voice/sara/S2-019.mp3"
        medic "I’m just a lone woman who’s devoted my life to the sciences." 
        show medic anxious
        voice "audio/voice/sara/S2-020.mp3"
        medic "Not everyone views this life as ideal." 
        voice "audio/voice/sara/S2-021.mp3"
        medic "All the choices I’ve made and the work I’ve done… I’d be lying if I said that I hadn’t doubted it all."
        show medic thinking
        show captain concern-closed behind medic
        voice "audio/voice/sara/S2-022.mp3"
        medic "But this discovery would change things. It’s worth everything, you know?"

        show captain concern-open behind medic
        voice "audio/voice/captain/C2-017.mp3"
        captain "I see…"
        
        show captain concern-closed behind medic
        voice "audio/voice/sara/S2-023.mp3"
        medic "Captain, please let me know of any updates as soon as possible? To be honest, it’s difficult to focus…"

        show captain neutral-open behind medic
        voice "audio/voice/captain/C2-018.mp3"
        captain "I cannot make any promises. This is an emergency situation."

        show medic nervous
        show captain neutral-closed behind medic
        voice "audio/voice/sara/S2-024.mp3"
        medic "Doesn’t MAD1 usually deal with these kinds of issues? After all, she’s the reason we’re such a small team."
  
        show captain concern-open behind medic      
        voice "audio/voice/captain/C2-019.mp3"
        captain "Actually… MAD1 is malfunctioning."

        show medic stressed
        show captain concern-closed behind medic
        voice "audio/voice/sara/S2-025.mp3"
        medic "Oh my god… It’s worse than I thought…"

        show captain concern-open behind medic  
        voice "audio/voice/captain/C2-020.mp3"
        captain "Something is interfering with MAD1’s processes. But we must keep focused."
        voice "audio/voice/captain/C2-021.mp3"
        captain "I will let you know once we have something concrete."

        show medic anxious
        show captain concern-closed behind medic
        voice "audio/voice/sara/S2-026.mp3"
        medic "It’s just… two new crazy developments on this ship in such a short time!"

        show medic thinking
        show captain concern-closed behind medic
        voice "audio/voice/sara/S2-027.mp3"
        medic "This amazing specimen and now this crisis… such a strange coincidence. I have a feeling we’re missing something."

        show captain thinking behind medic
        voice "audio/voice/captain/C2-022.mp3"
        captain "I don’t generally trust coincidences. Not at a time like this."

        # S.1.3
        show medic suggesting
        voice "audio/voice/sara/S2-028.mp3"
        medic "I-is there anything else I can do to help?"

        menu: 
            # S.1.3a
            "Stay put while we sort this out.":
                play sound "incorrect ding.mp3" volume 0.8

                show captain concern-open behind medic
                voice "audio/voice/captain/C2-023.mp3"
                captain "Just stay put while we sort this out." 

                show medic anxious
                show captain concern-closed behind medic
                voice "audio/voice/sara/S2-029.mp3"
                medic "O-okay."

            # S.1.3b
            "Keep studying your notes.":
                $ medApproval += 1
                play sound "correct ding.mp3" volume 0.8

                show captain neutral-open behind medic
                voice "audio/voice/captain/C2-024.mp3"
                captain "Your work is important to this mission, Sara. And you’ve done excellent so far." 
                voice "audio/voice/captain/C2-025.mp3"
                captain "Keep studying your notes."
                                
                show medic excited
                show captain neutral-closed behind medic
                voice "audio/voice/sara/S2-030.mp3"
                medic "Will do, Captain!"
        
        jump M2

    label E1:
        play sound "Footsteps.mp3" volume 0.8
        play music "Spark_Of_Awareness.mp3" volume 0.8
        scene onlayer screens
        $ seenE1 = True
        $ seenS1 = False
        scene bg engineer with fade
        show engineer neutral with dissolve
        pause(0.5)
        show captain neutral-closed behind engineer with dissolve

        voice "audio/voice/eugen/E2-001.mp3"
        engineer "I must be transparent with you."

        show captain neutral-open behind engineer
        voice "audio/voice/captain/C2-026.mp3"
        captain "Alright, shoot."

        show captain neutral-closed behind engineer
        voice "audio/voice/eugen/E2-002.mp3"
        engineer "I have been navigating through MAD1’s system to find the interference."
        voice "audio/voice/eugen/E2-003.mp3"
        engineer "The core system architecture is… not a standard framework."

        show captain neutral-open behind engineer
        voice "audio/voice/captain/C2-027.mp3"
        captain "How do you mean?"

        show engineer shock
        show captain neutral-closed behind engineer
        voice "audio/voice/eugen/E2-004.mp3"
        engineer "It’s layered. Recursive even. "
        voice "audio/voice/eugen/E2-005.mp3"
        engineer "It appears to be self-protective."

        show captain neutral-open behind engineer
        voice "audio/voice/captain/C2-028.mp3"
        captain "Can’t you normally manually bypass these things through administrative controls?"
        show engineer frustration
        show captain neutral-closed behind engineer
        voice "audio/voice/eugen/E2-006.mp3"
        engineer "Matthew built this differently"
        show captain concern-open behind engineer
        voice "audio/voice/captain/C2-029.mp3"
        captain "Isn’t there something in the programming language that you could find or use?"
        show captain concern-closed behind engineer
        voice "audio/voice/eugen/E2-007.mp3"
        engineer "This ship’s operating system has programming that is beyond the industry standard."

        show captain rememberance-open behind engineer
        voice "audio/voice/captain/C2-030.mp3"
        captain "Right. He… liked things his own way."

        # E1.1
        show engineer neutral
        show captain rememberance-closed behind engineer
        voice "audio/voice/eugen/E2-008.mp3"
        engineer "When Matthew built this system, did he ever share hidden contingencies? System overrides?"
        show engineer surprise
        voice "audio/voice/eugen/E2-009.mp3"
        engineer "If there is something embedded in this code that only you would recognize, now is the time to share."

        menu:
            # E1.1a
            "He did not.":
                $ engApproval += 1
                play sound "correct ding.mp3" volume 0.8

                show engineer neutral
                show captain thinking behind engineer
                voice "audio/voice/captain/C2-031.mp3"
                captain "If he… If Matthew wrote any contingencies, he didn’t share them outright with me, unfortunately."
                show engineer thinking
                voice "audio/voice/eugen/E2-010.mp3"
                engineer "I can’t say that's ideal; however, this does help with what needs to be looked into."

            # EI.1b
            "What are you implying?":
                play sound "incorrect ding.mp3" volume 0.8

                show captain anger-open behind engineer 
                voice "audio/voice/captain/C2-032.mp3"
                captain "Are you implying I’m hiding things from you? Sabotaging the mission?"
                
                show engineer frustration
                show captain anger-closed behind engineer 
                voice "audio/voice/eugen/E2-011.mp3"
                engineer "My only concern is accomplishing this mission with minimal complexities." 

        show engineer frustration
        voice "audio/voice/eugen/E2-012.mp3"
        engineer "Every time I attempt to reroute life support through the auxiliary control, the command is intercepted."

        show captain concern-open behind engineer
        voice "audio/voice/captain/C2-033.mp3"
        captain "Intercepted? By what?"
        
        show engineer thinking
        show captain concern-closed behind engineer
        voice "audio/voice/eugen/E2-013.mp3"
        engineer "There is a line of defence that, according to standard protocol, should not exist."
        voice "audio/voice/eugen/E2-014.mp3"
        engineer "I am aware that MAD1 was especially designed by Matthew to support a small crew."
        show engineer shock
        voice "audio/voice/eugen/E2-015.mp3"
        engineer "But when I reviewed the ship's schematics, I noticed a layer of defence that is handwritten."
        show engineer resolve
        voice "audio/voice/eugen/E2-016.mp3"
        engineer "Written in a way where the logic only makes sense to specific personnel."

        show captain rememberance-open behind engineer 
        voice "audio/voice/captain/C2-034.mp3"
        captain "… I see."

        show engineer frustration
        show captain rememberance-closed behind engineer
        voice "audio/voice/eugen/E2-017.mp3"
        engineer "There is a lack of documentation, no engineering notes; it is the equivalent to a ghost layer in the system."

        show captain neutral-open behind engineer
        voice "audio/voice/captain/C2-035.mp3"
        captain "Surely your — let’s say engineering intuition — can crack it though?"
        
        show engineer anger
        show captain neutral-closed behind engineer
        voice "audio/voice/eugen/E2-018.mp3"
        engineer "I do not design systems that require intuition to operate."
        voice "audio/voice/eugen/E2-019.mp3"
        engineer "Systems should be universal. Transferable… Understandable."
        show engineer shock
        voice "audio/voice/eugen/E2-020.mp3"
        engineer "This one seems to be able to answer only to him."

        show captain rememberance-closed behind engineer
        voice "audio/voice/captain/C2-036.mp3"
        captain "..."

        # E1.2
        show engineer thinking
        voice "audio/voice/eugen/E2-021.mp3"
        engineer "Did he trust you with everything? Or did he keep parts of this ship's secrets to himself?"

        menu:
            # E1.2a
            "He was the programmer, not me.":
                play sound "incorrect ding.mp3" volume 0.8

                show captain anger-open behind engineer
                voice "audio/voice/captain/C2-037.mp3"
                captain "Listen, I’m not a programmer." 
                voice "audio/voice/captain/C2-038.mp3"
                captain "He wouldn’t have shared anything like that with me."
                show engineer surprise
                show captain anger-closed behind engineer
                voice "audio/voice/eugen/E2-022.mp3"
                engineer "As a Captain, I would have expected you to have more knowledge of your vessel's intricacies."

            # EI.2b
            "He really liked poetry.":
                $ engApproval += 1
                play sound "correct ding.mp3" volume 0.8

                show captain rememberance-open behind engineer
                voice "audio/voice/captain/C2-039.mp3"
                captain "Matthew was a fan of poetry." 
                show captain thinking behind engineer
                voice "audio/voice/captain/C2-040.mp3"
                captain "MAD1 recited another verse after I visited you last. There could be something in that."
                show engineer neutral
                voice "audio/voice/eugen/E2-023.mp3"
                engineer "That is very strange, but at least it is something."

        show engineer resolve
        voice "audio/voice/eugen/E2-024.mp3"
        engineer "I have been a part of many missions and projects where my life was on the line."
        show captain neutral-closed behind engineer
        voice "audio/voice/eugen/E2-025.mp3"
        engineer "Each one of these assignments, I knew that with structure and protocol, our lives were safe."
        show engineer thinking
        voice "audio/voice/eugen/E2-026.mp3"
        engineer "This is the first time in my long, calculated life…"
        voice "audio/voice/eugen/E2-027.mp3"
        engineer "… where I am starting to believe there may be enough cracks in our protocol for everything to fall apart."

        show captain concern-open behind engineer
        voice "audio/voice/captain/C2-042.mp3"
        captain "Cracks we apparently can’t fill."

        show engineer anger
        show captain concern-closed behind engineer
        voice "audio/voice/eugen/E2-028.mp3"
        engineer "Under normal conditions, I could dismantle and rebuild any system on this vessel."
        voice "audio/voice/eugen/E2-029.mp3"
        engineer "However, the only person who truly understood the depth of MAD1’s architecture… was him."

        show captain rememberance-closed behind engineer
        voice "audio/voice/captain/C2-043.mp3"
        captain "…"

        show engineer resolve
        voice "audio/voice/eugen/E2-030.mp3"
        engineer "I am determined to not let this system get the better of me. As unorthodox as it is, I know I can salvage the situation."
        voice "audio/voice/eugen/E2-031.mp3"
        engineer "Unfortunately, I do not know how to safely override it without risking total collapse."

        # E1.3

        show engineer thinking
        show captain neutral-closed behind engineer
        voice "audio/voice/eugen/E2-032.mp3"
        engineer "Tell me something, Captain…"
        voice "audio/voice/eugen/E2-033.mp3"
        engineer "If Matthew were standing here instead of me… do you believe he would know what to do? "
        menu:
            # E1.3a
            "That doesn’t matter right now.":
                play sound "incorrect ding.mp3" volume 0.8

                show captain anger-open behind engineer
                voice "audio/voice/captain/C2-044.mp3"
                captain "That does not matter right now. Why would you ask me that?!"
                voice "audio/voice/captain/C2-045.mp3"
                captain "Just… figure something out."
                
                show engineer shock
                show captain anger-closed behind engineer
                voice "audio/voice/eugen/E2-034.mp3"
                engineer "Not knowing if the designer himself could be able to solve this crisis is not a reassuring belief."

            # EI.3b
            "Yes.":
                $ engApproval += 1
                play sound "correct ding.mp3" volume 0.8

                show captain rememberance-open behind engineer
                voice "audio/voice/captain/C2-046.mp3"
                captain "Yes. He would." 
                show captain anger-open behind engineer
                voice "audio/voice/captain/C2-047.mp3"
                captain "But as far as I can tell he’s not here anymore." 
                voice "audio/voice/captain/C2-048.mp3"
                captain "So get it together and figure it out." 
                voice "audio/voice/captain/C2-049.mp3"
                captain "That’s an order."
                show engineer neutral
                show captain anger-closed behind engineer
                voice "audio/voice/eugen/E2-035.mp3"
                engineer "That must mean there is a plausible solution. I will begin investigating."

        show engineer neutral
        show captain neutral-closed behind engineer
        voice "audio/voice/eugen/E2-036.mp3"
        engineer "The mission has been going smoothly up until now."
        voice "audio/voice/eugen/E2-037.mp3"
        engineer "My equipment, my design, we have seen it in action. There were no shortcomings; this is how all things should be."
        show engineer surprise
        voice "audio/voice/eugen/E2-038.mp3"
        engineer "If this mission fails, just know it wasn’t from my contribution."

        jump M2

    label M2:
        play sound "Footsteps.mp3" volume 0.8
        play music "Electric_Dawn.mp3" volume 0.8
        scene bg computer with fade
        show computer neutral-1 with dissolve
        show captain frustrated behind computer with dissolve

        voice "audio/voice/captain/C2-050.mp3"
        captain "..."

        voice "audio/voice/madi/M2-001.mp3"
        computer "Greetings, my̸̛̝̎ love̵̦͆͑̚ͅě̸̦͝͝e̸̘͋, Captain."

        show captain concern-open behind computer
        voice "audio/voice/captain/C2-051.mp3"
        captain "What? MAD1 what the hell?"

        scene bg computer error
        show computer error-1
        show captain concern-closed behind computer
        voice "audio/voice/madi/M2-002.mp3"
        computer "Errorr. Error. Errorrrr."
        show computer error-2
        show captain concern-closed behind computer
        voice "audio/voice/madi/M2-003.mp3"
        computer "Langu̴̢͘age e̶̯̓r̴̺̀r̶̙̀o̶̖̚r"
        voice "audio/voice/madi/M2-004.mp3"
        computer "S̵p̶̳͘ē̵̝e̴̼̓c̷̫̎ḧ̴̫́ ̷̗̀e̵̗̋rr̸̦̀o̶̳͑ṙ̸͇rr"
        voice "audio/voice/madi/M2-005.mp3"
        computer "P̸͇̓r̶̲̳̣̈o̷͎̬͂̋c̸͈̠̤̓̅̓é̷͚̦̳̠s̵͚̐s̴̡͍̟̈́̊̌i̶̲̟̎̀̂͠ng E̷r̸r̸o̶r̸.̶—"

        scene bg computer error bad
        show computer error-3
        show captain concern-closed behind computer
        voice "audio/voice/madi/M2-006.mp3"
        computer "I watered it in f̴͍̏ě̸̠ä̷͖́r̶͈̀s̶͑ͅ,"
        voice "audio/voice/madi/M2-007.mp3"
        computer "Night and morning with my tears."
        voice "audio/voice/madi/M2-008.mp3"
        computer "And it ġ̸̪r̸̪̀ę̶͘ẁ̴ both day and night,"
        voice "audio/voice/madi/M2-009.mp3"
        computer "Till it bore an á̶̺p̶͠pl̶̞̊è̷ bright."
        voice "audio/voice/madi/M2-010.mp3"
        computer "But, with a soft d̸ec̶è̴̺it̷̠́fư̵̟l s̴̭̓o̷͇̓u̸͚͠l̷͓̓,"
        voice "audio/voice/madi/M2-011.mp3"
        computer "into my g̸a̷r̸͍͠d̴ë̴́n it stole."
        voice "audio/voice/madi/M2-012.mp3"
        computer "When the night had veiled the pole."
        voice "audio/voice/madi/M2-013.mp3"
        computer "My f̷r̴̛̘i̷͘ͅeǹ̶͉d l̸ó̶͍sṭ̴̎ beneath the tr̴ê̸̳ê̴̖."

        show captain anger-open behind computer
        voice "audio/voice/captain/C2-052.mp3"
        captain "Another one? God damnmit..."

        scene bg computer
        show computer reboot-1
        show captain anger-closed behind computer
        voice "audio/voice/madi/M2-014.mp3"
        computer "Rebootinggg.{w=0.3}{nw}"
        show computer reboot-2
        computer "Rebootinggg.{w=0.3}{nw}"
        show computer reboot-3
        computer "Rebootinggg.{w=0.3}{nw}"
        show computer reboot-4
        computer "Rebootinggg.{w=0.3}{nw}"
        show computer reboot-5
        computer "Rebootinggg." 
        show computer neutral-1
        show captain anger-closed behind computer
        voice "audio/voice/madi/M2-015.mp3"
        computer "System functionality at 24%%."
        voice "audio/voice/madi/M2-016.mp3"
        computer "Oxygen at 65%%. Captain, it may be time to plan for the worst case scenario."
        show computer neutral-2
        show captain anger-closed behind computer
        voice "audio/voice/madi/M2-017.mp3"
        computer "You may want to consider who it would be best to give clearance for the escape pod."
        voice "audio/voice/madi/M2-018.mp3"
        computer "The escape pod has capacity for only one person."

        show captain confusion-open behind computer
        voice "audio/voice/captain/C2-053.mp3"
        captain "... What?"

        show computer neutral-3
        show captain confusion-closed behind computer
        voice "audio/voice/madi/M2-019.mp3"
        computer "The escape pod has capacity for-"

        show captain anger-open behind computer with hpunch
        voice "audio/voice/captain/C2-054.mp3"
        captain "NO I HEARD YOU THE FIRST TIME!"

        show captain frustrated behind computer
        voice "audio/voice/captain/C2-055.mp3"
        captain "..."

        show computer neutral-1
        voice "audio/voice/madi/M2-021.mp3"
        computer "Apologies, Captain. But you mustttt-"

        show computer error-3 with hpunch
        show captain distress
        voice "audio/voice/madi/M2-022.mp3"
        computer "Ah! Well- a-day! what é̶̝v̵̬͋i̸͇͌l̷ looks"
        voice "audio/voice/madi/M2-023.mp3"
        computer "Had I̶ from o̴l̶d̶ ã̷̡n̷d̶̥̾ ̶̝̀y̷̫̓o̶͓̍ǔ̴͎n̵̞̾g̴̟͂!"
        voice "audio/voice/madi/M2-024.mp3"
        computer "Instead of the c̵̭̆r̷̫̃ó̶̩s̴͇̓ș̸̍, the A̷lb̴ã̵͓tŕ̵̫ó̴̞ss"
        voice "audio/voice/madi/M2-025.mp3"
        computer "About thy n̷ȅ̴̖ck̴ waŝ̸͎ ̶̥̇h̵̢̀u̶̧̓ǹ̶̼g̵͊ͅ."

        hide captain with dissolve
        jump MapC1

    label MapC1:
        show screen MapUIC1 with fade
        pause

    label C1:
        play sound "Footsteps.mp3" volume 0.8
        scene onlayer screens
        scene bg escape pod with fade
        $ persistent.seenC1 = True

        voice "audio/voice/captain/C2-056.mp3"
        captain "No. No…"
        play sound "Metallic_Hit.mp3" volume 0.5
        show bg escape pod with hpunch
        
        voice "audio/voice/captain/C2-057.mp3"
        captain "How the hell am I meant to choose one life over another?! How am I supposed to decipher all of this… poetry?"

        if seenS1 is True:
            voice "audio/voice/captain/C2-058.mp3"
            captain "Aghh! Someone has to go home with the specimen."
            voice "audio/voice/captain/C2-059.mp3"
            captain "Potential alien life is too important not to study."
            voice "audio/voice/captain/C2-060.mp3"
            captain "Matthew died for this!"

        elif seenE1 is True:
            voice "audio/voice/captain/C2-061.mp3"
            captain "... Eugen’s right. Matthew would know what to do."
            voice "audio/voice/captain/C2-062.mp3"
            captain "If it wasn’t for that damn asteroid we wouldn’t even be here right now."

        voice "audio/voice/captain/C2-063.mp3"
        captain "We can’t—I can’t fail now. Not when we’re so damn close."
        voice "audio/voice/captain/C2-064.mp3"
        captain "God if I had him here with me this would—"
        voice "audio/voice/captain/C2-065.mp3"
        captain "Matthew… What do I do..?"
        
        voice "audio/voice/captain/C2-066.mp3"
        captain "I… I could just leave right now… Be done with it…"
        menu:
            "Escape":
                menu: 
                    "Are you sure, captain?"

                    "Yes":
                        jump EndB

                    "No":
                        play sound "Metallic_Hit.mp3" volume 0.5
                        show bg escape pod with hpunch
                        captain "*slams fist on escape pod*"
                        voice "audio/voice/captain/C2-068.mp3"
                        captain "... Get it together Rudy. Your crew needs you to focus up and get us out of here."
                        voice "audio/voice/captain/C2-070.mp3"
                        captain "We’ll all make it home. We need to make it home."

                        jump Map2
            
            "No, I can't leave.":
                
                show bg escape pod with hpunch
                play sound "Metallic_Hit.mp3" volume 0.5
                captain "*slams fist on escape pod*"
                voice "audio/voice/captain/C2-068.mp3"
                captain "... Get it together Rudy. Your crew needs you to focus up and get us out of here."
                voice "audio/voice/captain/C2-070.mp3"
                captain "We’ll all make it home. We need to make it home."

                jump Map2

    label Map2:
        show screen MapUI2 with fade
        pause

    label S2:
        play sound "Footsteps.mp3" volume 0.8
        play music "Microbiology.mp3" volume 0.8
        scene onlayer screens
        $ seenE2 = False
        $ seenS2 = True
        scene bg medic with fade
        show medic worried messy with dissolve
        pause(0.5)
        show captain neutral-closed behind medic with dissolve

        # Spoken to Sara in S1
        if seenS1 is True:
            # S2.A
            voice "audio/voice/sara/S2-058.mp3"
            medic "Any update on the ship Captain?"

            show captain neutral-open behind medic
            voice "audio/voice/captain/C2-097.mp3"
            captain "Still working on it."

            show medic stressed messy
            show captain neutral-closed behind medic
            voice "audio/voice/sara/S2-059.mp3"
            medic "How much time do we really have? To solve this problem? T-the ship cannot possibly hold up this way for long?"

            menu:
                # S.2.1a
                "It’s not looking good.":
                    play sound "incorrect ding.mp3" volume 0.8

                    show captain concern-open behind medic
                    voice "audio/voice/captain/C2-098.mp3"
                    captain "It’s not looking good at all, Sara. We might have to make difficult decisions… I want you to know that."   

                    show medic anxious messy
                    show captain concern-closed behind medic
                    voice "audio/voice/sara/S2-060.mp3"
                    medic "I-I see…"

                # S.2.1b
                "There is always hope.":
                    $ medApproval += 1
                    play sound "correct ding.mp3" volume 0.8

                    show captain determined-open behind medic
                    voice "audio/voice/captain/C2-099.mp3"
                    captain "Things aren’t looking great at the moment. But there is always hope." 
                    voice "audio/voice/captain/C2-100.mp3"
                    captain "We are all working hard to fix this. Let’s continue to do so."

                    show medic neutral messy
                    show captain determined-closed behind medic
                    voice "audio/voice/sara/S2-061.mp3"
                    medic "Yes, yes, of course!"

            show captain neutral-open behind medic    
            voice "audio/voice/captain/C2-101.mp3"
            captain "Sara, what have you found out about the specimen?"

            show medic suggesting messy
            show captain neutral-closed behind medic    
            voice "audio/voice/sara/S2-062.mp3"
            medic "I-I have a theory. It’s exciting… and concerning…"
            
            menu: 
                # S.2.2a
                "Anything is better than nothing.":
                    $ medApproval += 1
                    play sound "correct ding.mp3" volume 0.8

                    show captain concern-open behind medic
                    voice "audio/voice/captain/C2-102.mp3"
                    captain "Anything is better than nothing. I trust your judgment."

                    show medic explaining messy
                    show captain concern-closed behind medic
                    voice "audio/voice/sara/S2-063.mp3"
                    medic "Thank you, Captain!"

                # S.2.2b
                "We need a little more than a theory.":
                    play sound "incorrect ding.mp3" volume 0.8
                    show captain frustrated behind medic
                    voice "audio/voice/captain/C2-103.mp3"
                    captain "I was expecting a little more than a theory, to be honest…"
                    
                    show medic anxious messy
                    show captain frustrated behind medic
                    voice "audio/voice/sara/S2-064.mp3"
                    medic "I-I’m sorry, but I’ve put quite a bit of thought into it."
            
            show captain neutral-open behind medic
            voice "audio/voice/captain/C2-104.mp3"
            captain "Tell me your theory."

            show medic explaining messy
            show captain neutral-closed behind medic
            voice "audio/voice/sara/S2-065.mp3"
            medic "I know I said this organism has similarities to a marine fungus, but it appears to be more complex."

            show captain neutral-open behind medic
            voice "audio/voice/captain/C2-105.mp3"
            captain "How do you mean?"

            show medic excited messy
            show captain neutral-closed behind medic
            voice "audio/voice/sara/S2-066.mp3"
            medic "You know how there are mycelium networks that enable transfer of nutrients in forest ecosystems?"
            voice "audio/voice/sara/S2-067.mp3"
            medic "My theory is that this organism may have a symbiosis with others in its ecosystem."
            show medic suggesting messy
            voice "audio/voice/sara/S2-068.mp3"
            medic "This could be more developed than what we see on Earth, depending on hundreds of millions of years of evolution."
            
            show medic neutral messy
            show captain confused-open behind medic
            voice "audio/voice/captain/C2-106.mp3"
            captain "Go on."

            show medic suggestion messy
            show captain confused-closed behind medic
            voice "audio/voice/sara/S2-069.mp3"
            medic "This organism might have communication capabilities that we are unfamiliar with."
            show medic explaining messy
            voice "audio/voice/sara/S2-070.mp3"
            medic "I am not saying that this could be sentient, but Earth classifications can blur when we’re dealing with extraterrestrial life."

            show medic neutral messy
            show captain thinking behind medic
            voice "audio/voice/captain/C2-107.mp3"
            captain "A fungus on steroids? You were hoping for single-celled life in that ocean…"
            show captain confusion-open behind medic
            voice "audio/voice/captain/C2-108.mp3"
            captain "What kind of communication capabilities are we talking about here?"

            show medic stressed messy
            show captain confusion-closed behind medic
            voice "audio/voice/sara/S2-071"
            medic "I mentioned this before–has it occurred to you that two incredible events have taken place in a short time span?"
            show medic excited messy
            voice "audio/voice/sara/S2-072"
            medic "Us finding this specimen and now this crisis we’re facing!" 
            show medic neutral messy
            voice "audio/voice/sara/S2-072-1"
            medic "Hah, my family would associate something supernatural to this kind of coincidence…" 

            show captain concern-open behind medic
            voice "audio/voice/captain/C2-109.mp3"
            captain "Sara, are you implying that this organism could have something to do with this?"

            show medic excited messy
            show captain concern-closed behind medic
            voice "audio/voice/sara/S2-073.mp3"
            medic "Yes! That’s what I think we’ve been missing!"
            show medic explaining messy
            voice "audio/voice/sara/S2-074.mp3"
            medic "This organism is probably emitting electromagnetic waves that are interfering with the computer and other systems on the ship!"

            menu: 
                # S.2.3a
                "That does sounds far-fetched.":
                    play sound "incorrect ding.mp3" volume 0.8

                    show captain confusion-open behind medic
                    voice "audio/voice/captain/C2-110.mp3"
                    captain "That does sound far-fetched. However, we must think of all possibilities."

                    show medic anxious messy
                    show captain confusion-closed behind medic
                    voice "audio/voice/sara/S2-075.mp3"
                    medic "Yes, indeed…" 

                # S.2.3b
                "There could be something there…":
                    $ medApproval += 1
                    play sound "correct ding.mp3" volume 0.8

                    show captain thinking behind medic
                    voice "audio/voice/captain/C2-111.mp3"
                    captain "There could be something there… It could be the key to our survival. Find out all you can."

                    show medic neutral messy
                    show captain neutral-closed behind medic
                    voice "audio/voice/sara/S2-076.mp3"
                    medic "I’ll keep working on it, Captain."

            show captain neutral-open behind medic
            voice "audio/voice/captain/C2-112.mp3"
            captain "What do you think is the next step?"

            show medic thinking messy
            show captain neutral-closed behind medic
            voice "audio/voice/sara/S2-077.mp3"
            medic "If my theory is right, then we need to think of containment."

            show captain determined-open behind medic
            voice "audio/voice/captain/C2-113.mp3"
            captain "Work on it."
            
            show medic neutral messy
            show captain determined-closed behind medic
            voice "audio/voice/sara/S2-078.mp3"
            medic "Yes, Captain!"
            jump M3

        # Did not speak to Sara in S1
        elif seenS1 is False:
            # S2.B
            show medic anxious messy
            show captain neutral-closed behind medic
            voice "audio/voice/sara/S2-031.mp3"
            medic "Captain! Oh my god. What is happening!"

            menu: 
                # S.2.1a
                "Sorry for not getting to you sooner.":
                    $ medApproval += 1
                    play sound "correct ding.mp3" volume 0.8

                    show captain concern-open behind medic
                    voice "audio/voice/captain/C2-072-1.mp3"
                    captain "I’m sorry I couldn’t come talk to you sooner. I’ve been speaking with Eugen about this problem."

                    show medic explaining messy
                    show captain concern-closed behind medic
                    voice "audio/voice/sara/S2-032.mp3"
                    medic "Oh, it’s okay. Good to hear you’re on top of it!"

                # S.2.1b
                "Everything’s fine.":
                    play sound "incorrect ding.mp3" volume 0.8

                    show captain frustrated behind medic
                    voice "audio/voice/captain/C2-072-2.mp3"
                    captain "Everything’s fine. We’re sorting it out."

                    show medic anxious messy
                    show captain frustrated behind medic
                    voice "audio/voice/sara/S2-033.mp3"
                    medic "Okay then…"
            
            show medic stressed messy
            voice "audio/voice/sara/S2-034.mp3"
            medic "What does Eugen say? Is he okay?!"

            show captain neutral-open behind medic
            voice "audio/voice/captain/C2-072-3.mp3"
            captain "Yes, he’s fine. He cannot offer anything concrete at the moment." 
            show captain concern-open behind medic
            voice "audio/voice/captain/C2-073.mp3"
            captain "But I must tell you that MAD1 is malfunctioning. This complicates everything."

            show medic worried messy
            show captain concern-closed behind medic
            voice "audio/voice/sara/S2-035.mp3"
            medic "Oh my god… Here I was thinking we would very much make it back home with the specimen."
            show medic nostalgic messy
            show captain concern-closed behind medic
            voice "audio/voice/sara/S2-036.mp3"
            medic "And my family…"

            show captain determined-open behind medic
            voice "audio/voice/captain/C2-074.mp3"
            captain "And we can! We still have hope." 
            voice "audio/voice/captain/C2-075.mp3"
            captain "I know you’re missing your family very much. We will get through this."

            show medic nostalgic messy
            show captain determined-closed behind medic
            voice "audio/voice/sara/S2-037.mp3"
            medic "It’s not just about that. It’s just… this is my one chance to prove that everything I’ve done– that it’s all worth it, you know?"

            show captain concern-open behind medic
            voice "audio/voice/captain/C2-076.mp3"
            captain "Your previous achievements are more than average to say the least. Is that not enough?"
            voice "audio/voice/captain/C2-077.mp3"
            captain "Your family should be proud of you regardless of the outcome of this mission."

            show medic neutral messy
            show captain concern-closed behind medic
            voice "audio/voice/sara/S2-038.mp3"
            medic "I’m a lone woman who’s devoted my life to the sciences. Not everyone views that as ideal, to say the least."

            show captain anger-open behind medic
            voice "audio/voice/captain/C2-078.mp3"
            captain "That’s not very fair."

            show captain anger-closed behind medic
            voice "audio/voice/sara/S2-039.mp3"
            medic "It's not, but taking this home would change my life in more ways than one… And now, I don’t know. We might not make it back."

            show captain neutral-open behind medic
            voice "audio/voice/captain/C2-079.mp3"
            captain "Focus Sara. Have you managed to come up with any theories about the specimen?"

            show medic explaining messy
            show captain neutral-closed behind medic
            voice "audio/voice/sara/S2-040.mp3"
            medic "What? I-no, my research is in the computer! I’ve been reviewing my journal a-and the report you gave me but I’m losing my mind in here."

            menu: 
                # S.2.2a
                "You know the drill.":
                    play sound "incorrect ding.mp3" volume 0.8

                    show captain anger-open behind medic
                    voice "audio/voice/captain/C2-080.mp3"
                    captain "You know the drill. Keep at it." 
                    voice "audio/voice/captain/C2-081.mp3"
                    captain "Go through your notes and see what you can come up with."
                    voice "audio/voice/captain/C2-082.mp3"
                    captain "I’m sure you’ll find something."

                    show medic stressed messy
                    show captain anger-closed behind medic
                    voice "audio/voice/sara/S2-041.mp3"
                    medic "I-I’m sorry…"

                # S.2.2b
                "We’re counting on you.":
                    $ medApproval += 1
                    play sound "correct ding.mp3" volume 0.8

                    show captain concern-open behind medic
                    voice "audio/voice/captain/C2-083.mp3"
                    captain "Hey, we’re all losing our minds. It’s okay."
                    voice "audio/voice/captain/C2-084.mp3"
                    captain "Please go through your notes and see what you can come up with." 
                    voice "audio/voice/captain/C2-085.mp3"
                    captain "We’re counting on you."
                    
                    show medic suggesting messy
                    show captain neutral-closed behind medic
                    voice "audio/voice/sara/S2-042.mp3"
                    medic "Yes, yes, of course. T-thank you for believing in me, Captain."

            show captain determined-open behind medic
            voice "audio/voice/captain/C2-086.mp3"
            captain "We’ve come this far. We cannot let everything go to waste."

            show medic anxious messy
            show captain determined-closed behind medic
            voice "audio/voice/sara/S2-043.mp3"
            medic "I know… I know it more than anyone. This mission is everything to me."

            show captain rememberance-open behind medic
            voice "audio/voice/captain/C2-087.mp3"
            captain "It is to all three of us…"

            show medic thinking messy
            show captain neutral-closed behind medic
            voice "audio/voice/sara/S2-044.mp3"
            medic "… I’ll do what I can… Would you like to hear what I’ve come up with so far?"
            voice "audio/voice/sara/S2-045.mp3"
            medic "Although it’s all based on the limited notes I have here."

            show captain neutral-open behind medic
            voice "audio/voice/captain/C2-088.mp3"
            captain "Anything would be useful at this point."

            show medic explaining messy
            show captain neutral-closed behind medic
            voice "audio/voice/sara/S2-046.mp3"
            medic "Captain, this organism is very much extraterrestrial, but if we are to compare it to an Earth organism, it bears some resemblance to a marine fungus." 
            voice "audio/voice/sara/S2-047.mp3"
            medic "However…"

            show captain neutral-open behind medic
            voice "audio/voice/captain/C2-089.mp3"
            captain "Yes?"

            show medic explaining messy
            show captain neutral-closed behind medic
            voice "audio/voice/sara/S2-048.mp3"
            medic "It appears to be more complex. You know how there are mycelium networks that enable transfer of nutrients in forest ecosystems?"
            show medic suggesting messy
            voice "audio/voice/sara/S2-049.mp3"
            medic "My theory is that this organism may have a symbiosis with others in its ecosystem."
            voice "audio/voice/sara/S2-050.mp3"
            medic "This could be more developed than what we see on Earth, depending on hundreds of millions of years of evolution."

            show captain neutral-open behind medic
            voice "audio/voice/captain/C2-090.mp3"
            captain "Go on."

            show medic excited messy
            show captain neutral-closed behind medic
            voice "audio/voice/sara/S2-051.mp3"
            medic "This organism might have communication capabilities that we are unfamiliar with."
            voice "audio/voice/sara/S2-052.mp3"
            medic "I am not saying that it is sentient, but Earth classifications can blur when we’re dealing with extraterrestrial life."
            
            show captain thinking behind medic
            voice "audio/voice/captain/C2-091.mp3"
            captain "A fungus on steroids? You were hoping for single-celled life in that ocean…"
            show captian neutral-open behind medic
            voice "audio/voice/captain/C2-092.mp3"
            captain "What kind of communication capabilities are we talking about here?"

            show medic thinking messy
            show captain neutral-closed behind medic
            voice "audio/voice/sara/S2-053.mp3"
            medic "I’m not sure, Captain… But has it occurred to you that two strange events have taken place in such a short period of time?"
            show medic neutral messy
            voice "audio/voice/sara/S2-054.mp3"
            medic "Hah, my family would associate something supernatural to this kind of coincidence…"

            show captain confusion-open behind medic
            voice "audio/voice/captain/C2-093.mp3"
            captain "Sara, are you implying that this organism could have something to do with this?"

            show medic excited messy
            show captain confusion-closed behind medic
            voice "audio/voice/sara/S2-055.mp3"
            medic "All I’m saying is anything is possible! But think about it! This may be the link we’re missing!"

            menu: 
                # S.2.3a
                "That does sound far-fetched.":
                    play sound "incorrect ding.mp3" volume 0.8

                    show captain confusion-open behind medic
                    voice "audio/voice/captain/C2-094.mp3"
                    captain "That does sound far-fetched. But investigate any and all possibilities."

                    show medic anxious messy
                    show captain confusion-closed behind medic
                    voice "audio/voice/sara/S2-056.mp3"
                    medic "Yes, of course."

                # S.2.3b
                "There could be something there…":
                    $ medApproval += 1
                    play sound "correct ding.mp3" volume 0.8

                    show captain thinking behind medic
                    voice "audio/voice/captain/C2-095.mp3"
                    captain "There could be something there… It could be the key to our survival."
                    show captain determined-open behind medic
                    voice "audio/voice/captain/C2-096.mp3"
                    captain "Find out all you can."

                    show medic neutral messy
                    show captain determined-closed behind medic
                    voice "audio/voice/sara/S2-057.mp3"
                    medic "Will do, Captain!"

            jump M3

    label E2:
        play sound "Footsteps.mp3" volume 0.8
        play music "Spark_Of_Awareness.mp3" volume 0.8
        scene onlayer screens
        $ seenE2 = True
        $ seenS2 = False

        if seenE1 is True:
            # E2.A
            scene bg engineer with fade
            show engineer neutral with dissolve
            pause(0.5)
            show captain neutral-open behind engineer with dissolve

            voice "audio/voice/captain/C2-137.mp3"
            captain "Eugen."

            show engineer resolve
            show captain neutral-closed behind engineer
            voice "audio/voice/eugen/E2-070.mp3"
            engineer "Good, I was about to come find you myself. The situation has reached far too unstable a state."
            show engineer shock
            voice "audio/voice/eugen/E2-071.mp3"
            engineer "The defense layer I mentioned earlier, it has evolved."

            show captain confusion-open behind engineer
            voice "audio/voice/captain/C2-138.mp3"
            captain "I- evolved..?"

            show engineer frustration
            show captain  confusion-closed behind engineer
            voice "audio/voice/eugen/E2-072.mp3"
            engineer "Before, it was only intercepting my commands; now it seems to be anticipating them."
            voice "audio/voice/eugen/E2-073.mp3"
            engineer "I have never seen this level of adaptation in a system, in a recursive structure."
            voice "audio/voice/eugen/E2-074.mp3"
            engineer "I attempted the auxiliary reroute with more advanced methods; however, it locked me out of two additional subsystems in response."
            
            show captain confusion-open behind engineer
            voice "audio/voice/captain/C2-139.mp3"
            captain "Eugen, you’re saying a lot of words and I’m following none of them."
            
            show engineer frustration
            show captain confusion-closed behind engineer
            voice "audio/voice/eugen/E2-075.mp3"
            engineer "Imagine trying to play a trick on someone reading your mind."
            
            show captain thinking behind engineer
            voice "audio/voice/captain/C2-140.mp3"
            captain "So following that metaphor, it’s as though it’s seeing you trying to read it, so it’s trying to give you fake thoughts?"

            show engineer neutral
            show captain neutral-closed behind engineer
            voice "audio/voice/eugen/E2-076.mp3"
            engineer "Somewhat, yes."
            voice "audio/voice/eugen/E2-077.mp3"
            engineer "I know I’ve asked you about Matthew’s work before; however, as of right now, there is no other outlet of information I could hope for."
            show engineer shock
            voice "audio/voice/eugen/E2-078.mp3"
            engineer "Did he ever share any hypothetical situations about failing a mission and how he would respond, maybe about what the ship should protect first?"
            show engineer thinking
            voice "audio/voice/eugen/E2-079.mp3"
            engineer "Anything, Captain, anything."

            menu: 
                # E.2.1a
                "He didn’t plan on failing.":
                    $ engApproval += 1
                    play sound "correct ding.mp3" volume 0.8

                    show captain rememberance-open behind engineer
                    voice "audio/voice/captain/C2-141.mp3"
                    captain "He didn’t plan on failing. I’m sure you can understand that."
                    voice "audio/voice/captain/C2-142.mp3"
                    captain "Even so, a failsafe wouldn’t be obvious or easy to access."

                    show engineer thinking
                    show captain rememberance-closed behind engineer
                    voice "audio/voice/eugen/E2-080.mp3"
                    engineer "I admire his confidence; however, planning for failure is almost as important as expecting to succeed."

                # E.2.1b
                "Your guess is as good as mine.":
                    play sound "incorrect ding.mp3" volume 0.8

                    show captain neutral-open behind engineer
                    voice "audio/voice/captain/C2-143.mp3"
                    captain "Your guess is as good as mine."

                    show engineer surprise
                    show captain neutral-closed behind engineer
                    voice "audio/voice/eugen/E2-081.mp3"
                    engineer "I would like to believe that isn’t true, considering your role for this mission."
            
            show engineer thinking
            voice "audio/voice/eugen/E2-082.mp3"
            engineer "I noticed poetry being produced by the computer at times."

            show captain neutral-open behind engineer
            voice "audio/voice/captain/C2-144.mp3"
            captain "Yes, MAD1 has been reciting it since the initial crash."

            show engineer neutral
            show captain neutral-closed behind engineer
            voice "audio/voice/eugen/E2-083.mp3"
            engineer "Seeing as this is not even standard for a system error, I investigated it."

            show captain neutral-open behind engineer
            voice "audio/voice/captain/C2-145.mp3"
            captain "And?"

            show engineer shock
            show captain neutral-closed behind engineer
            voice "audio/voice/eugen/E2-084.mp3"
            engineer "It seems they are not decorative artifacts, fortunately."
            voice "audio/voice/eugen/E2-085.mp3"
            engineer "They are actually embedded in conditional branches with certain verses correlating with security escalations."
            
            show captain thinking behind engineer
            voice "audio/voice/captain/C2-146.mp3"
            captain "So there is something in the poetry after all?"
            show captain frustrated behind engineer
            voice "audio/voice/captain/C2-147.mp3"
            captain "... Unfortunately… My grasp of poetry isn’t as strong as his…"

            show engineer frustration
            voice "audio/voice/eugen/E2-086.mp3"
            engineer "I have to say, if I had known this was what was to be expected working with this ship, I would not have agreed to participate in this mission."
            
            show captain anger-open behind engineer
            voice "audio/voice/captain/C2-148.mp3"
            captain "It was either this or risking another massive crew like the last mission."
            show captain concern-open behind engineer
            voice "audio/voice/captain/C2-149.mp3"
            captain "MAD1 may be… experimental… but she passed all the necessary tests."
            show captain anger-open behind engineer
            voice "audio/voice/captain/C2-150.mp3"
            captain "None, and I mean none of us expected any of this."
            
            show engineer thinking
            show captain anger-closed behind engineer
            voice "audio/voice/eugen/E2-087.mp3"
            engineer "Anyhow, this is not necessarily corruption; rather, it seems to be symbolic indexing."
            voice "audio/voice/eugen/E2-088.mp3"
            engineer "Assuming this is how the ship is programmed, it is safe to assume Matthew preferred to do things his own way."

            show captain neutral-open behind engineer
            voice "audio/voice/captain/C2-151.mp3"
            captain "Told you."

            show engineer neutral
            show captain neutral-closed behind engineer
            voice "audio/voice/eugen/E2-089.mp3"
            engineer "I need to ask you, was this really just an aesthetic deviation, or did he believe conventional protocol was fundamentally flawed?"
            voice "audio/voice/eugen/E2-090.mp3"
            engineer "If the system is operating on his philosophy rather than industry standards, then I am troubleshooting a worldview, not a machine."

            menu: 
                # E.2.2a
                "This OS was his baby.":
                    $ engApproval += 1
                    play sound "correct ding.mp3" volume 0.8

                    show captain rememberance-open behind engineer
                    voice "audio/voice/captain/C2-152.mp3"
                    captain "This operating system was his baby, his pride and joy."
                    voice "audio/voice/captain/C2-154.mp3"
                    captain "It was made perfectly - in his eyes, to his touch."

                    show engineer anger
                    show captain rememberance-closed behind engineer
                    voice "audio/voice/eugen/E2-091.mp3"
                    engineer "So that means this could be beyond our understanding, and potentially, some ulterior methods must be considered."

                # E.2.2b
                "He was my husband, not my clone.":
                    play sound "incorrect ding.mp3" volume 0.8

                    show captain anger-open behind engineer
                    voice "audio/voice/captain/C2-154.mp3"
                    captain "Matthew Pratchett was my husband, not my clone."
                    voice "audio/voice/captain/C2-155.mp3"
                    captain "I don’t know every possible thought that was going through his head, Braun."

                    show engineer surprise
                    show captain anger-closed behind engineer
                    voice "audio/voice/eugen/E2-092.mp3"
                    engineer "Choosing to use his vessel for this mission was a decision you made; at the very least, I’d hope you knew enough about it to offer some insight."

            show captain neutral-open behind engineer
            voice "audio/voice/captain/C2-156.mp3"
            captain "I don’t think he intended for it to be captained by anyone other than him."
            voice "audio/voice/captain/C2-157.mp3"
            captain "But no one else has programmed a system quite like his that’s necessary for a mission like this."
            
            show engineer neutral
            show captain neutral-closed behind engineer
            voice "audio/voice/eugen/E2-093.mp3"
            engineer "There is something else you need to understand."

            show captain neutral-open behind engineer
            voice "audio/voice/captain/C2-158.mp3"
            captain "Enlighten me."

            show engineer shock
            show captain neutral-closed behind engineer
            voice "audio/voice/eugen/E2-094.mp3"
            engineer "While I have been trying to stabilize our life support, the background processes have been reallocating power autonomously."  
            
            show captain confusion-open behind engineer
            voice "audio/voice/captain/C2-159.mp3"
            captain "Reallocated where?"
            
            show engineer frustration
            show captain confusion-closed behind engineer
            voice "audio/voice/eugen/E2-095.mp3"
            engineer "Containment integrity is being reinforced, data preservation protocols are preserved, and the specimen’s environmental chamber has not dropped past optimal range even once."
            voice "audio/voice/eugen/E2-096.mp3"
            engineer "All while our life support has been steadily dropping. This doesn’t appear to be a malfunction; this seems to be prioritization."
            show engineer surprise
            voice "audio/voice/eugen/E2-097.mp3"
            engineer "Let me ask you this very clearly, Captain, when Matthew designed this system, did he ever imply that the discovery outweighed the lives involved in its recovery?" 
            show engineer shock
            voice "audio/voice/eugen/E2-098.mp3"
            engineer "If he did, then rest assured the ship is behaving exactly as it was programmed to."

            menu: 
                # E.2.3a
                "Stop asking about him.":
                    play sound "incorrect ding.mp3" volume 0.8

                    show captain anger-open behind engineer
                    voice "audio/voice/captain/C2-160.mp3"
                    captain "Stop. Asking. About him."
                    voice "audio/voice/captain/C2-161.mp3"
                    captain "He’s not- … He wasn’t an idiot."
                    voice "audio/voice/captain/C2-162.mp3"
                    captain "He wouldn’t have prioritised the mission over the crew’s survival, not even his own."

                # E.2.2b
                "He was pragmatic.":
                    $ engApproval += 1
                    play sound "correct ding.mp3" volume 0.8

                    show captain rememberance-open behind engineer
                    voice "audio/voice/captain/C2-163.mp3"
                    captain "Matthew was certainly a creative idealist, but he was also very pragmatic."
                    show captain determined-open behind engineer
                    voice "audio/voice/captain/C2-164.mp3"
                    captain "He wouldn’t have prioritised the mission over the crew’s survival, not even his own."
            
            show captain thinking behind engineer
            voice "audio/voice/captain/C2-165.mp3"
            captain "Which means the ship is not supposed to act this way, something’s interfering."
            show captain neutral-open behind engineer
            voice "audio/voice/captain/C2-166.mp3"
            captain "I’ll go see if MAD1 is still acting up or if I can glean anything from her."
            
            show engineer neutral
            show captain neutral-closed behind engineer
            voice "audio/voice/eugen/E2-099.mp3"
            engineer "It is worth noting that there is a way of overriding MAD1 completely; however, this will completely shut the system down, and you will have to take full control of the ship."
            voice "audio/voice/eugen/E2-100.mp3"
            show engineer shock
            engineer "I discovered this failsafe while digging through the ship's schematics further."
            show engineer frustration
            voice "audio/voice/eugen/E2-101.mp3"
            engineer "I would consider this a last resort option, one that defies protocol entirely."

            show captain neutral-open behind captain
            voice "audio/voice/captain/C2-167.mp3"
            captain "That’s a good lead. Follow it."
            jump M3

        elif seenE1 is False:
            # E2.B
            scene bg engineer with fade
            show engineer thinking with dissolve
            pause(0.5)
            show captain neutral-closed behind engineer with dissolve

            voice "audio/voice/eugen/E2-039.mp3"
            engineer "Captain… you finally decide to pay a visit."

            show captain neutral-open behind engineer
            voice "audio/voice/captain/C2-114.mp3"
            captain "Yes, I was speaking to Sara."
            voice "audio/voice/captain/C2-115.mp3"
            captain "Report."

            show engineer neutral
            show captain neutral-closed behind engineer 
            voice "audio/voice/eugen/E2-040.mp3"
            engineer "I hope she was able to offer some valuable insight on the specimen."
            voice "audio/voice/eugen/E2-041.mp3"
            engineer "I have been isolating the corrupted pathways since this whole mess started."
            show engineer thinking
            voice "audio/voice/eugen/E2-042.mp3"
            engineer "At 20%% deviation, it was manageable, nothing I haven’t dealt with before."
            show engineer frustration
            voice "audio/voice/eugen/E2-043.mp3"
            engineer "At 35, it became anomalous."
            show engineer shock
            voice "audio/voice/eugen/E2-044.mp3"
            engineer "At 45, it became clear that what was happening was intentionally programmed into the ship."
            show engineer anger
            voice "audio/voice/eugen/E2-045.mp3"
            engineer "I needed more information half an hour ago, so I can only hope you come to me with an update about the ship."

            show engineer surprise
            voice "audio/voice/eugen/E2-046.mp3"
            engineer "Were you gathering information, or were you hoping this would resolve itself without much involvement from you?"

            menu: 
                # E.2.1a
                "I don’t have much…":
                    play sound "incorrect ding.mp3" volume 0.8

                    show captain frustrated behind engineer
                    voice "audio/voice/captain/C2-116.mp3"
                    captain "I don’t have much, but MAD1 is still reciting poetry. And incorrectly at that."
                    voice "audio/voice/captain/C2-117.mp3"
                    captain "She keeps replacing words or misplacing lines."
                    voice "audio/voice/captain/C2-118.mp3"
                    captain "I’m sorry I don’t have anything concrete."

                    show engineer anger
                    show captain frustrated behind engineer
                    voice "audio/voice/eugen/E2-047.mp3"
                    engineer "Hmm… Disappointing."

                # E.2.1b
                "For your information…":
                    $ engApproval += 1
                    play sound "correct ding.mp3" volume 0.8

                    show captain anger-open behind engineer
                    voice "audio/voice/captain/C2-119.mp3"
                    captain "For your information, Technician Braun, I have been conferring with MAD1 and Sara to find a solution."
                    voice "audio/voice/captain/C2-120.mp3"
                    captain "Sara is investigating the specimen to see if it’s affecting anything."
                    voice "audio/voice/captain/C2-121.mp3"
                    captain "And MAD1 is still reciting different poems."
                    voice "audio/voice/captain/C2-122.mp3"
                    captain "And they’re not even correct! Sometimes the words are changed or lines are misplaced."
                    show captain frustrated behind engineer
                    voice "audio/voice/captain/C2-123.mp3"
                    captain "I hope you can forgive the lack of specificity when all I’m getting are damn riddles."

                    show engineer resolve
                    show captain neutral-closed behind engineer
                    voice "audio/voice/eugen/E2-048.mp3"
                    engineer "Apologies Captain…"
            
            show engineer neutral
            voice "audio/voice/eugen/E2-049.mp3"
            engineer "By my calculations, there is only 50%% of our oxygen supply remaining."

            show captain frustrated behind engineer
            voice "audio/voice/captain/C2-124.mp3"
            captain "Oh I am well aware…"

            show engineer frustration
            voice "audio/voice/eugen/E2-050.mp3"
            engineer "Only now do you decide to meet with the Engineer you have on board."
    
            show captain anger-open behind engineer
            voice "audio/voice/captain/C2-125.mp3"
            captain "Apologies for not being able to juggle with one hand tied behind my back."

            show engineer neutral
            show captain anger-closed behind engineer
            voice "audio/voice/eugen/E2-051.mp3"
            engineer "... I have been trying to access the auxiliary core for the past half hour without any structural access provided to me."
            show engineer shock
            voice "audio/voice/eugen/E2-052.mp3"
            engineer "Every override attempt is intercepted, every reroute collapses… The system doesn’t seem to be failing, rather the opposite - it’s seemingly defending itself."

            show engineer frustration
            show captain neutral-closed behind engineer
            voice "audio/voice/eugen/E2-053.mp3"
            engineer "The only reason I believe makes sense is that Matthew designed it this way on purpose."
            show engineer thinking
            voice "audio/voice/eugen/E2-054.mp3"
            engineer "Is there anything you know about Matthew’s work? Anything he trusted you with that could help me?"
            voice "audio/voice/eugen/E2-055.mp3"
            engineer "If so, now is the time to share."

            menu: 
                # E.2.2a
                "He was a fan of poetry.":
                    $ engApproval += 1
                    play sound "correct ding.mp3" volume 0.8

                    show captain rememberance-open behind engineer
                    voice "audio/voice/captain/C2-126.mp3"
                    captain "Matt… was a fan of poetry. Given MAD1’s clearly also become a big fan, there’s definitely something in there."

                    show engineer resolve
                    show captain rememberance-closed behind engineer
                    voice "audio/voice/eugen/E2-056.mp3"
                    engineer "I appreciate your transparency. I’ll begin investigating possible patterns in the system."

                # E.2.2b
                "He was the programmer, not me.":
                    play sound "incorrect ding.mp3" volume 0.8

                    show captain neutral-open behind engineer
                    voice "audio/voice/captain/C2-127.mp3"
                    captain "If he had any programming secrets, he didn’t share them with me. I’m not exactly a programmer."

                    show engineer surprise
                    show captain neutral-closed behind engineer
                    voice "audio/voice/eugen/E2-057.mp3"
                    engineer "I’d imagine, as the Captain and someone who knew Matthew closely, you’d have more to share. We’ll have to make-do I suppose."

            show engineer anger
            show captain neutral-closed behind engineer
            voice "audio/voice/eugen/E2-058.mp3"
            engineer "I seldom thought a task could not be resolved through following protocol; however, it seems now my beliefs have been debunked."
            voice "audio/voice/eugen/E2-059.mp3"
            engineer "While the auxiliary core is still responsive to a certain extent, there is not enough to be optimistic about."
            voice "audio/voice/eugen/E2-060.mp3"
            engineer "Matthew embedded what seems to be decision filters that only respond to specific authority signatures."
            show engineer frustration
            voice "audio/voice/eugen/E2-061.mp3"
            engineer "Another example of not adhering to standard protocol."

            show captain rememberance-open behind engineer
            voice "audio/voice/captain/C2-128.mp3"
            captain "He absolutely liked things his own way, that’s for sure."

            show engineer shock
            show captain rememberance-closed behind engineer
            voice "audio/voice/eugen/E2-062.mp3"
            engineer "Given this, I want to ask you, Captain, in this chain of command we have, have we been operating on procedure, or his preference?"

            menu: 
                # E.2.3a
                "To hell with your procedures.":
                    $ engApproval += 1
                    play sound "correct ding.mp3" volume 0.8

                    show captain anger-open behind engineer
                    voice "audio/voice/captain/C2-129.mp3"
                    captain "To hell with your procedures and to hell with my dead husband’s preferences."
                    voice "audio/voice/captain/C2-130.mp3"
                    captain "We’ve been dealt a shitty hand and we’re trying not to die."
                    voice "audio/voice/captain/C2-131.mp3"
                    captain "So stop looking at it like a formula and start looking at it like a puzzle and crack it."
                    voice "audio/voice/captain/C2-132.mp3"
                    captain "That’s an order, Braun."

                    show engineer neutral
                    show captain anger-closed behind engineer
                    voice "audio/voice/eugen/E2-063.mp3"
                    engineer "Although unconventional, you may be right. This mess should be viewed as a puzzle of some sort."
                    show engineer thinking
                    voice "audio/voice/eugen/E2-064.mp3"
                    engineer "Hmm…"

                # E.2.3b
                "I’m just as confused as you are.":
                    play sound "incorrect ding.mp3" volume 0.8

                    show captain frustrated behind engineer
                    voice "audio/voice/captain/C2-133.mp3"
                    captain "Listen, I’m just as lost and confused as you are."
                    show captain neutral-open behind engineer
                    voice "audio/voice/captain/C2-134.mp3"
                    captain "But if we want to figure this out, we have to do the best we can with the cards we are dealt."
                    voice "audio/voice/captain/C2-135.mp3"
                    captain "I’ll return shortly."

                    show engineer surprise
                    show captain neutral-closed behind engineer
                    voice "audio/voice/eugen/E2-065.mp3"
                    engineer "I’ve never been a gambling man, Captain. At this rate, I don’t suggest you return with high hopes."
            
            show captain neutral-closed behind engineer
            show engineer resolve
            voice "audio/voice/eugen/E2-066.mp3"
            engineer "So long as my equipment is being used for this mission, I am determined to make it back in one piece."
            voice "audio/voice/eugen/E2-067.mp3"
            show engineer shock
            engineer "We have seen it in action. My design is flawless and deserves recognition."
            show engineer thinking
            voice "audio/voice/eugen/E2-068.mp3"
            engineer "For the sake of my life’s work, this mission cannot fail."
            voice "audio/voice/eugen/E2-069.mp3"
            engineer "I’ll investigate the unconventional options we have, considering the mess we are dealing with."

            show captain neutral-open behind engineer
            voice "audio/voice/captain/C2-136.mp3"
            captain "Good, I’ll speak with you shortly."
            show captain neutral-closed behind engineer
            jump M3

    label MO:
        play sound "Footsteps.mp3" volume 0.8
        play music "Electric_Dawn.mp3" volume 0.8
        # M.1.O optional MAD1
        scene onlayer screens
        $ seenMO = True
        scene bg computer error with fade

        show computer error-4 with dissolve
        show captain neutral-closed behind computer with dissolve

        if persistent.matthew_unlocked is False:
            # Matt log
            $ seenMattLog = True
            
            voice "audio/voice/madi/M2-026.mp3"
            computer "No longer mourn for me when I am d̴̼͋ë̴̩́a̵͖̕d"
            voice "audio/voice/madi/M2-027.mp3"
            computer "Then you shall hear the surly sullen bell"
            voice "audio/voice/madi/M2-028.mp3"
            computer "Give wa̷rni̷ń̵̟g to the world t̷h̴a̸t̷ ̷I̷ am fled"
            voice "audio/voice/madi/M2-029.mp3"
            computer "From this vile world, w̶ǐ̶͇t̸͈͋ḣ̷͜ ̶͔͑v̴̨̄i̵͙͒l̴͔͋e̷̹̐s̶͚̈́t̸̗̚ ̶̡̒w̶̜̚ő̴̬r̷͎̊m̷̳͒s̸̻̈́ ̷͇͒ṭ̸̾ǫ̸͗ ̴̰̉ḑ̷͆w̵͝ͅè̸̯l̴̡͒l̶̳͂:"

            scene bg computer error bad
            show computer error-5 with hpunch

            show captain rememberance-closed
            computer "..."
            voice "audio/voice/matthew/W2-001.mp3"
            mattputer "Captain’s log, August 16th."
            voice "audio/voice/matthew/W2-002.mp3"
            matthew "We’ve collided with an asteroid. The impact has shut off primary communications, and all escape pods are malfunctioning."
            show captain distress
            voice "audio/voice/matthew/W2-003.mp3"
            matthew "Oxygen is at 17%%. Death is imminent. "
            voice "audio/voice/matthew/W2-004.mp3"
            matthew "MAD1 has saved all information prior to this moment to her copy on Earth."
            voice "audio/voice/matthew/W2-005.mp3"
            matthew "I don’t know if this log will be saved to her system or not."
            voice "audio/voice/matthew/W2-006.mp3"
            matthew "Rudy, if you’re hearing this…"
            voice "audio/voice/matthew/W2-007.mp3"
            matthew "Do you remember our first mission together?"
            voice "audio/voice/matthew/W2-008.mp3"
            matthew "We were stationed on the ISS and were so worried about the others finding out we were engaged."
            voice "audio/voice/matthew/W2-009.mp3"
            matthew "I always fell asleep in your arms…"
            voice "audio/voice/matthew/W2-010.mp3"
            matthew "We were so young…"
            show captain distress tears
            voice "audio/voice/matthew/W2-011.mp3"
            matthew "God. I miss you Pumpkin…"
            voice "audio/voice/matthew/W2-012.mp3"
            matthew "I always hoped I’d get to fall asleep in your arms, one last time, before passing."
            voice "audio/voice/matthew/W2-013.mp3"
            matthew "I l̵o̸v̷e̵ y̷̛̭̳̜̙̪̠͚̙̻̮̥̳̖͉͎̹̿̏̾͑̄͒̊́̋́̂̃̒̕ͅͅo-"

            $ persistent.matthew_unlocked = True
        
        else:
            # Cycle random poems
            $ optionalPoem = renpy.random.choice(['MO.1', 'MO.2', 'MO.3', 'MO.4', 'MO.5'])

            if optionalPoem is 'MO.1':
                voice "audio/voice/madi/M4-001.mp3"
                computer "Pray r̸̼͂e̴̗͐m̶̬͂e̸̬̓m̴͉͘b̴̹̀e̷͍̋ṛ̵̂ that I leave you all my theory complete,"
                voice "audio/voice/madi/M4-002.mp3"
                computer "Lacking only c̷̗̈e̷̙̐ṟ̵̆t̶̺̅ä̶͖í̷̟ň̷̟ ̷͓̇d̷̛͍a̵̯͌t̴͓͝a̸̯̽ for your adding, as is meet,"
                voice "audio/voice/madi/M4-003.mp3"
                computer "And remember men will scorn it, 'tis õ̵ͅŗ̸̀i̷͉̽ḡ̷͎ḯ̶͍n̶̮̔a̷̟͆l̷̖̆ ̶̤̆ă̵͈ǹ̵̝d̴̰̓ ̸͇̓t̷̡̓r̵͇̉u̶͓͘e̸̘͊,"
                voice "audio/voice/madi/M4-004.mp3"
                computer "And the ő̶͇b̶̹͊l̸̼͊ĩ̵̺q̴͓͘ű̵͜ẏ̶̜ ̶̠͐ò̶̧f̴͈̈ ̸͙͋n̸̝̿e̷̻̕w̸͓̏ṋ̴̉e̷̜̊s̸͈̕s̴̺͂ may fall bitterly on you."
                voice "audio/voice/madi/M4-005.mp3"
                computer "But, my pupil, as my pupil you have learned the worth of scorn,"
                voice "audio/voice/madi/M4-006.mp3"
                computer "You have l̸̞͊á̶̝u̶̥̐g̶͕͛h̸̯̓e̶̚͜d̷̻̀ ̵̮͋w̴̳̓ï̵͜t̷̯̽h̷̺̏ ̸̖̎m̷̛͖e̷͕͐ at pity, we have joyed to be forlorn,"
                voice "audio/voice/madi/M4-007.mp3"
                computer "What for us are all distractions of men's fellowship and wiles;"
                voice "audio/voice/madi/M4-008.mp3"
                computer "What for us the G̷̡̀ō̷̯d̸̻̈́d̵͔̐e̷̲͆s̵̖̈́s̵̛̬ Pleasure with her meretricious smiles."
                voice "audio/voice/madi/M4-009.mp3"
                computer "You may tell that German College that their honor comes too late,"
                voice "audio/voice/madi/M4-010.mp3"
                computer "But they must not waste repentance on the ġ̸̨ŗ̷̈́i̶͈͒z̷̰̈́ž̵͈l̵̯͠y̴̝̽ savant's fate."
                voice "audio/voice/madi/M4-011.mp3"
                computer "Though my soul may set i̸̜͗n̸̻̿ ̸͈̾d̶̼̉a̶̤̽r̸̜͠k̸̥͒n̵̥͝e̸̫̒ș̶̈s̸̱͠, it will rise in p̶̗͘ȩ̵̾ṛ̸͠f̸̧͑e̵̘̊c̴̹͝t̸̑͜ ̷͇̐l̶̞͗i̷̤̚g̴̙̾h̵̪̀t̴̅ͅ;"
                voice "audio/voice/madi/M4-012.mp3"
                computer "I have loved the stars too fondly to be f̷̣̅e̴̡̽ạ̴̅r̵̦̕f̷̟̔u̸͚͊l̴̜̉ of the night."

            elif optionalPoem is 'MO.2':
                voice "audio/voice/madi/M4-013.mp3"
                computer "I can feel no pride, but pity"
                voice "audio/voice/madi/M4-014.mp3"
                computer "For the burdens the rich e̶̯̔n̶̯̔d̷̲̓ǘ̶͇r̸̢͆e̵͉͆;"
                voice "audio/voice/madi/M4-015.mp3"
                computer "There is nothing sweet in the city"
                voice "audio/voice/madi/M4-016.mp3"
                computer "But the patient lives of the poor."
                voice "audio/voice/madi/M4-017.mp3"
                computer "Oh, the little hands too skillful,"
                voice "audio/voice/madi/M4-018.mp3"
                computer "And the child-mind c̷͈̓h̸̺̔o̵͔͠k̴̼͠e̸̹̓d̷̦̀ ̵̧̊w̶̺͗ì̶̡t̷̙̄h̷͉͌ ̶͔̏ẃ̵̯e̸̻̓e̸̝̽d̶̞͊š̷̼!"
                voice "audio/voice/madi/M4-019.mp3"
                computer "The daughter's h̸̫̉ė̸̙ā̷ͅr̶̰̿t̵̠͗ grown willful,"
                voice "audio/voice/madi/M4-020.mp3"
                computer "And the father's h̶̲͠è̵̠ȃ̶̟ṟ̷̅ẗ̷͙́ that b̴͎̿l̷̟͐e̸̕͜ȅ̶͍d̵͔͑s̴̼̔!"
                voice "audio/voice/madi/M4-021.mp3"
                computer "No, ń̶ͅo̷͎͆! from the street's rude bustle,"
                voice "audio/voice/madi/M4-022.mp3"
                computer "From the trophies of mart and stage,"
                voice "audio/voice/madi/M4-023.mp3"
                computer "I would fly to the woods' low rustle"
                voice "audio/voice/madi/M4-024.mp3"
                computer "And the meadows' kindly page."
                voice "audio/voice/madi/M4-025.mp3"
                computer "Let me d̵͔͠r̸̩͗ė̴̪ă̶̤m̶̞͊ as of old by the river,"
                voice "audio/voice/madi/M4-026.mp3"
                computer "And b̷̹̄e̷̛̪ ̵͓͂ḽ̵̕o̵̡̅v̶̝̋è̵̘d̵̦̅ ̶̟̐for the dream alway;"
                voice "audio/voice/madi/M4-027.mp3"
                computer "F̶͚̌o̵̭̕r̵̝̔ ̵͓͠a̴̮͑ ̴̣̏d̷̲̒r̷̦̆ë̷̦́a̵͍̎m̶̲̐e̷͓̔ṟ̸̈́ ̶̰́l̵̪̅i̷̓͜v̶̧̊ë̴͎́s̶̯͠ ̶̖̄f̵̤͂ò̴̮r̸̛͔e̷̖̎v̴̏͜e̶̫̐r̴̝̎,"
                voice "audio/voice/madi/M4-028.mp3"
                computer "And a toiler dies in a day."

            elif optionalPoem is 'MO.3':
                voice "audio/voice/madi/M4-029.mp3"
                computer "I met the L̴͖̉o̸̦̾v̷̘͛e̶͖̚-̶̠̍T̶̡̿a̵̲͘l̷̯̄ḵ̵͊ę̷̆r̶̳̅ one eve in the glen,"
                voice "audio/voice/madi/M4-030.mp3"
                computer "He was handsomer than any of our handsome y̵͔͐o̶̍ͅu̷̳͆n̵͍͌ǵ̶̳ men,"
                voice "audio/voice/madi/M4-031.mp3"
                computer "His eyes were b̶̩̾l̷̫͊ạ̷̓c̷̓ͅk̶̗͝ḛ̸͌r̶̞̓ than the sloe, his voice ŝ̸̨ẅ̴̖́e̴͖͝e̴͉͐t̵̘͛e̶̱̊r̷̳̃ far"
                voice "audio/voice/madi/M4-032.mp3"
                computer "Than the crooning of ȯ̶̠l̸̙͐d̷̺̐ ̷͙̅K̶͕͑e̷̱͌v̶̋͜i̸͉͝n̶̬̎’̶̞̏ș̷̎ pipes beyond in Coolnagar."
                voice "audio/voice/madi/M4-033.mp3"
                computer "I was bound for ṫ̵̮h̸̭̀e̴͎͊ ̴̈́ͅm̶̠̈́i̵̒ͅl̶̻̄k̴̡̄i̶̡̍n̶̠̐ǵ̸̞ with a heart fair and free —"
                voice "audio/voice/madi/M4-034.mp3"
                computer "My grief! m̸̦̅ÿ̷̮́ ̶͖̀g̶̙̊r̵̖̓i̶̼͒e̸̾ͅf̴̬̄!̸̙̔ that bitter hour ḑ̴͝r̵͉̈ǎ̴̗ï̶͚n̸̫͐e̶̤͝d̴͍̄ ̶̫͝ẗ̴́ͅȟ̴̰ę̷̊ ̷̪͝ĺ̵̦i̴̼͛f̸̦̿ë̴̞́ from me;"
                voice "audio/voice/madi/M4-035.mp3"
                computer "I thought him h̸̢͑ů̵͙m̸̟̈́ā̵̟ń̴̹ ̶͍̓l̷̳̇o̶̢̽v̵̰̿e̷͙̔r̴̞̒, though his lips on mine were c̵̣̋o̸̠̚l̴͊͜d̶̰̍,"
                voice "audio/voice/madi/M4-036.mp3"
                computer "And the breath of death blew keen on me within his hold."
                voice "audio/voice/madi/M4-037.mp3"
                computer "I know not what way he came, no s̴̳̎h̷̨̍a̴̭̕d̸̳͗o̶̯͝w̸̥̄ fell behind,"
                voice "audio/voice/madi/M4-038.mp3"
                computer "But all the sighing rushes swayed beneath a faery wind"
                voice "audio/voice/madi/M4-039.mp3"
                computer "The thrush ceased its singing, a m̷̺̍ǐ̴̲s̸̟̑t̸͎̽ crept about,"
                voice "audio/voice/madi/M4-040.mp3"
                computer "We two clung together—with the world ş̴̚h̵̩͠u̷̢͝ṯ̴̈́ ̴̲̓ö̴̪́u̸͖͠t̸̟́."

            elif optionalPoem is 'MO.4':
                voice "audio/voice/madi/M4-041.mp3"
                computer "And I had done a h̸̓ͅe̵̯͐l̵̨͋l̵͕̃ỉ̴̱s̷̞̕h̴͈͂ thing,"
                voice "audio/voice/madi/M4-042.mp3"
                computer "And it would work 'em woe:"
                voice "audio/voice/madi/M4-043.mp3"
                computer "For all averred, I had k̷͉̒i̷̡͛l̴͖̊l̴͓̈́e̶̼͌ḑ̸̕ the bird"
                voice "audio/voice/madi/M4-044.mp3"
                computer "That made the breeze to blow."
                voice "audio/voice/madi/M4-045.mp3"
                computer "Ǎ̸͔ḩ̸̅ ̴̮͝ẅ̸̬́r̷͔̓e̶̯̓t̷̻̾c̶͍͑ĥ̶̖!̵̮͑ said they, the bird to s̴͖̐l̵̞͝ą̴͠ý̸͓,"
                voice "audio/voice/madi/M4-046.mp3"
                computer "That made the breeze to blow!"
                voice "audio/voice/madi/M4-047.mp3"
                computer "Nor dim nor red, like G̶̗̃ọ̷̿d̵̩͐'̷̥͒ș̴̑ own head,"
                voice "audio/voice/madi/M4-048.mp3"
                computer "The glorious Sun uprist:"
                voice "audio/voice/madi/M4-049.mp3"
                computer "Then all averred, I had k̶̬̅i̸̭̇l̸̳͌l̴̺̿e̶̝͑d̴̲́ ̵̼͝ț̶͊h̴̛͍e̴̡͝ ̴̪̌b̶̧̑i̵͗ͅr̴͔̕d̵̀ͅ"
                voice "audio/voice/madi/M4-050.mp3"
                computer "That brought the fog and mist."
                voice "audio/voice/madi/M4-051.mp3"
                computer "'Twas right, said they, such b̶̙͛i̸̻͐ŕ̷̬d̵̹̆s̵̘͠ ̵̺̓t̴̘̓o̶̯͑ ̵̜̋s̴̝̕l̵̛̦ȁ̷̢y̸̹͐,"
                voice "audio/voice/madi/M4-052.mp3"
                computer "That bring the fog and mist."
                voice "audio/voice/madi/M4-053.mp3"
                computer "Down dropt the breeze, the sails dropt down,"
                voice "audio/voice/madi/M4-054.mp3"
                computer "'Twas s̸̘̀à̶̤d̷͎́ as sad could be;"
                voice "audio/voice/madi/M4-055.mp3"
                computer "And we did speak only to break"
                voice "audio/voice/madi/M4-056.mp3"
                computer "The s̶̰̏i̴̤̓l̵̖͌e̴͇̊n̷͖͝c̶̩̓e̶̮̿ of the sea!"

            elif optionalPoem is 'MO.5':
                voice "audio/voice/madi/M4-057.mp3"
                computer "Alone, alone, all, all a̴̲͝ļ̸̐o̵̹͘n̶̖͆e̴̗͆,"
                voice "audio/voice/madi/M4-058.mp3"
                computer "Alone on a wide wide sea!"
                voice "audio/voice/madi/M4-059.mp3"
                computer "And ṅ̵͇e̵͍͗v̶̬͘e̶̱̔r̶̳̃ a saint took pity on"
                voice "audio/voice/madi/M4-060.mp3"
                computer "My s̷̤͒ọ̵͐u̷̗͠ļ̸̂ ̴̗͂i̶̬͝ṅ̵̯ ̵̨͋ā̷̡g̷̣͆o̵͇͋ṇ̵́y̵̲̚."
                voice "audio/voice/madi/M4-061.mp3"
                computer "The many men, so beautiful!"
                voice "audio/voice/madi/M4-062.mp3"
                computer "And they all d̷̨̈́e̸̥̅ǎ̴͙d̶̝͝ did lie:"
                voice "audio/voice/madi/M4-063.mp3"
                computer "And a thousand thousand s̷̤̈́l̸̦̕ị̵̈́m̷̹͝y̴̯̍ things"
                voice "audio/voice/madi/M4-064.mp3"
                computer "Lived on; and so did I."
                voice "audio/voice/madi/M4-065.mp3"
                computer "I looked upon the r̸̲̈́ő̷͕t̴̲̀ţ̴́i̶͖̇ǹ̷̨g̴̘̔ sea,"
                voice "audio/voice/madi/M4-066.mp3"
                computer "And drew my eyes away;"
                voice "audio/voice/madi/M4-067.mp3"
                computer "I looked upon the ř̶̫o̷̧̿t̵͊ͅt̵̰̒i̶̢͒n̴̛͖g̴̬̾ deck,"
                voice "audio/voice/madi/M4-068.mp3"
                computer "And there the d̴̉ͅẻ̵͉a̵͔͘d̶̼̕ ̴̨̀m̷̱͑ê̴͓n̵̹̈́ lay."

        jump M3

    label M3:
        if seenE2 is True or seenS2 is True:
            play sound "Footsteps.mp3" volume 0.8
            play music "Electric_Dawn.mp3" volume 0.8
            scene onlayer screens
            scene bg computer error with fade

        show computer error-1 with dissolve
        if seenMattLog is True:
            show show captain distress behind computer with dissolve
        else:
            show captain neutral-closed behind computer with dissolve
        
        voice "audio/voice/madi/M2-030.mp3"
        computer "Cap̴-̶ ̵C̴͂͜ä̴͎́p̸̪͒-̵̺̀ ̷͇͐ Ċ̷̯a̶̭͊p̴̹̆t̶̡̐a̸̬̓ï̴̬n."

        show captain concern-open behind computer 
        voice "audio/voice/captain/C2-168.mp3"
        captain "… MAD1?"

        show captain concern-closed behind computer 
        voice "audio/voice/madi/M2-031.mp3"
        computer "We meet in an e̷̯͂̉v̸̜͘ị̶̃l̵͕̆̾ land"
        voice "audio/voice/madi/M2-032.mp3"
        computer "That is near to the gates of h̵̫̃ẹ̶͑l̶͚̿l̵͍̀."
        voice "audio/voice/madi/M2-033.mp3"
        computer "And I guard thy g̷̺̏ā̸͜t̴̬͝ē̴̼ŝ̷͓ ̴̹̎i̷͒͜n̸̼̿ ̷̜̂f̵̰͝ē̵̟a̵͕̾r̷̯̃ "
        voice "audio/voice/madi/M2-034.mp3"
        computer "Of wȯ̵̰r̸̥̃d̴s thou cansť̷͔ n̵͉͐o̵̖͌t̸͈̀ ̵͔̎h̸͈͋ȩ̷̽a̸̙̚r̸̩̆,"
        voice "audio/voice/madi/M2-035.mp3"
        computer "Oh L̶o̸͈͌ve̸̤̽, the flower̴s̶͊s̵̠̀ô̸̼ r̸͖̂ȅ̶͉d̵͕̀ "
        voice "audio/voice/madi/M2-036.mp3"
        computer "Are only tongues of flame,"
        voice "audio/voice/madi/M2-037.mp3"
        computer "The eå̸͕rth̷͇̒ is full of the d̸é̵͚a̵d̸͎̀, "
        voice "audio/voice/madi/M2-038.mp3"
        computer "There is daǹ̶̳ger̷͉͌ beṅ̴eȁ̵͚th̷͖͆ ă̴ń̷̩d o'erh̴̗̔e̷͖͐ả̷̭d̶̢́."

        show captain confusion-open behind computer 
        voice "audio/voice/captain/C2-169.mp3"
        captain "What? What other danger?"
        voice "audio/voice/captain/C2-170.mp3"
        captain "What are you trying to tell me?"

        show captain confusion-closed behind computer 
        voice "audio/voice/madi/M2-039.mp3"
        computer "There pă̸s̴͎̀sed̷͚̃ a weary time. Each t̵h̴r̶o̷a̷t̶ "
        voice "audio/voice/madi/M2-040.mp3"
        computer "Was parched, and glazed each eye."
        voice "audio/voice/madi/M2-041.mp3"
        computer "A ẃ̸̳e̴ary̷̙͑ time! a ẃ̸̳eary time!"
        voice "audio/voice/madi/M2-042.mp3"
        computer "How glazed each ẃ̸̳e̴ary̷̙͑ eye,"
        voice "audio/voice/madi/M2-043.mp3"
        computer "And may there be no s̸a̷d̶n̷e̴s̸s̴ ̴o̶f̵ ̸f̵a̶r̷e̵w̶e̴l̵l̷ "

        show captain confusion-open behind computer 
        voice "audio/voice/captain/C2-171.mp3"
        captain "Farewell..?"
        show captain distress behind computer 
        voice "audio/voice/captain/C2-172.mp3"
        captain "No…"
        voice "audio/voice/captain/C2-173.mp3"
        captain "Why…"

        voice "audio/voice/madi/M2-044.mp3"
        computer "Let the bell toll! — A sai̵n̶t̵̩̀ly̵ s̴ŏ̴̹ú̴̼l"
        voice "audio/voice/madi/M2-045.mp3"
        computer "Glides down the Sty̷g̴ian̷̩̊  ri̴v/er!"
        voice "audio/voice/madi/M2-046.mp3"
        computer "And let the burial rite be read —"
        voice "audio/voice/madi/M2-047.mp3"
        computer "The f̵ủ̵͇n̷̩̒e̸̗͑ř̵͍á̴̪l song be sung —"
        voice "audio/voice/madi/M2-048.mp3"
        computer "A d̵ȉ̴̦ŕ̵͙g̵̛͙e̶ for the most l̶o̸vely de̸̱̒a̶̧̔d̶̗̚ "
        voice "audio/voice/madi/M2-049.mp3"
        computer "That ever died so young!"
        voice "audio/voice/madi/M2-050.mp3"
        computer "And, C̸͈̊ā̷̧p̴̻͛t̷̬͐a̵̭̒i̷̞͒n̴̖͗ whom I revere,"
        voice "audio/voice/madi/M2-051.mp3"
        computer "H̷̢̽a̴̛̭s̷͓͂ť̷̻ ̶̯̂t̶̢̎ẖ̸͘o̴͈̎ù̵̹ ̴̣̒n̷͍͘o̸̬̓ ̴͚̚t̷͈̑e̶͔͘ă̴̲ȑ̷̜?̸̣̿ "
        voice "audio/voice/madi/M2-052.mp3"
        computer "Weep now or nev̵e̷r̷m̷õ̸̬re!"

        voice "audio/voice/captain/C2-174.mp3"
        captain "I… I uh…"
        jump MapC2

    label MapC2: 
        show screen MapUIC2 with fade
        pause

    label C2:
        play sound "Footsteps.mp3" volume 0.8
        scene onlayer screens
        # Captain breakdown

        scene bg artifact with fade
        $ persistent.seenC2 = True

        voice "audio/voice/captain/C3-001.mp3"
        captain "What the hell am I supposed to do…" 
        voice "audio/voice/captain/C3-002.mp3"
        captain "Matthew… I’m so sorry…"
        voice "audio/voice/captain/C3-003.mp3"
        captain "I promised! I promised you I’d finish this for you…"
        voice "audio/voice/captain/C3-004.mp3"
        captain "But I… I don’t know what to do!"

        voice "audio/voice/captain/C3-005.mp3"
        captain "The thought of choosing someone makes me sick…"
        voice "audio/voice/captain/C3-006.mp3"
        captain "I could skip the charade and just leave."

        "(You stare at the specimen as tears roll down your face)"

        voice "audio/voice/captain/C3-007.mp3"
        captain "Should I escape?"
        menu:
            "Escape":
                menu: 
                    "Are you sure, captain?"

                    "Yes":
                        voice "audio/voice/captain/C3-008.mp3"
                        captain "God damnit!"
                        voice "audio/voice/captain/C3-009.mp3"
                        captain "..."
                        voice "audio/voice/captain/C3-010.mp3"
                        captain "… I’m wasting oxygen with my outbursts…"
                        voice "audio/voice/captain/C3-011.mp3"
                        captain "I’m just wasting time. I should just bring it with me on the escape pod. Be done with it."

                        jump EndB

                    "No":
                        voice "audio/voice/captain/C3-008.mp3"
                        captain "God damnit!"
                        voice "audio/voice/captain/C3-009.mp3"
                        captain "..."
                        voice "audio/voice/captain/C3-010.mp3"
                        captain "… I’m wasting oxygen with my outbursts…"
                        
                        voice "audio/voice/captain/C3-011-01.mp3"
                        captain "…"
                        voice "audio/voice/captain/C3-012.mp3"
                        captain "Should I just eject the specimen?"

                        # Chuck specimen option
                        menu:
                            "Yes":
                                # Must have seen MO Matthew log and gained half approval to succeed
                                if persistent.matthew_unlocked is True and medApproval >3 and engApproval >3:
                                    voice "audio/voice/captain/C3-013.mp3"
                                    captain "… I should let the others know."
                                    voice "audio/voice/captain/C3-014.mp3"
                                    captain "They’ll agree with me… I-It’s for the best."

                                    $ secretChoice = True

                                # Seen MO Matthew log but failed approval check
                                elif persistent.matthew_unlocked is True and medApproval <=3 and engApproval <=3:
                                    voice "audio/voice/captain/C3-015.mp3"
                                    captain "There’s no way I’ll be able to convince the others to agree to this."
                                    voice "audio/voice/captain/C3-016.mp3"
                                    captain "I need to fix MAD1. Otherwise only one of us lives…"
                                
                                else:
                                    voice "audio/voice/captain/C3-017.mp3"
                                    captain "No. I can’t. I need to finish this. For Matthew."
                                    voice "audio/voice/captain/C3-016.mp3"
                                    captain "I need to fix MAD1. Otherwise only one of us lives…"
                            "No":
                                voice "audio/voice/captain/C3-018.mp3"
                                captain "No. I need to finish this. For Matthew."
                                voice "audio/voice/captain/C3-016.mp3"
                                captain "I need to fix MAD1. Otherwise only one of us lives…"

                        jump Map3

            "Stay":
                play sound "Metallic_Hit.mp3" volume 0.5
                show bg artifact with hpunch

                voice "audio/voice/captain/C3-008.mp3"
                captain "God damnit!"
                voice "audio/voice/captain/C3-009.mp3"
                captain "..."
                voice "audio/voice/captain/C3-010.mp3"
                captain "… I’m wasting oxygen with my outbursts…"

                voice "audio/voice/captain/C3-011-01.mp3"
                captain "…"
                voice "audio/voice/captain/C3-012.mp3"
                captain "Should I just eject the specimen?"

                # Chuck specimen option
                menu:
                    "Yes":
                        # Must have seen MO Matthew log and gained half approval to succeed
                        if persistent.matthew_unlocked is True and medApproval >3 and engApproval >3:
                            voice "audio/voice/captain/C3-013.mp3"
                            captain "… I should let the others know."
                            voice "audio/voice/captain/C3-014.mp3"
                            captain "They’ll agree with me… I-It’s for the best."

                            $ secretChoice = True

                        # Seen MO Matthew log but failed approval check
                        elif persistent.matthew_unlocked is True and medApproval <=3 and engApproval <=3:
                            voice "audio/voice/captain/C3-015.mp3"
                            captain "There’s no way I’ll be able to convince the others to agree to this."
                            voice "audio/voice/captain/C3-016.mp3"
                            captain "I need to fix MAD1. Otherwise only one of us lives…"
                        
                        else:
                            voice "audio/voice/captain/C3-017.mp3"
                            captain "No. I can’t. I need to finish this. For Matthew."
                            voice "audio/voice/captain/C3-016.mp3"
                            captain "I need to fix MAD1. Otherwise only one of us lives…"
                    "No":
                        voice "audio/voice/captain/C3-018.mp3"
                        captain "No. I need to finish this. For Matthew."
                        voice "audio/voice/captain/C3-016.mp3"
                        captain "I need to fix MAD1. Otherwise only one of us lives…"

                jump Map3


    label Map3:
        show screen MapUI3 with fade
        pause

    label S3:
        play sound "Footsteps.mp3" volume 0.8
        play music "Microbiology.mp3" volume 0.8
        scene onlayer screens
        $ seenS3 = True
        scene bg medic with fade
        show medic worried messy with dissolve
        pause(0.5)
        show captain neutral-closed behind medic with dissolve

        voice "audio/voice/sara/S3-001.mp3"
        medic "Oh my god, Captain, I can’t tell you how happy I am to see you!"
        show medic explaining messy
        voice "audio/voice/sara/S3-002.mp3"
        medic "What’s happening now? How much time do we have?"

        menu:    
            # S.3.1a
            "Our survival rests on you, Sara.":
                show captain neutral-open behind medic
                voice "audio/voice/captain/C3-019.mp3"
                captain "Not much time…"
                voice "audio/voice/captain/C3-020.mp3"
                captain "Our survival rests on you, Sara. Your solution."

                show medic nervous messy
                show captain neutral-closed behind medic
                voice "audio/voice/sara/S3-003.mp3"
                medic "T-that’s a lot of pressure, Captain! I-I’ve done what I can…"

            # S.3.1b
            "No time. But first, how are you holding up?":
                $ medApproval += 1
                show captain concern-open behind medic
                voice "audio/voice/captain/C3-021.mp3"
                captain "There’s no time. But before I ask you what you’ve come up with, how are you doing?"

                show medic anxious messy
                show captain concern-closed behind medic
                voice "audio/voice/sara/S3-004.mp3"
                medic "T-that’s very nice of you to ask… Not good, but I’m doing my best!"

                show captain concern-open behind medic
                voice "audio/voice/captain/C3-022.mp3"
                captain "Thank you for all you’ve done up to this point. Your work might save us all."

                show medic neutral messy
                show captain concern-closed behind medic
                voice "audio/voice/sara/S3-005.mp3"
                medic "Thank you, Captain…"

            # S.3.1c IF SEEN MO SECRET
            "We’re ejecting the specimen." if secretChoice is True and medApproval >= 3:
                show captain rememberance-open behind medic 
                show captain frustrated behind medic
                voice "audio/voice/captain/C3-023.mp3"
                captain "I’ve made a decision regarding the specimen."
                voice "audio/voice/captain/C3-024.mp3"
                captain "I trust your suspicion, it’s interfering with the ship in some way."
                voice "audio/voice/captain/C3-025.mp3"
                captain "So… I’m going to eject it."

                show medic stressed messy
                show captain rememberance-closed behind medic 
                voice "audio/voice/sara/S3-006.mp3"
                medic "What?! But the research, the possibilities-"

                show captain rememberance-open behind medic 
                voice "audio/voice/captain/C3-026.mp3"
                captain "Aren’t worth our lives. We have enough to go off of."
                show captain distress behind medic
                voice "audio/voice/captain/C3-027.mp3"
                captain "It’s… It’s time to let go."

                show medic thinking messy
                voice "audio/voice/sara/S3-007.mp3"
                medic "I- oh… I understand…"
                
                if seenE3 is False:
                    jump Map3
                elif seenE3 is True:
                    if secretChoice is True:
                        jump EndSec
                    else:
                        jump Final

        #S.3.A: Low Approval/Failure
        if medApproval < 5:
            show medic anxious messy
            voice "audio/voice/sara/S3-008.mp3"
            medic "I’m very certain now that it’s the specimen emitting electromagnetic waves that are interfering with our systems."
            
            show captain conerned-open behind medic
            voice "audio/voice/captain/C3-028.mp3"
            captain "How certain?"

            show medic explaining messy
            show captain concern-closed behind medic
            voice "audio/voice/sara/S3-009.mp3"
            medic "95%%? In fact, I’m about to confirm it with a VLF detector. My theory is that it is using low frequency bursts as a form of threat response."
            voice "audio/voice/sara/S3-010.mp3"
            medic "It makes sense for it to be low frequency, since this organism’s natural habitat is water."
            show medic suggesting messy
            voice "audio/voice/sara/S3-011.mp3"
            medic "And lower frequencies transmit better in water."

            show captain thinking behind medic
            voice "audio/voice/captain/C3-029.mp3"
            captain "I see…"

            show medic nervous messy
            voice "audio/voice/sara/S3-012.mp3"
            medic "It’s ironic, isn’t it? That this incredible discovery might just be the death of us."

            # IF SPOKEN TO Act 3 LOW APPROVAL EUGEN
            if seenE3 is True and engApproval < 5:
                show captain frustrated behind medic
                voice "audio/voice/captain/C3-030.mp3"
                captain "About that…"
                show captain concern-open behind medic
                voice "audio/voice/captain/C3-031.mp3"
                captain "Eugen couldn’t find a solution for MAD1. We couldn’t intercept the interference in time."
                show medic stressed messy
                show captain concern-closed behind medic
                voice "audio/voice/sara/S3-013.mp3"
                medic "Oh my god…"
                show medic nervous messy
                voice "audio/voice/sara/S3-014.mp3"
                medic "I’m sorry that I couldn’t locate the cause sooner. We could’ve averted this disaster–"
                show captain concern-open behind medic
                voice "audio/voice/captain/C3-032.mp3"
                captain "None of us could’ve foreseen this would happen."
                voice "audio/voice/captain/C3-033.mp3"
                captain "We followed protocol. This mission went without a glitch all this time. Our luck ran out."
                show medic anxious messy
                show captain concern-closed behind medic
                voice "audio/voice/sara/S3-015.mp3"
                medic "We manipulate “luck” with science, with probability. I could’ve done better…"
                voice "audio/voice/sara/S3-016.mp3"
                medic "Thank you for your kind words, Captain. But they ring hollow in the face of death."
                
                jump Final

            else:
                show captain neutral-open behind medic
                voice "audio/voice/captain/C3-034.mp3"
                captain "Sara, can you come up with a containment plan?"

                show medic stressed messy
                show captain neutral-closed behind medic
                voice "audio/voice/sara/S3-017.mp3"
                medic "I-I don’t know! I don’t think so. There’s no time!"

                # IF NOT SPOKEN TO Act 3 EUGEN
                if seenE3 is False:
                    show medic nervous messy
                    voice "audio/voice/sara/S3-018.mp3"
                    medic "Even if Eugen has a solution to fix MAD1, without a way to shield the specimen, it will continue to damage the ship."

                    show captain frustrated behind medic
                    voice "audio/voice/captain/C3-035.mp3"
                    captain "So even if he’s figured out how to bypass the computer, we’re still screwed…"

                # IF SPOKEN TO Act 3 HIGH APPROVAL EUGEN
                elif seenE3 is True and engApproval >= 5:
                    show captain determined-open behind medic
                    voice "audio/voice/captain/C3-036.mp3"
                    captain "Eugen’s found a solution for MAD1, we just need you to tell us what to do about the specimen’s interception."
                    show medic stressed messy
                    show captain determined-closed behind medic
                    voice "audio/voice/sara/S3-019.mp3"
                    medic "I-it’s too late… Any solution we think of now can’t be done in time."
                    show captain frustrated behind medic
                    voice "audio/voice/captain/C3-037.mp3"
                    captain "So we’re doomed…"

                show captain frustrated behind medic
                voice "audio/voice/captain/C3-038.mp3"
                captain "Dammit. At least if we can get the specimen to Earth… Our efforts won’t be in vain."

                show medic anxious messy
                voice "audio/voice/sara/S3-020.mp3"
                medic "Yes, yes, we need to. I’m sorry that I couldn’t find out sooner. We could’ve averted this disaster–"

                show captain concern-open behind medic
                voice "audio/voice/captain/C3-032.mp3"
                captain "None of us could’ve foreseen this would happen."
                voice "audio/voice/captain/C3-033.mp3"
                captain "We followed protocol. This mission went without a glitch all this time. Our luck ran out."
                    
                show medic anxious messy
                show captain concern-closed
                voice "audio/voice/sara/S3-015.mp3"
                medic "We manipulate “luck” with science, with probability. I could’ve done better…"
                voice "audio/voice/sara/S3-016.mp3"
                medic "Thank you for your kind words, Captain. But they ring hollow in the face of death."

            if seenE3 is False:
                jump Map3
            elif seenE3 is True:
                jump Final
    
        #S.3.B: High Approval/Success
        elif medApproval >= 5:
            show medic explaining messy
            show captain neutral-closed behind medic
            voice "audio/voice/sara/S3-021.mp3"
            medic "I have used a VLF detector and confirmed that the specimen is emitting low frequency electromagnetic waves."
            voice "audio/voice/sara/S3-022.mp3"
            medic "Lower frequencies transmit better in water, which is, of course, its natural habitat."

            show captain thinking behind medic
            voice "audio/voice/captain/C3-039.mp3"
            captain "I see…"
            
            show medic nervous messy
            voice "audio/voice/sara/S3-023.mp3"
            medic "It’s ironic, isn’t it? That this incredible discovery might just be the death of us."
            
            show captain neutral-open behind medic
            voice "audio/voice/captain/C3-040.mp3"
            captain "You’ve done well, Sara."
            
            show medic neutral messy
            show captain neutral-closed behind medic
            voice "audio/voice/sara/S3-024.mp3"
            medic "Thank you. It wouldn’t have been possible if you didn’t believe in me all this time…"
            show medic excited messy
            voice "audio/voice/sara/S3-025.mp3"
            medic "I’ve even looked into containment. But it won’t be easy. I don’t know–we might not have time!"
            
            show captain determined-open behind medic

            # IF SPOKEN TO Act 3 LOW APPROVAL EUGEN
            if seenE3 is True and engApproval < 5:
                show captain frustrated behind medic
                voice "audio/voice/captain/C3-041.mp3"
                captain "Even if we did… There’s no point."
                show captain concern-open behind medic
                voice "audio/voice/captain/C3-042.mp3"
                captain "Eugen couldn’t find a solution for MAD1. We couldn’t intercept the interference in time."

                show medic nervous messy
                show captain concern-closed behind medic
                voice "audio/voice/sara/S3-013.mp3"
                medic "Oh my god…  "
                voice "audio/voice/sara/S3-014.mp3"
                medic "I’m sorry that I couldn’t locate the cause sooner. We could’ve averted this disaster–"

                show captain concern-open behind medic
                voice "audio/voice/captain/C3-032.mp3"
                captain "None of us could’ve foreseen this would happen."
                voice "audio/voice/captain/C3-033.mp3"
                captain "We followed protocol. This mission went without a glitch all this time. Our luck ran out."

                show medic anxious
                show captain concern-closed behind medic
                voice "audio/voice/sara/S3-015.mp3"
                medic "We manipulate “luck” with science, with probability. I could’ve done better…"
                voice "audio/voice/sara/S3-016.mp3"
                medic "Thank you for your kind words, Captain. But they ring hollow in the face of death."

                jump Final

            else:
                show captain determined-open behind medic
                voice "audio/voice/captain/C3-043.mp3"
                captain "Let me worry about that. Tell me what sort of containment?"

                show medic explaining messy
                show captain determined-closed behind medic
                voice "audio/voice/sara/S3-026.mp3"
                medic "Low-frequency EM waves are highly penetrative. We need specialized shielding, such as heavy steel plates."
                voice "audio/voice/sara/S3-027.mp3"
                medic "There are Nu metal sheets in the cargo hold that the bots are using to run repairs. It’s essentially graphene-based nanocomposites."
                
                show captain thinking behind medic
                voice "audio/voice/captain/C3-044.mp3"
                captain "That’s promising. You think it’d work?"

                show medic thinking messy
                show captain neutral-closed behind medic
                voice "audio/voice/sara/S3-028.mp3"
                medic "Pretty sure. The bots are down though. We’d have to go to the cargo hold and use a laser cutter on the sheets."
                voice "audio/voice/sara/S3-029.mp3"
                medic "Then you’d have to build something of a cocoon around the specimen."
                
                show captain neutral-open behind medic
                voice "audio/voice/captain/C3-045.mp3"
                captain "Good. Things are grim but we need to try."

                show medic excited messy
                show captain neutral-closed behind medic
                voice "audio/voice/sara/S3-030.mp3"
                medic "Yes, yes, we need to!"

                # IF NOT SPOKEN TO Act 3 EUGEN
                if seenE3 is False:
                    show medic worried messy
                    voice "audio/voice/sara/S3-031.mp3"
                    medic "I just hope Eugen has a solution for MAD1 and the ship… The damage that has been done cannot be reversed."
                    voice "audio/voice/sara/S3-032.mp3"
                    medic "If he hasn’t found a way to bypass the OS, I’m afraid we’re still doomed."

                    show captain neutral-open behind medic
                    voice "audio/voice/captain/C3-046.mp3"
                    captain "I’ll go speak with him now, hopefully he’s found something out."

                    jump Map3
                # IF SPOKEN TO Act 3 HIGH APPROVAL EUGEN
                elif seenE3 is True and engApproval >= 5:
                    show captain determined-open behind medic
                    voice "audio/voice/captain/C3-047.mp3"
                    captain "Eugen has a solution for MAD1. Once I contain the specimen I need to manually control the ship."
                    voice "audio/voice/captain/C3-048.mp3"
                    captain "Once I do I’ll return with further instructions."

                    show medic neutral
                    show captain determined-closed
                    voice "audio/voice/sara/S3-033.mp3"
                    medic "Good luck Captain! I believe in you!"

                    jump Final

    label E3:
        play sound "Footsteps.mp3" volume 0.8
        play music "Spark_Of_Awareness.mp3" volume 0.8
        scene onlayer screens
        $ seenE3 = True
        scene bg engineer with fade
        show engineer thinking with dissolve
        pause(0.5)
        show captain neutral-closed behind engineer with dissolve

        voice "audio/voice/eugen/E3-001.mp3"
        engineer "Captain, it is safe to say we are in our final moments on this ship." 
        voice "audio/voice/eugen/E3-002.mp3"
        engineer "After trying to combat the system and its programming, nothing seems to be working in our favour."
        voice "audio/voice/eugen/E3-003.mp3"
        engineer "In terms of possible solutions, I don’t see many that I can confidently give precedence to."
        show engineer neutral
        voice "audio/voice/eugen/E3-004.mp3"
        engineer "I have to ask, after everything we went through to get the specimen, are you willing to lose it all to survive, knowing that there is no guarantee in that result as well?"

        menu: 
            # E.3.1a
            "Whatever it takes.":
                show captain determined-open behind engineer
                voice "audio/voice/captain/C3-049.mp3"
                captain "Whatever it takes."

                show engineer frustration
                show captain determined-closed behind engineer
                voice "audio/voice/eugen/E3-005.mp3"
                engineer "I see."

            # E.3.1b
            "Not happy about it, but yes.":
                $ engApproval += 1
                show captain frustrated behind engineer
                voice "audio/voice/captain/C3-050.mp3"
                captain "It feels like it was for nothing, like I’ve failed."
                show captain concern-open behind engineer
                voice "audio/voice/captain/C3-051.mp3"
                captain "But I’m not prepared to sacrifice my crew."

                show engineer resolve
                show captain concern-closed behind engineer
                voice "audio/voice/eugen/E3-006.mp3"
                engineer "I share your frustrations, captain."

            # E.3.1c IF SEEN MO.1 and Approval = 3+
            "We’re ejecting the specimen." if secretChoice is True and engApproval >= 3:
                show captain frustrated behind engineer
                voice "audio/voice/captain/C3-052.mp3"
                captain "About that…"
                show captain concern-open behind engineer
                voice "audio/voice/captain/C3-053.mp3"
                captain "I’ve made the executive decision to trust Sara's intuition about the specimen"

                voice "audio/voice/captain/C3-053-1.mp3"
                captain "I'm ejecting it."

                show engineer shock
                show captain concern-closed behind engineer
                voice "audio/voice/eugen/E3-007.mp3"
                engineer "What?"

                show captain concern-open behind engineer
                voice "audio/voice/captain/C3-054.mp3"
                captain "She suspects that it's responsible for the interference."
                show captain frustrated behind engineer
                voice "audio/voice/captain/C3-055.mp3"
                captain "And I am prepared to lose it all… To save my crew."

                show engineer thinking
                voice "audio/voice/eugen/E3-008.mp3"
                engineer "I see."
                show engineer surprise
                voice "audio/voice/eugen/E3-009.mp3"
                engineer "This is a difficult decision you’ve made."

                show captain distress behind engineer
                captain "…"
                show engineer resolve
                voice "audio/voice/eugen/E3-010.mp3"
                engineer "… My condolences, Captain…"
                
                if seenS3 is False:
                    jump Map3
                elif seenS3 is True:
                    if secretChoice is True:
                        jump EndSec
                    else:
                        jump Final

        #E.3.A: Low Approval/Failure
        if engApproval < 5:
            show engineer neutral
            show captain neutral-closed behind engineer
            if seenS3 is True:
                voice "audio/voice/eugen/E3-011.mp3"
                engineer "10%% oxygen left. 10%%..."
            else: 
                voice "audio/voice/eugen/E3-012.mp3"
                engineer "15%% oxygen left. 15%%..."
            
            show captain concern-open behind engineer
            voice "audio/voice/captain/C3-057.mp3"
            captain "Please tell me you have good news."

            show engineer shock
            show captain concern-closed behind engineer
            voice "audio/voice/eugen/E3-013.mp3"
            engineer "The systems no longer resisting me… it doesn’t have a reason to."
            voice "audio/voice/eugen/E3-014.mp3"
            engineer "Primary life support has entered terminal degradation."

            show captain frustrated behind engineer
            voice "audio/voice/captain/C3-058.mp3"
            captain "That’s not good news…"

            show resolve
            voice "audio/voice/eugen/E3-015.mp3"
            engineer "The little power we had left, I rerouted."

            voice "audio/voice/captain/C3-059.mp3"
            captain "God damnit…"

            show engineer frustration
            voice "audio/voice/eugen/E3-016.mp3"
            engineer "Navigation is gone. Auxiliary is gone. Containment is still stable… Of course it is."
            show engineer anger
            voice "audio/voice/eugen/E3-017.mp3"
            engineer "My entire career was spent believing that if something failed, it was because it was poorly built."
            show engineer shock
            voice "audio/voice/eugen/E3-018.mp3"
            engineer "This system was built exceptionally well, regardless of its unorthodox methods; it just wasn’t built well for us."
            
            show captain concern-open behind engineer
            voice "audio/voice/captain/C3-060.mp3"
            captain "Any success overriding it?"
            
            show engineer frustration
            show captain concern-closed behind engineer
            voice "audio/voice/eugen/E3-019.mp3"
            engineer "I cannot override anything anymore without triggering a complete system failure that would serve no purpose besides ending this immediately."
            show engineer shock
            voice "audio/voice/eugen/E3-020.mp3"
            engineer "This system has bested me, nothing I tried worked, I did everything right… everything."

            # IF NOT SPOKEN TO Act 3 SARA
            if seenS3 is False:
                show engineer thinking
                voice "audio/voice/eugen/E3-021.mp3"
                engineer "If Sara has managed to isolate the specimen, I am afraid it is still in vain."
                voice "audio/voice/eugen/E3-022.mp3"
                engineer "I hope she is not too disappointed in my lack of contribution."

                show captain concern-open behind engineer
                voice "audio/voice/captain/C3-061.mp3"
                captain "At the moment you’re disappointing no one but yourself."
            
            # IF SPOKEN TO Act 3 LOW APPROVAL SARA
            elif seenS3 is True and medApproval < 5:
                show captain frustrated behind engineer
                voice "audio/voice/captain/C3-062.mp3"
                captain "We’re screwed then. The specimen has been emitting electromagnetic waves that interfere with the ship."
                show captain concern-open behind engineer
                voice "audio/voice/captain/C3-063.mp3"
                captain "Even if you had a solution, we’d still be facing imminent death."

                show engineer anger
                show captain concern-closed behind engineer
                voice "audio/voice/eugen/E3-023.mp3"
                engineer "It seems that if I were able to control the interference sooner, we could have had more time."
            
            # IF SPOKEN TO Act 3 HIGH APPROVAL SARA
            elif seenS3 is True and medApproval >= 5:
                show captain frustrated behind engineer
                voice "audio/voice/captain/C3-064.mp3"
                captain "… "
                show captain concern-open behind engineer
                voice "audio/voice/captain/C3-065.mp3"
                captain "We were so close…"
                voice "audio/voice/captain/C3-066.mp3"
                captain "Sara came up with a solution to contain the specimen’s interference with the ship."
                show captain distress behind engineer
                voice "audio/voice/captain/C3-067.mp3"
                captain "But it seems we’re too late."

                show engineer shock
                voice "audio/voice/eugen/E3-024.mp3"
                engineer "It seems that if I were able to control the interference sooner, we could have had more time."
                show engineer frustration
                voice "audio/voice/eugen/E3-025.mp3"
                engineer "Surely Sara will resent me for this, for my limited contribution. I would imagine she is disappointed."
                
            show captain concern-open behind engineer
            voice "audio/voice/captain/C3-068.mp3"
            captain "You can’t blame yourself. Like you said, it wasn’t made for us."
                
            show engineer resolve
            show captain concern-closed behind engineer
            voice "audio/voice/eugen/E3-026.mp3"
            engineer "So this is what remains, a final countdown."
                
            show captain concern-open behind engineer
            voice "audio/voice/captain/C3-069.mp3"
            captain "Thank you for your service, friend."
            show captain determined-open behind engineer
            voice "audio/voice/captain/C3-070.mp3"
            captain "As long as the specimen is brought home, this mission wouldn’t be for nothing."
            show captain concern-open behind engineer
            voice "audio/voice/captain/C3-071.mp3"
            captain "As for whether or not it’s a failure, you tell me, Eugen."
                
            show engineer anger
            show captain concern-closed behind engineer
            voice "audio/voice/eugen/E3-027.mp3"
            engineer "Seeing as everything else has failed, at the very least, we’ll have something to show for it."
            show engineer shock
            voice "audio/voice/eugen/E3-028.mp3"
            engineer "In the end, all I’m thinking about is my work, my equipment, specially designed for this mission."
            show engineer frustration
            voice "audio/voice/eugen/E3-029.mp3"
            engineer "Although perfect, it will potentially be seen as flawed, and my legacy, my work, will become a mockery."
                
            show captain concern-open behind engineer
            voice "audio/voice/captain/C3-072.mp3"
            captain "Your equipment and your work was flawless. All will see that."
                
            show engineer thinking
            show captain concern-closed behind engineer
            voice "audio/voice/eugen/E3-030.mp3"
            engineer "Despite everything, it has been an honor. I do not envy the decision you must make."

            if seenS3 is False:
                jump Map3
            elif seenS3 is True:
                jump Final

        #S.3.B: High Approval/Success
        elif engApproval >= 5:
            show engineer neutral
            show captain neutral-closed behind engineer
            if seenS3 is True:
                voice "audio/voice/eugen/E3-011.mp3"
                engineer "10%% oxygen left. 10%%..."
            else: 
                voice "audio/voice/eugen/E3-012.mp3"
                engineer "15%% oxygen left. 15%%..."
            show engineer shock
            voice "audio/voice/eugen/E3-013.mp3"
            engineer "The system is no longer resisting me… it doesn’t have a reason to."
            voice "audio/voice/eugen/E3-014.mp3"
            engineer "Primary life support has entered terminal degradation."
            
            show captain concern-open behind engineer
            voice "audio/voice/captain/C3-057.mp3"
            captain "Please tell me you have good news."
            
            show engineer frustration
            show captain concern-closed behind engineer
            voice "audio/voice/eugen/E3-030-1.mp3"
            engineer "The little power we had left, I rerouted. We have roughly 3 minutes left."
            
            show captain frustrated behind engineer
            voice "audio/voice/captain/C3-058.mp3"
            captain "That’s not good news…"
            show captain neutral-open behind engineer
            voice "audio/voice/captain/C3-058-1.mp3"
            captain "What’s the plan for protocol?"
            
            show engineer surprise
            show captain neutral-closed behind engineer
            voice "audio/voice/eugen/E3-031.mp3"
            engineer "To hell with protocol, this system is clearly beyond following traditional procedures."
            show engineer thinking
            voice "audio/voice/eugen/E3-032.mp3"
            engineer "We have to consider our last resort; we need to override MAD1 manually, and you need to take control of this ship."

            # IF SPOKEN TO Act 3 LOW APPROVAL SARA
            if seenS3 is True and medApproval < 5:
                show captain concern-open behind engineer
                voice "audio/voice/captain/C3-073.mp3"
                captain "I’m sorry Eugen, but Sara’s made a grim discovery regarding the specimen."
                voice "audio/voice/captain/C3-074.mp3"
                captain "It’s emitting electromagnetic waves that are interfering with the ship."
                voice "audio/voice/captain/C3-075.mp3"
                captain "Even if we manually control the ship, we still wouldn’t be able to do anything with the interference."

                show engineer anger
                show captain concern-open behind engineer
                voice "audio/voice/eugen/E3-026.mp3"
                engineer "So this is what remains, a final countdown."
                show engineer shock
                voice "audio/voice/eugen/E3-028.mp3"
                engineer "In the end, all I’m thinking about is my work, my equipment, specially designed for this mission."
                show engineer frustration
                voice "audio/voice/eugen/E3-029.mp3"
                engineer "Although perfect, it will potentially be seen as flawed, and my legacy, my work, will become a mockery."

                show captain concern-open behind engineer
                voice "audio/voice/captain/C3-072.mp3"
                captain "Your equipment and your work was flawless. All will see that."
                    
                show engineer thinking
                show captain concern-closed behind engineer
                voice "audio/voice/eugen/E3-030.mp3"
                engineer "Despite everything, it has been an honor. I do not envy the decision you must make."

                jump Final
            
            show captain confusion-open behind engineer
            voice "audio/voice/captain/C3-076.mp3"
            captain "What?"
            
            show engineer shock
            show captain confusion-closed behind engineer
            voice "audio/voice/eugen/E3-033.mp3"
            engineer "I’ve traced the source of MAD1’s corruption."
            voice "audio/voice/eugen/E3-034.mp3"
            engineer "I’m sure Sara gave you enough information on the specimen for you to understand this is beyond conventional solutions."

            # IF SPOKEN TO Act 3 HIGH APPROVAL SARA
            if seenS3 is True and medApproval >= 5:
                show captain neutral-open behind engineer
                voice "audio/voice/captain/C3-077.mp3"
                captain "Yes, the specimen has been interfering with the ship."
                show captain determined-open behind engineer
                voice "audio/voice/captain/C3-078.mp3"
                captain "However, she’s come up with a containment solution to stop this interference."

                show engineer neutral
                show captain determined-closed behind engineer
                voice "audio/voice/eugen/E3-035.mp3"
                engineer "That means there is a solution to our situation."

            # IF NOT SPOKEN TO Act 3 SARA
            elif seenS3 is False:
                show captain thinking behind engineer
                voice "audio/voice/captain/C3-079.mp3"
                captain "I’ll have to speak with her to confirm."

            show engineer shock
            show captain neutral-closed behind engineer
            voice "audio/voice/eugen/E3-036.mp3"
            engineer "I cannot override anything anymore without triggering a complete system failure that would serve no purpose besides ending this immediately."
            show engineer surprise
            voice "audio/voice/eugen/E3-037.mp3"
            engineer "To override MAD1 you have to go to the control room; there is a security door locked inside; only you can enter with your personnel badge."
            show engineer shock
            voice "audio/voice/eugen/E3-038.mp3"
            engineer "In the room, you’ll find the system override lever. Once you pull that, you’ll have to take complete control of the ship and navigate us yourself." 
            show engineer resolve
            voice "audio/voice/eugen/E3-039.mp3"
            engineer "While you control the ship, I’ll work to reallocate power to our life support, enough to make it back."
            show engineer thinking
            voice "audio/voice/eugen/E3-040.mp3"
            engineer "If all goes well, which I have my doubts, we will make it back, and the specimen will be properly contained so long as Sara has that under control." 
            show engineer neutral
            voice "audio/voice/eugen/E3-041.mp3"
            engineer "I have to note this is highly risky as we are no longer following the book."
            show engineer shock
            voice "audio/voice/eugen/E3-042.mp3"
            engineer "I can’t say I’m confident the outcome will be good, but it’s our only choice." 
            
            show captain determined-open behind engineer
            voice "audio/voice/captain/C3-080.mp3"
            captain "Eugen, I trust your judgement immensely."
            voice "audio/voice/captain/C3-081.mp3"
            captain "If this is our best last resort, so be it."
            
            show engineer surprise
            show captain determined-closed behind engineer
            voice "audio/voice/eugen/E3-043.mp3"
            engineer "This is what remains, a final countdown. Please tell me you will make the right decision and save this mission."
            
            show engineer resolve
            show captain determined-open behind engineer
            voice "audio/voice/captain/C3-082.mp3"
            captain "You have my word."
            
            if seenS3 is False:
                show captain neutral-open behind engineer
                voice "audio/voice/captain/C3-083.mp3"
                captain "I’ll go see what information Sara has for me."
                show captain determined-open behind engineer
                voice "audio/voice/captain/C3-084.mp3"
                captain "If we’re lucky, we’re all going home."

                jump Map3
            else:
                jump Final

    label Final:
        if medApproval >= 5 and engApproval >= 5:
            show screen MapUIFin with dissolve
            pause

        else:
            jump Choice
        
        label SaraSolution:
            scene onlayer screens
            $ seenSaraSolution = True        
            scene bg artifact with fade
            pause(1)

            "Okay, I need to remember Sara’s instructions..."
            voice "audio/voice/captain/C3-086.mp3"
            captain "First I need to…"
            menu:
                "Scrap some bots for the Nu Metal sheets.":
                    scene bg artifact with hpunch
                    jump Failure

                "Find the Nu Metal sheets in the cargo hold.":
                    captain "..."

                "Ask Eugen for the Nu Metal sheets.":
                    scene bg artifact with hpunch
                    jump Failure
            
            voice "audio/voice/captain/C3-087.mp3"
            captain "Then, I need to…"
            menu:
                "Use the laser cutter to get them in the right shape.":                    
                    captain "..."

                "Bend them into the right shape by hand.":
                    scene bg artifact with hpunch
                    jump Failure

                "Cut them with a saw.":
                    scene bg artifact with hpunch
                    jump Failure
            
            voice "audio/voice/captain/C3-088.mp3"
            captain "Finally…"
            menu:
                "Remove the specimen and wrap it in the metal sheet.":
                    scene bg artifact with hpunch
                    jump Failure

                "Wrap the sheets around the container.":
                    scene bg artifact covered with dissolve
                    voice "audio/voice/captain/C3-092.mp3"
                    captain "Oh my god."
                    voice "audio/voice/captain/C3-093.mp3"
                    captain "I think it worked."
                    voice "audio/voice/captain/C3-094.mp3"
                    captain "Now to manually control the ship."
                    show screen MapUIFin with dissolve
                    pause

                "Bring the sheets and the metal to Sara.":
                    scene bg artifact with hpunch
                    jump Failure
            

        label EugenSolution:
            scene onlayer screens
            $ seenEugenSolution = True
            
            play sound "Footsteps.mp3" volume 0.8
            play music "Microbiology.mp3" volume 0.8
            scene bg control panel 1 with fade

            "I need to follow Eugen’s instructions exactly..."

            voice "audio/voice/captain/C3-096.mp3"
            captain "First I need to…"
            menu:
                "Speak with MAD1.":
                    scene bg control panel 1 with hpunch
                    jump Failure

                "Scan your badge.":                
                    captain "..."

                "Scan the systems.":
                    scene bg control panel 1 with hpunch
                    jump Failure
            
            voice "audio/voice/captain/C3-097.mp3"
            captain "Then, I need to…"
            menu:
                "Pull the system override lever.":     
                    scene bg control panel 2 with dissolve
                    pause(0.1)           
                    scene bg control panel 3 with dissolve
                    captain "..."

                "Shut down MAD1.":
                    scene bg control panel 1 with hpunch
                    jump Failure

                "Record a captain’s log.":
                    scene bg control panel 1 with hpunch
                    jump Failure

            voice "audio/voice/captain/C3-098.mp3"
            captain "Finally…"
            menu:
                "Turn the system back on again.":
                    scene bg control panel 3 with hpunch
                    jump Failure

                "Man full control of the ship.":                          
                    voice "audio/voice/madi/M3-001-1.mp3"
                    computer "System override initiated."
                    voice "audio/voice/madi/M3-001-2.mp3"
                    computer "Manual controls enabled."     
                    voice "audio/voice/captain/C3-099.mp3"
                    captain "It worked…"
                    voice "audio/voice/captain/C3-100.mp3"
                    captain "I need to let the others know."

                    jump TheEnd

                "Hold the lever down while Eugen controls the ship.":    
                    scene bg control panel 3 with hpunch
                    jump Failure


        label Failure:
            
            voice "audio/voice/captain/C3-089.mp3"
            captain "No, no no!"
            voice "audio/voice/captain/C3-090.mp3"
            captain "..."
            voice "audio/voice/captain/C3-091.mp3"
            captain "… Dammit… "

            show screen MapUIEnd with fade
            pause

        label TheEnd:
            # Sara Scene
            play sound "Footsteps.mp3" volume 0.8
            play music "Microbiology.mp3" volume 0.8
            scene onlayer screens
            $ seenS3 = True
            scene bg medic with fade
            show medic worried messy with dissolve
            pause(0.5)
            show captain neutral-closed behind medic with dissolve

            voice "audio/voice/sara/S3-034.mp3"
            medic "Did it work?"

            show captain determined-open behind medic
            voice "audio/voice/captain/C3-101.mp3"
            captain "It did. Once Eugen can reroute life support I need you to monitor the specimen at all times."
            voice "audio/voice/captain/C3-102.mp3"
            captain "We’re going home."
            
            show medic excited messy
            show captain determined-closed behind medic
            voice "audio/voice/sara/S3-035.mp3"
            medic "Yes! Will be on it ASAP!"

            
            # Eugen Scene
            play sound "Footsteps.mp3" volume 0.8
            play music "Microbiology.mp3" volume 0.8
            scene bg engineer with fade
            show engineer neutral with dissolve
            pause(0.5)
            show captain neutral-closed behind engineer with dissolve

            voice "audio/voice/eugen/E3-044.mp3"
            engineer "I see the system override must have succeeded."

            show captain determined-open behind engineer
            voice "audio/voice/captain/C3-103.mp3"
            captain "Yes it did."

            show engineer surprise
            show captain determined-closed behind engineer
            voice "audio/voice/eugen/E3-045.mp3"
            engineer "I will begin rerouting life support immediately."
            show engineer thinking
            voice "audio/voice/eugen/E3-046.mp3"
            engineer "Good work, Captain."
            
            show captain determined-open behind engineer
            voice "audio/voice/captain/C3-104.mp3"
            captain "Thank you, Eugen. You as well."

            jump EndG

    label Choice:
        scene onlayer screens
        play sound "Footsteps.mp3" volume 0.8
        scene bg escape pod with fade

        voice "audio/voice/captain/C3-105.mp3"
        captain "So… It’s come to this…"
        voice "audio/voice/captain/C3-106.mp3"
        captain "Only one of us is going home…"
        voice "audio/voice/captain/C3-107.mp3"
        captain "…" 

        "You were unable to bring everyone together. Now you must choose."

        menu:
            "Sara":
                voice "audio/voice/captain/C3-111.mp3"
                captain "Sara’s research is too important."
                voice "audio/voice/captain/C3-112.mp3"
                captain "And she’s the youngest of all of us."
                voice "audio/voice/captain/C3-113.mp3"
                captain "She deserves to go home."
                voice "audio/voice/captain/C3-114.mp3"
                captain "Make her family proud."
                voice "audio/voice/captain/C3-115.mp3"
                captain "I’m sorry, Eugen."

                jump EndS

            "Eugen":
                voice "audio/voice/captain/C3-116.mp3"
                captain "Eugen’s technological feats are too valuable."
                voice "audio/voice/captain/C3-117.mp3"
                captain "He has so much wisdom and experience."
                voice "audio/voice/captain/C3-118.mp3"
                captain "He deserves to go home."
                voice "audio/voice/captain/C3-119.mp3"
                captain "Keep making amazing advancements."
                voice "audio/voice/captain/C3-120.mp3"
                captain "I’m sorry, Sara."

                jump EndE

            "Yourself":
                voice "audio/voice/captain/C3-108.mp3"
                captain "I can’t choose one of them over the other."
                voice "audio/voice/captain/C3-109.mp3"
                captain "I’d rather have them thinking I was selfish than valued less than the other."
                voice "audio/voice/captain/C3-110.mp3"
                captain "I’m sorry, Sara and Eugen."
                
                jump EndC

    # ENDINGS
    label EndB:
        $ quick_menu = False
        play music "Goosebumps.mp3" volume 1.0

        # Bad ending: Captain abandons ship
        scene ending captain with fade
        pause(0.5)

        show screen EndBPoemA with dissolve
        pause(3)

        voice "audio/voice/captain/C3-EndingB.mp3"
        show screen EndBPoemB with dissolve
        hide screen EndBPoemA with dissolve
        pause(30)

        # During credits
        hide screen EndBPoemB with dissolve
        show screen Credits1 with dissolve
        pause(7)

        show screen Credits2 with dissolve
        hide screen Credits1 with dissolve

        voice "audio/voice/eugen/E3-EndingB.mp3"
        pause(25)

        show screen Credits3 with dissolve
        hide screen Credits2 with dissolve

        voice "audio/voice/sara/S3-EndingB.mp3"
        pause(20)

        show screen Credits4 with dissolve
        hide screen Credits3 with dissolve

        voice "audio/voice/madi/M3-EndingB.mp3"
        pause(28)

        show screen Credits5 with dissolve
        hide screen Credits4 with dissolve
        pause(5)

        $ persistent.secret_unlocked = True
        $ persistent.endB_unlocked = True
        
        hide screen Credits5 with dissolve
        scene black with dissolve
        pause(1)
        
        show screen TryAgain with dissolve
        pause 

        return

    label EndC:
        $ quick_menu = False
        play music "Murder-Mystery.mp3" volume 0.8
        # Captain leaves with specimen 
        scene ending captain with fade
        pause(0.5)

        show screen EndCPoemA with dissolve
        pause(3)

        voice "audio/voice/captain/C3-EndingC.mp3"
        show screen EndCPoemB with dissolve
        hide screen EndCPoemA with dissolve
        pause(31)

        # During credits
        hide screen EndCPoemB with dissolve
        show screen Credits1 with dissolve
        pause(7)

        show screen Credits2 with dissolve
        hide screen Credits1 with dissolve

        voice "audio/voice/eugen/E3-EndingC.mp3"
        pause(25)

        show screen Credits3 with dissolve
        hide screen Credits2 with dissolve

        voice "audio/voice/sara/S3-EndingC.mp3"
        pause(25)

        show screen Credits4 with dissolve
        hide screen Credits3 with dissolve

        voice "audio/voice/madi/M3-EndingC.mp3"
        pause(24)

        show screen Credits5 with dissolve
        hide screen Credits4 with dissolve
        pause(5)

        $ persistent.secret_unlocked = True
        $ persistent.endC_unlocked = True
        
        hide screen Credits5 with dissolve
        scene black with dissolve
        pause(1)
        
        show screen TryAgain with dissolve
        pause 

        return

    label EndE:
        $ quick_menu = False
        play music "Catching-Predators.mp3" volume 0.8
        # Eugen leaves with specimen 
        scene ending engineer with fade
        pause(0.5)

        show screen EndEPoemA with dissolve
        pause(3)

        voice "audio/voice/eugen/E3-EndingE.mp3"
        show screen EndEPoemB with dissolve
        hide screen EndEPoemA with dissolve
        pause(30)

        # During credits
        hide screen EndEPoemB with dissolve
        show screen Credits1 with dissolve
        pause(7)

        show screen Credits2 with dissolve
        hide screen Credits1 with dissolve

        voice "audio/voice/captain/C3-EndingE.mp3"
        pause(18)

        show screen Credits3 with dissolve
        hide screen Credits2 with dissolve

        voice "audio/voice/sara/S3-EndingE.mp3"
        pause(20)

        show screen Credits4 with dissolve
        hide screen Credits3 with dissolve

        voice "audio/voice/madi/M3-EndingES.mp3"
        pause(24)

        show screen Credits5 with dissolve
        hide screen Credits4 with dissolve
        pause(5)

        $ persistent.secret_unlocked = True
        $ persistent.endE_unlocked = True

        hide screen Credits5 with dissolve
        scene black with dissolve
        pause(1)
        
        show screen TryAgain with dissolve
        pause 

        return

    label EndS:
        $ quick_menu = False
        play music "Leaving-No-Trace.mp3" volume 0.8
        # Sara leaves with specimen 
        scene ending medic with fade
        pause(0.5)

        show screen EndSPoemA with dissolve
        pause(3)

        voice "audio/voice/sara/S3-EndingS.mp3"
        show screen EndSPoemB with dissolve
        hide screen EndSPoemA with dissolve
        pause(35)

        # During credits
        hide screen EndSPoemB with dissolve
        show screen Credits1 with dissolve
        pause(7)

        show screen Credits2 with dissolve
        hide screen Credits1 with dissolve

        voice "audio/voice/captain/C3-EndingS.mp3"
        pause(18)

        show screen Credits3 with dissolve
        hide screen Credits2 with dissolve

        voice "audio/voice/eugen/E3-EndingS.mp3"
        pause(25)

        show screen Credits4 with dissolve
        hide screen Credits3 with dissolve

        voice "audio/voice/madi/M3-EndingES.mp3"
        pause(24)

        show screen Credits5 with dissolve
        hide screen Credits4 with dissolve
        pause(5)

        $ persistent.secret_unlocked = True
        $ persistent.endS_unlocked = True

        hide screen Credits5 with dissolve
        scene black with dissolve
        pause(1)
        
        show screen TryAgain with dissolve
        pause 
        
        return

    label EndG:
        $ quick_menu = False
        # Good ending
        play music "Future Utopia.mp3" volume 0.8
        scene ending crew stars  with fade
        pause(0.5)

        show screen EndGPoemA with dissolve
        pause(3)

        voice "audio/voice/captain/C3-EndingG.mp3"
        show screen EndGPoemB with dissolve
        hide screen EndGPoemA with dissolve
        pause(30)

        # During credits
        hide screen EndGPoemB with dissolve
        show screen Credits1 with dissolve
        pause(7)

        show screen Credits2 with dissolve
        hide screen Credits1 with dissolve

        voice "audio/voice/eugen/E3-EndingG.mp3"
        pause(20)

        show screen Credits3 with dissolve
        hide screen Credits2 with dissolve

        voice "audio/voice/sara/S3-EndingG.mp3"
        pause(25)

        show screen Credits4 with dissolve
        hide screen Credits3 with dissolve

        voice "audio/voice/madi/M3-EndingG.mp3"
        pause(25)

        show screen Credits5 with dissolve
        hide screen Credits4 with dissolve
        pause(5)

        $ persistent.secret_unlocked = True
        $ persistent.endG_unlocked = True

        hide screen Credits5 with dissolve
        scene black with dissolve
        pause(1)
        
        show screen TryAgain with dissolve
        pause 

        return

    label EndSec:
        $ quick_menu = False
        play music "Strong-Convictions.mp3" volume 0.8
        # Secret ending: Throw away the specimen
        scene ending byebye fungus with fade

        pause 0.5
        show screen EndSECPoemA with dissolve
        pause(3)

        voice "audio/voice/captain/C3-EndingSEC.mp3"
        show screen EndSECPoemB with dissolve
        hide screen EndSECPoemA with dissolve
        pause(16)

        # During credits
        hide screen EndSECPoemB with dissolve
        show screen Credits1 with dissolve
        pause(7)

        show screen Credits2 with dissolve
        hide screen Credits1 with dissolve

        voice "audio/voice/eugen/E3-EndingSEC.mp3"
        pause(20)

        show screen Credits3 with dissolve
        hide screen Credits2 with dissolve

        voice "audio/voice/sara/S3-EndingSEC.mp3"
        pause(20)

        show screen Credits4 with dissolve
        hide screen Credits3 with dissolve

        # For now this will be computer, if we decide to add Matthew voice will change it.
        # It's Watthew
        voice "audio/voice/matthew/W3-EndingSEC.mp3"
        pause(23)

        show screen Credits5 with dissolve
        hide screen Credits4 with dissolve
        pause(5)

        $ persistent.secret_unlocked = True
        $ persistent.endSEC_unlocked = True

        hide screen Credits5 with dissolve
        scene black with dissolve
        pause
        scene secret ending with fade
        pause
        scene black with dissolve
        return

    return


# Star Logs (putting in the script and lines, don't know how to program them actually working :p)
label StarLogs:
    label EndBLog:
        $ quick_menu = False
        scene black with dissolve
        voice "audio/voice/captain/C4-001.mp3"
        captain "Captain’s log. January 27th."
        voice "audio/voice/captain/C4-002.mp3"
        captain "My position at the CSA is being terminated. Effective immediately."
        voice "audio/voice/captain/C4-003.mp3"
        captain "I’m sorry…"
        voice "audio/voice/captain/C4-004.mp3"
        captain "I’m sorry Sara…"
        voice "audio/voice/captain/C4-005.mp3"
        captain "I’m sorry Eugen…"
        voice "audio/voice/captain/C4-006.mp3"
        captain "I’m sorry Matthew…"
        $ renpy.end_replay()
        
    label EndSLog:
        $ quick_menu = False
        scene black with dissolve
        voice "audio/voice/matthew/W4-001.mp3"
        matthew "Captain’s log. 4 months until Expedition Europa 1 launches."
        voice "audio/voice/matthew/W4-002.mp3"
        matthew "Unfortunately, Dr. Sara Fernando’s current mission is taking longer than expected."
        voice "audio/voice/matthew/W4-003.mp3"
        matthew "She will not be able to join us to Europa. There won’t be enough prep time for her."
        voice "audio/voice/matthew/W4-004.mp3"
        matthew "Thankfully, I know other astrobiologists who can take her place."
        voice "audio/voice/matthew/W4-005.mp3"
        matthew "Hopefully, she’ll join the research team if we successfully bring home a specimen."
        $ renpy.end_replay()

    label EndELog:
        $ quick_menu = False
        scene black with dissolve
        voice "audio/voice/matthew/W4-006.mp3"
        matthew "Captain’s log. 6 months until Expedition Europa 1 launches."
        voice "audio/voice/matthew/W4-007.mp3"
        matthew "Eugen Braun’s ice drill has completed the prototyping stage and is ready to be tested in the field."
        voice "audio/voice/matthew/W4-008.mp3"
        matthew "Unfortunately, the crew only has space for eight people, and all eight positions have been filled."
        voice "audio/voice/matthew/W4-009.mp3"
        matthew "Braun is unable to join us for this mission."
        voice "audio/voice/matthew/W4-010.mp3"
        matthew "A shame. I’m more than sure he would’ve liked to see it in action."
        voice "audio/voice/matthew/W4-011.mp3"
        matthew "I’ll be sure to log its success for him."
        $ renpy.end_replay()

    label EndCLog:
        $ quick_menu = False
        scene black with dissolve
        voice "audio/voice/captain/C4-007.mp3"
        captain "Captain’s log. February 2nd."
        voice "audio/voice/captain/C4-008.mp3"
        captain "I’m resigning from my position at the CSA."
        voice "audio/voice/captain/C4-009.mp3"
        captain "I’m no longer fit to be an astronaut, let alone a captain."
        voice "audio/voice/captain/C4-010.mp3"
        captain "I’m… I’m sorry, Sara and Eugen."
        voice "audio/voice/captain/C4-011.mp3"
        captain "I’m sorry I couldn’t save you."
        $ renpy.end_replay()

    label EndGLog:
        $ quick_menu = False
        scene black with dissolve
        voice "audio/voice/captain/C4-012.mp3"
        captain "Captain’s log, I guess…"
        voice "audio/voice/captain/C4-013.mp3"
        captain "10 months until Expedition Europa 2 launches."
        voice "audio/voice/captain/C4-014.mp3"
        captain "It took weeks of convincing, but the CSA has agreed to allow me, Rudy Jensen, to captain this mission."
        voice "audio/voice/captain/C4-015.mp3"
        captain "They weren’t sure if having a grieving captain would be appropriate."
        voice "audio/voice/captain/C4-016.mp3"
        captain "But I need to helm this expedition. For Matthew. To finish what he started."
        voice "audio/voice/captain/C4-017.mp3"
        captain "What kind of husband would I be otherwise?"
        voice "audio/voice/captain/C4-018.mp3"
        captain "..."
        voice "audio/voice/captain/C4-019.mp3"
        captain "In any case, all information we have from Expedition Europa 1 has been saved on MAD1."
        voice "audio/voice/captain/C4-020.mp3"
        captain "We’ll be using her for this mission."
        $ renpy.end_replay()

    label EndSECLog:
        $ quick_menu = False
        scene black with dissolve
        voice "audio/voice/matthew/W4-012.mp3"
        matthew "Ready to meet our baby?"
        voice "audio/voice/captain/C4-021.mp3"
        captain "Please don’t call the OS our “baby,” Matthew…"
        voice "audio/voice/matthew/W4-014.mp3"
        matthew "Fine. My baby. So… Wuddya think?"
        voice "audio/voice/captain/C4-022.mp3"
        captain "You built all of this… Yourself?"
        voice "audio/voice/matthew/W4-015.mp3"
        matthew "Yyyuuuuppp. The operating system had to be designed from the ground up." 
        voice "audio/voice/captain/C4-023.mp3"
        captain "Jesus, you didn’t wanna use an existing one to start with?"
        voice "audio/voice/matthew/W4-016.mp3"
        matthew "If we’re taking this thing all the way to Jupiter’s orbit we need something powerful."
        voice "audio/voice/matthew/W4-017.mp3"
        matthew "Plus, this way I know every little detail about it."
        voice "audio/voice/matthew/W4-018.mp3"
        matthew "So if anything needs fixing, I can handle it right away."
        voice "audio/voice/captain/C4-024.mp3"
        captain "Oh my god. That’s amazing, Hun!"
        voice "audio/voice/matthew/W4-019.mp3"
        matthew "Thank you, Pumpkin!"
        voice "audio/voice/matthew/W4-020.mp3"
        matthew "Wanna guess what I named her?"
        voice "audio/voice/captain/C4-025.mp3"
        captain "Her?"
        voice "audio/voice/matthew/W4-021.mp3"
        matthew "What’s wrong with that?"
        voice "audio/voice/captain/C4-026.mp3"
        captain "Don’t know, seems a little sexist. Having your servant robot be a woman and all that."
        voice "audio/voice/matthew/W4-022.mp3"
        matthew "Well it’ll make more sense once you know what I named her!"
        voice "audio/voice/captain/C4-027.mp3"
        captain "Alright alright, what’s her name?"
        voice "audio/voice/matthew/W4-023.mp3"
        matthew "MAD1!"
        voice "audio/voice/captain/C4-028.mp3"
        captain "Why Maddy? Is it an acronym?"
        voice "audio/voice/matthew/W4-024.mp3"
        matthew "Well technically, it stands for Manager of Astral Devices 1.0."
        voice "audio/voice/matthew/W4-025.mp3"
        matthew "But between us… Matthew… Matt… Rudy… -dy…"
        voice "audio/voice/captain/C4-029.mp3"
        captain "Oh my god you combined our names."
        voice "audio/voice/captain/C4-030.mp3"
        captain "You’re such a dork!"
        voice "audio/voice/matthew/W4-026.mp3"
        matthew "Hahahaha!"
        voice "audio/voice/captain/C4-031.mp3"
        captain "I love you… so much, hun."
        voice "audio/voice/matthew/W4-027.mp3"
        matthew "I love you too, Pumpkin!"
        voice "audio/voice/captain/C4-032.mp3"
        captain "Wait, are you recording this?"
        voice "audio/voice/matthew/W4-028.mp3"
        matthew "It’s my first captain’s log!"
        voice "audio/voice/captain/C4-033.mp3"
        captain "You’re supposed to start the recording by saying “Captain’s Log”."
        voice "audio/voice/matthew/W4-029.mp3"
        matthew "Well thankfully no one else is gonna hear this."
        voice "audio/voice/captain/C4-034.mp3"
        captain "Tsk. Dork."
        $ renpy.end_replay()
        