"""v35-8: the Interaction states demo's success state. It read "Playing" next to a play icon, so the label named a state while
the icon offered an action. Once playback starts, a play button becomes Pause, so success now shows a pause icon and
"Pause", and the caption says why instead of "return to default", which fits a Save button but not this one.

Run once after v35-7: python3 tools/migrations/v35_8_states_pause.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import Book  # noqa: E402

b = Book()
assert 'id="i-pause"' not in b.s, 'already migrated'

b.after('<symbol id="i-play" viewBox="0 0 24 24"><path d="M7 5l12 7-12 7z"/></symbol>',
        '\n  <symbol id="i-pause" viewBox="0 0 24 24"><path d="M9 5v14"/><path d="M15 5v14"/></symbol>')

b.once("      success: ['Playing', 'Success: confirm briefly, then return to default.']",
       "      success: ['Pause', 'Success: show the result at once. Playback started, so the button now offers Pause.']")
b.once("      label.textContent = info[s][0]; cap.textContent = info[s][1];\n"
       "      $$('[data-state]', st)",
       "      label.textContent = info[s][0]; cap.textContent = info[s][1];\n"
       "      $('use', icon).setAttribute('href', s === 'success' ? '#i-pause' : '#i-play');\n"
       "      $$('[data-state]', st)")

b.save()
print('v35-8 applied')
