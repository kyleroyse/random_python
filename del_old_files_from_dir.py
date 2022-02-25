import os
from pathlib import Path
from datetime import datetime, timedata

root_folder = Path('path goes here')

def remove_old_files(root: Path):
    for dir in root.iterdir():
        for file in dir.glob('**/*.txt'):
            file_created_date = datetime.fromtimestamp(os.path.getmtime(file))
            now = datetime.now()
            ninety_days_ago = now - timedelta(days=90)
            if file_created_date >= ninety_days_ago:
                print(f'Deleting the file: {file}')
                file.unlink()


remove_old_files(root_folder)