import os
import shutil
import pandas as pd
import json

with open("result.json", "r", encoding="utf-8") as f:
    results = json.load(f)

input_folder = "input_images"
output_folder = "sorted_images"
os.makedirs(output_folder, exist_ok=True)

for result in results:
    filename = result["filename"]
    label = result["predicted_label"]

    label_folder = os.path.join(output_folder, label.replace(" ", "_"))
    os.makedirs(label_folder, exist_ok=True)

    src = os.path.join(input_folder, filename)
    dst = os.path.join(label_folder, filename)

    if os.path.exists(src):
        shutil.copy(src, dst)
        print(f"{filename} → {label_folder}/")
    else:
        print(f"파일을 찾을 수 없습니다: {src}")

print("\n이미지 정리가 완료되었습니다.")