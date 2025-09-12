#// auth_ Noobj2
#// Copyright (c) 2019-2025 Noobj2

from aqt import mw
from aqt import gui_hooks
from aqt.utils import showInfo
from aqt.reviewer import Reviewer

# Bury and mark for unburying
def burySkipped():
    if hasattr(mw.reviewer, "skipped_cards"):
        mw.reviewer.skipped_cards.append(mw.reviewer.card.id)
    else:
        mw.reviewer.skipped_cards = [mw.reviewer.card.id,]
    mw.checkpoint(_("Bury"))
    mw.col.sched.buryCards([mw.reviewer.card.id])
    mw.reset()
    
# Suspend and mark for unsuspending
def suspendSkipped():
    if hasattr(mw.reviewer, "skipped_cards"):
        mw.reviewer.skipped_cards.append(mw.reviewer.card.id)
    else:
        mw.reviewer.skipped_cards = [mw.reviewer.card.id,]
    mw.checkpoint(_("Suspend"))
    mw.col.sched.suspendCards([mw.reviewer.card.id])
    mw.reset()

# Unbury skipped cards
def unburySkipped():
    allburied = [int(x) for x in mw.col.findCards("is:buried")]
    to_rebury = []
    if allburied:
        for card in allburied:
            if not card in mw.reviewer.skipped_cards:
                to_rebury.append(card)
        del mw.reviewer.skipped_cards
        mw.col.sched.unburyCards()
        if to_rebury:
            mw.col.sched.buryCards(to_rebury)
        mw.reset()

# Unsuspend skipped cards
def unsuspendSkipped():
    allSuspended = [int(x) for x in mw.col.findCards("is:suspended")]
    to_unsuspend = []
    if allSuspended:
        for card in allSuspended:
            if card in mw.reviewer.skipped_cards:
                to_unsuspend.append(card)
        del mw.reviewer.skipped_cards
        mw.col.sched.unsuspendCards(to_unsuspend)
        mw.reset()

def try_unburySkipped():
    if hasattr(mw.reviewer, "skipped_cards"):
        unburySkipped()

def try_unsuspendSkipped():
    if hasattr(mw.reviewer, "skipped_cards"):
        unsuspendSkipped()

# Unbury skipped cards upon exiting review screen
gui_hooks.reviewer_will_end.append(try_unburySkipped)

# Unbury skipped cards upon exiting profile
gui_hooks.profile_will_close.append(try_unburySkipped)

def test():
    showInfo("{}".format(mw.col.sched.version))
