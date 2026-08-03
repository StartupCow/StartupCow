#!/bin/bash

if [ -n "$WAYLAND_DISPLAY" ]; then
    export QT_QPA_PLATFORM=xcb
fi

exec python3 "$HOME/cow.py" "$@"
