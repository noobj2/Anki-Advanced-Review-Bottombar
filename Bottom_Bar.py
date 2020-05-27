#// auth_ Mohamad Janati
#// AmirHassan Asvadi ;)
#// Copyright (c) 2019-2020 Mohamad Janati (freaking stupid, right? :|)
from anki import version
anki_version = int(version.replace('.', ''))
import json
from aqt import mw
import aqt
from aqt.qt import *
from aqt.utils import downArrow, shortcut
from aqt.reviewer import Reviewer
from anki.hooks import wrap
from aqt.deckbrowser import DeckBrowser
from aqt.overview import Overview
if anki_version > 2119:
    from aqt.deckbrowser import DeckBrowserBottomBar
    from aqt.overview import OverviewBottomBar
from copy import deepcopy
from . import Card_Info
from . import styles


#// getting config information
config = mw.addonManager.getConfig(__name__)
speedFocus_addOn = config['  Speed Focus Add-on']
bottombarButtons_style = config[' Review_ Bottombar Buttons Style']
style_mainScreenButtons = config['  Style Main Screen Buttons']
skip = config['Button_   Skip Button']
info = config['Button_   Info Button']
undo = config['Button_   Undo Button']
skip_shortcut = config ['Button_ Shortcut_ Skip Button'].lower()
info_shortcut = config['Button_ Shortcut_ Info Button'].lower()
undo_shortcut = config['Button_ Shortcut_ Undo Button'].lower()
info_position = config['Button_ Position_ Info Button'].lower()
skip_position = config['Button_ Position_ Skip Button'].lower()
undo_position = config['Button_ Position_ Undo Button'].lower()
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
undo_style = styles.undo_style
showAnswer_style = styles.showAnswer_style
more_style = styles.more_style
min_buttonSize = styles.min_buttonSize
bottombar_neon1 = styles.bottombar_neon1
bottombar_neon2 = styles.bottombar_neon2
bottombar_fill1 = styles.bottombar_fill1
bottombar_fill2 = styles.bottombar_fill2
#// adding shortcuts to _shortcutKeys function in anki
def _shortcutKeys_wrap(self, _old):
    original = _old(self)
    original.extend([
    (info_shortcut, lambda: Card_Info._cs.toggle()),
    (skip_shortcut, lambda: self.nextCard()),
    (undo_shortcut, lambda: mw.onUndo())
    ])
    return original


#// adding button links to link handler function
def linkHandler_wrap(reviewer, url):
    if url == "card_info":
        Card_Info._cs.toggle()
    elif url == "skip":
        reviewer.nextCard()
    elif url == "undo":
        mw.onUndo()
    else:
        Review_linkHandelr_Original(reviewer, url)

Review_linkHandelr_Original = Reviewer._linkHandler
Reviewer._linkHandler = linkHandler_wrap

#// Chosing stylinhg for review other buttons in reviewer bottombar based on chosen style
if bottombarButtons_style == 0:
    bottomHTML_style = "<style></style>"
elif bottombarButtons_style == 1:
    bottomHTML_style = bottombar_neon1
elif bottombarButtons_style == 2:
    bottomHTML_style = bottombar_neon2
elif bottombarButtons_style == 3:
    bottomHTML_style = bottombar_fill1
elif bottombarButtons_style == 4:
    bottomHTML_style = bottombar_fill2

#// info button | written in a separate functions to preserve the original bottombar
def info_button():
    if info:
        return """<button title="Shortcut key: {}" onclick="pycmd('card_info');" {}>Info</button>""".format(info_shortcut.upper(), info_style)
    else:
        return ""


#// skip button | written in a separate functions to preserve the original bottombar
def skip_button():
    if skip:
        return """<button title="Shortcut key: {}" onclick="pycmd('skip');" {}>Skip</button>""".format(skip_shortcut.upper(), skip_style)
    else:
        return ""


#// undo button
def undo_button():
    if undo:
        return """<button title="Shortcut key: {}" onclick="pycmd('undo');" {}>Undo Review</button>""".format(undo_shortcut, undo_style)
    else:
        return ""


#// Button Positions
leftSide_button1 = ""
leftSide_button2 = ""
leftSide_button3 = ""
middleLeftSide_button1 = ""
middleLeftSide_button2 = ""
middleLeftSide_button3 = ""
middleRightSide_button1 = ""
middleRightSide_button2 = ""
middleRightSide_button3 = ""
rightSide_button1 = ""
rightSide_button2 = ""
rightSide_button3 = ""

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

