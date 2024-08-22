#// auth_ Mohamad Janati
#// Copyright (c) 2019-2023 Mohamad Janati

import re
from aqt.reviewer import Reviewer
from aqt import mw
from aqt.utils import showInfo
from anki.scheduler.v3 import Scheduler as V3Scheduler
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
wideButton_percent = config[' Review_ Wide Button Percent']
if custom_buttonSize:
    buttons_height = config['Button_ Height_ All Bottombar Buttons']
    reviewButtons_width = config['Button_ Width_ Review Buttons']
    text_size = config['Button_ Text Size']
else:
    buttons_height = ""
    reviewButtons_width = ""
    text_size = ""
font_weights = [100, 200, 300, 400, 500, 600, 700, 800, 900]
buttonFontWeight = font_weights[int(config['Button_ Font Weight'])]
again_label = config['Button Label_ Again']
hard_label = config['Button Label_ Hard']
good_label = config['Button Label_ Good']
easy_label = config['Button Label_ Easy']
hideEasyIfNotLearning = config['  Hide Easy if not in Learning']

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
    #// Card Types: 0-> "Learn", 1-> "Review", 2-> "Relearn", 3-> "Filtered", 4-> "Resched"
    card_type = self.mw.col.db.all("SELECT type FROM revlog WHERE cid = ?", self.card.id)
    if card_type:
        card_type = card_type[-1][0]
    else:
        card_type = 0
    if cnt == 2:
        #// button = ((ease, "Label"),)
        again = ((1, f" {again_label} "),)
        good = ((2, f" {good_label} "),)
        buttons = again
        #// don't add button "good" to returned buttons if it's disabled
        if not hide_good:
            buttons += good
        return buttons
    elif cnt == 3:
        again = ((1, f" {again_label} "),)
        good = ((2, f" {good_label} "),)
        easy = ((3, f" {easy_label} "),)
        buttons = again
        if not hide_good:
            buttons += good
        if not hide_easy:
            if hideEasyIfNotLearning:
                if card_type == 0:
                    buttons += easy
            else:
                buttons += easy
        return buttons
    else:
        again = ((1, f" {again_label} "),)
        hard = ((2, f" {hard_label} "),)
        good = ((3, f" {good_label} "),)
        easy = ((4, f" {easy_label} "),)
        buttons = again
        if not hide_hard:
            buttons += hard
        if not hide_good:
            buttons += good
        if not hide_easy:
            if hideEasyIfNotLearning:
                if card_type == 0:
                    buttons += easy
            else:
                buttons += easy
        return buttons


def _answerButtons(self):
    cnt = self.mw.col.sched.answerButtons(self.card)
    default = self._defaultEase()

    if v3 := self._v3:
        assert isinstance(self.mw.col.sched, V3Scheduler)
        labels = self.mw.col.sched.describe_next_states(v3.states)
    else:
        labels = None

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
        due_plain = re.search(r'<span.*>(.*?)</span>', self._buttonTime(i, v3_labels=labels))
        if due_plain is None:
            due_plain = ""
        else:
            due_plain = due_plain.group(1)
        inButton_due = ""
        if interval_style == 1:
            if button_id == "again":
                due = f"<span class='nobold' style='color:{again_color}; font-size: {text_size}px;'>{due_plain}</span>"
            elif button_id == "hard":
                due = f"<span class='nobold' style='color:{hard_color}; font-size: {text_size}px;'>{due_plain}</span>"
            elif button_id == "good":
                due = f"<span class='nobold' style='color:{good_color}; font-size: {text_size}px;'>{due_plain}</span>"
            elif button_id == "easy":
                due = f"<span class='nobold' style='color:{easy_color}; font-size: {text_size}px;'>{due_plain}</span>"
            else:
                if due_plain:
                    due = due_plain
                else:
                    return
        elif interval_style == 2:
            if due_plain:
                due = ""
                inButton_due = f" | {due_plain}"
            else:
                due = ""
                inButton_due = ""
        else:
            if due_plain:
                due = f"<span class='nobold' style='font-size: {text_size}px;'>{due_plain}</span>"
            else:
                due = ""
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
            extra = f"style='{active_extra}; height: {buttons_height}px; width: {reviewButtons_width}px; font-size: {text_size}px; font-weight: {buttonFontWeight};'"
        else:
            extra = f"style='height: {buttons_height}px; width: {reviewButtons_width}px; font-size: {text_size}px; font-weight: {buttonFontWeight};'"
        #// Choosing button styles based on what user has chosen in config
        if button_style == 2 or button_style == 3:
            button_class = "wide"
            #// replacing styling for active button
            if i == default:
                extra = f"style='{active_extra}; border-radius: 3px; height: {buttons_height}px; font-size: {text_size}px; font-weight: {buttonFontWeight};'"
            else:
                extra = f"style='height: {buttons_height}px; font-size: {text_size}px; font-weight: {buttonFontWeight};'"
        else:
            button_class = "mybuttons"
        if interval_style == 2:
            bottombar_table = ""
        else:
            bottombar_table = ""
        return style + button_styles + f'''
<td align=center style="padding-top: 0px">{due}
<button title="Shortcut Key: {i}" data-ease="{i}" onclick='pycmd("ease{i}");' class={button_class} id={button_id} {extra}>{label}{inButton_due}</button>
</td>'''
    #// adjusting the answer button table for wide button
    if button_style == 2 or button_style == 3:
        bottombar_width = f"{wideButton_percent}%"
    else:
        bottombar_width = ""
    buf = f"<center><table cellpadding=0 cellspacing=0 width={bottombar_width}><tr>"
    for ease, label in self._answerButtonList():
        buf += but(ease, label)
    buf += "</tr></table>"
    script = """
<script>$(function () { $("#defease").focus(); });</script>"""
    return buf + script


#// replacing default functions with customized functions here
Reviewer._answerButtonList = _answerButtonList
Reviewer._answerButtons = _answerButtons
