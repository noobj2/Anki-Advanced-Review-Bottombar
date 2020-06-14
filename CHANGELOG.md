# Changelog

All changes of the Advanced Review Bottombar will be listed here

## 2020/6/9
- Added an option to turn off more overview stats

## 2020/5/30
- Changed answer tooltip (confirmation tooltip) behavior. (now it's size won't be based on button size unless it's position is on buttons. if it's position is fixed, it'll have a small fixed size)

## 2020/5/18
- Minor code changes/improvements

## 2020/5/15
- Now it designs review buttons that other add-ons add (like rememorize). it treats them like other bottombar button so their color and style will be like other bottombar buttons
- you can style other bottombar buttons that are added by other add-on (like deferer button) you'll need to change their code a bit. if you want to style them leave a comment here or on github page. (the last picture is how the extra buttons the those add-on add look after styling them using this add-on)
- finally a github page :\ Here it is
- Changed color of timer text in bottombar, now it uses the same color you have set for other bottombar buttons text color. (not a big deal though, right?)

## 2020/5/09
- Made neon and fill designs customizable.
- Made review bottombar buttons, deck overview buttons and main screen bottombar buttons customizable.
- Added an option to change show answer button border color based on card ease.needed).
- +Other settings menu and bottombar buttons changes and improvements.

## 2020/5/02
- Pressed button count bug fix

## 2020/5/01
- Added total time and time per card to information shown in pressed button stats

## 2020/4/28
- Added an option to choose card type [learn, review, re-learn, cram] for button count stats
- Added an option to manually change decks in button count stats
- #NOTE: if you want to use this option, please use V2 scheduler. the button stats won't be accurate on V1 scheduler (because i used button names instead of ease number in stats)

## 2020/4/27
- Added an option to choose time period for button count stats
- Added an option to change button count stats scope
- Button count stats window improvements

## 2020/4/26
- New Feature: pressed review button count + percent -> in development (read changelog in about tab for more info)

## 2020/4/22
- Made styling main screen and deck overview compatible with anki versions older than 2.1.19

## 2020/4/21
- Added an option to style main screen and deck overview buttons

## 2020/4/20
- Fixed tooltip bug (where it would show hard on tooltip when you pressed good if you were in a custom study session)
- Added card info sidebard auto open

## 2020/4/18
- Minor settings menu improvements

## 2020/4/17
- Fixed neon1 style bug
- Added Correct percentage, fastest review, slowest review, card ID and note ID options to card info sidebar

## 2020/4/16
- Added change button transition time option (for fill and neon designs only)

## 2020/4/15
- Added an option to change cursor type when you hover over bottombar buttons

## 2020/4/14
- Added answer tooltips
- Adjusted tooltips for neon and fill designs
- Adjusted tooltips for custom button sizes

## 2020/4/13
- Added a function to get shortcuts (Don't have to test keys that you want to set as shortcuts anymore, if it's Anki's default shortcut for something, the add-on wont accept it)
- Moved button design tooltip to another tab (noticed it was WAY too big for lower resulotions to be useful)
- #NOTE: if you're updating from any version other than 2020/4/12 you might run into some problems trying to open settings menu
- if you can't open settings menu after update open add-on folder and delete meta.json file if that didn't help go to settings.py and put a # in front of the last line then go to tools -> add-ons and press restore defaults on this add-on's config page

## 2020/4/12
- Changed settings menu so it's easier to work with on lower resolutions (had to code it all over again)
- Made picking colors completely automatic (no color code copy/paste, choose the color and it's set)
- Added an option for you to choose settings menu's position
- Made wide buttons compatible with no distractions add-on
- #NOTE: After update you need to restore config to defaults in tools -> add-ons

## 2020/4/8
- settings menu bugs fixes
- settings menu minor adjustments for smaller screens

## 2020/4/7
- settings menu improvements
- added an option to color intervals
- added an option to style other bottombar buttons
- added 4 new button designs

## 2020/4/6
- minor settings menu improvements
- card info sidebar improvements for old scheduler

## 2020/4/5
- minor settings menu improvements
- added tooltips with pictures for different settings
- fixed card info sidebar crash bug

## 2020/4/4
- added settings menu (took nearly 1500 lines of code, you hitting the like button would really make me feel like my work is being appreciated)
- #writing the settings menu really made me tired (af) so if it's normal for it to have some bugs (tested it though, removed the bugs that i encountered). with that being said, feel free to report bugs
- minor settings menu adjustments

## 2020/4/2
- fix for wide buttons
- fixed card info sidebar problem with beta versions of anki (2.1.23 and 2.1.24)

## 2020/4/1
- fixed issue with limiting card reviews in card info sidebar
- added an option to change active button indicator from border to glow and change it's color

## 2020/3/30
- adjusted colors and gradients for background color change for light mode
- added background shadow for review buttons (enable in config)

## 2020/3/29
- added undo button (enable in config)
- fixed button color for old scheduler

## 2020/3/29
- removed conflict with customize keyboard shortcuts add-on
- removed conflict with speed focus add-on (needs to be enabled in config)
- removed conflict with slackers add-on
- added an option to choose text color in review button background color change

## 2020/3/26
- added change button size option

## 2020/3/25
- added change skip and info button position option

## 2020/3/20
- fixed conflict with "replay button on card" add-on

## 2020/3/7
- adjusted the color for review buttons
- added an option to choose the font for the text in card info side bar in config
- added an option so you could limit the maximum number of previous reviews that are shown on sidebar for a card

## 2020/3/6
- made the info sidebar customizable, you can choose what you want to see on card info sidebar in config

## 2020/3/4
- fixed not showing review button colors on new in-app night mode
- adjusted review button text colors for new in-app night mode
- adjusted wide button widths

## 2020/2/8
- added an option for you to choose the shortcut key for skip and info buttons (in add-on config)
- added an option to choose the sidebar theme (in add-on config)

## 2020/1/2
- fix for old scheduler

## 2019/12/14
- Release
