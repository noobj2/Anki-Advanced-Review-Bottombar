#// auth_ Mohamad Janati
#// Copyright (c) 2019-2023 Mohamad Janati

from aqt import mw
from anki import version
anki_version = int(version.replace('.', ''))

is_nightMode = False
if anki_version > 2119:
    from aqt.theme import theme_manager
    is_nightMode = theme_manager.night_mode

#// getting config information
config = mw.addonManager.getConfig(__name__)

#// getting colors that user defined in config
again_color = config['Color_ Again']
again_hover_color = config['Color_ Again on hover']
hard_color = config['Color_ Hard']
hard_hover_color = config['Color_ Hard on hover']
good_color = config['Color_ Good']
good_hover_color = config['Color_ Good on hover']
easy_color = config['Color_ Easy']
easy_hover_color = config['Color_ Easy on hover']
button_style = config[' Review_ Buttons Style']
custom_colors = config[' Review_ Custom Colors']
hover_effect = config[' Review_ Hover Effect']
active_indicator = config[' Review_ Active Button Indicator']
bottombarButtons_style = config[' Review_ Bottombar Buttons Style']
textColor_background = config['Color_  General Text Color']
activeIndicator_color = config['Color_ Active Button Indicator']
bottombarButtonText_color = config['Color_ Bottombar Button Text Color']
bottombarButtonBorder_color = config['Color_ Bottombar Button Border Color']
custom_bottombarButtonTextColor = config['Color_ Custom Bottombar Button Text Color']
custom_bottombarButtonBorderColor = config['Color_ Custom Bottombar Button Border Color']
custom_buttonSize = config ['Button_  Custom Button Sizes']
buttons_height = config['Button_ Height_ All Bottombar Buttons']
edit_width = config['Button_ Width_ Edit Button']
# answer_width = config['Button_ Width_ Show Answer Button']
info_width = config['Button_ Width_ Info Button']
skip_width = config['Button_ Width_ Skip Button']
text_size = config["Button_ Text Size"]
showSkipped_width = config['Button_ Width_ Show Skipped Button']
undo_width = config['Button_ Width_ Undo Button']
more_width = config['Button_ Width_ More Button']
custom_activeIndicatorColor = config[" Review_ Custom Active Indicator Color"]
custom_reviewButtonTextColor = config[" Review_ Custom Review Button Text Color"]
cursor_style = config[' Review_ Cursor Style']
transition = "{}s".format(float(config[' Review_ Button Transition Time']/1000))
border_radius = "{}px".format(config[' Review_ Button Border Radius'])
font_weights = [100, 200, 300, 400, 500, 600, 700, 800, 900]
buttonFontWeight = font_weights[int(config['Button_ Font Weight'])]

######//////__BEGIN__ EXTRAS __BEGIN__//////######
#// replacing textColor with "default" if custom review button text color is disabled
if custom_reviewButtonTextColor == False:
    textColor_background = "default"

#//replacing indicator color with "default" is custom active indicator color is disabled
if custom_activeIndicatorColor == False:
    activeIndicator_color = "default"

#// Choosing cursor style
if cursor_style == 0:
    cursor = "normal"
elif cursor_style == 1:
    cursor = "pointer"

#// Choosing button text color
if not custom_reviewButtonTextColor:
    if is_nightMode:
        textColor = "#dedede"
        if button_style > 3:
            textColor = "black"
    else:
        textColor = "black"
else:
    textColor = textColor_background

#// choosing color for general buttons
if custom_bottombarButtonTextColor:
    bottombarButton_textColor = bottombarButtonText_color
else:
    if is_nightMode:
        bottombarButton_textColor = "#F0F0F0"
    else:
        bottombarButton_textColor = "#2F2F31"

#// choosing border color for general buttons
if custom_bottombarButtonBorderColor:
    border_color = bottombarButtonBorder_color
else:
    if is_nightMode:
        if bottombarButtons_style == 0:
            border_color = ""
        elif bottombarButtons_style in [1, 2]:
            border_color = "#939399"
        elif bottombarButtons_style == 3:
            border_color = "#dedede"
        elif bottombarButtons_style == 4:
            border_color = "#BFBFC7"
    else:
        if bottombarButtons_style == 0:
            border_color = ""
        elif bottombarButtons_style == 1:
            border_color = "#404040"
        elif bottombarButtons_style == 2:
            border_color = "#939399"
        elif bottombarButtons_style in[3, 4]:
            border_color = "#080808"

#// setting colors for neon and fill designs when custom colors is disabled
if not custom_colors:
    again_color = "#FF1111"
    hard_color = "#FF9814"
    good_color = "#33FF2D"
    easy_color = "#21C0FF"

######//////__END__ EXTRAS __END__ //////######

