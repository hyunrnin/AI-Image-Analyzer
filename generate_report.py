import os
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import json
import csv

# 한글 폰트 설정 (Windows 기준)
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 예측 결과 불러오기
with open("result.json", "r", encoding="utf-8") as f:
    results = json.load(f)

# 폴더 경로 설정
input_folder = "input_images"
wrong_folder = "wrong_predictions"
os.makedirs(wrong_folder, exist_ok=True)

# 정답 라벨 파일을 CSV로 불러오기
gt_labels = {}
if os.path.exists("labels.csv"):
    with open("labels.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            gt_labels[row["filename"]] = row["ground_truth"]

# 정답과 비교
df = pd.DataFrame(results)
df["ground_truth"] = df["filename"].map(gt_labels)
df["correct"] = df["predicted_label"] == df["ground_truth"]

# 정확도 계산 및 오답 이미지 복사
if "ground_truth" in df.columns and df["ground_truth"].notna().any():
    acc = df["correct"].mean() * 100
    print(f"\n정확도: {acc:.2f}%")

    for _, row in df.iterrows():
        if row["correct"] is False:
            src = os.path.join(input_folder, row["filename"])
            dst = os.path.join(wrong_folder, row["filename"])
            if os.path.exists(src):
                shutil.copy(src, dst)

# 예측 분포 차트 생성
counts = df["predicted_label"].value_counts()
counts.plot(kind="bar", title="AI 예측 분포")
plt.ylabel("개수")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("class_distribution.png")
print("class_distribution.png 파일이 저장되었습니다.")

# 결과 JSON 저장 (정답 비교 포함)
with open("result.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("result.json 파일이 업데이트되었습니다.")
