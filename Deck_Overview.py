

import time
from datetime import date, timedelta
from aqt import mw
from copy import deepcopy
from aqt.utils import shortcut, showInfo, tr
from anki import version
anki_version = int(version.replace('.', ''))
if anki_version > 2119:
    from aqt.deckbrowser import DeckBrowserBottomBar
    from aqt.overview import OverviewBottomBar
from aqt.deckbrowser import DeckBrowser
from aqt.overview import Overview
from . import styles

config = mw.addonManager.getConfig(__name__)
studyNow_label = config['Button Label_ Study Now']
more_overviewStats = config['  More Overview Stats']
bottombarButtons_style = config[' Review_ Bottombar Buttons Style']
style_mainScreenButtons = config['  Style Main Screen Buttons']

bottombar_neon1 = styles.bottombar_neon1
bottombar_neon2 = styles.bottombar_neon2
bottombar_fill1 = styles.bottombar_fill1
bottombar_fill2 = styles.bottombar_fill2

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
            b[0] = ("Shortcut key: %s") % shortcut(b[0])
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
        ["O", "opts", tr.actions_options()],
    ]
    if self.mw.col.decks.current()["dyn"]:
        links.append(["R", "refresh", tr.actions_rebuild()])
        links.append(["E", "empty", tr.studying_empty()])
    else:
        links.append(["C", "studymore", tr.actions_custom_study()])
        # links.append(["F", "cram", ("Filter/Cram")])
    if self.mw.col.sched.haveBuried():
        links.append(["U", "unbury", tr.studying_unbury()])
    links.append(["", "description", tr.scheduling_description()])
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
            b[0] = ("Shortcut key: %s") % shortcut(b[0])
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
                </td></tr>''' % (bottomHTML_style, tr.browsing_sidebar_due_today(), counts[0], counts[1], counts[2])

        if (dconf.get('new')):
            html += '''
                <tr><td nowrap="nowrap">%s:</td><td align=right>
                    <span title="new" class="new-count">%s</span>
                    <span title="learn" class="learn-count">%s</span>
                    <span title="review" class="review-count">%s</span>
                </td></tr>''' % (tr.statistics_due_tomorrow(), dueTomorrow[0],
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
        </table>''' % (tr.statistics_counts_total_cards(), totals[0], totals[1], totals[2], totals[4],
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
            </tr></table>''' % (but("study", ("{}".format(studyNow_label)), id="{}".format(studyButton_id), extra="autofocus"))

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

        labels['mature'] = tr.statistics_counts_mature_cards()
        labels['young'] = tr.statistics_counts_young_cards()
        labels['unseen'] = ('Unseen')
        labels['suspended'] = tr.statistics_counts_suspended_cards()

        labels['total'] = tr.statistics_counts_total_cards()
        labels['learned'] = ('Learned')
        labels['unlearned'] = ('Unlearned')

        labels['new'] = tr.statistics_counts_new_cards()
        labels['learning'] = tr.statistics_counts_learning_cards()
        labels['review'] = ('Review')
        # labels['due'] = ('Due')

        labels['doneDate'] = ('Done in')

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
            '''.format(button=button('study', tr.studying_study_now(), id='{}'.format(studyButton_id), extra="autofocus"))

        return output

else:
    def _table(self):
            counts = list(self.mw.col.sched.counts())
            finished = not sum(counts)
            if self.mw.col.sched_ver() == 1:
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
                    tr.actions_new(),
                    counts[0],
                    tr.scheduling_learning(),
                    counts[1],
                    tr.studying_to_review(),
                    counts[2],
                    but("study", tr.studying_study_now(), id="{}".format(studyButton_id), extra="autofocus"),
                )

def _limit(counts):
    for i, count in enumerate(counts):
        if count >= 1000:
	        counts[i] = "1000+"
    return counts


Overview._renderBottom = _renderBottom
DeckBrowser._drawButtons = _drawButtons
Overview._table = _table