######//////__BEGIN__ GENERAL BUTTON DESIGNS __BEGIN__ //////######
#// changing height and width of bottombar buttons based on button design or sizes that user has given
#// bottomHTML_style makes us able to add classes ids or edit bottombar buttons altogether
#// edit_style, info_style, etc. make us able to define classes, ids or add styles to each button
#// classes and ids should be defined in bottomHTML_style first
if is_nightMode:
    bottombar_neon1 = """
    #main {
      padding: 5px 20px;
      color: %(text)s;
      border: 1px solid %(border_color)s;
      border-radius: %(border_radius)s !important;
      font-weight: %(font_weight)s;
      background: none;
      cursor: %(cursor)s;
      transition: %(transition)s;
    }
    #main:hover {
      background: %(text)s;
      border-radius: %(border_radius)s !important;
      color: black;
      box-shadow: 0 2px 10px 0 %(text)s;
    }
    """ % dict (text=bottombarButton_textColor, border_color=border_color, border_radius=border_radius, font_weight=buttonFontWeight, cursor=cursor, transition=transition)
    bottombar_neon2 = """
    #main {
      padding: 5px 20px;
      color: black;
      border: 1px solid %(border_color)s;
      border-radius: %(border_radius)s !important;
      font-weight: %(font_weight)s;
      background: %(text)s;
      cursor: %(cursor)s;
      transition: %(transition)s;
      box-shadow: 0 2px 10px 0 %(text)s;
    }
    #main:hover {
      background: none;
      border-radius: %(border_radius)s !important;
      color: %(text)s;
      box-shadow: none;
    }
    """ % dict (text=bottombarButton_textColor, border_color=border_color, border_radius=border_radius, font_weight=buttonFontWeight, cursor=cursor, transition=transition)
    bottombar_fill1 = """
    #main {
      padding: 5px 20px;
      border: 1px solid %(border_color)s;
      background: none;
      cursor: %(cursor)s;
      transition: %(transition)s;
      position: relative;
      overflow: hidden;
      border-radius: %(border_radius)s !important;
      font-weight: %(font_weight)s;
      color: %(text)s;
    }
    #main:hover {
      color: #2F2F31;
    }
    #main::before {
      content: "";
      position: absolute;
      left: 0;
      width: 100%%;
      height: 0%%;
      background: %(text)s;
      z-index: -1;
      transition: %(transition)s;
      bottom: 0;
      border-radius: 50%% 50%% 0 0;
    }
    #main:hover::before {
      height: 180%%;
    }
    """ % dict(text=bottombarButton_textColor, border_color=border_color, cursor=cursor, transition=transition, border_radius=border_radius, font_weight=buttonFontWeight)
    bottombar_fill2 = """
        #main {
          padding: 5px 20px;
          border: 1px solid %(border_color)s;
          background: none;
          cursor: %(cursor)s;
          transition: %(transition)s;
          position: relative;
          overflow: hidden;
          border-radius: %(border_radius)s !important;
          font-weight: %(font_weight)s;
          color: black;
        }
        #main:hover {
          color: %(text)s;
        }
        #main::before {
          content: "";
          position: absolute;
          left: 0;
          width: 100%%;
          height:180%%;
          background: %(text)s;
          z-index: -1;
          transition: %(transition)s;
          bottom: 0;
          border-radius: 50%% 50%% 0 0;
        }
        #main:hover::before {
          height: 0%%;
        }
        """ % dict(text=bottombarButton_textColor, border_color=border_color, cursor=cursor, transition=transition, border_radius=border_radius, font_weight=buttonFontWeight)
else:
    bottombar_neon1 = """
    #main {
      padding: 5px 20px;
      color: %(text)s;
      border: 1px solid %(border_color)s;
      border-radius: %(border_radius)s !important;
      font-weight: %(font_weight)s;
      background: none;
      cursor: %(cursor)s;
      transition: %(transition)s;
    }
    #main:hover {
      background: %(text)s;
      border-radius: %(border_radius)s !important;
      color: #f0f0f0;
      box-shadow: 0 2px 10px 0 %(text)s;
    }
    """ % dict (text=bottombarButton_textColor, border_color=border_color, border_radius=border_radius, font_weight=buttonFontWeight, cursor=cursor, transition=transition)
    bottombar_neon2 = """
    #main {
      padding: 5px 20px;
      color: white;
      border: 1px solid %(border_color)s;
      border-radius: %(border_radius)s !important;
      font-weight: %(font_weight)s;
      background: %(text)s;
      cursor: %(cursor)s;
      transition: %(transition)s;
      box-shadow: 0 2px 10px 0 %(text)s;
    }
    #main:hover {
      border: 1px solid %(text)s;
      background: none;
      border-radius: %(border_radius)s !important;
      color: %(text)s;
      box-shadow: none;
    }
    """ % dict (text=bottombarButton_textColor, border_color=border_color, border_radius=border_radius, font_weight=buttonFontWeight, cursor=cursor, transition=transition)
    bottombar_fill1 = """
    #main {
      padding: 5px 20px;
      border: 1px solid %(border_color)s;
      background: none;
      cursor: %(cursor)s;
      transition: %(transition)s;
      position: relative;
      overflow: hidden;
      border-radius: %(border_radius)s !important;
      font-weight: %(font_weight)s;
      color: %(text)s;
    }
    #main:hover {
      color: white;
    }
    #main::before {
      content: "";
      position: absolute;
      left: 0;
      width: 100%%;
      height: 0%%;
      background: %(text)s;
      z-index: -1;
      transition: %(transition)s;
      bottom: 0;
      border-radius: 50%% 50%% 0 0;
    }
    #main:hover::before {
      height: 180%%;
    }
    """ % dict(text=bottombarButton_textColor, border_color=border_color, cursor=cursor, transition=transition, border_radius=border_radius, font_weight=buttonFontWeight)
    bottombar_fill2 = """
        #main {
          padding: 5px 20px;
          border: 1px solid %(border_color)s;
          background: none;
          cursor: %(cursor)s;
          transition: %(transition)s;
          position: relative;
          overflow: hidden;
          border-radius: %(border_radius)s !important;
          font-weight: %(font_weight)s;
          color: white;
        }
        #main:hover {
          color: %(text)s;
        }
        #main::before {
          content: "";
          position: absolute;
          left: 0;
          width: 100%%;
          height:180%%;
          background: %(text)s;
          z-index: -1;
          transition: %(transition)s;
          bottom: 0;
          border-radius: 50%% 50%% 0 0;
        }
        #main:hover::before {
          height: 0%%;
        }
        """ % dict(text=bottombarButton_textColor, border_color=border_color, cursor=cursor, transition=transition, border_radius=border_radius, font_weight=buttonFontWeight)

