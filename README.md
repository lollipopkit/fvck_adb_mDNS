[简体中文](README_zh.md) | English

## Intro
If your device supports mDNS and can normally discover services, but your development device fails to automatically connect to your Android device after enabling wifi adb on it, you might need this tool.

Common symptoms include: executing `adb mdns check`, outputting `ERROR: mdns daemon unavailable`, but you can see your Android device with `avahi-browse -a`.

## Usage
```py
python3 auto_adb.py
```

## More
- First, check if your device supports mDNS.
- If your device does not support mDNS, you may need to enable it manually.