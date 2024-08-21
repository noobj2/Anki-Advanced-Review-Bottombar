#// auth_ Mohamad Janati
#// Copyright (c) 2019-2023 Mohamad Janati

import json
from aqt import mw
import aqt
from aqt.qt import *
from aqt.utils import downArrow, shortcut, showInfo
from aqt.reviewer import Reviewer
from anki.hooks import wrap
from . import Card_Info
from . import styles
from .Skip import test
from .Skip import burySkipped
from .Skip import try_unburySkipped


#// getting config information
config = mw.addonManager.getConfig(__name__)
speedFocus_addOn = config['  Speed Focus Add-on']
bottombarButtons_style = config[' Review_ Bottombar Buttons Style']
skipMethod = config['  Skip Method']
skip = config['Button_   Skip Button']
showSkipped = config['Button_   Show Skipped Button']
info = config['Button_   Info Button']
undo = config['Button_   Undo Button']
skip_shortcut = config ['Button_ Shortcut_ Skip Button'].lower()
showSkipped_shortcut = config ['Button_ Shortcut_ Show Skipped Button'].lower()
info_shortcut = config['Button_ Shortcut_ Info Button'].lower()
undo_shortcut = config['Button_ Shortcut_ Undo Button'].lower()
info_position = config['Button_ Position_ Info Button'].lower()
skip_position = config['Button_ Position_ Skip Button'].lower()
showSkipped_position = config['Button_ Position_ Show Skipped Button'].lower()
undo_position = config['Button_ Position_ Undo Button'].lower()

edit_label = config['Button Label_ Edit']
showAnswer_label = config['Button Label_ Show Answer']
more_label = config['Button Label_ More']
info_label = config['Button Label_ Info']
skip_label = config['Button Label_ Skip']
showSkipped_label = config['Button Label_ Show Skipped']
undo_label = config['Button Label_ Undo']

custom_buttonSize = config ['Button_  Custom Button Sizes']
buttons_height = config['Button_ Height_ All Bottombar Buttons']
answer_width = config['Button_ Width_ Show Answer Button']
text_size = config['Button_ Text Size']

if custom_buttonSize:
    bottomBar_top_padding = text_size + 10
else:
    text_size = ''
    bottomBar_top_padding = 25

custom_bottombarButtonBorderColor = config['Color_ Custom Bottombar Button Border Color']
bottombarButtonBorder_color = config['Color_ Bottombar Button Border Color']
showAnswerBorderColor_style = config['ShowAnswer_ Border Color Style']
showAnswerEase1 = config['ShowAnswer_ Ease1']
showAnswerEase2 = config['ShowAnswer_ Ease2']
showAnswerEase3 = config['ShowAnswer_ Ease3']
showAnswerEase4 = config['ShowAnswer_ Ease4']
showAnswerEase1_color = config['ShowAnswer_ Ease1 Color']
showAnswerEase2_color = config['ShowAnswer_ Ease2 Color']
showAnswerEase3_color = config['ShowAnswer_ Ease3 Color']
showAnswerEase4_color = config['ShowAnswer_ Ease4 Color']

edit_style = styles.edit_style
info_style = styles.info_style
skip_style = styles.skip_style
showSkipped_style = styles.showSkipped_style
undo_style = styles.undo_style
more_style = styles.more_style
min_buttonSize = styles.min_buttonSize
bottombar_neon1 = styles.bottombar_neon1
bottombar_neon2 = styles.bottombar_neon2
bottombar_fill1 = styles.bottombar_fill1
bottombar_fill2 = styles.bottombar_fill2

#// adding shortcuts to _shortcutKeys function in anki
def _shortcutKeys_wrap(self, _old):
    original = _old(self)
    sched_ver = mw.col.sched.version
    if sched_ver > 2 or skipMethod == 1:
        original.append((skip_shortcut, lambda: burySkipped()))
        original.append((showSkipped_shortcut, lambda: try_unburySkipped()))
    else:
        original.append((skip_shortcut, lambda: self.nextCard()))
    original.extend([
    (info_shortcut, lambda: Card_Info._card_stats.toggle()),
    (undo_shortcut, lambda: mw.onUndo())
    ])
    return original