if custom_buttonSize:
    if bottombarButtons_style == 0:
        edit_style = f'style="height: {buttons_height}px; width: {edit_width}px; font-size: {text_size}px;"'
        info_style = f'style="height: {buttons_height}px; width: {info_width}px; font-size: {text_size}px;"'
        skip_style = f'style="height: {buttons_height}px; width: {skip_width}px; font-size: {text_size}px;"'
        showSkipped_style = f'style="height: {buttons_height}px; width: {showSkipped_width}px; font-size: {text_size}px;"'
        undo_style = f'style="height: {buttons_height}px; width: {undo_width}px; font-size: {text_size}px;"'
        more_style = f'style="height: {buttons_height}px; width: {more_width}px; font-size: {text_size}px;"'
        min_buttonSize = """
        <style>
          button {
            min-width: 5px;
            cursor: %(cursor)s;
            border-radius: %(border_radius)s !important;
            font-weight: %(font_weight)s;
            }
        </style>
        """ %dict(cursor=cursor, border_radius=border_radius, font_weight=buttonFontWeight)
    else:
        edit_style = f'style="height: {buttons_height}px; width: {edit_width}px; font-size: {text_size}px;" id=main'
        info_style = f'style="height: {buttons_height}px; width: {info_width}px; font-size: {text_size}px;" id=main'
        skip_style = f'style="height: {buttons_height}px; width: {skip_width}px; font-size: {text_size}px;" id=main'
        showSkipped_style = f'style="height: {buttons_height}px; width: {showSkipped_width}px; font-size: {text_size}px;" id=main'
        undo_style = f'style="height: {buttons_height}px; width: {undo_width}px; font-size: {text_size}px;" id=main'
        more_style = f'style="height: {buttons_height}px; width: {more_width}px; font-size: {text_size}px;" id=main'
        min_buttonSize = """
        <style>
          button {
            min-width: 5px;
            cursor: %(cursor)s;
            border-radius: %(border_radius)s !important;
            font-weight: %(font_weight)s;
            }
        </style>
        """ %dict(cursor=cursor, border_radius=border_radius, font_weight=buttonFontWeight)
else:
    if bottombarButtons_style == 0:
        edit_style = ""
        info_style = ""
        skip_style = ""
        showSkipped_style = ""
        undo_style = ""
        more_style = ""
        min_buttonSize = """
        <style>
          button {
            cursor: %(cursor)s;
            border-radius: %(border_radius)s !important;
            font-weight: %(font_weight)s;
            }
        </style>
        """ %dict(cursor=cursor, border_radius=border_radius, font_weight=buttonFontWeight)
    else:
        edit_style = "id=main"
        info_style = "id=main"
        skip_style = "id=main"
        showSkipped_style = "id=main"
        undo_style = "id=main"
        more_style = "id=main"
        min_buttonSize = """
        <style>
          button {
            cursor: %(cursor)s;
            border-radius: %(border_radius)s !important;
            font-weight: %(font_weight)s;
            }
        </style>
        """ %dict(cursor=cursor, border_radius=border_radius, font_weight=buttonFontWeight)
######//////__END__ GENERAL BUTTON DESIGNS __END__//////######

######//////__BEGIN__ ACtIVE BUTTON INDICATORS __BEGIN__//////######
#// active button indicator
if activeIndicator_color == "default":
    activeIndicator_color = "#21BFFF"
if active_indicator == 2:
    active_extra = "border: solid 1px; border-color: {0}; box-shadow: 0 0 5px {0}, 0 0 20px {0}, 0 0 40px {0}".format(activeIndicator_color)
