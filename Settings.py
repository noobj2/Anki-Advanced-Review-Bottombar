#// auth_ Mohamad Janati
#// Copyright (c) 2019-2023 Mohamad Janati

from os.path import join, dirname
from datetime import datetime
import webbrowser
from aqt import mw
from aqt.qt import *
from aqt.utils import tooltip, showInfo, askUser, getText
from anki.utils import is_lin, is_mac, is_win
import random
import os
import json
import subprocess


def refreshConfig():
    #// Makes the information that it gets from "config" global, so I can use them for loading the current settings in "loadCurrent(self)" function
    global C_style_mainScreenButtons, C_button_style, C_hover_effect, C_active_indicator, C_bottombarButtons_style, C_cursor_style, C_interval_style, C_showAnswerBorderColor_style, C_buttonTransition_time, C_buttonBorderRadius, C_wideButton_percent, C_reviewTooltip, C_reviewTooltip_timer, C_reviewTooltipText_color, C_reviewTooltip_style, C_reviewTooltip_position, C_reviewTooltip_offset, C_info, C_skip, C_showSkipped, C_undo, C_hideHard, C_hideGood, C_hideEasy, C_right_info, C_middleRight_info, C_middleLeft_info, C_left_info, C_right_skip, C_middleRight_skip, C_middleLeft_skip, C_left_skip, C_right_showSkipped, C_middleRight_showSkipped, C_middleLeft_showSkipped, C_left_showSkipped, C_right_undo, C_middleRight_undo, C_middleLeft_undo, C_left_undo, C_skip_shortcut, C_showSkipped_shortcut, C_info_shortcut, C_undo_shortcut, C_custom_sizes, C_text_size, C_buttonFontWeight, C_buttons_height, C_reviewButtons_width, C_edit_width, C_answer_width, C_more_width, C_info_width, C_skip_width, C_showSkipped_width, C_undo_width, C_buttonLabel_studyNow, C_buttonLabel_edit, C_buttonLabel_showAnswer, C_buttonLabel_more, C_buttonLabel_info, C_buttonLabel_skip, C_buttonLabel_showSkipped, C_buttonLabel_undo, C_buttonLabel_again, C_buttonLabel_hard, C_buttonLabel_good, C_buttonLabel_easy, C_sidebar_theme, C_sidebar_font, C_sidebar_hideCurrentCard, C_sidebar_PreviousCards, C_sidebar_reviewsToShow, C_sidebar_currentReviewCount, C_sidebar_reviewsToShow, C_sidebar_dateCreated, C_sidebar_dateEdited, C_sidebar_firstReview, C_sidebar_latestReview, C_sidebar_due, C_sidebar_interval, C_sidebar_ease, C_sidebar_numberOfReviews, C_sidebar_lapses, C_infobar_correctPercent, C_infobar_fastestReview, C_infobar_slowestReview, C_sidebar_averageTime, C_sidebar_totalTime, C_sidebar_cardType, C_sidebar_noteType, C_sidebar_deck, C_sidebar_tags, C_infobar_noteID, C_infobar_cardID, C_sidebar_sortField, C_sidebar_autoOpen, C_sidebar_warningNote, C_custom_reviewButtonColors, C_custom_reviewButtonTextColor, C_custom_activeIndicatorColor, C_custom_bottombarButtonTextColor, C_custom_bottombarButtonBorderColor, C_reviewButtonText_color, C_activeIndicator_color, C_bottombarButtonText_color, C_bottombarButtonBorder_color, C_again_color, C_againHover_color, C_hard_color, C_hardHover_color, C_good_color, C_goodHover_color, C_easy_color, C_easyHover_color, C_button_colors, C_showAnswerEase1, C_showAnswerEase2, C_showAnswerEase3, C_showAnswerEase4, C_showAnswerEase1_color, C_showAnswerEase2_color, C_showAnswerEase3_color, C_showAnswerEase4_color, C_addOn_speedFocus, C_addOn_rebuildEmptyAll, C_configEdit, C_hideEasyIfNotLearning, C_overViewStats, C_settingsMenu_palce, C_skipMethod

    config = mw.addonManager.getConfig(__name__)

    #// Gets the information from the config and assigns them to the "C_" variables, so I can make them global | "C_" is added to the name of the parts of the settings variables to avoid confusion :D
    #// Just delete the "C_" from the name to find related parts of the settings (C_style_mainScreenButtons -> style_mainScreenButtons)
    C_style_mainScreenButtons = config['  Style Main Screen Buttons']

    C_button_style = config[' Review_ Buttons Style']
    C_hover_effect = config[' Review_ Hover Effect']
    C_active_indicator = config[' Review_ Active Button Indicator']
    C_bottombarButtons_style = config[' Review_ Bottombar Buttons Style']
    C_cursor_style = config[' Review_ Cursor Style']
    C_interval_style = config[' Review_ Interval Style']
    C_buttonTransition_time = config[' Review_ Button Transition Time']
    # Button Border Radius is used for all buttons, not just the review buttons
    C_buttonBorderRadius = config[' Review_ Button Border Radius']
    C_wideButton_percent = config[' Review_ Wide Button Percent']

    C_reviewTooltip = config['Tooltip']
    C_reviewTooltip_timer = config['Tooltip Timer']
    C_reviewTooltipText_color = config['Tooltip Text Color']
    C_reviewTooltip_style = config['Tooltip Style']
    C_reviewTooltip_position = config['Tooltip Position']
    C_reviewTooltip_offset = config['Tooltip Offset']

    C_info = config['Button_   Info Button']
    C_skip = config['Button_   Skip Button']
    C_showSkipped = config['Button_   Show Skipped Button']
    C_undo = config['Button_   Undo Button']
    C_hideHard = config['Button_   Hide Hard']
    C_hideGood = config['Button_   Hide Good']
    C_hideEasy = config['Button_   Hide Easy']
    C_info_position = config['Button_ Position_ Info Button']
    C_skip_position = config['Button_ Position_ Skip Button']
    C_showSkipped_position = config['Button_ Position_ Show Skipped Button']
    C_undo_position = config['Button_ Position_ Undo Button']
    C_skip_shortcut = config ['Button_ Shortcut_ Skip Button']
    C_showSkipped_shortcut = config ['Button_ Shortcut_ Show Skipped Button']
    C_info_shortcut = config['Button_ Shortcut_ Info Button']
    C_undo_shortcut = config['Button_ Shortcut_ Undo Button']

    C_custom_sizes = config ['Button_  Custom Button Sizes']
    C_text_size = config['Button_ Text Size']
    C_buttonFontWeight = config['Button_ Font Weight']
    C_buttons_height = config['Button_ Height_ All Bottombar Buttons']
    C_reviewButtons_width = config['Button_ Width_ Review Buttons']
    C_edit_width = config['Button_ Width_ Edit Button']
    C_answer_width = config['Button_ Width_ Show Answer Button']
    C_more_width = config['Button_ Width_ More Button']
    C_info_width = config['Button_ Width_ Info Button']
    C_skip_width = config['Button_ Width_ Skip Button']
    C_showSkipped_width = config['Button_ Width_ Show Skipped Button']
    C_undo_width = config['Button_ Width_ Undo Button']

    C_buttonLabel_studyNow = config['Button Label_ Study Now']
    C_buttonLabel_edit = config['Button Label_ Edit']
    C_buttonLabel_showAnswer = config['Button Label_ Show Answer']
    C_buttonLabel_more = config['Button Label_ More']
    C_buttonLabel_info = config['Button Label_ Info']
    C_buttonLabel_skip = config['Button Label_ Skip']
    C_buttonLabel_showSkipped = config['Button Label_ Show Skipped']
    C_buttonLabel_undo = config['Button Label_ Undo']
    C_buttonLabel_again = config['Button Label_ Again']
    C_buttonLabel_hard = config['Button Label_ Hard']
    C_buttonLabel_good = config['Button Label_ Good']
    C_buttonLabel_easy = config['Button Label_ Easy']

    C_sidebar_theme = config['Card Info sidebar_ theme']
    C_sidebar_font = config['Card Info sidebar_ Font']
    C_sidebar_hideCurrentCard = config['Card Info sidebar_ Hide Current Card']
    C_sidebar_PreviousCards = config['Card Info sidebar_ Number of previous cards to show']
    C_sidebar_reviewsToShow = config['Card Info sidebar_ number of reviews to show for a card']
    C_sidebar_currentReviewCount = config['Card Info sidebar_ Current Review Count']
    C_sidebar_dateCreated = config['Card Info sidebar_ Created']
    C_sidebar_dateEdited = config['Card Info sidebar_ Edited']
    C_sidebar_firstReview = config['Card Info sidebar_ First Review']
    C_sidebar_latestReview = config['Card Info sidebar_ Latest Review']
    C_sidebar_due = config['Card Info sidebar_ Due']
    C_sidebar_interval = config['Card Info sidebar_ Interval']
    C_sidebar_ease = config['Card Info sidebar_ Ease']
    C_sidebar_numberOfReviews = config['Card Info sidebar_ Reviews']
    C_sidebar_lapses = config['Card Info sidebar_ Lapses']
    C_infobar_correctPercent = config['Card Info Sidebar_ Correct Percent']
    C_infobar_fastestReview = config['Card Info Sidebar_ Fastest Review']
    C_infobar_slowestReview = config['Card Info Sidebar_ Slowest Review']
    C_sidebar_averageTime = config['Card Info sidebar_ Average Time']
    C_sidebar_totalTime = config['Card Info sidebar_ Total Time']
    C_sidebar_cardType = config['Card Info sidebar_ Card Type']
    C_sidebar_noteType = config['Card Info sidebar_ Note Type']
    C_sidebar_deck = config['Card Info sidebar_ Deck']
    C_sidebar_tags = config['Card Info sidebar_ Tags']
    C_infobar_noteID = config['Card Info Sidebar_ Note ID']
    C_infobar_cardID = config['Card Info Sidebar_ Card ID']
    C_sidebar_sortField = config['Card Info sidebar_ Sort Field']
    C_sidebar_autoOpen = config['Card Info sidebar_ Auto Open']
    C_sidebar_warningNote = config['Card Info sidebar_ warning note']

    C_custom_reviewButtonColors = config[' Review_ Custom Colors']
    C_custom_reviewButtonTextColor = config[' Review_ Custom Review Button Text Color']
    C_custom_activeIndicatorColor = config[' Review_ Custom Active Indicator Color']
    C_custom_bottombarButtonTextColor = config['Color_ Custom Bottombar Button Text Color']
    C_custom_bottombarButtonBorderColor = config['Color_ Custom Bottombar Button Border Color']
    C_reviewButtonText_color = config['Color_  General Text Color']
    C_activeIndicator_color = config['Color_ Active Button Indicator']
    C_bottombarButtonText_color = config['Color_ Bottombar Button Text Color']
    C_bottombarButtonBorder_color = config['Color_ Bottombar Button Border Color']
    C_again_color = config['Color_ Again']
    C_againHover_color = config['Color_ Again on hover']
    C_hard_color = config['Color_ Hard']
    C_hardHover_color = config['Color_ Hard on hover']
    C_good_color = config['Color_ Good']
    C_goodHover_color = config['Color_ Good on hover']
    C_easy_color = config['Color_ Easy']
    C_easyHover_color = config['Color_ Easy on hover']

    C_showAnswerBorderColor_style = config['ShowAnswer_ Border Color Style']
    C_showAnswerEase1 = config['ShowAnswer_ Ease1']
    C_showAnswerEase2 = config['ShowAnswer_ Ease2']
    C_showAnswerEase3 = config['ShowAnswer_ Ease3']
    C_showAnswerEase4 = config['ShowAnswer_ Ease4']
    C_showAnswerEase1_color = config['ShowAnswer_ Ease1 Color']
    C_showAnswerEase2_color = config['ShowAnswer_ Ease2 Color']
    C_showAnswerEase3_color = config['ShowAnswer_ Ease3 Color']
    C_showAnswerEase4_color = config['ShowAnswer_ Ease4 Color']

    C_button_colors = config['  Button Colors']
    C_configEdit = config['  Direct Config Edit']
    C_hideEasyIfNotLearning = config['  Hide Easy if not in Learning']
    C_overViewStats = config['  More Overview Stats']
    C_settingsMenu_palce = config['  Settings Menu Place']
    C_skipMethod = config['  Skip Method']

    C_addOn_speedFocus = config['  Speed Focus Add-on']
    C_addOn_rebuildEmptyAll = config['  Rebuild Empty All Add-on']

    #// it's easier to store extra button positions as text in config | but here in the settings, I hate to turn it into true/false as each checkbox is disabled/enabled like that :|
    #// Every checkbox is disabled by default
    C_right_info = False
    C_middleRight_info = False
    C_middleLeft_info = False
    C_left_info = False
    C_right_skip = False
    C_middleRight_skip = False
    C_middleLeft_skip = False
    C_left_showSkipped = False
    C_right_showSkipped = False
    C_middleRight_showSkipped = False
    C_middleLeft_showSkipped = False
    C_left_showSkipped = False
    C_right_undo = False
    C_middleRight_undo = False
    C_middleLeft_undo = False
    C_left_undo = False

    #// here we enable (make it "True") the correct checkbox based on the config value
    #// All of this is for loading the current settings in "loadCurrent(self)" function
    if C_info_position == "right":
        C_right_info = True
    elif C_info_position == "middle right":
        C_middleRight_info = True
    elif C_info_position == "middle left":
        C_middleLeft_info = True
    else:
        C_left_info = True
    if C_skip_position == "right":
        C_right_skip = True
    elif C_skip_position == "middle right":
        C_middleRight_skip = True
    elif C_skip_position == "middle left":
        C_middleLeft_skip = True
    else:
        C_left_skip = True
    if C_showSkipped_position == "right":
        C_right_showSkipped = True
    elif C_showSkipped_position == "middle right":
        C_middleRight_showSkipped = True
    elif C_showSkipped_position == "middle left":
        C_middleLeft_showSkipped = True
    else:
        C_left_showSkipped = True
    if C_undo_position == "right":
        C_right_undo = True
    elif C_undo_position == "middle right":
        C_middleRight_undo = True
    elif C_undo_position == "middle left":
        C_middleLeft_undo = True
    else:
        C_left_undo = True

