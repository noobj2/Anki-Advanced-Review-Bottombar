#// auth_ Mohamad Janati
#// Copyright (c) 2019-2021 Mohamad Janati (freaking stupid, right? :|)

from aqt import mw
from anki import version
from anki.collection import _Collection
config = mw.addonManager.getConfig(__name__)
button_colors = config['  Button Colors']
reviewTooltip = config['Tooltip']

anki_version = int(version.replace('.', ''))
from . import Bottom_Bar
from . import Settings
if reviewTooltip:
    from . import Tooltip

if button_colors:
    from . import Button_Colors
if anki_version > 2119:
    from . import Graph_Fix
