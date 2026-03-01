# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define captain = Character("Captain", image="captain@3.5/captain", kind=bubble)
define engineer = Character("Eugen", image="engineer placeholder", kind=bubble)
define medic = Character("Sara", image="medic/medic", kind=bubble)
define computer = Character("MAD1", image="computer/computer", kind=bubble)

# Sound Settingsa
default preferences.volume.music = 0.5
default preferences.volume.sfx = 0.5

# Setting base approval scores
init python:
    medApproval = 0
    engApproval = 0

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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "Electric_Dawn.mp3"

    scene bg computer

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show computer neutral-1
    show captain neutral-open behind computer
    
    play sound "captainslog_background.mp3"

    voice "voice/captain/C1.001.mp3"
    captain "Captain’s Log — September 24th." 
    voice "voice/captain/C1.002.mp3"
    captain "We’ve successfully drilled through the ice layer of Europa and retrieved an 
                artifact that resembles life."
    voice "voice/captain/C1.003.mp3"
    captain "Short on time, we’ve started the course back 
                to Earth."
    voice "voice/captain/C1.004.mp3"
    captain "Dr. Fernando’s begun studying the specimen. I’ve ordered her to confirm the 
                form of life." 
    voice "voice/captain/C1.005.mp3"
    captain "And Technician Braun’s been commanded to 
                conduct maintenance on the equipment in the bio-lab." 

    play sound "m4d1_notification.mp3"
    show computer neutral-2
    show captain neutral-closed behind computer

    voice "voice/madi/M1.001.mp3"
    computer "Message from Cosmotechnician Eugene Braun. Open message?"

    menu:
        "Open message":
            show captain neutral-open behind computer
            voice "voice/captain/C1.006.mp3"
            captain "Open and read."

    play sound "m4d1_message_open.mp3" 
    show computer neutral-3
    show captain neutral-closed behind computer

    voice "voice/madi/M1.002.1.mp3"
    computer "Engineer: Captain, I have been reviewing the bio lab’s system; the data does not align with standard 
                operating parameters." 
    voice "voice/madi/M1.002.2.mp3"
    computer "Engineer: This does not appear to be a malfunction or human error; there seems to be an 
                interference with the processes. It will be best to address this immediately."

    show captain frustrated behind computer
    voice "voice/captain/C1.007.mp3"
    captain "(Sighs, rubs temples)"
    voice "voice/captain/C1.008.mp3"
    captain "MAD1, run ship diagnostics."

    show computer processing-1
    voice "voice/madi/M1.003.mp3"
    computer "Initiating system diagnostics. Analyzing running operations."

    play sound "system_diagnostic_start.mp3"
    show computer processing-2

    show captain rememberance-closed behind computer

    show computer processing-3
    captain "This is probably my fault… I made us take an extra day travelling to find his ship. I’m rushing us home to return on time."

    play sound "electric_oh_no.mp3"
    show computer error-1
    voice "voice/madi/M1.004.1.mp3"
    computer "Error. Process failure.{w=0.5}" 
    show computer processing-1
    voice sustain
    voice "voice/madi/M1.004.2.mp3"
    computer " Reinitiating process.{w=0.5}" 
    show computer processing-2
    show computer processing-3
    show computer error-1
    voice sustain
    voice "voice/madi/M1.004.3.mp3"
    computer " Error. System failure.{w=0.5}"
    
    scene bg computer error
    show computer error-1
    show captain confusion-closed behind computer
    
    stop music fadeout 1.0
    play sound "error_sound_1.mp3"
    voice sustain
    voice "voice/madi/M1.004.4.mp3"
    computer " Error. Error. E̷̠̓r̷̖͆r̵̼͋o̷̳̔r{w=0.5}{nw}"

    show captain confusion-open with hpunch 
    voice "voice/captain/C1.010.mp3"
    captain "What’s happening? MAD1, show me the error logs."

    scene bg computer error bad
    show computer error-1
    show captain confusion-closed behind computer

    voice "voice/madi/M1.005.1.mp3"
    computer "Error. Unable to end process." 
    play sound "error_sound_2.mp3"
    voice sustain
    voice "voice/madi/M1.005.2.mp3"
    computer "Pulling error log̶̕s.{w=0.5}{nw}"
    voice sustain
    voice "voice/madi/M1.005.3.mp3"
    computer "Ê̴̋͒͠r̵̛̈̏r̸̳̯͎͍̬̊̇̀o̵r̷͘. {w=0.3}{nw}" 
    voice sustain
    voice "voice/madi/M1.005.4.mp3"
    computer "Sys̷̖̏ṭ̷̋e̵̗̬͋m̵̩͋̕ṡ̴̨͎ dò̷̧͎͍͇̫͆̕ẃ̵̛̔n̶-{w=0.5}{nw}"

    stop sound
    play sound "systems_off.mp3"
    scene bgCompDark
    show computer error-2
    show captainConfusedClosedDark behind computer

    "The lights go out. Everything stops." 
    "The buzz and rumbles of the ship go deadly silent, and it’s as if time and space have frozen solid." 
    "Everything goes wrong."
    "Only one terminal blinks online."

    voice "voice/madi/M1.006.mp3"
    computer "But O heart! heart! H̷̢̚e̷a̵ŕ̶̤t̵͈́!̵̺̾
                O the b̵̝̀l̷̨͠e̶̹̕ȩ̵̔d̴̲̅i̶n̵̕ġ̷͍ drops of red,
                Where on the deck my Captain lies,
                Fallen cold and d̸̻̈́e̵͉̋a̸̪̿d̸̙͆."

    "The terminal displays strange text. I’ve never seen MAD1 act this way before."

    show captainConfusedOpenDark behind computer
    voice "voice/captain/C1.011.mp3"
    captain "What the hell?" 
    
    show captainConfusedClosedDark behind computer   
    play sound "captain_smack_1.mp3" 
    captain "(Smacks terminal)" with hpunch 

    scene bg computer
    play sound "systems_back_online.mp3"
    play music "Ice_Cold.mp3"

    show computer reboot-1
    show captain confusion-closed behind computer   

    "Then the lights come on again. Thankfully."
    show computer reboot-2
    "Sound returns as I presume the system reboots."
    show computer reboot-3

    voice "voice/madi/M1.007.mp3"
    computer "System force restart. Diagnostics complete." 
    show computer neutral-1
    voice "voice/madi/M1.008.mp3"
    computer "Power systems offline. Emergency power engaged." 
    voice "voice/madi/M1.009.mp3"
    computer "Navigation systems paused." 
    voice "voice/madi/M1.010.mp3"
    computer "Internal communications offline." 
    show computer neutral-2
    voice "voice/madi/M1.011.mp3"
    computer "Satellite communication offline." 
    voice "voice/madi/M1.012.mp3"
    computer "Data systems offline." 
    voice "voice/madi/M1.013.mp3"
    computer "Thermal control offline." 
    show computer neutral-3
    voice "voice/madi/M1.0014.mp3"
    computer "Oxygen system offline." 
    voice "voice/madi/M1.015.mp3"
    computer "Emergency Life support protocol engaged."

    show captain anger-open behind computer 
    voice "voice/captain/C1.012.mp3"
    captain "MAD1, what the hell is going on?"

    show captain anger-closed behind computer 

    voice "voice/madi/M1.016.mp3"
    computer "Mission status paused. To preserve power and life support, non-essential rooms have been sealed. Oxygen will be rerouted."

    play sound "captain_smack_2.mp3" 

    captain "(Slams fist on table)" with hpunch 
    show captain anger-open behind computer
    voice "voice/captain/C1.013.mp3"
    captain "Right now? But we're so close..."
    
    show captain anger-closed behind computer 

    voice "voice/madi/M1.017.mp3"
    computer "Captain, I recommend checking on the crew to maintain morale and investigate the cause of the system failure."

    show captain frustrated behind computer 
    captain "(Sighs)" 
    show captain neutral-open behind computer 
    voice "voice/captain/C1.014.mp3"
    captain "I suppose you’re right. Give me periodic reports on the oxygen levels."
    show captain neutral-closed behind computer 

    voice "voice/madi/M1.018.mp3"
    computer "Aye, aye, Captain. Oxygen levels at 99%%."

    show captain frustrated behind computer 
    captain "..." 
    voice "voice/captain/C1.015.1.mp3"
    captain "Thanks..."
    show captain neutral-open behind computer 
    voice "voice/captain/C1.015.2.mp3"
    captain "Let’s check on the crew."
    show captain neutral-closed behind computer 

    $ seenSI = False
    $ seenEI = False

    menu:
        "Speak to Eugen":
            voice "voice/captain/C1.017.mp3"
            captain "I should speak to Eugen. He’ll probably know what’s happening."
            jump EI

        "Speak to Sara":
            voice "voice/captain/C1.016.mp3"
            captain "I should speak to Sara. She’s probably freaking out right now."
            jump SI
        
    
    label SI:
        $ seenSI = True
        scene bg medic
        show medic nervous
        show captain neutral-closed behind medic

        voice "voice/sara/S1.001.mp3"
        medic "Captain! W-what just happened! Thank goodness you arrived when you did. I was going to—" 
        
        show captain neutral-open behind medic
        voice "voice/captain/C1.018.mp3"
        captain "Yes, quite unexpected. I’m sorting it out with Eugen." 
        voice "voice/captain/C1.019.mp3"
        captain "We’ve had good luck so far—we’ve achieved something no man has managed before. These things happen."

        show medic neutral
        show captain neutral-closed behind medic
        voice "voice/sara/S1.002.mp3"
        medic "Yes, yes, of course!" 

        show medic explaining
        show captain neutral-closed behind medic
        voice "voice/sara/S1.003.mp3"
        medic "I mean, this cargo—this discovery—would revolutionize everything." 
        voice "voice/sara/S1.004.mp3"
        medic "Our very understanding of the universe. Extraterrestrial life! Aboard this ship." 
        show medic excited
        show captain neutral-closed behind medic
        voice "voice/sara/S1.005.mp3"
        medic "I still can’t believe it." 
        show medic neutral
        show captain neutral-closed behind medic
        voice "voice/sara/S1.006.mp3"
        medic "But this… development is most concerning." 

        show medic nervous
        show captain neutral-closed behind medic
        voice "voice/sara/S1.007.mp3"
        medic "What could possibly be happening, Captain?" 
        voice "voice/sara/S1.008.mp3"
        medic "Could it—could this result in some kind of irreparable, cascading failure?"

        show captain neutral-open behind medic
        voice "voice/captain/C1.020.mp3"
        captain "Like I said before, Sara, we’ll find out soon. There is no reason to assume the worst." 

        show captain neutral-closed behind medic
        voice "voice/sara/S1.009.mp3"
        medic "I understand. I just—given what has happened before…"

        show captain anger-open behind medic
        voice "voice/captain/C1.021.mp3"
        captain "What happened to the previous mission has nothing to do with what is happening now."

        # SI.1
        show medic stressed
        show captain anger-closed behind medic
        voice "voice/sara/S1.010.mp3"
        medic "I’m sorry. I-I guess I’ve always felt you were easier to talk to on this ship." 
        voice "voice/sara/S1.011.mp3"
        medic "I admit this incident isn’t making me think straight. I shouldn’t have brought it up." 
        voice "voice/sara/S1.012.mp3"
        medic "I understand it must be painful for you—"

        menu:
            # SI.1.a
            "We’re all stressed.":
                $ medApproval += 1

                show captain concern-open behind medic
                voice "voice/captain/C1.022.mp3"
                captain "It’s okay, Sara. This is stressful for all of us."

                show medic neutral
                show captain concern-closed behind medic
                voice "voice/sara/S1.013.mp3"
                medic "This is true, I apologize for bringing it up."

            # SI.1.b
            "It’s fine.":
                $ medApproval -= 1

                show captain anger-open behind medic
                voice "voice/captain/C1.023.mp3"
                captain "It’s fine. Just don’t do it again."

                show medic stressed
                show captain anger-closed behind medic
                voice "voice/sara/S1.014.mp3"
                medic "I’m sorry, Captain. I’ll just, um…"

        show captain neutral-open behind medic
        voice "voice/captain/C1.024.mp3"
        captain "How about you go through your notes so far?"
        voice "voice/captain/C1.025.mp3"
        captain "We could use any theories on what this specimen is and its properties."

        show medic excited
        show captain neutral-closed behind medic
        voice "voice/sara/S1.015.mp3"
        medic "Yes, yes… I already have working hypotheses, though nothing exactly seems to work out perfectly at the moment."
        
        show medic nervous
        show captain neutral-closed behind medic
        voice "voice/sara/S1.016.mp3"
        medic "I should work harder…"

        show captain concern-open behind medic
        voice "voice/captain/C1.026.mp3"
        captain "Sara, you’re already working very hard."
        voice "voice/captain/C1.027.mp3"
        captain "You’re the best in the field. Remember; it’s why we have you on this mission."

        show medic neutral
        show captain concern-closed behind medic
        voice "voice/sara/S1.017.mp3"
        medic "Thank you, Captain. I can’t overstate how much this mission means to me."
        show medic excited
        show captain concern-closed behind medic
        voice "voice/sara/S1.018.mp3"
        medic "This—this specimen we’ve found is the holy grail of astrobiology."

        show captain neutral-open behind medic 
        voice "voice/captain/C1.028.mp3"
        captain "And that’s exactly why I need you to tell us what we’re dealing with here."
        voice "voice/captain/C1.029.mp3"
        captain "I’m counting on you Sarah."
        voice "voice/captain/C1.030.mp3"
        captain "We’ll get the system back up one way or another."

        # SI.2
        show medic stressed
        show captain neutral-closed behind medic
        voice "voice/sara/S1.019.mp3"
        medic "But my research is in the system. How long will it take?" 
        voice "voice/sara/S1.020.mp3"
        medic "All I have to work with is my journal." 
        voice "voice/sara/S1.021.mp3"
        medic "I-if this takes a long time, what am I supposed to do?"
        
        show medic nervous
        show captain neutral-closed behind medic

        menu:
            # SI.2.a
            "You can figure it out.":
                $ medApproval -= 1
                
                show captain anger-open behind medic
                voice "voice/captain/C1.031.mp3"
                captain "Figure it out. That’s an order."

                show medic stressed
                show captain anger-closed behind medic
                voice "voice/sara/S1.022.mp3"
                medic "O-of course Captain."

            # SI.2.b
            "I have faith in you." :
                $ medApproval += 1
                
                show captain neutral-open behind medic
                voice "voice/captain/C1.032.mp3"
                captain "I can’t say for sure, but I’ve seen you work with less before."
                voice "voice/captain/C1.033.mp3"
                captain "I expect you’d gain more insight once you study your notes. I have faith in you."

                show medic neutral
                show captain neutral-closed behind medic
                voice "voice/sara/S1.023.mp3"
                medic "I won’t let you down!"

        if seenEI is False:
            menu: 
                "Speak to Eugen":
                    show captain neutral-closed behind medic
                    voice "voice/captain/C1.017.mp3"
                    captain "I should speak to Eugen now. He’ll probably know what’s happening."
                    jump EI

        else:
            jump M1


    label EI:
        $ seenEI = True
        scene bg engineer
        show engineer neutral
        show captain neutral-closed behind engineer

        show captain neutral-open behind engineer
        voice "voice/captain/C1.034.mp3"
        captain "How’re you holding up Eugen?"

        show captain neutral-closed behind engineer
        voice "voice/eugen/E1.003.mp3"
        engineer "As well as one can, given the circumstances." 
        voice "voice/eugen/E1.004.mp3"
        engineer "May we skip the pleasantries? I dislike small talk." 
        voice "voice/eugen/E1.005.mp3"
        engineer "I’m sure Sara would appreciate it more."

        show captain neutral-open behind engineer
        voice "voice/captain/C1.035.mp3"
        captain "Got it... Straight to the point then. Report."

        show captain neutral-closed behind engineer
        voice "voice/eugen/E1.006.mp3"
        engineer "Captain, the situation is not ideal. There appears to be a system failure on a magnitude I’ve never seen."
        voice "voice/eugen/E1.007.mp3"
        engineer "I am looking into it, however, little progress is being made."
        voice "voice/eugen/E1.008.mp3"
        engineer "At the rate we’re losing oxygen, I estimate that we have approximately one hour."
        
        show captain frustrated behind engineer
        voice "voice/captain/C1.036.mp3"
        captain "Shit… Well there goes my hope for any good news."

        # EI.1
        show captain neutral-closed behind engineer
        voice "voice/eugen/E1.009.mp3"
        engineer "Is there any information you can provide? Do you know what might have caused this?"

        menu:
            # EI.1a
            "I’m not sure yet.":
                $ engApproval -= 1
                show captain thinking behind engineer
                voice "voice/captain/C1.037.mp3"
                captain "I’m not sure yet. I want to find out a bit more before I give any concrete answers."

                # show engineer frustrated
                # show captain thinking behind engineer
                voice "voice/eugen/E1.010.mp3"
                engineer "I urge you to produce any information as soon as possible. When you have something, please let me know."

            # EI.1b
            "Share what you know.":
                $ engApproval += 1

                show captain confusion-open behind engineer
                voice "voice/captain/C1.038.mp3"
                captain "The computer began to glitch after beginning a diagnostic."
                voice "voice/captain/C1.039.mp3"
                captain "It started reciting Walt Whitman before the entire system crashed."

                show engineer neutral
                show captain confusion-closed behind engineer
                voice "voice/eugen/E1.011.mp3"
                engineer "Can’t say I’ve ever heard of something like this; but, everything has a fix."
                voice "voice/eugen/E1.012.mp3"
                engineer "I’ll begin looking into this immediately."
        
        show engineer neutral
        show captain confusion-closed behind engineer      

        voice "voice/eugen/E1.013.mp3"
        engineer "In the meantime, I’ve reviewed the oxygen depletion curve 3 times now."
        voice "voice/eugen/E1.014.mp3"
        engineer "This is not a random failure. Something is interfering with the system's command execution."

        show captain confusion-open behind engineer    
        voice "voice/captain/C1.040.mp3"    
        captain "What could possibly be interfering? Everything on this mission has been smooth thus far." 
        voice "voice/captain/C1.041.mp3"
        captain "And why the whole system? A function or two, sure those might glitch and need maintenance." 
        voice "voice/captain/C1.042.mp3"
        captain "But what the hell happened to MAD1?"

        # EI.2
        show captain confusion-closed behind engineer

        voice "voice/eugen/E1.015.mp3"
        engineer "We must stay focused, Captain. If we’re to correct this, we must proceed methodically."

        menu: 
            # EI.2a
            "Stand by.":
                $ engApproval -= 1
                show captain anger-open behind engineer
                voice "voice/captain/C1.043.mp3"
                captain "I am proceeding methodically... I need more information first."
                voice "voice/captain/C1.044.mp3"
                captain "Stand by for now."

                #show engineer frustrated
                show captain anger-closed behind engineer
                voice "voice/eugen/E1.016.mp3"
                engineer "As you wish, however, I urge you to think about this decision further."
            
            # EI.2b
            "Make haste.":
                $ engApproval += 1
                show captain confusion-open behind engineer
                voice "voice/captain/C1.045.mp3"
                captain "Make haste but proceed with caution." 
                voice "voice/captain/C1.046.mp3"
                captain "We don’t fully know yet what’s happening, but I trust you to make progress."

                show captain confusion-closed behind engineer
                voice "voice/eugen/E1.017.mp3"
                engineer "Of course, the sooner we address this, the sooner the root of the problem will present itself."

        if seenSI is False:
            menu: 
                "Speak to Sara":
                    show captain neutral-closed behind engineer
                    voice "voice/captain/C1.016.mp3"
                    captain "I should speak to Sara. She’s probably freaking out right now."
                    jump SI

        else:
            jump M1

    label M1:
        scene bg computer
        show computer neutral-1
        show captain neutral-closed behind computer

        voice "voice/madi/M1.019.mp3"
        computer "Welcome back, Captain. Oxygen at 75%%."

        show captain neutral-open behind computer
        voice "voice/captain/C1.047.mp3"
        captain "The Astrobiologist and Cosmotechnician both are on track now to find out what’s wrong with the ship."
        show captain frustrated behind computer
        voice "voice/captain/C1.048.mp3"
        captain "And I guess you… Please don’t break on me again…"
        show captain concern-open behind computer
        voice "voice/captain/C1.049.mp3"
        captain "How’s the ship doing MAD1?"

        show computer processing-1
        show captain concern-closed behind computer
        voice "voice/madi/M1.020.mp3"
        computer "Assessing ship systems…"
        show computer processing-2
        show captain concern-closed behind computer
        voice "voice/madi/M1.021.mp3"
        computer "Processi̶̒͜n̵͖̕ġ̷͍ġ̷͍ġ̷͍-"

        scene bg computer error
        show computer error-1
        show captain confusion-closed behind computer with hpunch 
        voice "voice/madi/M1.022.mp3"
        computer "Water, water, every where,
                    And all the boards did shrink;
                    Water, water, every where,
                    Nor any drop to drink."
        
        show captain confusion-open behind computer with hpunch 
        voice "voice/captain/C1.050.mp3"
        captain "More poems? MAD1 I can’t lose you right now!"

        scene bg computer
        show computer reboot-1
        show captain confusion-closed behind computer
        voice "voice/madi/M1.024.mp3"
        computer "Rebooting.{w=0.5}{nw}"
        show computer reboot-2
        show captain confusion-closed behind computer
        voice "voice/madi/M1.024.mp3"
        computer "Rebooting.{w=0.5}{nw}"
        show computer reboot-3
        show captain confusion-closed behind computer
        voice "voice/madi/M1.024.mp3"
        computer "Rebooting."
        show computer neutral-2
        show captain confusion-closed behind computer
        voice "voice/madi/M1.023.mp3"
        computer "System functionality at 69%%." 
        voice "voice/madi/M1.025.mp3"
        computer "Apologies, Captain. It seems my software is continuing to deteriorate." 
        voice "voice/madi/M1.026.mp3"
        computer "Something is interfering with the ship systems and my code. I am unable to identify wh̸̥͛a̸͇̋t̶̜̕" 
        voice "voice/madi/M1.027.mp3"
        computer "Captain, I’m afraid my ability to assist you will be limited soon."

        show captain anger-open behind computer with hpunch
        voice "voice/captain/C1.051.mp3"
        captain "Dammit! I can’t afford to have more things break down now."
        voice "voice/captain/C1.052.mp3"
        captain "What am I supposed to do?"

        show computer neutral-3
        show captain anger-closed behind computer
        voice "voice/madi/M1.028.mp3"
        computer "I suggest checking with the crew, Captain. 
            Perhaps they will have answers soon with your ss-ssupp-portt-ttt-"

        show computer error-1 with hpunch
        show captain anger-closed behind computer with hpunch 

        voice "voice/madi/M1.029.mp3"
        computer "The one by toil, the other to complain
                    How far I toil, still farther off from thee."

        show computer error-2
        show captain concern-open behind computer
        voice "voice/captain/C1.053.mp3"
        captain "... How far I toil, indeed."
        voice "voice/captain/C1.054.mp3"
        captain "I hope one of them has found something."
        voice "voice/captain/C1.055.mp3"
        captain "Hang in there MAD1."

        "End of Demo"

    return
