################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")
    activate_sound "audio/Button_Select.mp3"
    
style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/scroll-bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_idle_thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/PreferencePage-Option2-SliderContainer.png", gui.slider_borders, tile=gui.slider_tile)
    thumb Frame("gui/slider/PreferencePage-Option2-Slider.png", gui.slider_borders, tile=gui.scrollbar_tile)

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/PreferencePage-Option2-SliderContainer.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb Frame("gui/slider/PreferencePage-Option2-Slider.png", gui.slider_borders, tile=gui.scrollbar_tile)


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=0.5)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    hbox:
        for i in items:
            textbutton i.caption action i.action

style choice_hbox is hbox
style choice_button is button
style choice_button_text is button_text

style choice_hbox:
    xalign 0.5
    ypos 605
    xanchor 0.5
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    activate_sound "audio/Button_Select.mp3"
style choice_button_text is default:
    hover_bold True
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Back") action Rollback()
            # textbutton _("History") action ShowMenu('history')
            # textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            # textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"
        spacing gui.navigation_spacing

        if main_menu and not renpy.get_screen("load") and not renpy.get_screen("preferences"):
            textbutton _("NEW GAME") action Start():
                pos (928, 288)
            
            textbutton _("LOAD GAME") action ShowMenu("load"):
                pos (960, 352)   
            
            textbutton _("OPTIONS") action ShowMenu("preferences"):
                pos (962, 418)

            if renpy.variant("pc"):
                textbutton _("QUIT") action Quit(confirm=True):
                    pos (935, 475)

            imagebutton:
                xpos 1750    
                ypos 630
                idle "gui/information-button.png" 
                hover "gui/information-button.png" 
                action ShowMenu("help")

            imagebutton:
                if persistent.secret_unlocked is True:
                    xpos 1529    
                    ypos 450
                    idle "gui/gallery-icon-expanded.png" 
                    hover "gui/gallery-icon-expanded.png" 
                    action ShowMenu("gallery") 
                else: 
                    xpos 1750    
                    ypos 450
                    idle "gui/gallery-icon.png" 
                    hover "gui/gallery-icon.png"  
                    action NullAction()

            # Ending Stars
            hbox:
                # Bad End Star
                imagebutton:
                    xpos 0
                    ypos 450
                    if persistent.endB_unlocked is True:
                        idle "images/End Stars@15/endB.PNG"                    
                        hover "images/End Stars@15/endB.PNG"
                        action Replay("EndBLog")
                    else:
                        idle "images/End Stars@15/empty star.PNG"                    
                        hover "images/End Stars@15/empty star.PNG"
                        action NullAction()
                
                # Sara Star
                imagebutton:
                    xpos 0
                    ypos 450
                    if persistent.endS_unlocked is True:
                        idle "images/End Stars@15/endS.PNG"                    
                        hover "images/End Stars@15/endS.PNG"
                        action Replay("EndSLog")
                    else:
                        idle "images/End Stars@15/empty star.PNG"                    
                        hover "images/End Stars@15/empty star.PNG"
                        action NullAction()

                # Eugen Star
                imagebutton:
                    xpos 0
                    ypos 450
                    if persistent.endE_unlocked is True:
                        idle "images/End Stars@15/endE.PNG"                    
                        hover "images/End Stars@15/endE.PNG"
                        action Replay("EndELog")
                    else:
                        idle "images/End Stars@15/empty star.PNG"                    
                        hover "images/End Stars@15/empty star.PNG"
                        action NullAction()

                # Captain Star
                imagebutton:
                    xpos 0
                    ypos 450
                    if persistent.endC_unlocked is True:
                        idle "images/End Stars@15/endC.PNG"                    
                        hover "images/End Stars@15/endC.PNG"
                        action Replay("EndCLog")
                    else:
                        idle "images/End Stars@15/empty star.PNG"                    
                        hover "images/End Stars@15/empty star.PNG"
                        action NullAction()

                # Good End Star
                imagebutton:
                    xpos 0
                    ypos 450
                    if persistent.endG_unlocked is True:
                        idle "images/End Stars@15/endG.PNG"                    
                        hover "images/End Stars@15/endG.PNG"
                        action Replay("EndGLog")
                    else:
                        idle "images/End Stars@15/empty star.PNG"                    
                        hover "images/End Stars@15/empty star.PNG"
                        action NullAction()

                # Secret Star
                imagebutton:
                    xpos 0
                    ypos 450
                    if persistent.endSEC_unlocked is True:
                        idle "images/End Stars@15/endSEC.PNG"                    
                        hover "images/End Stars@15/endSEC.PNG"
                        action Replay("EndSECLog")
                    else:
                        idle "images/End Stars@15/empty star.PNG"                    
                        hover "images/End Stars@15/empty star.PNG"
                        action NullAction()

        else:
            # FIX: These buttons must be indented 4 spaces further than the 'else:'
            textbutton _("Resume") action Return()
            textbutton _("Save Game") action ShowMenu("save")
            textbutton _("Settings") action ShowMenu("preferences")
            textbutton _("Exit Game") action MainMenu(False)