else:
    active_extra = f"border: solid 1px; border-color: {activeIndicator_color}"
if active_indicator == 0 or button_style in [4, 5, 6, 7]:
    active_extra = ""
######//////__END__ ACtIVE BUTTON INDICATORS __END__//////######


######//////__BEGIN__ HOVER EFFECTS __BEGIN__//////######
if not custom_colors:
    again_shadow = "box-shadow: 0 0 5px #BA0C0C, 0 0 20px #BA0C0C, 0 0 40px #BA0C0C;"
    hard_shadow = "box-shadow: 0 0 5px #BF720F, 0 0 20px #BF720F, 0 0 40px #BF720F;"
    good_shadow = "box-shadow: 0 0 5px #20A11C, 0 0 20px #20A11C, 0 0 40px #20A11C;"
    easy_shadow = "box-shadow: 0 0 5px #188AB8, 0 0 20px #188AB8, 0 0 40px #188AB8;"
else:
    again_shadow = "box-shadow: 0 0 5px {0}, 0 0 20px {0}, 0 0 40px {0};".format(again_hover_color)
    hard_shadow = "box-shadow: 0 0 5px {0}, 0 0 20px {0}, 0 0 40px {0};".format(hard_hover_color)
    good_shadow = "box-shadow: 0 0 5px {0}, 0 0 20px {0}, 0 0 40px {0};".format(good_hover_color)
    easy_shadow = "box-shadow: 0 0 5px {0}, 0 0 20px {0}, 0 0 40px {0};".format(easy_hover_color)
again_hover = ""
hard_hover = ""
good_hover = ""
easy_hover = ""
if not custom_colors:
    if button_style == 0 or button_style == 2:
        if hover_effect == 1:
            again_hover = "color: #FF1111;"
            hard_hover = "color: #FF9814;"
            good_hover = "color: #33FF2D;"
            easy_hover = "color: #21C0FF;"
        elif hover_effect == 2:
            again_hover = again_shadow
            hard_hover = hard_shadow
            good_hover = good_shadow
            easy_hover = easy_shadow
        elif hover_effect == 3:
            again_hover = f"color: #FF1111; {again_shadow}"
            hard_hover = f"color: #FF9814; {hard_shadow}"
            good_hover = f"color: #33FF2D; {good_shadow}"
            easy_hover = f"color: #21C0FF; {easy_shadow}"
    elif button_style == 1 or button_style == 3:
        if hover_effect == 1:
            if is_nightMode:
                again_hover = "background: #FF1111;"
                hard_hover = "background: #FF9814;"
                good_hover = "background: #33FF2D;"
                easy_hover = "background: #21C0FF;"
            else:
                again_hover = "background: linear-gradient(0deg, #E02A1C, #FF3020);"
                hard_hover = "background: linear-gradient(0deg, #E08C08, #FF9F09);"
                good_hover = "background: linear-gradient(0deg, #22D414, #27F217);"
                easy_hover = "background: linear-gradient(0deg, #11A7D1, #13C0F0);"
        elif hover_effect == 2:
            again_hover = again_shadow
            hard_hover = hard_shadow
            good_hover = good_shadow
            easy_hover = easy_shadow
        elif hover_effect == 3:
            if is_nightMode:
                again_hover = f"background: #FF1111; {again_shadow}"
                hard_hover = f"background: #FF9814; {hard_shadow}"
                good_hover = f"background: #2CDB27; {good_shadow}"
                easy_hover = f"background: #21C0FF; {easy_shadow}"
            else:
                again_hover = f"background: linear-gradient(0deg, #E02A1C, #FF3020); {again_shadow}"
                hard_hover = f"background: linear-gradient(0deg, #E08C08, #FF9F09); {hard_shadow}"
                good_hover = f"background: linear-gradient(0deg, #22D414, #27F217); {good_shadow}"
                easy_hover = f"background: linear-gradient(0deg, #11A7D1, #13C0F0); {easy_shadow}"
else:
    if button_style == 0 or button_style == 2:
        if hover_effect == 1:
            again_hover = f"color: {again_hover_color};"
            hard_hover = f"color: {hard_hover_color};"
            good_hover = f"color: {good_hover_color};"
            easy_hover = f"color: {easy_hover_color};"
        elif hover_effect == 2:
            again_hover = again_shadow
            hard_hover = hard_shadow
            good_hover = good_shadow
            easy_hover = easy_shadow
        elif hover_effect == 3:
            again_hover = f"color: {again_hover_color}; {again_shadow}"
            hard_hover = f"color: {hard_hover_color}; {hard_shadow}"
            good_hover = f"color: {good_hover_color}; {good_shadow}"
            easy_hover = f"color: {easy_hover_color}; {easy_shadow}"
    elif button_style == 1 or button_style == 3:
        if hover_effect == 1:
            again_hover = f"background: {again_hover_color};"
            hard_hover = f"background: {hard_hover_color};"
            good_hover = f"background: {good_hover_color};"
            easy_hover = f"background: {easy_hover_color};"
        elif hover_effect == 2:
            again_hover = again_shadow
            hard_hover = hard_shadow
            good_hover = good_shadow
            easy_hover = easy_shadow
        elif hover_effect == 3:
            again_hover = f"background: {again_hover_color}; {again_shadow}"
            hard_hover = f"background: {hard_hover_color}; {hard_shadow}"
            good_hover = f"background: {good_hover_color}; {good_shadow}"
            easy_hover = f"background: {easy_hover_color}; {easy_shadow}"
