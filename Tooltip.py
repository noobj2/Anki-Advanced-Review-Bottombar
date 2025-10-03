from aqt.utils import tooltip, showInfo
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
generalBottombarButtons_style = config[' Review_ Bottombar Buttons Style']
custom_sizes = config ['Button_  Custom Button Sizes']
custom_reviewButtonColors = config[' Review_ Custom Colors']
againHover_color = config['Color_ Again on hover']
hardHover_color = config['Color_ Hard on hover']
goodHover_color = config['Color_ Good on hover']
easyHover_color = config['Color_ Easy on hover']
tooltip_style = config['Tooltip Style']
fixed_tooltip_height = config['Tooltip Height']
fixed_tooltip_width = config['Tooltip Width']
tooltip_position = config['Tooltip Position']
tooltip_offset = config['Tooltip Offset']
info_position = config["Button_ Position_ Info Button"]
skip_position = config['Button_ Position_ Skip Button']
showSkipped_position = config['Button_ Position_ Show Skipped Button']
undo_position = config['Button_ Position_ Undo Button']
info = config['Button_   Info Button']
skip = config['Button_   Skip Button']
showSkipped = config['Button_   Show Skipped Button']
undo = config['Button_   Undo Button']
again_label = config['Button Label_ Again']
hard_label = config['Button Label_ Hard']
good_label = config['Button Label_ Good']
easy_label = config['Button Label_ Easy']
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


def showTooltip(text, background_color, tooltip_textColor, tooltip_width, tooltip_height, x_offset, y_offset, period=3000, parent=None):
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
    lab.setFixedWidth(tooltip_width)
    lab.setFixedHeight(tooltip_height)
    lab.setWindowFlags(Qt.WindowType.ToolTip)
    p = QPalette()
    p.setColor(QPalette.ColorRole.Window, QColor(background_color))
    p.setColor(QPalette.ColorRole.WindowText, QColor("transparent"))
    lab.setPalette(p)
    
    # tooltip on button
    if tooltip_style == 0:
        # x_offset: automatic offset
        # tooltip_offset: user defined offset
        # for x, positive values move tooltip to right
        # for y, positive values move tooltip down
        x_coordinate = int(x_offset + tooltip_offset[0] + (aw.width() - tooltip_width)/2)
        y_coordinate = int(y_offset - tooltip_offset[1] + (aw.height() - tooltip_height))
        lab.move(aw.mapToGlobal(QPoint(x_coordinate, y_coordinate)))
    # tooltip fixed position
    else:
        # The min() is so that the tooltip doesn't leave the viewport if the x and y offsets are too high
        x_coordinate = min(x_offset, (aw.width() - tooltip_width))
        y_coordinate = min(y_offset, (aw.height() - tooltip_height))
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

