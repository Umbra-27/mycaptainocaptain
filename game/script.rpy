# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define captain = Character("Captain", image="captain/captain", kind=bubble)
define engineer = Character("Eugene", image="engineer placeholder", kind=bubble)
define medic = Character("Sarah", image="medic placeholder", kind=bubble)
define computer = Character("MAD1", image="computer/computer", kind=bubble)

# realigning captain images
image captain neutral-open = Image("captain/captain neutral-open.png", yalign=0.25)
image captain anger-open = Image("captain/captain anger-open.png", yalign=0.25)

# dark ver
image bgCompDark = im.MatrixColor(
    "bg computer.png",
    im.matrix.brightness(-0.5))

image captainDark = im.MatrixColor(
    "captain",
    im.matrix.brightness(-0.5))

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
    play sound "error.mp3"
    computer "Error. Error. E̷̠̓r̷̖͆r̵̼͋o̷̳̔r"

    show captain confusion-open with hpunch 
    captain "What’s happening? MAD1, show me the error logs."

    scene bg computer error bad
    show computer error-1
    show captain confusion-closed behind computer

    computer "Error. Unable to end process." 
    computer "Pulling error log̶̕s. Ê̴̋͒͠r̵̛̈̏r̸̳̯͎͍̬̊̇̀o̵r̷͘. Sys̷̖̏ṭ̷̋e̵̗̬͋m̵̩͋̕ṡ̴̨͎ dò̷̧͎͍͇̫͆̕ẃ̵̛̔n̶-"

    stop sound
    play sound "systems_off.mp3"
    scene bgCompDark
    show computer error-2
    show captainDark behind computer

    "The lights go out. Everything stops. The buzz and rumbles of the ship go deadly silent, and it’s as if time and space have frozen solid." 
    "Everything goes wrong."
    "Only one terminal blinks online."

    computer "But O heart! heart! H̷̢̚e̷a̵ŕ̶̤t̵͈́!̵̺̾
                O the b̵̝̀l̷̨͠e̶̹̕ȩ̵̔d̴̲̅i̶n̵̕ġ̷͍ drops of red,
                Where on the deck my Captain lies,
                Fallen cold and d̸̻̈́e̵͉̋a̸̪̿d̸̙͆."

    "The terminal displays strange text. I’ve never seen MAD1 act this way before."

    show captain confusion-open behind computer
    captain "What the hell?" 
    
    show captain confusion-closed behind computer   
    play sound "captain_smack_1.mp3" 
    captain "(Smacks terminal)" with hpunch 

    play sound "systems_back_online.mp3"
    play music "Ice_Cold.mp3"

    "Then the lights come on again. Thankfully."
    "Sound returns as I presume the system reboots."

    computer "System force restart. Diagnostics complete." 
    computer "Power systems offline. Emergency power engaged." 
    computer "Navigation systems paused." 
    computer "Internal communications offline." 
    computer "Satellite communication offline." 
    computer "Data systems offline." 
    computer "Thermal control offline." 
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
    
    show captain anger-open behind computer 

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

    menu:
        "Speak to Eugene":
            captain "I should speak to Eugene. He’ll probably know what’s happening."
            #block of code to run
            jump endDemo

        "Speak to Sarah":
            captain "I should speak to Sarah. She’s probably freaking out right now."
            #block of code to run
            jump endDemo
        
    label endDemo:
        "End of MVP"

    return