#// adding button links to link handler function
def linkHandler_wrap(reviewer, url):
    sched_ver = mw.col.sched.version
    if url == "card_info":
        Card_Info._card_stats.toggle()
    elif url == "skip":
        if sched_ver > 2 or skipMethod == 1:
            burySkipped()
        else:
            reviewer.nextCard()
    elif url == "showSkipped":
        if sched_ver > 2 or skipMethod == 1:
            try_unburySkipped()
        else:
            showInfo("Your skip method is not \"Bury\" Hence you don't have any skipped cards that can be shown using this button.")
    elif url == "undo":
        mw.onUndo()
    else:
        Review_linkHandelr_Original(reviewer, url)

Review_linkHandelr_Original = Reviewer._linkHandler
Reviewer._linkHandler = linkHandler_wrap

#// Choosing styling for review other buttons in reviewer bottombar based on chosen style
timer_style = """
.timer_style {
    position: absolute;
    white-space: nowrap;
    font-size: small;
    right: 0px;
    transform: translate(-50%, -100%);
    font-weight: normal;
    display: inline-block;
    }
"""
if bottombarButtons_style == 0:
    bottomHTML_style = f"<style>{timer_style}</style>"
elif bottombarButtons_style == 1:
    bottomHTML_style = f"<style>{bottombar_neon1}{timer_style}</style>"
elif bottombarButtons_style == 2:
    bottomHTML_style = f"<style>{bottombar_neon2}{timer_style}</style>"
elif bottombarButtons_style == 3:
    bottomHTML_style = f"<style>{bottombar_fill1}{timer_style}</style>"
elif bottombarButtons_style == 4:
    bottomHTML_style = f"<style>{bottombar_fill2}{timer_style}</style>"

#// info button | written in a separate functions to preserve the original bottombar
def info_button():
    if info:
        return f"""<button title="Shortcut key: {info_shortcut.upper()}" onclick="pycmd('card_info');" {info_style}>{info_label}</button>"""
    else:
        return ""


#// skip button | written in a separate functions to preserve the original bottombar
def skip_button():
    if skip:
        return f"""<button title="Shortcut key: {skip_shortcut.upper()}" onclick="pycmd('skip');" {skip_style}>{skip_label}</button>"""
    else:
        return ""

#// Show Skipped button
def showSkipped_button():
    if showSkipped:
        return f"""<button title="Shortcut key: {showSkipped_shortcut.upper()}" onclick="pycmd('showSkipped');" {showSkipped_style}>{showSkipped_label}</button>"""
    else:
        return ""


#// undo button
def undo_button():
    if undo:
        return f"""<button title="Shortcut key: {undo_shortcut}" onclick="pycmd('undo');" {undo_style}>{undo_label}</button>"""
    else:
        return ""


#// Button Positions
leftSide_button1 = ""
leftSide_button2 = ""
leftSide_button3 = ""
leftSide_button4 = ""
middleLeftSide_button1 = ""
middleLeftSide_button2 = ""
middleLeftSide_button3 = ""
middleLeftSide_button4 = ""
middleRightSide_button1 = ""
middleRightSide_button2 = ""
middleRightSide_button3 = ""
middleRightSide_button4 = ""
rightSide_button1 = ""
rightSide_button2 = ""
rightSide_button3 = ""
rightSide_button4 = ""

if info_position == "right":
    rightSide_button1 = info_button()
elif info_position == "middle left":
    middleLeftSide_button1 = info_button()
elif info_position == "middle right":
    middleRightSide_button1 = info_button()
else:
    leftSide_button1 = info_button()

if skip_position == "left":
    leftSide_button2 = skip_button()
elif skip_position == "middle right":
    middleRightSide_button2 = skip_button()
elif skip_position == "right":
    rightSide_button2 = skip_button()