screen pause():
    tag menu
    
    # ADD BACKGROUNDS HERE
    
    add "gui/pause_overlay.png" alpha 1.00
    add "gui/pause_abstract_background.png"
    add "gui/pause_abstract_background.png"
    use game_menu(_("Game Paused"))
    
screen pause_navigation():
    vbox:
        style_prefix "navigation"
        
        # 1. Expand the vbox to the full width of the screen
        xfill True  
        
        yalign 0.5
        spacing gui.navigation_spacing

        textbutton _("Resume") action Return()
        textbutton _("Save Game") action ShowMenu("save") 
        textbutton _("Settings") action ShowMenu("preferences")
        textbutton _("Exit Game") action MainMenu(confirm=True)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    # 2. REMOVE size_group "navigation"
    properties gui.button_properties("navigation_button")
    
    activate_sound "audio/Button_Select.mp3"

    # 3. Center the button and its contents
    xalign 0.5
    
    hover_background Transform("gui/menu_item_highlight.png", xalign=0.5, yalign=0.5, zoom=0.99)
    
style navigation_button_text:
    properties gui.text_properties("navigation_button")
    font "fonts/Orbitron-VariableFont_wght.ttf"
    
    # 4. Ensure the text inside the button is centered
    text_align 0.5
    xalign 0.5
    
    hover_bold True
    color "#ffffff"
    hover_color "#ffffff"
    size 44    

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "gui/main_menu.png"
    add "gui/abstract_details_layer.png"
    # Add your logo here
    add "images/logo.png":
        pos (25,400)
    ## This empty frame darkens the main menu.
    ##frame:
    ## style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    ##if gui.show_name:

       ## vbox:
          ##  style "main_menu_vbox"

          ##  text "[config.name!t]":
             ##   style "main_menu_title"

           ## text "[config.version]":
            ##    style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add "gui/pause_abstract_background.png"
        add "gui/pause_overlay.png" alpha 0.85
        add "gui/pause_abstract_background.png"

# This should be at the bottom of the game_menu screen, 
    # not indented inside the 'hbox' or 'frame' blocks.
    if title == _("Pause") or title == _("Game Paused"):
        use pause_navigation
        
    
    # 2. Show the content frame for EVERY screen EXCEPT the Pause screens
    else:
        frame:
            style "game_menu_outer_frame"
            hbox:
                frame:
                    style "game_menu_navigation_frame"
                    # Optional: use navigation here if you want a sidebar on Save/Load
                
                frame:
                    style "game_menu_content_frame"
                    if scroll == "viewport":
                        viewport:
                            yinitial yinitial
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True
                            side_yfill True
                            vbox:
                                spacing spacing
                                transclude
                    else:
                        transclude

    # 3. Handle the Return button for sub-menus
    key "game_menu" action Return()
    if title != _("Pause") and title != _("Game Paused"):
        textbutton _("Return"):
            style "return_button"
            action Return()
    
    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label:
    xalign 0.5        # Change from xpos 75 to xalign 0.5
    #ypos 20           # Adjust this to move the title up or down
    yalign 0.06
    ysize 400

style game_menu_label_text:
    font "fonts/Orbitron-VariableFont_wght.ttf" # Use your custom font
    size 54
    color "#ffffff"
    xalign 0.5        # Center the text inside the label
    text_align 0.5
    yalign 0.5

style return_button is default:
    properties gui.button_properties("return_button")
    # Add subpixel=True to stop the graphic from snapping to pixels
    hover_background Transform("gui/menu_item_highlight.png", xalign=0.5, yalign=0.5, zoom=0.99, subpixel=True)
    xoffset 60
    
style return_button_text is navigation_button_text:
    properties gui.text_properties("navigation_button")
    size 44
    color "#ffffff"
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 300

    background None
    

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xalign 0.5        # Centers the container horizontally
    yalign 0.06       # Adjusts vertical height from the top
    ysize 400        # Height of the title area

style game_menu_label_text:
    size 54
    color "#ffffff"
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True
       

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.3
                yalign 0.000002
                yoffset -20

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5
    yoffset -90

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")
    xpadding 15
    ypadding 15

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                # vbox:
                    # style_prefix "check"
                    # label _("Skip")
                    # textbutton _("Unseen Text") action Preference("skip", "toggle")
                    # textbutton _("After Choices") action Preference("after choices", "toggle")
                    # textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