######//////__END__ HOVER EFFECTS __END__//////######

######//////__BEGIN__ REVIEW BUTTON DESIGNS __BEGIN__//////######
fill2 = """<style>
    #again {
      padding: 5px 20px;
      border: 1px solid %(again_color)s;
      background: none;
      cursor: %(cursor)s;
      transition: %(transition)s;
      position: relative;
      overflow: hidden;
      border-radius: %(border_radius)s !important;
      color: %(text)s;
    }
    #again:hover {
      color: %(again_color)s;
    }
    #again::before {
      content: "";
      position: absolute;
      left: 0;
      width: 100%%;
      height:180%%;
      background: %(again_color)s;
      z-index: -1;
      transition: %(transition)s;
      bottom: 0;
      border-radius: 50%% 50%% 0 0;
    }
    #again:hover::before {
      height: 0%%;
    }
    #hard {
      padding: 5px 20px;
      border: 1px solid %(hard_color)s;
      background: none;
      cursor: %(cursor)s;
      transition: %(transition)s;
      position: relative;
      overflow: hidden;
      border-radius: %(border_radius)s !important;
      color: %(text)s;
    }
    #hard:hover {
      color: %(hard_color)s;
    }
    #hard::before {
      content: "";
      position: absolute;
      left: 0;
      width: 100%%;
      height:180%%;
      background: %(hard_color)s;
      z-index: -1;
      transition: %(transition)s;
      bottom: 0;
      border-radius: 50%% 50%% 0 0;
    }
    #hard:hover::before {
      height: 0%%;
    }
    #good {
      padding: 5px 20px;
      border: 1px solid %(good_color)s;
      background: none;
      cursor: %(cursor)s;
      transition: %(transition)s;
      position: relative;
      overflow: hidden;
      border-radius: %(border_radius)s !important;
      color: %(text)s;
    }
    #good:hover {
      color: %(good_color)s;
    }
    #good::before {
      content: "";
      position: absolute;
      left: 0;
      width: 100%%;
      height:180%%;
      background: %(good_color)s;
      z-index: -1;
      transition: %(transition)s;
      bottom: 0;
      border-radius: 50%% 50%% 0 0;
    }
    #good:hover::before {
      height: 0%%;
    }
    #easy {
      padding: 5px 20px;
      border: 1px solid %(easy_color)s;
      background: none;
      cursor: %(cursor)s;
      transition: %(transition)s;
      position: relative;
      overflow: hidden;
      border-radius: %(border_radius)s !important;
      color: %(text)s;
    }
    #easy:hover {
      color: %(easy_color)s;
    }
    #easy::before {
      content: "";
      position: absolute;
      left: 0;
      width: 100%%;
      height:180%%;
      background: %(easy_color)s;
      z-index: -1;
      transition: %(transition)s;
      bottom: 0;
      border-radius: 50%% 50%% 0 0;
    }
    #easy:hover::before {
      height: 0%%;
    }
    </style>""" % dict(text=textColor, again_color=again_color,hard_color=hard_color, good_color=good_color,
    easy_color=easy_color,cursor=cursor, transition=transition, border_radius=border_radius)