else:
    middleLeftSide_button2 = skip_button()

if showSkipped_position == "left":
    leftSide_button3 = showSkipped_button()
elif showSkipped_position == "middle right":
    middleRightSide_button3 = showSkipped_button()
elif showSkipped_position == "right":
    rightSide_button3 = showSkipped_button()
else:
    middleLeftSide_button3 = showSkipped_button()

if undo_position == "left":
    leftSide_button4 = undo_button()
elif undo_position == "middle right":
    middleRightSide_button4 = undo_button()
elif undo_position == "right":
    rightSide_button4 = undo_button()
else:
    middleLeftSide_button4 = undo_button()

#// Speed focus remove conflicts
if speedFocus_addOn:
    SF_bottomHTML = """
var autoAnswerTimeout = 0;
var autoAgainTimeout = 0;
var autoAlertTimeout = 0;

var setAutoAnswer = function(ms) {
    clearTimeout(autoAnswerTimeout);
    autoAnswerTimeout = setTimeout(function () { pycmd('ans') }, ms);
}
var setAutoAgain = function(ms) {
    clearTimeout(autoAgainTimeout);
    autoAgainTimeout = setTimeout(function () { pycmd("ease1"); }, ms);
}
var setAutoAlert = function(ms) {
    clearTimeout(autoAlertTimeout);
    autoAlertTimeout = setTimeout(function () { pycmd("autoalert"); }, ms);
}"""
else:
    SF_bottomHTML = ""

#// setting buttons based on their position
if leftSide_button1 != "":
    left_side1 = f"<td width=50 align=left valign=top class=stat style='padding-top: 0px'> {leftSide_button1} </td>"
else:
    left_side1 = ""

if leftSide_button2 != "":
    left_side2 = f"<td width=50 align=left valign=top class=stat style='padding-top: 0px'> {leftSide_button2} </td>"
else:
    left_side2 = ""

if leftSide_button3 != "":
    left_side3 = f"<td width=50 align=left valign=top class=stat style='padding-top: 0px'> {leftSide_button3} </td>"
else:
    left_side3 = ""

if leftSide_button4 != "":
    left_side4 = f"<td width=50 align=left valign=top class=stat style='padding-top: 0px'> {leftSide_button4} </td>"
else:
    left_side4 = ""

if rightSide_button1 != "":
    right_side1 = f"<td width=50 align=right valign=top class=stat style='padding-top: 0px'> {rightSide_button1} </td>"
else:
    right_side1 = ""

if rightSide_button2 != "":
    right_side2 = f"<td width=50 align=right valign=top class=stat style='padding-top: 0px'> {rightSide_button2} </td>"
else:
    right_side2 = ""

if rightSide_button3 != "":
    right_side3 = f"<td width=50 align=right valign=top class=stat style='padding-top: 0px'> {rightSide_button3} </td>"
else:
    right_side3 = ""

if rightSide_button4 != "":
    right_side4 = f"<td width=50 align=right valign=top class=stat style='padding-top: 0px'> {rightSide_button4} </td>"
else:
    right_side4 = ""