if undo_position == "left":
    leftSide_button3 = undo_button()
elif undo_position == "middle right":
    middleRightSide_button3 = undo_button()
elif undo_position == "right":
    rightSide_button3 = undo_button()
else:
    middleLeftSide_button3 = undo_button()

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
    left_side1 = "<td width=50 align=left valign=top class=stat><br> {} </td>".format(leftSide_button1)
else:
    left_side1 = ""

if leftSide_button2 != "":
    left_side2 = "<td width=50 align=left valign=top class=stat><br> {} </td>".format(leftSide_button2)
else:
    left_side2 = ""

if leftSide_button3 != "":
    left_side3 = "<td width=50 align=left valign=top class=stat><br> {} </td>".format(leftSide_button3)
else:
    left_side3 = ""

if rightSide_button1 != "":
    right_side1 = "<td width=50 align=right valign=top class=stat><br> {} </td>".format(rightSide_button1)
else:
    right_side1 = ""

if rightSide_button2 != "":
    right_side2 = "<td width=50 align=right valign=top class=stat><br> {} </td>".format(rightSide_button2)
else:
    right_side2 = ""

if rightSide_button3 != "":
    right_side3 = "<td width=50 align=right valign=top class=stat><br> {} </td>".format(rightSide_button3)
else:
    right_side3 = ""

#// Review Screen Bottombar HTML
def _bottomHTML(self):
    time_color = ""
    if custom_bottombarButtonBorderColor:
        time_color = bottombarButtonBorder_color

    return """%(bottomHTML_style)s
%(min_buttonSize)s
<center id=outer>
<table id=innertable width=100%% cellspacing=0 cellpadding=0>
<tr>
<td align=left width=50 valign=top class=stat>
<br>
<button title="Shortcut key: E" onclick="pycmd('edit');" %(edit_style)s>Edit</button></td>
%(left_side1)s
%(left_side2)s
%(left_side3)s
<td align=center valign=top id=middle>
</td>
%(right_side1)s
%(right_side2)s
%(right_side3)s
<td width=50 align=right valign=top class=stat style='color: %(time_color)s'><span id=time class=stattxt>
</span><br>
<button onclick="pycmd('more');" %(more_style)s>More %(downArrow)s</button>
</td>
</tr>
</table>
</center>
<script>
time = %(time)d;
%(SF_bottomHTML)s
</script>
""" % dict(bottomHTML_style=bottomHTML_style, min_buttonSize=min_buttonSize, rem=self._remaining(), downArrow=downArrow(), time=self.card.timeTaken() // 1000,
    edit_style=edit_style, left_side1=left_side1, left_side2=left_side2, left_side3=left_side3, right_side1=right_side1,
    right_side2=right_side2, right_side3=right_side3, more_style=more_style, SF_bottomHTML=SF_bottomHTML, time_color=time_color)

#// Show Answer Button
def _showAnswerButton(self):
    showAnswer_text = "Show Answer"
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
    #// removing conflict with speed focus add-on
    if speedFocus_addOn:
        c = self.mw.col.decks.confForDid(self.card.odid or self.card.did)
        if c.get('autoAnswer', 0) > 0:
            self.bottom.web.eval("setAutoAnswer(%d);" % (c['autoAnswer'] * 1000))
        if c.get('autoAlert', 0) > 0:
            self.bottom.web.eval("setAutoAlert(%d);" % (c['autoAlert'] * 1000))

    if not self.typeCorrect:
        self.bottom.web.setFocus()
    middle = '''
<table cellspacing=0 cellpadding=0><tr><td class=stat2 align=center>
<span class=stattxt> %(remaining)s </span><br>
%(middleLeft_side1)s
%(middleLeft_side2)s
%(middleLeft_side3)s
<button title="Shortcut key: Space" onclick='pycmd("ans");' %(answer_style)s style='border-color: %(showAnswerBorder_color)s'>%(showAnswer_text)s</button>
%(middleRight_side1)s
%(middleRight_side2)s
%(middleRight_side3)s
</td></tr></table>''' % dict(remaining=self._remaining(), middleLeft_side1=middleLeftSide_button1, middleLeft_side2=middleLeftSide_button2, middleLeft_side3=middleLeftSide_button3,
    answer_style=showAnswer_style, middleRight_side1=middleRightSide_button1, middleRight_side2=middleRightSide_button2, middleRight_side3=middleRightSide_button3, showAnswerBorder_color=showAnswerBorder_color, showAnswer_text=showAnswer_text)
    # wrap it in a table so it has the same top margin as the ease buttons
    middle = "%s" % middle
    if self.card.shouldShowTimer():
        maxTime = self.card.timeLimit() / 1000
    else:
        maxTime = 0
    self.bottom.web.eval("showQuestion(%s,%d);" % (json.dumps(middle), maxTime))
    self.bottom.web.adjustHeightToFit()

