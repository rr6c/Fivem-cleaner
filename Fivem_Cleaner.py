import os, shutil, time

os.system('title unban made by Noot#0515')
print("""
 /$$   /$$                       /$$       /$$ /$$    /$$$$$$  /$$$$$$$   /$$   /$$$$$$$ 
| $$$ | $$                      | $$      / $$/ $$   /$$$_  $$| $$____/ /$$$$  | $$____/ 
| $$$$| $$  /$$$$$$   /$$$$$$  /$$$$$$   /$$$$$$$$$$| $$$$\ $$| $$     |_  $$  | $$      
| $$ $$ $$ /$$__  $$ /$$__  $$|_  $$_/  |   $$  $$_/| $$ $$ $$| $$$$$$$  | $$  | $$$$$$$ 
| $$  $$$$| $$  \ $$| $$  \ $$  | $$     /$$$$$$$$$$| $$\ $$$$|_____  $$ | $$  |_____  $$
| $$\  $$$| $$  | $$| $$  | $$  | $$ /$$|_  $$  $$_/| $$ \ $$$ /$$  \ $$ | $$   /$$  \ $$
| $$ \  $$|  $$$$$$/|  $$$$$$/  |  $$$$/  | $$| $$  |  $$$$$$/|  $$$$$$//$$$$$$|  $$$$$$/
|__/  \__/ \______/  \______/    \___/    |__/|__/   \______/  \______/|______/ \______/ 
""")

def Cleaner():
    user = os.getlogin()
    time.sleep(0.8)
    shutil.rmtree(f"C:\\Users\\{user}\\AppData\\Local\\DigitalEntitlements")
    time.sleep(0.8)
    shutil.rmtree(f"C:\\Users\\{user}\\AppData\\Local\\FiveM\\FiveM.app\\citizen")
    time.sleep(0.8)
    shutil.rmtree(f"C:\\Users\\{user}\\AppData\\Local\\FiveM\\FiveM.app\\data\\cache")
    time.sleep(0.8)
    shutil.rmtree(f"C:\\Users\\{user}\\AppData\\Roaming\\CitizenFX")
    time.sleep(0.8)
    shutil.rmtree(f"C:\\Users\\{user}\\AppData\\Local\\FiveM\\FiveM.app\\logs")
    time.sleep(0.8)
    input("Enter any key for close...")
Cleaner()