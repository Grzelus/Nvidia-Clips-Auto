import os
import shutil
import re


def filter(keyword, source_folder, extention):
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(extention) and keyword in filename:
            match = re.search(r"\d{4}\.\d{2}\.\d{2}", filename)
            if match:
                date = match.group(0)
                target_folder = os.path.join(source_folder,date)

                os.makedirs(target_folder, exist_ok=True)

                src_path = os.path.join(source_folder,filename)
                dst_path = os.path.join(target_folder,filename)

                if not os.path.exists(dst_path):
                    shutil.move(src_path, dst_path)