class GetShortcut(QDialog):
    def __init__(self, parent, button_variable):
        QDialog.__init__(self, parent=parent)
        self.parent = parent
        self.button_variable = button_variable
        #// when recording a shortcut, there is 0 active (pushed) key at first | by pressing each key, this increases by +1
        self.active = 0
        #// and the state of all the accepted keys on the keyboard is "False" | by pressing each key, the state for that button changes to "True"
        self.ctrl = False
        self.alt = False
        self.shift = False
        self.f1 = False
        self.f2 = False
        self.f3 = False
        self.f4 = False
        self.f5 = False
        self.f3 = False
        self.f6 = False
        self.f7 = False
        self.f8 = False
        self.f9 = False
        self.f10 = False
        self.f11 = False
        self.f12 = False
        self.extra = None
        self.getShortcutWindow()

    def getShortcutWindow(self):
        #// Sets up the screen that asks you to press the shortcut you want to assign
        text = QLabel('<div style="font-size: 15px">Press the new shortcut key...</div>')
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(text)
        self.setLayout(mainLayout)
        self.setWindowTitle('Set Shortcut')

    def keyPressEvent(self, evt):
        #// increases the active keys count upon pressing each key
        self.active += 1
        #// limits the allowed keys to keyboard keys
        if evt.key() > 30 and evt.key() < 127:
            self.extra = chr(evt.key())
        #// stores the pressed key in a variable, so we could later add it in a list and use it as a key combination
        elif evt.key() == Qt.Key.Key_Control:
            self.ctrl = True
        elif evt.key() == Qt.Key.Key_Alt:
            self.alt = True
        elif evt.key() == Qt.Key.Key_Shift:
            self.shift = True
        elif evt.key() == Qt.Key.Key_F1:
            self.f1 = True
        elif evt.key() == Qt.Key.Key_F2:
            self.f2 = True
        elif evt.key() == Qt.Key.Key_F3:
            self.f3 = True
        elif evt.key() == Qt.Key.Key_F4:
            self.f4 = True
        elif evt.key() == Qt.Key.Key_F5:
            self.f5 = True
        elif evt.key() == Qt.Key.Key_F6:
            self.f6 = True
        elif evt.key() == Qt.Key.Key_F7:
            self.f7 = True
        elif evt.key() == Qt.Key.Key_F8:
            self.f8 = True
        elif evt.key() == Qt.Key.Key_F9:
            self.f9 = True
        elif evt.key() == Qt.Key.Key_F10:
            self.f10 = True
        elif evt.key() == Qt.Key.Key_F11:
            self.f11 = True
        elif evt.key() == Qt.Key.Key_F12:
            self.f12 = True

    def keyReleaseEvent(self, evt):
        #// reduces the number of held keys upon releasing each key
        self.active -= 1
        message = "You can't set \"{}\" as a shortcut!"
        if is_mac:
            altMessage = message.format("Option")
            ctrlMessage = message.format("Command")
        else:
            altMessage = message.format("Alt")
            ctrlMessage = message.format("Ctrl")
        if not (self.f1 or self.f2 or self.f3 or self.f4 or self.f5 or self.f6 or self.f7 or self.f8 or self.f9 or self.f10 or self.f11 or self.f12):
            if not self.extra:
                #// lets the users that the pressed key is not allowed to be used in a shortcut
                if self.alt:
                    showInfo(f"{altMessage}".format(), title="Advanced Review Bottombar")
                elif self.shift:
                    showInfo(message.format("Shift"), title="Advanced Review Bottombar")
                elif self.ctrl:
                    showInfo(f"{ctrlMessage}".format(), title="Advanced Review Bottombar")
                elif evt.key() == Qt.Key_Escape:
                    showInfo(message.format("Esc"), title="Advanced Review Bottombar")
                elif evt.key() == Qt.Key_Tab:
                    showInfo(message.format("Tab"), title="Advanced Review Bottombar")
                elif evt.key() == Qt.Key_Backspace:
                    showInfo(message.format("Backspace"), title="Advanced Review Bottombar")
                elif evt.key() == Qt.Key_Enter:
                    showInfo(message.format("Esc"), title="Advanced Review Bottombar")
                elif evt.key() == Qt.Key_Return:
                    showInfo(message.format("Enter"), title="Advanced Review Bottombar")
                elif evt.key() == Qt.Key_Insert:
                    showInfo(message.format("Insert"), title="Advanced Review Bottombar")
                elif evt.key() == Qt.Key_Delete:
                    showInfo(message.format("Delete"), title="Advanced Review Bottombar")
                elif evt.key() == Qt.Key_Pause:
                    showInfo(message.format("Pause/Break"), title="Advanced Review Bottombar")
                elif evt.key() == Qt.Key_Home:
                    showInfo(message.format("Home Key"), title="Advanced Review Bottombar")
                elif evt.key() == Qt.Key_Left:
                    showInfo(message.format("Left"), title="Advanced Review Bottombar")
                elif evt.key() == Qt.Key_Up:
                    showInfo(message.format("Up"), title="Advanced Review Bottombar")
                elif evt.key() == Qt.Key_Right:
                    showInfo(message.format("Right"), title="Advanced Review Bottombar")
                elif evt.key() == Qt.Key_Down:
                    showInfo(message.format("Down"), title="Advanced Review Bottombar")
                elif evt.key() == Qt.Key_PageUp:
                    showInfo(message.format("Page Up"), title="Advanced Review Bottombar")
                elif evt.key() == Qt.Key_PageDown:
                    showInfo(message.format("Page DOwn"), title="Advanced Review Bottombar")
                elif evt.key() == Qt.Key_CapsLock:
                    showInfo(message.format("CAPS Lock"), title="Advanced Review Bottombar")
                elif evt.key() == Qt.Key_NumLock:
                    showInfo(message.format("Num Lock"), title="Advanced Review Bottombar")
                else:
                    showInfo("You can't use that as shortcut, try something else.", title="Advanced Review Bottombar")
                self.alt = False
                self.shift = False
                self.ctrl = False
                self.extra = None
                self.active = 0
                evt = False
                combination = []
                return

        #// the (empty) list for storing keys and then turning them into a shortcut
        combination = []
        if self.ctrl:
            combination.append("Ctrl")
        if self.shift:
            combination.append("Shift")
        if self.alt:
            combination.append("Alt")
        if self.f1:
            combination.append("F1")
        if self.f2:
            combination.append("F2")
        if self.f3:
            combination.append("F3")
        if self.f4:
            combination.append("F4")
        if self.f5:
            combination.append("F5")
        if self.f6:
            combination.append("F6")
        if self.f7:
            combination.append("F7")
        if self.f8:
            combination.append("F8")
        if self.f9:
            combination.append("F9")
        if self.f10:
            combination.append("F10")
        if self.f11:
            combination.append("F11")
        if self.f12:
            combination.append("F12")
        if self.extra:
            combination.append(self.extra)
        combination = "+".join(combination)
        #// preventing users from assigning a default Anki shortcut to something else | to avoid conflicts and stuff :|
        if combination in ["E", " ", "F5", "Ctrl+1", "Ctrl+2", "Ctrl+3", "Ctrl+4", "Shift+*", "=", "-", "Shift+!", "Shift+@", "Ctrl+Delete", "V", "Shift+V", "O", "1", "2", "3", "4", "5", "6", "7", "T", "Y", "A", "S", "D", "F", "B", "I", "/", "F1", "Ctrl+Q", "Ctrl+E", "Ctrl+P", "Ctrl+Shift+I", "Ctrl+Shift+P", "Ctrl+Shift+A", "Ctrl+Shift+:", "Ctrl+Shift+N"]:
            if combination == "E":
                showInfo("\"E\" is default Anki shortcut for \"Edit Current Card\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == " ":
                showInfo("\"Space Bar\" is default Anki shortcut for \"Show Answer\" or \"Default Review Button\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "F5":
                showInfo("\"F5\" is default Anki shortcut for \"Replay Audio\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Ctrl+1":
                showInfo("\"Ctrl+1\" is default Anki shortcut for \"Set Red Flag\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Ctrl+2":
                showInfo("\"Ctrl+2\" is default Anki shortcut for \"Set Orange Flag\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Ctrl+3":
                showInfo("\"Ctrl+3\" is default Anki shortcut for \"Set Green Flag\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Ctrl+4":
                showInfo("\"Ctrl+4\" is default Anki shortcut for \"Set Blue Flag\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Shift+*":
                showInfo("\"*\" is default Anki shortcut for \"Mark Current Card\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "=":
                showInfo("\"=\" is default Anki shortcut for \"Bury Note\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "-":
                showInfo("\"-\" is default Anki shortcut for \"Bury Current Card\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Shift+!":
                showInfo("\"!\" is default Anki shortcut for \"Suspend Note\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Shift+@":
                showInfo("\"@\" is default Anki shortcut for \"Suspend Current Card\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Ctrl+Delete":
                showInfo("\"Ctrl+Delete\" is default Anki shortcut for \"Delete Note\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "V":
                showInfo("\"V\" is default Anki shortcut for \"Replay Audio\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Shift+V":
                showInfo("\"Shift+V\" is default Anki shortcut for \"Record Voice\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "O":
                showInfo("\"O\" is default Anki shortcut for \"Options\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "1":
                showInfo("\"1\" is default Anki shortcut for \"Answer with ease 1 (Again)\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "2":
                showInfo("\"2\" is default Anki shortcut for \"Answer with ease 2 (usually Hard)\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "3":
                showInfo("\"3\" is default Anki shortcut for \"Answer with ease 3 (usually Good)\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "4":
                showInfo("\"4\" is default Anki shortcut for \"Answer with ease 4 (Easy)\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "5":
                showInfo("\"5\" is default Anki shortcut for \"Pause Audio\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "6":
                showInfo("\"6\" is default Anki shortcut for \"Seek Backward\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "7":
                showInfo("\"7\" is default Anki shortcut for \"Seek Forward\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "T":
                showInfo("\"T\" is default Anki shortcut for \"Stats\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Y":
                showInfo("\"Y\" is default Anki shortcut for \"Sync\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "A":
                showInfo("\"A\" is default Anki shortcut for \"Add Cards\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "S":
                showInfo("\"S\" is default Anki shortcut for \"Toggle Study Current Deck\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "D":
                showInfo("\"D\" is default Anki shortcut for \"Decks View\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "F":
                showInfo("\"F\" is default Anki shortcut for \"Create Filtered Deck\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "B":
                showInfo("\"B\" is default Anki shortcut for \"Browse\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "I":
                showInfo("\"I\" is default Anki shortcut for \"Card Info Window\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "/":
                showInfo("\"/\" is default Anki shortcut for \"Study Deck\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "F1":
                showInfo("\"F1\" is default Anki shortcut for \"Open Guide (Anki Manual)\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Ctrl+Q":
                showInfo("\"Ctrl+Q\" is default Anki shortcut for \"Exit\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Ctrl+E":
                showInfo("\"Ctrl+E\" is default Anki shortcut for \"Export\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Ctrl+P":
                showInfo("\"Ctrl+P\" is default Anki shortcut for \"Preferences\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Ctrl+Shift+I":
                showInfo("\"Ctrl+Shift+I\" is default Anki shortcut for \"Import\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Ctrl+Shift+P":
                showInfo("\"Ctrl+Shift+P\" is default Anki shortcut for \"Switch Profile\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Ctrl+Shift+A":
                showInfo("\"Ctrl+Shift+A\" is default Anki shortcut for \"Add-ons\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Ctrl+Shift+:":
                showInfo("\"Ctrl+Shift+:\" is default Anki shortcut for \"Debug Console\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Ctrl+Shift+N":
                showInfo("\"Ctrl+Shift+N\" is default Anki shortcut for \"Manage Note Types\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            if combination == "Ctrl+Shift+Z":
                showInfo("\"Ctrl+Shift+Z\" is default Anki shortcut for \"Undo\" You can't use this shortcut.", type="warning", title="Advanced Review Bottombar")
            self.ctrl = False
            self.alt = False
            self.shift = False
            self.extra = None
            self.f1 = False
            self.f5 = False
            self.active = 0
            combination = []
            return
        elif combination == "Ctrl+Z":
            combination = "NOT_SET"
        self.parent.updateShortcut(self.button_variable, combination)
        self.close()

class SettingsMenu(QDialog):
    refreshConfig()
    addon_path = dirname(__file__)
    images = join(addon_path, 'images')
    begin = "<div style='font-size: 14px'>"
    end = "</div>"
    info_shortcut = C_info_shortcut
    skip_shortcut = C_skip_shortcut
    showSkipped_shortcut = C_showSkipped_shortcut
    undo_shortcut = C_undo_shortcut
    def __init__(self, parent=None):
        super(SettingsMenu, self).__init__(parent)
        self.mainWindow()
        self.reviewButtonText_color = C_reviewButtonText_color
        self.activeIndicator_color = C_activeIndicator_color
        self.bottombarButtonText_color = C_bottombarButtonText_color
        self.bottombarButtonBorder_color = C_bottombarButtonBorder_color
        self.reviewTooltipText_color = C_reviewTooltipText_color
        self.again_color = C_again_color
        self.againHover_color = C_againHover_color
        self.hard_color = C_hard_color
        self.hardHover_color = C_hardHover_color
        self.good_color = C_good_color
        self.goodHover_color = C_goodHover_color
        self.easy_color = C_easy_color
        self.easyHover_color = C_easyHover_color
        self.showAnswerEase1_color = C_showAnswerEase1_color
        self.showAnswerEase2_color = C_showAnswerEase2_color
        self.showAnswerEase3_color = C_showAnswerEase3_color
        self.showAnswerEase4_color = C_showAnswerEase4_color
    def mainWindow(self):
        images = self.images
        self.createFirstTab()
        self.createSecondTab()
        self.createThirdTab()
        self.createFourthTab()
        self.createFifthTab()
        self.createSixthTab()
        self.createSeventhTab()
        self.createEighthTab()
        self.createNinthTab()
        self.loadCurrent()

        #// Create the bottom row of settings menu
        loadSettingsButton = QPushButton("&Load Settings")
        loadSettingsButton.clicked.connect(self.onLoadSettings)
        saveSettingsButton = QPushButton("&Backup Settings")
        saveSettingsButton.clicked.connect(self.onSaveSettings)
        acceptButton = QPushButton("&Apply")
        acceptButton.clicked.connect(self.onApply)
        rejectButton = QPushButton("&Discard")
        rejectButton.clicked.connect(self.reject)
        rejectButton.clicked.connect(lambda: tooltip("Changes Discarded."))
        buttonbox = QHBoxLayout()
        buttonbox.addWidget(loadSettingsButton)
        buttonbox.addWidget(saveSettingsButton)
        buttonbox.addStretch()
        buttonbox.addWidget(acceptButton)
        buttonbox.addWidget(rejectButton)
        supportMe_button = QPushButton("❤️ Support Me")
        supportMe_button.clicked.connect(lambda: webbrowser.open('https://www.buymeacoffee.com/noobj2'))
        support_box = QHBoxLayout()
        support_box.addWidget(supportMe_button)

        #// create tabs widget and adds each tab
        tabs = QTabWidget()
        tabs.addTab(self.tab1, "Styles")
        tabs.addTab(self.tab2, "Answer Tooltip")
        tabs.addTab(self.tab3, "Bottombar Buttons")
        tabs.addTab(self.tab4, "Button Sizes")
        tabs.addTab(self.tab5, "Button Labels")
        tabs.addTab(self.tab6, "Sidebar")
        tabs.addTab(self.tab7, "Colors")
        tabs.addTab(self.tab8, "Misc")
        tabs.addTab(self.tab9, "About")

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        vbox.addLayout(buttonbox)
        vbox.addLayout(support_box)

        self.setLayout(vbox)
        self.setWindowTitle("Advanced Review Bottombar Settings Menu")
        self.setWindowIcon(QIcon(images + "/icon.png"))

    def createFirstTab(self):
        begin = self.begin
        end = self.end
        images = self.images
        buttonStyle_label = QLabel("Button Style:")
        buttonStyle_label.setToolTip("{0} Changes the way review buttons look.{1}".format(begin, end))
        buttonStyle_label.setFixedWidth(180)
        self.button_style = QComboBox()
        self.button_style.addItems(["Default + Text Color", "Default + Background Color", "Wide + Text Color", "Wide + Background Color", "Neon 1", "Neon 2", "Fill 1", "Fill 2"])
        self.button_style.setToolTip("{0}To see designs please go to about tab.{1}".format(begin, end))
        self.button_style.setFixedWidth(180)
        reviewButtonDesigns_button = QPushButton("Show Designs")
        reviewButtonDesigns_button.setFixedWidth(180)
        reviewButtonDesigns_text = "{0}Default + Text Color <br> <img src='{2}/buttonStyle_defaultText.png'><hr> Default\
        + Background Color<br> <img src='{2}/buttonStyle_defaultBackground.png'><hr>\
        Wide + Text Color<br> <img src='{2}/buttonStyle_wideText.png'><hr>Wide +\
        Background Color<br> <img src='{2}/buttonStyle_wideBackground.png'><hr>Neon1 (Easy is hovered over)<br>\
        <img src='{2}/buttonStyle_neon1.png'><hr>Neon2 (Easy is hovered over)<br>\
        <img src='{2}/buttonStyle_neon2.png'><hr> Fill1 (Easy is hovered over)<br><img src='{2}/buttonStyle_fill1.png'><hr>\
        Fill2 (Easy is hovered over)<br><img src='{2}/buttonStyle_fill2.png'>{1}".format(begin, end, images)
        reviewButton_designs = QLabel()
        reviewButton_designs.setText(reviewButtonDesigns_text)
        reviewButtonDesigns_scroll = QScrollArea()
        reviewButtonDesigns_scroll.setWidget(reviewButton_designs)
        reviewButtonDesigns_layout = QVBoxLayout()
        reviewButtonDesigns_layout.addWidget(reviewButtonDesigns_scroll)
        reviewButtonDesigns_window = QDialog()
        reviewButtonDesigns_window.setWindowTitle("Advanced Review Bottombar [Review Button Designs]")
        reviewButtonDesigns_window.setWindowIcon(QIcon(images + "/icon.png"))
        reviewButtonDesigns_window.setLayout(reviewButtonDesigns_layout)
        reviewButtonDesigns_button.clicked.connect(lambda: reviewButtonDesigns_window.exec())
        buttonStyle_holder = QHBoxLayout()
        buttonStyle_holder.addWidget(buttonStyle_label)
        buttonStyle_holder.addWidget(self.button_style)
        buttonStyle_holder.addWidget(reviewButtonDesigns_button)
        buttonStyle_holder.addStretch()
        bottombaButtonsStyle_label = QLabel("General Buttons Style:")
        bottombaButtonsStyle_label.setToolTip("{0} Changes The way general buttons (main screen bottombar, deck overview, show answer, edit, etc.) look. {1}".format(begin, end))
        bottombaButtonsStyle_label.setFixedWidth(180)
        self.bottombarButtons_style = QComboBox()
        self.bottombarButtons_style.addItems(["Default", "Neon 1", "Neon 2", "Fill1", "Fill 2"])
        self.bottombarButtons_style.setToolTip("{0}To see what every design looks like, please go to about tab{1}".format(begin, end))
        self.bottombarButtons_style.setMinimumWidth(180)
        otherBottombarButtonDesigns_button = QPushButton("Show Designs")
        otherBottombarButtonDesigns_button.setFixedWidth(180)
        otherBottombarButtonDesigns_text = "{0} Default<br><img src='{2}/bottombarButtonsStyle_default.png'><hr>\
        Neon1 (Show answer is hovered over)<br> <img src='{2}/bottombarButtonsStyle_neon1.png'>\
        <hr>Neon2 (Show answer is hovered over)<br> <img src='{2}/bottombarButtonsStyle_neon2.png'><hr>Fill1 (Show answer is hovered over)<br>\
        <img src='{2}/bottombarButtonsStyle_fill1.png'><hr>Fill2 (Show answer is hovered over)<br>\
        <img src='{2}/bottombarButtonsStyle_fill2.png'>{1}".format(begin, end, images)
        otherBottombarButton_designs = QLabel()
        otherBottombarButton_designs.setText(otherBottombarButtonDesigns_text)
        otherBottombarButtonDesigns_scroll = QScrollArea()
        otherBottombarButtonDesigns_scroll.setWidget(otherBottombarButton_designs)
        otherBottombarButtonDesigns_layout = QVBoxLayout()
        otherBottombarButtonDesigns_layout.addWidget(otherBottombarButtonDesigns_scroll)
        otherBottombarButtonDesigns_window = QDialog()
        otherBottombarButtonDesigns_window.setWindowTitle("Advanced Review Bottombar [Other Bottombar Buttons Designs]")
        otherBottombarButtonDesigns_window.setWindowIcon(QIcon(images + "/icon.png"))
        otherBottombarButtonDesigns_window.setLayout(otherBottombarButtonDesigns_layout)
        otherBottombarButtonDesigns_button.clicked.connect(lambda: otherBottombarButtonDesigns_window.exec())
        bottombarButtonsStyle_holder = QHBoxLayout()
        bottombarButtonsStyle_holder.addWidget(bottombaButtonsStyle_label)
        bottombarButtonsStyle_holder.addWidget(self.bottombarButtons_style)
        bottombarButtonsStyle_holder.addWidget(otherBottombarButtonDesigns_button)
        bottombarButtonsStyle_holder.addStretch()
        hoverEffect_label = QLabel("Hover Effect:")
        hoverEffect_label.setToolTip("{0} Changes the way review buttons look when you hover over them.\
        <hr> This option does not change hover effect for neon buttons.<hr> If you use\
        custom colors for review buttons, brighten and glow colors will be the color\
        you have set for each buttons hover color.{1}".format(begin, end))
        hoverEffect_label.setFixedWidth(180)
        self.hover_effect = QComboBox()
        self.hover_effect.addItems(["Disable", "Brighten", "Glow", "Brighten + Glow"])
        self.hover_effect.setToolTip("{0} Disable -> Buttons won't change as you hover\
        over them.<hr> Brighten -> The text or the background color will get brightened\
        as you hover over them.<br><img src='{2}/hoverEffect_brighten.png'><hr> Glow ->\
        There will be a shadow around the button as you hover them.<br><img src='{2}/hoverEffect_glow.png'><hr>\
        Glow + Brighten -> Combines both glow and brighten effects.<br> <img src='{2}/hoverEffect_glowBrighten.png'>{1}".format(begin, end, images))
        self.hover_effect.setMinimumWidth(180)
        hoverEffect_holder = QHBoxLayout()
        hoverEffect_holder.addWidget(hoverEffect_label)
        hoverEffect_holder.addWidget(self.hover_effect)
        hoverEffect_holder.addStretch()
        activeIndicator_label = QLabel("Active Indicator:")
        activeIndicator_label.setToolTip("{0} Changes the way active review button looks. active button\
        is the button that is clicked if you press spacebar or enter.<hr> This option can not change active\
        indicator for neon and fill buttons as it's disabled on those designs. {1}".format(begin, end))
        activeIndicator_label.setFixedWidth(180)
        self.active_indicator = QComboBox()
        self.active_indicator.addItems(["Disable", "Border", "Glow"])
        self.active_indicator.setToolTip("{0} Indicator is turned off and all review buttons are the\
        same.<br> {1} <img src='{2}/activeIndicator_none.png'>{0}<hr> Indicator is\
        set on border and there is a thin border around active button.<br>\
        {1} <img src='{2}/activeIndicator_border.png'>{0}<hr> Indicator is set on\
        glow and active button is glowing. <br> {1}\
        <img src='{2}/activeIndicator_glow.png'>".format(begin, end, images))
        self.active_indicator.setMinimumWidth(180)
        activeIndicator_holder = QHBoxLayout()
        activeIndicator_holder.addWidget(activeIndicator_label)
        activeIndicator_holder.addWidget(self.active_indicator)
        activeIndicator_holder.addStretch()
        cursorStyle_label = QLabel("Cursor Style:")
        cursorStyle_label.setToolTip("{0}Changes the cursor style when hovered over buttons.{1}".format(begin, end))
        cursorStyle_label.setFixedWidth(180)
        self.cursor_style = QComboBox()
        self.cursor_style.addItems(["Normal", "Pointer"])
        self.cursor_style.setFixedWidth(180)
        cursorStyle_holder = QHBoxLayout()
        cursorStyle_holder.addWidget(cursorStyle_label)
        cursorStyle_holder.addWidget(self.cursor_style)
        cursorStyle_holder.addStretch()
        showAnswerBorderType_label = QLabel("Show Answer Border Color Style:")
        showAnswerBorderType_label.setToolTip("{0}Changes how show answer border color behaves.<hr>\
        if set on \"Fixed\" it's border color will be the same as other bottombar buttons.<br>\
        if set on \"Bases on Card Ease\" it's color will change based on card ease.\
        <hr> you can change it's color for each ease range in colors tab.{1}".format(begin, end))
        showAnswerBorderType_label.setFixedWidth(180)
        self.showAnswerBorderColor_style = QComboBox()
        self.showAnswerBorderColor_style.addItems(["Fixed", "Show Based on Card Ease"])
        self.showAnswerBorderColor_style.setFixedWidth(180)
        showAnswerBorderType_holder = QHBoxLayout()
        showAnswerBorderType_holder.addWidget(showAnswerBorderType_label)
        showAnswerBorderType_holder.addWidget(self.showAnswerBorderColor_style)
        showAnswerBorderType_holder.addStretch()            
        intervalStyle_label = QLabel("Button Interval Style:")
        intervalStyle_label.setToolTip("{0}Changes the style of button intervals.{1}".format(begin, end))
        intervalStyle_label.setFixedWidth(180)
        self.interval_style = QComboBox()
        self.interval_style.addItems(["Stock", "Colored Stock", "Inside the Buttons"])
        self.interval_style.setFixedWidth(180)
        if not mw.col.conf["estTimes"]:
            self.interval_style.setDisabled(True)
            intervalStyle_label.setToolTip("{0}To enable this option you need to enable \"Show next review time above answer buttons\" in \"Tools > Preferences > Review\".{1}".format(begin, end))
        intervalStyle_holder = QHBoxLayout()
        intervalStyle_holder.addWidget(intervalStyle_label)
        intervalStyle_holder.addWidget(self.interval_style)
        intervalStyle_holder.addStretch()
        buttonFontWeight_label = QLabel("Button Font Weight:")
        buttonFontWeight_label.setToolTip("{0}Change font weight for the buttons.{1}".format(begin, end))
        buttonFontWeight_label.setFixedWidth(180)
        self.buttonFontWeight = QComboBox()
        self.buttonFontWeight.addItems(["Thin", "Extra Light", "Light", "Normal", "Medium", "Semi Bold", "Bold", "Extra Bold", "Black"])
        self.buttonFontWeight.setFixedWidth(180)
        buttonFontWeight_holder = QHBoxLayout()
        buttonFontWeight_holder.addWidget(buttonFontWeight_label)
        buttonFontWeight_holder.addWidget(self.buttonFontWeight)
        buttonFontWeight_holder.addStretch()
        buttonTransitionTime_label = QLabel("Button Transition Time:")
        buttonTransitionTime_label.setToolTip("{0}Changes button animation time for fill and neon styles.{1}".format(begin, end))
        buttonTransitionTime_label.setFixedWidth(180)
        self.buttonTransition_time = QSpinBox()
        self.buttonTransition_time.setMinimum(0)
        self.buttonTransition_time.setMaximum(10000)
        self.buttonTransition_time.setSingleStep(20)
        self.buttonTransition_time.setFixedWidth(180)
        buttonTransitionTime_ms = QLabel("ms")
        buttonTransitionTime_holder = QHBoxLayout()
        buttonTransitionTime_holder.addWidget(buttonTransitionTime_label)
        buttonTransitionTime_holder.addWidget(self.buttonTransition_time)
        buttonTransitionTime_holder.addWidget(buttonTransitionTime_ms)
        buttonTransitionTime_holder.addStretch()
        buttonBorderRadius_label = QLabel("Button Border Radius:")
        buttonBorderRadius_label.setToolTip("{0}Changer the roundness of the buttons.{1}".format(begin, end))
        buttonBorderRadius_label.setFixedWidth(180)
        self.buttonBorderRadius = QSpinBox()
        self.buttonBorderRadius.setMinimum(0)
        self.buttonBorderRadius.setMaximum(100)
        self.buttonBorderRadius.setSingleStep(1)
        self.buttonBorderRadius.setFixedWidth(180)
        buttonBorderRadius_px = QLabel("px")
        buttonBorderRadius_holder = QHBoxLayout()
        buttonBorderRadius_holder.addWidget(buttonBorderRadius_label)
        buttonBorderRadius_holder.addWidget(self.buttonBorderRadius)
        buttonBorderRadius_holder.addWidget(buttonBorderRadius_px)
        wideButtonPercent_label = QLabel("Wide Review Buttons Percent:")
        wideButtonPercent_label.setToolTip("{0}Changes the percent of the empty bottombar that's occupied by\
        the review buttons to change the spacing between the review buttons and the other bottombar buttons for wide buttons.{1}".format(begin, end))
        wideButtonPercent_label.setFixedWidth(180)
        self.wideButtonPercent = QSpinBox()
        self.wideButtonPercent.setMinimum(0)
        self.wideButtonPercent.setMaximum(100)
        self.wideButtonPercent.setSingleStep(1)
        self.wideButtonPercent.setFixedWidth(180)
        wideButtonPercent_sign = QLabel("%")
        wideButtonPercent_holder = QHBoxLayout()
        wideButtonPercent_holder.addWidget(wideButtonPercent_label)
        wideButtonPercent_holder.addWidget(self.wideButtonPercent)
        wideButtonPercent_holder.addWidget(wideButtonPercent_sign)
        def buttonStyle_signal():
            buttonStyle_index = self.button_style.currentIndex()
            self.hover_effect.setDisabled(True)
            if buttonStyle_index in [0, 1, 2, 3]:
                self.hover_effect.setEnabled(True)
            self.active_indicator.setDisabled(True)
            if buttonStyle_index in [0, 1, 2, 3]:
                self.active_indicator.setEnabled(True)
            # self.cursor_style.setDisabled(True)
            self.buttonTransition_time.setDisabled(True)
            if buttonStyle_index in [4, 5, 6, 7]:
                # self.cursor_style.setEnabled(True)
                self.buttonTransition_time.setEnabled(True)
            self.wideButtonPercent.setDisabled(True)
            if buttonStyle_index in [2, 3]:
                self.wideButtonPercent.setEnabled(True)
        buttonStyle_signal()
        self.button_style.currentIndexChanged.connect(buttonStyle_signal)
        self.style_mainScreenButtons = QCheckBox("Style Main Screen Buttons")
        self.style_mainScreenButtons.setToolTip("{0}Changes style of main screen and deck overview buttons if enabled.<hr>\
        <img src='{2}/changeMainScreenButtons.png'><br>\
        <img src='{2}/changeMainScreenButtons2.png'><br>\
        <img src='{2}/changeMainScreenButtons3.png'>{1}".format(begin, end, images))
        self.style_mainScreenButtons.setFixedWidth(180)
        tab1line5 = QHBoxLayout()
        tab1line5.addWidget(self.style_mainScreenButtons)
        tab1line5.addStretch()
        layout = QVBoxLayout()
        layout.addLayout(buttonStyle_holder)
        layout.addLayout(bottombarButtonsStyle_holder)
        layout.addLayout(hoverEffect_holder)
        layout.addLayout(activeIndicator_holder)
        layout.addLayout(cursorStyle_holder)
        layout.addLayout(showAnswerBorderType_holder)
        layout.addLayout(intervalStyle_holder)
        layout.addLayout(buttonFontWeight_holder)
        layout.addLayout(buttonTransitionTime_holder)
        layout.addLayout(buttonBorderRadius_holder)
        layout.addLayout(wideButtonPercent_holder)
        layout.addLayout(tab1line5)
        layout.addStretch()
        layout_holder = QWidget()
        layout_holder.setLayout(layout)
        self.tab1 = QScrollArea()
        self.tab1.setFixedWidth(690)
        self.tab1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.tab1.setWidgetResizable(True)
        self.tab1.setWidget(layout_holder)

    def createSecondTab(self):
        begin = self.begin
        end = self.end
        images = self.images

        # start 1 box
        reviewTooltip_label = QLabel("Review Confirmation Tooltip:")
        reviewTooltip_label.setToolTip("{0}Shows a tooltip when you press any of\
        review buttons, showing you what button you have pressed.{1}".format(begin, end))
        reviewTooltip_label.setFixedWidth(180)
        self.reviewTooltip_on = QRadioButton("On")
        self.reviewTooltip_on.setFixedWidth(90)
        self.reviewTooltip_off = QRadioButton("off")
        self.reviewTooltip_off.setFixedWidth(90)
        reviewTooltip_holder = QHBoxLayout()
        reviewTooltip_holder.addWidget(reviewTooltip_label)
        reviewTooltip_holder.addWidget(self.reviewTooltip_on)
        reviewTooltip_holder.addWidget(self.reviewTooltip_off)
        reviewTooltip_holder.addStretch()
        tab2box1 = QGroupBox()
        tab2box1.setLayout(reviewTooltip_holder)
        # end 1 box

        # start 2 box
        reviewTooltipStyle_label = QLabel("Tooltip Position:")
        reviewTooltipStyle_label.setToolTip("{0}Changes the position of answer tooltip.{1}".format(begin, end))
        reviewTooltipStyle_label.setFixedWidth(180)
        self.reviewTooltip_style = QComboBox()
        self.reviewTooltip_style.addItems(["On Buttons", "Fixed Position"])
        self.reviewTooltip_style.setToolTip("{0}On buttons -> Shows the tooltip on the button that you have pressed<hr>\
        Fixed Position -> Shows all the tooltips in a position that you have chosen in review tooltip position box.{1}".format(begin, end))
        self.reviewTooltip_style.setFixedWidth(180)
        reviewTooltipStyle_holder = QHBoxLayout()
        reviewTooltipStyle_holder.addWidget(reviewTooltipStyle_label)
        reviewTooltipStyle_holder.addWidget(self.reviewTooltip_style)
        reviewTooltipStyle_holder.addStretch()

        reviewTooltipTimer_label = QLabel("Tooltip Show Duration:")
        reviewTooltipTimer_label.setToolTip("{0}Changes length of the period that tooltip is shown.<hr>the unit is millisecond, 1000ms = 1s{1} (I know everybody knows this, put it here just in case :|)".format(begin, end))
        reviewTooltipTimer_label.setFixedWidth(180)
        self.reviewTooltip_timer = QSpinBox()
        self.reviewTooltip_timer.setFixedWidth(180)
        self.reviewTooltip_timer.setMinimum(100)
        self.reviewTooltip_timer.setMaximum(10000)
        reviewerTooltipTimer_ms = QLabel("ms")
        reviewTooltipTimer_holder = QHBoxLayout()
        reviewTooltipTimer_holder.addWidget(reviewTooltipTimer_label)
        reviewTooltipTimer_holder.addWidget(self.reviewTooltip_timer)
        reviewTooltipTimer_holder.addWidget(reviewerTooltipTimer_ms)
        reviewTooltipTimer_holder.addStretch()

        reviewTooltipTextColor_label = QLabel("Tooltip Text Color:")
        reviewTooltipTextColor_label.setToolTip("{0}Changes color of the text inside tooltips.{1}".format(begin, end))
        reviewTooltipTextColor_label.setFixedWidth(180)
        self.reviewTooltipTextColor_button = QPushButton()
        self.reviewTooltipTextColor_button.setFixedWidth(180)
        self.reviewTooltipTextColor_button.clicked.connect(lambda: self.getNewColor("reviewTooltipText_color", self.reviewTooltipTextColor_button))
        reviewTooltipTextColor_holder = QHBoxLayout()
        reviewTooltipTextColor_holder.addWidget(reviewTooltipTextColor_label)
        reviewTooltipTextColor_holder.addWidget(self.reviewTooltipTextColor_button)
        reviewTooltipTextColor_holder.addStretch()

        tab2line2 = QVBoxLayout()
        tab2line2.addLayout(reviewTooltipStyle_holder)
        tab2line2.addLayout(reviewTooltipTimer_holder)
        tab2line2.addLayout(reviewTooltipTextColor_holder)
        tab2box2 = QGroupBox()
        tab2box2.setLayout(tab2line2)
        # end 2 box

        # start 3 box
        self.reviewTooltipPositionX = QSlider(Qt.Orientation.Horizontal)
        self.reviewTooltipPositionX.setFixedWidth(200)
        self.reviewTooltipPositionX.setMinimum(0)
        self.reviewTooltipPositionX.setMaximum(1850)
        self.reviewTooltipPositionX.setPageStep(100)
        self.reviewTooltipPositionX.setSliderPosition(0)
        reviewerTooltipPosition_holder = QHBoxLayout()
        self.reviewTooltipPositionY = QSlider(Qt.Orientation.Vertical)
        self.reviewTooltipPositionY.setFixedHeight(200)
        self.reviewTooltipPositionY.setMinimum(-950)
        self.reviewTooltipPositionY.setMaximum(0)
        self.reviewTooltipPositionY.setPageStep(100)
        self.reviewTooltipPositionY.setSliderPosition(0)
        reviewerTooltipPosition_holder = QHBoxLayout()
        reviewerTooltipPosition_holder.addWidget(self.reviewTooltipPositionX)
        reviewerTooltipPosition_holder.addWidget(self.reviewTooltipPositionY)
        reviewerTooltipPosition_holder.addStretch()

        tab2line3 = QVBoxLayout()
        tab2line3.addLayout(reviewerTooltipPosition_holder)
        tab2box3 = QGroupBox("Tooltip Position (Fixed Position)")
        tab2box3.setToolTip("{0}Changes position of the fixed tooltip.<hr>\
        <font color=red># NOTE:</font> If your resulotion is not 1920 x 1080, it's not accurate, but you\
        can find the place that you wanna put the tooltip on, by toying with the sliders\
        and restarting anki till you get the desired result.<br>\
        <font color=red># NOTE:</font> If your resolution is 1920 x 1080 the sliders are accurate for\
        maximized anki window.<br> <font color=red># NOTE:</font> If you set the position for a window that\
        it's size is for example 500 x 500, the position will not be accurate when you\
        change anki's window size to any other size. and if you decide to resize anki's\
        window, you should set the positions again in order for the tooltip to be in the\
        position you want.{1}".format(begin, end))
        tab2box3.setLayout(tab2line3)
        tab2box3.setEnabled(True)
        self.reviewTooltip_off.toggled.connect(tab2box3.setDisabled)
        tab2box2.setDisabled(True)
        if self.reviewTooltip_on.isChecked():
            tab2box2.setEnabled(True)
        self.reviewTooltip_on.toggled.connect(tab2box2.setEnabled)
        # end 3 box

        # start 4 box
        self.reviewTooltipOffsetX = QSlider(Qt.Orientation.Horizontal)
        self.reviewTooltipOffsetX.setFixedWidth(200)
        self.reviewTooltipOffsetX.setMinimum(-800)
        self.reviewTooltipOffsetX.setMaximum(800)
        self.reviewTooltipOffsetX.setPageStep(100)
        self.reviewTooltipOffsetX.setSliderPosition(0)
        reviewerTooltipOffset_holder = QHBoxLayout()

        self.reviewTooltipOffsetY = QSlider(Qt.Orientation.Vertical)
        self.reviewTooltipOffsetY.setFixedHeight(200)
        self.reviewTooltipOffsetY.setMinimum(0)
        self.reviewTooltipOffsetY.setMaximum(500)
        self.reviewTooltipOffsetY.setPageStep(100)
        self.reviewTooltipOffsetY.setSliderPosition(0)
        reviewerTooltipOffset_holder = QHBoxLayout()

        reviewerTooltipOffset_holder.addWidget(self.reviewTooltipOffsetX)
        reviewerTooltipOffset_holder.addWidget(self.reviewTooltipOffsetY)
        reviewerTooltipOffset_holder.addStretch()

        tab2line4 = QVBoxLayout()
        tab2line4.addLayout(reviewerTooltipOffset_holder)
        tab2box4 = QGroupBox("Tooltip Position (On Buttons)")
        tab2box4.setToolTip("{0}Change the offset according to the button..<hr>\
        <font color=red># NOTE:</font> The centre of the x-axis is the zero point, moving to the left is \
        offset to the left according to the button and moving to the right is offset to \
        the right according to the button.{1}".format(begin, end))
        tab2box4.setLayout(tab2line4)
        tab2box4.setEnabled(True)
        self.reviewTooltip_off.toggled.connect(tab2box4.setDisabled)
        tab2box2.setDisabled(True)
        if self.reviewTooltip_on.isChecked():
            tab2box2.setEnabled(True)
        self.reviewTooltip_on.toggled.connect(tab2box2.setEnabled)
        # end 4 box

        layout = QVBoxLayout()
        layout.addWidget(tab2box1)
        layout.addWidget(tab2box2)
        layout.addWidget(tab2box3)
        layout.addWidget(tab2box4)
        layout.addStretch()
        layout_holder = QWidget()
        layout_holder.setLayout(layout)
        self.tab2 = QScrollArea()
        self.tab2.setFixedWidth(690)
        self.tab2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.tab2.setWidgetResizable(True)
        self.tab2.setWidget(layout_holder)

    def createThirdTab(self):
        begin = self.begin
        end = self.end
        images = self.images
        self.info = QCheckBox("Info")
        self.info.setToolTip("{0} If enabled adds info button to review bottombar. {1}".format(begin, end))
        self.skip = QCheckBox("Skip")
        self.skip.setToolTip("{0} If enabled adds skip card button to review bottombar. {1}".format(begin, end))
        self.showSkipped = QCheckBox("Show Skipped")
        self.showSkipped.setToolTip("{0} If enabled adds show skipped button to review bottombar. {1}".format(begin, end))
        self.undo = QCheckBox("Undo")
        self.undo.setToolTip("{0} If enabled adds undo review button to review bottombar. {1}".format(begin, end))
        extraButtonsPart = QHBoxLayout()
        extraButtonsPart.addWidget(self.info)
        extraButtonsPart.addWidget(self.skip)
        extraButtonsPart.addWidget(self.showSkipped)
        extraButtonsPart.addWidget(self.undo)
        extraButtonsBox = QGroupBox("Extra Buttons")
        extraButtonsBox.setLayout(extraButtonsPart)
        self.hideHard = QCheckBox("Hide Hard")
        self.hideHard.setToolTip("{0}Hides the Hard button.{1}".format(begin, end))
        self.hideGood = QCheckBox("Hide Good")
        self.hideGood.setToolTip("{0}Hides the Good button.{1}".format(begin, end))
        self.hideEasy = QCheckBox("Hide Easy")
        self.hideEasy.setToolTip("{0}Hides the Easy button.{1}".format(begin, end))
        hideButtonsPart = QHBoxLayout()
        hideButtonsPart.addWidget(self.hideHard)
        hideButtonsPart.addWidget(self.hideGood)
        hideButtonsPart.addWidget(self.hideEasy)
        hideButtonsPart.addWidget(QLabel(""))
        hideButtonsBox = QGroupBox("Hide Buttons")
        hideButtonsBox.setLayout(hideButtonsPart)
        infoPosition_label = QLabel("Info:")
        infoPosition_label.setToolTip("{0} Changes info button position in bottombar. {1}".format(begin, end))
        self.left_info = QRadioButton("Left")
        self.middleLeft_info = QRadioButton("Middle left")
        self.middleRight_info = QRadioButton("Middle right")
        self.right_info = QRadioButton("Right")
        infoPosition_holder = QHBoxLayout()
        infoPosition_holder.addWidget(infoPosition_label)
        infoPosition_holder.addWidget(self.left_info)
        infoPosition_holder.addWidget(self.middleLeft_info)
        infoPosition_holder.addWidget(self.middleRight_info)
        infoPosition_holder.addWidget(self.right_info)
        infoButtonPositionBox = QGroupBox()
        infoButtonPositionBox.setDisabled(True)
        if self.info.isChecked():
            self.infoButtonPositionBox.setEnabled(True)
        self.info.toggled.connect(infoButtonPositionBox.setEnabled)
        infoButtonPositionBox.setLayout(infoPosition_holder)
        skipPosition_label = QLabel("Skip:")
        skipPosition_label.setToolTip("{0} Changes skip button position in bottombar. {1}".format(begin, end))
        self.left_skip = QRadioButton("Left")
        self.middleLeft_skip = QRadioButton("Middle left")
        self.middleRight_skip = QRadioButton("Middle right")
        self.right_skip = QRadioButton("Right")
        skipPosition_holder = QHBoxLayout()
        skipPosition_holder.addWidget(skipPosition_label)
        skipPosition_holder.addWidget(self.left_skip)
        skipPosition_holder.addWidget(self.middleLeft_skip)
        skipPosition_holder.addWidget(self.middleRight_skip)
        skipPosition_holder.addWidget(self.right_skip)
        skipButtonPositionBox = QGroupBox()
        skipButtonPositionBox.setDisabled(True)
        if self.skip.isChecked():
            skipButtonPositionBox.setEnabled(True)
        self.skip.toggled.connect(skipButtonPositionBox.setEnabled)
        skipButtonPositionBox.setLayout(skipPosition_holder)
        showSkippedPosition_label = QLabel("Show Skipped:")
        showSkippedPosition_label.setToolTip("{0} Changes show skipped button position in bottombar. {1}".format(begin, end))
        self.left_showSkipped = QRadioButton("Left")
        self.middleLeft_showSkipped = QRadioButton("Middle left")
        self.middleRight_showSkipped = QRadioButton("Middle right")
        self.right_showSkipped = QRadioButton("Right")
        showSkippedPosition_holder = QHBoxLayout()
        showSkippedPosition_holder.addWidget(showSkippedPosition_label)
        showSkippedPosition_holder.addWidget(self.left_showSkipped)
        showSkippedPosition_holder.addWidget(self.middleLeft_showSkipped)
        showSkippedPosition_holder.addWidget(self.middleRight_showSkipped)
        showSkippedPosition_holder.addWidget(self.right_showSkipped)
        showSkippedButtonPositionBox = QGroupBox()
        showSkippedButtonPositionBox.setDisabled(True)
        if self.showSkipped.isChecked():
            showSkippedButtonPositionBox.setEnabled(True)
        self.showSkipped.toggled.connect(showSkippedButtonPositionBox.setEnabled)
        showSkippedButtonPositionBox.setLayout(showSkippedPosition_holder)
        undoPosition_label = QLabel("Undo:")
        undoPosition_label.setToolTip("{0} Changes undo review button position in bottombar. {1}".format(begin, end))
        self.left_undo = QRadioButton("Left")
        self.middleLeft_undo = QRadioButton("Middle left")
        self.middleRight_undo = QRadioButton("Middle right")
        self.right_undo = QRadioButton("Right")
        undoPosition_holder = QHBoxLayout()
        undoPosition_holder.addWidget(undoPosition_label)
        undoPosition_holder.addWidget(self.left_undo)
        undoPosition_holder.addWidget(self.middleLeft_undo)
        undoPosition_holder.addWidget(self.middleRight_undo)
        undoPosition_holder.addWidget(self.right_undo)
        undoButtonPositionBox = QGroupBox()
        undoButtonPositionBox.setDisabled(True)
        if self.undo.isChecked():
            undoButtonPositionBox.setEnabled(True)
        self.undo.toggled.connect(undoButtonPositionBox.setEnabled)
        undoButtonPositionBox.setLayout(undoPosition_holder)
        buttonPositionsPart = QVBoxLayout()
        buttonPositionsPart.addWidget(infoButtonPositionBox)
        buttonPositionsPart.addWidget(skipButtonPositionBox)
        buttonPositionsPart.addWidget(showSkippedButtonPositionBox)
        buttonPositionsPart.addWidget(undoButtonPositionBox)
        buttonPositionsBox = QGroupBox("Button Positions")
        buttonPositionsBox.setLayout(buttonPositionsPart)
        infoShortcut_label = QLabel("Info:")
        infoShortcut_label.setToolTip("{0} Changes show card info shortcut.<hr> Shortcut will work even if\
        you disable the Info button.<hr> Info button can be a single key\
        like \"i\" or \"f4\" or a combination of keys like \"ctrl+i\" or \"alt+i\".<hr>\
        <font color=red>NOTE: </font>Make sure the shortcut you want to set for the\
        button isn't already in use by anki itself or another add-on. {1}".format(begin, end))
        infoShortcut_label.setFixedWidth(125)
        self.infoShortcut_button = QPushButton(self)
        self.infoShortcut_button.setFixedWidth(300)
        self.infoShortcut_button.clicked.connect(lambda: self.showGetShortcut("info_shortcut"))
        infoShortcut_holder = QHBoxLayout()
        infoShortcut_holder.addWidget(infoShortcut_label)
        infoShortcut_holder.addStretch()
        infoShortcut_holder.addWidget(self.infoShortcut_button)
        skipShortcut_label = QLabel("Skip:")
        skipShortcut_label.setToolTip("{0} Changes skip card shortcut.<hr> Shortcut will work even if\
        you disable the skip button.<hr> skip button can be a single key\
        like \"s\" or \"f6\" or a combination of keys like \"ctrl+s\" or \"alt+s\".<hr>\
        <font color=red>NOTE: </font>Make sure the shortcut you want to set for the\
        button isn't already in use by anki itself or another add-on. {1}".format(begin, end))
        skipShortcut_label.setFixedWidth(125)
        self.skipShortcut_button = QPushButton()
        self.skipShortcut_button.setFixedWidth(300)
        self.skipShortcut_button.clicked.connect(lambda: self.showGetShortcut("skip_shortcut"))
        skipShortcut_holder = QHBoxLayout()
        skipShortcut_holder.addWidget(skipShortcut_label)
        skipShortcut_holder.addStretch()
        skipShortcut_holder.addWidget(self.skipShortcut_button)
        showSkippedShortcut_label = QLabel("Show Skipped:")
        showSkippedShortcut_label.setToolTip("{0} Changes Show Skipped cards shortcut.<hr> Shortcut will work even if\
        you disable the Show Skipped Cards button.<hr> Show Skipped cards button shortcut can be a single key\
        like \"s\" or \"f6\" or a combination of keys like \"ctrl+s\" or \"alt+s\".<hr>\
        <font color=red>NOTE: </font>Make sure the shortcut you want to set for the\
        button isn't already in use by anki itself or another add-on. {1}".format(begin, end))
        showSkippedShortcut_label.setFixedWidth(125)
        self.showSkippedShortcut_button = QPushButton()
        self.showSkippedShortcut_button.setFixedWidth(300)
        self.showSkippedShortcut_button.clicked.connect(lambda: self.showGetShortcut("showSkipped_shortcut"))
        showSkippedShortcut_holder = QHBoxLayout()
        showSkippedShortcut_holder.addWidget(showSkippedShortcut_label)
        showSkippedShortcut_holder.addStretch()
        showSkippedShortcut_holder.addWidget(self.showSkippedShortcut_button)
        undoShortcut_label = QLabel("Undo:")
        undoShortcut_label.setToolTip("{0} Changes undo review shortcut.<hr> Shortcut will work even if\
        you disable the undo button.<hr> undo button shortcut can be a single key\
        like \"z\" or \"f1\" or a combination of keys like \"ctrl+z\" or \"alt+z\".<hr>\
        <font color=red>NOTE: </font>Make sure the shortcut you want to set for the button isn't already\
        in use by anki itself or another add-on.<hr> the default shortcut for this\
        action is (Ctrl+Z), by changing th shortcut here, the default shortcut\
        will still wok, in other words, if you set a shortcut for undo review\
        here, you will have two shortcuts for it, one is the default (Ctrl+Z)\
        and the other is the shortcut that you have set. {1}".format(begin, end))
        undoShortcut_label.setFixedWidth(125)
        self.undoShortcut_button = QPushButton()
        self.undoShortcut_button.setFixedWidth(300)
        self.undoShortcut_button.clicked.connect(lambda: self.showGetShortcut("undo_shortcut"))
        undoShortcut_holder = QHBoxLayout()
        undoShortcut_holder.addWidget(undoShortcut_label)
        undoShortcut_holder.addStretch()
        undoShortcut_holder.addWidget(self.undoShortcut_button)
        buttonShortcutsPart = QVBoxLayout()
        buttonShortcutsPart.addLayout(infoShortcut_holder)
        buttonShortcutsPart.addLayout(skipShortcut_holder)
        buttonShortcutsPart.addLayout(showSkippedShortcut_holder)
        buttonShortcutsPart.addLayout(undoShortcut_holder)
        buttonShortcutsBox = QGroupBox("Button Shortcuts")
        buttonShortcutsBox.setToolTip("{0}Use \"Ctrl+Z\" to unmap a shortcut.{1}".format(begin, end))
        buttonShortcutsBox.setLayout(buttonShortcutsPart)
        layout = QVBoxLayout()
        layout.addWidget(extraButtonsBox)
        layout.addWidget(hideButtonsBox)
        layout.addWidget(buttonPositionsBox)
        layout.addWidget(buttonShortcutsBox)
        layout.addStretch()
        layout_holder = QWidget()
        layout_holder.setLayout(layout)
        self.tab3 = QScrollArea()
        self.tab3.setFixedWidth(690)
        self.tab3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.tab3.setWidgetResizable(True)
        self.tab3.setWidget(layout_holder)

    def createFourthTab(self):
        begin = self.begin
        end = self.end
        images = self.images
        customSizes_label = QLabel('Custom Sizes:')
        customSizes_label.setToolTip("{0} Enables and disables custom button sizes.<hr> If Enabled\
        button sizes will change according to the sizes you set for each button.<hr>\
        If disabled button sizes will be set on default size.<hr> <font color=red>NOTE: </font>If you use\
        wide buttons, you won't be able to change review buttons width and even when\
        you disable custom button sizes, review buttons will be wide. {1}".format(begin, end))
        customSizes_label.setFixedWidth(180)
        self.customSizes_on = QRadioButton("On")
        self.customSizes_on.setToolTip("{0} Button sizes is disabled and buttons height and width\
        is set to height and width that we have set.<hr> {1} <img src='{2}/buttonSizes_on.png'>\
        <br><img src='{2}/buttonSizes_on2.png'>".format(begin, end, images))
        self.customSizes_on.setFixedWidth(90)
        self.customSizes_off = QRadioButton("Off")
        self.customSizes_off.setToolTip("{0} Button sizes is disabled and all buttons are in default size.<hr>\
        {1} <img src='{2}/buttonSizes_off.png'><img src='{2}/buttonSizes_off2.png'>".format(begin, end, images))
        self.customSizes_off.setFixedWidth(90)
        tab4line1 = QHBoxLayout()
        tab4line1.addWidget(customSizes_label)
        tab4line1.addWidget(self.customSizes_on)
        tab4line1.addWidget(self.customSizes_off)
        tab4line1.addStretch()
        tab4box1 = QGroupBox()
        tab4box1.setLayout(tab4line1)
        textSize_label = QLabel("Buttons Text Size:")
        textSize_label.setToolTip("{0}Sets the text size for all bottombar buttons.\
        It only works on review screen buttons and it will not affect main screen\
         and study screen buttons{1}".format(begin, end))
        textSize_label.setFixedWidth(180)
        self.text_size = QSpinBox()
        self.text_size.setFixedWidth(120)
        self.text_size.setMinimum(0)
        self.text_size.setMaximum(200)
        textSize_px = QLabel("px")
        textSize_holder = QHBoxLayout()
        textSize_holder.addWidget(textSize_label)
        textSize_holder.addWidget(self.text_size)
        textSize_holder.addWidget(textSize_px)
        buttonsHeight_label = QLabel("Bottombar Buttons Height:")
        buttonsHeight_label.setToolTip("{0} Sets height for all bottombar buttons including edit, info,\
        ski, show answer, undo review, more and review buttons.".format(begin, end))
        buttonsHeight_label.setFixedWidth(180)
        self.buttons_height = QSpinBox()
        self.buttons_height.setFixedWidth(120)
        self.buttons_height.setMinimum(0)
        self.buttons_height.setMaximum(200)
        buttonsHeight_px = QLabel("px")
        buttonsHeight_holder = QHBoxLayout()
        buttonsHeight_holder.addWidget(buttonsHeight_label)
        buttonsHeight_holder.addWidget(self.buttons_height)
        buttonsHeight_holder.addWidget(buttonsHeight_px)
        reviewButtonsWidth_label = QLabel("Review Buttons Width:")
        reviewButtonsWidth_label.setToolTip("{0} Sets width for review buttons\
        (again, hard, good and easy buttons).{1}".format(begin, end))
        reviewButtonsWidth_label.setFixedWidth(180)
        self.reviewButtons_width = QSpinBox()
        self.reviewButtons_width.setFixedWidth(120)
        self.reviewButtons_width.setMinimum(0)
        self.reviewButtons_width.setMaximum(400)
        reviewButtonsWidth_px = QLabel("px")
        reviewButtonsWidth_holder = QHBoxLayout()
        reviewButtonsWidth_holder.addWidget(reviewButtonsWidth_label)
        reviewButtonsWidth_holder.addWidget(self.reviewButtons_width)
        reviewButtonsWidth_holder.addWidget(reviewButtonsWidth_px)
        editWidth_label = QLabel("Edit Width:")
        editWidth_label.setToolTip("{0} Sets width for edit button.{1}".format(begin, end))
        editWidth_label.setFixedWidth(180)
        self.edit_width = QSpinBox()
        self.edit_width.setFixedWidth(120)
        self.edit_width.setMinimum(0)
        self.edit_width.setMaximum(400)
        editWidth_px = QLabel("px")
        editWidth_holder = QHBoxLayout()
        editWidth_holder.addWidget(editWidth_label)
        editWidth_holder.addWidget(self.edit_width)
        editWidth_holder.addWidget(editWidth_px)
        answerWidth_label = QLabel("Show Answer Width:")
        answerWidth_label.setToolTip("{0} Sets width for show answer button.{1}".format(begin, end))
        answerWidth_label.setFixedWidth(180)
        self.answer_width = QSpinBox()
        self.answer_width.setFixedWidth(120)
        self.answer_width.setMinimum(0)
        self.answer_width.setMaximum(400)
        answerWidth_px = QLabel("px")
        answerWidth_holder = QHBoxLayout()
        answerWidth_holder.addWidget(answerWidth_label)
        answerWidth_holder.addWidget(self.answer_width)
        answerWidth_holder.addWidget(answerWidth_px)
        moreWidth_label = QLabel("More Width:")
        moreWidth_label.setToolTip("{0} Sets width for more button.{1}".format(begin, end))
        moreWidth_label.setFixedWidth(180)
        self.more_width = QSpinBox()
        self.more_width.setFixedWidth(120)
        self.more_width.setMinimum(0)
        self.more_width.setMaximum(400)
        moreWidth_px = QLabel("px")
        moreWidth_holder = QHBoxLayout()
        moreWidth_holder.addWidget(moreWidth_label)
        moreWidth_holder.addWidget(self.more_width)
        moreWidth_holder.addWidget(moreWidth_px)
        infoWidth_label = QLabel("Info Width:")
        infoWidth_label.setToolTip("{0} Sets width for info button.{1}".format(begin, end))
        infoWidth_label.setFixedWidth(180)
        self.info_width = QSpinBox()
        self.info_width.setFixedWidth(120)
        self.info_width.setMinimum(0)
        self.info_width.setMaximum(400)
        infoWidth_px = QLabel("px")
        infoWidth_holder = QHBoxLayout()
        infoWidth_holder.addWidget(infoWidth_label)
        infoWidth_holder.addWidget(self.info_width)
        infoWidth_holder.addWidget(infoWidth_px)
        skipWidth_label = QLabel("Skip Width:")
        skipWidth_label.setToolTip("{0} Sets width for skip button.{1}".format(begin, end))
        skipWidth_label.setFixedWidth(180)
        self.skip_width = QSpinBox()
        self.skip_width.setFixedWidth(120)
        self.skip_width.setMinimum(0)
        self.skip_width.setMaximum(400)
        skipWidth_px = QLabel("px")
        skipWidth_holder = QHBoxLayout()
        skipWidth_holder.addWidget(skipWidth_label)
        skipWidth_holder.addWidget(self.skip_width)
        skipWidth_holder.addWidget(skipWidth_px)
        showSkippedWidth_label = QLabel("Show Skipped Width:")
        showSkippedWidth_label.setToolTip("{0} Sets width for Show Skipped button.{1}".format(begin, end))
        showSkippedWidth_label.setFixedWidth(180)
        self.showSkipped_width = QSpinBox()
        self.showSkipped_width.setFixedWidth(120)
        self.showSkipped_width.setMinimum(0)
        self.showSkipped_width.setMaximum(400)
        showSkippedWidth_px = QLabel("px")
        showSkippedWidth_holder = QHBoxLayout()
        showSkippedWidth_holder.addWidget(showSkippedWidth_label)
        showSkippedWidth_holder.addWidget(self.showSkipped_width)
        showSkippedWidth_holder.addWidget(showSkippedWidth_px)
        undoWidth_label = QLabel("Undo Width:")
        undoWidth_label.setToolTip("{0} Sets width for undo button.{1}".format(begin, end))
        undoWidth_label.setFixedWidth(180)
        self.undo_width = QSpinBox()
        self.undo_width.setFixedWidth(120)
        self.undo_width.setMinimum(0)
        self.undo_width.setMaximum(400)
        undoWidth_px = QLabel("px")
        undoWidth_holder = QHBoxLayout()
        undoWidth_holder.addWidget(undoWidth_label)
        undoWidth_holder.addWidget(self.undo_width)
        undoWidth_holder.addWidget(undoWidth_px)
        tab4line2 = QVBoxLayout()
        tab4line2.addLayout(textSize_holder)
        tab4line2.addLayout(buttonsHeight_holder)
        tab4line2.addLayout(reviewButtonsWidth_holder)
        tab4line2.addLayout(editWidth_holder)
        tab4line2.addLayout(answerWidth_holder)
        tab4line2.addLayout(moreWidth_holder)
        tab4line2.addLayout(infoWidth_holder)
        tab4line2.addLayout(skipWidth_holder)
        tab4line2.addLayout(showSkippedWidth_holder)
        tab4line2.addLayout(undoWidth_holder)
        tab4box2 = QGroupBox()
        tab4box2.setDisabled(True)
        if self.customSizes_on.isChecked():
            tab4box2.setEnabled(True)
        self.customSizes_on.toggled.connect(tab4box2.setEnabled)
        tab4box2.setLayout(tab4line2)
        layout = QVBoxLayout()
        layout.addWidget(tab4box1)
        layout.addWidget(tab4box2)
        layout.addStretch()
        layout_holder = QWidget()
        layout_holder.setLayout(layout)
        self.tab4 = QScrollArea()
        self.tab4.setFixedWidth(690)
        self.tab4.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.tab4.setWidgetResizable(True)
        self.tab4.setWidget(layout_holder)

    def createFifthTab(self):
        begin = self.begin
        end = self.end
        images = self.images
        buttonLabel_studyNow_label = QLabel("Study Now:")
        buttonLabel_studyNow_label.setToolTip("{0}Replaces the text for \"Study Now\" Button with your custom text.{1}".format(begin, end))
        buttonLabel_studyNow_label.setFixedWidth(90)
        self.buttonLabel_studyNow = QLineEdit()
        buttonlabel_studyNow_holder = QHBoxLayout()
        buttonlabel_studyNow_holder.addWidget(buttonLabel_studyNow_label)
        buttonlabel_studyNow_holder.addWidget(self.buttonLabel_studyNow)
        buttonLabel_studyNow_box = QGroupBox()
        buttonLabel_studyNow_box.setLayout(buttonlabel_studyNow_holder)
        buttonLabel_edit_label = QLabel("Edit:")
        buttonLabel_edit_label.setToolTip("{0}Replaces the text for \"Edit\" Button with your custom text.{1}".format(begin, end))
        buttonLabel_edit_label.setFixedWidth(90)
        self.buttonLabel_edit = QLineEdit()
        buttonlabel_edit_holder = QHBoxLayout()
        buttonlabel_edit_holder.addWidget(buttonLabel_edit_label)
        buttonlabel_edit_holder.addWidget(self.buttonLabel_edit)
        buttonLabel_edit_box = QGroupBox()
        buttonLabel_edit_box.setLayout(buttonlabel_edit_holder)
        firstLine = QHBoxLayout()
        firstLine.addWidget(buttonLabel_studyNow_box)
        firstLine.addWidget(buttonLabel_edit_box)
        buttonLabel_showAnswer_label = QLabel("Show Answer:")
        buttonLabel_showAnswer_label.setToolTip("{0}Replaces the text for \"Show Answer\" Button with your custom text.{1}".format(begin, end))
        buttonLabel_showAnswer_label.setFixedWidth(90)
        self.buttonLabel_showAnswer = QLineEdit()
        buttonlabel_showAnswer_holder = QHBoxLayout()
        buttonlabel_showAnswer_holder.addWidget(buttonLabel_showAnswer_label)
        buttonlabel_showAnswer_holder.addWidget(self.buttonLabel_showAnswer)
        buttonLabel_showAnswer_box = QGroupBox()
        buttonLabel_showAnswer_box.setLayout(buttonlabel_showAnswer_holder)
        buttonLabel_more_label = QLabel("More:")
        buttonLabel_more_label.setToolTip("{0}Replaces the text for \"More\" Button with your custom text.{1}".format(begin, end))
        buttonLabel_more_label.setFixedWidth(90)
        self.buttonLabel_more = QLineEdit()
        buttonlabel_more_holder = QHBoxLayout()
        buttonlabel_more_holder.addWidget(buttonLabel_more_label)
        buttonlabel_more_holder.addWidget(self.buttonLabel_more)
        buttonLabel_more_box = QGroupBox()
        buttonLabel_more_box.setLayout(buttonlabel_more_holder)
        secondLine = QHBoxLayout()
        secondLine.addWidget(buttonLabel_showAnswer_box)
        secondLine.addWidget(buttonLabel_more_box)
        buttonLabel_info_label = QLabel("Info:")
        buttonLabel_info_label.setToolTip("{0}Replaces the text for \"Info\" Button with your custom text.{1}".format(begin, end))
        buttonLabel_info_label.setFixedWidth(90)
        self.buttonLabel_info = QLineEdit()
        buttonlabel_info_holder = QHBoxLayout()
        buttonlabel_info_holder.addWidget(buttonLabel_info_label)
        buttonlabel_info_holder.addWidget(self.buttonLabel_info)
        buttonLabel_info_box = QGroupBox()
        buttonLabel_info_box.setLayout(buttonlabel_info_holder)
        buttonLabel_skip_label = QLabel("Skip:")
        buttonLabel_skip_label.setToolTip("{0}Replaces the text for \"Skip\" Button with your custom text.{1}".format(begin, end))
        buttonLabel_skip_label.setFixedWidth(90)
        self.buttonLabel_skip = QLineEdit()
        buttonlabel_skip_holder = QHBoxLayout()
        buttonlabel_skip_holder.addWidget(buttonLabel_skip_label)
        buttonlabel_skip_holder.addWidget(self.buttonLabel_skip)
        buttonLabel_skip_box = QGroupBox()
        buttonLabel_skip_box.setLayout(buttonlabel_skip_holder)
        thirdLine = QHBoxLayout()
        thirdLine.addWidget(buttonLabel_info_box)
        thirdLine.addWidget(buttonLabel_skip_box)
        buttonLabel_undo_label = QLabel("Undo:")
        buttonLabel_undo_label.setToolTip("{0}Replaces the text for \"Undo\" Button with your custom text.{1}".format(begin, end))
        buttonLabel_undo_label.setFixedWidth(90)
        self.buttonLabel_undo = QLineEdit()
        buttonlabel_undo_holder = QHBoxLayout()
        buttonlabel_undo_holder.addWidget(buttonLabel_undo_label)
        buttonlabel_undo_holder.addWidget(self.buttonLabel_undo)
        buttonLabel_undo_box = QGroupBox()
        buttonLabel_undo_box.setLayout(buttonlabel_undo_holder)
        buttonLabel_showSkipped_label = QLabel("Show Skipped:")
        buttonLabel_showSkipped_label.setToolTip("{0}Replaces the text for \"Show Skipped\" Button with your custom text.{1}".format(begin, end))
        buttonLabel_showSkipped_label.setFixedWidth(90)
        self.buttonLabel_showSkipped = QLineEdit()
        buttonlabel_showSkipped_holder = QHBoxLayout()
        buttonlabel_showSkipped_holder.addWidget(buttonLabel_showSkipped_label)
        buttonlabel_showSkipped_holder.addWidget(self.buttonLabel_showSkipped)
        buttonLabel_showSkipped_box = QGroupBox()
        buttonLabel_showSkipped_box.setLayout(buttonlabel_showSkipped_holder)
        fourthLine = QHBoxLayout()
        fourthLine.addWidget(buttonLabel_undo_box)
        fourthLine.addWidget(buttonLabel_showSkipped_box)
        buttonLabel_again_label = QLabel("Again:")
        buttonLabel_again_label.setToolTip("{0}Replaces the text for \"Again\" Button with your custom text.{1}".format(begin, end))
        buttonLabel_again_label.setFixedWidth(90)
        self.buttonLabel_again = QLineEdit()
        buttonlabel_again_holder = QHBoxLayout()
        buttonlabel_again_holder.addWidget(buttonLabel_again_label)
        buttonlabel_again_holder.addWidget(self.buttonLabel_again)
        buttonLabel_again_box = QGroupBox()
        buttonLabel_again_box.setLayout(buttonlabel_again_holder)
        buttonLabel_hard_label = QLabel("Hard:")
        buttonLabel_hard_label.setToolTip("{0}Replaces the text for \"Hard\" Button with your custom text.{1}".format(begin, end))
        buttonLabel_hard_label.setFixedWidth(90)
        self.buttonLabel_hard = QLineEdit()
        buttonlabel_hard_holder = QHBoxLayout()
        buttonlabel_hard_holder.addWidget(buttonLabel_hard_label)
        buttonlabel_hard_holder.addWidget(self.buttonLabel_hard)
        buttonLabel_hard_box = QGroupBox()
        buttonLabel_hard_box.setLayout(buttonlabel_hard_holder)
        fifthLine = QHBoxLayout()
        fifthLine.addWidget(buttonLabel_again_box)
        fifthLine.addWidget(buttonLabel_hard_box)
        buttonLabel_good_label = QLabel("Good:")
        buttonLabel_good_label.setToolTip("{0}Replaces the text for \"Good\" Button with your custom text.{1}".format(begin, end))
        buttonLabel_good_label.setFixedWidth(90)
        self.buttonLabel_good = QLineEdit()
        buttonlabel_good_holder = QHBoxLayout()
        buttonlabel_good_holder.addWidget(buttonLabel_good_label)
        buttonlabel_good_holder.addWidget(self.buttonLabel_good)
        buttonLabel_good_box = QGroupBox()
        buttonLabel_good_box.setLayout(buttonlabel_good_holder)
        buttonLabel_easy_label = QLabel("Easy:")
        buttonLabel_easy_label.setToolTip("{0}Replaces the text for \"Easy\" Button with your custom text.{1}".format(begin, end))
        buttonLabel_easy_label.setFixedWidth(90)
        self.buttonLabel_easy = QLineEdit()
        buttonlabel_easy_holder = QHBoxLayout()
        buttonlabel_easy_holder.addWidget(buttonLabel_easy_label)
        buttonlabel_easy_holder.addWidget(self.buttonLabel_easy)
        buttonLabel_easy_box = QGroupBox()
        buttonLabel_easy_box.setLayout(buttonlabel_easy_holder)
        sixthLine = QHBoxLayout()
        sixthLine.addWidget(buttonLabel_good_box)
        sixthLine.addWidget(buttonLabel_easy_box)
        layout = QVBoxLayout()
        layout.addLayout(firstLine)
        layout.addLayout(secondLine)
        layout.addLayout(thirdLine)
        layout.addLayout(fourthLine)
        layout.addLayout(fifthLine)
        layout.addLayout(sixthLine)
        layout.addStretch()
        layout_holder = QWidget()
        layout_holder.setLayout(layout)
        self.tab5 = QScrollArea()
        self.tab5.setFixedWidth(690)
        self.tab5.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.tab5.setWidgetResizable(True)
        self.tab5.setWidget(layout_holder)

    def createSixthTab(self):
        begin = self.begin
        end = self.end
        images = self.images
        SIDEBAR_ITEM_WIDTH = 150
        sidebarTheme_label = QLabel("Card Info Sidebar Theme:")
        sidebarTheme_label.setToolTip("{0} Changes sidebar theme. {1}".format(begin, end))
        sidebarTheme_label.setFixedWidth(195)
        self.sidebar_theme = QComboBox()
        self.sidebar_theme.addItems(["Auto", "Day/Light", "Night/Dark"])
        self.sidebar_theme.setToolTip("{0} Auto: Chooses the sidebar theme based on your anki theme.<br>\
        <font color=red>NOTE: </font>This option only supports anki's native night\
        mode and does not work with night mode add-on.<hr> Day: Forces sidebar to use light theme whether your anki is\
        in night mode or not.<hr> Night: Forces sidebar to use dark theme whether your anki is\
        in night mode or not. {1}".format(begin, end))
        self.sidebar_theme.setMinimumWidth(200)
        sideBarTheme_holder = QHBoxLayout()
        sideBarTheme_holder.addWidget(sidebarTheme_label)
        sideBarTheme_holder.addWidget(self.sidebar_theme)
        sideBarTheme_holder.addStretch()
        sidebarFont_label = QLabel("Card Info Sidebar Font:")
        sidebarFont_label.setToolTip("{0} Changes card info sidebar font. {1}".format(begin, end))
        sidebarFont_label.setFixedWidth(195)
        self.sidebar_font = QFontComboBox()
        self.sidebar_font.setMinimumWidth(200)
        sidebarFont_holder = QHBoxLayout()
        sidebarFont_holder.addWidget(sidebarFont_label)
        sidebarFont_holder.addWidget(self.sidebar_font)
        sidebarFont_holder.addStretch()
        sidebarHideCurrentCard_label = QLabel("Hide Current Card:")
        sidebarHideCurrentCard_label.setToolTip("{0}If Enabled, the info for the current card in review will not\
        be shown on the sidebar.{1}".format(begin, end))
        sidebarHideCurrentCard_label.setFixedWidth(195)
        self.sidebar_hideCurrentCard = QComboBox()
        self.sidebar_hideCurrentCard.addItems(["Disabled", "Enabled"])
        self.sidebar_hideCurrentCard.setMinimumWidth(200)
        sidebarHideCurrentCard_holder = QHBoxLayout()
        sidebarHideCurrentCard_holder.addWidget(sidebarHideCurrentCard_label)
        sidebarHideCurrentCard_holder.addWidget(self.sidebar_hideCurrentCard)
        sidebarHideCurrentCard_holder.addStretch()
        sidebarPreviousCards_label = QLabel("Number of Previous Cards To Show:")
        sidebarPreviousCards_label.setToolTip("{0} Changes number of previous cards that show on the card\
        info sidebar.</font> {1}".format(begin, end))
        sidebarPreviousCards_label.setFixedWidth(195)
        self.sidebar_PreviousCards = QSpinBox()
        self.sidebar_PreviousCards.setMinimumWidth(200)
        self.sidebar_PreviousCards.setMaximum(4)
        sidebarPreviousCards_holder = QHBoxLayout()
        sidebarPreviousCards_holder.addWidget(sidebarPreviousCards_label)
        sidebarPreviousCards_holder.addWidget(self.sidebar_PreviousCards)
        sidebarPreviousCards_holder.addStretch()
        sidebarReviewsToShow_label = QLabel("Card Previous Reviews To Show:")
        sidebarReviewsToShow_label.setToolTip("{0} Changes number of previous reviews for a card to show on\
        the card info sidebar.<hr><font color=red> If you want it to show all reviews for a card, set it on 0.{1}".format(begin, end))
        sidebarReviewsToShow_label.setFixedWidth(195)
        self.sidebar_reviewsToShow = QSpinBox()
        self.sidebar_reviewsToShow.setMinimumWidth(200)
        self.sidebar_reviewsToShow.setMaximum(500)
        sidebarReviewsToShow_holder = QHBoxLayout()
        sidebarReviewsToShow_holder.addWidget(sidebarReviewsToShow_label)
        sidebarReviewsToShow_holder.addWidget(self.sidebar_reviewsToShow)
        sidebarReviewsToShow_holder.addStretch()
        tab5line1 = QVBoxLayout()
        tab5line1.addLayout(sideBarTheme_holder)
        tab5line1.addLayout(sidebarFont_holder)
        tab5line1.addLayout(sidebarHideCurrentCard_holder)
        tab5line1.addLayout(sidebarPreviousCards_holder)
        tab5line1.addLayout(sidebarReviewsToShow_holder)
        tab5box1 = QGroupBox()
        tab5box1.setLayout(tab5line1)
        self.sidebar_currentReviewCount = QCheckBox("Current Review Count")
        self.sidebar_currentReviewCount.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        self.sidebar_dateCreated = QCheckBox('Date Created')
        self.sidebar_dateCreated.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        self.sidebar_dateEdited = QCheckBox('Dated Edited')
        self.sidebar_dateEdited.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        tab5subline1 = QHBoxLayout()
        tab5subline1.addWidget(self.sidebar_currentReviewCount)
        tab5subline1.addWidget(self.sidebar_dateCreated)
        tab5subline1.addWidget(self.sidebar_dateEdited)
        tab5subline1.addStretch()
        self.sidebar_firstReview = QCheckBox('First Review')
        self.sidebar_firstReview.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        self.sidebar_latestReview = QCheckBox('Latest Review')
        self.sidebar_latestReview.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        self.sidebar_due = QCheckBox('Due')
        self.sidebar_due.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        tab5subline2 = QHBoxLayout()
        tab5subline2.addWidget(self.sidebar_firstReview)
        tab5subline2.addWidget(self.sidebar_latestReview)
        tab5subline2.addWidget(self.sidebar_due)
        tab5subline2.addStretch()
        self.sidebar_interval = QCheckBox('Interval')
        self.sidebar_interval.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        self.sidebar_ease = QCheckBox('Ease')
        self.sidebar_ease.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        self.sidebar_numberOfReviews = QCheckBox('Number of Reviews')
        self.sidebar_numberOfReviews.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        tab5subline3 = QHBoxLayout()
        tab5subline3.addWidget(self.sidebar_interval)
        tab5subline3.addWidget(self.sidebar_ease)
        tab5subline3.addWidget(self.sidebar_numberOfReviews)
        tab5subline3.addStretch()
        self.sidebar_lapses = QCheckBox('Lapses')
        self.sidebar_lapses.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        self.sidebar_averageTime = QCheckBox('Average Time')
        self.sidebar_averageTime.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        self.sidebar_totalTime = QCheckBox('Total Time')
        self.sidebar_totalTime.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        tab5subline4 = QHBoxLayout()
        tab5subline4.addWidget(self.sidebar_lapses)
        tab5subline4.addWidget(self.sidebar_averageTime)
        tab5subline4.addWidget(self.sidebar_totalTime)
        tab5subline4.addStretch()
        self.sidebar_cardType = QCheckBox('Card Type')
        self.sidebar_cardType.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        self.sidebar_noteType = QCheckBox('Note Type')
        self.sidebar_noteType.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        self.sidebar_deck = QCheckBox('Deck')
        self.sidebar_deck.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        tab5subline5 = QHBoxLayout()
        tab5subline5.addWidget(self.sidebar_cardType)
        tab5subline5.addWidget(self.sidebar_noteType)
        tab5subline5.addWidget(self.sidebar_deck)
        tab5subline5.addStretch()
        self.sidebar_tags = QCheckBox('Tags')
        self.sidebar_tags.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        self.sidebar_sortField = QCheckBox('Sort Field')
        self.sidebar_sortField.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        self.sidebar_warningNote = QCheckBox('Warning Note')
        self.sidebar_warningNote.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        tab5subline6 = QHBoxLayout()
        tab5subline6.addWidget(self.sidebar_tags)
        tab5subline6.addWidget(self.sidebar_sortField)
        tab5subline6.addWidget(self.sidebar_warningNote)
        tab5subline6.addStretch()
        self.sidebar_correctPercent = QCheckBox('Correct Percentage')
        self.sidebar_correctPercent.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        self.sidebar_fastestReview = QCheckBox('Fastest Review')
        self.sidebar_fastestReview.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        self.sidebar_slowestReview = QCheckBox('Slowest Review')
        self.sidebar_slowestReview.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        tab5subline7 = QHBoxLayout()
        tab5subline7.addWidget(self.sidebar_correctPercent)
        tab5subline7.addWidget(self.sidebar_fastestReview)
        tab5subline7.addWidget(self.sidebar_slowestReview)
        tab5subline7.addStretch()
        self.sidebar_noteID = QCheckBox('Note ID')
        self.sidebar_noteID.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        self.sidebar_cardID = QCheckBox('Card ID')
        self.sidebar_cardID.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        self.sidebar_autoOpen = QCheckBox('Auto Open')
        self.sidebar_autoOpen.setToolTip("Opens sidebar automatically when you review a card")
        self.sidebar_autoOpen.setFixedWidth(SIDEBAR_ITEM_WIDTH)
        tab5subline8 = QHBoxLayout()
        tab5subline8.addWidget(self.sidebar_noteID)
        tab5subline8.addWidget(self.sidebar_cardID)
        tab5subline8.addWidget(self.sidebar_autoOpen)
        tab5subline8.addStretch()
        tab5line2 = QVBoxLayout()
        tab5line2.addLayout(tab5subline1)
        tab5line2.addLayout(tab5subline2)
        tab5line2.addLayout(tab5subline3)
        tab5line2.addLayout(tab5subline4)
        tab5line2.addLayout(tab5subline5)
        tab5line2.addLayout(tab5subline6)
        tab5line2.addLayout(tab5subline7)
        tab5line2.addLayout(tab5subline8)
        tab5box2 = QGroupBox()
        tab5box2.setLayout(tab5line2)
        layout = QVBoxLayout()
        layout.addWidget(tab5box1)
        layout.addWidget(tab5box2)
        layout.addStretch()
        layout_holder = QWidget()
        layout_holder.setLayout(layout)
        self.tab6 = QScrollArea()
        self.tab6.setFixedWidth(690)
        self.tab6.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.tab6.setWidgetResizable(True)
        self.tab6.setWidget(layout_holder)

    def createSeventhTab(self):
        begin = self.begin
        end = self.end
        images = self.images
        self.custom_reviewButtonColors = QGroupBox("Custom Review Button Colors")
        self.custom_reviewButtonColors.setToolTip("{0}Changes text or background color and hover colors for review buttons.<hr>\
        as the neon and fill buttons don't have a separate hover color, changing hover color will not affect those buttons.{1}".format(begin, end))
        self.custom_reviewButtonColors.setCheckable(True)
        self.custom_reviewButtonColors.setChecked(False)
        againColor_label = QLabel("Again:")
        againColor_label.setFixedWidth(140)
        self.againColor_button = QPushButton()
        self.againColor_button.clicked.connect(lambda: self.getNewColor("again_color", self.againColor_button))
        againColor_holder = QHBoxLayout()
        againColor_holder.addWidget(againColor_label)
        againColor_holder.addWidget(self.againColor_button)
        againColor_box = QGroupBox()
        againColor_box.setLayout(againColor_holder)
        againHoverColor_label = QLabel("Again on Hover:")
        againHoverColor_label.setFixedWidth(140)
        self.againHoverColor_button = QPushButton()
        self.againHoverColor_button.clicked.connect(lambda: self.getNewColor("againHover_color", self.againHoverColor_button))
        againHoverColor_holder = QHBoxLayout()
        againHoverColor_holder.addWidget(againHoverColor_label)
        againHoverColor_holder.addWidget(self.againHoverColor_button)
        againHover_box = QGroupBox()
        againHover_box.setLayout(againHoverColor_holder)
        again_line = QHBoxLayout()
        again_line.addWidget(againColor_box)
        again_line.addWidget(againHover_box)
        hardColor_label = QLabel("Hard:")
        hardColor_label.setFixedWidth(140)
        self.hardColor_button = QPushButton()
        self.hardColor_button.clicked.connect(lambda: self.getNewColor("hard_color", self.hardColor_button))
        hardColor_holder = QHBoxLayout()
        hardColor_holder.addWidget(hardColor_label)
        hardColor_holder.addWidget(self.hardColor_button)
        hardColor_box = QGroupBox()
        hardColor_box.setLayout(hardColor_holder)
        hardHoverColor_label = QLabel("Hard on Hover:")
        hardHoverColor_label.setFixedWidth(140)
        self.hardHoverColor_button = QPushButton()
        self.hardHoverColor_button.clicked.connect(lambda: self.getNewColor("hardHover_color", self.hardHoverColor_button))
        hardHoverColor_holder = QHBoxLayout()
        hardHoverColor_holder.addWidget(hardHoverColor_label)
        hardHoverColor_holder.addWidget(self.hardHoverColor_button)
        hardHover_box = QGroupBox()
        hardHover_box.setLayout(hardHoverColor_holder)
        hard_line = QHBoxLayout()
        hard_line.addWidget(hardColor_box)
        hard_line.addWidget(hardHover_box)
        goodColor_label = QLabel("Good:")
        goodColor_label.setFixedWidth(140)
        self.goodColor_button = QPushButton()
        self.goodColor_button.clicked.connect(lambda: self.getNewColor("good_color", self.goodColor_button))
        goodColor_holder = QHBoxLayout()
        goodColor_holder.addWidget(goodColor_label)
        goodColor_holder.addWidget(self.goodColor_button)
        goodColor_box = QGroupBox()
        goodColor_box.setLayout(goodColor_holder)
        goodHoverColor_label = QLabel("Good on Hover:")
        goodHoverColor_label.setFixedWidth(140)
        self.goodHoverColor_button = QPushButton()
        self.goodHoverColor_button.clicked.connect(lambda: self.getNewColor("goodHover_color", self.goodHoverColor_button))
        goodHoverColor_holder = QHBoxLayout()
        goodHoverColor_holder.addWidget(goodHoverColor_label)
        goodHoverColor_holder.addWidget(self.goodHoverColor_button)
        goodHover_box = QGroupBox()
        goodHover_box.setLayout(goodHoverColor_holder)
        good_line = QHBoxLayout()
        good_line.addWidget(goodColor_box)
        good_line.addWidget(goodHover_box)
        easyColor_label = QLabel("Easy:")
        easyColor_label.setFixedWidth(140)
        self.easyColor_button = QPushButton()
        self.easyColor_button.clicked.connect(lambda: self.getNewColor("easy_color", self.easyColor_button))
        easyColor_holder = QHBoxLayout()
        easyColor_holder.addWidget(easyColor_label)
        easyColor_holder.addWidget(self.easyColor_button)
        easyColor_box = QGroupBox()
        easyColor_box.setLayout(easyColor_holder)
        easyHoverColor_label = QLabel("Easy on Hover:")
        easyHoverColor_label.setFixedWidth(140)
        self.easyHoverColor_button = QPushButton()
        self.easyHoverColor_button.clicked.connect(lambda: self.getNewColor("easyHover_color", self.easyHoverColor_button))
        easyHoverColor_holder = QHBoxLayout()
        easyHoverColor_holder.addWidget(easyHoverColor_label)
        easyHoverColor_holder.addWidget(self.easyHoverColor_button)
        easyHover_box = QGroupBox()
        easyHover_box.setLayout(easyHoverColor_holder)
        easy_line = QHBoxLayout()
        easy_line.addWidget(easyColor_box)
        easy_line.addWidget(easyHover_box)
        reviewButtonColors_layout = QVBoxLayout()
        reviewButtonColors_layout.addLayout(again_line)
        reviewButtonColors_layout.addLayout(hard_line)
        reviewButtonColors_layout.addLayout(good_line)
        reviewButtonColors_layout.addLayout(easy_line)
        self.custom_reviewButtonColors.setLayout(reviewButtonColors_layout)
        self.custom_reviewButtonTextColor = QCheckBox("Review Button Text:")
        self.custom_reviewButtonTextColor.setToolTip("{0}Changes the color of general text color inside buttons.\
        <hr> This option does not work on Default + Text Color and Wide + Text Color Styles {1}".format(begin, end))
        self.custom_reviewButtonTextColor.setFixedWidth(140)
        self.reviewButtonTextColor_button = QPushButton()
        self.reviewButtonTextColor_button.clicked.connect(lambda: self.getNewColor("reviewButtonText_color", self.reviewButtonTextColor_button))
        reviewButtonTextColor_holder = QHBoxLayout()
        reviewButtonTextColor_holder.addWidget(self.custom_reviewButtonTextColor)
        reviewButtonTextColor_holder.addWidget(self.reviewButtonTextColor_button)
        reviewButtonTextColor_box = QGroupBox()
        reviewButtonTextColor_box.setLayout(reviewButtonTextColor_holder)
        self.reviewButtonTextColor_button.setDisabled(True)
        if self.custom_reviewButtonTextColor.isChecked():
            self.reviewButtonTextColor_button.setEnabled(True)
        self.custom_reviewButtonTextColor.toggled.connect(self.reviewButtonTextColor_button.setEnabled)
        self.custom_activeIndicatorColor = QCheckBox("Active Indicator:")
        self.custom_activeIndicatorColor.setToolTip("{0}Changes the active indicator color.<hr>\
        This option does not work on neon and fill buttons as they don't have active indicator for active buttons.{1}".format(begin, end))
        self.custom_activeIndicatorColor.setFixedWidth(140)
        self.activeIndicatorColor_button = QPushButton()
        self.activeIndicatorColor_button.clicked.connect(lambda: self.getNewColor("activeIndicator_color", self.activeIndicatorColor_button))
        activeIndicatorColor_holder = QHBoxLayout()
        activeIndicatorColor_holder.addWidget(self.custom_activeIndicatorColor)
        activeIndicatorColor_holder.addWidget(self.activeIndicatorColor_button)
        activeIndicatorColor_box = QGroupBox()
        activeIndicatorColor_box.setLayout(activeIndicatorColor_holder)
        self.activeIndicatorColor_button.setDisabled(True)
        if self.custom_activeIndicatorColor.isChecked():
            self.activeIndicatorColor_button.setEnabled(True)
        self.custom_activeIndicatorColor.toggled.connect(self.activeIndicatorColor_button.setEnabled)
        reviewButtonTextColor_activeIndicatorColor_line = QHBoxLayout()
        reviewButtonTextColor_activeIndicatorColor_line.addWidget(reviewButtonTextColor_box)
        reviewButtonTextColor_activeIndicatorColor_line.addWidget(activeIndicatorColor_box)
        self.custom_bottombarButtonTextColor = QCheckBox("General Button Text:")
        self.custom_bottombarButtonTextColor.setToolTip("{0}Changes color of text inside all buttons including bottombar buttons, deck overview buttons and main screen bottombar buttons.{1}".format(begin, end))
        self.custom_bottombarButtonTextColor.setFixedWidth(140)
        self.bottombarButtonTextColor_button = QPushButton()
        self.bottombarButtonTextColor_button.clicked.connect(lambda: self.getNewColor("bottombarButtonText_color", self.bottombarButtonTextColor_button))
        bottombarButtonTextColor_holder = QHBoxLayout()
        bottombarButtonTextColor_holder.addWidget(self.custom_bottombarButtonTextColor)
        bottombarButtonTextColor_holder.addWidget(self.bottombarButtonTextColor_button)
        bottombarButtonTextColor_box = QGroupBox()
        bottombarButtonTextColor_box.setLayout(bottombarButtonTextColor_holder)
        self.bottombarButtonTextColor_button.setDisabled(True)
        if self.custom_bottombarButtonTextColor.isChecked():
            self.bottombarButtonTextColor_button.setEnabled(True)
        self.custom_bottombarButtonTextColor.toggled.connect(self.bottombarButtonTextColor_button.setEnabled)
        self.custom_bottombarButtonBorderColor = QCheckBox("General Button Border:")
        self.custom_bottombarButtonBorderColor.setToolTip("{0}Changes border color for all buttons including bottombar buttons, deck overview buttons and main screen bottombar buttons.{1}".format(begin, end))
        self.custom_bottombarButtonBorderColor.setFixedWidth(140)
        self.bottombarButtonBorderColor_button = QPushButton()
        self.bottombarButtonBorderColor_button.clicked.connect(lambda: self.getNewColor("bottombarButtonBorder_color", self.bottombarButtonBorderColor_button))
        bottombarButtonBorderColor_holder = QHBoxLayout()
        bottombarButtonBorderColor_holder.addWidget(self.custom_bottombarButtonBorderColor)
        bottombarButtonBorderColor_holder.addWidget(self.bottombarButtonBorderColor_button)
        bottombarButtonBorderColor_box = QGroupBox()
        bottombarButtonBorderColor_box.setLayout(bottombarButtonBorderColor_holder)
        self.bottombarButtonBorderColor_button.setDisabled(True)
        if self.custom_bottombarButtonBorderColor.isChecked():
            self.bottombarButtonBorderColor_button.setEnabled(True)
        self.custom_bottombarButtonBorderColor.toggled.connect(self.bottombarButtonBorderColor_button.setEnabled)
        bottobarButtonTextColor_bottombarButtonBorderColor_line = QHBoxLayout()
        bottobarButtonTextColor_bottombarButtonBorderColor_line.addWidget(bottombarButtonTextColor_box)
        bottobarButtonTextColor_bottombarButtonBorderColor_line.addWidget(bottombarButtonBorderColor_box)
        showAnswerEase1_label = QLabel("Ease less than")
        showAnswerEase1_label.setFixedWidth(120)
        self.showAnswerEase1 = QSpinBox()
        self.showAnswerEase1.setFixedWidth(90)
        self.showAnswerEase1.setMinimum(130)
        self.showAnswerEase1.setMaximum(999999)
        self.showAnswerEase1_button = QPushButton()
        self.showAnswerEase1_button.setFixedWidth(210)
        self.showAnswerEase1_button.clicked.connect(lambda: self.getNewColor("showAnswerEase1", self.showAnswerEase1_button))
        showAnswerEase1_holder = QHBoxLayout()
        showAnswerEase1_holder.addWidget(showAnswerEase1_label)
        showAnswerEase1_holder.addWidget(self.showAnswerEase1)
        showAnswerEase1_holder.addStretch()
        showAnswerEase1_holder.addWidget(self.showAnswerEase1_button)
        showAnswerEase1_box = QGroupBox()
        showAnswerEase1_box.setLayout(showAnswerEase1_holder)
        showAnswerEase2_label = QLabel("Ease from {} to".format(C_showAnswerEase1))
        showAnswerEase2_label.setFixedWidth(120)
        self.showAnswerEase2 = QSpinBox()
        self.showAnswerEase2.setMinimum(130)
        self.showAnswerEase2.setMaximum(999999)
        self.showAnswerEase2.setFixedWidth(90)
        self.showAnswerEase2_button = QPushButton()
        self.showAnswerEase2_button.setFixedWidth(210)
        self.showAnswerEase2_button.clicked.connect(lambda: self.getNewColor("showAnswerEase2", self.showAnswerEase2_button))
        showAnswerEase2_holder = QHBoxLayout()
        showAnswerEase2_holder.addWidget(showAnswerEase2_label)
        showAnswerEase2_holder.addWidget(self.showAnswerEase2)
        showAnswerEase2_holder.addStretch()
        showAnswerEase2_holder.addWidget(self.showAnswerEase2_button)
        showAnswerEase2_box = QGroupBox()
        showAnswerEase2_box.setLayout(showAnswerEase2_holder)
        showAnswerEase3_label = QLabel("Ease from {} to".format(C_showAnswerEase2))
        showAnswerEase3_label.setFixedWidth(120)
        self.showAnswerEase3 = QSpinBox()
        self.showAnswerEase3.setMinimum(130)
        self.showAnswerEase3.setMaximum(999999)
        self.showAnswerEase3.setFixedWidth(90)
        self.showAnswerEase3_button = QPushButton()
        self.showAnswerEase3_button.setFixedWidth(210)
        self.showAnswerEase3_button.clicked.connect(lambda: self.getNewColor("showAnswerEase3", self.showAnswerEase3_button))
        showAnswerEase3_holder = QHBoxLayout()
        showAnswerEase3_holder.addWidget(showAnswerEase3_label)
        showAnswerEase3_holder.addWidget(self.showAnswerEase3)
        showAnswerEase3_holder.addStretch()
        showAnswerEase3_holder.addWidget(self.showAnswerEase3_button)
        showAnswerEase3_box = QGroupBox()
        showAnswerEase3_box.setLayout(showAnswerEase3_holder)
        showAnswerEase4_label = QLabel("Ease from {} to".format(C_showAnswerEase3))
        showAnswerEase4_label.setFixedWidth(120)
        self.showAnswerEase4 = QSpinBox()
        self.showAnswerEase4.setMinimum(130)
        self.showAnswerEase4.setMaximum(999999)
        self.showAnswerEase4.setFixedWidth(90)
        self.showAnswerEase4_button = QPushButton()
        self.showAnswerEase4_button.setFixedWidth(210)
        self.showAnswerEase4_button.clicked.connect(lambda: self.getNewColor("showAnswerEase4", self.showAnswerEase4_button))
        showAnswerEase4_holder = QHBoxLayout()
        showAnswerEase4_holder.addWidget(showAnswerEase4_label)
        showAnswerEase4_holder.addWidget(self.showAnswerEase4)
        showAnswerEase4_holder.addStretch()
        showAnswerEase4_holder.addWidget(self.showAnswerEase4_button)
        showAnswerEase4_box = QGroupBox()
        showAnswerEase4_box.setLayout(showAnswerEase4_holder)
        showAnswerColors_layout = QVBoxLayout()
        showAnswerColors_layout.addWidget(showAnswerEase1_box)
        showAnswerColors_layout.addWidget(showAnswerEase2_box)
        showAnswerColors_layout.addWidget(showAnswerEase3_box)
        showAnswerColors_layout.addWidget(showAnswerEase4_box)
        self.showAnswerColors_box = QGroupBox()
        self.showAnswerColors_box.setLayout(showAnswerColors_layout)
        def showAnswerType_signal():
            self.showAnswerColors_box.setEnabled(True)
            if self.showAnswerBorderColor_style.currentIndex() == 0:
                self.showAnswerColors_box.setDisabled(True)
        showAnswerType_signal()
        self.showAnswerBorderColor_style.currentIndexChanged.connect(showAnswerType_signal)
        layout = QVBoxLayout()
        layout.addWidget(self.custom_reviewButtonColors)
        layout.addLayout(reviewButtonTextColor_activeIndicatorColor_line)
        layout.addLayout(bottobarButtonTextColor_bottombarButtonBorderColor_line)
        layout.addWidget(self.showAnswerColors_box)
        layout.addStretch()
        layout_holder = QWidget()
        layout_holder.setLayout(layout)
        self.tab7 = QScrollArea()
        #// I use this part to control the initial settings menu width -_-
        self.tab7.setFixedWidth(690)
        self.tab7.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.tab7.setWidgetResizable(True)
        self.tab7.setWidget(layout_holder)

    def createEighthTab(self):
        begin = self.begin
        end = self.end
        images = self.images
        overViewStats_label = QLabel("More Overview Stats:")
        overViewStats_label.setToolTip("{0}Shows number of new, learn and review cards for today and\
        tomorrow and show total number of new, review, learn, buried and suspended cards on deck overview\
        if enabled.{1}".format(begin, end))
        overViewStats_label.setFixedWidth(180)
        self.overViewStats = QComboBox()
        self.overViewStats.addItems(["Stock", "Stock-ish", "Detailed"])
        self.overViewStats.setFixedWidth(150)
        overViewStats_holder = QHBoxLayout()
        overViewStats_holder.addWidget(overViewStats_label)
        overViewStats_holder.addWidget(self.overViewStats)
        overViewStats_holder.addStretch()
        settingsMenuPlace_label = QLabel("Settings Menu Placement:")
        settingsMenuPlace_label.setToolTip("{0}Changes the position of settings menu.{1}".format(begin, end))
        settingsMenuPlace_label.setFixedWidth(180)
        self.settingsMenu_place = QComboBox()
        self.settingsMenu_place.addItems(["Main Toolbar", "Tools Menu"])
        self.settingsMenu_place.setFixedWidth(150)
        settingsMenuPlace_holder = QHBoxLayout()
        settingsMenuPlace_holder.addWidget(settingsMenuPlace_label)
        settingsMenuPlace_holder.addWidget(self.settingsMenu_place)
        settingsMenuPlace_holder.addStretch()
        skipMethod_label = QLabel("Skip Method:")
        skipMethod_label.setToolTip("{0}Changes Skip method.\n\"Next Card\" just skips the card and the skipped cards will be shown again randomly\
        while \"Bury\" buries the skipped cards and the skipped cards will get unburied when you finish reviewing normal cards. You\
        can manually unbury skipped cards by pressing the \"Show Skipped\" button or by pressing the shortcut key that you've chosen for the button.{1}".format(begin, end))
        skipMethod_label.setFixedWidth(180)
        self.skipMethod = QComboBox()
        self.skipMethod.addItems(["Next Card", "Bury"])
        self.skipMethod.setFixedWidth(150)
        skipMethod_holder = QHBoxLayout()
        skipMethod_holder.addWidget(skipMethod_label)
        skipMethod_holder.addWidget(self.skipMethod)
        skipMethod_holder.addStretch()
        skipMethod_box = QVBoxLayout()
        skipMethod_box.addLayout(overViewStats_holder)
        skipMethod_box.addLayout(settingsMenuPlace_holder)
        skipMethod_box.addLayout(skipMethod_holder)
        general_box = QGroupBox()
        general_box.setLayout(skipMethod_box)
        buttonColors_label = QLabel("Button Styling:")
        buttonColors_label.setToolTip("{0} Enables and disables review buttons styling.<hr> If you use\
        any other add-on to change review button styles, turn this off and you can\
        use other functions of this add-on without using this add-on to change\
        review button stylings.<hr> This should be enabled for options Review Button\
        Background Shadow, Button Style, Change Style, Review Active Button Indicator\
        and Review Buttons Width to work.<hr> <font color=red># NOTE:</font> If you disable this feature\
        hiding review buttons will also stop working.{1}".format(begin, end, images))
        buttonColors_label.setFixedWidth(180)
        self.buttonColors_on = QRadioButton("On")
        self.buttonColors_on.setToolTip("{0} Enabled -> Buttons are styled by this\
        add-on. <br><img src='{2}/buttonColors_on.png'>{1}".format(begin, end, images))
        self.buttonColors_on.setFixedWidth(90)
        self.buttonColors_off = QRadioButton("Off")
        self.buttonColors_off.setToolTip("{0} Disabled ->  Buttons are\
        not styled by this add-on and since there is no other add-on styling them,\
        they are in default mode.<hr><img src='{2}/buttonColors_off.png'>{1}".format(begin, end, images))
        self.buttonColors_off.setFixedWidth(90)
        buttonColors_holder = QHBoxLayout()
        buttonColors_holder.addWidget(buttonColors_label)
        buttonColors_holder.addWidget(self.buttonColors_on)
        buttonColors_holder.addWidget(self.buttonColors_off)
        buttonColors_holder.addStretch()
        buttonColors_box = QGroupBox()
        buttonColors_box.setLayout(buttonColors_holder)
        configEdit_label = QLabel("Direct Config Edit:")
        configEdit_label.setToolTip("{0} Enables direct config editor.\
        If you enable this option, clicking on \"Config\" in add-ons window\
        won't open ARBb settings window and will open the config editor instead.{1}".format(begin, end))
        configEdit_label.setFixedWidth(180)
        self.configEdit_on = QRadioButton("On")
        self.configEdit_on.setFixedWidth(90)
        self.configEdit_off = QRadioButton("Off")
        self.configEdit_off.setFixedWidth(90)
        configEdit_holder = QHBoxLayout()
        configEdit_holder.addWidget(configEdit_label)
        configEdit_holder.addWidget(self.configEdit_on)
        configEdit_holder.addWidget(self.configEdit_off)
        configEdit_holder.addStretch()
        configEdit_box = QGroupBox()
        configEdit_box.setLayout(configEdit_holder)

        hideEasyIfNotLearning_label = QLabel("Hide Easy if not in Learning:")
        hideEasyIfNotLearning_label.setToolTip("{0} Hides the \"Easy\" Button if the \
        card is not in learning phase.{1}".format(begin, end))
        hideEasyIfNotLearning_label.setFixedWidth(180)
        self.hideEasyIfNotLearning_on = QRadioButton("On")
        self.hideEasyIfNotLearning_on.setFixedWidth(90)
        self.hideEasyIfNotLearning_off = QRadioButton("Off")
        self.hideEasyIfNotLearning_off.setFixedWidth(90)
        hideEasyIfNotLearning_holder = QHBoxLayout()
        hideEasyIfNotLearning_holder.addWidget(hideEasyIfNotLearning_label)
        hideEasyIfNotLearning_holder.addWidget(self.hideEasyIfNotLearning_on)
        hideEasyIfNotLearning_holder.addWidget(self.hideEasyIfNotLearning_off)
        hideEasyIfNotLearning_holder.addStretch()
        hideEasyIfNotLearning_box = QGroupBox()
        hideEasyIfNotLearning_box.setLayout(hideEasyIfNotLearning_holder)

        ADDONS_ITEM_WIDTH = 180
        self.addOn_speedFocus = QCheckBox("Speed Focus")
        self.addOn_speedFocus.setToolTip("{0} Removes the conflict with speed focus add-on so you can\
        use this add-on on speed focus add-on at the same time without having issues.<hr>\
        Don't forget to disable this option when you don't want to use speed focus add-on,\
        otherwise this add-on will automatically reveal the answer after the time\
        you set on speed focus add-on is passed.<hr> DON'T ENABLE THIS IF YOU DON'T\
        HAVE SPEED FOCUS ADD-ON. {1}".format(begin, end))
        self.addOn_speedFocus.setFixedWidth(ADDONS_ITEM_WIDTH)
        self.addOn_rebuildEmptyAll = QCheckBox("Rebuild/Empty All")
        self.addOn_rebuildEmptyAll.setToolTip("{0}Adds buttons for\
        \"rebuild/empty some or all filtered decks\" add-on to the bottombar.{1}".format(begin, end))
        self.addOn_rebuildEmptyAll.setFixedWidth(ADDONS_ITEM_WIDTH)
        addOns_line1 = QHBoxLayout()
        addOns_line1.addWidget(self.addOn_speedFocus)
        addOns_line1.addWidget(self.addOn_rebuildEmptyAll)
        addOns_line1.addStretch()
        addOns_line2 = QHBoxLayout()
        addOns_layout = QVBoxLayout()
        addOns_layout.addLayout(addOns_line1)
        addOns_box = QGroupBox()
        addOns_box.setLayout(addOns_layout)

        layout = QVBoxLayout()
        layout.addWidget(general_box)
        layout.addWidget(buttonColors_box)
        layout.addWidget(configEdit_box)
        layout.addWidget(hideEasyIfNotLearning_box)
        layout.addWidget(addOns_box)
        layout.addStretch()
        layout_holder = QWidget()
        layout_holder.setLayout(layout)
        self.tab8 = QScrollArea()
        self.tab8.setFixedWidth(690)
        self.tab8.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.tab8.setWidgetResizable(True)
        self.tab8.setWidget(layout_holder)
        self.tab1.setDisabled(True)
        if self.buttonColors_on.isChecked():
            self.tab1.setEnabled(True)
        self.buttonColors_on.toggled.connect(self.tab1.setEnabled)

    def createNinthTab(self):
        begin = self.begin
        end = self.end
        images = self.images
        about_text = """
        <div class="None">
          <font color="tomato">Don't know what each option does?<br></font>
          hover over the title and you'll see a brief description about that option <br><br>

          <font color="tomato">Wanna see what each design is like without having to restart anki?<br></font>
          by hovering over options in front of titles, if the option is related to styling buttons<br>
          or changing how something looks like, you'll see pictures showing you what each option looks like<br>
          Hovering over them won't show you the animations, if the buttons are animated<br><br><br>

          <font color="tomato">Have an idea for a new feature?<br></font>
          Feel free to tell me in comment section on <a href="https://ankiweb.net/shared/info/1136455830">Add-ons Page</a> or <a href="mailto:mamad.jj98@gmail.com">Email me</a><br><br>

          <font color="tomato">Saw a cool button design somewhere?<br></font>
          send me a link to where you saw that design, i'll try to replicate that design<br>
          and put it on the add-on as and option for you to choose<br>
          <a href="https://ankiweb.net/shared/info/1136455830">Add-ons Page</a> or <a href="mailto:mamad.jj98@gmail.com">my Email</a><br><br>

          <font color="tomato">Encountered a bug or some part is not acting how it's supposed to?<br></font>
          Tell me what your settings were on add-on, what's your anki version or if anki showed you an error log,<br>
          copy the error log and comment it on <a href="https://ankiweb.net/shared/info/1136455830">Add-ons Page</a> or <a href="mailto:mamad.jj98@gmail.com">Email me</a> <br>
          (the more information you give me,<br>
          the sooner i find out what's causing the problem and i fix the bug)<br><br>

          <font color="tomato">Like the add-on?<br></font>
          Give it a like on <a href="https://ankiweb.net/shared/review/1136455830">Add-ons Page</a>
        </div>
        """
        about = QLabel()
        about.setText(about_text)
        about.setOpenExternalLinks(True)
        about_scroll = QScrollArea()
        about_scroll.setWidget(about)
        changeLog_window = QDialog()
        changeLog_window.setWindowFlags(Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowMaximizeButtonHint | Qt.WindowType.WindowMinimizeButtonHint)
        changeLog_window.setWindowTitle("Changelog")
        changeLog_window.setWindowIcon(QIcon(images + "\icon.png"))
        changeLog_button = QPushButton("Show Changelog")
        self.changeLog_webView = QWebEngineView()
        self.loadChangeLog()
        changeLog_layout = QVBoxLayout()
        changeLog_layout.addWidget(self.changeLog_webView)
        changeLog_window.setLayout(changeLog_layout)
        changeLog_button.clicked.connect(lambda: changeLog_window.exec())
        layout = QVBoxLayout()
        layout.addWidget(about_scroll)
        layout.addWidget(changeLog_button)
        layout_holder = QWidget()
        layout_holder.setLayout(layout)
        self.tab9 = QScrollArea()
        self.tab9.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.tab9.setWidgetResizable(True)
        self.tab9.setWidget(layout_holder)

    def loadChangeLog(self):
        #// For some weird reason, using dirname(__file__) inside the .format() thingy doesn't seem to be working on macOS
        #// Can't confirm tho -_- since I can't test my add-on on Mac
        addon_path = dirname(__file__)
        file = "{}/changelog.html".format(addon_path)
        with open(file, 'r') as f:
            html = f.read()
            self.changeLog_webView.setHtml(html)

    def loadCurrent(self):
        self.button_style.setCurrentIndex(C_button_style)
        self.bottombarButtons_style.setCurrentIndex(C_bottombarButtons_style)
        self.hover_effect.setCurrentIndex(C_hover_effect)
        self.active_indicator.setCurrentIndex(C_active_indicator)
        self.cursor_style.setCurrentIndex(C_cursor_style)
        self.interval_style.setCurrentIndex(C_interval_style)
        self.buttonFontWeight.setCurrentIndex(C_buttonFontWeight)
        self.showAnswerBorderColor_style.setCurrentIndex(C_showAnswerBorderColor_style)
        self.buttonTransition_time.setValue(int(C_buttonTransition_time))
        self.buttonBorderRadius.setValue(int(C_buttonBorderRadius))
        self.wideButtonPercent.setValue(int(C_wideButton_percent))
        if C_style_mainScreenButtons:
            self.style_mainScreenButtons.setChecked(True)
        if C_reviewTooltip:
            self.reviewTooltip_on.setChecked(True)
        else:
            self.reviewTooltip_off.setChecked(True)
        self.reviewTooltip_style.setCurrentIndex(C_reviewTooltip_style)
        self.reviewTooltip_timer.setValue(int(C_reviewTooltip_timer))
        self.changeButtonColor(self.reviewTooltipTextColor_button, C_reviewTooltipText_color)
        self.reviewTooltipPositionX.setValue(int(C_reviewTooltip_position[0]))
        self.reviewTooltipPositionY.setValue(int(C_reviewTooltip_position[1]))
        self.reviewTooltipOffsetX.setValue(int(C_reviewTooltip_offset[0]))
        self.reviewTooltipOffsetY.setValue(int(C_reviewTooltip_offset[1]))

        if C_info:
            self.info.setChecked(True)
        if C_skip:
            self.skip.setChecked(True)
        if C_showSkipped:
            self.showSkipped.setChecked(True)
        if C_undo:
            self.undo.setChecked(True)
        if C_hideHard:
            self.hideHard.setChecked(True)
        if C_hideGood:
            self.hideGood.setChecked(True)
        if C_hideEasy:
            self.hideEasy.setChecked(True)
        if C_right_info:
            self.right_info.setChecked(True)
        elif C_middleRight_info:
            self.middleRight_info.setChecked(True)
        elif C_middleLeft_info:
            self.middleLeft_info.setChecked(True)
        else:
            self.left_info.setChecked(True)
        if C_right_skip:
            self.right_skip.setChecked(True)
        elif C_middleRight_skip:
            self.middleRight_skip.setChecked(True)
        elif C_middleLeft_skip:
            self.middleLeft_skip.setChecked(True)
        else:
            self.left_skip.setChecked(True)
        if C_right_showSkipped:
            self.right_showSkipped.setChecked(True)
        elif C_middleRight_showSkipped:
            self.middleRight_showSkipped.setChecked(True)
        elif C_middleLeft_showSkipped:
            self.middleLeft_showSkipped.setChecked(True)
        else:
            self.left_showSkipped.setChecked(True)
        if C_right_undo:
            self.right_undo.setChecked(True)
        elif C_middleRight_undo:
            self.middleRight_undo.setChecked(True)
        elif C_middleLeft_undo:
            self.middleLeft_undo.setChecked(True)
        else:
            self.left_undo.setChecked(True)
        self.infoShortcut_button.setText("Change Shortcut (Current: {})".format(C_info_shortcut))
        self.skipShortcut_button.setText("Change Shortcut (Current: {})".format(C_skip_shortcut))
        self.showSkippedShortcut_button.setText("Change Shortcut (Current: {})".format(C_showSkipped_shortcut))
        self.undoShortcut_button.setText("Change Shortcut (Current: {})".format(C_undo_shortcut))
        if C_custom_sizes:
            self.customSizes_on.setChecked(True)
        else:
            self.customSizes_off.setChecked(True)
        self.text_size.setValue(int(C_text_size))
        self.buttons_height.setValue(int(C_buttons_height))
        self.reviewButtons_width.setValue(int(C_reviewButtons_width))
        self.edit_width.setValue(int(C_edit_width))
        self.answer_width.setValue(int(C_answer_width))
        self.more_width.setValue(int(C_more_width))
        self.info_width.setValue(int(C_info_width))
        self.skip_width.setValue(int(C_skip_width))
        self.showSkipped_width.setValue(int(C_showSkipped_width))
        self.undo_width.setValue(int(C_undo_width))
        self.buttonLabel_studyNow.setText(C_buttonLabel_studyNow)
        self.buttonLabel_edit.setText(C_buttonLabel_edit)
        self.buttonLabel_showAnswer.setText(C_buttonLabel_showAnswer)
        self.buttonLabel_more.setText(C_buttonLabel_more)
        self.buttonLabel_info.setText(C_buttonLabel_info)
        self.buttonLabel_skip.setText(C_buttonLabel_skip)
        self.buttonLabel_showSkipped.setText(C_buttonLabel_showSkipped)
        self.buttonLabel_undo.setText(C_buttonLabel_undo)
        self.buttonLabel_again.setText(C_buttonLabel_again)
        self.buttonLabel_hard.setText(C_buttonLabel_hard)
        self.buttonLabel_good.setText(C_buttonLabel_good)
        self.buttonLabel_easy.setText(C_buttonLabel_easy)
        self.sidebar_theme.setCurrentIndex(C_sidebar_theme)
        self.sidebar_font.setCurrentFont(QFont(C_sidebar_font))
        self.sidebar_hideCurrentCard.setCurrentIndex(C_sidebar_hideCurrentCard)
        self.sidebar_PreviousCards.setValue(int(C_sidebar_PreviousCards))
        self.sidebar_reviewsToShow.setValue(int(C_sidebar_reviewsToShow))
        if C_sidebar_currentReviewCount:
            self.sidebar_currentReviewCount.setChecked(True)
        if C_sidebar_dateCreated:
            self.sidebar_dateCreated.setChecked(True)
        if C_sidebar_dateEdited:
            self.sidebar_dateEdited.setChecked(True)
        if C_sidebar_firstReview:
            self.sidebar_firstReview.setChecked(True)
        if C_sidebar_latestReview:
            self.sidebar_latestReview.setChecked(True)
        if C_sidebar_due:
            self.sidebar_due.setChecked(True)
        if C_sidebar_interval:
            self.sidebar_interval.setChecked(True)
        if C_sidebar_ease:
            self.sidebar_ease.setChecked(True)
        if C_sidebar_numberOfReviews:
            self.sidebar_numberOfReviews.setChecked(True)
        if C_sidebar_lapses:
            self.sidebar_lapses.setChecked(True)
        if C_sidebar_averageTime:
            self.sidebar_averageTime.setChecked(True)
        if C_sidebar_totalTime:
            self.sidebar_totalTime.setChecked(True)
        if C_sidebar_cardType:
            self.sidebar_cardType.setChecked(True)
        if C_sidebar_noteType:
            self.sidebar_noteType.setChecked(True)
        if C_sidebar_deck:
            self.sidebar_deck.setChecked(True)
        if C_sidebar_tags:
            self.sidebar_tags.setChecked(True)
        if C_sidebar_sortField:
            self.sidebar_sortField.setChecked(True)
        if C_sidebar_warningNote:
            self.sidebar_warningNote.setChecked(True)
        if C_infobar_correctPercent:
            self.sidebar_correctPercent.setChecked(True)
        if C_infobar_fastestReview:
            self.sidebar_fastestReview.setChecked(True)
        if C_infobar_slowestReview:
            self.sidebar_slowestReview.setChecked(True)
        if C_infobar_noteID:
            self.sidebar_noteID.setChecked(True)
        if C_infobar_cardID:
            self.sidebar_cardID.setChecked(True)
        if C_sidebar_autoOpen:
            self.sidebar_autoOpen.setChecked(True)
        if C_custom_reviewButtonColors:
            self.custom_reviewButtonColors.setChecked(True)
        if C_custom_reviewButtonTextColor:
            self.custom_reviewButtonTextColor.setChecked(True)
        if C_custom_activeIndicatorColor:
            self.custom_activeIndicatorColor.setChecked(True)
        if C_custom_bottombarButtonTextColor:
            self.custom_bottombarButtonTextColor.setChecked(True)
        if C_custom_bottombarButtonBorderColor:
            self.custom_bottombarButtonBorderColor.setChecked(True)
        self.changeButtonColor(self.reviewButtonTextColor_button, C_reviewButtonText_color)
        self.changeButtonColor(self.activeIndicatorColor_button, C_activeIndicator_color)
        self.changeButtonColor(self.bottombarButtonTextColor_button, C_bottombarButtonText_color)
        self.changeButtonColor(self.bottombarButtonBorderColor_button, C_bottombarButtonBorder_color)
        self.changeButtonColor(self.againColor_button, C_again_color)
        self.changeButtonColor(self.againHoverColor_button, C_againHover_color)
        self.changeButtonColor(self.hardColor_button, C_hard_color)
        self.changeButtonColor(self.hardHoverColor_button, C_hardHover_color)
        self.changeButtonColor(self.goodColor_button, C_good_color)
        self.changeButtonColor(self.goodHoverColor_button, C_goodHover_color)
        self.changeButtonColor(self.easyColor_button, C_easy_color)
        self.changeButtonColor(self.easyHoverColor_button, C_easyHover_color)
        self.showAnswerEase1.setValue(int(C_showAnswerEase1))
        self.showAnswerEase2.setValue(int(C_showAnswerEase2))
        self.showAnswerEase3.setValue(int(C_showAnswerEase3))
        self.showAnswerEase4.setValue(int(C_showAnswerEase4))
        self.changeButtonColor(self.showAnswerEase1_button, C_showAnswerEase1_color)
        self.changeButtonColor(self.showAnswerEase2_button, C_showAnswerEase2_color)
        self.changeButtonColor(self.showAnswerEase3_button, C_showAnswerEase3_color)
        self.changeButtonColor(self.showAnswerEase4_button, C_showAnswerEase4_color)
        if C_button_colors:
            self.buttonColors_on.setChecked(True)
        else:
            self.buttonColors_off.setChecked(True)
        if C_configEdit:
            self.configEdit_on.setChecked(True)
        else:
            self.configEdit_off.setChecked(True)
        if C_hideEasyIfNotLearning:
            self.hideEasyIfNotLearning_on.setChecked(True)
        else:
            self.hideEasyIfNotLearning_off.setChecked(True)
        if C_addOn_speedFocus:
            self.addOn_speedFocus.setChecked(True)
        if C_addOn_rebuildEmptyAll:
            self.addOn_rebuildEmptyAll.setChecked(True)
        self.overViewStats.setCurrentIndex(C_overViewStats)
        self.settingsMenu_place.setCurrentIndex(C_settingsMenu_palce)
        self.skipMethod.setCurrentIndex(C_skipMethod)

    def onLoadSettings(self):
        addon_path = dirname(__file__)
        #// Open a file browser to choose the settings file (returns a tuple) the first item in the tuple is the settings file location
        fileName_tuple = QFileDialog.getOpenFileName(self, 'Open file', r'{}\user_files'.format(addon_path))
        #// If user cancels the operation and no file is chosen, then return without doing anything
        if not fileName_tuple[0]:
            return
        #// Select the settings file from the tuple
        settingsFile = fileName_tuple[0]
        #// Open and read the JSON File
        settings = open("{}".format(settingsFile), "r")
        conf = json.load(settings)
        settingsFile_name = os.path.basename(settingsFile)
        load = askUser("Replace current settings with settings file <{}>?".format(settingsFile_name), self, None, defaultno=True, title="Advanced Review Bottombar")
        if load:
            mw.addonManager.writeConfig(__name__, conf)
            showInfo("<div style='font-size: 15px;'>Settings Loaded Successfully.\
            </div><div style='color: red; font-size: 15px;'> Changes will take \
            effect after you restart anki.</div>", title="Advanced Review Bottombar Settings")
            self.close()
            refreshConfig()
        else:
            return
        settings.close()

    def onSaveSettings(self):
        addon_path = dirname(__file__)
        #// Choose a name for the backup file
        file_name = "ARBb {}".format(datetime.now().strftime("%d-%b-%Y %H-%M-%S"))
        path_to_file = "{}\\user_files\\{}.json".format(addon_path, file_name)
        f = open(path_to_file, "w")

        if self.left_skip.isChecked():
            skip_position = "left"
        elif self.middleRight_skip.isChecked():
            skip_position ="middle right"
        elif self.right_skip.isChecked():
            skip_position ="right"
        else:
            skip_position = "middle left"
        if self.left_showSkipped.isChecked():
            showSkipped_position = "left"
        elif self.middleRight_showSkipped.isChecked():
            showSkipped_position ="middle right"
        elif self.right_showSkipped.isChecked():
            showSkipped_position ="right"
        else:
            showSkipped_position = "middle left"
        if self.middleLeft_info.isChecked():
            info_position = "middle left"
        elif self.middleRight_info.isChecked():
            info_position = "middle right"
        elif self.right_info.isChecked():
            info_position = "right"
        else:
            info_position = "left"
        if self.left_undo.isChecked():
            undo_position = "left"
        elif self.middleLeft_undo.isChecked():
            undo_position = "middle left"
        elif self.right_undo.isChecked():
            undo_position = "right"
        else:
            undo_position = "middle right"
        if self.showAnswerEase1.value() > self.showAnswerEase2.value():
            self.showAnswerEase2.setValue((self.showAnswerEase1.value() + 50))
        if self.showAnswerEase2.value() > self.showAnswerEase3.value():
            self.showAnswerEase3.setValue((self.showAnswerEase2.value() + 50))
        if self.showAnswerEase3.value() > self.showAnswerEase4.value():
            self.showAnswerEase4.setValue((self.showAnswerEase3.value() + 50))

        conf = {
        "  Button Colors": self.buttonColors_on.isChecked(),
        "  Speed Focus Add-on": self.addOn_speedFocus.isChecked(),
        "  Rebuild Empty All Add-on": self.addOn_rebuildEmptyAll.isChecked(),
        "  Direct Config Edit": self.configEdit_on.isChecked(),
        "  Hide Easy if not in Learning": self.hideEasyIfNotLearning_on.isChecked(),
        "  More Overview Stats": self.overViewStats.currentIndex(),
        "  Settings Menu Place": self.settingsMenu_place.currentIndex(),
        "  Skip Method": self.skipMethod.currentIndex(),
        "  Style Main Screen Buttons": self.style_mainScreenButtons.isChecked(),
        " Review_ Active Button Indicator": self.active_indicator.currentIndex(),
        " Review_ Buttons Style": self.button_style.currentIndex(),
        " Review_ Hover Effect": self.hover_effect.currentIndex(),
        " Review_ Custom Colors": self.custom_reviewButtonColors.isChecked(),
        " Review_ Custom Review Button Text Color": self.custom_reviewButtonTextColor.isChecked(),
        " Review_ Custom Active Indicator Color": self.custom_activeIndicatorColor.isChecked(),
        " Review_ Bottombar Buttons Style": self.bottombarButtons_style.currentIndex(),
        " Review_ Cursor Style": self.cursor_style.currentIndex(),
        " Review_ Interval Style": self.interval_style.currentIndex(),
        " Review_ Button Transition Time": self.buttonTransition_time.value(),
        " Review_ Button Border Radius": self.buttonBorderRadius.value(),
        " Review_ Wide Button Percent": self.wideButtonPercent.value(),
        "Button_   Info Button": self.info.isChecked(),
        "Button_   Skip Button": self.skip.isChecked(),
        "Button_   Show Skipped Button": self.showSkipped.isChecked(),
        "Button_   Undo Button": self.undo.isChecked(),
        "Button_   Hide Hard": self.hideHard.isChecked(),
        "Button_   Hide Good": self.hideGood.isChecked(),
        "Button_   Hide Easy": self.hideEasy.isChecked(),
        "Button_  Custom Button Sizes": self.customSizes_on.isChecked(),
        "Button_ Shortcut_ Skip Button": self.skip_shortcut,
        "Button_ Shortcut_ Show Skipped Button": self.showSkipped_shortcut,
        "Button_ Shortcut_ Info Button": self.info_shortcut,
        "Button_ Shortcut_ Undo Button": self.undo_shortcut,
        "Button_ Position_ Info Button": info_position,
        "Button_ Position_ Skip Button": skip_position,
        "Button_ Position_ Show Skipped Button": showSkipped_position,
        "Button_ Position_ Undo Button": undo_position,
        "Button_ Text Size": self.text_size.value(),
        "Button_ Font Weight": self.buttonFontWeight.currentIndex(),
        "Button_ Height_ All Bottombar Buttons": self.buttons_height.value(),
        "Button_ Width_ Edit Button": self.edit_width.value(),
        "Button_ Width_ Show Answer Button": self.answer_width.value(),
        "Button_ Width_ Info Button": self.info_width.value(),
        "Button_ Width_ Skip Button": self.skip_width.value(),
        "Button_ Width_ Show Skipped Button": self.showSkipped_width.value(),
        "Button_ Width_ More Button": self.more_width.value(),
        "Button_ Width_ Review Buttons": self.reviewButtons_width.value(),
        "Button_ Width_ Undo Button": self.undo_width.value(),
        "Button Label_ Study Now": self.buttonLabel_studyNow.text(),
        "Button Label_ Edit": self.buttonLabel_edit.text(),
        "Button Label_ Show Answer": self.buttonLabel_showAnswer.text(),
        "Button Label_ More": self.buttonLabel_more.text(),
        "Button Label_ Info": self.buttonLabel_info.text(),
        "Button Label_ Skip": self.buttonLabel_skip.text(),
        "Button Label_ Show Skipped": self.buttonLabel_showSkipped.text(),
        "Button Label_ Undo": self.buttonLabel_undo.text(),
        "Button Label_ Again": self.buttonLabel_again.text(),
        "Button Label_ Hard": self.buttonLabel_hard.text(),
        "Button Label_ Good": self.buttonLabel_good.text(),
        "Button Label_ Easy": self.buttonLabel_easy.text(),
        "Card Info sidebar_ Hide Current Card": self.sidebar_hideCurrentCard.currentIndex(),
        "Card Info sidebar_ Number of previous cards to show": self.sidebar_PreviousCards.value(),
        "Card Info sidebar_ theme": self.sidebar_theme.currentIndex(),
        "Card Info sidebar_ Created": self.sidebar_dateCreated.isChecked(),
        "Card Info sidebar_ Edited": self.sidebar_dateEdited.isChecked(),
        "Card Info sidebar_ First Review": self.sidebar_firstReview.isChecked(),
        "Card Info sidebar_ Latest Review": self.sidebar_latestReview.isChecked(),
        "Card Info sidebar_ Due": self.sidebar_due.isChecked(),
        "Card Info sidebar_ Interval": self.sidebar_interval.isChecked(),
        "Card Info sidebar_ Ease": self.sidebar_ease.isChecked(),
        "Card Info sidebar_ Reviews": self.sidebar_numberOfReviews.isChecked(),
        "Card Info sidebar_ Lapses": self.sidebar_lapses.isChecked(),
		"Card Info Sidebar_ Correct Percent": self.sidebar_correctPercent.isChecked(),
		"Card Info Sidebar_ Fastest Review": self.sidebar_fastestReview.isChecked(),
		"Card Info Sidebar_ Slowest Review": self.sidebar_slowestReview.isChecked(),
        "Card Info sidebar_ Average Time": self.sidebar_averageTime.isChecked(),
        "Card Info sidebar_ Total Time": self.sidebar_totalTime.isChecked(),
        "Card Info sidebar_ Card Type": self.sidebar_cardType.isChecked(),
        "Card Info sidebar_ Note Type": self.sidebar_noteType.isChecked(),
        "Card Info sidebar_ Deck": self.sidebar_deck.isChecked(),
        "Card Info sidebar_ Tags": self.sidebar_tags.isChecked(),
		"Card Info Sidebar_ Note ID": self.sidebar_noteID.isChecked(),
		"Card Info Sidebar_ Card ID": self.sidebar_cardID.isChecked(),
        "Card Info sidebar_ Sort Field": self.sidebar_sortField.isChecked(),
        "Card Info sidebar_ Current Review Count": self.sidebar_currentReviewCount.isChecked(),
        "Card Info sidebar_ Font": self.sidebar_font.currentFont().family(),
        "Card Info sidebar_ number of reviews to show for a card": self.sidebar_reviewsToShow.value(),
        "Card Info sidebar_ Auto Open": self.sidebar_autoOpen.isChecked(),
        "Card Info sidebar_ warning note": self.sidebar_warningNote.isChecked(),
        "Color_  General Text Color": self.reviewButtonText_color,
        "Color_ Active Button Indicator": self.activeIndicator_color,
    	"Color_ Bottombar Button Text Color": self.bottombarButtonText_color,
    	"Color_ Bottombar Button Border Color": self.bottombarButtonBorder_color,
    	"Color_ Custom Bottombar Button Text Color": self.custom_bottombarButtonTextColor.isChecked(),
    	"Color_ Custom Bottombar Button Border Color": self.custom_bottombarButtonBorderColor.isChecked(),
        "Color_ Again": self.again_color,
        "Color_ Again on hover": self.againHover_color,
        "Color_ Hard": self.hard_color,
        "Color_ Hard on hover": self.hardHover_color,
        "Color_ Good":self.good_color,
        "Color_ Good on hover": self.goodHover_color,
        "Color_ Easy": self.easy_color,
        "Color_ Easy on hover": self.easyHover_color,
        "Tooltip": self.reviewTooltip_on.isChecked(),
        "Tooltip Timer": self.reviewTooltip_timer.value(),
        "Tooltip Text Color": self.reviewTooltipText_color,
        "Tooltip Style": self.reviewTooltip_style.currentIndex(),
        "Tooltip Position": [self.reviewTooltipPositionX.value(), self.reviewTooltipPositionY.value()],
        "Tooltip Offset": [self.reviewTooltipOffsetX.value(), self.reviewTooltipOffsetY.value()],
        "ShowAnswer_ Border Color Style": self.showAnswerBorderColor_style.currentIndex(),
		"ShowAnswer_ Ease1": self.showAnswerEase1.value(),
		"ShowAnswer_ Ease2": self.showAnswerEase2.value(),
		"ShowAnswer_ Ease3": self.showAnswerEase3.value(),
		"ShowAnswer_ Ease4": self.showAnswerEase4.value(),
		"ShowAnswer_ Ease1 Color": self.showAnswerEase1_color,
		"ShowAnswer_ Ease2 Color": self.showAnswerEase2_color,
		"ShowAnswer_ Ease3 Color": self.showAnswerEase3_color,
		"ShowAnswer_ Ease4 Color": self.showAnswerEase4_color
      }
        #// Save settings in a JSON file
        json.dump(conf, f, indent=4)
        #// Open file explorer after saving so users know where the backup file is (and maybe save it somewhere else)
        if is_mac:
            select_method = ['open', '-R']
        else:
            select_method = ['explorer',  '/select,']
        subprocess.Popen(select_method + [path_to_file])
        f.close()

    def onApply(self):
        if self.left_skip.isChecked():
            skip_position = "left"
        elif self.middleRight_skip.isChecked():
            skip_position ="middle right"
        elif self.right_skip.isChecked():
            skip_position ="right"
        else:
            skip_position = "middle left"
        if self.left_showSkipped.isChecked():
            showSkipped_position = "left"
        elif self.middleRight_showSkipped.isChecked():
            showSkipped_position ="middle right"
        elif self.right_showSkipped.isChecked():
            showSkipped_position ="right"
        else:
            showSkipped_position = "middle left"
        if self.middleLeft_info.isChecked():
            info_position = "middle left"
        elif self.middleRight_info.isChecked():
            info_position = "middle right"
        elif self.right_info.isChecked():
            info_position = "right"
        else:
            info_position = "left"
        if self.left_undo.isChecked():
            undo_position = "left"
        elif self.middleLeft_undo.isChecked():
            undo_position = "middle left"
        elif self.right_undo.isChecked():
            undo_position = "right"
        else:
            undo_position = "middle right"
        if self.showAnswerEase1.value() > self.showAnswerEase2.value():
            self.showAnswerEase2.setValue((self.showAnswerEase1.value() + 50))
        if self.showAnswerEase2.value() > self.showAnswerEase3.value():
            self.showAnswerEase3.setValue((self.showAnswerEase2.value() + 50))
        if self.showAnswerEase3.value() > self.showAnswerEase4.value():
            self.showAnswerEase4.setValue((self.showAnswerEase3.value() + 50))

        conf = {
        "  Button Colors": self.buttonColors_on.isChecked(),
        "  Speed Focus Add-on": self.addOn_speedFocus.isChecked(),
        "  Rebuild Empty All Add-on": self.addOn_rebuildEmptyAll.isChecked(),
        "  Direct Config Edit": self.configEdit_on.isChecked(),
        "  Hide Easy if not in Learning": self.hideEasyIfNotLearning_on.isChecked(),
        "  More Overview Stats": self.overViewStats.currentIndex(),
        "  Settings Menu Place": self.settingsMenu_place.currentIndex(),
        "  Skip Method": self.skipMethod.currentIndex(),
        "  Style Main Screen Buttons": self.style_mainScreenButtons.isChecked(),
        " Review_ Active Button Indicator": self.active_indicator.currentIndex(),
        " Review_ Buttons Style": self.button_style.currentIndex(),
        " Review_ Hover Effect": self.hover_effect.currentIndex(),
        " Review_ Custom Colors": self.custom_reviewButtonColors.isChecked(),
        " Review_ Custom Review Button Text Color": self.custom_reviewButtonTextColor.isChecked(),
        " Review_ Custom Active Indicator Color": self.custom_activeIndicatorColor.isChecked(),
        " Review_ Bottombar Buttons Style": self.bottombarButtons_style.currentIndex(),
        " Review_ Cursor Style": self.cursor_style.currentIndex(),
        " Review_ Interval Style": self.interval_style.currentIndex(),
        " Review_ Button Transition Time": self.buttonTransition_time.value(),
        " Review_ Button Border Radius": self.buttonBorderRadius.value(),
        " Review_ Wide Button Percent": self.wideButtonPercent.value(),
        "Button_   Info Button": self.info.isChecked(),
        "Button_   Skip Button": self.skip.isChecked(),
        "Button_   Show Skipped Button": self.showSkipped.isChecked(),
        "Button_   Undo Button": self.undo.isChecked(),
        "Button_   Hide Hard": self.hideHard.isChecked(),
        "Button_   Hide Good": self.hideGood.isChecked(),
        "Button_   Hide Easy": self.hideEasy.isChecked(),
        "Button_  Custom Button Sizes": self.customSizes_on.isChecked(),
        "Button_ Shortcut_ Skip Button": self.skip_shortcut,
        "Button_ Shortcut_ Show Skipped Button": self.showSkipped_shortcut,
        "Button_ Shortcut_ Info Button": self.info_shortcut,
        "Button_ Shortcut_ Undo Button": self.undo_shortcut,
        "Button_ Position_ Info Button": info_position,
        "Button_ Position_ Skip Button": skip_position,
        "Button_ Position_ Show Skipped Button": showSkipped_position,
        "Button_ Position_ Undo Button": undo_position,
        "Button_ Text Size": self.text_size.value(),
        "Button_ Font Weight": self.buttonFontWeight.currentIndex(),
        "Button_ Height_ All Bottombar Buttons": self.buttons_height.value(),
        "Button_ Width_ Edit Button": self.edit_width.value(),
        "Button_ Width_ Show Answer Button": self.answer_width.value(),
        "Button_ Width_ Info Button": self.info_width.value(),
        "Button_ Width_ Skip Button": self.skip_width.value(),
        "Button_ Width_ Show Skipped Button": self.showSkipped_width.value(),
        "Button_ Width_ More Button": self.more_width.value(),
        "Button_ Width_ Review Buttons": self.reviewButtons_width.value(),
        "Button_ Width_ Undo Button": self.undo_width.value(),
        "Button Label_ Study Now": self.buttonLabel_studyNow.text(),
        "Button Label_ Edit": self.buttonLabel_edit.text(),
        "Button Label_ Show Answer": self.buttonLabel_showAnswer.text(),
        "Button Label_ More": self.buttonLabel_more.text(),
        "Button Label_ Info": self.buttonLabel_info.text(),
        "Button Label_ Skip": self.buttonLabel_skip.text(),
        "Button Label_ Show Skipped": self.buttonLabel_showSkipped.text(),
        "Button Label_ Undo": self.buttonLabel_undo.text(),
        "Button Label_ Again": self.buttonLabel_again.text(),
        "Button Label_ Hard": self.buttonLabel_hard.text(),
        "Button Label_ Good": self.buttonLabel_good.text(),
        "Button Label_ Easy": self.buttonLabel_easy.text(),
        "Card Info sidebar_ Hide Current Card": self.sidebar_hideCurrentCard.currentIndex(),
        "Card Info sidebar_ Number of previous cards to show": self.sidebar_PreviousCards.value(),
        "Card Info sidebar_ theme": self.sidebar_theme.currentIndex(),
        "Card Info sidebar_ Created": self.sidebar_dateCreated.isChecked(),
        "Card Info sidebar_ Edited": self.sidebar_dateEdited.isChecked(),
        "Card Info sidebar_ First Review": self.sidebar_firstReview.isChecked(),
        "Card Info sidebar_ Latest Review": self.sidebar_latestReview.isChecked(),
        "Card Info sidebar_ Due": self.sidebar_due.isChecked(),
        "Card Info sidebar_ Interval": self.sidebar_interval.isChecked(),
        "Card Info sidebar_ Ease": self.sidebar_ease.isChecked(),
        "Card Info sidebar_ Reviews": self.sidebar_numberOfReviews.isChecked(),
        "Card Info sidebar_ Lapses": self.sidebar_lapses.isChecked(),
		"Card Info Sidebar_ Correct Percent": self.sidebar_correctPercent.isChecked(),
		"Card Info Sidebar_ Fastest Review": self.sidebar_fastestReview.isChecked(),
		"Card Info Sidebar_ Slowest Review": self.sidebar_slowestReview.isChecked(),
        "Card Info sidebar_ Average Time": self.sidebar_averageTime.isChecked(),
        "Card Info sidebar_ Total Time": self.sidebar_totalTime.isChecked(),
        "Card Info sidebar_ Card Type": self.sidebar_cardType.isChecked(),
        "Card Info sidebar_ Note Type": self.sidebar_noteType.isChecked(),
        "Card Info sidebar_ Deck": self.sidebar_deck.isChecked(),
        "Card Info sidebar_ Tags": self.sidebar_tags.isChecked(),
		"Card Info Sidebar_ Note ID": self.sidebar_noteID.isChecked(),
		"Card Info Sidebar_ Card ID": self.sidebar_cardID.isChecked(),
        "Card Info sidebar_ Sort Field": self.sidebar_sortField.isChecked(),
        "Card Info sidebar_ Current Review Count": self.sidebar_currentReviewCount.isChecked(),
        "Card Info sidebar_ Font": self.sidebar_font.currentFont().family(),
        "Card Info sidebar_ number of reviews to show for a card": self.sidebar_reviewsToShow.value(),
        "Card Info sidebar_ Auto Open": self.sidebar_autoOpen.isChecked(),
        "Card Info sidebar_ warning note": self.sidebar_warningNote.isChecked(),
        "Color_  General Text Color": self.reviewButtonText_color,
        "Color_ Active Button Indicator": self.activeIndicator_color,
    	"Color_ Bottombar Button Text Color": self.bottombarButtonText_color,
    	"Color_ Bottombar Button Border Color": self.bottombarButtonBorder_color,
    	"Color_ Custom Bottombar Button Text Color": self.custom_bottombarButtonTextColor.isChecked(),
    	"Color_ Custom Bottombar Button Border Color": self.custom_bottombarButtonBorderColor.isChecked(),
        "Color_ Again": self.again_color,
        "Color_ Again on hover": self.againHover_color,
        "Color_ Hard": self.hard_color,
        "Color_ Hard on hover": self.hardHover_color,
        "Color_ Good":self.good_color,
        "Color_ Good on hover": self.goodHover_color,
        "Color_ Easy": self.easy_color,
        "Color_ Easy on hover": self.easyHover_color,
        "Tooltip": self.reviewTooltip_on.isChecked(),
        "Tooltip Timer": self.reviewTooltip_timer.value(),
        "Tooltip Text Color": self.reviewTooltipText_color,
        "Tooltip Style": self.reviewTooltip_style.currentIndex(),
        "Tooltip Position": [self.reviewTooltipPositionX.value(), self.reviewTooltipPositionY.value()],
        "Tooltip Offset": [self.reviewTooltipOffsetX.value(), self.reviewTooltipOffsetY.value()],
        "ShowAnswer_ Border Color Style": self.showAnswerBorderColor_style.currentIndex(),
		"ShowAnswer_ Ease1": self.showAnswerEase1.value(),
		"ShowAnswer_ Ease2": self.showAnswerEase2.value(),
		"ShowAnswer_ Ease3": self.showAnswerEase3.value(),
		"ShowAnswer_ Ease4": self.showAnswerEase4.value(),
		"ShowAnswer_ Ease1 Color": self.showAnswerEase1_color,
		"ShowAnswer_ Ease2 Color": self.showAnswerEase2_color,
		"ShowAnswer_ Ease3 Color": self.showAnswerEase3_color,
		"ShowAnswer_ Ease4 Color": self.showAnswerEase4_color
      }
        mw.addonManager.writeConfig(__name__, conf)
        showInfo("<div style='color: red;\
        font-size: 15px;'> Changes will take effect after you restart anki. </div>\
        <div style='font-size: 15px;'> Sidebar changes will take effect immediately.\
        </div>", title="Advanced Review Bottombar Settings")
        refreshConfig()
        self.close()

    def getNewColor(self, color_variable, color_button):
        color_window = QColorDialog()
        color = color_window.getColor()
        if color.isValid():
            color = color.name()
            if color_variable == "again_color":
                self.again_color = color
            elif color_variable == "againHover_color":
                self.againHover_color = color
            elif color_variable == "hard_color":
                self.hard_color = color
            elif color_variable == "hardHover_color":
                self.hardHover_color = color
            elif color_variable == "good_color":
                self.good_color = color
            elif color_variable == "goodHover_color":
                self.goodHover_color = color
            elif color_variable == "easy_color":
                self.easy_color = color
            elif color_variable == "easyHover_color":
                self.easyHover_color = color
            elif color_variable == "reviewButtonText_color":
                self.reviewButtonText_color = color
            elif color_variable == "activeIndicator_color":
                self.activeIndicator_color = color
            elif color_variable == "reviewTooltipText_color":
                self.reviewTooltipText_color = color
            elif color_variable == "bottombarButtonText_color":
                self.bottombarButtonText_color = color
            elif color_variable == "bottombarButtonBorder_color":
                self.bottombarButtonBorder_color = color
            elif color_variable == "showAnswerEase1":
                self.showAnswerEase1_color = color
            elif color_variable == "showAnswerEase2":
                self.showAnswerEase2_color = color
            elif color_variable == "showAnswerEase3":
                self.showAnswerEase3_color = color
            elif color_variable == "showAnswerEase4":
                self.showAnswerEase4_color = color
            self.changeButtonColor(color_button, color)

    def changeButtonColor(self, button, color):
        pixmap = QPixmap(95, 18)
        qcolour = QColor(0, 0, 0)
        qcolour.setNamedColor(color)
        pixmap.fill(qcolour)
        button.setIcon(QIcon(pixmap))
        button.setIconSize(QSize(95, 18))

    def updateShortcut(self, button_variable, combination=None):
        """Update hotkey label and attribute"""
        if button_variable == "info_shortcut":
            shortcut = combination or self.info_shortcut
            self.infoShortcut_button.setText("Change Shortcut (Current: {})".format(shortcut))
        elif button_variable == "skip_shortcut":
            shortcut = combination or self.skip_shortcut
            self.skipShortcut_button.setText("Change Shortcut (Current: {})".format(shortcut))
        elif button_variable == "showSkipped_shortcut":
            shortcut = combination or self.showSkippedp_shortcut
            self.showSkippedShortcut_button.setText("Change Shortcut (Current: {})".format(shortcut))
        elif button_variable == "undo_shortcut":
            shortcut = combination or self.undo_shortcut
            self.undoShortcut_button.setText("Change Shortcut (Current: {})".format(shortcut))
        else:
            return

        if combination:
            if button_variable == "info_shortcut":
                self.info_shortcut = combination
            elif button_variable == "skip_shortcut":
                self.skip_shortcut = combination
            elif button_variable == "showSkipped_shortcut":
                self.showSkipped_shortcut = combination
            elif button_variable == "undo_shortcut":
                self.undo_shortcut = combination
            else:
                return

    def showGetShortcut(self, button_variable):
        getShortcut = GetShortcut(self, button_variable)
        getShortcut.exec()

def open_settings():
    settings = SettingsMenu()
    #// For styling settings menu -_-
    # settings.setStyle(QStyleFactory.create("Fusion"))
    settings.exec()

def setupMenu():
    settings = QAction('&Advanced Review Bottombar Settings', mw)
    if C_settingsMenu_palce == 1:
        mw.form.menuTools.addAction(settings)
    else:
        mw.ARBB_menu = QMenu('&ARBb', mw)
        mw.ARBB_menu.addAction(settings)
        mw.form.menubar.insertMenu(mw.form.menuHelp.menuAction(), mw.ARBB_menu)
    settings.triggered.connect(open_settings)
    settings.setShortcut(QKeySequence('Shift+A'))
setupMenu()

if not C_configEdit:
    mw.addonManager.setConfigAction(__name__, open_settings)
