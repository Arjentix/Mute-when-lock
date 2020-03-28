# Mute when lock

**Manjaro Linux** with **Gnome** DE (may be other Linux distributives too) doesn't mute the sound when user session is locked. This program fixes it.

Sound will be unmuted after unlock.

## Installation

You should have `python3` installed.

```bash
chmod +x install.sh
sudo ./install.sh
```

Now program is installed but will not be running at startup.  To do that just add `Mute when lock` application to autostart menu in `Gnome Tweaks`.

## Features

By default this program will mute all possible audio-outputs. In fact, it's pretty slow, because there are much more *virtual* audio-outputs than *physical*. In my case I have laptop integrated audio and HDMI output. But Linux can see 28 audio-outputs (it's different combinations of some preferences with my two physical outputs).

So you can speed up this program by providing your typical audio-outputs:

1. Select audio-output in settings

2. Run the next command:

   ```bash
   pacmd list-cards | sed -n 's/^.*active profile: <\(\S*\)>$/\1/p'
   ```

3. And repeat this for every your output-device.

4. Change the `Exec` line in *mute-when-lock.desktop* file by providing your audio-outputs (from 2'nd step) as the arguments to the program. For example this is my `Exec` line:

   ```
   Exec=/usr/bin/python3 /usr/local/bin/mute.py output:hdmi-stereo output:analog-stereo
   ```

> Also the first audio-output will be selected when session will be unlocked