#// Main Screen Bottombar Buttons
def _drawButtons(self):
    buf = "{}".format(bottomHTML_style)
    if style_mainScreenButtons:
        #// style='height: px' -> to prevent changing main screen buttons heights
        # based on height defined in #main {}
        mainScreen_style = """id=main style='height: px' """
    else:
        mainScreen_style = ""
    drawLinks = deepcopy(self.drawLinks)
    for b in drawLinks:
        b.insert(0, "{}".format(mainScreen_style))
        if b[0]:
            b[0] = _("Shortcut key: %s") % shortcut(b[0])
        buf += """
<button %s title='%s' onclick='pycmd(\"%s\");'>%s</button>""" % (tuple(b))
    if anki_version > 2121:
        self.bottom.draw(
            buf=buf,
            link_handler=self._linkHandler,
            web_context=DeckBrowserBottomBar(self),
        )
    else:
        self.bottom.draw(buf)
        self.bottom.web.onBridgeCmd = self._linkHandler


#// Deck Overview Bottombar Buttons
def _renderBottom(self):
    links = [
        ["O", "opts", _("Options")],
    ]
    if self.mw.col.decks.current()["dyn"]:
        links.append(["R", "refresh", _("Rebuild")])
        links.append(["E", "empty", _("Empty")])
    else:
        links.append(["C", "studymore", _("Custom Study")])
        # links.append(["F", "cram", _("Filter/Cram")])
    if self.mw.col.sched.haveBuried():
        links.append(["U", "unbury", _("Unbury")])
    buf = "{}".format(bottomHTML_style)
    if style_mainScreenButtons:
        #// style='height: px' -> to prevent changing main screen buttons heights
        # based on height defined in #main {}
        mainScreen_style = """id=main style='height: px' """
    else:
        mainScreen_style = ""
    for b in links:
        b.insert(0, "{}".format(mainScreen_style))
        if b[0]:
            b[0] = _("Shortcut key: %s") % shortcut(b[0])
        buf += """
<button %s title="%s" onclick='pycmd("%s")'>%s</button>""" % tuple(b)
    if anki_version > 2121:
        self.bottom.draw(
            buf=buf,
            link_handler=self._linkHandler,
            web_context=OverviewBottomBar(self)
        )
    else:
        self.bottom.draw(buf)
        self.bottom.web.onBridgeCmd = self._linkHandler


more_overViewStats = False

