import socket, threading, time, json, tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import concurrent.futures

# ================= GLOBAL =================
scan_results = {}
scan_start_time = 0
total_ports = 1
scanned_ports = 0

# ================= SERVICE DETECTION =================
def detect_service(port):
    common = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
        53: "DNS", 80: "HTTP", 443: "HTTPS",
        3306: "MySQL", 8080: "HTTP-Alt"
    }
    return common.get(port, "Unknown")

# ================= FAST SCAN =================
def fast_scan(targets, start, end):
    global scan_start_time, scanned_ports, total_ports

    scan_output.delete(1.0, tk.END)
    scan_results.clear()

    scan_start_time = time.time()
    scanned_ports = 0
    total_ports = len(targets) * (end - start)

    def scan(ip, port):
        global scanned_ports

        s = socket.socket()
        s.settimeout(0.3)

        try:
            if s.connect_ex((ip, port)) == 0:
                service = detect_service(port)

                if ip not in scan_results:
                    scan_results[ip] = []

                scan_results[ip].append((port, service))

                root.after(0, lambda:
                    scan_output.insert(tk.END, f"{ip}:{port} → {service}\n"))
        except:
            pass
        finally:
            s.close()

        scanned_ports += 1

    with concurrent.futures.ThreadPoolExecutor(max_workers=speed_scale.get()) as executor:
        for ip in targets:
            for port in range(start, end):
                executor.submit(scan, ip, port)

    root.after(0, finish_scan)

# ================= FINISH =================
def finish_scan():
    duration = time.time() - scan_start_time
    speed = int(scanned_ports / duration) if duration > 0 else 0
    status_var.set(f"✅ Done | {scanned_ports} ports | {speed} ports/sec")

# ================= START =================
def start_scan():
    targets_input = entry_target.get()

    if not targets_input:
        messagebox.showerror("Error", "Enter target")
        return

    try:
        targets = [socket.gethostbyname(t.strip()) for t in targets_input.split(",")]
    except:
        messagebox.showerror("Error", "Invalid target")
        return

    try:
        start = int(entry_start.get() or 1)
        end = int(entry_end.get() or 1024)
    except:
        messagebox.showerror("Error", "Invalid ports")
        return

    threading.Thread(target=fast_scan, args=(targets, start, end), daemon=True).start()

# ================= PROGRESS =================
def update_progress():
    if total_ports > 0:
        percent = int((scanned_ports / total_ports) * 100)
        progress_var.set(percent)
        progress_label.config(text=f"{percent}%")

    root.after(200, update_progress)

# ================= SAVE =================
def save_results():
    with open("results.json", "w") as f:
        json.dump(scan_results, f, indent=4)

    status_var.set("💾 Results saved")

# ================= GUI =================
root = tk.Tk()
root.title("🔥 Nitin Maurya Cyber Scanner 🔥")
root.geometry("1000x650")
root.configure(bg="#1e1e1e")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# ---- SCANNER TAB ----
scan_tab = tk.Frame(notebook, bg="#1e1e1e")
notebook.add(scan_tab, text="Scanner")

entry_target = tk.Entry(scan_tab, bg="#2b2b2b", fg="white")
entry_target.pack(pady=5)
entry_target.insert(0, "scanme.nmap.org")

entry_start = tk.Entry(scan_tab, bg="#2b2b2b", fg="white")
entry_start.pack()
entry_start.insert(0, "1")

entry_end = tk.Entry(scan_tab, bg="#2b2b2b", fg="white")
entry_end.pack()
entry_end.insert(0, "1024")

tk.Button(scan_tab, text="Start Scan", command=start_scan).pack(pady=5)

# ---- SPEED CONTROL ----
speed_scale = tk.Scale(scan_tab, from_=50, to=500,
                       orient="horizontal",
                       label="Speed (Threads)",
                       bg="#1e1e1e", fg="white")
speed_scale.set(200)
speed_scale.pack()

# ---- PROGRESS ----
progress_var = tk.DoubleVar()
ttk.Progressbar(scan_tab, variable=progress_var, maximum=100).pack(fill="x")

progress_label = tk.Label(scan_tab, text="0%", bg="#1e1e1e", fg="white")
progress_label.pack()

# ---- OUTPUT ----
scan_output = scrolledtext.ScrolledText(scan_tab,
                                        bg="#121212",
                                        fg="#00ffcc")
scan_output.pack(fill="both", expand=True)

# ---- STATUS ----
status_var = tk.StringVar()
status_var.set("Ready")

status_bar = tk.Label(root, textvariable=status_var,
                      bg="#1e1e1e", fg="#00ffcc")
status_bar.pack(fill="x")

# ---- SAVE BUTTON ----
tk.Button(root, text="Save Results", command=save_results).pack()

# START PROGRESS LOOP
update_progress()

root.mainloop()