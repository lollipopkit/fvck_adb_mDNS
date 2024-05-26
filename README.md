[简体中文](README_zh.md) | English

## Intro
If your device supports mDNS and can normally discover services, but your development device fails to automatically connect to your Android device after enabling wifi adb on it, you might need this tool.

Common symptoms include: executing `adb mdns check`, outputting `ERROR: mdns daemon unavailable`, but you can see your Android device with `avahi-browse -a`.

## Usage
**[Global activation](#global-activation) or [as service](#as-service) is only supported on Linux, please find tutorials for Windows by yourself.**

#### Once
```py
python3 auto_adb.py
```

#### Global activation
```sh
chmod +x auto_adb.py
# Or you can put it in any of your PATH directories
sudo ln -s /path/to/auto_adb.py /usr/bin/auto_adb.py
```
Then you can run `auto_adb` in any directory.

#### As service
Open crontab
```sh
crontab -e
```
Write the following content (run auto_adb.py every minute):
```cron
* * * * * /usr/bin/python3 /path/to/auto_adb.py
```
After saving and exiting, the service will be started automatically. It behaves like macOS's adb daemon which can automatically connect to your Android device.

## More
- First, check if your device supports mDNS.
- If your device does not support mDNS, you may need to enable it manually.