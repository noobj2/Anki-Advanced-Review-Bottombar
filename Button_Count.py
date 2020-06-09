#// auth_ Mohamad Janati
#// AmirHassan Asvadi ;)
#// Copyright (c) 2019-2020 Mohamad Janati (freaking stupid, right? :|)

#// settings -> auto open after review cleanup
#// Button to add to bottombar
#// Create a shortcut [should i add the settings to main settings? or i should add it to the other tab?]
#// If added an option for a bottombar button, don't forget to adjust tooltips and add it's own place to bottombar buttons code
# [woudln't it be easier just not to add the button :| - i mean is it really worth going through all the trouble? no one would even care]
#// Colored text inside table?

from os.path import  join, dirname
from aqt import mw
from aqt.qt import *
import time
from anki.utils import ids2str

def refreshConfig():
    global C_style_mainScreenButtons, C_button_style, C_hover_effect, C_active_indicator, C_bottombarButtons_style, C_cursor_style, C_showAnswerBorderColor_style, C_buttonTransition_time, C_colored_intervals, C_reviewTooltip, C_reviewTooltip_timer, C_reviewTooltipText_color, C_reviewTooltip_style, C_reviewTooltip_position, C_info, C_skip, C_undo, C_right_info, C_info_position, C_skip_position, C_undo_position, C_skip_shortcut, C_info_shortcut, C_undo_shortcut, C_custom_sizes, C_buttons_height, C_reviewButtons_width, C_edit_width, C_answer_width, C_more_width, C_info_width, C_skip_width, C_undo_width, C_sidebar_theme, C_sidebar_font, C_sidebar_PreviousCards, C_sidebar_reviewsToShow, C_sidebar_currentReviewCount, C_sidebar_reviewsToShow, C_sidebar_dateCreated, C_sidebar_dateEdited, C_sidebar_firstReview, C_sidebar_latestReview, C_sidebar_due, C_sidebar_interval, C_sidebar_ease, C_sidebar_numberOfReviews, C_sidebar_lapses, C_infobar_correctPercent, C_infobar_fastestReview, C_infobar_slowestReview, C_sidebar_averageTime, C_sidebar_totalTime, C_sidebar_cardType, C_sidebar_noteType, C_sidebar_deck, C_sidebar_tags, C_infobar_noteID, C_infobar_cardID, C_sidebar_sortField, C_sidebar_autoOpen, C_sidebar_warningNote, C_custom_reviewButtonColors, C_custom_reviewButtonTextColor, C_custom_activeIndicatorColor, C_custom_bottombarButtonTextColor, C_custom_bottombarButtonBorderColor, C_reviewButtonText_color, C_activeIndicator_color, C_bottombarButtonText_color, C_bottombarButtonBorder_color, C_again_color, C_againHover_color, C_hard_color, C_hardHover_color, C_good_color, C_goodHover_color, C_easy_color, C_easyHover_color, C_button_colors, C_showAnswerEase1, C_showAnswerEase2, C_showAnswerEase3, C_showAnswerEase4, C_showAnswerEase1_color, C_showAnswerEase2_color, C_showAnswerEase3_color, C_showAnswerEase4_color, C_speedFocus, C_moreOverviewStats, C_settingsMenu_palce, C_buttonCount_type, C_buttonCount_scope, C_buttonCount_timeSpinbox, C_buttonCount_period

    config = mw.addonManager.getConfig(__name__)

    C_style_mainScreenButtons = config['  Style Main Screen Buttons']

    C_button_style = config[' Review_ Buttons Style']
    C_hover_effect = config[' Review_ Hover Effect']
    C_active_indicator = config[' Review_ Active Button Indicator']
    C_bottombarButtons_style = config[' Review_ Bottombar Buttons Style']
    C_cursor_style = config[' Review_ Cursor Style']
    C_buttonTransition_time = config[' Review_ Button Transition Time']
    C_colored_intervals = config[' Review_ Colored Dues']

    C_reviewTooltip = config['Tooltip']
    C_reviewTooltip_timer = config['Tooltip Timer']
    C_reviewTooltipText_color = config['Tooltip Text Color']
    C_reviewTooltip_style = config['Tooltip Style']
    C_reviewTooltip_position = config['Tooltip Position']

    C_info = config['Button_   Info Button']
    C_skip = config['Button_   Skip Button']
    C_undo = config['Button_   Undo Button']
    C_info_position = config['Button_ Position_ Info Button']
    C_skip_position = config['Button_ Position_ Skip Button']
    C_undo_position = config['Button_ Position_ Undo Button']
    C_skip_shortcut = config ['Button_ Shortcut_ Skip Button']
    C_info_shortcut = config['Button_ Shortcut_ Info Button']
    C_undo_shortcut = config['Button_ Shortcut_ Undo Button']

    C_custom_sizes = config ['Button_  Custom Button Sizes']
    C_buttons_height = config['Button_ Height_ All Bottombar Buttons']
    C_reviewButtons_width = config['Button_ Width_ Review Buttons']
    C_edit_width = config['Button_ Width_ Edit Button']
    C_answer_width = config['Button_ Width_ Show Answer Button']
    C_more_width = config['Button_ Width_ More Button']
    C_info_width = config['Button_ Width_ Info Button']
    C_skip_width = config['Button_ Width_ Skip Button']
    C_undo_width = config['Button_ Width_ Undo Button']

    C_sidebar_theme = config['Card Info sidebar_ theme']
    C_sidebar_font = config['Card Info sidebar_ Font']
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
    C_infobar_correctPercent = config['Card Info Sidebar_ COrrect Percent']
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
    C_speedFocus = config['  Speed Focus Add-on']
    C_moreOverviewStats = config['  More Overview Stats']
    C_settingsMenu_palce = config['  Settings Menu Place']

    C_buttonCount_type = config['ButtonCount_ Type']
    C_buttonCount_scope = config['ButtonCount_ Scope']
    C_buttonCount_timeSpinbox = config['ButtonCount_ Time Spinbox']
    C_buttonCount_period = config['ButtonCount_ Period']

