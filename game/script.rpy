# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define captain = Character("Captain", image="captain@3.5/captain", kind=bubble)
define engineer = Character("Eugen", image="engineer placeholder", kind=bubble)
define medic = Character("Sara", image="medic/medic", kind=bubble)
define computer = Character("MAD1", image="computer/computer", kind=bubble)

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

    captain "Captain’s Log — September 24th." 
    captain "We’ve successfully drilled through the ice layer of Europa and retrieved an 
                artifact that resembles life. Short on time, we’ve started the course back 
                to Earth."
    captain "Dr. Fernando’s begun studying the artifact. I’ve ordered her to confirm the 
                form of life, and Technician Braun’s been commanded to 
                conduct maintenance on the equipment in the bio-lab." 

    play sound "m4d1_notification.mp3"
    show computer neutral-2
    show captain neutral-closed behind computer

    computer "Message from Cosmotechnician Eugene Braun. Open message?"

    menu:
        "Open message":
            show captain neutral-open behind computer
            captain "Open and read."

    play sound "m4d1_message_open.mp3"
    show computer neutral-3
    show captain neutral-closed behind computer

    computer "Engineer: Commander, I have been reviewing the bio lab’s system; the data does not align with standard 
                operating parameters." 
    computer "This does not appear to be a malfunction or human error; there seems to be an 
                interference with the processes. It will be best to address this immediately."

    show captain frustrated behind computer
    captain "(Sighs, rubs temples)"
    captain "MAD1, run ship diagnostics."

    show computer processing-1
    computer "Initiating system diagnostics. Analyzing running operations."

    play sound "system_diagnostic_start.mp3"
    show computer processing-2

    show captain rememberance-closed behind computer

    show computer processing-3
    captain "This is probably my fault… I made us take an extra day travelling to find his ship. I’m rushing us home to return on time."

    play sound "electric_oh_no.mp3"
    show computer error-1
    computer "Error. Process failure." 
    show computer processing-1
    computer "Reinitiating process." 
    show computer processing-2
    show computer processing-3
    show computer error-1
    computer "Error. System failure."
    
    scene bg computer error
    show computer error-1
    show captain confusion-closed behind computer
    
    stop music fadeout 1.0
    play sound "error_sound_1.mp3"
    computer "Error. Error. E̷̠̓r̷̖͆r̵̼͋o̷̳̔r"

    show captain confusion-open with hpunch 
    captain "What’s happening? MAD1, show me the error logs."

    scene bg computer error bad
    show computer error-1
    show captain confusion-closed behind computer

    computer "Error. Unable to end process." 
    play sound "error_sound_2.mp3"
    computer "Pulling error log̶̕s.{w=0.5}{nw}"
    computer "Ê̴̋͒͠r̵̛̈̏r̸̳̯͎͍̬̊̇̀o̵r̷͘. {w=0.3}{nw}" 
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

    computer "But O heart! heart! H̷̢̚e̷a̵ŕ̶̤t̵͈́!̵̺̾
                O the b̵̝̀l̷̨͠e̶̹̕ȩ̵̔d̴̲̅i̶n̵̕ġ̷͍ drops of red,
                Where on the deck my Captain lies,
                Fallen cold and d̸̻̈́e̵͉̋a̸̪̿d̸̙͆."

    "The terminal displays strange text. I’ve never seen MAD1 act this way before."

    show captainConfusedOpenDark behind computer
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

    computer "System force restart. Diagnostics complete." 
    show computer neutral-1
    computer "Power systems offline. Emergency power engaged." 
    computer "Navigation systems paused." 
    computer "Internal communications offline." 
    show computer neutral-2
    computer "Satellite communication offline." 
    computer "Data systems offline." 
    computer "Thermal control offline." 
    show computer neutral-3
    computer "Oxygen system offline." 
    computer "Emergency Life support protocol engaged."

    show captain anger-open behind computer 
    captain "MAD1, what the hell is going on?"

    show captain anger-closed behind computer 

    computer "Mission status paused. To preserve power and life support, non-essential rooms have been sealed. Oxygen will be rerouted."

    play sound "captain_smack_2.mp3" 

    captain "(Slams fist on table)" with hpunch 
    show captain anger-open behind computer
    captain "Right now? In the most important phase of this mission?"
    
    show captain anger-closed behind computer 

    computer "Captain, I recommend checking on the crew to maintain morale and investigate the cause of the system failure."

    show captain frustrated behind computer 
    captain "(Sighs)" 
    show captain neutral-open behind computer 
    captain "I suppose you’re right. Give me periodic reports on the oxygen levels."
    show captain neutral-closed behind computer 

    computer "Aye, aye, Captain. Oxygen levels at 99%%."

    show captain frustrated behind computer 
    captain "..." 
    captain "Thanks..."
    show captain neutral-open behind computer 
    captain "Let’s check on the crew."
    show captain neutral-closed behind computer 

    $ seenSI = False
    $ seenEI = False

    menu:
        "Speak to Eugen":
            captain "I should speak to Eugen. He’ll probably know what’s happening."
            jump EI

        "Speak to Sara":
            captain "I should speak to Sara. She’s probably freaking out right now."
            jump SI
        
    
    label SI:
        $ seenSI = True
        scene bg medic
        show medic nervous
        show captain neutral-closed behind medic

        medic "Captain! W-what just happened! Thank goodness you arrived when you did. I was going to—" 
        
        show captain neutral-open behind medic
        captain "Yes, quite unexpected. I’m sorting it out with Eugen." 
        captain "We’ve had good luck so far—we’ve achieved something no man has managed before. These things happen."

        show medic neutral
        show captain neutral-closed behind medic
        medic "Yes, yes, of course!" 

        show medic explaining
        show captain neutral-closed behind medic
        medic "I mean, this cargo—this discovery—would revolutionize everything." 
        medic "Our very understanding of the universe. Extraterrestrial life! Aboard this ship." 
        show medic excited
        show captain neutral-closed behind medic
        medic "I still can’t believe it." 
        show medic neutral
        show captain neutral-closed behind medic
        medic "But this… development is most concerning." 

        show medic nervous
        show captain neutral-closed behind medic
        medic "What could possibly be happening, Captain?" 
        medic "Could it—could this result in some kind of irreparable, cascading failure?"

        show captain neutral-open behind medic
        captain "Like I said before, Sara, we’ll find out soon. There is no reason to assume the worst." 

        show captain neutral-closed behind medic
        medic "I understand. I just—given what has happened before…"

        show captain anger-open behind medic
        captain "What happened to the previous mission has nothing to do with what is happening now."

        # SI.1
        show medic stressed
        show captain anger-closed behind medic
        medic "I’m sorry. I-I guess I’ve always felt you were easier to talk to on this ship." 
        medic "I admit this incident isn’t making me think straight. I shouldn’t have brought it up." 
        medic "I understand it must be painful for you—"

        menu:
            # SI.1.a
            "We’re all stressed.":
                $ medApproval += 1

                show captain concern-open behind medic
                captain "It’s okay, Sara. This is stressful for all of us."

                show medic neutral
                show captain concern-closed behind medic
                medic "This is true, I apologize for bringing it up."

            # SI.1.b
            "It’s fine.":
                $ medApproval -= 1

                show captain anger-open behind medic
                captain "It’s fine. Just don’t do it again."

                show medic stressed
                show captain anger-closed behind medic
                medic "I’m sorry, Captain. I’ll just, um…"

        show captain neutral-open behind medic
        captain "How about you go through your notes so far?"
        captain "We could use any theories on what this specimen is and its properties."

        show medic excited
        show captain neutral-closed behind medic
        medic "Yes, yes… I already have working hypotheses, though nothing exactly seems to work out perfectly at the moment."
        
        show medic nervous
        show captain neutral-closed behind medic
        medic "I should work harder…"

        show captain concern-open behind medic
        captain "Sara, you’re already working very hard."
        captain "You’re the best in the field. Remember; it’s why we have you on this mission."

        show medic neutral
        show captain concern-closed behind medic
        medic "Thank you, Captain. I can’t overstate how much this mission means to me."
        show medic excited
        show captain concern-closed behind medic
        medic "This—this specimen we’ve found is the holy grail of astrobiology."

        show captain neutral-open behind medic 
        captain "And that’s exactly why I need you to tell us what we’re dealing with here."
        captain "I’m counting on you Sarah."
        captain "We’ll get the system back up one way or another."

        # SI.2
        show medic stressed
        show captain neutral-closed behind medic
        medic "But my research is in the system. How long will it take?" 
        medic "All I have to work with is my journal." 
        medic "I-if this takes a long time, what am I supposed to do?"
        
        show medic nervous
        show captain neutral-closed behind medic

        menu:
            # SI.2.a
            "You can figure it out.":
                $ medApproval -= 1
                
                show captain anger-open behind medic
                captain "Figure it out. That’s an order."

                show medic stressed
                show captain anger-closed behind medic
                medic "O-of course Captain."

            # SI.2.b
            "I have faith in you." :
                $ medApproval += 1
                
                show captain neutral-open behind medic
                captain "I can’t say for sure, but I’ve seen you work with less before."
                captain "I expect you’d gain more insight once you study your notes. I have faith in you."

                show medic neutral
                show captain neutral-closed behind medic
                medic "I won’t let you down!"

        if seenEI is False:
            menu: 
                "Speak to Eugen":
                    show captain neutral-closed behind medic
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
        captain "How’re you holding up Eugen?"

        show captain neutral-closed behind engineer
        engineer "As well as one can, given the circumstances." 
        engineer "May we skip the pleasantries? I dislike small talk." 
        engineer "I’m sure Sara would appreciate it more."

        show captain neutral-open behind engineer
        captain "Got it... Straight to the point then. Report."

        show captain neutral-closed behind engineer
        engineer "Captain, the situation is not ideal. There appears to be a system failure on a magnitude I’ve never seen."
        engineer "I am looking into it, however, little progress is being made."
        engineer "At the rate we’re losing oxygen, I estimate that we have approximately one hour."
        
        show captain frustrated behind engineer
        captain "Shit… Well there goes my hope for any good news."

        # EI.1
        show captain neutral-closed behind engineer
        engineer "Is there any information you can provide? Do you know what might have caused this?"

        menu:
            # EI.1a
            "I’m not sure yet.":
                $ engApproval -= 1
                show captain thinking behind engineer
                captain "I’m not sure yet. I want to find out a bit more before I give any concrete answers."

                # show engineer frustrated
                # show captain thinking behind engineer
                engineer "I urge you to produce any information as soon as possible. When you have something, please let me know."

            # EI.1b
            "Share what you know.":
                $ engApproval += 1

                show captain confusion-open behind engineer
                captain "The computer began to glitch after beginning a diagnostic."
                captain "It started reciting Walt Whitman before the entire system crashed."

                show engineer neutral
                show captain confusion-closed behind engineer
                engineer "Can’t say I’ve ever heard of something like this; but, everything has a fix."
                engineer "I’ll begin looking into this immediately."
        
        show engineer neutral
        show captain confusion-closed behind engineer      

        engineer "In the meantime, I’ve reviewed the oxygen depletion curve 3 times now."
        engineer "This is not a random failure. Something is interfering with the system's command execution."

        show captain confusion-open behind engineer        
        captain "Captain.040: What could possibly be interfering? Everything on this mission has been smooth thus far." 
        captain "And why the whole system? A function or two, sure those might glitch and need maintenance." 
        captain "But what the hell happened to MAD1?"

        # EI.2
        show captain confusion-closed behind engineer

        engineer "We must stay focused, Captain. If we’re to correct this, we must proceed methodically."

        menu: 
            # EI.2a
            "Stand by.":
                $ engApproval -= 1
                show captain anger-open behind engineer
                captain "I am proceeding methodically... I need more information first."
                captain "Stand by for now."

                #show engineer frustrated
                show captain anger-closed behind engineer
                engineer "As you wish, however, I urge you to think about this decision further."
            
            # EI.2b
            "Make haste.":
                $ engApproval += 1
                show captain confusion-open behind engineer
                captain "Make haste but proceed with caution." 
                captain "We don’t fully know yet what’s happening, but I trust you to make progress."

                show captain confusion-closed behind engineer
                engineer "Of course, the sooner we address this, the sooner the root of the problem will present itself."

        if seenSI is False:
            menu: 
                "Speak to Sara":
                    show captain neutral-closed behind engineer
                    captain "I should speak to Sara. She’s probably freaking out right now."
                    jump SI

        else:
            jump M1

    label M1:
        scene bg computer
        show computer neutral-1
        show captain neutral-closed behind computer

        computer "Welcome back, Captain. Oxygen at 75%%."

        show captain neutral-open behind computer
        captain "The Astrobiologist and Cosmotechnician both are on track now to find out what’s wrong with the ship."
        show captain frustrated behind computer
        captain "And I guess you… Please don’t break on me again…"
        show captain concern-open behind computer
        captain "How’s the ship doing MAD1?"

        show computer processing-1
        show captain concern-closed behind computer
        computer "Assessing ship systems…"
        show computer processing-2
        show captain concern-closed behind computer
        computer "Processi̶̒͜n̵͖̕ġ̷͍ġ̷͍ġ̷͍-"

        scene bg computer error
        show computer error-1
        show captain confusion-closed behind computer with hpunch 
        computer "Water, water, every where,
                    And all the boards did shrink;
                    Water, water, every where,
                    Nor any drop to drink."
        
        show captain confusion-open behind computer with hpunch 
        captain "More poems? MAD1 I can’t lose you right now!"

        scene bg computer
        show computer reboot-1
        show captain confusion-closed behind computer
        computer "Rebooting.{w=0.5}{nw}"
        show computer reboot-2
        show captain confusion-closed behind computer
        computer "Rebooting.{w=0.5}{nw}"
        show computer reboot-3
        show captain confusion-closed behind computer
        computer "Rebooting."
        show computer neutral-2
        show captain confusion-closed behind computer
        computer "System functionality at 69%%." 
        computer "Apologies, Captain. It seems my software is continuing to deteriorate." 
        computer "Something is interfering with the ship systems and my code. I am unable to identify wh̸̥͛a̸͇̋t̶̜̕" 
        computer "Captain, I’m afraid my ability to assist you will be limited soon."

        show captain anger-open behind computer with hpunch
        captain "Dammit! I can’t afford to have more things break down now."
        captain "What am I supposed to do?"

        show computer neutral-3
        show captain anger-closed behind computer
        computer "I suggest checking with the crew, Captain." 
        computer "Perhaps they will have answers soon with your ss-ssupp-portt-ttt-"

        show computer error-1 with hpunch
        show captain anger-closed behind computer with hpunch 

        computer "The one by toil, the other to complain
                    How far I toil, still farther off from thee."

        show computer error-2
        show captain concern-open behind computer
        captain "... How far I toil, indeed."
        captain "I hope one of them has found something."
        captain "Hang in there MAD1."

        "End of Demo"

    return