fill1 = """<style>
    #again {
      padding: 5px 20px;
      border: 1px solid %(again_color)s;
      background: none;
      cursor: %(cursor)s;
      transition: %(transition)s;
      position: relative;
      overflow: hidden;
      border-radius: %(border_radius)s !important;
      color: %(again_color)s;
    }
    #again:hover {
      color: %(text)s;
    }
    #again::before {
      content: "";
      position: absolute;
      left: 0;
      width: 100%%;
      height: 0%%;
      background: %(again_color)s;
      z-index: -1;
      transition: %(transition)s;
      bottom: 0;
      border-radius: 50%% 50%% 0 0;
    }
    #again:hover::before {
      height: 180%%;
    }
    #hard {
      padding: 5px 20px;
      border: 1px solid %(hard_color)s;
      background: none;
      cursor: %(cursor)s;
      transition: %(transition)s;
      position: relative;
      overflow: hidden;
      border-radius: %(border_radius)s !important;
      color: %(hard_color)s;
    }
    #hard:hover {
      color: %(text)s;
    }
    #hard::before {
      content: "";
      position: absolute;
      left: 0;
      width: 100%%;
      height: 0%%;
      background: %(hard_color)s;
      z-index: -1;
      transition: %(transition)s;
      bottom: 0;
      border-radius: 50%% 50%% 0 0;
    }
    #hard:hover::before {
      height: 180%%;
    }
    #good {
      padding: 5px 20px;
      border: 1px solid %(good_color)s;
      background: none;
      cursor: %(cursor)s;
      transition: %(transition)s;
      position: relative;
      overflow: hidden;
      border-radius: %(border_radius)s !important;
      color: %(good_color)s;
    }
    #good:hover {
      color: %(text)s;
    }
    #good::before {
      content: "";
      position: absolute;
      left: 0;
      width: 100%%;
      height: 0%%;
      background: %(good_color)s;
      z-index: -1;
      transition: %(transition)s;
      bottom: 0;
      border-radius: 50%% 50%% 0 0;
    }
    #good:hover::before {
      height: 180%%;
    }
    #easy {
      padding: 5px 20px;
      border: 1px solid %(easy_color)s;
      background: none;
      cursor: %(cursor)s;
      transition: %(transition)s;
      position: relative;
      overflow: hidden;
      border-radius: %(border_radius)s !important;
      color: %(easy_color)s;
    }
    #easy:hover {
      color: %(text)s;
    }
    #easy::before {
      content: "";
      position: absolute;
      left: 0;
      width: 100%%;
      height: 0%%;
      background: %(easy_color)s;
      z-index: -1;
      transition: %(transition)s;
      bottom: 0;
      border-radius: 50%% 50%% 0 0;
    }
    #easy:hover::before {
      height: 180%%;
    }
    </style>""" % dict(text=textColor, again_color=again_color, hard_color=hard_color, good_color=good_color,
    easy_color=easy_color, cursor=cursor, transition=transition, border_radius=border_radius)
neon2 = """<style>
    #again {
      color: %(text)s;
      border: 1px solid %(again_color)s;
      padding: 5px 20px;
      border-radius: %(border_radius)s !important;
      background: %(again_color)s;
      cursor: %(cursor)s;
      transition: %(transition)s;
      box-shadow: 0 2px 20px 0 %(again_color)s inset, 0 2px 20px 0 %(again_color)s;
    }
    #again:hover {
      background: none;
      border-radius: %(border_radius)s !important;
      color: %(again_color)s;
      box-shadow: none;
    }
    #hard {
      color: %(text)s;
      border: 1px solid %(hard_color)s;
      padding: 5px 20px;
      border-radius: %(border_radius)s !important;
      background: %(hard_color)s;
      cursor: %(cursor)s;
      transition: %(transition)s;
      box-shadow: 0 2px 20px 0 %(hard_color)s inset, 0 2px 20px 0 %(hard_color)s;
    }
    #hard:hover {
      background: none;
      border-radius: %(border_radius)s !important;
      color: %(hard_color)s;
      box-shadow: none;
    }
    #good {
      color: %(text)s;
      border: 1px solid %(good_color)s;
      padding: 5px 20px;
      border-radius: %(border_radius)s !important;
      background: %(good_color)s;
      cursor: %(cursor)s;
      transition: %(transition)s;
      box-shadow: 0 2px 20px 0 %(good_color)s inset, 0 2px 20px 0 %(good_color)s;
    }
    #good:hover {
      background: none;
      border-radius: %(border_radius)s !important;
      color: %(good_color)s;
      box-shadow: none;
    }
    #easy {
      color: %(text)s;
      border: 1px solid %(easy_color)s;
      padding: 5px 20px;
      border-radius: %(border_radius)s !important;
      background: %(easy_color)s;
      cursor: %(cursor)s;
      transition: %(transition)s;
      box-shadow: 0 2px 20px 0 %(easy_color)s inset, 0 2px 20px 0 %(easy_color)s;
    }
    #easy:hover {
      background: none;
      border-radius: %(border_radius)s !important;
      color: %(easy_color)s;
      box-shadow: none;
    }
    </style>""" % dict(text=textColor, again_color=again_color,hard_color=hard_color,
    good_color=good_color, easy_color=easy_color, cursor=cursor, transition=transition, border_radius=border_radius)
