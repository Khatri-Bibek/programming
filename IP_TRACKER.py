def track_ip(ip_address):
    url = f"http://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    return data
if _name_ == "_main_":
    ip = input("Enter IP address: ")
    info = track_ip(ip)
    print("\n--- IP Information ---")
    for key, value in info.items():
        print(f"{key}: {value}")
import tkinter as tk
from tkinter import messagebox
import requests

def track_ip():
    ip = entry.get()
    if not ip:
        messagebox.showwarning("Input Error", "Please enter an IP address")
        return
    url = f"http://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        data = response.json()
        result = "\n".join(f"{key}: {value}" for key, value in data.items())
        messagebox.showinfo("IP Information", result)   
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")