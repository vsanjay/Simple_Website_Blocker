
"""
Created on Sun Jul  2 17:50:37 2017

@author: verdusanjay

"""
import time
from datetime import datetime as dt

hosts_path_mac_or_linux = "/private/etc/hosts"

hosts_path_windows = "C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"

websites_to_block = ["www.facebook.com","facebook.com","www.gmail.com","gmail.com"]

count = 0

while True:
    
    with open(hosts_path_mac_or_linux,'r+') as file:
        
        content = file.read()
        
        for website in websites_to_block:
            
            if website in content:
                pass
            else:
                file.write(redirect + " " + website + "\n")
                
    time.sleep(5)
                
            
            
    