def myTooltip(self, ease):
    aw = aqt.mw.app.activeWindow() or aqt.mw
    window_width = aw.width()
    winddow_height = aw.height()
    if ease == 1:
        button = [again_label, again_backgroundColor]
    elif ease == 2:
        button = [hard_label, hard_backgroundColor]
    elif ease == 3:
        button = [good_label, good_backgroundColor]
    elif ease == 4:
        button = [easy_label, easy_backgroundColor]
    else:
        button = ["", "transparent"]

    x_offset = 0
    y_offset = 0
    text = button[0]

    if custom_sizes:
        buttons_height = config['Button_ Height_ All Bottombar Buttons']
        reviewButtons_width = config['Button_ Width_ Review Buttons']
        edit_width = config["Button_ Width_ Edit Button"]
        info_width = config["Button_ Width_ Info Button"]
        skip_width = config["Button_ Width_ Skip Button"]
        showSkipped_width = config["Button_ Width_ Show Skipped Button"]
        more_width = config["Button_ Width_ More Button"]
        undo_width = config["Button_ Width_ Undo Button"]
        tooltip_height = buttons_height + 10
        tooltip_width = reviewButtons_width + 44
    else:
        edit_width = 72
        info_width = 64
        skip_width = 64
        showSkipped_width = 64
        undo_width = 64
        more_width = 72
        if reviewButton_style in [0, 1]:
            tooltip_width = 72
            tooltip_height = 29
        elif reviewButton_style in [2, 3]:
            tooltip_width = (window_width // 4) - 5
            tooltip_height = 29
        elif reviewButton_style in [4, 5, 6, 7]:
            tooltip_width = 100
            tooltip_height = 29
        else:
            tooltip_width = 72
            tooltip_height = 29
    
    # TODO: adjust extra buttons offsets for custom sizes too
    # Offsets for general bottombar buttons with default sizes based on their position
    if info:
        if generalBottombarButtons_style == 0:
            if info_position == "left":
                x_offset += info_width - 12
            elif info_position == "right":
                x_offset -= info_width - 12
        else:
            if info_position == "left":
                x_offset += info_width - 3
            elif info_position == "right":
                x_offset -= info_width - 5
    
    if skip:
        if generalBottombarButtons_style == 0:
            if skip_position == "left":
                x_offset += skip_width - 12
            elif skip_position == "right":
                x_offset -= skip_width - 12
        else:
            if skip_position == "left":
                x_offset += skip_width - 5
            elif skip_position == "right":
                x_offset -= skip_width - 3
    
    if showSkipped:
        if generalBottombarButtons_style == 0:
            if showSkipped_position == "left":
                x_offset += showSkipped_width
            elif showSkipped_position == "right":
                x_offset -= showSkipped_width
        else:
            if showSkipped_position == "left":
                x_offset += showSkipped_width + 8
            elif showSkipped_position == "right":
                x_offset -= showSkipped_width + 7
    
    if undo:
        if generalBottombarButtons_style == 0:
            if undo_position == "left":
                x_offset += undo_width - 3
            elif undo_position == "right":
                x_offset -= undo_width - 3
        else:
            if undo_position == "left":
                x_offset += undo_width + 3
            elif undo_position == "right":
                x_offset -= undo_width + 4

    # default button sizes
    if not custom_sizes:
        # Offsets for different review button styles with default sizes
        if reviewButton_style in [0, 1]:
            y_offset += 10
            if ease == 1:
                x_offset -= 130
            elif ease == 2:
                x_offset -= 43
            elif ease == 3:
                x_offset += 43
            elif ease == 4:
                x_offset += 130
        elif reviewButton_style in [2, 3]:
            y_offset += 10
            if ease == 1:
                x_offset -= int(0.3*window_width)
            elif ease == 2:
                x_offset -= int(0.1*window_width)
            elif ease == 3:
                x_offset += int(0.1*window_width)
            elif ease == 4:
                x_offset += int(0.3*window_width)
        elif reviewButton_style in [4, 5, 6, 7]:
            y_offset += 10
            if ease == 1:
                x_offset -= 180
            elif ease == 2:
                x_offset -= 60
            elif ease == 3:
                x_offset += 60
            elif ease == 4:
                x_offset += 180
        else:
            y_offset += 10
            if ease == 1:
                x_offset -= 130
            elif ease == 2:
                x_offset -= 43
            elif ease == 3:
                x_offset += 43
            elif ease == 4:
                x_offset += 130
    
    if custom_sizes:
        x_offset += edit_width//2
        x_offset -= more_width//2
        # y_offset += tooltip_height * 0.25
        if reviewButtons_width < 61:
            if ease == 1:
                x_offset -= tooltip_width*1.8
            elif ease == 2:
                x_offset -= tooltip_width*0.65
            elif ease == 3:
                x_offset += tooltip_width*0.65
            elif ease == 4:
                x_offset += tooltip_width*1.8
        elif 60 < reviewButtons_width < 81:
            if ease == 1:
                x_offset -= tooltip_width*1.7
            elif ease == 2:
                x_offset -= tooltip_width*0.6
            elif ease == 3:
                x_offset += tooltip_width*0.6
            elif ease == 4:
                x_offset += tooltip_width*1.7
        elif 80 < reviewButtons_width < 101:
            if ease == 1:
                x_offset -= tooltip_width*1.7
            elif ease == 2:
                x_offset -= tooltip_width*0.6
            elif ease == 3:
                x_offset += tooltip_width*0.6
            elif ease == 4:
                x_offset += tooltip_width*1.7
        elif 100 < reviewButtons_width < 121:
            if ease == 1:
                x_offset -= tooltip_width*1.66
            elif ease == 2:
                x_offset -= tooltip_width*0.55
            elif ease == 3:
                x_offset += tooltip_width*0.57
            elif ease == 4:
                x_offset += tooltip_width*1.66
        elif 120 < reviewButtons_width < 141:
            if ease == 1:
                x_offset -= tooltip_width*1.64
            elif ease == 2:
                x_offset -= tooltip_width*0.54
            elif ease == 3:
                x_offset += tooltip_width*0.55
            elif ease == 4:
                x_offset += tooltip_width*1.64
        elif 140 < reviewButtons_width < 161:
            if ease == 1:
                x_offset -= tooltip_width*1.62
            elif ease == 2:
                x_offset -= tooltip_width*0.53
            elif ease == 3:
                x_offset += tooltip_width*0.54
            elif ease == 4:
                x_offset += tooltip_width*1.62
        elif 160 < reviewButtons_width < 181:
            if ease == 1:
                x_offset -= tooltip_width*1.61
            elif ease == 2:
                x_offset -= tooltip_width*0.54
            elif ease == 3:
                x_offset += tooltip_width*0.54
            elif ease == 4:
                x_offset += tooltip_width*1.61
        elif 180 < reviewButtons_width < 201:
            if ease == 1:
                x_offset -= tooltip_width*1.6
            elif ease == 2:
                x_offset -= tooltip_width*0.53
            elif ease == 3:
                x_offset += tooltip_width*0.53
            elif ease == 4:
                x_offset += tooltip_width*1.6
        elif 200 < reviewButtons_width < 221:
            if ease == 1:
                x_offset -= tooltip_width*1.6
            elif ease == 2:
                x_offset -= tooltip_width*0.54
            elif ease == 3:
                x_offset += tooltip_width*0.53
            elif ease == 4:
                x_offset += tooltip_width*1.59
        elif 220 < reviewButtons_width < 241:
            if ease == 1:
                x_offset -= tooltip_width*1.59
            elif ease == 2:
                x_offset -= tooltip_width*0.53
            elif ease == 3:
                x_offset += tooltip_width*0.53
            elif ease == 4:
                x_offset += tooltip_width*1.59
        elif 240 < reviewButtons_width < 261:
            if ease == 1:
                x_offset -= tooltip_width*1.58
            elif ease == 2:
                x_offset -= tooltip_width*0.53
            elif ease == 3:
                x_offset += tooltip_width*0.53
            elif ease == 4:
                x_offset += tooltip_width*1.58
        elif 260 < reviewButtons_width < 281:
            if ease == 1:
                x_offset -= tooltip_width*1.57
            elif ease == 2:
                x_offset -= tooltip_width*0.52
            elif ease == 3:
                x_offset += tooltip_width*0.53
            elif ease == 4:
                x_offset += tooltip_width*1.58
        elif 280 < reviewButtons_width < 321:
            if ease == 1:
                x_offset -= tooltip_width*1.57
            elif ease == 2:
                x_offset -= tooltip_width*0.52
            elif ease == 3:
                x_offset += tooltip_width*0.52
            elif ease == 4:
                x_offset += tooltip_width*1.57
        elif 320 < reviewButtons_width < 341:
            if ease == 1:
                x_offset -= tooltip_width*1.56
            elif ease == 2:
                x_offset -= tooltip_width*0.52
            elif ease == 3:
                x_offset += tooltip_width*0.53
            elif ease == 4:
                x_offset += tooltip_width*1.57
        elif 340 < reviewButtons_width < 401:
            if ease == 1:
                x_offset -= tooltip_width*1.56
            elif ease == 2:
                x_offset -= tooltip_width*0.52
            elif ease == 3:
                x_offset += tooltip_width*0.52
            elif ease == 4:
                x_offset += tooltip_width*1.56

    if tooltip_style == 1:
        x_offset = tooltip_position[0]
        y_offset = -tooltip_position[1]
        tooltip_height = fixed_tooltip_height
        tooltip_width = fixed_tooltip_width

    background_color = button[1]

    # if self.state == "answer": #// don't show tooltip if user hasn't pressed show answer button (you're really cool for a bug, so, I'm fucking keeping you :D)
    showTooltip(text, background_color, tooltip_textColor, tooltip_width, tooltip_height, x_offset, y_offset, period=tooltip_timer)
if anki_version > 2119:
    _tooltipTimer: Optional[QTimer] = None
    _tooltipLabel: Optional[QLabel] = None
else:
    _tooltipTimer = None
    _tooltipLabel = None


Reviewer._answerCard = wrap(Reviewer._answerCard, myTooltip, 'before')
