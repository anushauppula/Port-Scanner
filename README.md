# Fast Multi-Threaded Port Scanner 🚀

## 📌 About
A high-speed TCP port scanner built in Python using socket programming and multi-threading. Scans 1000 ports in ~2 seconds vs 500+ seconds with single-threaded approach.This confirms the scanner correctly identifies open ports at the network packet level.

### How to Reproduce:
1. Start Wireshark: `sudo wireshark`
2. Capture on `Loopback: lo` with filter `tcp.port == 445`
3. Run scanner on `127.0.0.1` port `445`
4. Observe SYN/SYN-ACK handshake in Wireshark

## ⚡ Features
- **300 Threads**: High speed scanning using `threading` module
- **Custom Port Range**: Scan specific ranges like 1-1000, 80-443
- **Queue Management**: Prevents race conditions with `queue.Queue`
- **Execution Timer**: Shows exact scan duration using `time` module
- **Error Handling**: Handles invalid IPs and port inputs gracefully
- **Clean Output**: Displays only open ports with status

## 🔧 Tech Stack
Python 3, `socket`, `threading`, `queue`, `time`
## ⚠️ Legal & Safe Testing

**IMPORTANT:** Only scan IPs you own or have explicit permission to test.

### How to Test Safely:

**Option 1: Scan Your Own Machine**
```bash
python port_scanner.py 127.0.0.1

## 📸 Sample Output
Scanning 127.0.0.1 ports 1-100...
Port 22: OPEN | SSH-2.0-OpenSSH_8.2
Port 80: OPEN | HTTP
Scan completed in 0.34 seconds
