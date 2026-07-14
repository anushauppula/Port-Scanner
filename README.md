# Fast Multi-Threaded Port Scanner 🚀

## 📌 About
A high-speed TCP port scanner built in Python using socket programming and multi-threading. Scans 1000 ports in ~2 seconds vs 500+ seconds with single-threaded approach.

## ⚡ Features
- **300 Threads**: High speed scanning using `threading` module
- **Custom Port Range**: Scan specific ranges like 1-1000, 80-443
- **Queue Management**: Prevents race conditions with `queue.Queue`
- **Execution Timer**: Shows exact scan duration using `time` module
- **Error Handling**: Handles invalid IPs and port inputs gracefully
- **Clean Output**: Displays only open ports with status

## 🔧 Tech Stack
Python 3, `socket`, `threading`, `queue`, `time`

## 📸 Sample Output