neon1 = """<style>
    #again {
    background: none;
    color: %(again_color)s;
    border: 1px solid %(again_color)s;
    padding: 5px 20px;
    border-radius: %(border_radius)s !important;
    cursor: %(cursor)s;
    transition: %(transition)s;
    box-shadow: none;
    }
    #again:hover {
    background: %(again_color)s;
    color: %(text)s;
    border-radius: %(border_radius)s !important;
    box-shadow: 0 2px 20px 0 %(again_color)s inset, 0 2px 20px 0 %(again_color)s;
    }
    #hard {
    background: none;
    color: %(hard_color)s;
    border: 1px solid %(hard_color)s;
    padding: 5px 20px;
    border-radius: %(border_radius)s !important;
    cursor: %(cursor)s;
    transition: %(transition)s;
    box-shadow: none;
    }
    #hard:hover {
    background: %(hard_color)s;
    color: %(text)s;
    border-radius: %(border_radius)s !important;
    box-shadow: 0 2px 20px 0 %(hard_color)s inset, 0 2px 20px 0 %(hard_color)s;
    }
    #good {
    background: none;
    color: %(good_color)s;
    border: 1px solid %(good_color)s;
    padding: 5px 20px;
    border-radius: %(border_radius)s !important;
    cursor: %(cursor)s;
    transition: %(transition)s;
    box-shadow: none;
    }
    #good:hover {
    background: %(good_color)s;
    color: %(text)s;
    border-radius: %(border_radius)s !important;
    box-shadow: 0 2px 20px 0 %(good_color)s inset, 0 2px 20px 0 %(good_color)s;
    }
    #easy {
    background: none;
    color: %(easy_color)s;
    border: 1px solid %(easy_color)s;
    padding: 5px 20px;
    border-radius: %(border_radius)s !important;
    cursor: %(cursor)s;
    transition: %(transition)s;
    box-shadow: none;
    }
    #easy:hover {
    background: %(easy_color)s;
    color: %(text)s;
    border-radius: %(border_radius)s !important;
    box-shadow: 0 2px 20px 0 %(easy_color)s inset, 0 2px 20px 0 %(easy_color)s;
    }
    </style>""" % dict(text=textColor, again_color=again_color, hard_color=hard_color,
    good_color=good_color, easy_color=easy_color, cursor=cursor, transition=transition, border_radius=border_radius)
#// styling for text color change method
text_color = """<style>
    #again {
      color: #BA0C0C;
      cursor: %(cursor)s;
      }
    #again:hover{
      %(again_hover)s
    }
    #hard {
      color: #BF720F;
      cursor: %(cursor)s;
    }
    #hard:hover{
      %(hard_hover)s
    }
    #good {
      color: #20A11C;
      cursor: %(cursor)s;
    }
    #good:hover{
      %(good_hover)s
    }
    #easy {
      color: #188AB8;
      cursor: %(cursor)s;
    }
    #easy:hover{
      %(easy_hover)s
    }
    </style>""" % dict(cursor=cursor, again_hover=again_hover, hard_hover=hard_hover, good_hover=good_hover, easy_hover=easy_hover)

#// styling for background color change method
if is_nightMode:  #// style if anki version is 2.1.20 and night mode is enabled
    background_color = """<style>
        #again, #hard, #good, #easy {
          border: hidden;
          color: %(text)s;
          cursor: %(cursor)s;
          text-shadow: none;
        }
        #again {
          background: #BA0C0C;
        }
        #again:hover{
          color: %(text)s;
          %(again_hover)s
        }
        #hard {
          background: #BF720F;
        }
        #hard:hover{
          color: %(text)s;
          %(hard_hover)s
        }
        #good {
          background: #20A11C;
        }
        #good:hover{
          color: %(text)s;
          %(good_hover)s
        }
        #easy {
          background: #188AB8;
        }
        #easy:hover{
          color: %(text)s;
          %(easy_hover)s
        }
        </style>""" % dict (text=textColor, cursor=cursor, again_hover=again_hover, hard_hover=hard_hover, good_hover=good_hover, easy_hover=easy_hover)
else:  #// style if anki version is older than 2.1.20 or night mode is disabled
    background_color = """<style>
        #again, #hard, #good, #easy {
          border: hidden;
          color: %(text)s;
          cursor: %(cursor)s;
          text-shadow: none;
          border-radius: 3px;
        }
        #again {
          background: linear-gradient(0deg, #B52217, #CF271A);
        }
        #again:hover{
          color: %(text)s;
          %(again_hover)s
        }
        #hard {
          background: linear-gradient(0deg, #BF7707, #D98708);
        }
        #hard:hover{
          color: %(text)s;
          %(hard_hover)s
        }
        #good {
          background: linear-gradient(0deg, #1CA810, #20C212);
        }
        #good:hover{
          color: %(text)s;
          %(good_hover)s
        }
        #easy {
          background: linear-gradient(0deg, #0F95BA, #11AAD4);
        }
        #easy:hover{
          color: %(text)s;
          %(easy_hover)s
        }
        </style>""" % dict (text=textColor, cursor=cursor, again_hover=again_hover, hard_hover=hard_hover, good_hover=good_hover, easy_hover=easy_hover)

#// styling for custom text color change method
custom_text = """<style>
    #again {
      color: %(again_color)s;
      cursor: %(cursor)s;
    }
    #again:hover{
      %(again_hover)s
    }
    #hard {
      color: %(hard_color)s;
      cursor: %(cursor)s;
    }
    #hard:hover{
      %(hard_hover)s
    }
    #good {
      color: %(good_color)s;
      cursor: %(cursor)s;
    }
    #good:hover{
      %(good_hover)s
    }
    #easy {
      color: %(easy_color)s;
      cursor: %(cursor)s;
    }
    #easy:hover{
      %(easy_hover)s
    }
    </style>""" % dict(again_color=again_color, hard_color=hard_color, good_color=good_color, easy_color=easy_color, easy_hover_color=easy_hover_color,
    again_hover=again_hover, hard_hover=hard_hover, good_hover=good_hover, easy_hover=easy_hover, cursor=cursor)

