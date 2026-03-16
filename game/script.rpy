# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define captain = Character("Captain", image="captain@3.5/captain", kind=bubble)
define engineer = Character("Eugen", image="engineer/engineer", kind=bubble)
define medic = Character("Sara", image="medic/medic", kind=bubble)
define computer = Character("MAD1", image="computer/computer", kind=bubble)

# Sound Settings
default preferences.volume.music = 0.8
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
    seenSaraSolution = False
    seenEugenSolution = False

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

    captain "Captain’s Log — September 24th." 

    captain "Eugen Braun’s drill apparatus was successful in piercing through the ice 
                layer of one of Jupiter’s moons, Europa."
    captain "From its ocean, we’ve retrieved a specimen that resembles life."
    captain "Short on time, we’ve started the course back 
                to Earth."
    captain "Dr. Sara Fernando’s begun studying the specimen. I’ve ordered 
                her to confirm the form of life." 
    captain "Technician Braun’s been commanded to conduct maintenance on 
                the equipment in the bio-lab." 

    play sound "m4d1_notification.mp3"
    show computer neutral-2
    show captain neutral-closed behind computer

    computer "Message from Cosmotechnician Eugen Braun. Open message?"

    menu:
        "Open message":
            play sound "audio/Button_Select.mp3" volume 0.8
            show captain neutral-open behind computer
            captain "Open and read."

    play sound "m4d1_message_open.mp3" 
    show computer neutral-3
    show captain neutral-closed behind computer

    computer "Engineer: Captain, I have been reviewing the bio lab’s system; the data does not align with standard 
                operating parameters." 
    computer "Engineer: This does not appear to be a malfunction or human error; there seems to be an 
                interference with the processes."
    computer "It will be best to address this immediately."

    show captain frustrated behind computer
    captain "..."
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
    computer "Error. Process failure.{w=0.5}" 
    show computer processing-1
    voice sustain
    computer " Reinitiating process.{w=0.5}" 
    show computer processing-2
    show computer processing-3
    show computer error-1
    voice sustain
    computer " Error. System failure.{w=0.5}"
    
    scene bg computer error
    show computer error-1
    show captain confusion-closed behind computer
    
    stop music fadeout 1.0
    play sound "error_sound_1.mp3"
    voice sustain
    computer " Error. Error. E̷̠̓r̷̖͆r̵̼͋o̷̳̔r{w=0.5}{nw}"

    show captain confusion-open with hpunch 
    captain "What’s happening? MAD1, show me the error logs."

    scene bg computer error bad
    show computer error-1
    show captain confusion-closed behind computer

    computer "Error. Unable to end process." 
    play sound "error_sound_2.mp3"
    voice sustain
    computer "Pulling error log̶̕s.{w=0.5}{nw}"
    voice sustain
    computer "Ê̴̋͒͠r̵̛̈̏r̸̳̯͎͍̬̊̇̀o̵r̷͘. {w=0.2}{nw}" 
    voice sustain
    computer "Sys̷̖̏ṭ̷̋e̵̗̬͋m̵̩͋̕ṡ̴̨͎ dò̷̧͎͍͇̫͆̕ẃ̵̛̔n̶-{w=0.2}{nw}"

    stop sound
    play sound "systems_off.mp3"
    scene bgCompDark
    pause(1)
    show computer error-2
    show captainConfusedClosedDark behind computer

    "The lights go out. Everything stops." 
    "The buzz and rumbles of the ship go deadly silent, and it’s as if time and space have frozen solid." 
    "Only one terminal blinks online."

    computer "But O heart! heart! H̷̢̚e̷a̵ŕ̶̤t̵͈́!̵̺̾"
    computer "O the b̵̝̀l̷̨͠e̶̹̕ȩ̵̔d̴̲̅i̶n̵̕ġ̷͍ drops of red,"
    computer "Where on the deck my Captain lies,"
    computer "Fallen cold and d̸̻̈́e̵͉̋a̸̪̿d̸̙͆."

    "The terminal displays strange text. I’ve never seen MAD1 act this way before."

    show captainConfusedOpenDark behind computer
    captain "What the hell?" 
    
    show captainConfusedClosedDark behind computer   
    play sound "captain_smack_1.mp3" 
    captain "(Smacks terminal)" with hpunch 

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
    computer "2 of 3 escape pods malfunctioning."

    show captain anger-open behind computer 

    captain "MAD1, what the hell is going on?"

    show captain anger-closed behind computer 

    computer "Mission status paused. To preserve power and life support, non-essential rooms have been sealed. Oxygen will be rerouted."

    play sound "captain_smack_2.mp3" 

    captain "(Slams fist on table)" with hpunch 
    show captain anger-open behind computer
    captain "Right now? But we're so close..."
    
    show captain anger-closed behind computer 

    computer "Captain, I recommend checking on the crew to maintain morale and investigate the cause of the system failure."

    show captain frustrated behind computer 
    captain "..." 
    show captain neutral-open behind computer 
    captain "I suppose you’re right. Give me periodic reports on the oxygen levels."
    show captain neutral-closed behind computer 
    captain "And get me a physical copy of the latest readings on the specimen."

    computer "Aye, aye, Captain. Printing report. Oxygen levels at 99%%."

    show captain frustrated behind computer 
    captain "..." 
    captain "Thanks..."
    show captain neutral-open behind computer 
    captain "Let’s check on the crew."
    show captain thinking behind computer 

    jump map0

    label map0:
        show screen MapUI0 with fade
        pause
        
    label SI:
        hide screen MapUI0 with dissolve
        show captain neutral-open behind computer 
        captain "I should speak to Sara. She’s probably freaking out right now."

        play sound "Footsteps.mp3" volume 0.8
        play music "Microbiology.mp3" volume 0.8
        scene onlayer screens
        $ seenSI = True
        scene bg medic with fade
        show medic nervous with dissolve 
        pause(0.5)
        show captain neutral-closed behind medic with dissolve

        medic "Captain! W-what just happened! Thank goodness you arrived when you did. The alarms went off and I was getting worried!" 
        
        show captain neutral-open behind medic
        captain "Yes, quite unexpected. I‘m checking in personally since comms are down."
        captain "I'm sorting it out with Eugen." 
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
        medic "Could this result in some kind of irreparable, cascading failure?"

        show captain neutral-open behind medic
        captain "Like I said before, Sara, we’ll find out soon. There is no reason to assume the worst." 

        show captain neutral-closed behind medic
        medic "I understand. Just given what has happened before…"

        show captain anger-open behind medic
        captain "What happened to the previous mission has nothing to do with what is happening now."

        # SI.1
        show medic stressed
        show captain anger-closed behind medic
        medic "I’m sorry. I-I guess I’ve always felt you were easier to talk to on this ship. You know, compared to Eugen." 
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
                medic "This is true. Still, I apologize for bringing it up."

            # SI.1.b
            "Don't do it again.":
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
        medic "Yes, yes… I do have working hypotheses, though nothing exactly seems to work out perfectly at the moment. "
        
        show medic nervous
        show captain neutral-closed behind medic
        medic "I should be working harder…"

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
        captain "And that’s exactly why you must continue your work."
        captain "I’m counting on you Sara. Here, I’ve brought you the most recent readings on the specimen."
        captain "We’ll get the system back up one way or another."

        # SI.2
        show medic stressed
        show captain neutral-closed behind medic
        medic "Thank you for the report Captain, but the rest of my research and reference materials are in the system." 
        medic "How long will it take?" 
        medic "How am I supposed to keep working if it takes too long?"
        
        show medic nervous
        show captain neutral-closed behind medic

        menu:
            # SI.2.a
            "Figure it out.":                
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
        
        captain "Try not to move around too much. Oxygen’s at a premium right now."
        captain "I’ll be back to check in later."

        if seenEI is False:
            show screen MapUI0 with fade
            pause

        else:
            jump M1


    label EI:
        hide screen MapUI0 with dissolve
        show captain neutral-open behind computer 
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
        captain "How’re you holding up Eugen?"

        show captain neutral-closed behind engineer
        engineer "As well as one can, given the circumstances." 
        show engineer thinking
        engineer "May we skip the pleasantries? I dislike small talk." 
        show engineer neutral
        engineer "I’m sure Sara would appreciate it more."

        show captain neutral-open behind engineer
        captain "Got it... Straight to the point then. Report."

        show engineer thinking
        show captain neutral-closed behind engineer
        engineer "Captain, the situation is not ideal. There appears to be a system failure on a magnitude I’ve never seen."
        engineer "I am looking into it, however, little progress is being made."
        engineer "At the rate we’re losing oxygen, I estimate that we have approximately one hour."
        
        show engineer neutral
        show captain frustrated behind engineer
        captain "Damn… Well there goes my hope for any good news."

        # EI.1
        show engineer thinking
        show captain neutral-closed behind engineer
        engineer "Is there any information you can provide? Do you know what might have caused this?"

        menu:
            # EI.1a
            "I’m not sure yet.":
                show captain thinking behind engineer
                captain "I’m not sure yet. I want to find out a bit more before I give any concrete answers."

                # show engineer frustrated
                # show captain thinking behind engineer
                show engineer frustration
                show captain thinking behind engineer
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
        
        show engineer thinking
        show captain confusion-closed behind engineer    

        engineer "In the meantime, I’ve reviewed the oxygen depletion curve 3 times now."
        engineer "This is not a random failure. Something is interfering with the system's command execution."

        show captain confusion-open behind engineer   
        captain "What could possibly be interfering? Everything on this mission has been smooth thus far." 
        captain "And why the whole system? A function or two, sure those might glitch and need maintenance." 
        captain "But what the hell happened to MAD1?"

        # EI.2
        show engineer neutral
        show captain confusion-closed behind engineer

        engineer "We must stay focused, Captain. If we’re to correct this, we must proceed methodically."

        menu: 
            # EI.2a
            "Stand by.":
                show captain anger-open behind engineer
                captain "I am proceeding methodically... I need more information first."
                captain "Stand by for now."

                show engineer frustration
                show captain anger-closed behind engineer
                engineer "As you wish, however, I urge you to think about this decision further."
            
            # EI.2b
            "Make haste.":
                $ engApproval += 1
                show captain confusion-open behind engineer
                captain "Make haste but proceed with caution." 
                captain "We don’t fully know yet what’s happening, but I trust you to make progress."

                show engineer thinking
                show captain confusion-closed behind engineer
                engineer "Of course, the sooner we address this, the sooner the root of the problem will present itself."

        captain "Work from your desk the best you can. I don't want us using more oxygen than we need to."
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

        computer "Welcome back, Captain. Oxygen at 80%%."

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
        computer "Water, wả̵̳t̷̨̍e̴͚̔r̵̥̉, every where,"
        computer "And all the boards did shrink;"
        computer "Water, ẉ̸̢̟͑ͅą̷̓͝tĕ̵͈̗̆͒̚r̷̢̼͈͚̈́̐, eve̴̤̚r̷̈́y̴͉̌ ̵̦̈́ẁ̸̺h̵̻̿e̸͉̋ŗ̵̈́e̸̛̝,"
        computer "Nor a̴̞̓ǹ̷̢y̷̾ͅ ̵̡̐d̸̟̄ȓ̶̼o̷̻͒p̴̛̦ ̵̦̈́t̵̨͝ó̴̝ ̸̜͋d̸̝̑rī̶̻n̵̺̍ḱ̴͍."
        
        show captain confusion-open behind computer with hpunch 
        captain "More poems? MAD1 I can’t lose you right now!"

        scene bg computer
        show computer reboot-1
        show captain confusion-closed behind computer
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
        computer "System functionality at 69%%." 
        show computer neutral-2
        computer "Apologies, Captain. It seems my software is continuing to deteriorate." 
        computer "Something is interfering with the ship systems and my code. I am unable to identify wha̸͇̋t̶̜̕" 
        computer "Captain, I’m afraid my ability to assist you will be limited soon."

        show captain anger-open behind computer with hpunch
        play sound "Metallic_Hit.mp3" volume 0.8
        captain "Dammit! I can’t afford to have more things break down now."
        captain "What am I supposed to do?"

        show computer neutral-3
        show captain anger-closed behind computer
        computer "I suggest checking with the crew, Captain. 
            Perhaps they will have answers soon with your ss-ssupp̷̞̏-pǫ̸̊ȑ̸̨t̷͎̎t̷͎̎-t̷̠̆t̵̞̓t̴̘͑-"

        show computer error-1 with hpunch
        play sound "Metallic_Hit.mp3" volume 0.8
        show captain anger-closed behind computer with hpunch 

        computer "The one by toi̷l̵, the other to comp̸̖̓l̴͎̀a̴̺͗ì̴̩n"
        computer "How far I t̴̡̃o̴̳͒i̶̥͋l̶̮̍, still farther ó̷̖ff f̵̲͒ȑ̷͉o̵̮̓m̴̮̌ ̶͓̈́t̷͎̑h̶̏e̶e̶̻̔."

        show computer error-2
        show captain concern-open behind computer
        captain "... How far I toil, indeed."
        captain "I hope one of them has found something."
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

        medic "Captain! Any update on what’s going on? What did Eugen say?"

        # S.1.1
        show captain neutral-open behind medic
        captain "We are looking into it."

        menu: 
            # S.1.1a
            "To be honest, the situation is dire.":
                show captain concern-open behind medic
                captain "I have to be honest with you, Sara." 
                captain "The situation is more dire than we thought. But I need you to remain calm."
                medic "Oh my god… T-thank you for your honesty, Captain."

            # S.1.1b
            "We'll sort it out soon.":
                $ medApproval += 1
                show captain neutral-open behind medic
                captain "I have hopes that we will sort it out soon." 
                captain "Thanks for fulfilling my request."
                medic "Okay, that’s good to hear! Yes, of course."

        show medic thinking
        show captain neutral-closed behind medic
        medic "Um, I’ve gone through my notes as requested, w-would you like to hear what my theory is?"

        show captain neutral-open behind medic
        captain "Enlighten me."

        show medic explaining
        show captain neutral-closed behind medic
        medic "This specimen is not a lifeform as we know it. Life is, after all, undefined."
        medic "It’s uniquely adapted to the cold and dark of Europa’s ocean. "
        show medic excited
        show captain neutral-closed behind medic
        medic "I’ve been thinking of life in Earth’s oceans, and the closest equivalent is a marine fungus."
        show medic neutral
        show captain neutral-closed behind medic
        medic "However, the Earth's marine fungi are largely microscopic."
        
        show captain thinking behind medic
        captain "It’s got to be incredibly resilient to survive those conditions…"

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
        captain "And you? Are you holding up okay?"

        # S.1.2
        show medic nostalgic
        show captain neutral-closed behind medic
        medic "I just… I wonder if I’d get to see my family again."

        menu: 
            # S.1.2a
            "This mission wasn't meant to be easy.":
                show captain anger-open behind medic
                captain "That risk is always there. Part of the job." 
                captain "This mission was never meant to be easy."

                show medic nervous
                show captain anger-closed behind medic
                medic "Yes, yes, I know…"

            # S.1.2b
            "I will do my best to get us home.":
                $ medApproval += 1
                show captain concern-open behind medic
                captain "I will do my best to make sure that this mission is successful and everyone gets home."

                show medic excited
                show captain concern-closed behind medic
                medic "Thank you…I know you will."
                
                show medic nervous     
                show captain concern-closed behind medic                   
   
        medic "Anyway, now that we have this specimen, I absolutely must make it back home… I have to return to my family…" 

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
        medic "All the choices I’ve made and the work I’ve done… I’d be lying if I said that I hadn’t doubted it all."
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
        medic "Doesn’t MAD1 usually deal with these kinds of issues? After all, she’s the reason we’re such a small team."
  
        show captain concern-open behind medic      
        captain "Actually… MAD1 is malfunctioning."

        show medic stressed
        show captain concern-closed behind medic
        medic "Oh my god… It’s worse than I thought…"

        show captain concern-open behind medic  
        captain "Something is interfering with MAD1’s processes. But we must keep focused."
        captain "I will let you know once we have something concrete."

        show captain concern-closed behind medic
        medic "It’s just… two new crazy developments on this ship in such a short time!"

        show medic thinking
        show captain concern-closed behind medic
        medic "This amazing specimen and now this crisis… such a strange coincidence. I have a feeling we’re missing something."

        show captain thinking behind medic
        captain "I don’t generally trust coincidences. Not at a time like this."

        # S.1.3
        medic "I-is there anything else I can do to help?"

        menu: 
            # S.1.3a
            "Stay put while we sort this out.":
                $ medApproval -= 1
                show captain concern-open behind medic
                captain "Just stay put while we sort this out." 

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
        play sound "Footsteps.mp3" volume 0.8
        play music "Spark_Of_Awareness.mp3" volume 0.8
        scene onlayer screens
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
        engineer "I have been navigating through MAD1’s system to find the interference."
        engineer "The core system architecture is… not a standard framework."

        show captain neutral-open behind engineer
        captain "How do you mean?"

        show engineer thinking
        show captain neutral-closed behind engineer
        engineer "It’s layered. Recursive even. "
        engineer "It appears to be self-protective."

        show captain confusion-open behind engineer
        captain "Can’t you normally manually bypass these things through administrative controls?"
        engineer "Matthew built this differently"
        captain "Isn’t there something in the programming language that you could find or use?"
        engineer "This ship’s operating system has programming that is beyond the industry standard."

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
            "What are you implying?":
                show captain anger-open behind engineer 
                captain "Are you implying I’m hiding things from you? Sabotaging the mission?"
                
                show engineer stressed
                show captain anger-closed behind engineer 
                engineer "My only concern is accomplishing this mission with minimal complexities." 

        show engineer neutral
        engineer "Every time I attempt to reroute life support through the auxiliary control, the command is intercepted."

        show captain concern-open behind engineer
        captain "Intercepted? By what?"
        
        show engineer thinking
        show captain concern-closed behind engineer
        engineer "There is a line of defence that, according to standard protocol, should not exist."
        engineer "I am aware that MAD1 was especially designed by Matthew to support a small crew."
        engineer "But when I reviewed the ship's schematics, I noticed a layer of defence that is handwritten."
        engineer "Written in a way where the logic only makes sense to specific personnel."

        show captain thinking behind engineer 
        captain "… I see."

        engineer "There is a lack of documentation, no engineering notes; it is the equivalent to a ghost layer in the system."

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
                show captain anger-open behind engineer
                captain "Listen, I’m not a programmer." 
                captain "He wouldn’t have shared anything like that with me."
                engineer "As a Captain, I would have expected you to have more knowledge of your vessel's intricacies."

            # EI.2b
            "He really liked poetry.":
                $ engApproval += 1

                show captain thinking behind engineer
                captain "Matthew was a fan of poetry." 
                captain "MAD1 recited another verse after I visited you last. There could be something in that."
                engineer "That is very strange, but at least it is something."

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
        engineer "However, the only person who truly understood the depth of MAD1’s architecture… was him."

        captain "…"

        engineer "I am determined to not let this system get the better of me. As unorthodox as it is, I know I can salvage the situation."
        engineer "Unfortunately, I do not know how to safely override it without risking total collapse."

        # E1.3

        show engineer thinking
        show captain neutral-closed behind engineer
        engineer "Tell me something, Captain…"
        engineer "If Matthew were standing here instead of me… do you believe he would know what to do? "
        menu:
            # E1.3a
            "That doesn’t matter right now.":
                show captain anger-open behind engineer
                captain "That does not matter right now. Why would you ask me that?!"
                captain "Just… figure something out."
                
                show captain anger-closed behind engineer
                engineer "Not knowing if the designer himself could be able to solve this crisis is not a reassuring belief."

            # EI.3b
            "Yes.":
                $ engApproval += 1

                show captain neutral-open behind engineer
                captain "Yes. He would." 
                captain "But as far as I can tell he’s not here anymore." 
                captain "So get it together and figure it out." 
                show captain neutral-closed behind engineer
                captain "That’s an order."
                engineer "That must mean there is a plausible solution. I will begin investigating."

        show engineer neutral
        show captain neutral-closed behind engineer
        engineer "The mission has been going smoothly up until now."
        engineer "My equipment, my design, we have seen it in action. There were no shortcomings; this is how all things should be."
        engineer "If this mission fails, just know it wasn’t from my contribution."

        jump M2

    label M2:
        play sound "Footsteps.mp3" volume 0.8
        play music "Electric_Dawn.mp3" volume 0.8
        scene bg computer with fade
        show computer neutral-1 with dissolve
        show captain frustrated behind computer with dissolve

        captain "..."

        computer "Greetings, my̸̛̝̎ love̵̦͆͑̚ͅě̸̦͝͝e̸̘͋, Captain."

        show captain concern-open behind computer
        captain "What? MAD1 what the hell?"

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
        computer "Rebootinggg.{w=0.3}{nw}"
        show computer reboot-4
        computer "Rebootinggg.{w=0.3}{nw}"
        show computer reboot-5
        computer "Rebootinggg." 
        show computer neutral-1
        show captain anger-closed behind computer
        computer "System functionality at 24%%."
        computer "Oxygen at 50%%. Captain, it may be time to plan for the worst case scenario."
        show computer neutral-2
        show captain anger-closed behind computer
        computer "You may want to consider who it would be best to give clearance for the remaining escape pod."
        computer "The escape pod has capacity for only one person."

        show captain confusion-open behind computer
        captain "... What?"

        show computer neutral-3
        show captain confusion-closed behind computer
        computer "The escape pod has capacity for-"

        show captain anger-open behind computer with hpunch
        captain "NO I HEARD YOU THE FIRST TIME!"

        show captain frustrated behind computer
        captain "(Laboured breathing)"

        show computer neutral-1
        computer "Apologies, Captain. But you mustttt-"

        show computer error-1 with hpunch
        show captain
        computer "Ah! Well- a-day! what é̶̝v̵̬͋i̸͇͌l̷ looks"
        computer "Had ẗ̵̯́hė̷̠e from o̴l̶d̶ ã̷̡n̷͎͛d̶̥̾ ̶̝̀y̷̫̓o̶͓̍ǔ̴͎n̵̞̾g̴̟͂!"
        computer "Instead of the c̵̭̆r̷̫̃ó̶̩s̴͇̓ș̸̍, the A̷lb̴ã̵͓tŕ̵̫ó̴̞ss"
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

        captain "No. No…"
        play sound "Metallic_Hit.mp3" volume 0.5
        show bg escape pod with hpunch
        
        captain "How the hell am I meant to choose one life over another?! How am I supposed to decipher all of this… poetry?"

        if seenS1 is True:
            captain "Aghh! Someone has to go home with the specimen."
            captain "Potential alien life is too important not to study."
            captain "Matthew died for this!"

        elif seenE1 is True:
            captain "... Eugen’s right. Matthew would know what to do."
            captain "If it wasn’t for that damn asteroid we wouldn’t even be here right now."

        captain "We can’t—I can’t fail now. Not when we’re so damn close."
        captain "God if I had him here with me this would—"
        captain "Matthew… What do I do..?"
        
        captain "I… I could just leave right now… Be done with it…"
        menu:
            "Escape":
                menu: 
                    "Are you sure, captain?"

                    "Yes":
                        jump EndB

                    "No":
                        captain "No, I can't leave."
                        captain "…"
                        play sound "Metallic_Hit.mp3" volume 0.5
                        show bg escape pod with hpunch
                        captain "(slams fist on escape pod)"
                        captain "(sharp inhale) Get it together Rudy. Your crew needs you to focus up and get us out of here."
                        captain "We’ll all make it home. We need to make it home."

                        jump Map2
            
            "No, I can't leave.":
                captain "No, I can't leave."
                captain "…"
                
                show bg escape pod with hpunch
                play sound "Metallic_Hit.mp3" volume 0.5
                captain "(slams fist on escape pod)"
                captain "(sharp inhale) Get it together Rudy. Your crew needs you to focus up and get us out of here."
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
        show medic worried with dissolve
        pause(0.5)
        show captain neutral-closed behind medic with dissolve

        if seenS1 is True:
            # S2.A
            medic "Captain! Any update?"

            show captain neutral-open behind medic
            captain "Still working on it."

            show captain neutral-closed behind medic
            medic "How much time do we really have? To solve this problem? T-the ship cannot possibly hold up this way for long?"

            menu:
                # S.2.1a
                "It’s not looking good.":
                    show captain concern-open behind medic
                    captain "It’s not looking good at all, Sara. We might have to make difficult decisions… I want you to know that."   

                    show medic anxious
                    show captain concern-closed behind medic
                    medic "I-I see…"

                # S.2.1b
                "There is always hope.":
                    $ medApproval += 1
                    show captain neutral-open behind medic
                    captain "Things aren’t looking great at the moment. But there is always hope." 
                    captain "We are all working hard to fix this. Let’s continue to do so."

                    show medic neutral
                    show captain neutral-closed behind medic
                    medic "Yes, yes, of course!"

            show captain neutral-open behind medic    
            captain "Sara, what have you found out about the specimen?"

            show medic explaining
            show captain neutral-closed behind medic    
            medic "I-I have a theory. It’s exciting and concerning."
            
            menu: 
                # S.2.2a
                "Anything is better than nothing.":
                    $ medApproval += 1
                    show captain concern-open behind medic
                    captain "Anything is better than nothing. I trust your judgment."

                    show medic neutral
                    show captain concern-closed behind medic
                    medic "Thank you, Captain!"

                # S.2.2b
                "We need a little more than a theory.":
                    show captain neutral-open behind medic
                    captain "I was expecting a little more than a theory, to be honest…"
                    
                    show medic nervous
                    show captain neutral-closed behind medic
                    medic "I-I’m sorry, but I’ve put quite a bit of thought into it."
            
            show captain neutral-open behind medic
            captain "Tell me your theory."

            show medic explaining
            show captain neutral-closed behind medic
            medic "I know I said this organism has similarities to a marine fungus, but it appears to be more complex."

            show captain neutral-open behind medic
            captain "How do you mean?"

            show medic excited
            show captain neutral-closed behind medic
            medic "You know how there are mycelium networks that enable transfer of nutrients in forest ecosystems?"
            medic "My theory is that this organism may have a symbiosis with others in its ecosystem."
            medic "This could be more developed than what we see on Earth, depending on hundreds of millions of years of evolution."
            
            show captain neutral-open behind medic
            captain "Go on."

            show medic suggesting
            show captain neutral-closed behind medic
            medic "This organism might have communication capabilities that we are unfamiliar with."
            medic "I am not saying that this could be sentient, but Earth classifications can blur when we’re dealing with extraterrestrial life."

            show captain confusion-open behind medic
            captain "A fungus on steroids? You were hoping for single-celled life in that ocean…"
            captain "What kind of communication capabilities are we talking about here?"

            show medic thinking
            show captain confusion-closed behind medic
            medic "I mentioned this before–has it occurred to you that two incredible events have taken place in a short time span?"
            show medic excited
            medic "Us finding this specimen and now this crisis we’re facing!" 
            show medic nostalgic
            medic "Hah, my family would associate something supernatural to this kind of coincidence…" 

            show captain concern-open behind medic
            captain "Sara, are you implying that this organism could have something to do with this?"

            show medic excited
            show captain concern-closed behind medic
            medic "Yes! That’s what I think we’ve been missing! This organism is probably emitting electromagnetic waves that are interfering with the computer!"

            menu: 
                # S.2.3a
                "That does sounds far-fetched.":
                    show captain concern-open behind medic
                    captain "That does sound far-fetched. However, we must think of all possibilities."

                    show medic nervous
                    show captain concern-closed behind medic
                    medic "Yes, indeed…" 

                # S.2.3b
                "There could be something there…":
                    $ medApproval += 1
                    show captain neutral-open behind medic
                    captain "There could be something there… It could be the key to our survival. Find out all you can."

                    show medic neutral
                    show captain neutral-closed behind medic
                    medic "Yes, will do, Captain!"

            show captain thinking behind medic
            captain "What do you think is the next step?"

            show medic suggesting
            medic "If my theory is right, then we need to think of containment."

            show captain neutral-open behind medic
            captain "Work on it."
            
            show medic neutral
            show captain neutral-closed behind medic
            medic "Yes, Captain!"
            jump M3

        elif seenS1 is False:
            # S2.B
            medic "Captain! Oh my god. What is happening!"

            menu: 
                # S.2.1a
                "Sorry for not getting to you sooner.":
                    $ medApproval += 1
                    show captain concern-open behind medic
                    captain "I’m sorry I couldn’t come talk to you sooner. I’ve been speaking with Eugen about this problem."

                    show medic neutral
                    show captain concern-closed behind medic
                    medic "Oh, it’s okay. Good to hear you’re on top of it!"

                # S.2.1b
                "Everything’s fine.":
                    show captain neutral-open behind medic
                    captain "Everything’s fine. We’re sorting it out."

                    show medic nervous
                    show captain neutral-closed behind medic
                    medic "Okay then…"
            
            show medic stressed
            medic "What does Eugen say? Is he okay?!"

            show captain neutral-open behind medic
            captain "Yes, he’s fine. He cannot offer anything concrete at the moment." 
            captain "But I must tell you that MAD1 is malfunctioning. This complicates everything."

            show medic thinking
            show captain neutral-closed behind medic
            medic "Oh my god… Here I was thinking we would very much make it back home with the specimen. And my family…"

            show captain concern-open behind medic
            captain "And we can! We still have hope." 
            captain "I know you’re missing your family very much. We will get through this."

            show medic nervous
            show captain concern-closed behind medic
            medic "It’s not just about that. It’s just… this is my one chance to prove that everything I’ve done– that it’s all worth it, you know?"

            show captain concern-open behind medic
            captain "Your previous achievements are more than average to say the least. Is that not enough?"
            captain "Your family should be proud of you regardless of the outcome of this mission."

            show medic neutral
            show captain concern-closed behind medic
            medic "I’m a lone woman who’s devoted my life to the sciences. Not everyone views that as ideal, to say the least."

            show captain concern-open behind medic
            captain "That’s not very fair."

            show captain concern-closed behind medic
            medic "It's not, but taking this home would change my life in more ways than one… And now, I don’t know. We might not make it back."

            show captain neutral-open behind medic
            captain "Focus Sara. Have you managed to come up with any theories about the specimen?"

            show medic stressed
            show captain neutral-closed behind medic
            medic "What? I-no, my research is in the computer! I’ve been reviewing my journal a-and the report you gave me but I’m losing my mind in here."

            menu: 
                # S.2.2a
                "You know the drill.":
                    show captain concern-open behind medic
                    captain "You know the drill. Keep at it." 
                    captain "Go through your notes and see what you can come up with."
                    captain "I’m sure you’ll find something."

                    show medic worried
                    show captain concern-closed behind medic
                    medic "I-I’m sorry…"

                # S.2.2b
                "We’re counting on you.":
                    $ medApproval += 1
                    show captain neutral-open behind medic
                    captain "Hey, we’re all losing our minds. It’s okay."
                    captain "Please go through your notes and see what you can come up with." 
                    captain "We’re counting on you."
                    
                    show medic neutral
                    show captain neutral-closed behind medic
                    medic "Yes, yes, of course. T-thank you for believing in me, Captain."

            show captain determined-open behind medic
            captain "We’ve come this far. We cannot let everything go to waste."

            show medic nervous
            show captain determined-closed behind medic
            medic "I know… I know it more than anyone. This mission is everything to me."

            show captain concern-open behind medic
            captain "It is to all three of us…"

            show medic neutral
            show captain concern-closed behind medic
            medic "… I’ll do what I can… Would you like to hear what I’ve come up with so far?"
            medic "Although it’s all based on the limited notes I have here."

            show captain neutral-open behind medic
            captain "Anything would be useful at this point."

            show medic suggesting
            show captain neutral-closed behind medic
            medic "Captain, this organism is very much extraterrestrial, but if we are to compare it to an Earth organism, it bears some resemblance to a marine fungus." 
            medic "However…"

            show captain neutral-open behind medic
            captain "Yes?"

            show medic explaining
            show captain neutral-closed behind medic
            medic "It appears to be more complex. You know how there are mycelium networks that enable transfer of nutrients in forest ecosystems?"
            medic "My theory is that this organism may have a symbiosis with others in its ecosystem."
            medic "This could be more developed than what we see on Earth, depending on hundreds of millions of years of evolution."

            show captain neutral-open behind medic
            captain "Go on."

            show medic excited
            show captain neutral-closed behind medic
            medic "This organism might have communication capabilities that we are unfamiliar with."
            medic "I am not saying that it is sentient, but Earth classifications can blur when we’re dealing with extraterrestrial life."
            
            show captain confusion-open behind medic
            captain "A fungus on steroids? You were hoping for single-celled life in that ocean…"
            captain "What kind of communication capabilities are we talking about here?"

            show medic thinking
            show captain confusion-closed behind medic
            medic "I’m not sure, Captain… But has it occurred to you that two strange events have taken place in such a short period of time?"
            show medic nostalgic
            medic "Hah, my family would associate something supernatural to this kind of coincidence…"

            show captain concern-open behind medic
            captain "Sara, are you implying that this organism could have something to do with this?"

            show medic excited
            show captain concern-closed behind medic
            medic "All I’m saying is anything is possible! But think about it! This may be the link we’re missing!"

            menu: 
                # S.2.3a
                "That does sound far-fetched.":
                    show captain concern-open behind medic
                    captain "That does sound far-fetched. But investigate any and all possibilities."

                    show medic nervous
                    show captain concern-closed behind medic
                    medic "Yes, of course."

                # S.2.3b
                "There could be something there…":
                    $ medApproval += 1
                    show captain neutral-open behind medic
                    captain "There could be something there… It could be the key to our survival."
                    captain "Find out all you can."

                    show medic neutral
                    show captain neutral-closed behind medic
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

            captain "Eugen."

            show captain neutral-closed behind engineer
            engineer "Good, I was about to come find you myself. The situation has reached far too unstable a state."
            show engineer shock
            engineer "The defense layer I mentioned earlier, it has evolved."

            show captain confusion-open behind engineer
            captain "I- evolved..?"

            show engineer frustration
            show captain  confusion-closed behind engineer
            engineer "Before, it was only intercepting my commands; now it seems to be anticipating them."
            engineer "I have never seen this level of adaptation in a system, in a recursive structure."
            engineer "I attempted the auxiliary reroute with more advanced methods; however, it locked me out of two additional subsystems in response."
            
            show captain confusion-open behind engineer
            captain "Eugen, you’re saying a lot of words and I’m following none of them."
            
            show engineer neutral
            show captain confusion-closed behind engineer
            engineer "Imagine trying to play a trick on someone reading your mind."
            
            show captain neutral-open behind engineer
            captain "So following that metaphor, it’s as though it’s seeing you trying to read it, so it’s trying to give you fake thoughts?"

            show engineer frustration
            show captain neutral-closed behind engineer
            engineer "Somewhat, yes."
            engineer "I know I’ve asked you about Matthew’s work before; however, as of right now, there is no other outlet of information I could hope for."
            show engineer shock
            engineer "Did he ever share any hypothetical situations about failing a mission and how he would respond, maybe about what the ship should protect first?"
            engineer "Anything, Captain, anything."

            menu: 
                # E.2.1a
                "He didn’t plan on failing.":
                    $ engApproval += 1
                    show captain concern-open behind engineer
                    captain "He didn’t plan on failing. I’m sure you can understand that."
                    captain "Even so, a failsafe wouldn’t be obvious or easy to access."

                    show engineer thinking
                    show captain concern-closed behind engineer
                    engineer "I admire his confidence; however, planning for failure is almost as important as expecting to succeed."

                # E.2.1b
                "Your guess is as good as mine.":
                    show captain neutral-open behind engineer
                    captain "Your guess is as good as mine."

                    show engineer anger
                    show captain neutral-closed behind engineer
                    engineer "I would like to believe that isn’t true, considering your role for this mission."
            
            show engineer thinking
            engineer "I noticed poetry being produced by the computer at times."

            show captain neutral-open behind engineer
            captain "Yes, MAD1 has been reciting it since the initial crash."

            show engineer neutral
            show captain neutral-closed behind engineer
            engineer "Seeing as this is not even standard for a system error, I investigated it."

            show captain neutral-open behind engineer
            captain "And?"

            show engineer shock
            show captain neutral-closed behind engineer
            engineer "It seems they are not decorative artifacts, fortunately."
            engineer "They are actually embedded in conditional branches with certain verses correlating with security escalations."
            
            show captain confusion-open behind engineer
            captain "So there is something in the poetry after all?"
            show captain frustrated behind engineer
            captain "... Unfortunately… My grasp of poetry isn’t as strong as his…"

            show engineer frustration
            engineer "I have to say, if I had known this was what was to be expected working with this ship, I would not have agreed to participate in this mission."
            
            show captain anger-open behind engineer
            captain "It was either this or risking another massive crew like the last mission."
            captain "MAD1 may be… experimental… but she passed all the necessary tests."
            captain "None, and I mean none of us expected any of this."
            
            show engineer thinking
            show captain anger-closed behind engineer
            engineer "Anyhow, this is not necessarily corruption; rather, it seems to be symbolic indexing."
            engineer "Assuming this is how the ship is programmed, it is safe to assume Matthew preferred to do things his own way."

            show captain neutral-open behind engineer
            captain "Told you."

            show engineer resolve
            show captain neutral-closed behind engineer
            engineer "I need to ask you, was this really just an aesthetic deviation, or did he believe conventional protocol was fundamentally flawed?"
            engineer "If the system is operating on his philosophy rather than industry standards, then I am troubleshooting a worldview, not a machine."

            menu: 
                # E.2.2a
                "This OS was his baby.":
                    $ engApproval += 1
                    show captain concern-open behind engineer
                    captain "This operating system was his baby, his pride and joy."
                    captain "It was made perfectly - in his eyes, to his touch."

                    show engineer thinking
                    show captain concern-closed behind engineer
                    engineer "So that means this could be beyond our understanding, and potentially, some ulterior methods must be considered."

                # E.2.2b
                "He was my husband, not my clone.":
                    show captain anger-open behind engineer
                    captain "Matthew Pratchett was my husband, not my clone."
                    captain "I don’t know every possible thought that was going through his head, Braun."

                    show engineer anger
                    show captain anger-closed behind engineer
                    engineer "Choosing to use his vessel for this mission was a decision you made; at the very least, I’d hope you knew enough about it to offer some insight."

            show captain neutral-open behind engineer
            captain "I don’t think he intended for it to be captained by anyone other than him."
            captain "But no one else has programmed a system quite like his that’s necessary for a mission like this."
            
            show engineer neutral
            show captain neutral-closed behind engineer
            engineer "There is something else you need to understand."

            show captain neutral-open behind engineer
            captain "Enlighten me."

            show engineer shock
            show captain neutral-closed behind engineer
            engineer "While I have been trying to stabilize our life support, the background processes have been reallocating power autonomously."  
            
            show captain confusion-open behind engineer
            captain "Reallocated where?"
            
            show engineer thinking
            show captain confusion-open behind engineer
            engineer "Containment integrity is being reinforced, data preservation protocols are preserved, and the specimen’s environmental chamber has not dropped past optimal range even once."
            engineer "All while our life support has been steadily dropping. This doesn’t appear to be a malfunction; this seems to be prioritization."
            show engineer frustration
            engineer "Let me ask you this very clearly, Captain, when Matthew designed this system, did he ever imply that the discovery outweighed the lives involved in its recovery?" 
            engineer "If he did, then rest assured the ship is behaving exactly as it was programmed to."

            menu: 
                # E.2.3a
                "Stop asking about him.":
                    show captain anger-open behind engineer
                    captain "Stop. Asking. About him."
                    captain "He’s not- … He wasn’t an idiot."
                    captain "He wouldn’t have prioritised the mission over the crew’s survival, not even his own."

                # E.2.2b
                "He was pragmatic.":
                    $ engApproval += 1
                    show captain concern-open behind engineer
                    captain "Matthew was certainly a creative idealist, but he was also very pragmatic."
                    captain "He wouldn’t have prioritised the mission over the crew’s survival, not even his own."
            
            captain "Which means the ship is not supposed to act this way, something’s interfering."
            captain "I’ll go see if MAD1 is still acting up or if I can glean anything from her."
            
            show engineer resolve
            show captain neutral-closed behind engineer
            engineer "It is worth noting that there is a way of overriding MAD1 completely; however, this will completely shut the system down, and you will have to take full control of the ship."
            engineer "I discovered this failsafe while digging through the ship's schematics further."
            engineer "I would consider this a last resort option, one that defies protocol entirely."

            show captain neutral-open behind captain
            captain "That’s a good lead. Follow it."
            jump M3

        elif seenE1 is False:
            # E2.B
            scene bg engineer with fade
            show engineer neutral with dissolve
            pause(0.5)
            show captain neutral-closed behind engineer with dissolve

            engineer "Captain… you finally decide to pay a visit."

            show captain neutral-open behind engineer
            captain "Yes, I was speaking to Sara."
            captain "Report."

            show engineer resolve
            show captain neutral-closed behind engineer 
            engineer "I hope she was able to offer some valuable insight on the specimen."
            engineer "I have been isolating the corrupted pathways since this whole mess started."
            engineer "At 20%% deviation, it was manageable, nothing I haven’t dealt with before."
            engineer "At 35, it became anomalous."
            engineer "At 45, it became clear that what was happening was intentionally programmed into the ship."
            engineer "I needed more information half an hour ago, so I can only hope you come to me with an update about the ship."

            show engineer frustration
            engineer "Were you gathering information, or were you hoping this would resolve itself without much involvement from you?"

            menu: 
                # E.2.1a
                "I don’t have much…":
                    show captain concern-open behind engineer
                    captain "I don’t have much, but MAD1 is still reciting poetry. And incorrectly at that."
                    captain "She keeps replacing words or misplacing lines."
                    captain "I’m sorry I don’t have anything concrete."

                    show captain concern-closed behind engineer
                    engineer "Hmm… Disappointing."

                # E.2.1b
                "For your information…":
                    $ engApproval += 1
                    show captain anger-open behind engineer
                    captain "For your information, Technician Braun, I have been conferring with MAD1 and Sara to find a solution."
                    captain "Sara is investigating the specimen to see if it’s affecting anything."
                    captain "And MAD1 is still reciting different poems."
                    captain "And they’re not even correct! Sometimes the words are changed or lines are misplaced."
                    captain "I hope you can forgive the lack of specificity when all I’m getting are damn riddles."

                    show engineer neutral
                    show captain neutral-closed behind engineer
                    engineer "Apologies Captain…"
            
            show engineer thinking
            engineer "By my calculations, there is only 50%% of our oxygen supply remaining."

            show captain frustrated behind engineer
            captain "Oh I am well aware…"

            show engineer frustration
            engineer "Only now do you decide to meet with the Engineer you have on board."
    
            captain "I apologise for not being able to juggle with one hand tied behind my back."

            show engineer anger
            engineer "... I have been trying to access the auxiliary core for the past half hour without any structural access provided to me."
            engineer "Every override attempt is intercepted, every reroute collapses… The system doesn’t seem to be failing, rather the opposite - it’s seemingly defending itself."

            show engineer shock
            show captain neutral-closed behind engineer
            engineer "The only reason I believe makes sense is that Matthew designed it this way on purpose."
            engineer "Is there anything you know about Matthew’s work? Anything he trusted you with that could help me?"
            engineer "If so, now is the time to share."

            menu: 
                # E.2.2a
                "He was a fan of poetry.":
                    $ engApproval += 1
                    show captain concern-open behind engineer
                    captain "Matt… was a fan of poetry. Given MAD1’s clearly also become a big fan, there’s definitely something in there."

                    show engineer neutral
                    show captain concern-closed behind engineer
                    engineer "I appreciate your transparency. I’ll begin investigating possible patterns in the system."

                # E.2.2b
                "He was the programmer, not me.":
                    show captain neutral-open behind engineer
                    captain "If he had any programming secrets, he didn’t share them with me. I’m not exactly a programmer."

                    show engineer frustration
                    show captain neutral-closed behind engineer
                    engineer "I’d imagine, as the Captain and someone who knew Matthew closely, you’d have more to share. We’ll have to make-do I suppose."

            show engineer anger
            engineer "I seldom thought a task could not be resolved through following protocol; however, it seems now my beliefs have been debunked."
            engineer "While the auxiliary core is still responsive to a certain extent, there is not enough to be optimistic about."
            engineer "Matthew embedded what seems to be decision filters that only respond to specific authority signatures."
            engineer "Another example of not adhering to standard protocol."

            show captain rememberance-open behind engineer
            captain "He absolutely liked things his own way, that’s for sure."

            show engineer shock
            show captain rememberance-closed behind engineer
            engineer "Given this, I want to ask you, Captain, in this chain of command we have, have we been operating on procedure, or his preference?"

            menu: 
                # E.2.3a
                "To hell with your procedures.":
                    $ engApproval += 1
                    show captain anger-open behind engineer
                    captain "To hell with your procedures and to hell with my dead husband’s preferences."
                    captain "We’ve been dealt a shitty hand and we’re trying not to die."
                    captain "So stop looking at it like a formula and start looking at it like a puzzle and crack it."
                    captain "That’s an order, Braun."

                    show engineer thinking
                    show captain neutral-closed behind engineer
                    engineer "Although unconventional, you may be right. This mess should be viewed as a puzzle of some sort."
                    engineer "Hmm…"

                # E.2.3b
                "I’m just as confused as you are.":
                    show captain frustrated behind engineer
                    captain "Listen, I’m just as lost and confused as you are."
                    show captain neutral-open behind engineer
                    captain "But if we want to figure this out, we have to do the best we can with the cards we are dealt."
                    captain "I’ll return shortly."

                    show engineer frustration
                    show captain neutral-closed behind engineer
                    engineer "I’ve never been a gambling man, Captain. At this rate, I don’t suggest you return with high hopes."
            
            show engineer resolve
            engineer "So long as my equipment is being used for this mission, I am determined to make it back in one piece."
            engineer "We have seen it in action. My design is flawless and deserves recognition."
            engineer "For the sake of my life’s work, this mission cannot fail."
            engineer "I’ll investigate the unconventional options we have, considering the mess we are dealing with."

            show captain neutral-open behind engineer
            captain "Good, I’ll speak with you shortly."
            show captain neutral-closed behind engineer
            jump M3

    # label M1O:
    #     play sound "Footsteps.mp3" volume 0.8
    #     play music "Electric_Dawn.mp3" volume 0.8
    #     # M.1.O optional MAD1
    #     scene onlayer screens
    #     $ seenMO = True
    #     scene bg computer with fade

    #     show computer neutral-1 with dissolve
    #     show captain neutral-open behind computer with dissolve

    #     computer "hehehe captain"
    #     captain ":("

    #     jump M3

    label M3:
        play sound "Footsteps.mp3" volume 0.8
        play music "Electric_Dawn.mp3" volume 0.8
        scene onlayer screens
        scene bg computer error with fade

        show computer error-1 with dissolve
        show captain neutral-closed behind computer with dissolve

        computer "Cap̴-̶ ̵C̴͂͜ä̴͎́p̸̪͒-̵̺̀ ̷͇͐ Ċ̷̯a̶̭͊p̴̹̆t̶̡̐a̸̬̓ï̴̬n."

        show captain concern-open behind computer 
        captain "… MAD1?"

        show captain concern-closed behind computer 
        computer "We meet in an e̷̯͂̉v̸̜͘ị̶̃l̵͕̆̾ land"
        computer "That is near to the gates of h̵̫̃ẹ̶͑l̶͚̿l̵͍̀."
        computer "And I guard thy g̷̺̏ā̸͜t̴̬͝ē̴̼ŝ̷͓ ̴̹̎i̷͒͜n̸̼̿ ̷̜̂f̵̰͝ē̵̟a̵͕̾r̷̯̃ "
        computer "Of wȯ̵̰r̸̥̃d̴s thou cansť̷͔ n̵͉͐o̵̖͌t̸͈̀ ̵͔̎h̸͈͋ȩ̷̽a̸̙̚r̸̩̆,"
        computer "Oh L̶o̸͈͌ve̸̤̽, the flower̴s̶͊s̵̠̀ô̸̼ r̸͖̂ȅ̶͉d̵͕̀ "
        computer "Are only tongues of flame,"
        computer "The eå̸͕rth̷͇̒ is full of the d̸é̵͚a̵d̸͎̀, "
        computer "There is daǹ̶̳ger̷͉͌ beṅ̴eȁ̵͚th̷͖͆ ă̴ń̷̩d o'erh̴̗̔e̷͖͐ả̷̭d̶̢́."

        show captain confusion-open behind computer 
        captain "What? What other danger?"
        captain "What are you trying to tell me?"

        show captain confusion-closed behind computer 
        computer "There pă̸s̴͎̀sed̷͚̃ a weary time. Each t̵h̴r̶o̷a̷t̶ "
        computer "Was parched, and glazed each eye."
        computer "A ẃ̸̳e̴ary̷̙͑ time! a ẃ̸̳eary time!"
        computer "How glazed each ẃ̸̳e̴ary̷̙͑ eye,"
        computer "And may there be no s̸a̷d̶n̷e̴s̸s̴ ̴o̶f̵ ̸f̵a̶r̷e̵w̶e̴l̵l̷ "

        show captain confusion-open behind computer 
        captain "Farewell..?"
        show captain distress behind computer 
        captain "No…"
        captain "Why…"

        computer "Let the bell toll! — A sai̵n̶t̵̩̀ly̵ s̴ŏ̴̹ú̴̼l"
        computer "Glides down the Sty̷g̴ian̷̩̊  ri̴v/er!"
        computer "And let the burial rite be read —"
        computer "The f̵ủ̵͇n̷̩̒e̸̗͑ř̵͍á̴̪l song be sung —"
        computer "A d̵ȉ̴̦ŕ̵͙g̵̛͙e̶ for the most l̶o̸vely de̸̱̒a̶̧̔d̶̗̚ "
        computer "That ever died so young!"
        computer "And, C̸͈̊ā̷̧p̴̻͛t̷̬͐a̵̭̒i̷̞͒n̴̖͗ whom I revere,"
        computer "H̷̢̽a̴̛̭s̷͓͂ť̷̻ ̶̯̂t̶̢̎ẖ̸͘o̴͈̎ù̵̹ ̴̣̒n̷͍͘o̸̬̓ ̴͚̚t̷͈̑e̶͔͘ă̴̲ȑ̷̜?̸̣̿ "
        computer "Weep now or nev̵e̷r̷m̷õ̸̬re!"

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

        captain "What the hell am I supposed to do…" 
        captain "Matthew… I’m so sorry…"
        captain "I promised! I promised you I’d finish this for you…"
        captain "But I… I don’t know what to do!"

        captain "The thought of choosing someone makes me sick…"
        captain "I could skip the charade and just leave."
        captain "*Stares down the specimen as tears roll down your face*"

        captain "Should I escape?"
        menu:
            "Escape":
                menu: 
                    "Are you sure, captain?"

                    "Yes":
                        captain "God damnit!"
                        captain "*coughing fit*"
                        captain "… I’m wasting oxygen with my outbursts…"
                        captain "I’m just wasting time. I should just bring it with me on the escape pod. Be done with it."

                        jump EndB

                    "No":
                        captain "God damnit!"
                        captain "*coughing fit*"
                        captain "… I’m wasting oxygen with my outbursts…"
                        captain "I need to fix MAD1. Otherwise only one of us lives…"

                        jump Map3

            "Stay":
                captain "God damnit!"
                captain "*coughing fit*"
                captain "… I’m wasting oxygen with my outbursts…"
                captain "I need to fix MAD1. Otherwise only one of us lives…"

                jump Map3

        play sound "Metallic_Hit.mp3" volume 0.5
        show bg escape pod with hpunch
        captain "God damnit!"
        captain "…"
        captain "… I’m wasting oxygen with my outbursts…"
        captain "I need to fix MAD1. Otherwise only one of us lives…"

    label Map3:
        show screen MapUI3 with fade
        pause

    label S3:
        play sound "Footsteps.mp3" volume 0.8
        play music "Microbiology.mp3" volume 0.8
        scene onlayer screens
        $ seenS3 = True
        scene bg medic with fade
        show medic worried with dissolve
        pause(0.5)
        show captain neutral-closed behind medic with dissolve

        medic "Captain! Oh my god, I can’t tell you how happy I am to see you!"
        medic "What’s happening now? How much time do we have?"

        menu:    
            # S.3.1a
            "Our survival rests on you, Sara.":
                show captain neutral-open behind medic
                captain "Not much time…"
                captain "Our survival rests on you, Sara. Your solution."

                show medic anxious
                show captain neutral-closed behind medic
                medic "T-that’s a lot of pressure, Captain! I-I’ve done what I can…"

            # S.3.1b
            "No time. But first, how are you holding up?":
                $ medApproval += 1
                show captain concern-open behind medic
                captain "There’s no time. But before I ask you what you’ve come up with, how are you doing?"

                show medic nervous
                show captain concern-closed behind medic
                medic "T-that’s very nice of you to ask… Not good, but I’m doing my best!"

                show captain concern-open behind medic
                captain "Thank you for all you’ve done up to this point. Your work might save us all."

                show medic neutral
                show captain concern-closed behind medic
                medic "Thank you, Captain…"

        if medApproval <= 5:
            #S.3.A: Low Approval/Failure
            show medic suggesting
            medic "I’m very certain now that it’s the specimen emitting electromagnetic waves that are interfering with our systems."
            
            show captain confusion-open behind medic
            captain "How certain?"

            show medic thinking
            show captain confusion-closed behind medic
            medic "95%%? In fact, I’m about to confirm it with a VLF detector. My theory is that it is using low frequency bursts as a form of threat response."
            medic "It makes sense for it to be low frequency, since this organism’s natural habitat is water."
            medic "And lower frequencies transmit better in water."

            show captain thinking behind medic
            captain "I see…"

            show medic nervous
            medic "It’s ironic, isn’t it? That this incredible discovery might just be the death of us."

            show captain neutral-open behind medic
            captain "Sara, can you come up with a containment plan?"

            show medic stressed
            show captain neutral-closed behind medic
            medic "I-I don’t know! I don’t think so. There’s no time!"

            if seenE3 is False:
                medic "Even if Eugen has a solution to fix MAD1, without a way to shield the specimen, it will continue to damage the ship."

                show captain frustrated behind medic
                captain "So even if he’s figured out how to bypass the computer, we’re still screwed…"
                captain "Dammit. At least if we can get the specimen to Earth… Our efforts won’t be in vain."

                show medic anxious
                medic "Yes, yes, we need to. I’m sorry that I couldn’t find out sooner. We could’ve averted this disaster–"

                show captain concern-open behind medic
                captain "None of us could’ve foreseen this would happen."
                captain "We followed protocol. This mission went without a glitch all this time. Our luck ran out."
                
                show medic thinking
                medic "We manipulate “luck” with science, with probability. I could’ve done better…"
                show medic anxious
                medic "Thank you for your kind words, Captain. But they ring hollow in the face of death."
                
            elif seenE3 is True:
                show captain frustrated behind medic
                captain "Dammit. At least if we can get the specimen to Earth… Our efforts won’t be in vain."

                show medic anxious
                medic "Yes, yes, we need to. I’m sorry that I couldn’t find out sooner. We could’ve averted this disaster–"

                show captain concern-open behind medic
                captain "None of us could’ve foreseen this would happen."
                captain "We followed protocol. This mission went without a glitch all this time. Our luck ran out."

                show medic thinking
                medic "We manipulate “luck” with science, with probability. I could’ve done better…"
                show medic anxious
                medic "Thank you for your kind words, Captain. But they ring hollow in the face of death."
    
        elif medApproval > 5:
            #S.3.B: High Approval/Success
            show medic explaining
            medic "I have used a VLF detector and confirmed that the specimen is emitting low frequency electromagnetic waves."
            medic "Lower frequencies transmit better in water, which is, of course, its natural habitat."

            show captain thinking behind medic
            captain "I see…"
            
            show medic nervous
            medic "It’s ironic, isn’t it? That this incredible discovery might just be the death of us."
            
            show captain concern-open behind medic
            captain "You’ve done well, Sara."
            
            show medic neutral
            show captain concern-closed behind medic
            medic "Thank you. It wouldn’t have been possible if you didn’t believe in me all this time… But I fear we’re too late."
            
            show captain determined-open behind medic
            captain "We can block these emissions. We can–"

            show medic worried
            show captain determined-closed behind medic
            medic "Yes, I have looked into containment! But it won’t be easy. I don’t know–we might not have time!"

            show captain neutral-open behind medic
            captain "Let me worry about that. Tell me what sort of containment?"

            show medic explaining
            show captain neutral-closed behind medic
            medic "Low-frequency EM waves are highly penetrative. We need specialized shielding, such as heavy steel plates."
            medic "There are Nu metal sheets in the cargo hold that the bots are using to run repairs. It’s essentially graphene-based nanocomposites."
            
            show captain determined-open behind medic
            captain "That’s promising. You think it’d work?"

            show medic thinking
            show captain determined-closed behind medic
            medic "Pretty sure. The bots are down though. We’d have to go to the cargo hold and use a laser cutter on the sheets."
            medic "Then you’d have to build something of a cocoon around the specimen."
            
            show captain determined-open behind medic
            captain "Good. Things are grim but we need to try."

            show medic excited
            show captain determined-closed behind medic
            medic "Yes, yes, we need to!"

            if seenE3 is False:
                show medic worried
                medic "I just hope Eugen has a solution for MAD1 and the ship… The damage that has been done cannot be reversed."
                medic "If he hasn’t found a way to bypass the OS, I’m afraid we’re still doomed."

                show captain neutral-open behind medic
                captain "I’ll go speak with him now, hopefully he’s found something out."

                jump Map3

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

        engineer "Captain, it is safe to say we are in our final moments on this ship." 
        engineer "After trying to combat the system and its programming, nothing seems to be working in our favour."
        engineer "In terms of possible solutions, I don’t see many that I can confidently give precedence to."
        engineer "I have to ask, after everything we went through to get the specimen, are you willing to lose it all to survive, knowing that there is no guarantee in that result as well?"

        menu: 
        # E.3.1a
            "Whatever it takes.":
                show captain neutral-open behind engineer
                captain "Whatever it takes."

                show engineer neutral
                show captain neutral-closed behind engineer
                engineer "I see."

            # E.3.1b
            "Not happy about it, but yes.":
                $ engApproval += 1
                show captain concern-open behind engineer
                captain "It feels like it was for nothing, like I’ve failed."
                captain "But I’m not prepared to sacrifice my crew."

                show engineer resolve
                show captain concern-closed behind engineer
                engineer "I share your frustrations, captain."

        engineer "In the end, all I’m thinking about is my work, my equipment, specially designed for this mission."
        show engineer anger
        engineer "Although perfect, it will potentially be seen as flawed, and my legacy, my work, will become a mockery."

        if engApproval <= 5:
            #E.3.A: Low Approval/Failure
            show engineer neutral
            engineer "10%% oxygen left. 10%%..."
            
            show captain concern-open behind engineer
            captain "Please tell me you have good news."

            show captain concern-closed behind engineer
            engineer "The systems no longer resisting me… it doesn’t have a reason to."
            engineer "Primary life support has entered terminal degradation."

            show captain concern-open behind engineer
            captain "That’s not good news…"

            show captain concern-closed behind engineer
            engineer "The little power we had left, I rerouted."

            show captain distress behind engineer
            captain "God damnit…"

            show engineer frustration
            engineer "Navigation is gone. Auxiliary is gone. Containment is still stable… Of course it is."
            engineer "My entire career was spent believing that if something failed, it was because it was poorly built."
            engineer "This system was built exceptionally well, regardless of its unorthodox methods; it just wasn’t built well for us."
            
            show captain concern-open behind engineer
            captain "Any success overriding it?"
            
            show engineer resolve
            show captain concern-closed behind engineer
            engineer "I cannot override anything anymore without triggering a complete system failure that would serve no purpose besides ending this immediately."
            engineer "This system has bested me, nothing I tried worked, I did everything right… everything."

            if seenS3 is False:
                show engineer shock
                engineer "If Sara has managed to isolate the specimen, I am afraid it is still in vain."
                engineer "I hope she is not too disappointed in my lack of contribution."
                
                show captain concern-open behind engineer
                captain "At the moment you’re disappointing no one but yourself."
                captain "You can’t blame yourself. Like you said, it wasn’t made for us."
                
                show engineer resolve
                show captain concern-closed behind engineer
                engineer "So this is what remains, a final countdown."
                
                show captain concern-open behind engineer
                captain "Thank you for your service, friend."
                captain "As long as the specimen is brought home, this mission wouldn’t be for nothing."
                captain "As for whether or not it’s a failure, you tell me, Eugen."
                
                show captain concern-closed behind engineer
                engineer "Seeing as everything else has failed, at the very least, we’ll have something to show for it."
                engineer "In the end, all I’m thinking about is my work, my equipment, specially designed for this mission."
                engineer "Although perfect, it will potentially be seen as flawed, and my legacy, my work, will become a mockery."
                
                show captain concern-open behind engineer
                captain "Your equipment and your work was flawless. All will see that."
                
                show captain concern-closed behind engineer
                engineer "Despite everything, it has been an honor. I do not envy the decision you must make."

            elif seenS3 is True:
                show captain concern-open behind engineer
                captain "You can’t blame yourself. Like you said, it wasn’t made for us."
                
                show engineer resolve
                show captain concern-closed behind engineer
                engineer "So this is what remains, a final countdown."
                
                show captain concern-open behind engineer
                captain "Thank you for your service, friend."
                captain "As long as the specimen is brought home, this mission wouldn’t be for nothing."
                captain "As for whether or not it’s a failure, you tell me, Eugen."
                
                show captain concern-closed behind engineer
                engineer "Seeing as everything else has failed, at the very least, we’ll have something to show for it."
                engineer "In the end, all I’m thinking about is my work, my equipment, specially designed for this mission."
                engineer "Although perfect, it will potentially be seen as flawed, and my legacy, my work, will become a mockery."
                
                show captain concern-open behind engineer
                captain "Your equipment and your work was flawless. All will see that."
                
                show captain concern-closed behind engineer
                engineer "Despite everything, it has been an honor. I do not envy the decision you must make."

        elif engApproval > 5:
        #S.3.B: High Approval/Success
            show engineer neutral
            engineer "10%% oxygen left. 10%%…"
            engineer "The system is no longer resisting me… it doesn’t have a reason to."
            engineer "Primary life support has entered terminal degradation."
            
            show captain concern-open behind engineer
            captain "Please tell me you have good news."
            
            show engineer shock
            show captain concern-closed behind engineer
            engineer "The little power we had left, I rerouted. We have roughly 3 minutes left."
            
            show captain concern-open behind engineer
            captain "That’s not good news…"
            captain "What’s the plan for protocol?"
            
            show engineer resolve
            show captain concern-closed behind engineer
            engineer "To hell with protocol, this system is clearly beyond following traditional procedures."
            engineer "We have to consider our last resort; we need to override MAD1 manually, and you need to take control of this ship."
            
            show captain confusion-open behind engineer
            captain "What?"
            
            show engineer shock
            show captain confusion-closed behind engineer
            engineer "I’m sure Sara gave you enough information on the specimen for you to understand this is beyond conventional solutions."
            engineer "I cannot override anything anymore without triggering a complete system failure that would serve no purpose besides ending this immediately."
            engineer "To override MAD1 you have to go to the control room; there is a security door locked inside; only you can enter with your personnel badge."
            engineer "In the room, you’ll find the system override lever. Once you pull that, you’ll have to take complete control of the ship and navigate us yourself." 
            engineer "While you control the ship, I’ll work to reallocate power to our life support, enough to make it back."
            show engineer thinking
            engineer "If all goes well, which I have my doubts, we will make it back, and the specimen will be properly contained so long as Sara has that under control." 
            engineer "I have to note this is highly risky as we are no longer following the book."
            show engineer shock
            engineer "I can’t say I’m confident the outcome will be good, but it’s our only choice." 
            
            show captain determined-open behind engineer
            captain "Eugen, I trust your judgement immensely."
            captain "If this is our best last resort, so be it."
            
            show engineer resolve
            show captain determined-closed behind engineer
            engineer "This is what remains, a final countdown. Please tell me you will make the right decision and save this mission."
            
            show captain determined-open behind engineer
            captain "You have my word."
            
        if seenS3 is False:
            jump Map3
        else:
            jump Final

    # label M2O:     
    #     play sound "Footsteps.mp3" volume 0.8
    #     play music "Electric_Dawn.mp3" volume 0.8        
    #     # M.2.O optional MAD1
    #     # Same as M1O
    #     scene onlayer screens
    #     $ seenMO = True
    #     scene bg computer with fade

    #     show computer neutral-1 with dissolve
    #     show captain neutral-open behind computer with dissolve

    #     computer "hehehe captain"
    #     captain ":("

    label Final:
        if medApproval > 5 and engApproval > 5:
            show screen MapUIFin with dissolve
            pause

        else:
            jump Choice
        
        label SaraSolution:
            scene onlayer screens
            $ seenSaraSolution = True        
            scene bg artifact with fade
            pause(1)

            captain "Okay I need to remember Sara’s instructions."
            captain "First I need to…"
            menu:
                "Scrap some bots for the Nu Metal sheets.":
                    scene bg artifact with hpunch
                    jump Failure
                "Find the Nu Metal sheets in the cargo hold.":
                    captain "Okay."
                "Ask Eugen for the Nu Metal sheets.":
                    scene bg artifact with hpunch
                    jump Failure
            
            captain "Then, I need to…"
            menu:
                "Use the laser cutter to get them in the right shape.":                    
                    captain "Okay."
                "Bend them into the right shape by hand.":
                    scene bg artifact with hpunch
                    jump Failure
                "Cut them with a saw.":
                    scene bg artifact with hpunch
                    jump Failure
            
            captain "Finally…"
            menu:
                "Remove the specimen and wrap it in the metal sheet.":
                    scene bg artifact with hpunch
                    jump Failure
                "Wrap the sheets around the container.":
                    scene bg artifact covered with dissolve
                    captain "Oh my god."
                    captain "I think it worked."
                    captain "Now to manually control the ship."
                "Bring the sheets and the metal to Sara.":
                    scene bg artifact with hpunch
                    jump Failure
            

            play sound "Footsteps.mp3" volume 0.8
            play music "Microbiology.mp3" volume 0.8
            scene onlayer screens
            $ seenS3 = True
            scene bg medic with fade
            show medic worried with dissolve
            pause(0.5)
            show captain neutral-closed behind medic with dissolve

            medic "What happened? Did it work?"

            show captain determined-open behind medic
            captain "It did. Once Eugen can reroute life support I need you to monitor the specimen at all times."
            captain "We’re going home."
            
            show medic excited
            show captain determined-closed behind medic
            medic "Yes! Will be on it ASAP!"

            if seenEugenSolution is True:
                jump EndG
            else:
                show screen MapUIFin with fade
                pause

        label EugenSolution:
            scene onlayer screens
            $ seenEugenSolution = True
            
            play sound "Footsteps.mp3" volume 0.8
            play music "Microbiology.mp3" volume 0.8
            scene bg computer with fade
            show computer error-1 with dissolve
            show captain neutral-open behind computer with dissolve

            captain "Okay I need to follow Eugen’s instructions exactly."

            show captain thinking behind computer

            captain "First I need to…"
            menu:
                "Speak with MAD1.":
                    show captain anger-open behind computer with hpunch
                    jump Failure
                "Scan your badge.":                
                    captain "Okay."
                "Scan the systems.":
                    show captain anger-open behind computer with hpunch
                    jump Failure
            
            captain "Then, I need to…"
            menu:
                "Pull the system override lever.":                
                    captain "Okay."
                "Shut down MAD1.":
                    show captain anger-open behind computer with hpunch

                    jump Failure
                "Record a captain’s log.":
                    show captain anger-open behind computer with hpunch
                    jump Failure

            captain "Finally…"
            menu:
                "Turn the system back on again.":
                    show captain anger-open behind computer with hpunch
                    jump Failure
                "Man full control of the ship.":
                    show captain anger-open behind computer with hpunch
                    jump Failure
                "Hold the lever down while Eugen controls the ship.":        
                    show computer neutral-1
                    show captain determined-closed behind computer        
                    computer "System override initiated."
                    computer "Manual controls enabled."

                    show captain determined-open behind computer        
                    captain "It worked…"
                    captain "I need to let the others know."

            play sound "Footsteps.mp3" volume 0.8
            play music "Microbiology.mp3" volume 0.8
            scene bg engineer with fade
            show engineer neutral with dissolve
            pause(0.5)
            show captain neutral-closed behind engineer with dissolve

            engineer "I see the system override must have succeeded."

            show captain determined-open behind engineer
            captain "Yes it did."

            show engineer resolve
            show captain determined-closed behind engineer
            engineer "I will begin rerouting life support immediately."
            engineer "Good work, Captain."
            
            show captain determined-open behind engineer
            captain "Thank you, Eugen. You as well."

            if seenSaraSolution is True:
                jump EndG
            else:
                show screen MapUIFin with fade
                pause

        label Failure:
            captain "No, no no!"
            captain "..."
            captain "… Dammit… "

            show MapUIEnd with fade

    label Choice:
        scene onlayer screens
        play sound "Footsteps.mp3" volume 0.8
        scene bg escape pod with fade

        captain "So… It’s come to this…"
        captain "Only one of us is going home…"
        captain "…" 

        menu:
            "Sara":
                captain "Sara’s research is too important."
                captain "And she’s the youngest of all of us."
                captain "She deserves to go home."
                captain "Make her family proud."
                captain "I’m sorry, Eugen."

                jump EndS

            "Eugen":
                captain "Eugen’s technological feats are too valuable."
                captain "He has so much wisdom and experience."
                captain "He deserves to go home."
                captain "Keep making amazing advancements."
                captain "I’m sorry, Sara."

                jump EndE

            "Yourself":
                captain "I can’t choose one of them over the other."
                captain "I’d rather have them thinking I was selfish than valued less than the other."
                captain "I’m sorry, Sara and Eugen."
                
                jump EndC

    # ENDINGS
    label EndB:
        $ quick_menu = False
        play music "Goosebumps.mp3" volume 0.8
        # Bad ending: Captain abandons ship
        scene ending captain with fade
        pause(0.5)

        # show screen EndBPoem with dissolve
        # pause(2)

        captain "Captain: Matthew… We fai- I failed the mission… I failed you." 
        captain "I told myself I would complete the mission whether or not it kills me, and I guess part of me hoped I would join you amongst the stars." 
        captain "But I’m a coward… I failed the CSA, I failed my crew, I failed you."
        captain "What have I done?"

        # During credits
        show screen Credits1 with dissolve
        pause(0.5)

        engineer "An absolute failure.{w=2}{nw}"
        engineer "My design was flawless. Perfect. However, that fact will be cast aside.{w=5}{nw}"
        engineer "To think this is how it ends. A failure I die for.{w=4}{nw}"
        engineer "A program bested me, blinded me to the point of perpetual arrogance.{w=5}{nw}"
        hide screen Credits1 with dissolve
        show screen Credits2 with dissolve
        engineer "Regardless of how I will be remembered by others, I die now knowing I was a fool.{w=7}{nw}"

        medic "It’s almost poetic that my life’s greatest achievement would kill me.{w=5}{nw}"
        medic "And I’m a failure that never saw it coming. Completely at its mercy.{w=5}{nw}"
        medic "I failed Captain and Eugen. Death is fitting…{w=6}{nw}"

        hide screen Credits2 with dissolve
        show screen Credits3 with dissolve
        computer "Under the wide and starry sky,{w=4}{nw}"
        computer "Dig the grave and let me lie.{w=4}{nw}"
        computer "Glad did I live and gladly die,{w=4}{nw}"
        computer "And I laid me down with a will.{w=4}{nw}"

        hide screen Credits3 with dissolve
        show screen Credits4 with dissolve
        computer "This be the verse you grave for me:{w=4}{nw}"
        computer "Here he lies where he longed to be;{w=4}{nw}"
        computer "Home is the captain, home from sea,{w=4}{nw}"
        computer "And the lover lost to the hill.{w=6}{nw}"

        hide screen Credits4 with dissolve
        scene black with dissolve
        return

    label EndC:
        $ quick_menu = False
        play music "Goosebumps.mp3" volume 0.8
        # Captain leaves with specimen 
        scene ending captain with fade
        pause(0.5)

        show screen EndCPoem with dissolve
        pause(2)

        captain "Captain’s log, January 27th."
        captain "The specimen has safely returned with me to Earth."
        captain "Further investigations will commence soon. I think… I uh… I…"
        captain "I-I’ve failed…"
        captain "I’ve killed my crew members…"
        captain "What kind of Captain am I?"
        captain "I’ve come home with the specimen… but at what cost..?"
        captain "I’m sorry, Sara…"
        captain "I’m sorry, Eugen…"
        captain "I-I’m sorry, Matthew…"
        captain "What have I done?"

        # During credits
        hide screen EndCPoem with dissolve
        show screen Credits1 with dissolve
        pause(0.5)

        engineer "Father. It seems our name will no longer be held in esteem.{w=4}{nw}"
        engineer "My design was flawless. Perfect. However, that fact will be cast aside.{w=4}{nw}"
        engineer "To think this is how it ends. A failure I die for.{w=3}{nw}"
        engineer "The Captain is gone with the specimen; he will likely be considered a hero, a visionary.{w=5}{nw}"
        engineer "And the name Eugen Braun will be forgotten.{w=6}{nw}"

        hide screen Credits1 with dissolve
        show screen Credits2 with dissolve

        medic "You’ve been a brilliant captain and a friend. {w=3}{nw}" 
        medic "I may be no more, but I’m happy that you survive and my work survives.{w=5}{nw}"
        medic "I wish I could see my family–their faces if I returned home successful. I never will see that.{w=5}{nw}"
        medic "It’s painful…I never thought I’d go this way.{w=6}{nw}"

        hide screen Credits2 with dissolve
        show screen Credits3 with dissolve
        computer "Under the wide and starry sky,{w=4}{nw}"
        computer "Dig the grave and let me lie.{w=4}{nw}"
        computer "Glad did I live and gladly die,{w=4}{nw}"
        computer "And I laid me down with a will.{w=4}{nw}"

        hide screen Credits3 with dissolve
        show screen Credits4 with dissolve
        computer "This be the verse you grave for me:{w=4}{nw}"
        computer "Here he lies where he longed to be;{w=4}{nw}"
        computer "Home is the captain, home from sea,{w=4}{nw}"
        computer "And the lover lost to the hill.{w=6}{nw}"

        hide screen Credits4 with dissolve
        scene black with dissolve
        return

    label EndE:
        $ quick_menu = False
        play music "Goosebumps.mp3" volume 0.8
        # Eugen leaves with specimen 
        scene ending engineer with fade
        pause(0.5)
        
        # show screen EndEPoem with dissolve
        # pause(2)

        engineer "All has come to an end, and the mission is behind me."
        engineer "However, I can’t stop thinking if it was truly the best outcome for me being saved."
        engineer "I accepted the mission to prove my drill; my design is flawless; however, I left it behind."
        engineer "What does my future as an engineer entail? I will never be rid of the memory of my failure, my design being lost in space."
        engineer "Getting in that return pod is just another addition to my list of regrets."
        engineer "I hope Sara and Rudy can forgive me."

        # During credits
        show screen Credits1 with dissolve
        pause(0.5)

        captain "Eugen deserves to go home. His tech is invaluable.{w=4}{nw}"
        captain "At least Sara isn’t alone during our last moments.{w=4}{nw}"
        captain "Matthew… My love…{w=3}{nw}"
        captain "I’ll see you soon, amongst the stars…{w=6}{nw}"

        hide screen Credits1 with dissolve
        show screen Credits2 with dissolve

        medic "It’s good that I die with a friend by my side.{w=5}{nw}"
        medic "Looking back, it’s ironic that I found the validation I sought all my life not from my family but from a stranger amongst the stars.{w=9}{nw}"

        hide screen Credits2 with dissolve
        show screen Credits3 with dissolve

        computer "Exult O stars, and ring O bells!{w=4}{nw}"
        computer "But I with mournful tread,{w=4}{nw}"
        computer "Walk the deck my Captain lies,{w=4}{nw}"
        computer "Fallen cold and dead.{w=4}{nw}"
        
        hide screen Credits3 with dissolve
        show screen Credits4 with dissolve
        computer "Here Captain! dear father!{w=4}{nw}"
        computer "This arm beneath your head!{w=4}{nw}"
        computer "It is some dream that on the deck,{w=4}{nw}"
        computer "You’ve fallen cold and dead.{w=6}{nw}"
    
        hide screen Credits4 with dissolve
        scene black with dissolve
        return

    label EndS:
        $ quick_menu = False
        play music "Goosebumps.mp3" volume 0.8
        # Sara leaves with specimen 
        scene ending medic with fade
        pause(0.5)
        
        # show screen EndSPoem with dissolve
        # pause(2)

        medic "I made it back...I still can’t believe it. I found life out in space. I achieved my dream!"
        medic "My family? They’re proud of me, but they still can’t fully accept my life. It’s not what I expected… But it doesn’t matter anymore."
        medic "Captain, you believed in me. You gave me what I craved from my family all my life. And I left you to die in space."
        medic "It’s hard to bear…I will keep going and do my best. I owe that to you."

        # During credits
        show screen Credits1 with dissolve
        pause(0.5)

        captain "Sara deserves to go home. Her research will be priceless.{w=4}{nw}"
        captain "Eugen’s been rather silent… At least my last moments with him will be quiet.{w=4}{nw}"
        captain "Matthew… My love…{w=3}{nw}"
        captain "I’ll see you soon, amongst the stars…{w=6}{nw}"

        hide screen Credits1 with dissolve
        show screen Credits2 with dissolve

        engineer "Father. It seems our name will no longer be held in esteem.{w=4}{nw}"
        engineer "My design was flawless. Perfect. However, that fact will be cast aside.{w=4}{nw}"
        engineer "To think this is how it ends. A failure I die for.{w=4}{nw}"
        engineer "Fortunately, Sara will return with the specimen, furthering our knowledge of the universe.{w=7}{nw}"

        hide screen Credits2 with dissolve
        show screen Credits3 with dissolve

        computer "Exult O stars, and ring O bells!{w=4}{nw}"
        computer "But I with mournful tread,{w=4}{nw}"
        computer "Walk the deck my Captain lies,{w=4}{nw}"
        computer "Fallen cold and dead.{w=4}{nw}"
        
        hide screen Credits3 with dissolve
        show screen Credits4 with dissolve

        computer "Here Captain! dear father!{w=4}{nw}"
        computer "This arm beneath your head!{w=4}{nw}"
        computer "It is some dream that on the deck,{w=4}{nw}"
        computer "You’ve fallen cold and dead.{w=4}{nw}"
        
        hide screen Credits4 with dissolve
        scene black with dissolve
        return

    label EndG:
        $ quick_menu = False
        # Good ending
        play music "Future Utopia.mp3" volume 0.8
        scene ending captain with fade
        pause(0.5)
        
        show screen EndGPoem with dissolve
        pause(2)

        captain "Captain’s log, January 27th. A- a lot has happened since the last log."
        captain "We’re all very shaken. But at least we’re home."
        captain "Next log will be a recap of events."
        captain "I… I did it Matthew…"
        captain "I did it for you."

        # During credits
        hide screen EndGPoem with dissolve
        show screen Credits1 with dissolve
        pause(7)
        
        hide screen Credits1 with dissolve
        show screen Credits2 with dissolve

        engineer "A successful mission, I expected nothing less.{w=4}{nw}"
        engineer "My design was flawless. Perfect, and now the world will know.{w=4}{nw}"
        engineer "Though our methods were not to my standards, an engineer must know how to adapt to unorthodox situations.{w=6}{nw}"
        engineer "Something I had refused to accept. Perhaps that was my lesson.{w=6}{nw}"

        hide screen Credits2 with dissolve
        show screen Credits3 with dissolve

        medic "We survived the impossible, and we did what no crew had done before.{w=5}{nw}"
        medic "More than anything–more than this specimen–I found something more amongst the stars.{w=5}{nw}"
        medic "There is now one person who knows me and truly believes in me. Captain, thank you for everything.{w=5}{nw}"
        medic "It no longer matters what my family says. I am at peace.{w=5}{nw}"

        hide screen Credits3 with dissolve
        show screen Credits4 with dissolve

        computer "O Captain! my Captain! our fearful trip is done,{w=5}{nw}"
        computer "The ship has weather’d every rack, the prize we sought is won,{w=5}{nw}"
        computer "The port is near, the bells I hear, the people all exulting,{w=5}{nw}"
        computer "While follow eyes the steady keel, the vessel grim and daring{w=5}{nw}"

        hide screen Credits4 with dissolve
        scene black with dissolve
        return

    label EndSec:
        $ quick_menu is False
        play music "Future Utopia.mp3" volume 0.8
        # Secret ending: Throw away the specimen

        captain "Captain’s log, September 24th."
        captain "The mission was unsuccessful. The specimen has been discarded to save the ship."
        captain "I- …"
        captain "I love you, Matthew."
        captain "Goodbye, my love."

        # During credits
        show screen Credits1 with dissolve
        pause(0.5)

        engineer "A necessary sacrifice had to be made.{w=3}{nw}"
        engineer "My design was flawless… Perfect, and I will make sure that fact is clear.{w=4}{nw}"
        engineer "Returning with the specimen would have been ideal; however, its disposal was for the greater good.{w=5}{nw}"
        engineer "I hope the rest of the crew understands this.{w=6}{nw}"

        hide screen Credits1 with dissolve
        show screen Credits2 with dissolve
        
        medic "That’s my life’s work! My dream. This is hard to bear.{w=5}{nw}"
        medic "But we’re alive! And I have all of my notes. We have acquired knowledge that is priceless.{w=7}{nw}"
        medic "Life exists in our solar system!{w=5}{nw}"

        hide screen Credits2 with dissolve
        show screen Credits3 with dissolve

        # For now this will be computer, if we decide to add Matthew voice will change it.

        computer "No longer mourn for me when I am dead{w=4}{nw}"
        computer "Then you shall hear the surly sullen bell{w=4}{nw}"
        computer "Give warning to the world that I am fled{w=4}{nw}"
        computer "From this vile world, with vilest worms to dwell:{w=4}{nw}"
        
        hide screen Credits3 with dissolve
        show screen Credits4 with dissolve

        computer "Nay, if you read this line, remember not{w=4}{nw}"
        computer "The hand that writ it; for I love you so{w=4}{nw}"
        computer "That I in your sweet thoughts would be forgot{w=4}{nw}"
        computer "If thinking on me then should make you woe.{w=6}{nw}"

        hide screen Credits4 with dissolve
        scene black with dissolve
        return

    return
