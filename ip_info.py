#!/usr/bin/env python3
# ==========================================
# RIK HACKER IP INFORMATION TOOL v4.0
# PART 1
# ==========================================

import os
import sys
import socket
import platform
import time
from datetime import datetime

# -----------------------------
# Install requests automatically
# -----------------------------
try:
    import requests
except ImportError:
    print("[+] Installing requests...")
    os.system(f"{sys.executable} -m pip install requests")
    import requests

# ==========================================
# COLORS
# ==========================================

RESET = "\033[0m"
BOLD = "\033[1m"

BLACK     = "\033[30m"
RED       = "\033[91m"
GREEN     = "\033[92m"
YELLOW    = "\033[93m"
BLUE      = "\033[94m"
MAGENTA   = "\033[95m"
CYAN      = "\033[96m"
WHITE     = "\033[97m"

LRED      = "\033[31m"
LGREEN    = "\033[32m"
LYELLOW   = "\033[33m"
LBLUE     = "\033[34m"
LMAGENTA  = "\033[35m"
LCYAN     = "\033[36m"

# ==========================================
# CLEAR SCREEN
# ==========================================

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ==========================================
# RIK HACKER BANNER
# ==========================================

def banner():
    try:
        os.system('termux-open-url "https://www.youtube.com/@Rik-Hacker"')
    except Exception:
        pass
    print(CYAN + "\n📺 Opening RIK HACKER YouTube Channel...\n" + RESET)
    time.sleep(2)
    clear()
    clear()

    print(CYAN + BOLD + r"""
██████╗ ██╗██╗  ██╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗
██╔══██╗██║██║ ██╔╝    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝██║█████╔╝     ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
██╔══██╗██║██╔═██╗     ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║██║██║  ██╗    ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
""" + RESET)

    print(GREEN + "╔══════════════════════════════════════════════════════════════╗")
    print("║               🌍 RIK HACKER - IP INFO TOOL v4.0            ║")
    print("╚══════════════════════════════════════════════════════════════╝" + RESET)

# ==========================================
# PRINT LINE
# ==========================================

def info_line(icon, title, value, color=WHITE):
    value=str(value)
    time.sleep(1)
    print(color + f"│ {icon} {title:<18}: {value}" + RESET)

# ==========================================
# SECTION HEADER
# ==========================================

def section(title):
    print(YELLOW + "┌──────────────────────────────────────────────────────────────┐")
    print(f"│ {title:<60}│")
    print("├──────────────────────────────────────────────────────────────┤" + RESET)

# ==========================================
# SECTION FOOTER
# ==========================================

def end_section():
    print(YELLOW + "└──────────────────────────────────────────────────────────────┘" + RESET)


# ==========================================
# PART 2
# IP LOOKUP & DATA COLLECTION
# ==========================================

API_URL = "http://ip-api.com/json/"

def get_ip_info(ip=""):
    """
    Get information for the current public IP
    or a user-provided public IP.
    """

    try:
        url = API_URL + ip.strip()
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(RED + "[!] Server Error!" + RESET)
            return None

        data = response.json()

        if data.get("status") != "success":
            print(RED + f"[!] {data.get('message','Lookup Failed')}" + RESET)
            return None

        return data

    except requests.exceptions.ConnectionError:
        print(RED + "[!] No Internet Connection!" + RESET)
        return None

    except requests.exceptions.Timeout:
        print(RED + "[!] Request Timed Out!" + RESET)
        return None

    except KeyboardInterrupt:
        print("\n" + RED + "[!] Cancelled by User." + RESET)
        sys.exit()

    except Exception as e:
        print(RED + f"[!] Error: {e}" + RESET)
        return None


# ==========================================
# HOSTNAME
# ==========================================

def get_hostname(ip):

    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return "N/A"


# ==========================================
# IP VERSION
# ==========================================

def get_ip_version(ip):

    if ":" in ip:
        return "IPv6"
    return "IPv4"


