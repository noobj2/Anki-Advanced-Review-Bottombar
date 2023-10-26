#// auth_ Mohamad Janati
#// Copyright (c) 2019-2023 Mohamad Janati


from aqt.utils import tooltip
from anki.hooks import wrap
import aqt
from aqt.reviewer import Reviewer
import aqt
from aqt.qt import *
from aqt import mw
from anki import version
anki_version = int(version.replace('.', ''))
if anki_version > 2119:
    from typing import Optional

config = mw.addonManager.getConfig(__name__)
tooltip_timer = config["Tooltip Timer"]
tooltip_textColor = config["Tooltip Text Color"]
reviewButton_style = config[" Review_ Buttons Style"]
custom_sizes = config ['Button_  Custom Button Sizes']
buttons_height = config['Button_ Height_ All Bottombar Buttons']
reviewButtons_width = config['Button_ Width_ Review Buttons']
custom_reviewButtonColors = config[' Review_ Custom Colors']
againHover_color = config['Color_ Again on hover']
hardHover_color = config['Color_ Hard on hover']
goodHover_color = config['Color_ Good on hover']
easyHover_color = config['Color_ Easy on hover']
tooltip_style = config['Tooltip Style']
tooltip_position = config['Tooltip Position']
tooltip_offset = config['Tooltip Offset']
info_position = config["Button_ Position_ Info Button"]
skip_position = config['Button_ Position_ Skip Button']
undo_position = config['Button_ Position_ Undo Button']
info = config['Button_   Info Button']
skip = config['Button_   Skip Button']
undo = config['Button_   Undo Button']
edit_width = config["Button_ Width_ Edit Button"]
info_width = config["Button_ Width_ Info Button"]
skip_width = config["Button_ Width_ Skip Button"]
more_width = config["Button_ Width_ More Button"]
undo_width = config["Button_ Width_ Undo Button"]
again_label = config['Button Label_ Again']
hard_label = config['Button Label_ Hard']
good_label = config['Button Label_ Good']
easy_label = config['Button Label_ Easy']
if not custom_sizes:
    edit_width = 72
    info_width = 64
    skip_width = 64
    undo_width = 64
    more_width = 72
if custom_reviewButtonColors:
    again_backgroundColor = config['Color_ Again on hover']
    hard_backgroundColor = config['Color_ Hard on hover']
    good_backgroundColor = config['Color_ Good on hover']
    easy_backgroundColor = config['Color_ Easy on hover']
else:
    again_backgroundColor = "#FF1111"
    hard_backgroundColor = "#FF9814"
    good_backgroundColor = "#33FF2D"
    easy_backgroundColor = "#21C0FF"