## Gallery screen #######################################################
##
## Screen for ending CGs to be accessed after the player has seen them.
##

init python:

    # Step 1. Create the gallery object.
    g = Gallery()

    # Step 2. Add buttons and images to the gallery.
    g.button ("Lock")
    
    g.button("Main Menu")
    g.image("images/bg menu.png")

    g.button("Eugen")
    g.image("images/bg engineer.png")

    g.button("Sara")
    g.image("images/bg medic.jpg")
    
    g.button("MAD1")
    g.image("images/bg computer.png")

    g.button("Escape")
    g.image("images/bg escape pod.png")

    g.button("Specimen")
    g.condition("persistent.seenC2")
    g.image("images/bg artifact.png")
    g.image("images/bg artifact covered.png")
    g.condition("persistent.seenC2 and persistent.endSEC_unlocked")
    
    g.button("Captain Ending")
    g.image("images/End Screens/ending captain.png")
    g.condition("persistent.endC_unlocked or persistent.endB_unlocked")

    g.button("Eugen Ending")
    g.image("images/End Screens/ending engineer.png")
    g.condition("persistent.endE_unlocked")

    g.button("Sara Ending")
    g.image("images/End Screens/ending medic.png")
    g.condition("persistent.endS_unlocked")

    g.button("Good Ending")
    g.image("images/End Screens/ending crew stars.png")
    g.condition("persistent.endG_unlocked")

    g.button("Secret Ending1")
    g.image("images/End Screens/ending byebye fungus.png")
    g.condition("persistent.endSEC_unlocked")
    
    g.button("Secret Ending2")
    g.image("images/End Screens/secret ending.png")
    g.condition("persistent.endSEC_unlocked")

    # The transition used when switching images.
    g.transition = dissolve

    thumbnail_x = 455
    thumbnail_y = 261
    

