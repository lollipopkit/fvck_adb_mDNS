简体中文 | [English](README.md)

## 介绍
如果你的设备支持 mDNS 且能够正常发现服务，但是你的开发设备却无法在你的 Android 设备开启 wifi adb 后自动连接你的Android 设备，那么你可能需要该工具。

常见的表现为：执行 `adb mdns check`，输出 `ERROR: mdns daemon unavailable`，但是 `avahi-browse -a` 可以看到你的 Android 设备。

## 使用
**[全局激活](#全局激活) 或 [作为服务](#作为服务) 的代码仅支持 Linux，Windows 请自行查找教程。**

#### 一次性
```py
python3 auto_adb.py
```

#### 全局激活
```sh
chmod +x auto_adb.py
# 或者你可以将它放在任何 PATH 目录下
sudo ln -s /path/to/auto_adb.py /usr/bin/auto_adb.py
```

#### 作为服务
打开 crontab
```sh
crontab -e
```
输入以下内容（每分钟运行 auto_adb.py）：
```cron
* * * * * /usr/bin/python3 /path/to/auto_adb.py
```
保存并退出后，服务将会自动启动。它的行为类似于 macOS 的 adb 守护进程，可以自动连接到你的 Android 设备。

## 更多
- 请先检查设备是否支持 mDNS
- 如果你的设备不支持 mDNS，你就可能需要手动去开启
