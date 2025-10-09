# let’s build a real-world DevOps-style Python automation script that uses
# os + shutil + datetime
# to create daily backups and clean up old ones automatically.

# project_root/
# │
# ├── logs/
# │   ├── app.log
# │   └── debug.log
# │
# ├── backups/
# │
# └── backup_script.py


import os
import shutil
from datetime import datetime, timedelta

# === CONFIGURATION ===
SOURCE_DIR = "logs"              # folder to back up
BACKUP_DIR = "backups"           # where backups are stored
RETENTION_DAYS = 7               # keep backups for 7 days

# === CREATE BACKUP FOLDER IF NOT EXISTS ===
os.makedirs(BACKUP_DIR, exist_ok=True)

# === CREATE TIMESTAMPED BACKUP NAME ===
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_name = f"backup_{timestamp}"
backup_path = os.path.join(BACKUP_DIR, backup_name)

# === CREATE COMPRESSED BACKUP ===
shutil.make_archive(backup_path, "zip", SOURCE_DIR)
print(f"✅ Backup created: {backup_path}.zip")

# === DELETE OLD BACKUPS ===
now = datetime.now()
for filename in os.listdir(BACKUP_DIR):
    file_path = os.path.join(BACKUP_DIR, filename)
    if os.path.isfile(file_path):
        modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        age = now - modified_time
        if age > timedelta(days=RETENTION_DAYS):
            os.remove(file_path)
            print(f"🗑️ Deleted old backup: {filename}")

print("🎉 Backup task complete.")


# What This Does

# Creates a timestamped ZIP backup of your logs/ folder.
# Stores it under backups/ (e.g., backups/backup_2025-10-08_09-40-21.zip)
# Automatically deletes backups older than 7 days.


# Optional Enhancements

# Add email/slack alert after backup success.
# Integrate with cron (Linux) or Task Scheduler (Windows) to run daily.
# Backup multiple directories by looping through a list.


# example Cron Job (Linux)
# Run every day at 1 AM:
# 0 1 * * * /usr/bin/python3 /home/user/project/backup_script.py


# Result Example

# Backup created: backups/backup_2025-10-08_09-40-21.zip
# Deleted old backup: backup_2025-09-28_09-12-04.zip
# Backup task complete.
