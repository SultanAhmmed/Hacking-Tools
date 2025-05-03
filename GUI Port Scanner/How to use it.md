# 🔍 GUI Port Scanner Tool

A sleek, multi-threaded **GUI-based Port Scanner** built with Python and Tkinter.  
This tool allows users to scan a range of ports on a target IP address or hostname to find **open ports** in an efficient and user-friendly manner.

---

## 📌 Why This Tool?

Most port scanners run in the terminal and require technical knowledge. This project was created to:

- ✅ Simplify port scanning with a **graphical interface**
- 🚀 Enable **faster scanning** using **multi-threading**
- 🎯 Help students, developers, and network admins identify open services on a host easily
- 🎨 Provide a **modern, user-friendly design**

---

## 🖥️ Features

- 🌐 Target Hostname or IP input
- 🔢 Start and End Port Range selection
- 🚀 Multi-threaded fast scanning
- 📝 Live output window with open ports listed
- 🖼️ Modern UI using `ttk` theme and custom styles
- 📋 Scrollable results pane

---

## 🛠️ Requirements

- Python 3.7+
- `tkinter` (usually pre-installed with Python)

---

## 💻 How to Use

### 🔷 On Windows

1. **Clone the repository** or download the `.py` file.

2. Double-click the `.bat` launcher:

```bat
@echo off
python "Port Scanner.py"
```
This will automatically run the GUI without needing to open a terminal manually.
- ⚠️ Make sure Python is added to your PATH.

### 🐧 On Linux/macOS
Open terminal in the project directory.</br>
Run the script using:
```bash
python3 "Port Scanner.py"
```
## 📸 Screenshots  
![image](https://github.com/user-attachments/assets/21808c02-e4e1-43d1-8068-63e1eeba6cb3)

⚙️ How It Works  
- Uses the socket module to attempt connections to each port.  
- Multithreaded with ThreadPoolExecutor for fast performance.  
- UI built with tkinter, styled using ttk themes.  
- Results are printed to a ScrolledText widget.

## 🔐 Disclaimer  
This tool is for educational and authorized network testing purposes only.  
Do not scan networks without permission.

## 👨‍💻 Author  
<i>Sultan Ahmmed<i>  
<em>Made with ❤️ in Python.<em>
