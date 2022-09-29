#// auth_ Mohamad Janati
#// Copyright (c) 2019-2021 Mohamad Janati (freaking stupid, right? :|)

from aqt.reviewer import Reviewer
from aqt import mw
from . import styles


#// getting confing information
config = mw.addonManager.getConfig(__name__)
button_style = config[' Review_ Buttons Style']
custom_colors = config[' Review_ Custom Colors']
hide_hard = config['Button_   Hide Hard']
hide_good = config['Button_   Hide Good']
hide_easy = config['Button_   Hide Easy']
custom_buttonSize = config['Button_  Custom Button Sizes']
interval_style = config[' Review_ Interval Style']
if custom_buttonSize:
    buttons_height = config['Button_ Height_ All Bottombar Buttons']
    reviewButtons_width = config['Button_ Width_ Review Buttons']
    text_size = config['Button_ Text Size']
else:
    buttons_height = ""
    reviewButtons_width = ""
    text_size = ""
again_label = config['Button Label_ Again']
hard_label = config['Button Label_ Hard']
good_label = config['Button Label_ Good']
easy_label = config['Button Label_ Easy']

#// getting styles from styles.py
text_color = styles.text_color
again_color = styles.again_color
hard_color = styles.hard_color
good_color = styles.good_color
easy_color = styles.easy_color
background_color = styles.background_color
custom_text = styles.custom_text
custom_background = styles.custom_background
button_styles = styles.button_styles
active_extra = styles.active_extra
neon1 = styles.neon1
neon2 = styles.neon2
fill1 = styles.fill1
fill2 = styles.fill2

def _answerButtonList(self):
    cnt = self.mw.col.sched.answerButtons(self.card)
    if cnt == 2:
        #// button = ((ease, "Label"),)
        again = ((1, " {} ".format(again_label)),)
        good = ((2, " {} ".format(good_label)),)
        buttons = again
        #// don't add button "good" to returned buttons if it's disabled
        if not hide_good:
            buttons += good
        return buttons
    elif cnt == 3:
        again = ((1, " {} ".format(again_label)),)
        good = ((2, " {} ".format(good_label)),)
        easy = ((3, " {} ".format(easy_label)),)
        buttons = again
        if not hide_good:
            buttons += good
        if not hide_easy:
            buttons += easy
        return buttons
    else:
        again = ((1, " {} ".format(again_label)),)
        hard = ((2, " {} ".format(hard_label)),)
        good = ((3, " {} ".format(good_label)),)
        easy = ((4, " {} ".format(easy_label)),)
        buttons = again
        if not hide_hard:
            buttons += hard
        if not hide_good:
            buttons += good
        if not hide_easy:
            buttons += easy
        return buttons


def _answerButtons(self):
    cnt = self.mw.col.sched.answerButtons(self.card)
    default = self._defaultEase()
    def but(i, label):
        #// Setting id name for each button based on their ease value
        if cnt == 2:
            if i == 1:
                button_id = "again"
            elif i == 2:
                button_id = "good"
            else:
                button_id = ""
        elif cnt == 3:
            if i == 1:
                button_id = "again"
            elif i == 2:
                button_id = "good"
            elif i == 3:
                button_id = "easy"
            else:
                button_id = ""
        elif cnt == 4:
            if i == 1:
                button_id = "again"
            elif i == 2:
                button_id = "hard"
            elif i == 3:
                button_id = "good"
            elif i == 4:
                button_id = "easy"
            else:
                button_id = ""
        else:
            if i == 1:
                button_id = "again"
            elif i == 2:
                button_id = "hard"
            elif i == 3:
                button_id = "good"
            elif i == 4:
                button_id = "easy"
            else:
                button_id = ""
        due_plain = self._buttonTime(i)
        inButton_due = ""
        if interval_style == 1:
            if button_id == "again":
                due = "<font color={}>{}</font>".format(again_color, due_plain)
            elif button_id == "hard":
                due = "<font color={}>{}</font>".format(hard_color, due_plain)
            elif button_id == "good":
                due = "<font color={}>{}</font>".format(good_color, due_plain)
            elif button_id == "easy":
                due = "<font color={}>{}</font>".format(easy_color, due_plain)
            else:
                if due_plain:
                    due = due_plain
                else:
                    return
        elif interval_style == 2:
            if due_plain:
                due = "<br>"
                inButton_due = " | {}".format(due_plain)
            else:
                return
        else:
            if due_plain:
                due = due_plain
            else:
                return
        #// Choosing button classes based on what user has chosen in config
        if button_style == 1 or button_style == 3:
            if custom_colors:
                style = custom_background
            else:
                style = background_color
        elif button_style == 4:
            style = neon1
        elif button_style == 5:
            style = neon2
        elif button_style == 6:
            style = fill1
        elif button_style == 7:
            style = fill2
        else:
            if custom_colors:
                style = custom_text
            else:
                style = text_color
        #// Choosing style for active button
        if i == default:
            extra = "style='{}; height: {}px; width: {}px; font-size: {}px;'".format(active_extra, buttons_height, reviewButtons_width, text_size)
        else:
            extra = "style='height: {}px; width: {}px; font-size: {}px;'".format(buttons_height, reviewButtons_width, text_size)
        #// Choosing button styles based on what user has chosen in config
        if button_style == 2 or button_style == 3:
            button_class = "wide"
            #// replacing styling for active button
            if i == default:
                extra = "style='{}; border-radius: 3px; height: {}px;'".format(active_extra, buttons_height)
            else:
                extra = "style='height: {}px'".format(buttons_height)
        else:
            button_class = "mybuttons"
        if interval_style == 2:
            bottombar_table = ""
        else:
            bottombar_table = ""
        return style + button_styles + '''
<td align=center>{0}
<button title="Shortcut Key: {1}" data-ease="{1}" onclick='pycmd("ease{1}");' class={2} id={3} {4}>{5}{6}</button>
</td>'''.format(due, i, button_class, button_id, extra, label, inButton_due)
    #// adjusting the answer button table for wide button
    if button_style == 2 or button_style == 3:
        bottombar_width = "80%"
    else:
        bottombar_width = ""
    buf = "<center><table cellpadding=0 cellspacing=0 width={}><tr>".format(bottombar_width)
    for ease, label in self._answerButtonList():
        buf += but(ease, label)
    buf += "</tr></table>"
    script = """
<script>$(function () { $("#defease").focus(); });</script>"""
    return buf + script


#// replacing default functions with customized functions here
Reviewer._answerButtonList = _answerButtonList
Reviewer._answerButtons = _answerButtons
