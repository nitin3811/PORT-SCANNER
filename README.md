# PORT-SCANNER
# 🔥 Nitin Maurya Cyber Scanner

A high-performance, multi-threaded port scanner built with Python and Tkinter.
Designed for speed, usability, and real-world cybersecurity learning.

---

## ⚡ Features

* 🚀 Ultra-fast multi-threaded scanning
* 🌐 Multi-target support (scan multiple hosts)
* 📊 Live progress bar with percentage
* ⚡ Speed meter (ports per second)
* 🎯 Service detection (common ports)
* 🎛️ Adjustable scan speed (thread control)
* 💾 Export scan results to JSON
* 🖥️ Clean dark hacker-style GUI

---

## 🧠 How It Works

* Uses Python sockets for TCP connection scanning
* Multi-threading via `ThreadPoolExecutor` for high performance
* Real-time UI updates using Tkinter
* Lightweight service detection based on common ports

---

## 📦 Installation

### 1. Clone Repository

```bash
git clone https://github.com/nitin3811/cyber-scanner.git
cd cyber-scanner
```

---

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

*(If no requirements file, install manually)*

```bash
pip install tkinter
```

---

## ▶️ Usage

```bash
python main.py
```

---

## 🧪 Example Input

```
Target: scanme.nmap.org
Start Port: 1
End Port: 1024
```

You can also scan multiple targets:

```
scanme.nmap.org, google.com, 192.168.1.1
```

---

## 📊 Output Example

```
scanme.nmap.org:22 → SSH
scanme.nmap.org:80 → HTTP
scanme.nmap.org:443 → HTTPS
```

---

## ⚙️ Configuration

### Thread Speed

* 100 → Stable
* 200 → Fast (recommended)
* 300+ → Very fast (high CPU usage)

---

## 💾 Export Results

Click **"Save Results"** to export scan results:

```
results.json
```

---

## ⚠️ Disclaimer

This tool is built for:

* Educational purposes
* Ethical hacking labs
* Personal network testing

Do NOT use it on networks without permission.

---

## 🛠️ Built With

* Python
* Tkinter
* Socket Programming
* Threading / Concurrency

---

## 🚀 Future Improvements

* 🔍 Service version detection (-sV)
* 🧠 CVE vulnerability scanner
* 📊 SOC dashboard with graphs
* 📄 HTML/PDF reporting
* 🌐 Web-based dashboard

---

## 👨‍💻 Author

**Nitin Maurya**
Cybersecurity Enthusiast 🚀

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🧠 Contribute improvements

---
