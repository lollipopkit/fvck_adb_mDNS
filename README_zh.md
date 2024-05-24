简体中文 | [English](README.md)

## 介绍
如果你的设备支持 mDNS 且能够正常发现服务，但是你的开发设备却无法在你的 Android 设备开启 wifi adb 后自动连接你的Android 设备，那么你可能需要该工具。

常见的表现为：执行 `adb mdns check`，输出 `ERROR: mdns daemon unavailable`，但是 `avahi-browse -a` 可以看到你的 Android 设备。

## 使用
```py
python3 auto_adb.py
```

## 更多
- 请先检查设备是否支持 mDNS
- 如果你的设备不支持 mDNS，你就可能需要手动去开启
