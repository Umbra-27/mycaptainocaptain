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
    
    config.window_hide_transition = None
    config.window_show_transition = None
    config.empty_window = nvl_show_core

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
    play music "Electric_Dawn.mp3"

    scene bg computer with fade

    show computer neutral-1 with dissolve
    show captain neutral-open behind computer with dissolve
    
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
    captain "..."
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
    computer "Pulling error log̶̕s.{nw}"
    voice sustain
    voice "voice/madi/M1.005.3.mp3"
    computer "Ê̴̋͒͠r̵̛̈̏r̸̳̯͎͍̬̊̇̀o̵r̷͘. {nw}" 
    voice sustain
    voice "voice/madi/M1.005.4.mp3"
    computer "Sys̷̖̏ṭ̷̋e̵̗̬͋m̵̩͋̕ṡ̴̨͎ dò̷̧͎͍͇̫͆̕ẃ̵̛̔n̶-{nw}"

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
    show captain thinking behind computer 

    $ seenSI = False
    $ seenEI = False

    menu:
        "Speak to Eugen":
            show captain neutral-open behind computer 
            voice "voice/captain/C1.017.mp3"
            captain "I should speak to Eugen. He’ll probably know what’s happening."
            jump EI 

        "Speak to Sara":
            show captain neutral-open behind computer 
            voice "voice/captain/C1.016.mp3"
            captain "I should speak to Sara. She’s probably freaking out right now."
            jump SI
        
    
    label SI:
        $ seenSI = True
        scene bg medic with fade
        show medic nervous with dissolve 
        pause(0.5)
        show captain neutral-closed behind medic with dissolve

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
        scene bg engineer with fade
        show engineer neutral with dissolve
        pause(0.5)
        show captain neutral-closed behind engineer with dissolve

        show captain neutral-open behind engineer
        voice "voice/captain/C1.034.mp3"
        captain "How’re you holding up Eugen?"

        show captain neutral-closed behind engineer
        voice "voice/eugen/E1.003.mp3"
        engineer "As well as one can, given the circumstances." 
        voice "voice/eugen/E1.004.mp3"
        show engineer thinking
        engineer "May we skip the pleasantries? I dislike small talk." 
        voice "voice/eugen/E1.005.mp3"
        show engineer neutral
        engineer "I’m sure Sara would appreciate it more."

        show captain neutral-open behind engineer
        voice "voice/captain/C1.035.mp3"
        captain "Got it... Straight to the point then. Report."

        show engineer thinking
        show captain neutral-closed behind engineer
        voice "voice/eugen/E1.006.mp3"
        engineer "Captain, the situation is not ideal. There appears to be a system failure on a magnitude I’ve never seen."
        voice "voice/eugen/E1.007.mp3"
        engineer "I am looking into it, however, little progress is being made."
        voice "voice/eugen/E1.008.mp3"
        engineer "At the rate we’re losing oxygen, I estimate that we have approximately one hour."
        
        show engineer neutral
        show captain frustrated behind engineer
        voice "voice/captain/C1.036.mp3"
        captain "Shit… Well there goes my hope for any good news."

        # EI.1
        show engineer thinking
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
                show engineer stressed
                show captain thinking behind engineer
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
        
        show engineer thinking
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
        show engineer neutral
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

                show engineer stressed
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

                show engineer thinking
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
        scene bg computer with fade
        show computer neutral-1 with dissolve
        show captain neutral-closed behind computer with dissolve

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
        computer "Water, wả̵̳t̷̨̍e̴͚̔r̵̥̉, every where,
                    And all the boards did shrink;
                    Water, ẉ̸̢̟͑ͅą̷̓͝tĕ̵͈̗̆͒̚r̷̢̼͈͚̈́̐, eve̴̤̚r̷̈́y̴͉̌ ̵̦̈́ẁ̸̺h̵̻̿e̸͉̋ŗ̵̈́e̸̛̝,
                    Nor a̴̞̓ǹ̷̢y̷̾ͅ ̵̡̐d̸̟̄ȓ̶̼o̷̻͒p̴̛̦ ̵̦̈́t̵̨͝ó̴̝ ̸̜͋d̸̝̑rī̶̻n̵̺̍ḱ̴͍."
        
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
        computer "Something is interfering with the ship systems and my code. I am unable to identify wha̸͇̋t̶̜̕" 
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
            Perhaps they will have answers soon with your ss-ssupp̷̞̏-pǫ̸̊ȑ̸̨t̷͎̎t̷͎̎-t̷̠̆t̵̞̓t̴̘͑-"

        show computer error-1 with hpunch
        show captain anger-closed behind computer with hpunch 

        voice "voice/madi/M1.029.mp3"
        computer "The one by toi̷l̵, the other to comp̸̖̓l̴͎̀a̴̺͗ì̴̩n
                    How far I t̴̡̃o̴̳͒i̶̥͋l̶̮̍, still farther ó̷̖ff f̵̲͒ȑ̷͉o̵̮̓m̴̮̌ ̶͓̈́t̷͎̑h̶̏e̶e̶̻̔."

        show computer error-2
        show captain concern-open behind computer
        voice "voice/captain/C1.053.mp3"
        captain "... How far I toil, indeed."
        voice "voice/captain/C1.054.mp3"
        captain "I hope one of them has found something."
        voice "voice/captain/C1.055.mp3"
        captain "Hang in there MAD1."

        show captain thinking behind computer
        $ seenS1 = False
        $ seenE1 = False
        menu:
            "Speak to Eugen":
                jump E1 

            "Speak to Sara":
                jump S1

    label S1:
        $ seenS1 = True
        $ seenE1 = False
        scene bg medic with fade
        show medic nervous with dissolve 
        pause(0.5)
        show captain neutral-closed behind medic with dissolve

        medic "Captain, I have gone over my notes as requested. But first… can I know what is going on? What did Eugen say?"

        # S.1.1
        show captain neutral-open behind medic
        captain "We are looking into it."

        menu: 
            # S.1.1a
            "The situation is dire.":
                $ medApproval -= 1
                show captain concern-open behind medic
                captain "I have to be honest with you, Sara." 
                captain "The situation is more dire than we thought. But I need you to remain calm."

            # S.1.1b
            "I have hopes we’d sort it out soon.":
                $ medApproval += 1
                show captain neutral-open behind medic
                captain "I have hopes that we will sort it out soon." 
                captain "Thank you for fulfilling my request."

        show medic thinking
        show captain neutral-closed behind medic
        medic "Yes, um, w-would you like to hear what my theory is?"

        show captain neutral-open behind medic
        captain "Enlighten me."

        show medic explaining
        show captain neutral-closed behind medic
        medic "This specimen is not a lifeform as we know it. Life is, after all, undefined."
        medic "It’s uniquely adapted to the cold and dark of Europa’s ocean. "
        show medic excited
        show captain neutral-closed behind medic
        medic "I’ve been thinking of life in Earth’s ocean, and the closest equivalent is a marine fungus. "
        show medic neutral
        show captain neutral-closed behind medic
        medic "However, the Earth's marine fungi are largely microscopic."
        
        show captain thinking behind medic
        captain "It’s gotta be incredibly resilient to survive those conditions…"

        show medic explaining
        show captain thinking behind medic
        medic "Indeed. Even on Earth, we have extremophiles. The tardigrade is a good example. "
        show medic nervous 
        show captain thinking behind medic
        medic "As exciting and era-defining as this discovery is, I must say… I’m worried for our survival. "
        medic "Captain, we’ve never experienced anything like this! What if–"  
        
        show captain frustrated behind medic
        captain "Sara, we went over this…"
        
        show medic stressed
        medic "Okay… How is Eugen doing? Is he alright?"
        
        show captain neutral-open behind medic
        captain "He’s doing alright. He’s looking into the problem."

        # S.1.2
        show medic nervous 
        show captain neutral-closed behind medic
        medic "I just… I wonder if I’d get to see my family again."

        menu: 
            # S.1.2a
            "It’s a risk we signed up for.":
                $ medApproval -= 1
                show medic thinking
                show captain anger-open behind medic
                captain "That risk is always there. Part of the job." 
                captain "This mission was never meant to be easy."

                show medic nervous
                show captain anger-closed behind medic
                medic "Yes, yes, I know…"

            # S.1.2b
            "I will do my best to get us home.":
                $ medApproval += 1
                show medic thinking
                show captain concern-open behind medic
                captain "I will do my best to make sure that this mission is successful and everyone gets home."

                show medic excited
                show captain concern-closed behind medic
                medic "Thank you…I know you will."
                
                show medic nervous     
                show captain concern-closed behind medic                   
   
        medic "Anyway, Now that we have this specimen, I absolutely must make it back home… I have to return to my family…" 

        show captain neutral-open behind medic
        captain "What do you mean?"

        show medic thinking
        show captain neutral-closed behind medic
        medic "Mmmh… Let’s just say that my family has certain expectations of a woman…"
        medic "Always been like that." 

        show captain concern-open behind medic
        captain "Your achievements are more than average to say the least. Is that not enough?" 
        captain "Your family should be proud of you regardless of the outcome of this mission."

        show medic neutral
        show captain concern-closed behind medic
        medic "I’m just a lone woman who’s devoted my life to the sciences." 
        medic "Not everyone views this life as ideal." 
        medic "All the choices I’ve made and the work I’ve done… I’d be lying if I say that I hadn’t doubted it all."
        show medic thinking
        show captain concern-closed behind medic
        medic "But this discovery would change things. It’s worth everything, you know?"

        show captain neutral-open behind medic
        captain "I see…"
        
        show captain neutral-closed behind medic
        medic "Captain, please let me know of any updates as soon as possible? To be honest, it’s difficult to focus…"

        show captain neutral-open behind medic
        captain "I cannot make any promises. This is an emergency situation."

        show medic nervous
        show captain neutral-closed behind medic
        medic "SARA: But can MAD1 not figure out what is happening?"
  
        show captain concern-open behind medic      
        captain "Actually… MAD1 is malfunctioning."

        show medic stressed
        show captain concern-closed behind medic
        medic "Oh my god… It’s worse than I thought!"

        show captain concern-open behind medic  
        captain "Something is interfering with MAD1’s processes. We must keep focused."
        captain "I will let you know once we have something concrete."

        show captain concern-closed behind medic
        medic "It’s just–two new crazy developments on this ship in such a short time!"

        show medic thinking
        show captain concern-closed behind medic
        medic "This amazing specimen and now this event...Everything is interconnected. I have a feeling we’re missing something."

        show captain thinking behind medic
        captain "It is certainly interconnected. The survival of this specimen and our own are tied to the outcome of this crisis."

        # S.1.3
        medic "I-is there anything I can do to help?"

        menu: 
            # S.1.3a
            "Stay put while we sort this out.":
                $ medApproval -= 1
                show captain concern-open behind medic
                captain "We’ll sort this out." 
                captain "Stay calm and do whatever you can."

                show medic stressed
                show captain concern-closed behind medic
                medic "O-okay."

            # S.1.3b
            "Keep studying your notes.":
                $ medApproval += 1
                show captain neutral-open behind medic
                captain "Your work is important to this mission, Sara. And you’ve done excellent so far." 
                captain "Keep studying your notes."
                                
                show medic excited
                show captain neutral-closed behind medic
                medic "Will do, Captain!"
        
        jump M2

    label E1:
        $ seenE1 = True
        $ seenS1 = False
        scene bg engineer with fade
        show engineer neutral with dissolve
        pause(0.5)
        show captain neutral-closed behind engineer with dissolve

        engineer "I must be transparent with you."

        show captain neutral-open behind engineer
        captain "Alright, shoot."

        show captain neutral-closed behind engineer
        engineer "I’ve navigated through MAD1’s system to find the virus."
        engineer "The core system architecture is… not a standard framework."

        show captain neutral-open behind engineer
        captain "How do you mean?"

        show engineer thinking
        show captain neutral-closed behind engineer
        engineer "It’s layered. Recursive even. "
        engineer "It appears to be self-protective."

        show captain confusion-open behind engineer
        captain "Can’t you normally manually bypass these things through administrative controls?"

        engineer "This ship is not programmed to the industry standard."

        show captain rememberance-open behind engineer
        captain "Right. He… liked things his own way."

        # E1.1
        engineer "When Matthew built this system, did he ever share hidden contingencies? System overrides?"
        engineer "If there is something embedded in this code that only you would recognize, now is the time to share."

        menu:
            # E1.1a
            "He did not.":
                $ engApproval += 1

                show captain thinking behind engineer
                captain "If he… If Matthew wrote any contingencies, he didn’t share them outright with me, unfortunately."
                
                show engineer neutral
                show captain thinking behind engineer
                engineer "I can’t say that's ideal; however, this does help with what needs to be looked into."

            # EI.1b
            "I don’t know yet.":
                $ engApproval -= 1

                show captain anger-open behind engineer 
                captain "Are you implying I’m hiding things from you? Sabotaging the mission?"
                
                show engineer stressed
                show captain anger-closed behind engineer 
                engineer "My only concern is accomplishing this mission with minimal complexities." 
                engineer "If you have information, I’m only asking that you share."

        show engineer neutral
        engineer "Every time I attempt to reroute life support through the auxiliary control, the command is intercepted."

        show captain concern-open behind engineer
        captain "Intercepted? By what?"
        
        show engineer thinking
        show captain concern-closed behind engineer
        engineer "There is a line of defence that, according to standard protocol, should not exist."
        engineer "I’ve reviewed the ship's schematics. This layer of defence is handwritten."
        engineer "Written in a way where the logic only makes sense to specific personnel."

        show captain thinking behind engineer 
        captain "… I see."

        engineer "There is a lack of documentation, no engineering notes; it is the equivalent of a ghost layer in the system."

        show captain neutral-open behind engineer
        captain "Surely your — let’s say engineering intuition — can crack it though?"
        
        show engineer neutral
        show captain neutral-closed behind engineer
        engineer "I do not design systems that require intuition to operate."
        engineer "Systems should be universal. Transferable… Understandable."
        engineer "This one seems to be able to answer only to him."

        show captain frustrated behind engineer
        captain "..."

        # E1.2
        show engineer thinking
        engineer "Did he trust you with everything? Or did he keep parts of this ship's secrets to himself?"

        menu:
            # E1.2a
            "He was the programmer, not me.":
                $ engApproval -= 1

                show captain anger-open behind engineer
                captain "Listen, I’m not a programmer." 
                captain "He wouldn’t have shared anything like that with me."

            # EI.2b
            "He really liked poetry.":
                $ engApproval += 1

                show captain thinking behind engineer
                captain "Matthew was a fan of poetry." 
                captain "MAD1 recited another verse after I visited you last. There could be something in that."

        show engineer neutral
        engineer "I have been a part of many missions and projects where my life was on the line."
        engineer "Each time, I never considered the possibility of anyone dying."

        show captain neutral-open behind engineer
        captain "I’m sure none of us have."

        show engineer thinking
        show captain neutral-closed behind engineer
        engineer "Each one of these assignments, I knew that with structure and protocol, our lives were safe."
        engineer "This is the first time in my long, calculated life…"
        engineer "… where I am starting to believe there may be enough cracks in our protocol for everything to fall apart."

        show captain concern-open behind engineer
        captain "Cracks we apparently can’t fill."

        show engineer neutral
        show captain concern-closed behind engineer
        engineer "Under normal conditions, I could dismantle and rebuild any system on this vessel."
        engineer "However, the only person who truly understood the depth of this architecture… was him."

        captain "…"

        engineer "I am determined to not let this system get the better of me. As unorthodox as it is, I know I can salvage the situation."
        engineer "Unfortunately, I do not know how to safely override it without risking total collapse."

        # E1.3

        show engineer thinking
        show captain neutral-closed behind engineer
        engineer "Eugen: Tell me something, Captain…"
        engineer "If Matthew were standing here instead of me… do you believe he would know what to do? "
        menu:
            # E1.3a
            "That doesn’t matter right now.":
                $ engApproval -= 1

                show captain anger-open behind engineer
                captain "That does not matter right now. Why would you ask me that?!"
                captain "Just… figure something out."
                
                show captain anger-closed behind engineer

            # EI.3b
            "Yes.":
                $ engApproval += 1

                show captain neutral-open behind engineer
                captain "Yes. He would." 
                captain "But as far as I can tell he’s not here anymore." 
                captain "So get it together and figure it out." 
                show captain neutral-closed behind engineer
                captain "That’s an order."

        show engineer neutral
        show captain neutral-closed behind engineer
        engineer "The mission has been going smoothly up until now."
        engineer "My equipment, my design, we have seen it in action. There were no shortcomings; this is how all things should be."
        engineer "If this mission fails, just know it wasn’t from my contribution."

        jump M2

    label M2:
        scene bg computer with fade
        show computer neutral-1 with dissolve
        show captain frustrated behind computer with dissolve

        captain "(sigh)"

        computer "Greetings, my̸̛̝̎ love̵̦͆͑̚ͅě̸̦͝͝e̸̘͋, Captain."

        show captain concern-open behind computer
        captain "What? MAD1 what the fuck?"

        scene bg computer error
        show computer error-1
        show captain concern-closed behind computer
        computer "Errorr. Error. Errorrrr."
        computer "langu̴̢͘age e̶̯̓r̴̺̀r̶̙̀o̶̖̚r"
        computer "S̵p̶̳͘ē̵̝e̴̼̓c̷̫̎ḧ̴̫́ ̷̗̀e̵̗̋rr̸̦̀o̶̳͑ṙ̸͇rr"
        computer "P̸͇̓r̶̲̳̣̈o̷͎̬͂̋c̸͈̠̤̓̅̓é̷͚̦̳̠s̵͚̐s̴̡͍̟̈́̊̌i̶̲̟̎̀̂͠ng E̷r̸r̸o̶r̸.̶—"

        scene bg computer error bad
        show computer error-2
        show captain concern-closed behind computer
        computer "I watered it in fears,
                Night and morning with my tears.
                And it grew both day and night,
                Till it bore an apple bright."
        computer "But, with a soft deceitful soul,
                into my garden it stole.
                When the night had veiled the pole.
                My friend, lost beneath the tree."

        show captain anger-open behind computer with hpunch
        captain "Another one?! God damnmit! (Slams terminal)"

        scene bg computer
        show computer reboot-1
        show captain anger-closed behind computer
        computer "Rebootinggg.{w=0.3}{nw}"
        show computer reboot-2
        computer "Rebootinggg.{w=0.3}{nw}"
        show computer reboot-3
        computer "Rebootinggg." 
        show computer neutral-1
        show captain anger-closed behind computer
        computer "System functionality at 24%%."
        computer "Oxygen at 50%%. Captain, it may be time to plan for the worst case scenario."
        show computer neutral-2
        show captain anger-closed behind computer
        computer "You may want to consider who it would be best to give clearance for the escape pod."
        computer "The escape pod has capacity for only one person."

        show captain confusion-open behind computer
        captain "... What?"

        show computer neutral-3
        show captain confusion-closed behind computer
        computer "The escape pod has capacity for-"

        show captain anger-open behind computer with hpunch
        captain "NO I HEARD YOU THE FIRST TIME!"
        captain "(Laboured breathing)"

        show computer neutral-1
        computer "Apologies, Captain. But you mustttt-"

        show computer error-1 with hpunch
        show captain
        computer "Ah! Well- a-day! what evil looks
                Had thee from old and young!
                Instead of the cross, the Albatross
                About thy neck was hung."
        jump C1

    label C1:
        scene bg escape pod with fade

        captain "No. No…"
        show bg escape pod with hpunch
        captain "How the fuck am I meant to choose one life over another?! How am I supposed to decipher all of this… poetry?"

        if seenS1 is True:
            captain "Aghh! Someone has to go home with the specimen."
            captain "Potential alien life is too important not to study."
            captain "Matthew died for this!"

        elif seenE1 is True:
            captain "*sighs* Eugen’s right. Matthew would know what to do."
            captain "If it wasn’t for that fucking asteroid we wouldn’t even be here right now."

        captain "We can’t—I can’t fail now. Not when we’re so fucking close."
        captain "God if I had him here with me this would—"
        captain "Matthew… What do I do..?"
        
        captain "I… I could just leave right now… Be done with it… Be with him…"
        menu:
            "Escape":
                jump EndC
            
            "No, I can't leave.":
                captain "No, I can't leave."
                captain "…"
                
                show bg escape pod with hpunch
                captain "(slams fist on escape pod)"
                captain "(sharp inhale) Get it together Rudy. Your crew needs you to focus up and get us out of here."
                captain "We’ll all make it home. We need to make it home."

    label EndC:
        nvl clear
        
        init python:
            config.window_hide_transition = dissolve
            config.window_show_transition = dissolve

        window hide
        scene ending captain with fade
        pause(1.0)
        window show

        "He rose the morrow morn.
        A sadder and a wiser man.
        He went like one that hath been stunned,
        And is of sense forlorn:
        The Captain, whose eye is dark,
        Whose beard with age is hoar,
        Is gone."

    return