#// Review Screen Bottombar HTML
def _bottomHTML(self):
    time_color = ""
    if custom_bottombarButtonBorderColor:
        time_color = bottombarButtonBorder_color

    return f"""%(bottomHTML_style)s
%(min_buttonSize)s
<center id=outer style="display: flex; justify-content: center; align-items: center;">
<table id=innertable width=100%% cellspacing=0 cellpadding=0 style="padding-top: {bottomBar_top_padding}px">
<tr>
<td align=start width=50 valign=top class=stat style="padding-top: 0">

<button title="Shortcut key: E" onclick="pycmd('edit');" {edit_style}>{edit_label}</button></td>
{left_side1}
{left_side2}
{left_side3}
{left_side4}
<td align=center valign=top id=middle style="padding-top: 0px">
</td>
{right_side1}
{right_side2}
{right_side3}
{right_side4}
<td width=50 align=end valign=top class=stat style='color: {time_color}; padding-top: 0px'>
<span id=time class=timer_style>hey
</span>
<button onclick="pycmd('more');" {more_style}>{more_label} %(downArrow)s</button>
</td>
</tr>
</table>
</center>
<script>
time = %(time)d;
{SF_bottomHTML}
</script>
""" % dict(bottomHTML_style=bottomHTML_style, min_buttonSize=min_buttonSize, rem=self._remaining(), downArrow=downArrow(), time=self.card.time_taken() // 1000)

#// Show Answer Button
def _showAnswerButton(self):
    showAnswer_text = showAnswer_label
    highEase_tooltip = ""

    if self.card.type not in [0, 1] and showAnswerBorderColor_style in [1, 3]:
        if self.card.factor // 10 < showAnswerEase1:
            showAnswerBorder_color = showAnswerEase1_color
        elif (showAnswerEase1 - 1) < self.card.factor // 10 < showAnswerEase2:
            showAnswerBorder_color = showAnswerEase2_color
        elif (showAnswerEase2 - 1) < self.card.factor // 10 < showAnswerEase3:
            showAnswerBorder_color = showAnswerEase3_color
        elif (showAnswerEase3 - 1) < self.card.factor // 10 < showAnswerEase4:
            showAnswerBorder_color = showAnswerEase4_color
        else:
            showAnswerBorder_color = "#7000A8"
            showAnswer_text = "<font size=6 color='#7000A8'> ^_~ </font>"
    else:
        showAnswerBorder_color = ""

    #// Moved show answer button size from "styles.py" here to make show answer border color based on ease compatible with custom button sizes
    if custom_buttonSize:
        if bottombarButtons_style ==0:
            showAnswer_style = f'style="height: {buttons_height}px; width: {answer_width}px; font-size: {text_size}px; border-color: {showAnswerBorder_color};"'
        else:
            showAnswer_style = f'style="height: {buttons_height}px; width: {answer_width}px; font-size: {text_size}px; border-color: {showAnswerBorder_color};" id=main'
    else:
        if bottombarButtons_style == 0:
            showAnswer_style = f"style='border-color: {showAnswerBorder_color}' id=ansbut"  #// removed id=ansbut from its own code for styling
        else:
            showAnswer_style = f"style='border-color: {showAnswerBorder_color}' id=main"

    #// removing conflict with speed focus add-on
    if speedFocus_addOn:
        c = self.mw.col.decks.confForDid(self.card.odid or self.card.did)
        if c.get('autoAnswer', 0) > 0:
            self.bottom.web.eval("setAutoAnswer(%d);" % (c['autoAnswer'] * 1000))
        if c.get('autoAlert', 0) > 0:
            self.bottom.web.eval("setAutoAlert(%d);" % (c['autoAlert'] * 1000))
    middle = f'''
<table cellspacing=0 cellpadding=0>
<tr><td class=stat2 align=center style="padding-top: 0px">
<span class=stattxt style="font-size: {text_size}px;"> %(remaining)s </span>
{middleLeftSide_button1}
{middleLeftSide_button2}
{middleLeftSide_button3}
{middleLeftSide_button4}
<button title="Shortcut key: Space" onclick='pycmd("ans");' {showAnswer_style}>{showAnswer_text}</button>
{middleRightSide_button1}
{middleRightSide_button2}
{middleRightSide_button3}
{middleRightSide_button4}
</td></tr>
</table>''' % dict(remaining=self._remaining())
    if self.card.should_show_timer():
        maxTime = self.card.time_limit() / 1000
    else:
        maxTime = 0
    self.bottom.web.eval("showQuestion(%s,%d);" % (json.dumps(middle), maxTime))


#// replacing/wrapping functions
Reviewer._shortcutKeys = wrap(Reviewer._shortcutKeys, _shortcutKeys_wrap, 'around')
Reviewer._showAnswerButton = _showAnswerButton
Reviewer._bottomHTML =  _bottomHTML
