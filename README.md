# ScreenRecorder

Really simple screen recorder for Linux with x11 using ffmpeg.

# Description

ScreenRecorder use ffmpeg to record x11 display. No settings are available (at least for now). 
The record is saved in the default user's videos folder (xdg-user-dir VIDEOS) in a file named with current unix epoch dot mp4 (1640364957.mp4).

# Usage

## Install

```
chmod +x install.sh
sudo ./install.sh
```

## Recording

To start recording exec `screenrecorder` and to stop re-execute it.

## Uninstall

```
sudo ./install.sh remove
```

# Limitation

It's possible only to make a recording at a time.

# LICENSE

[GPLv3](LICENSE)
