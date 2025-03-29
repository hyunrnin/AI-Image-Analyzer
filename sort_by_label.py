import os
import shutil
import pandas as pd
import json

# 예측 결과 파일 불러오기
with open("result.json", "r", encoding="utf-8") as f:
    results = json.load(f)

# 입력 이미지 폴더와 출력 폴더 설정
input_folder = "input_images"
output_folder = "sorted_images"
os.makedirs(output_folder, exist_ok=True)

# 예측 라벨에 따라 이미지 분류
for result in results:
    filename = result["filename"]
    label = result["predicted_label"]

    # 라벨 내 공백을 _로 변경하여 폴더 이름 생성
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