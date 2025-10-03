#// auth_ Mohamad Janati
#// Copyright (c) 2019-2023 Mohamad Janati

from aqt import mw
from anki import version
from anki.collection import _Collection
import re
config = mw.addonManager.getConfig(__name__)
button_colors = config['  Button Colors']
reviewTooltip = config['Tooltip']

try:
    # Normalize version by removing any non-digit/non-dot characters (e.g. '25.06b4' -> '25.064')
    cleaned = re.sub(r'[^0-9.]', '', version)
    anki_version = int(cleaned.replace('.', ''))
except Exception:
    # Fallback: keep only digits; if none, set to 0
    digits = ''.join(ch for ch in version if ch.isdigit())
    anki_version = int(digits) if digits else 0

from . import Bottom_Bar
from . import Settings
from . import Deck_Overview
if reviewTooltip:
    from . import Tooltip

if button_colors:
    from . import Button_Colors
