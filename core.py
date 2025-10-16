import psutil
import socket
import platform
import subprocess
import requests
import os

# -------------------- Battery --------------------
def get_battery_status():
    battery = psutil.sensors_battery()
    if battery is None:
        return "Battery information is not available on this device."
    percent = battery.percent
    plugged = battery.power_plugged
    status = "charging" if plugged else "not charging"
    return f"Battery is at {percent}% and is currently {status}."

# -------------------- Volume --------------------
def get_volume_level():
    try:
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        level = int(volume.GetMasterVolumeLevelScalar() * 100)
        return f"The current volume level is {level} percent."
    except Exception as e:
        return f"Failed to get volume level: {e}"

def set_volume_level(level):
    try:
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(level / 100.0, None)
        return f"Volume set to {level} percent."
    except Exception as e:
        return f"Failed to set volume: {e}"

def mute_volume():
    return set_volume_level(0)

def max_volume():
    return set_volume_level(100)

# -------------------- Wi-Fi Status --------------------

def is_wifi_connected():
    try:
        result = subprocess.check_output("netsh wlan show interfaces", shell=True, universal_newlines=True)
        if "State" in result and "connected" in result.lower():
            return "Wi-Fi is connected."
        else:
            return "Wi-Fi is not connected."
    except Exception as e:
        return f"Could not determine Wi-Fi status: {e}"

# -------------------- Bluetooth Status --------------------

def is_bluetooth_connected():
    try:
        result = subprocess.check_output("PowerShell -Command \"Get-PnpDevice -Class Bluetooth | Where-Object { $_.Status -eq 'OK' }\"", shell=True, universal_newlines=True)
        if result.strip():
            return "Bluetooth is connected."
        else:
            return "Bluetooth is not connected."
    except Exception as e:
        return f"Could not determine Bluetooth status: {e}"

# -------------------- Process Management --------------------
def get_running_processes(limit=10):
    processes = []
    for p in psutil.process_iter(['name', 'cpu_percent']):
        try:
            cpu = p.cpu_percent(interval=0.1)
            if cpu is not None:
                processes.append((p.info['name'], cpu))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    sorted_procs = sorted(processes, key=lambda x: x[1], reverse=True)
    return [f"{name} - {cpu}% CPU" for name, cpu in sorted_procs[:limit]]


def kill_process(name):
    killed = False
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if name.lower() in proc.info['name'].lower():
                proc.kill()
                killed = True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return f"Process matching '{name}' killed." if killed else f"No process matching '{name}' found or access denied."


# -------------------- Network Utilities --------------------
def get_ip_info():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        public_ip = requests.get('https://api.ipify.org').text
        return f"Local IP: {local_ip}, Public IP: {public_ip}"
    except Exception as e:
        return f"Could not fetch IP information: {e}"
    
def run_speed_test():
    try:
        import sys
        real_stdout = sys.stdout
        sys.stdout = sys.__stdout__  # Fix for Anaconda

        import speedtest
        st = speedtest.Speedtest()
        st.get_best_server()
        download = round(st.download() / 1_000_000, 2)
        upload = round(st.upload() / 1_000_000, 2)

        sys.stdout = real_stdout  # Restore

        # Determine tier
        if download >= 100 and upload >= 50:
            tier = "Outstanding"
        elif download >= 40 and upload >= 20:
            tier = "Decent"
        elif download >= 10 and upload >= 5:
            tier = "Average"
        else:
            tier = "Poor- bhai band kar ke soja"

        return f"Download speed: {download} Mbps\nUpload speed: {upload} Mbps\nConnection tier: {tier}"

    except Exception as e:
        sys.stdout = real_stdout
        return f"Speed test failed: {e}"