#// Deck Overview Study Now Button | code from more overview stats to add more overview stats, OBVIOUSLY
if more_overViewStats:
    def _table(self):
        """Returns html table with more statistics than before."""
        sched = self.mw.col.sched
        deck = self.mw.col.decks.current()
        dconf = self.mw.col.decks.confForDid(deck.get('id'))
        but = self.mw.button

        # Get default counts
        # 0 = new, 1 = learn, 2 = review
        counts = list(sched.counts())
        finished = not sum(counts)
        counts = _limit(counts)

        totals = [
            #new
            sched.col.db.scalar("""
                select count() from (select id from cards where did = %s
                and queue = 0)""" % deck.get('id')),
            # learn
            sched.col.db.scalar("""
                select count() from (select id from cards where did = %s
                and queue in (1,3))""" % deck.get('id')),
            # review
            sched.col.db.scalar("""
                select count() from (select id from cards where did = %s
                and queue = 2)""" % deck.get('id')),
             # suspended
            sched.col.db.scalar("""
                select count() from (select id from cards where did = %s
                and queue = -1)""" % deck.get('id')),
            # buried
            sched.col.db.scalar("""
                select count() from (select id from cards where did = %s
                and queue = -2)""" % deck.get('id')),
        ]

        if (dconf.get('new')):
            dueTomorrow = _limit([
                # new
                min(dconf.get('new').get('perDay'), totals[0]),
                # review
                sched.col.db.scalar("""
                    select count() from cards where did = %s and queue = 3
                    and due = ?""" % deck.get('id'), sched.today + 1),
                sched.col.db.scalar("""
                    select count() from cards where did = %s and queue = 2
                    and due = ?""" % deck.get('id'), sched.today + 1)
            ])

        html = ''

        # Style if less than 2.1.20
        if (int(version.replace('.', '')) < 2120):
            html += '''
                <style>
                    .new-count {color: #00a}
                    .learn-count {color: #C35617}
                    .review-count {color: #0a0}
                </style>'''

        # No need to show due if we have finished collection today
        if finished:
            mssg = sched.finishedMsg()
            html +=  '''
                <div style="white-space: pre-wrap;">%s</div>
                <table cellspacing=5>''' % mssg
        else:
            html +='''%s
                <table cellpadding=5>
                <tr><td align=center valign=top nowrap="nowrap">
                <table cellspacing=5>
                <tr><td nowrap="nowrap">%s:</td><td align=right>
                    <span title="new" class="new-count">%s</span>
                    <span title="learn" class="learn-count">%s</span>
                    <span title="review" class="review-count">%s</span>
                </td></tr>''' % (bottomHTML_style, _("Due today"), counts[0], counts[1], counts[2])

        if (dconf.get('new')):
            html += '''
                <tr><td nowrap="nowrap">%s:</td><td align=right>
                    <span title="new" class="new-count">%s</span>
                    <span title="learn" class="learn-count">%s</span>
                    <span title="review" class="review-count">%s</span>
                </td></tr>''' % (_("Due tomorrow"), dueTomorrow[0],
                dueTomorrow[1], dueTomorrow[2])

        html += '''
            <tr>
                <td nowrap="nowrap">%s:</td>
                <td align=right nowrap="nowrap">
                    <span title="new" class="new-count">%s</span>
                    <span title="learn" class="learn-count">%s</span>
                    <span title="review" class="review-count">%s</span>
                    <span title="buried" style="color:#ffa500">%s</span>
                    <span title="suspended" style="color:#adb300">%s</span>
                </td>
            </tr>
        </table>''' % (_("Total Cards"), totals[0], totals[1], totals[2], totals[4],
        totals[3])

        if not finished:
            if style_mainScreenButtons:
                #// style='height: px' -> to prevent changing main screen buttons heights
                # based on height defined in #main {}
                mainScreen_style = """id=main style='height: px' """
            else:
                mainScreen_style = ""
            if style_mainScreenButtons:
                studyButton_id = "main"
            else:
                studyButton_id = "study"
            html += '''</td>
                <td align=center nowrap="nowrap">%s</td>
            </tr></table>''' % (but("study", _("Study Now"), id="{}".format(studyButton_id), extra="autofocus"))

        return html
else:
    def _table(self):
            counts = list(self.mw.col.sched.counts())
            finished = not sum(counts)
            if self.mw.col.schedVer() == 1:
                for n in range(len(counts)):
                    if counts[n] >= 1000:
                        counts[n] = "1000+"
            but = self.mw.button
            if finished:
                return '<div style="white-space: pre-wrap;">%s</div>' % (
                    self.mw.col.sched.finishedMsg()
                )
            else:
                if style_mainScreenButtons:
                    #// style='height: px' -> to prevent changing main screen buttons heights
                    # based on height defined in #main {}
                    mainScreen_style = """id=main style='height: px' """
                else:
                    mainScreen_style = ""
                if style_mainScreenButtons:
                    studyButton_id = "main"
                else:
                    studyButton_id = "study"
                return """%s
    <table width=400 cellpadding=5>
    <tr><td align=center valign=top>
    <table cellspacing=5>
    <tr><td>%s:</td><td><b><span class=new-count>%s</span></b></td></tr>
    <tr><td>%s:</td><td><b><span class=learn-count>%s</span></b></td></tr>
    <tr><td>%s:</td><td><b><span class=review-count>%s</span></b></td></tr>
    </table>
    </td><td align=center>
    %s</td></tr></table>""" % (
                    bottomHTML_style,
                    _("New"),
                    counts[0],
                    _("Learning"),
                    counts[1],
                    _("To Review"),
                    counts[2],
                    but("study", _("Study Now"), id="{}".format(studyButton_id), extra="autofocus"),
                )

def _limit(counts):
    for i, count in enumerate(counts):
        if count >= 1000:
	        counts[i] = "1000+"
    return counts


#// replacing/wraping functions
Reviewer._shortcutKeys = wrap(Reviewer._shortcutKeys, _shortcutKeys_wrap, 'around')
Reviewer._showAnswerButton = _showAnswerButton
Reviewer._bottomHTML =  _bottomHTML
DeckBrowser._drawButtons = _drawButtons
Overview._renderBottom = _renderBottom
Overview._table = _table