class StatsWindow(QDialog):
    refreshConfig()
    addon_path = dirname(__file__)
    images = join(addon_path, 'images')
    begin = "<div style='font-size: 14px'>"
    end = "</div>"
    def __init__(self, parent=None):
        super(StatsWindow, self).__init__(parent)
        self.mainWindow()

    def mainWindow(self):
        images = self.images
        self.createFirstTab()
        self.loadCurrent()

        tabs = QTabWidget()
        tabs.addTab(self.tab1, "Stats")

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)
        self.setWindowTitle("Pressed Buttons Stats")
        self.setWindowIcon(QIcon(images + "/icon.png"))

    def createFirstTab(self):
        begin = self.begin
        end = self.end
        images = self.images
        decks = mw.col.decks.all()
        deckname_list = []
        deckid_list = []
        for deck in decks:
            deck_name = deck["name"]
            deck_id = deck["id"]
            deckname_list.append(deck_name)
            deckid_list.append("({})".format(deck_id))
        refreshConfig()
        selected_type = C_buttonCount_type
        selected_scope = C_buttonCount_scope
        selected_time = C_buttonCount_timeSpinbox
        if C_buttonCount_period == 1:
            selected_time *= 60
        elif C_buttonCount_period == 2:
            selected_time *= 60*24
        elif C_buttonCount_period == 3:
            selected_time *= 60*24*7
        elif C_buttonCount_period == 4:
            selected_time *= 60*24*30
        elif C_buttonCount_period == 5:
            selected_time *= 60*24*30*12
        today = time.time()
        limit = ((today*1000) - (selected_time*60*1000))
        active_deck = ids2str(mw.col.decks.active())
        if selected_type == 0:
            type = ""
        elif selected_type == 1:
            type = "and type = 0"
        elif selected_type == 2:
            type = "and type = 1"
        elif selected_type == 3:
            type = "and type = 2"
        elif selected_type == 4:
            type = "and type = 3"
        elif selected_type == 5:
            type = "and (type = 0 or type = 2)"
        if selected_scope == 0:
            scope = ""
        elif selected_scope == 1:
            scope = "and cid in (select id from cards where did in {})".format(active_deck)
        else:
            scope = "and cid in (select id from cards where did in {})".format(deckid_list[int(selected_scope) - 2])
        pressed_again = mw.col.db.scalar("""select sum(case when ease = 1 then 1 else 0 end) from revlog where id > {} {} {}""".format(limit, type, scope))
        pressed_hard = mw.col.db.scalar("""select sum(case when ease = 2 then 1 else 0 end) from revlog where id > {} {} {}""".format(limit, type, scope))
        pressed_good = mw.col.db.scalar("""select sum(case when ease = 3 then 1 else 0 end) from revlog where id > {} {} {}""".format(limit, type, scope))
        pressed_easy = mw.col.db.scalar("""select sum(case when ease = 4 then 1 else 0 end) from revlog where id > {} {} {}""".format(limit, type, scope))
        time_again = mw.col.db.scalar("""select sum(time)/1000 from revlog where ease = 1 and id > {} {} {}""".format(limit, type, scope))
        time_hard = mw.col.db.scalar("""select sum(time)/1000 from revlog where ease = 2 and id > {} {} {}""".format(limit, type, scope))
        time_good = mw.col.db.scalar("""select sum(time)/1000 from revlog where ease = 3 and id > {} {} {}""".format(limit, type, scope))
        time_easy = mw.col.db.scalar("""select sum(time)/1000 from revlog where ease = 4 and id > {} {} {}""".format(limit, type, scope))
        if not time_again:
            time_again = 0
        if not time_hard:
            time_hard = 0
        if not time_good:
            time_good = 0
        if not time_easy:
            time_easy = 0

        if not pressed_again:
            pressed_again = 0
        if not pressed_hard:
            pressed_hard = 0
        if not pressed_good:
            pressed_good = 0
        if not pressed_easy:
            pressed_easy = 0
        pressed_all = pressed_again + pressed_hard + pressed_good + pressed_easy
        if not pressed_all:
            pressed_all = 1
        if pressed_again or pressed_hard or pressed_good or pressed_easy:
            if mw.col.schedVer() == 1:
                ease = "Ease"
                ease_1 = "1"
                ease_2 = "2"
                ease_3 = "3"
                ease_4 = "4"
            else:
                ease = "Button"
                ease_1 = "Again"
                ease_2 = "Hard"
                ease_3 = "Good"
                ease_4 = "Easy"
            buttonsCount_text = """<style>
            table, th, td {
              border: 1px solid black;
              border-collapse: collapse;
            }
            </style>
            """
            buttonsCount_text += """<table cellpadding=5 width=100%>"""
            buttonsCount_text += """<tr>"""
            buttonsCount_text += """<th width=120 align=left>{}</th><th width=120 align=left>{}</th><th width=120 align=left>{}</th><th width=120 align=left>{}</th><th width=120 align=left>{}</th>""".format(ease, "Count", "Percent", "Total Time", "Time/Card")
            buttonsCount_text += """</tr>"""
            buttonsCount_text += """<tr>""" #// """<tr {}>""".format("style='color: red' if colored else ''") -> for colored text inside them
            buttonsCount_text += """<td>{}</td><td>{}</td><td>{:.2f}%</td><td>{}</td><td>{}</td>""".format(ease_1, pressed_again, float((pressed_again/pressed_all)*100), self.time(time_again, "all"), self.time(time_again/(pressed_again if pressed_again else 1)))
            buttonsCount_text += """</tr>"""
            buttonsCount_text += """<tr>"""
            buttonsCount_text += """<td>{}</td><td>{}</td><td>{:.2f}%</td><td>{}</td><td>{}</td>""".format(ease_2, pressed_hard, float((pressed_hard/pressed_all)*100), self.time(time_hard, "all"), self.time(time_hard/(pressed_hard if pressed_hard else 1)))
            buttonsCount_text += """</tr>"""
            buttonsCount_text += """<tr>"""
            buttonsCount_text += """<td>{}</td><td>{}</td><td>{:.2f}%</td><td>{}</td><td>{}</td>""".format(ease_3, pressed_good, float((pressed_good/pressed_all)*100), self.time(time_good, "all"), self.time(time_good/(pressed_good if pressed_good else 1)))
            buttonsCount_text += """</tr>"""
            buttonsCount_text += """<tr>"""
            buttonsCount_text += """<td>{}</td><td>{}</td><td>{:.2f}%</td><td>{}</td><td>{}</td>""".format(ease_4, pressed_easy, float((pressed_easy/pressed_all)*100), self.time(time_easy, "all"), self.time(time_easy/(pressed_easy if pressed_easy else 1)))
            buttonsCount_text += """</tr>"""
            buttonsCount_text += """</table>"""
        else:
            buttonsCount_text = "No reviews found."
        if selected_scope == 1 and mw.state not in ["overview", "review"]:
            buttonsCount_text = "No active deck found.<br>Please select a deck and try again."

        reviewButton_designs = QLabel()
        reviewButton_designs.setText(buttonsCount_text)
        stats_scroll = QScrollArea()
        stats_scroll.setMinimumWidth(620)
        stats_scroll.setWidget(reviewButton_designs)
        find_button = QPushButton("Find")
        for_label = QLabel("Reviews for")
        self.type_select = QComboBox()
        self.type_select.addItems([ "All Cards", "Learn Cards", "Review Cards", "re-Learn Cards", "Cram Cards", "Learn + re-Learn Cards"])
        self.scope_select = QComboBox()
        in_label = QLabel("in")
        self.scope_select.addItems(["Whole Collection", "Current Deck"])
        self.scope_select.addItems(deckname_list)
        past_title = QLabel("in past")
        self.time_spinbox = QSpinBox()
        self.time_spinbox.setMinimum(0)
        self.period_select = QComboBox()
        self.period_select.addItems(["Minutes", "Hours", "Days", "Weeks", "Months", "Years"])
        bottom_holder = QHBoxLayout()
        bottom_holder.addWidget(find_button)
        bottom_holder.addWidget(for_label)
        bottom_holder.addWidget(self.type_select)
        bottom_holder.addWidget(in_label)
        bottom_holder.addWidget(self.scope_select)
        bottom_holder.addWidget(past_title)
        bottom_holder.addWidget(self.time_spinbox)
        bottom_holder.addWidget(self.period_select)
        find_button.clicked.connect(lambda: self.onFind())

        layout = QVBoxLayout()
        layout.addWidget(stats_scroll)
        layout.addLayout(bottom_holder)
        self.tab1 = QWidget()
        self.tab1.setLayout(layout)
    def time(self, time, time_variable=None):
        if time_variable == "all":
            if time < 60:
                return ("{:.2f} seconds".format(time))
            elif 59 < time < 3600:
                return ("{:.2f} minutes".format(time/60))
            else:
                return ("{:.2f} hours".format(time/3600))
        else:
            if time < 60:
                return ("{:.2f} s/card".format(time))
            elif 59 < time < 3600:
                return ("{:.2f} m/card".format(time/60))
            else:
                return ("{:.2f} h/card".format(time/3600))

    def loadCurrent(self):
        self.type_select.setCurrentIndex(C_buttonCount_type)
        self.scope_select.setCurrentIndex(C_buttonCount_scope)
        self.time_spinbox.setValue(int(C_buttonCount_timeSpinbox))
        self.period_select.setCurrentIndex(C_buttonCount_period)

    def onFind(self):
        conf = {
        "  Button Colors": C_button_colors,
        "  Speed Focus Add-on": C_speedFocus,
        "  More Overview Stats": C_moreOverviewStats,
        "  Settings Menu Place": C_settingsMenu_palce,
        "  Style Main Screen Buttons": C_style_mainScreenButtons,
        " Review_ Active Button Indicator": C_active_indicator,
        " Review_ Buttons Style": C_button_style,
        " Review_ Hover Effect": C_hover_effect,
        " Review_ Custom Colors": C_custom_reviewButtonColors,
        " Review_ Custom Review Button Text Color": C_custom_reviewButtonTextColor,
        " Review_ Custom Active Indicator Color": C_custom_activeIndicatorColor,
        " Review_ Bottombar Buttons Style": C_bottombarButtons_style,
        " Review_ Cursor Style": C_cursor_style,
        " Review_ Button Transition Time": C_buttonTransition_time,
        " Review_ Colored Dues": C_colored_intervals,
        "Button_   Info Button": C_info,
        "Button_   Skip Button": C_skip,
        "Button_   Undo Button": C_undo,
        "Button_  Custom Button Sizes": C_custom_sizes,
        "Button_ Shortcut_ Skip Button": C_skip_shortcut,
        "Button_ Shortcut_ Info Button": C_info_shortcut,
        "Button_ Shortcut_ Undo Button": C_undo_shortcut,
        "Button_ Position_ Info Button": C_info_position,
        "Button_ Position_ Skip Button": C_skip_position,
        "Button_ Position_ Undo Button": C_undo_position,
        "Button_ Height_ All Bottombar Buttons": C_buttons_height,
        "Button_ Width_ Edit Button": C_edit_width,
        "Button_ Width_ Show Answer Button": C_answer_width,
        "Button_ Width_ Info Button": C_info_width,
        "Button_ Width_ Skip Button": C_skip_width,
        "Button_ Width_ More Button": C_more_width,
        "Button_ Width_ Review Buttons": C_reviewButtons_width,
        "Button_ Width_ Undo Button": C_undo_width,
        "Card Info sidebar_ Number of previous cards to show": C_sidebar_PreviousCards,
        "Card Info sidebar_ theme": C_sidebar_theme,
        "Card Info sidebar_ Created": C_sidebar_dateCreated,
        "Card Info sidebar_ Edited": C_sidebar_dateEdited,
        "Card Info sidebar_ First Review": C_sidebar_firstReview,
        "Card Info sidebar_ Latest Review": C_sidebar_latestReview,
        "Card Info sidebar_ Due": C_sidebar_due,
        "Card Info sidebar_ Interval": C_sidebar_interval,
        "Card Info sidebar_ Ease": C_sidebar_ease,
        "Card Info sidebar_ Reviews": C_sidebar_numberOfReviews,
        "Card Info sidebar_ Lapses": C_sidebar_lapses,
		"Card Info Sidebar_ COrrect Percent": C_infobar_correctPercent,
		"Card Info Sidebar_ Fastest Review": C_infobar_fastestReview,
		"Card Info Sidebar_ Slowest Review": C_infobar_slowestReview,
        "Card Info sidebar_ Average Time": C_sidebar_averageTime,
        "Card Info sidebar_ Total Time": C_sidebar_totalTime,
        "Card Info sidebar_ Card Type": C_sidebar_cardType,
        "Card Info sidebar_ Note Type": C_sidebar_noteType,
        "Card Info sidebar_ Deck": C_sidebar_deck,
        "Card Info sidebar_ Tags": C_sidebar_tags,
		"Card Info Sidebar_ Note ID": C_infobar_noteID,
		"Card Info Sidebar_ Card ID": C_infobar_cardID,
        "Card Info sidebar_ Sort Field": C_sidebar_sortField,
        "Card Info sidebar_ Current Review Count": C_sidebar_currentReviewCount,
        "Card Info sidebar_ Font": C_sidebar_font,
        "Card Info sidebar_ number of reviews to show for a card": C_sidebar_reviewsToShow,
        "Card Info sidebar_ Auto Open": C_sidebar_autoOpen,
        "Card Info sidebar_ warning note": C_sidebar_warningNote,
        "Color_  General Text Color": C_reviewButtonText_color,
        "Color_ Active Button Indicator": C_activeIndicator_color,
    	"Color_ Bottombar Button Text Color": C_bottombarButtonText_color,
    	"Color_ Bottombar Button Border Color": C_bottombarButtonBorder_color,
    	"Color_ Custom Bottombar Button Text Color": C_custom_bottombarButtonTextColor,
    	"Color_ Custom Bottombar Button Border Color": C_custom_bottombarButtonBorderColor,
        "Color_ Again": C_again_color,
        "Color_ Again on hover": C_againHover_color,
        "Color_ Hard": C_hard_color,
        "Color_ Hard on hover": C_hardHover_color,
        "Color_ Good": C_good_color,
        "Color_ Good on hover": C_goodHover_color,
        "Color_ Easy": C_easy_color,
        "Color_ Easy on hover": C_easyHover_color,
        "Tooltip": C_reviewTooltip,
        "Tooltip Timer": C_reviewTooltip_timer,
        "Tooltip Text Color": C_reviewTooltipText_color,
        "Tooltip Style": C_reviewTooltip_style,
        "Tooltip Position": C_reviewTooltip_position,
        "ButtonCount_ Type": self.type_select.currentIndex(),
        "ButtonCount_ Scope": self.scope_select.currentIndex(),
        "ButtonCount_ Time Spinbox": self.time_spinbox.value(),
        "ButtonCount_ Period": self.period_select.currentIndex(),
        "ShowAnswer_ Border Color Style": C_showAnswerBorderColor_style,
        "ShowAnswer_ Ease1": C_showAnswerEase1,
		"ShowAnswer_ Ease2": C_showAnswerEase2,
		"ShowAnswer_ Ease3": C_showAnswerEase3,
		"ShowAnswer_ Ease4": C_showAnswerEase4,
		"ShowAnswer_ Ease1 Color": C_showAnswerEase1_color,
		"ShowAnswer_ Ease2 Color": C_showAnswerEase2_color,
		"ShowAnswer_ Ease3 Color": C_showAnswerEase3_color,
		"ShowAnswer_ Ease4 Color": C_showAnswerEase4_color
      }
        mw.addonManager.writeConfig(__name__, conf)
        self.accept()
        refreshConfig()
        StatsWindow().exec()

def open_stats():
    stats = StatsWindow()
    stats.exec()

config = mw.addonManager.getConfig(__name__)
StatsWindow_palce = config['  Settings Menu Place']

def setupMenu():
    if StatsWindow_palce == 1:
        stats = QAction('Pressed Review Button &Stats', mw)
        mw.form.menuTools.addAction(stats)
    else:
        stats = QAction('&Pressed Review Button Stats', mw)
        mw.ARBB_menu.addAction(stats)
        mw.form.menubar.insertMenu(mw.form.menuHelp.menuAction(), mw.ARBB_menu)
    stats.triggered.connect(open_stats)
    stats.setShortcut(QKeySequence('Shift+S'))
setupMenu()