# Step 3. The gallery screen we use.
screen gallery():

    # Ensure this replaces the main menu.
    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    # The background.
    add "gui/main_menu.png"
    add "gui/pause_overlay.png"

    default gallery_page = FilePage(1)

    fixed:
        use game_menu(_("Gallery")):

            # A grid of buttons.
            grid 3 2:
                style_prefix "gallery"

                xalign 0.5
                yalign 0.000002
                yoffset -20

                spacing gui.slot_spacing

                xfill True
                yfill True
                
                # if FilePage(1):
                #     # Call make_button to show a particular button.
                #     add g.make_button("Main Menu", im.Scale("images/bg menu.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5) 
                #     add g.make_button("Eugen", im.Scale("images/bg engineer.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5) 
                #     add g.make_button("Sara", im.Scale("images/bg medic.jpg", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5) 

                #     add g.make_button("MAD1", im.Scale("images/bg computer.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5) 
                #     add g.make_button("Escape", im.Scale("images/bg escape pod.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5) 
                #     if persistent.seenC2 == True:
                #         add g.make_button("Specimen", im.Scale("images/bg artifact.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5)
                #     else:
                #         add g.make_button("Lock", im.Scale("gui/Gallery Locked.png", 485, 291), xalign=0.5, yalign=0.5)

                # elif FilePage(2):
                # Captain End Screen
                if persistent.endB_unlocked == True or persistent.endC_unlocked == True:
                    add g.make_button("Captain Ending", im.Scale("images/End Screens/ending captain.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5) 
                else:
                    add g.make_button("Lock", im.Scale("gui/Gallery Locked.png", 485, 291), xalign=0.5, yalign=0.5)
                
                # Eugen End Screen
                if persistent.endE_unlocked == True:
                    add g.make_button("Eugen Ending", im.Scale("images/End Screens/ending engineer.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5) 
                else:
                    add g.make_button("Lock", im.Scale("gui/Gallery Locked.png", 485, 291), xalign=0.5, yalign=0.5)

                # Sara End Screen
                if persistent.endS_unlocked == True:
                    add g.make_button("Sara Ending", im.Scale("images/End Screens/ending medic.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5) 
                else:
                    add g.make_button("Lock", im.Scale("gui/Gallery Locked.png", 485, 291), xalign=0.5, yalign=0.5)

                # Good End Screen
                if persistent.endG_unlocked == True:
                    add g.make_button("Good Ending", im.Scale("images/End Screens/ending crew stars.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5) 
                else:
                    add g.make_button("Lock", im.Scale("gui/Gallery Locked.png", 485, 291), xalign=0.5, yalign=0.5)

                # Secrert End Screen
                if persistent.endSEC_unlocked == True:
                    add g.make_button("Secret Ending1", im.Scale("images/End Screens/ending byebye fungus.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5) 
                else:
                    add g.make_button("Lock", im.Scale("gui/Gallery Locked.png", 485, 291), xalign=0.5, yalign=0.5)

                # Secret End Screen
                if persistent.endSEC_unlocked == True:
                    add g.make_button("Secret Ending2", im.Scale("images/End Screens/secret ending.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5) 
                else:
                    add g.make_button("Lock", im.Scale("gui/Gallery Locked.png", 485, 291), xalign=0.5, yalign=0.5)

                # The screen is responsible for returning to the main menu. It could also
                # navigate to other gallery screens.
            # hbox:
            #     style_prefix "page"
            #     xalign 0.5
            #     yalign 1.0

            #     spacing gui.page_spacing
            #     textbutton _("<") action FilePagePrevious()
            #     key "save_page_prev" action FilePagePrevious()

            #     textbutton _("1") action FilePage(1)
            #     textbutton _("2") action FilePage(2)

            #     textbutton _(">") action FilePageNext()
            #     key "save_page_next" action FilePageNext()


style gallery_label is gui_label
style gallery_label_text is gui_label_text
style gallery_button is gui_button
style gallery_button_text is gui_button_text

style gallery_label:
    xpadding 75
    ypadding 5
    xalign 0.5
    yoffset -90

style gallery_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style gallery_button:
    properties gui.button_properties("gallery_button")
    xpadding 15
    ypadding 15
    background Frame(("gui/Gallery Unlock.png"), gui.slot_button_borders, tile=gui.frame_tile)

style gallery_button_text:
    properties gui.text_properties("gallery_button")

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    add "gui/help_page@2.08.jpg"    

    default device = "keyboard"

    # use game_menu(_("Information"), scroll="viewport"):

    style_prefix "help"

    vbox:
        xpos 700      
        ypos 280
        spacing 20
            
        if device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help

 
    vbox:
        xpos 250        # Far left of the screen
        ypos 280       # Use this to move them up or down
        spacing 25
        style_prefix "help"

        textbutton _("Keyboard"):
            style "help_side_button"
            action SetScreenVariable("device", "keyboard")
        textbutton _("Mouse"):
            style "help_side_button"
            action SetScreenVariable("device", "mouse")

    # 3. The Exit Button
    # Positioned at 1600 (far right) as per your previous code
    imagebutton:
        xpos 1595      # Change this to 80 if you want it on the left too
        ypos 120
        idle "gui/exit-button.png" 
        hover "gui/exit-button.png" 
        action Return()


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    # hbox:
    #     label _("Ctrl")
    #     text _("Skips dialogue while held down.")

    # hbox:
    #     label _("Tab")
    #     text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    # hbox:
    #     label "V"
    #     text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text
style help_content_frame is game_menu_content_frame

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 10

style help_label_text:
    size 25
    xalign 0.0
    textalign 1.0

style help_text:
    size 25
    xalign 0.0
    textalign 1.0

style help_content_frame:
    xfill True
    left_margin 10
    right_margin 30
    top_margin 15

style help_side_button:
    properties gui.button_properties("confirm_button")    

    activate_sound "audio/Button_Select.mp3"

    # 3. Center the button and its contents
    xalign 0.5
    
    hover_background Transform("gui/menu_item_highlight.png", xalign=0.5, yalign=0.5, zoom=0.70)
    selected_background Transform("gui/menu_item_highlight.png", xalign=0.5, yalign=0.5, zoom=0.70)

################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is navigation_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")    

    activate_sound "audio/Button_Select.mp3"

    # 3. Center the button and its contents
    xalign 0.5
    
    hover_background Transform("gui/button/BTN_Overlay_Highlight.png", xalign=0.5, yalign=0.5, zoom=0.70)

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    # background im.Alpha("gui/phone/nvl.png", 0.5)
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 5
    top_padding 5
    bottom_padding 5
    left_padding 20
    right_padding 20

style bubble_namebox:
    xalign 0.08
    yalign 0.17

style bubble_who:
    xalign 0.1
    textalign 0.5
    color "#fff"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#fff"

define bubble.frame = Frame("gui/bubble.png", 400, 600, 1120, 315)
define bubble.captain = Frame("gui/rudybubble.png", 400, 540, 1120, 495)
define bubble.computer = Frame("gui/computerbubble.png", 400, 540, 1120, 495)
define bubble.engineer = Frame("gui/eugenebubble.png", 400, 540, 1120, 495)
define bubble.medic = Frame("gui/sarabubble.png", 400, 540, 1120, 495)
define bubble.captainbreakdown = Frame("gui/rudythoughtbubble.png", 400, 540, 1120, 495)
define bubble.computersolution = Frame("gui/computer frame.png", 400, 540, 1120, 495)

define bubble.properties = {
    "captain" : {
        "window_background" : bubble.captain,
        "window_top_padding" : 10,
        "window_left_padding" : 25,
        "window_right_padding" : 20,
    },
    
    "computer" : {
        "window_background" : bubble.computer,
        "window_top_padding" : 10,
    },

    "engineer" : {
        "window_background" : bubble.engineer,
        "window_top_padding" : 10,
    },
    
    "medic" : {
        "window_background" : bubble.medic,
        "window_top_padding" : 10,
    },

    "captainbreakdown" : {
        "window_background" : bubble.captainbreakdown,
        "window_top_padding" : 10,
        "window_left_padding" : 25,
        "window_right_padding" : 20,
    },
    
    "computersolution" : {
        "window_background" : bubble.computersolution,
        "window_top_padding" : 10,
    },
}

define bubble.expand_area = {
    "thought" : (0, 0, 0, 0),
    "captain" : (0, 0, 0, 0),
    "computer" : (0, 0, 0, 0),    
    "engineer" : (0, 0, 0, 0),
    "medic" : (0, 0, 0, 0),
}


# Map 0 %99
screen MapUI0():
    tag map
    imagebutton:
        idle "map/bg spaceship.png"
        hover "map/bg spaceship.png"
        action NullAction()

    if seenSI is True or seenEI is True:
        imagebutton:
            xalign 1.0
            idle "oxygen/oxygen-meter-99.png"
            hover "oxygen/oxygen-meter-99.png"
            action NullAction()
    else:
        imagebutton:
            xalign 1.0
            idle "oxygen/oxygen-meter-90.png"
            hover "oxygen/oxygen-meter-90.png"
            action NullAction()
   
    # medic
    if seenSI is False:
        imagebutton:
            xpos 725
            ypos 422
            idle "map/medicidle.png"
            hover "map/medichover.png"
            activate_sound "audio/Button_Select.mp3"
            action Jump("SI")

    # engineer
    if seenEI is False:
        imagebutton:
            xpos 1080
            ypos 615
            idle "map/engineeridle.png"
            hover "map/engineerhover.png"
            activate_sound "audio/Button_Select.mp3"
            action Jump("EI")

# Map 1
screen MapUI1():
    tag map
    # background
    imagebutton:
        idle "map/bg spaceship.png"
        hover "map/bg spaceship.png"
        action NullAction()

    # oxygen at 80%
    imagebutton:
        xalign 1.0
        idle "oxygen/oxygen-meter-80.png"
        hover "oxygen/oxygen-meter-80.png"
        action NullAction()
        
    # medic
    imagebutton:
        xpos 725
        ypos 422
        idle "map/medicidle.png"
        hover "map/medichover.png"
        activate_sound "audio/Button_Select.mp3"
        action Jump("S1")
         
    # engineer
    imagebutton:
        xpos 1080
        ypos 615
        idle "map/engineeridle.png"
        hover "map/engineerhover.png"
        activate_sound "audio/Button_Select.mp3"
        action Jump("E1")
        
# Map 1b transition to C1
screen MapUIC1():
    tag map
    # background
    imagebutton:
        idle "map/bg spaceship.png"
        hover "map/bg spaceship.png"
        action NullAction()

    # oxygen at 65%
    imagebutton:
        xalign 1.0
        idle "oxygen/oxygen-meter-65.png"
        hover "oxygen/oxygen-meter-65.png"
        action NullAction()

    # escape
    imagebutton:
        xpos 1405
        ypos 513
        idle "map/escapeidle.png"
        hover "map/escapehover.png"
        action Jump("C1")


# Map 2
screen MapUI2():
    tag map
    # background
    imagebutton:
        idle "map/bg spaceship.png"
        hover "map/bg spaceship.png"
        action NullAction()

    # oxygen at 50% (if seen MO, 30%)
    if seenMO is True:
        imagebutton:
            idle "oxygen/oxygen-meter-30.png"
            hover "oxygen/oxygen-meter-30.png"
            action NullAction()
    else:
        imagebutton:
            xalign 1.0
            idle "oxygen/oxygen-meter-50.png"
            hover "oxygen/oxygen-meter-50.png"
            action NullAction()

    # medic
    imagebutton:
        xpos 725
        ypos 422
        idle "map/medicidle.png"
        hover "map/medichover.png"
        activate_sound "audio/Button_Select.mp3"
        action Jump("S2")

    # engineer
    imagebutton:
        xpos 1080
        ypos 615
        idle "map/engineeridle.png"
        hover "map/engineerhover.png"
        activate_sound "audio/Button_Select.mp3"
        action Jump("E2")

    # computer
    if seenMO is False:
        imagebutton:
            xpos 180
            ypos 480
            idle "map/computeridle.png"
            hover "map/computerhover.png"
            activate_sound "audio/Button_Select.mp3"
            action Jump("MO")

# Map 2b transition to C2
screen MapUIC2():
    tag map
    # background
    imagebutton:
        idle "map/bg spaceship.png"
        hover "map/bg spaceship.png"
        action NullAction()

    # oxygen at 20%
    imagebutton:
        xalign 1.0
        idle "oxygen/oxygen-meter-20.png"
        hover "oxygen/oxygen-meter-20.png"
        action NullAction()

    # storage
    imagebutton:
        xpos 1080
        ypos 268
        idle "map/storageidle.png"
        hover "map/storagehover.png"
        action Jump("C2")

# Map 3
screen MapUI3():
    tag map
    #background
    imagebutton:
        idle "map/bg spaceship.png"
        hover "map/bg spaceship.png"
        action NullAction()

    # oxygen at 10%
    imagebutton:
        xalign 1.0
        idle "oxygen/oxygen-meter-10.png"
        hover "oxygen/oxygen-meter-10.png"
        action NullAction()
        
    # medic
    if seenS3 is False:
        imagebutton:
            xpos 725
            ypos 422
            idle "map/medicidle.png"
            hover "map/medichover.png"
            activate_sound "audio/Button_Select.mp3"
            action Jump("S3")

    # engineer
    if seenE3 is False:
        imagebutton:
            xpos 1080
            ypos 615
            idle "map/engineeridle.png"
            hover "map/engineerhover.png"
            activate_sound "audio/Button_Select.mp3"
            action Jump("E3")

screen MapUIFin():
    tag map
    # background
    imagebutton:
        idle "map/bg spaceship.png"
        hover "map/bg spaceship.png"
        action NullAction()

    # oxygen at 10%
    imagebutton:
        xalign 1.0
        idle "oxygen/oxygen-meter-10.png"
        hover "oxygen/oxygen-meter-10.png"
        action NullAction()
        
    # storage
    if seenSaraSolution is False:
        imagebutton:
            xpos 1080
            ypos 268
            idle "map/storageidle.png"
            hover "map/storagehover.png"
            action Jump("SaraSolution")

    # computer
    if seenSaraSolution is True and seenEugenSolution is False:
        imagebutton:
            xpos 180
            ypos 480
            idle "map/computeridle.png"
            hover "map/computerhover.png"
            action Jump("EugenSolution")
    
screen MapUIEnd():
    tag map
    # background
    imagebutton:
        idle "map/bg spaceship.png"
        hover "map/bg spaceship.png"
        action NullAction()

    # oxygen
    imagebutton:
        xalign 1.0
        idle "oxygen/oxygen-meter-10.png"
        hover "oxygen/oxygen-meter-10.png"
        action NullAction()

    # escape pod
    imagebutton:
        xpos 1405
        ypos 513
        idle "map/escapeidle.png"
        hover "map/escapehover.png"
        action Jump("Choice")


# # MapUI base
# screen MapUI():
#     tag map
#    # background
#     imagebutton:
#         idle "map/bg spaceship.png"
#         hover "map/bg spaceship.png"
#         action NullAction()

#    # oxygen
#     imagebutton:
#         xalign 1.0
#         idle "oxygen/oxygen-meter-90.png"
#         hover "oxygen/oxygen-meter-90.png"
#         action NullAction()

#     # captain
#     imagebutton:
#         xpos 725
#         ypos 580
#         idle "map/captainidle.png"
#         hover "map/captainhover.png"
#         action NullAction()
        
#     # storage
#     imagebutton:
#         xpos 1080
#         ypos 268
#         idle "map/storageidle.png"
#         hover "map/storagehover.png"
#         action NullAction()

#     # escape
#     imagebutton:
#         xpos 1405
#         ypos 513
#         idle "map/escapeidle.png"
#         hover "map/escapehover.png"
#         action NullAction()

#     # medic
#     imagebutton:
#         xpos 725
#         ypos 422
#         idle "map/medicidle.png"
#         hover "map/medichover.png"
#         action NullAction()

#     # engineer
#     imagebutton:
#         xpos 1080
#         ypos 615
#         idle "map/engineeridle.png"
#         hover "map/engineerhover.png"
#         action NullAction()

#     # computer
#     imagebutton:
#         xpos 180
#         ypos 480
#         idle "map/computeridle.png"
#         hover "map/computerhover.png"
#         action NullAction()

screen EndCPoemA():
    
    style_prefix "credits"
    
    frame:
        xpos 75
        ypos 50
        vbox:
            style_prefix "poem"
            ypos 100
            xpos 225
            text """
            He rose the morrow morn.
            A sadder and a wiser man.
            He went like one that hath been stunned,
            And is of sense forlorn:
            The Captain, whose eye is dark,
            Whose beard with age is hoar
            Is gone.
            """

screen EndCPoemB():
    
    style_prefix "credits"
    
    frame:
        xpos 75
        ypos 50
        vbox:
            style_prefix "poem"
            ypos 100
            xpos 225
            text """
            He rose the morrow morn.
            A sadder and a wiser man.
            He went like one that hath been stunned,
            And is of sense forlorn:
            The Captain, whose eye is dark,
            Whose beard with age is hoar
            Is gone.
            """

        vbox:
            ypos 350
            xpos 15
            text """
            Captain’s log, January 27th.
            The specimen has safely returned with me to Earth.
            Further investigations will commence soon. 
            I think… I uh… I…
            I-I’ve failed…
            I’ve killed my crew members…
            What kind of Captain am I?                
            I’ve come home with the specimen… but at what cost..?
            I’m sorry, Sara…
            I’m sorry, Eugen…
            What have I done?
            """

screen EndEPoemA():
    style_prefix "credits"
    
    frame:
        xpos 75
        ypos 50
        
        vbox:
            style_prefix "poem"
            ypos 100
            xpos 225
            text """
            We are the hard-luck folk, who strove
            Zealously, but in vain;
            We lost and lost, while our comrades throve,
            And still we lost again.
            """

screen EndEPoemB():
    style_prefix "credits"
    
    frame:
        xpos 75
        ypos 50
        
        vbox:
            style_prefix "poem"
            ypos 100
            xpos 225
            text """
            We are the hard-luck folk, who strove
            Zealously, but in vain;
            We lost and lost, while our comrades throve,
            And still we lost again.
            """

        vbox:
            ypos 300
            xpos 15
            text """
            Eugen's Log:
            All has come to an end, and the mission is behind me.
            However, I can’t stop thinking if it was truly the best 
            outcome for me being saved.
            I accepted the mission to prove my drill; my design is 
            flawless; however, I left it behind.
            What does my future as an engineer entail? I will never be 
            rid of the memory of my failure, my design being lost in space.
            Getting in that return pod is just another addition to my 
            list of regrets.
            I hope Sara and Rudy can forgive me.
            """

screen EndSPoemA():

    style_prefix "credits"

    frame:
        xpos 75
        ypos 50
        vbox:
            style_prefix "poem"
            ypos 100
            xpos 250
            text """
            When I compare
            What I have lost with what I have gained,
            What I have missed with what attained,
            Little room do I find for pride
            """

screen EndSPoemB():

    style_prefix "credits"

    frame:
        xpos 75
        ypos 50
        vbox:
            style_prefix "poem"
            ypos 100
            xpos 250
            text """
            When I compare
            What I have lost with what I have gained,
            What I have missed with what attained,
            Little room do I find for pride
            """

        vbox:
            ypos 300
            xpos 15
            text """
            Sara's Log:
            I made it back...I still can’t believe it. 
            I found life out in space. I achieved my dream!
            My family? They’re proud of me, but they still can’t fully 
            accept my life. 
            It’s not what I expected… But it doesn’t matter anymore.
            Captain, you believed in me. You gave me what I craved 
            from my family all my life. And I left you to die in space.
            It’s hard to bear…I will keep going and do my best. 
            I owe that to you.
            """

screen EndGPoemA():
    
    style_prefix "credits"

    frame:
        xpos 75
        ypos 50
    
        vbox:
            style_prefix "poem"
            ypos 100
            xpos 75
            text """
            The ship is anchor’d safe and sound, its voyage closed and done,
            From fearful trip the victor ship comes in with object won.
            """

screen EndGPoemB():
    
    style_prefix "credits"

    frame:
        xpos 75
        ypos 50
    
        vbox:
            style_prefix "poem"
            ypos 100
            xpos 75
            text """
            The ship is anchor’d safe and sound, its voyage closed and done,
            From fearful trip the victor ship comes in with object won.
            """

        vbox:
            ypos 250
            xpos 15
            text """
            Captain’s log, January 27th. 
            A- a lot has happened since the last log.
            We’re all very shaken. But at least we’re home.
            Next log will be a recap of events.
            I… I did it Matthew…
            I did it for you.
            """

screen EndBPoemA():
    
    style_prefix "credits"
    
    frame:
        xpos 75
        ypos 50
        vbox:
            style_prefix "poem"
            ypos 100
            xpos 75
            text """
            Not every man knows what is waiting for him, or what he shall sing
            When the ship he is on slips into darkness, there at the end.
            """

screen EndBPoemB():
    
    style_prefix "credits"

    frame:
        xpos 75
        ypos 50
        vbox:
            style_prefix "poem"
            ypos 100
            xpos 75
            text """
            Not every man knows what is waiting for him, or what he shall sing
            When the ship he is on slips into darkness, there at the end.
            """

        vbox:
            ypos 250
            xpos 15
            text """
            Captain's Log:
            Matthew… We fai- I failed the mission… I failed you. 
            I told myself I would complete the mission whether 
            or not it kills me, and I guess part of me hoped 
            I would join you amongst the stars. 
            But I’m a coward… I failed the CSA, 
            I failed my crew, I failed you.
            What have I done?
            """


screen EndSECPoemA():
    
    style_prefix "credits"

    frame:
        xpos 75
        ypos 50
        vbox:
            style_prefix "poem"
            ypos 100
            xpos 225
            text """
            I love thee freely, as men strive for right.
            I love thee purely, as they turn from praise.
            I love thee with the passion put to use.
            """

screen EndSECPoemB():
    
    style_prefix "credits"

    frame:
        xpos 75
        ypos 50
        vbox:
            style_prefix "poem"
            ypos 100
            xpos 225
            text """
            I love thee freely, as men strive for right.
            I love thee purely, as they turn from praise.
            I love thee with the passion put to use.
            """

        vbox:
            ypos 250
            xpos 15
            text """
            Captain’s log, September 24th.
            The mission was unsuccessful. 
            The specimen has been discarded to save the ship.
            I- …
            I love you, Matthew.
            Goodbye, my love.
            """

screen TryAgain():
    vbox :
        style_prefix "tryagain"
        ypos 600
        xalign 0.5
        text """
        Death is nothing at all.
        I have only slipped away to the next room.
        Play, smile, think of me. Pray for me.
        I am but waiting for you.
        """

style poem_text:
    text_align 0.5
    size gui.poem_text_size

style tryagain_text:
    text_align 0.5
## Credits ######

screen Credits1():

    style_prefix "credits"
    frame:
        xpos 75
        ypos 50

        vbox:
            ypos 80
            xpos 80
            text """
            Created By
                Lindsay Buckingham & Mariya Mubeen

            Art Director
                Lindsay Buckingham

            Game Producer
                Mariya Mubeen

            
            Team Captains

                Art - Lindsay Buckingham
                Programming - Carine Ho
                Sound - Jason Byrne
                UI/UX - Karina Bittencourt
                Writing - Mariya Mubeen
                Voice - Feodor Romanenkov
            """

screen Credits2():
    
    style_prefix "credits"
    frame:
        xpos 75
        ypos 50

        vbox:
            ypos 80
            xpos 80
            text """
            Art

            Captain Rudy - Lindsay Buckingham
            MAD1 - Alex Kurina
            Cosmotechnician Eugen - Muhammad Nafeh Masood
            Astrobiologist Sara - Leah Tran
            Map and console design - Ling Yang


            Writing

            Captain Rudy - Feodor Romanenkov
            MAD1 - Carine Ho
            Cosmotechnician Eugen - Omar Shahin
            Astrobiologist Sara - Suprabha Irugalratne
            Final Editing - Mariya Mubeen
            """ 

screen Credits3():
    
    style_prefix "credits"
    frame:
        xpos 75
        ypos 50
        vbox:
            ypos 80
            xpos 80
            text """
            Programming

            Carine Ho
            Feodor Romanenkov
            Jason Byrne


            User Experience/Interface Design

            Karina Bittencourt
            Lucie Hunter
            Jamie Choi
            Ling Yang 
            

            Game Design

            Mariya Mubeen 
            Omar Shahin
            """ 

screen Credits4():
    
    style_prefix "credits"
    frame:
        xpos 75
        ypos 50
        vbox:
            ypos 80
            xpos 80
            text """
            Sound Design

            Jason Byrne
            Feodor Romanenkov


            Voice Talent

            Performance Director - Feodor Romanenkov

            Captain Rudy - Feodor Romanenkov
            MAD1 - Carine Ho
            Cosmotechnician Eugen - Jason Byrne
            Astrobiologist Sara - Mariya Mubeen
            """ 

screen Credits5():

    style_prefix "credits"
    frame:
        xpos 75
        ypos 50
        vbox:
            ypos 80
            xpos 80
            text """
            Special Thanks To

            Dr. Kristopher Alexander
            Maeve Fitzgerald
            TMU Sound Library

            """

style credits_frame:
    background Frame("gui/credit frame.png", gui.credit_frame_borders)
    xysize (1182, 982)


################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    # background im.Alpha("gui/phone/nvl.png", 0.5)

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"
    

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
