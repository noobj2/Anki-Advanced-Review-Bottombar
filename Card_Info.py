#// auth_ Mohamad Janati
#// Copyright (c) 2019-2023 Mohamad Janati

import os
import io

from anki.hooks import addHook
from aqt.qt import *
from aqt.webview import AnkiWebView
import aqt.stats
import time
import datetime
from anki.lang import _
from anki.utils import fmtTimeSpan
from anki.stats import CardStats
from aqt import *
from aqt.utils import showInfo
from anki.utils import html_to_text_line
from anki.collection import _Collection
from aqt.reviewer import Reviewer


#// sidebar functions
class StatsSidebar(object):
    def __init__(self, mw):
        config = mw.addonManager.getConfig(__name__)
        sidebar_autoOpen = config['Card Info sidebar_ Auto Open']
        self.mw = mw
        self.shown = False
        addHook("showQuestion", self._update)
        addHook("reviewCleanup", self._update)
        if sidebar_autoOpen:
                addHook("showQuestion", self.show)

    def _addDockable(self, title, w):
        class DockableWithClose(QDockWidget):
            closed = pyqtSignal()
            def closeEvent(self, evt):
                self.closed.emit()
                QDockWidget.closeEvent(self, evt)
        dock = DockableWithClose(title, mw)
        dock.setObjectName(title)
        dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)
        # dock.setFeatures(QDockWidget.AllDockWidgetFeatures)
        dock.setWidget(w)
        if mw.width() < 600:
            mw.resize(QSize(600, mw.height()))
        mw.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)
        return dock

    def _remDockable(self, dock):
        mw.removeDockWidget(dock)

    def show(self):
        if not self.shown:
            class ThinAnkiWebView(AnkiWebView):
                def sizeHint(self):
                    return QSize(200, 100)
            self.web = ThinAnkiWebView()
            self.shown = self._addDockable("Card Info", self.web)
            self.shown.closed.connect(self._onClosed)
        self._update()

    def hide(self):
        if self.shown:
            self._remDockable(self.shown)
            self.shown = None

    def toggle(self):
        if self.shown:
            self.hide()
        else:
            self.show()

    def _onClosed(self):
        # schedule removal for after evt has finished
        self.mw.progress.timer(100, self.hide, False)

    # modified _revlogData function
    def _revlogData_mod(self, card, card_stats):
        config = mw.addonManager.getConfig(__name__)
        sidebar_font = config['Card Info sidebar_ Font']
        reviewsToShow = config['Card Info sidebar_ number of reviews to show for a card']
        limited_review_warning_note = config['Card Info sidebar_ warning note']
        custom_colors = config[' Review_ Custom Colors']
        again_color = config['Color_ Again']
        hard_color = config['Color_ Hard']
        good_color = config['Color_ Good']
        easy_color = config['Color_ Easy']
        entries = self.mw.col.db.all("select id/1000.0, ease, ivl, factor, time/1000.0, type from revlog where cid = ?", card.id)
        if not entries:
            return ""
        s = "<div style='text-align: center; font-family: arial; font-weight: bold;'> Reviews </div>"
        s += ("<style>th {font-family: %s; font-size: 13px;}</style><table width=100%% ><tr><th align=left>%s</th>") % (sidebar_font, "Date")
        s += ("<th align=center >%s</th>" * 5) % ("Type", "Button", "Interval", "Ease", "Time")
        cnt = 0
        for (date, ease, ivl, factor, taken, type) in reversed(entries):
            cnt += 1
            s += "<tr><td>%s</td>" % time.strftime("<b>%y/%m/%d</b><br>%H:%M", time.localtime(date))
            tstr = ["Learn", "Review", "Relearn", "Filtered", "Resched"][type]
            import anki.stats as st

            fmt = "<span style='color:%s'>%s</span>"
            if type == 0:
                tstr = fmt % (st.colLearn, tstr)
            elif type == 1:
                tstr = fmt % (st.colMature, tstr)
            elif type == 2:
                tstr = fmt % (st.colRelearn, tstr)
            elif type == 3:
                tstr = fmt % (st.colCram, tstr)
            else:
                tstr = fmt % ("#000", tstr)
            if ease == 1:
                tstr = fmt % (st.colRelearn, tstr)
                ####################
            int_due = "%s" % time.strftime("%y/%m/%d", time.localtime(date))
            if ivl > 0:
                int_due_date = time.localtime(date + (ivl * 24 * 60 * 60))
                int_due = time.strftime("%y/%m/%d", int_due_date)
                ####################
            if ivl == 0:
                ivl = "0d"
            elif ivl > 0:
                ivl = fmtTimeSpan(ivl * 86400, short=True)
            else:
                ivl = card_stats.time(-ivl)

            if not custom_colors:
                again_color = "#FF1111"
                hard_color = "#FF9814"
                good_color = "#33FF2D"
                easy_color = "#21C0FF"
            if self.mw.col.sched_ver() == 1 and type == 3:
                if ease == 1:
                    button = f"<div style='color: {again_color};'>Again</div>"
                elif ease == 2:
                    button = f"<div style='color: {good_color};'>Good</div>"
                elif ease == 3:
                    button = f"<div style='color: {good_color};'>Good</div>"
                elif ease == 4:
                    button = f"<div style='color: {easy_color};'>Easy</div>"
                else:
                    button = f"ease: {ease}"
            elif self.mw.col.sched_ver() == 1 and (type == 0 or type == 2):
                if ease == 1:
                    button = f"<div style='color: {again_color};'>Again</div>"
                elif ease == 2:
                    button = f"<div style='color: {good_color};'>Good</div>"
                elif ease == 3:
                    button = f"<div style='color: {easy_color};'>Easy</div>"
                elif ease == 4:
                    button = f"<div style='color: {easy_color};'>Easy</div>"
                else:
                    button = f"ease: {ease}"
            else:
                if ease == 1:
                    button = f"<div style='color: {again_color};'>Again</div>"
                elif ease == 2:
                    button = f"<div style='color: {hard_color};'>Hard</div>"
                elif ease == 3:
                    button = f"<div style='color: {good_color};'>Good</div>"
                elif ease == 4:
                    button = f"<div style='color: {easy_color};'>Easy</div>"
                else:
                    button = f"ease: {ease}"
            if not factor:
                factor_text = ''
            else:
                factor = factor / 10
                if factor <= 110:
                    factor_text = f"D:{round(factor - 10)}"
                else:
                    factor_text = f"{round(factor)}"
            s += ("<td align=center>%s</td>" * 5) % (tstr, button, "%s<br>(%s)" %(ivl, int_due), "%s%%" % factor_text, card_stats.time(taken)) + "</tr>"
            # Stability stat for future updates
            # showInfo(f"{self.mw.col.compute_memory_state(card.id)}")
            if reviewsToShow != 0:
                if cnt > int(reviewsToShow) - 1:
                    break
            else:
                continue
        s += "</table>"
        warning = ""
        if limited_review_warning_note:
            if cnt < card.reps:
                try:
                    a = int(reviewsToShow)
                    warning = f"""<div style="font-family: consolas; font-size: 12px;"><hr> You have limited previous review information number to "{reviewsToShow}" reviews.</div>"""
                except ValueError:
                    warning = """<div style="font-family: consolas; font-size: 12px;"><hr>Some of the history is missing. For more information, please see the browser documentation.</div>"""
        return s + warning


    # adds the modified _revlogData function to Reviewer class in aqt.browser
    Reviewer._revlogData_mod = _revlogData_mod


    # modified report function
    def report_mod(self):
        from anki import version
        anki_version = int(version.replace('.', ''))
        if anki_version > 2119:
            from aqt.theme import theme_manager
        config = mw.addonManager.getConfig(__name__)

        infobar_created = config['Card Info sidebar_ Created']
        infobar_edited = config['Card Info sidebar_ Edited']
        infobar_firstReview = config['Card Info sidebar_ First Review']
        infobar_latestReview = config['Card Info sidebar_ Latest Review']
        infobar_due = config['Card Info sidebar_ Due']
        infobar_interval = config['Card Info sidebar_ Interval']
        infobar_ease = config['Card Info sidebar_ Ease']
        infobar_reviews = config['Card Info sidebar_ Reviews']
        infobar_lapses = config['Card Info sidebar_ Lapses']
        infobar_correctPercent = config['Card Info Sidebar_ Correct Percent']
        infobar_fastestReview = config['Card Info Sidebar_ Fastest Review']
        infobar_slowestReview = config['Card Info Sidebar_ Slowest Review']
        infobar_avgTime = config['Card Info sidebar_ Average Time']
        infobar_totalTime = config['Card Info sidebar_ Total Time']
        infobar_cardType = config['Card Info sidebar_ Card Type']
        infobar_noteType = config['Card Info sidebar_ Note Type']
        infobar_deck = config['Card Info sidebar_ Deck']
        infobar_tags = config['Card Info sidebar_ Tags']
        infobar_noteID = config['Card Info Sidebar_ Note ID']
        infobar_cardID = config['Card Info Sidebar_ Card ID']
        infobar_sortField = config['Card Info sidebar_ Sort Field']

        c = self.card
        fmt = lambda x, **kwargs: fmtTimeSpan(x, short=True, **kwargs)
        self.txt = "<table width=100%>"
        if infobar_created:
            self.addLine("Created", time.strftime("%Y-%m-%d | %H:%M", time.localtime(c.id/1000)))
        if infobar_edited:
            if c.note().mod != False and time.localtime(c.id/1000) != time.localtime(c.note().mod):
                self.addLine("Edited", time.strftime("%Y-%m-%d | %H:%M", time.localtime(c.note().mod)))
        first = self.col.db.scalar("select min(id) from revlog where cid = ?", c.id)
        last = self.col.db.scalar("select max(id) from revlog where cid = ?", c.id)
        if first:
            if infobar_firstReview:
                self.addLine("First Review", time.strftime("%Y-%m-%d | %H:%M", time.localtime(first/1000)))
            if infobar_latestReview:
                self.addLine("Latest Review", time.strftime("%Y-%m-%d | %H:%M", time.localtime(last/1000)))
        if c.type != 0:
            if c.odid or c.queue < 0:
                next = None
            else:
                if c.queue in (2,3):
                    next = time.time()+((c.due - self.col.sched.today)*86400)
                else:
                    next = c.due
                next = self.date(next)
            if next:
                if infobar_due:
                    self.addLine("Due", next)
            if c.queue == 2:
                if infobar_interval:
                    self.addLine("Interval", fmt(c.ivl * 86400))
            if infobar_ease:
                self.addLine("Ease", "%d%%" % (c.factor/10.0))
            if infobar_lapses:
                self.addLine("Lapses", "%d" % c.lapses)
            if self.col.sched_ver() == 1:
                pressed_again = mw.col.db.scalar("select sum(case when ease = 1 then 1 else 0 end) from revlog where cid = ?", c.id)
                pressed_good = mw.col.db.scalar("select sum(case when ease = 2 then 1 else 0 end) from revlog where cid = ?", c.id)
                pressed_easy = mw.col.db.scalar("select sum(case when ease = 3 then 1 else 0 end) from revlog where cid = ?", c.id)
                if not pressed_again:
                    pressed_again = 0
                if not pressed_hard:
                    pressed_hard = 0
                if not pressed_good:
                    pressed_good = 0
                if not pressed_easy:
                    pressed_easy = 0
                pressed_all = pressed_again + pressed_good + pressed_easy
                if pressed_all == 0:
                    pressed_all = 1
                self.addLine("Again", "{} | {:.0f}%".format(str(pressed_again).rjust(4), float(pressed_again/pressed_all)*100))
                self.addLine("Good", "{} | {:.0f}%".format(str(pressed_good).rjust(4), float(pressed_good/pressed_all)*100))
                self.addLine("Easy", "{} | {:.0f}%".format(str(pressed_easy).rjust(4), float(pressed_easy/pressed_all)*100))
            elif self.col.sched_ver() == 2:
                pressed_again = mw.col.db.scalar("select sum(case when ease = 1 then 1 else 0 end) from revlog where cid = ?", c.id)
                pressed_hard = mw.col.db.scalar("select sum(case when ease = 2 then 1 else 0 end) from revlog where cid = ?", c.id)
                pressed_good = mw.col.db.scalar("select sum(case when ease = 3 then 1 else 0 end) from revlog where cid = ?", c.id)
                pressed_easy = mw.col.db.scalar("select sum(case when ease = 4 then 1 else 0 end) from revlog where cid = ?", c.id)
                if not pressed_again:
                    pressed_again = 0
                if not pressed_hard:
                    pressed_hard = 0
                if not pressed_good:
                    pressed_good = 0
                if not pressed_easy:
                    pressed_easy = 0
                pressed_all = pressed_again + pressed_hard + pressed_good + pressed_easy
                if pressed_all == 0:
                    pressed_all = 1
                self.addLine("Again", "{} | {:.0f}%".format(str(pressed_again).rjust(4), float(pressed_again/pressed_all)*100))
                self.addLine("Hard", "{} | {:.0f}%".format(str(pressed_hard).rjust(4), float(pressed_hard/pressed_all)*100))
                self.addLine("Good", "{} | {:.0f}%".format(str(pressed_good).rjust(4), float(pressed_good/pressed_all)*100))
                self.addLine("Easy", "{} | {:.0f}%".format(str(pressed_easy).rjust(4), float(pressed_easy/pressed_all)*100))
            if infobar_reviews:
                self.addLine("Reviews", "%d" % c.reps)
            (cnt, total) = self.col.db.first("select count(), sum(time)/1000 from revlog where cid = ?", c.id)
            if infobar_correctPercent and c.reps > 0:
                self.addLine("Correct Percentage", "{:.0f}%".format(float((c.reps-c.lapses)/c.reps)*100))
            if infobar_fastestReview:
                fastes_rev = mw.col.db.scalar("select time/1000.0 from revlog where cid = ? order by time asc limit 1", c.id)
                self.addLine("Fastest Review", self.time(fastes_rev))
            if infobar_slowestReview:
                slowest_rev = mw.col.db.scalar("select time/1000.0 from revlog where cid = ? order by time desc limit 1", c.id)
                self.addLine("Slowest Review", self.time(slowest_rev))
            if cnt:
                if infobar_avgTime:
                    self.addLine("Average Time", self.time(total / float(cnt)))
                if infobar_totalTime:
                    self.addLine("Total Time", self.time(total))
        elif c.queue == 0:
            if infobar_due:
                self.addLine("Position", c.due)
        if infobar_cardType:
            self.addLine("Card Type", c.template()['name'])
        if infobar_noteType:
            self.addLine("Note Type", c.model()['name'])
        if infobar_noteID:
            self.addLine("Note ID", c.nid)
        if infobar_cardID:
            self.addLine("Card ID", c.id)
        if infobar_deck:
            self.addLine("Deck", self.col.decks.name(c.did))
        if c.note().tags:
            if infobar_tags:
                self.addLine("Tags", " | ".join(c.note().tags))
        f = c.note()
        sort_field = html_to_text_line(f.fields[self.col.models.sortIdx(f.model())])
        if infobar_sortField:
            if len(sort_field) > 40:
                self.addLine("Sort Field", "[{}<br>{}<br>{}...]".format(sort_field[:20], sort_field[20:41], sort_field[41:58]))
            else:
                self.addLine("Sort Field", html_to_text_line(f.fields[self.col.models.sortIdx(f.model())]))
        self.txt += "</table>"
        return self.txt


    # adds the modified report functions to CardStats class in anki.stats
    CardStats.report_mod = report_mod


    # modified cardStats function
    def cardStats_mod(self, card):
        from anki.stats import CardStats
        return CardStats(self, card).report_mod()


     # adds a modified cardStats function to _Collection class in anki.collection
    _Collection.cardStats_mod = cardStats_mod


    # functions to get more previous cards to add them to sidebard
    def lastCard2(self):
        if self._answeredIds:
            if len(self._answeredIds) > 1:
                try:
                    return self.mw.col.getCard(self._answeredIds[-2])
                except TypeError:
                    return
    def lastCard3(self):
        if self._answeredIds:
            if len(self._answeredIds) > 2:
                try:
                    return self.mw.col.getCard(self._answeredIds[-3])
                except TypeError:
                    return
    def lastCard4(self):
        if self._answeredIds:
            if len(self._answeredIds) > 3:
                try:
                    return self.mw.col.getCard(self._answeredIds[-4])
                except TypeError:
                    return

    # adds functions above to Reviewer class in aqt.reviewer
    Reviewer.lastCard2 = lastCard2
    Reviewer.lastCard3 = lastCard3
    Reviewer.lastCard4 = lastCard4


    def _update(self):
        config = mw.addonManager.getConfig(__name__)
        hide_current_card = config['Card Info sidebar_ Hide Current Card']
        infobar_currentReviewCount = config['Card Info sidebar_ Current Review Count']
        try:
            sidebar_PreviousCards = int(config['Card Info sidebar_ Number of previous cards to show'])
        except ValueError:
            sidebar_PreviousCards = 2
        if not self.shown:
            return
        txt = ""
        r = self.mw.reviewer
        d = self.mw.col
        card_stats = CardStats(d, r.card)
        current_card = r.card
        review_count = len(self.mw.reviewer._answeredIds)
        styles = """<style>
        .title {
          font-family: arial;
          padding-bottom: 15px;
          font-weight: bold;
        }</style>"""
        currentReviewCount = f"<div class='title'>Current Card</div><div style='font-family: courier; font-size: 10px;'>Current Review Count: {review_count}</div>"
        if current_card and not hide_current_card:
            txt += styles
            if infobar_currentReviewCount:
                txt += currentReviewCount
            else:
                txt += "<div class='title'>Current Card</div>"
            txt += d.cardStats_mod(current_card)
            txt += "<p>"
            txt += r._revlogData_mod(current_card, card_stats)
            card2 = r.lastCard()
            if card2 and sidebar_PreviousCards > 1:
                if sidebar_PreviousCards == 2:
                    txt += "<hr><div class='title'>Last Card</div>"
                else:
                    txt += "<hr><div class='title'>Card 2</div>"
                txt += d.cardStats_mod(card2)
                txt += "<p>"
                txt += r._revlogData_mod(card2, card_stats)
                if sidebar_PreviousCards < 3:
                    if infobar_currentReviewCount:
                        txt += currentReviewCount
                card3 = r.lastCard2()
                if card3 and sidebar_PreviousCards > 2:
                    txt += "<hr><div class='title''>Card 3</div>"
                    txt += d.cardStats_mod(card3)
                    txt += "<p>"
                    txt += r._revlogData_mod(card3, card_stats)
                    if sidebar_PreviousCards < 4:
                        if infobar_currentReviewCount:
                            txt += currentReviewCount
                    card4 = r.lastCard3()
                    if card4 and sidebar_PreviousCards > 3:
                        txt += "<hr><div class='title''>Card 4</div>"
                        txt += d.cardStats_mod(card4)
                        txt += "<p>"
                        txt += r._revlogData_mod(card4, card_stats)
                        if infobar_currentReviewCount:
                            txt += currentReviewCount
        if not txt:
            styles = """<style>
        .title {
          font-family: arial;
          padding-bottom: 15px;
          font-weight: bold;
        }</style>"""
            txt = styles
            card2 = r.lastCard()
            if card2 and sidebar_PreviousCards > 1:
                txt += "<div class='title'>Last Card</div>"
                txt += d.cardStats_mod(card2)
                txt += "<p>"
                txt += r._revlogData_mod(card2, card_stats)
                if sidebar_PreviousCards < 3:
                    if infobar_currentReviewCount:
                        txt += currentReviewCount
                card3 = r.lastCard2()
                if card3 and sidebar_PreviousCards > 2:
                    txt += "<hr><div class='title''>Card 2</div>"
                    txt += d.cardStats_mod(card3)
                    txt += "<p>"
                    txt += r._revlogData_mod(card3, card_stats)
                    if sidebar_PreviousCards < 4:
                        if infobar_currentReviewCount:
                            txt += currentReviewCount
                    card4 = r.lastCard3()
                    if card4 and sidebar_PreviousCards > 3:
                        txt += "<hr><div class='title''>Card 3</div>"
                        txt += d.cardStats_mod(card4)
                        txt += "<p>"
                        txt += r._revlogData_mod(card4, card_stats)
                        if infobar_currentReviewCount:
                            txt += currentReviewCount
        style = self._style()
        self.web.setHtml("""
<html>
    <head>
        <style>%s</style>
    </head>
        <body>
            <center>%s</center>
        </body>
</html>
"""% (style, txt))


    def _style(self):
        from anki import version
        anki_version = int(version.replace('.', ''))
        if anki_version > 2119:
            from aqt.theme import theme_manager
        config = mw.addonManager.getConfig(__name__)
        sidebar_theme = config['Card Info sidebar_ theme']
        sidebar_font = config['Card Info sidebar_ Font']
        from . import styles
        dark_styles = styles.dark
        light_styles = styles.light
        if anki_version > 2119:
            if sidebar_theme == 2:
                mystyle = dark_styles
            elif sidebar_theme == 1:
                mystyle = light_styles
            else:
                if theme_manager.night_mode:
                    mystyle = dark_styles
                else:
                    mystyle = light_styles
        else:
            if sidebar_theme == 2:
                mystyle = dark_styles
            else:
                mystyle = light_styles


        from anki import version
        if version.startswith("2.0."):
            return ""
        return mystyle + "td { font-size: 75%; font-family:" + f"{sidebar_font}" + ";}"


_card_stats = StatsSidebar(mw)


def cardStats(on):
    _card_stats.toggle()
