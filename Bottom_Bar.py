#// auth_ Mohamad Janati
#// Copyright (c) 2019-2021 Mohamad Janati (freaking stupid, right? :|)
from anki import version
anki_version = int(version.replace('.', ''))
import json
import time
from datetime import date, timedelta
from aqt import mw
import aqt
from aqt.qt import *
from aqt.utils import downArrow, shortcut, showInfo
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
more_overviewStats = config['  More Overview Stats']
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

studyNow_label = config['Button Label_ Study Now']
edit_label = config['Button Label_ Edit']
showAnswer_label = config['Button Label_ Show Answer']
more_label = config['Button Label_ More']
info_label = config['Button Label_ Info']
skip_label = config['Button Label_ Skip']
undo_label = config['Button Label_ Undo']

custom_buttonSize = config ['Button_  Custom Button Sizes']
buttons_height = config['Button_ Height_ All Bottombar Buttons']
answer_width = config['Button_ Width_ Show Answer Button']

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
        return """<button title="Shortcut key: {}" onclick="pycmd('card_info');" {}>{}</button>""".format(info_shortcut.upper(), info_style, info_label)
    else:
        return ""


#// skip button | written in a separate functions to preserve the original bottombar
def skip_button():
    if skip:
        return """<button title="Shortcut key: {}" onclick="pycmd('skip');" {}>{}</button>""".format(skip_shortcut.upper(), skip_style, skip_label)
    else:
        return ""