#// should i store text, color and position all in this function?? YESSS
#// this function stores text, color and position of tooltip -> button = ["TOOLTIP_TEXT", TOOLTIP_COLOR, TOOLTIP_X, TOOLTIP_Y]
def myTooltip(self, ease):
    button_count = self.mw.col.sched.answerButtons(self.card)
    if button_count == 2:
        if ease == 1:
            button = [again_label, again_backgroundColor, -1, -39]
        elif ease == 2:
            button = [good_label, good_backgroundColor, 70, -39]
        else:
            button = ["", "transparent", 20000, 20000]
    elif button_count == 3:
            if ease == 1:
                button = [again_label, again_backgroundColor, -37, -39]
            elif ease == 2:
                button = [good_label, good_backgroundColor, 35, -39]
            elif ease == 3:
                button = [easy_label, easy_backgroundColor, 107, -39]
            else:
                button = ["", "transparent", 20000, 20000]
    else:
        if ease == 1:
            button = [again_label, again_backgroundColor, -73, -39]
        elif ease == 2:
            button = [hard_label, hard_backgroundColor, -3, -39]
        elif ease == 3:
            button = [good_label, good_backgroundColor, 70, -39]
        elif ease == 4:
            button = [easy_label, easy_backgroundColor, 142, -39]
        else:
            button = ["", "transparent", 20000, 20000]
    # default button size
    button_width = 72
    button_height = 29
    x_offset = button[2]
    y_offset = button[3]
    text = button[0]
    if custom_sizes and reviewButton_style not in [2, 3]:
        button_height = buttons_height
        button_width = reviewButtons_width
        y_offset -= (buttons_height - 30)
        if button_count == 2:
            if reviewButtons_width < 61:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset += 19
                elif ease == 2:
                    x_offset += reviewButtons_width/4
                    x_offset -= 15
            elif 60 < reviewButtons_width < 81:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset += 14
                elif ease == 2:
                    x_offset += reviewButtons_width/4
                    x_offset -= 10
            elif 80 < reviewButtons_width < 101:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset += 9
                elif ease == 2:
                    x_offset += reviewButtons_width/4
                    x_offset -= 5
            elif 100 < reviewButtons_width < 121:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset += 4
                elif ease == 2:
                    x_offset += reviewButtons_width/4
            elif 120 < reviewButtons_width < 141:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset -= 1
                elif ease == 2:
                    x_offset += reviewButtons_width/4
                    x_offset += 5
            elif 140 < reviewButtons_width < 161:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset -= 6
                elif ease == 2:
                    x_offset += reviewButtons_width/4
                    x_offset += 10
            elif 160 < reviewButtons_width < 181:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset -= 11
                elif ease == 2:
                    x_offset += reviewButtons_width/4
                    x_offset += 15
            elif 180 < reviewButtons_width < 201:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset -= 16
                elif ease == 2:
                    x_offset += reviewButtons_width/4
                    x_offset += 20
            elif 200 < reviewButtons_width < 221:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset -= 21
                elif ease == 2:
                    x_offset += reviewButtons_width/4
                    x_offset += 25
            elif 220 < reviewButtons_width < 241:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset -= 26
                elif ease == 2:
                    x_offset += reviewButtons_width/4
                    x_offset += 30
            elif 240 < reviewButtons_width < 261:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset -= 31
                elif ease == 2:
                    x_offset += reviewButtons_width/4
                    x_offset += 35
            elif 260 < reviewButtons_width < 281:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset -= 36
                elif ease == 2:
                    x_offset += reviewButtons_width/4
                    x_offset += 40
            elif 280 < reviewButtons_width < 301:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset -= 41
                elif ease == 2:
                    x_offset += reviewButtons_width/4
                    x_offset += 45
            elif 300 < reviewButtons_width < 321:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset -= 46
                elif ease == 2:
                    x_offset += reviewButtons_width/4
                    x_offset += 50
            elif 320 < reviewButtons_width < 341:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset -= 51
                elif ease == 2:
                    x_offset += reviewButtons_width/4
                    x_offset += 55
            elif 340 < reviewButtons_width < 361:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset -= 56
                elif ease == 2:
                    x_offset += reviewButtons_width/4
                    x_offset += 60
            elif 360 < reviewButtons_width < 381:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset -= 61
                elif ease == 2:
                    x_offset += reviewButtons_width/4
                    x_offset += 65
            elif 380 < reviewButtons_width < 401:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset -= 65
                elif ease == 2:
                    x_offset += reviewButtons_width/4
                    x_offset += 70
        elif button_count == 3:
            if ease == 1:
                x_offset -= button_width
                x_offset += 62
            elif ease == 2:
                x_offset += 2
            elif ease == 3:
                x_offset += button_width
                x_offset -= 59
        elif button_count == 4:
            if reviewButtons_width < 61:
                if ease == 1:
                    x_offset -= reviewButtons_width/4
                    x_offset += 29
                elif ease == 2:
                    x_offset -= reviewButtons_width/4
                    x_offset += 21
                elif ease == 3:
                    x_offset += reviewButtons_width/4
                    x_offset -= 15
                elif ease == 4:
                    x_offset += reviewButtons_width/4
                    x_offset -= 25
            elif 60 < reviewButtons_width < 81:
                if ease == 1:
                    x_offset -= reviewButtons_width/2
                    x_offset += 21
                elif ease == 2:
                    x_offset -= reviewButtons_width/4
                    x_offset += 15
                elif ease == 3:
                    x_offset += reviewButtons_width/4
                    x_offset -= 10
                elif ease == 4:
                    x_offset += reviewButtons_width/2
                    x_offset -= 18
            elif 80 < reviewButtons_width < 101:
                if ease == 1:
                    x_offset -= reviewButtons_width/2
                elif ease == 2:
                    x_offset -= reviewButtons_width/4
                    x_offset += 10
                elif ease == 3:
                    x_offset += reviewButtons_width/4
                    x_offset -= 5
                elif ease == 4:
                    x_offset += reviewButtons_width/2
                    x_offset += 2
            elif 100 < reviewButtons_width < 121:
                if ease == 1:
                    x_offset -= reviewButtons_width
                    x_offset += 37
                elif ease == 2:
                    x_offset -= reviewButtons_width/3
                    x_offset += 15
                elif ease == 3:
                    x_offset += reviewButtons_width/3
                    x_offset -= 9
                elif ease == 4:
                    x_offset += reviewButtons_width
                    x_offset -= 33
            elif 120 < reviewButtons_width < 141:
                if ease == 1:
                    x_offset -= reviewButtons_width
                    x_offset += 26
                elif ease == 2:
                    x_offset -= reviewButtons_width/3
                    x_offset += 13
                elif ease == 3:
                    x_offset += reviewButtons_width/3
                    x_offset -= 6
                elif ease == 4:
                    x_offset += reviewButtons_width
                    x_offset -= 23
            elif 140 < reviewButtons_width < 161:
                if ease == 1:
                    x_offset -= reviewButtons_width
                    x_offset += 16
                elif ease == 2:
                    x_offset -= reviewButtons_width/3
                    x_offset += 7
                elif ease == 3:
                    x_offset += reviewButtons_width/3
                    x_offset -= 3
                elif ease == 4:
                    x_offset += reviewButtons_width
                    x_offset -= 13
            elif 160 < reviewButtons_width < 181:
                if ease == 1:
                    x_offset -= reviewButtons_width
                elif ease == 2:
                    x_offset -= reviewButtons_width/3
                    x_offset += 5
                elif ease == 3:
                    x_offset += reviewButtons_width/3
                    x_offset += 3
                elif ease == 4:
                    x_offset += reviewButtons_width
                    x_offset -= 3
            elif 180 < reviewButtons_width < 201:
                if ease == 1:
                    x_offset -= reviewButtons_width
                    x_offset -= 5
                elif ease == 2:
                    x_offset -= reviewButtons_width/3
                    x_offset += 4
                elif ease == 3:
                    x_offset += reviewButtons_width/3
                    x_offset += 4
                elif ease == 4:
                    x_offset += reviewButtons_width
                    x_offset += 7
            elif 200 < reviewButtons_width < 221:
                if ease == 1:
                    x_offset -= reviewButtons_width
                    x_offset -= 13
                elif ease == 2:
                    x_offset -= reviewButtons_width/3
                    x_offset -= 1
                elif ease == 3:
                    x_offset += reviewButtons_width/3
                    x_offset += 7
                elif ease == 4:
                    x_offset += reviewButtons_width
                    x_offset += 17
            elif 220 < reviewButtons_width < 241:
                if ease == 1:
                    x_offset -= reviewButtons_width
                    x_offset -= 23
                elif ease == 2:
                    x_offset -= reviewButtons_width/3
                    x_offset -= 5
                elif ease == 3:
                    x_offset += reviewButtons_width/3
                    x_offset += 11
                elif ease == 4:
                    x_offset += reviewButtons_width
                    x_offset += 27
            elif 240 < reviewButtons_width < 261:
                if ease == 1:
                    x_offset -= reviewButtons_width
                    x_offset -= 33
                elif ease == 2:
                    x_offset -= reviewButtons_width/3
                    x_offset -= 8
                elif ease == 3:
                    x_offset += reviewButtons_width/3
                    x_offset += 14
                elif ease == 4:
                    x_offset += reviewButtons_width
                    x_offset += 37
            elif 260 < reviewButtons_width < 281:
                if ease == 1:
                    x_offset -= reviewButtons_width
                    x_offset -= 43
                elif ease == 2:
                    x_offset -= reviewButtons_width/3
                    x_offset -= 11
                elif ease == 3:
                    x_offset += reviewButtons_width/3
                    x_offset += 17
                elif ease == 4:
                    x_offset += reviewButtons_width
                    x_offset += 47
            elif 280 < reviewButtons_width < 301:
                if ease == 1:
                    x_offset -= reviewButtons_width
                    x_offset -= 53
                elif ease == 2:
                    x_offset -= reviewButtons_width/3
                    x_offset -= 14
                elif ease == 3:
                    x_offset += reviewButtons_width/3
                    x_offset += 21
                elif ease == 4:
                    x_offset += reviewButtons_width
                    x_offset += 57
            elif 300 < reviewButtons_width < 321:
                if ease == 1:
                    x_offset -= reviewButtons_width
                    x_offset -= 63
                elif ease == 2:
                    x_offset -= reviewButtons_width/3
                    x_offset -= 17
                elif ease == 3:
                    x_offset += reviewButtons_width/3
                    x_offset += 24
                elif ease == 4:
                    x_offset += reviewButtons_width
                    x_offset += 67
            elif 320 < reviewButtons_width < 341:
                if ease == 1:
                    x_offset -= reviewButtons_width
                    x_offset -= 73
                elif ease == 2:
                    x_offset -= reviewButtons_width/3
                    x_offset -= 22
                elif ease == 3:
                    x_offset += reviewButtons_width/3
                    x_offset += 27
                elif ease == 4:
                    x_offset += reviewButtons_width
                    x_offset += 77
            elif 340 < reviewButtons_width < 361:
                if ease == 1:
                    x_offset -= reviewButtons_width
                    x_offset -= 83
                elif ease == 2:
                    x_offset -= reviewButtons_width/3
                    x_offset -= 25
                elif ease == 3:
                    x_offset += reviewButtons_width/3
                    x_offset += 31
                elif ease == 4:
                    x_offset += reviewButtons_width
                    x_offset += 87
            elif 360 < reviewButtons_width < 381:
                if ease == 1:
                    x_offset -= reviewButtons_width
                    x_offset -= 93
                elif ease == 2:
                    x_offset -= reviewButtons_width/3
                    x_offset -= 28
                elif ease == 3:
                    x_offset += reviewButtons_width/3
                    x_offset += 34
                elif ease == 4:
                    x_offset += reviewButtons_width
                    x_offset += 97
            elif 380 < reviewButtons_width < 401:
                if ease == 1:
                    x_offset -= reviewButtons_width
                    x_offset -= 103
                elif ease == 2:
                    x_offset -= reviewButtons_width/3
                    x_offset -= 31
                elif ease == 3:
                    x_offset += reviewButtons_width/3
                    x_offset += 37
                elif ease == 4:
                    x_offset += reviewButtons_width
                    x_offset += 107
    if reviewButton_style in [4, 5, 6, 7]:
        y_offset -= 1
        if button_count == 2:
            if ease == 1:
                x_offset -= 4
            elif ease == 2:
                x_offset += 2
        elif button_count == 3:
            if ease == 1:
                x_offset -= 1
            elif ease == 2:
                x_offset -= 1
        elif button_count == 4:
            if ease == 1:
                x_offset -= 5
            elif ease == 2:
                x_offset -= 2
            elif ease == 3:
                x_offset += 1
            elif ease == 4:
                x_offset += 5
    if reviewButton_style in [4, 5, 6, 7] and not custom_sizes:
        button_height = 29
        button_width = 72
        y_offset += 2
        if button_count == 2:
            if ease == 1:
                x_offset -= 3
            elif ease == 2:
                x_offset += 4
        elif button_count == 3:
            if ease == 1:
                x_offset -= 10
            elif ease == 2:
                x_offset += 4
            elif ease == 3:
                x_offset += 10
        elif button_count == 4:
            if ease == 1:
                x_offset -= 10
            elif ease == 2:
                x_offset += 4
            elif ease == 3:
                x_offset += 8
            elif ease == 4:
                x_offset += 15
    if not info or info_position in ['middle left', 'middle right']:
        x_offset -= 36
    if info and info_position == "left":
        x_offset += (info_width-64)/2
    if info and info_position == "right":
        x_offset -= 72
        x_offset -= (info_width-64)/2
    if skip and skip_position == "left":
        x_offset += 36
        x_offset += (skip_width-64)/2
    if skip and skip_position == "right":
        x_offset -= 36
        x_offset -= (skip_width-64)/2
    if undo and undo_position == "left":
        x_offset += 52
        x_offset += (undo_width-86)/2
    if undo and undo_position == "right":
        x_offset -= 52
        x_offset -= (undo_width-86)/2
    if reviewButton_style in [4, 5, 6, 7]:
        if not info or info_position in ['middle left', 'middle right']:
            x_offset -= 8
        if info and info_position == "right":
            x_offset -= 16
        if undo and undo_position == "left":
            x_offset +=8
        if undo and undo_position == "right":
            x_offset -= 17
        x_offset -= 7
    x_offset -= (more_width-72)/2
    x_offset += (edit_width-72)/2
    if tooltip_style == 1:
        x_offset = tooltip_position[0]
        y_offset = -tooltip_position[1]
        button_width = 72
        button_height = 29
    background_color = button[1]

    # if self.state == "answer": #// don't show tooltip if user hasn't pressed show answer button (you're really cool for a bug, so, I'm fucking keeping you :D)
    showTooltip(text, background_color, tooltip_textColor, button_width, button_height, x_offset, y_offset, period=tooltip_timer)
