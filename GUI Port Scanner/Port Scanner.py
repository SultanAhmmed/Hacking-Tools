#!/bin/python3

########################################################
# All praise is due to Allah, who created the universe.
# Script Author : Sultan Ahmmed
# Written Date : May 3, 2025
########################################################



import socket
import threading
from concurrent.futures import ThreadPoolExecutor
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk

# Set default socket timeout
socket.setdefaulttimeout(3)

def scan_port(target, port, output_box):
    try:
        s = socket.socket()
        s.connect((target, port))
        s.close()
        output_box.config(state="normal")
        output_box.insert(tk.END, f"[+] Port {port} is open\n")
        output_box.see(tk.END)
        output_box.config(state="disabled")
        
    except:
        pass

def start_scan():
    target = target_entry.get()
    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Start and End Ports must be integers.")
        return

    if start_port < 0 or end_port > 65535 or start_port > end_port:
        messagebox.showerror("Input Error", "Invalid port range.")
        return
    output_box.config(state="normal")
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, f"🔍 Scanning {target} from port {start_port} to {end_port}...\n\n")

    def scan():
        with ThreadPoolExecutor(max_workers=100) as executor:
            for port in range(start_port, end_port + 1):
                executor.submit(scan_port, target, port, output_box)

        output_box.config(state="normal")
        output_box.insert(tk.END, f"\n✅ Scan completed successfully.")
        output_box.see(tk.END)
        output_box.config(state="disabled")
    
    threading.Thread(target=scan).start()
    output_box.config(state="disabled")

# === GUI Setup ===
root = tk.Tk()
root.title("Port Scanner by Sultan Ahmmed")

root.iconbitmap("./icons.ico") 

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 450
window_height = 480
x_pos = int((screen_width - window_width) / 2)
y_pos = int((screen_height - window_height-200) / 2)

root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")



root.configure(bg="#213448")
root.resizable(False, False)
style = ttk.Style()
style.theme_use('clam')

FONT = ('Segoe UI', 10)
LABEL_STYLE = {"font": FONT, "background": "#213448", "foreground":"white"}

# Layout
ttk.Label(root, text="Target IP or Hostname:", **LABEL_STYLE).grid(row=0, column=0, padx=10, pady=(15, 5), sticky='w')
target_entry = ttk.Entry(root, width=30, font=FONT)
target_entry.grid(row=0, column=1, padx=10, pady=(15, 5), sticky='w')

ttk.Label(root, text="Start Port:", **LABEL_STYLE).grid(row=1, column=0, padx=10, pady=5, sticky='w')
start_port_entry = ttk.Entry(root, width=10, font=FONT)
start_port_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

ttk.Label(root, text="End Port:", **LABEL_STYLE).grid(row=2, column=0, padx=10, pady=5, sticky='w')
end_port_entry = ttk.Entry(root, width=10, font=FONT)
end_port_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')

# Custom style button
style.configure("Custom.TButton",
                font=('Segoe UI', 10),
                foreground="white",
                background="#183B4E")

style.map("Custom.TButton",
          foreground=[("active", "white"),  
                     ("pressed", "white")], 
          background=[("active", "#24596b"),
                      ("pressed", "#122c38")]) 

scan_button = ttk.Button(root, text="Start Scan", command=start_scan, style="Custom.TButton")
scan_button.grid(row=3, column=0, columnspan=3, pady=10)

output_box = scrolledtext.ScrolledText(root, width=60, height=20, font=('Consolas', 10), foreground="#1DCD9F", background="#210F37",bd=0)
output_box.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
output_box.config(state="disabled")

root.mainloop()