#// undo button
def undo_button():
    if undo:
        return """<button title="Shortcut key: {}" onclick="pycmd('undo');" {}>{}</button>""".format(undo_shortcut, undo_style, undo_label)
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
<button title="Shortcut key: E" onclick="pycmd('edit');" %(edit_style)s>%(edit_label)s</button></td>
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
<button onclick="pycmd('more');" %(more_style)s>%(more_label)s %(downArrow)s</button>
</td>
</tr>
</table>
</center>
<script>
time = %(time)d;
%(SF_bottomHTML)s
</script>
""" % dict(bottomHTML_style=bottomHTML_style, min_buttonSize=min_buttonSize, rem=self._remaining(), downArrow=downArrow(), time=self.card.timeTaken() // 1000,
    edit_style=edit_style, edit_label=edit_label, left_side1=left_side1, left_side2=left_side2, left_side3=left_side3, right_side1=right_side1,
    right_side2=right_side2, right_side3=right_side3, more_style=more_style, more_label=more_label, SF_bottomHTML=SF_bottomHTML, time_color=time_color)

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
            showAnswer_style = 'style="height: {}px; width: {}px; border-color: {};"'.format(buttons_height, answer_width, showAnswerBorder_color)
        else:
            showAnswer_style = 'style="height: {}px; width: {}px; border-color: {};" id=main'.format(buttons_height, answer_width, showAnswerBorder_color)
    else:
        if bottombarButtons_style == 0:
            showAnswer_style = "style='border-color: {}' id=ansbut".format(showAnswerBorder_color)  #// removed id=ansbut from it's own code for styling
        else:
            showAnswer_style = "style='border-color: {}' id=main".format(showAnswerBorder_color)

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
<button title="Shortcut key: Space" onclick='pycmd("ans");' %(answer_style)s>%(showAnswer_text)s</button>
%(middleRight_side1)s
%(middleRight_side2)s
%(middleRight_side3)s
</td></tr></table>''' % dict(remaining=self._remaining(), middleLeft_side1=middleLeftSide_button1, middleLeft_side2=middleLeftSide_button2, middleLeft_side3=middleLeftSide_button3,
    answer_style=showAnswer_style, middleRight_side1=middleRightSide_button1, middleRight_side2=middleRightSide_button2, middleRight_side3=middleRightSide_button3, showAnswer_text=showAnswer_text)
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


#// Deck Overview Study Now Button | code from more overview stats to add more overview stats, OBVIOUSLY
if more_overviewStats == 1:
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
            </tr></table>''' % (but("study", _("{}".format(studyNow_label)), id="{}".format(studyButton_id), extra="autofocus"))

        return html

elif more_overviewStats == 2:
    def _table(self):
        stat_colors = {
          "New" : "#00a",
          "Learning" : "#a00",
          "Review" : "#080",
          "Percent" : "#888",
          "Mature" : "#0051ff",
          "Young" : "#0051ff",
          "Learned" : "#080",
          "Unseen" : "#a00",
          "Suspended" : "#e7a100",
          "Done on Date" : "#ddd",
          "Days until done" : "#ddd",
          "Total" : "#ddd",
        }
        date_format = "%d.%m.%Y"
        correction_for_notes = 1
        last_match_length = 0
        current_deck_name = self.mw.col.decks.current()['name']
        date_format = "%m/%d/%Y"

        try:
            learn_per_day = self.mw.col.decks.confForDid(self.mw.col.decks.current()['id'])['new']['perDay']
        except:
            learn_per_day = 0

        total, mature, young, unseen, suspended, due = self.mw.col.db.first(
        u'''
          select
          -- total
          count(id),
          -- mature
          sum(case when queue = 2 and ivl >= 21
               then 1 else 0 end),
          -- young / learning
          sum(case when queue in (1, 3) or (queue = 2 and ivl < 21)
               then 1 else 0 end),
          -- unseen
          sum(case when queue = 0
               then 1 else 0 end),
          -- suspended
          sum(case when queue < 0
               then 1 else 0 end),
          -- due
          sum(case when queue = 1 and due <= ?
               then 1 else 0 end)
          from cards where did in {:s}
        '''.format(self.mw.col.sched._deckLimit()), round(time.time())
        )
        if not total:
            return u'<p> No Cards Found.</p>'

        scheduled_counts = list(self.mw.col.sched.counts())
        deck_is_finished = not sum(scheduled_counts)

        cards = {}

        cards['mature'] = mature // int(correction_for_notes)
        cards['young'] = young // int(correction_for_notes)
        cards['unseen'] = unseen // int(correction_for_notes)
        cards['suspended'] = suspended // int(correction_for_notes)

        cards['total'] = total // int(correction_for_notes)
        cards['learned'] = cards['mature'] + cards['young']
        cards['unlearned'] = cards['total'] - cards['learned']

        cards['new'] = scheduled_counts[0]
        cards['learning'] = scheduled_counts[1]
        cards['review'] = scheduled_counts[2]
        # cards['due'] = due + cards['review']

        cards['total_without_suspended'] = cards['total'] - cards['suspended']

        try:
            daysUntilDone = math.ceil(cards['unseen'] / learn_per_day)
        except:
            daysUntilDone = 0

        try:
            cards['doneDate'] = (date.today()+timedelta(days=daysUntilDone)).strftime(date_format)
        except:
            showInfo("Unsupported date format. Defaulting to Day.Month.Year instead. Use one of the shorthands: \"us\", \"asia\" or \"eu\", or specify the date like \"\%d.\%m.\%Y\", \"\%m/\%d/\%Y\" etc.\n For more information check the table at: https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior", type="warning", title="More Overview Stats 2.1 Warning")
            print(date_format)
            cards['doneDate'] = (date.today()+timedelta(days=daysUntilDone)).strftime("%d.%m.%Y")

        cards['daysLeft'] = daysUntilDone

        if(daysUntilDone == 1):
            cards['daysLeft'] = '{} day'.format(daysUntilDone)
        else:
            cards['daysLeft'] = '{} days'.format(daysUntilDone)

        cards_percent = {}

        cards_percent['mature'] = cards['mature'] * 1.0 / cards['total']
        cards_percent['young'] = cards['young'] * 1.0 / cards['total']
        cards_percent['unseen'] = cards['unseen'] * 1.0 / cards['total']
        cards_percent['suspended'] = cards['suspended'] * 1.0 / cards['total']

        cards_percent['total'] = 1.0
        cards_percent['learned'] = cards['learned'] * 1.0 / cards['total']
        cards_percent['unlearned'] = cards['unlearned'] * 1.0 / cards['total']

        cards_percent['new'] = cards['new'] * 1.0 / cards['total']
        cards_percent['learning'] = cards['learning'] * 1.0 / cards['total']
        cards_percent['review'] = cards['review'] * 1.0 / cards['total']
        # cards_percent['due'] = cards['due'] * 1.0 / cards['total']

        cards_percent_without_suspended = {}

        if(cards['total_without_suspended'] != 0):
            cards_percent_without_suspended['mature'] = cards['mature'] * 1.0 / cards['total_without_suspended']
            cards_percent_without_suspended['young'] = cards['young'] * 1.0 / cards['total_without_suspended']
            cards_percent_without_suspended['unseen'] = cards['unseen'] * 1.0 / cards['total_without_suspended']
            cards_percent_without_suspended['suspended'] = cards['suspended'] * 1.0 / cards['total_without_suspended']

            cards_percent_without_suspended['total'] = 1.0
            cards_percent_without_suspended['learned'] = cards['learned'] * 1.0 / cards['total_without_suspended']
            cards_percent_without_suspended['unlearned'] = cards['unlearned'] * 1.0 / cards['total_without_suspended']

            cards_percent_without_suspended['new'] = cards['new'] * 1.0 / cards['total_without_suspended']
            cards_percent_without_suspended['learning'] = cards['learning'] * 1.0 / cards['total_without_suspended']
            cards_percent_without_suspended['review'] = cards['review'] * 1.0 / cards['total_without_suspended']
        else:
            cards_percent_without_suspended['mature'] = 0
            cards_percent_without_suspended['young'] = 0
            cards_percent_without_suspended['unseen'] = 0
            cards_percent_without_suspended['suspended'] = 0

            cards_percent_without_suspended['total'] = 1.0
            cards_percent_without_suspended['learned'] = 0
            cards_percent_without_suspended['unlearned'] = 0

            cards_percent_without_suspended['new'] = 0
            cards_percent_without_suspended['learning'] = 0
            cards_percent_without_suspended['review'] = 0

        labels = {}

        labels['mature'] = _('Mature')
        labels['young'] = _('Young')
        labels['unseen'] = _('Unseen')
        labels['suspended'] = _('Suspended')

        labels['total'] = _('Total')
        labels['learned'] = _('Learned')
        labels['unlearned'] = _('Unlearned')

        labels['new'] = _('New')
        labels['learning'] = _('Learning')
        labels['review'] = _('Review')
        # labels['due'] = _('Due')

        labels['doneDate'] = _('Done in')

        for key in labels:
            labels[key] = u'{:s}:'.format(labels[key])

        button = self.mw.button

        output_table = u'''
          <style type="text/css">
          <!--
          hr {
            height: 1px;
            border: none;
            border-top: 1px solid #aaa;
          }

          td {
            vertical-align: top;
          }

          td.row1 {
            text-align: left;
          }

          td.row2 {
            text-align: right;
            padding-left: 1.2em;
            padding-right: 1.2em;
          }

          td.row3 {
            text-align: left;
            padding-left: 1.2em;
            padding-right: 1.2em;
          }

          td.row4 {
            text-align: right;
          }

          td.new {
            font-weight: bold;
            color: ''' + stat_colors["New"] + ''';
          }

          td.learning {
            font-weight: bold;
            color: ''' + stat_colors["Learning"] + ''';
          }

          td.review {
            font-weight: bold;
            color: ''' + stat_colors["Review"] + ''';
          }

          td.percent {
            font-weight: normal;
            color: ''' + stat_colors["Percent"] + ''';
          }

          td.mature {
            font-weight: normal;
            color: ''' + stat_colors["Mature"] + ''';
          }

          td.young {
            font-weight: normal;
            color: ''' + stat_colors["Young"] + ''';
          }

          td.learned {
            font-weight: normal;
            color: ''' + stat_colors["Learned"] + ''';
          }

          td.unseen {
            font-weight: normal;
            color: ''' + stat_colors["Unseen"] + ''';
          }

          td.suspended {
            font-weight: normal;
            color: ''' + stat_colors["Suspended"] + ''';
          }

          td.doneDate {
            font-weight: bold;
            color: ''' + stat_colors["Done on Date"] + ''';
          }

          td.daysLeft {
            font-weight: bold;
            color: ''' + stat_colors["Days until done"] + ''';
          }

          td.total {
            font-weight: bold;
            color: ''' + stat_colors["Total"] + ''';
          }
          -->
          </style>

          <table cellspacing="2">
        '''

        if not deck_is_finished:
            output_table += u'''
              <tr>
                <td class="row1">{label[new]:s}</td>
                <td class="row2 new">{cards[new]:d}</td>
                <td class="row3 percent">{percent[new]:.0%}</td>
                <td class="row4 percent">{percent2[new]:.0%}</td>
              </tr>
              <tr>
                <td class="row1">{label[learning]:s}</td>
                <td class="row2 learning">{cards[learning]:d}</td>
                <td class="row3 percent">{percent[learning]:.0%}</td>
                <td class="row4 percent">{percent2[learning]:.0%}</td>
              </tr>
              <tr>
                <td class="row1">{label[review]:s}</td>
                <td class="row2 review">{cards[review]:d}</td>
                <td class="row3 percent">{percent[review]:.0%}</td>
                <td class="row4 percent">{percent2[review]:.0%}</td>
              </tr>
              <tr>
                <td colspan="4"><hr /></td>
              </tr>
            '''.format(label=labels, cards=cards, percent=cards_percent, percent2=cards_percent_without_suspended)
        output_table += u'''
          <tr>
            <td class="row1">{label[mature]:s}</td>
            <td class="row2 mature">{cards[mature]:d}</td>
            <td class="row3 percent">{percent[mature]:.0%}</td>
            <td class="row4 percent">{percent2[mature]:.0%}</td>
          </tr>
          <tr>
            <td class="row1">{label[young]:s}</td>
            <td class="row2 young">{cards[young]:d}</td>
            <td class="row3 percent">{percent[young]:.0%}</td>
            <td class="row4 percent">{percent2[young]:.0%}</td>
          </tr>
          <tr>
            <td colspan="4"><hr /></td>
          </tr>
          <tr>
            <td class="row1">{label[learned]:s}</td>
            <td class="row2 learned">{cards[learned]:d}</td>
            <td class="row3 percent">{percent[learned]:.0%}</td>
            <td class="row4 percent">{percent2[learned]:.0%}</td>
          </tr>
          <tr>
            <td class="row1">{label[unseen]:s}</td>
            <td class="row2 unseen">{cards[unseen]:d}</td>
            <td class="row3 percent">{percent[unseen]:.0%}</td>
            <td class="row4 percent">{percent2[unseen]:.0%}</td>
          </tr>
          <tr>
            <td class="row1">{label[suspended]:s}</td>
            <td class="row2 suspended">{cards[suspended]:d}</td>
            <td class="row3 percent">{percent[suspended]:.0%}</td>
            <td class="row4 percent">ignored</td>
          </tr>
          <tr>
            <td colspan="4"><hr /></td>
          </tr>
          <tr>
            <td class="row1">{label[total]:s}</td>
            <td class="row2 total">{cards[total]:d}</td>
            <td class="row3 percent">{percent[total]:.0%}</td>
            <td class="row4 percent">{percent2[total]:.0%}</td>
          </tr>
            <td colspan="4"><hr /></td>
          <tr>
            <td class="row1">{label[doneDate]:s}</td>
            <td class="row2 daysLeft">{cards[daysLeft]:s}</td>
            <td class="row3">on:</td>
            <td class="row4 doneDate">{cards[doneDate]:s}</td>
          </tr>
        '''.format(label=labels, cards=cards, percent=cards_percent, percent2=cards_percent_without_suspended)

        output = ''

        if deck_is_finished:
            if (config == None or not 'options' in config) or (config['options'].get('Show table for finished decks', True)):
                output += output_table
                output += u'''
                  </table>
                  <hr style="margin: 1.5em 0; border-top: 1px dotted #888;" />
                '''
            output += u'''
              <div style="white-space: pre-wrap;">{:s}</div>
            '''.format(self.mw.col.sched.finishedMsg())
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

            output += output_table
            output += bottomHTML_style
            output += u'''
              <tr>
                <td colspan="4" style="text-align: center; padding-top: 0.6em;">{button:s}</td>
              </tr>
              </table>
            '''.format(button=button('study', _('Study Now'), id='{}'.format(studyButton_id), extra="autofocus"))

        return output

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