#// styling for custom background color change method
if is_nightMode:  #// style if anki version is 2.1.20 and above and night mode is enabled
    custom_background = """<style>
    #again, #hard, #good, #easy {
      border: hidden;
      color: %(text)s;
      cursor: %(cursor)s;
      text-shadow: none;
    }
    #again {
      background: %(again_color)s;
      }
    #again:hover{
      color: %(text)s;
      %(again_hover)s
    }
    #hard {
      background: %(hard_color)s;
    }
    #hard:hover{
      color: %(text)s;
      %(hard_hover)s
    }
    #good {
      background: %(good_color)s;
    }
    #good:hover{
      color: %(text)s;
      %(good_hover)s
    }
    #easy {
      background: %(easy_color)s;
    }
    #easy:hover{
      color: %(text)s;
      %(easy_hover)s
    }
    </style>""" % dict (text=textColor, cursor=cursor, again_color=again_color, hard_color=hard_color, good_color=good_color, easy_color=easy_color,
    again_hover=again_hover, hard_hover=hard_hover, good_hover=good_hover, easy_hover=easy_hover)
else:  #// style if anki is in day/light mode or anki version is older than 2.1.20
    custom_background = """<style>
    #again, #hard, #good, #easy {
      border: hidden;
      color: %(text)s;
      cursor: %(cursor)s;
      text-shadow: none;
      border-radius: 3px
    }
    #again {
      background: %(again_color)s;
    }
    #again:hover{
      color: %(text)s;
      background: %(again_hover_color)s;
      %(again_hover)s
    }
    #hard {
      background: %(hard_color)s;
    }
    #hard:hover{
      color: %(text)s;
      background: %(hard_hover_color)s;
      %(hard_hover)s
    }
    #good {
      background: %(good_color)s;
    }
    #good:hover{
      color: %(text)s;
      background: %(good_hover_color)s;
      %(good_hover)s
    }
    #easy {
      background: %(easy_color)s;
    }
    #easy:hover{
      color: %(text)s;
      background: %(easy_hover_color)s;
      %(easy_hover)s
    }
    </style>""" % dict (text=textColor, cursor=cursor, again_color=again_color, again_hover_color=again_hover_color, hard_color=hard_color, hard_hover_color=hard_hover_color, good_color=good_color, good_hover_color=good_hover_color, easy_color=easy_color, easy_hover_color=easy_hover_color,
    again_hover=again_hover, hard_hover=hard_hover, good_hover=good_hover, easy_hover=easy_hover)

button_styles = """<style>
    .wide {
      min-width: 70px;
      width: 98%;
      margin: 6px 0px;
      padding: 3px 0px;
      font-size: 12px
    }
    .mybuttons {
      padding: 3px;
      font-size: 12px;
    }
    </style>"""
######//////__END__ REVIEW BUTTONS DESIGNS __END__//////######

######//////__BEGIN__ CARD INFO STYLING __BEGIN//////######
light = """
body {
    margin: 8px;
    background-color: #dedede;
}
p {
    margin-top: 1em;
    margin-bottom: 1em;
}
h1,h2,h3,h4{
    display: block;
    font-size: 1.17em;
    margin-top: 1em;
    margin-bottom: 1em;
    margin-left: 0;
    margin-right: 0;
    font-weight: bold;
}
a:link {
    text-decoration: none;
    color:black;
}

/* anki.stats

colYoung = "#7c7"
colMature = "#070"
colCum = "rgba(0,0,0,0.9)"
colLearn = "#00F"
colRelearn = "#c00"
colCram = "#ff0"
colIvl = "#077"
colHour = "#ccc"
colTime = "#770"
colUnseen = "#000"
colSusp = "#ff0"
*/

.color_learn {color: #00F;}
.color_mature {color: #070;}
.color_relearn {color: #c00;}
.color_type3 {color: #3c9690;}
.color_rest {color: #000;}
.color_ease3 {color: navy;}
.color_ease4 {color:  darkgreen;}

.critical_color_lower {color:  red;}
.critical_color_upper {color:  blue;}
"""
dark = """
body {
    background-color: #272828;
    color: #d7d7d7;
    margin: 8px;
}
p {
    background-color: #272828;
    color: #d7d7d7;
    margin-top: 1em;
    margin-bottom: 1em;
}
h1,h2,h3,h4{
    background-color: #272828;
    color: #d7d7d7;
    display: block;
    font-size: 1.17em;
    margin-top: 1em;
    margin-bottom: 1em;
    margin-left: 0;
    margin-right: 0;
    font-weight: bold;
}
a:link {
    text-decoration: none;
    color:#d7d7d7;
}

.color_learn {color: #01b3f5;}
.color_mature {color: #070;}
.color_relearn {color: #ff0000;}
.color_type3 {color: #57d9d1;}
.color_rest {color: #dedede;}
.color_ease3 {color: #00aaff;}
.color_ease4 {color:  #55ff00;}

.critical_color_lower {color:  #ff0000;}
.critical_color_upper {color:  #00aaff;}
"""
######//////__END__ CARD INFO __END__//////######