if anki_version > 2119:
    _tooltipTimer: Optional[QTimer] = None
    _tooltipLabel: Optional[QLabel] = None
else:
    _tooltipTimer = None
    _tooltipLabel = None

def showTooltip(text, background_color, tooltip_textColor, button_width, button_height, x_offset, y_offset, period=3000, parent=None):
    global _tooltipTimer, _tooltipLabel

    class CustomLabel(QLabel):
        silentlyClose = True

        def mousePressEvent(self, evt):
            evt.accept()
            self.hide()

    closeTooltip()
    aw = parent or aqt.mw.app.activeWindow() or aqt.mw
    table = """
    <table align=center>
    <tr>
    <td><div style='color: {0};'>{1}</div></td>
    </tr>
    </table>
    """.format(tooltip_textColor, text)
    lab = CustomLabel(table, aw)
    lab.setFrameStyle(QFrame.Shape.Panel)
    lab.setLineWidth(2)
    lab.setFixedWidth(button_width)
    lab.setFixedHeight(button_height)
    lab.setWindowFlags(Qt.WindowType.ToolTip)
    p = QPalette()
    p.setColor(QPalette.ColorRole.Window, QColor(background_color))
    p.setColor(QPalette.ColorRole.WindowText, QColor("transparent"))
    lab.setPalette(p)
    # Handle button offset.
    if tooltip_style == 0:
        x_coordinate = int(x_offset + tooltip_offset[0] + (aw.width()-button_width)/2)
        y_coordinate = y_offset + aw.height() - tooltip_offset[1]
        lab.move(aw.mapToGlobal(QPoint(x_coordinate, y_coordinate)))
    else:
        x_coordinate = min(x_offset, aw.width())
        y_coordinate = min(y_offset, aw.height())
        lab.move(aw.mapToGlobal(QPoint(x_coordinate, y_coordinate)))
    lab.show()
    _tooltipTimer = aqt.mw.progress.timer(period, closeTooltip, False, requiresCollection=False)
    _tooltipLabel = lab


def closeTooltip():
    global _tooltipLabel, _tooltipTimer
    if _tooltipLabel:
        try:
            _tooltipLabel.deleteLater()
        except:
            # already deleted as parent window closed
            pass
        _tooltipLabel = None
    if _tooltipTimer:
        _tooltipTimer.stop()
        _tooltipTimer = None

Reviewer._answerCard = wrap(Reviewer._answerCard, myTooltip, 'before')