# ==========================================
# GOOGLE MAPS LINK
# ==========================================

def maps_link(lat, lon):
    return f"https://maps.google.com/?q={lat},{lon}"


# ==========================================
# SCAN TIME
# ==========================================

def scan_time():
    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")


# ==========================================
# SYSTEM INFO
# ==========================================

def system_info():

    return {
        "os": platform.system() + " " + platform.release(),
        "python": platform.python_version(),
        "hostname": socket.gethostname()
    }


# ==========================================
# MAIN INPUT
# ==========================================

banner()

print(CYAN + "\nEnter Public IP Address")
print(YELLOW + "Leave blank to scan your own public IP.\n" + RESET)

target_ip = input(GREEN + "IP >>> " + RESET).strip()

data = get_ip_info(target_ip)

if data is None:
    sys.exit()
    
    
# ==========================================
# PART 3
# NETWORK INFORMATION
# ==========================================

section("🌐 NETWORK INFORMATION")

info_line(
    "🌍",
    "Public IP",
    data.get("query", "N/A"),
    GREEN
)

info_line(
    "🔢",
    "IP Version",
    get_ip_version(data.get("query", "")),
    CYAN
)

info_line(
    "🧭",
    "Hostname",
    get_hostname(data.get("query", "")),
    YELLOW
)

info_line(
    "📡",
    "ISP",
    data.get("isp", "N/A"),
    BLUE
)

info_line(
    "🏢",
    "Organization",
    data.get("org", "N/A"),
    MAGENTA
)

info_line(
    "🆔",
    "ASN",
    data.get("as", "N/A"),
    LRED
)

info_line(
    "🌐",
    "AS Name",
    data.get("asname", "N/A"),
    LCYAN
)

info_line(
    "📶",
    "Mobile",
    str(data.get("mobile", "N/A")),
    LGREEN
)

info_line(
    "🔐",
    "Proxy",
    str(data.get("proxy", "N/A")),
    LYELLOW
)

info_line(
    "🏠",
    "Hosting",
    str(data.get("hosting", "N/A")),
    LBLUE
)

end_section()  



# ==========================================
# PART 4
# LOCATION INFORMATION
# ==========================================

section("📍 LOCATION INFORMATION")

info_line("🌎", "Country", data.get("country", "N/A"), GREEN)
info_line("🏳️", "Country Code", data.get("countryCode", "N/A"), CYAN)
info_line("🏙️", "Region", data.get("regionName", "N/A"), YELLOW)
info_line("📍", "Region Code", data.get("region", "N/A"), BLUE)
info_line("🏠", "City", data.get("city", "N/A"), MAGENTA)
info_line("📮", "ZIP Code", data.get("zip", "N/A"), LRED)
info_line("🕒", "Timezone", data.get("timezone", "N/A"), LCYAN)
info_line("📍", "Latitude", str(data.get("lat", "N/A")), LGREEN)
info_line("📍", "Longitude", str(data.get("lon", "N/A")), LYELLOW)
info_line(
    "🗺️",
    "Google Maps",
    maps_link(data.get("lat"), data.get("lon")),
    WHITE
)

end_section()

# ==========================================
# SYSTEM INFORMATION
# ==========================================

sys_info = system_info()

section("💻 SYSTEM INFORMATION")

info_line("🖥️", "OS", sys_info["os"], GREEN)
info_line("🐍", "Python", sys_info["python"], CYAN)
info_line("💻", "Device", sys_info["hostname"], YELLOW)
info_line("🕐", "Scan Time", scan_time(), MAGENTA)
info_line("✅", "Status", "Online", LGREEN)

end_section()

# ==========================================
# FOOTER
# ==========================================

print(CYAN + "╔══════════════════════════════════════════════════════════════╗")
print("║          ❤️ THANK YOU FOR USING RIK HACKER ❤️             ║")
print("║                IP INFORMATION TOOL v4.0                    ║")
print("╚══════════════════════════════════════════════════════════════╝")
print(RESET)  