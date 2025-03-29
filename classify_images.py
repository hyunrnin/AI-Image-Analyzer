import os
import requests
from dotenv import load_dotenv
import json

# 환경 변수에서 API 키 불러오기
load_dotenv()
API_KEY = os.getenv("API_KEY")
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# 모델 URL (사전 학습된 이미지 분류 모델)
BASE_URL = "https://api-inference.huggingface.co/models/facebook/deit-base-patch16-224"

# 환경 변수 및 URL 유효성 확인
if not API_KEY:
    raise ValueError("API_KEY를 불러올 수 없습니다. .env 파일을 확인하세요.")
if not BASE_URL.startswith("https://"):
    raise ValueError("BASE_URL이 잘못되었습니다.")

# 이미지 분류 함수
def classify_image(path):
    with open(path, "rb") as f:
        image_data = f.read()

    response = requests.post(BASE_URL, headers=HEADERS, data=image_data)

    try:
        result = response.json()
        if isinstance(result, list):
            return result[0]["label"], result[0]["score"]
        else:
            return "unknown", 0.0
    except Exception as e:
        print(f"JSON 파싱 오류: {e}")
        return "error", 0.0

# 입력 이미지 폴더 설정
input_dir = "input_images"
results = []

# 이미지 반복 처리
for filename in os.listdir(input_dir):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        filepath = os.path.join(input_dir, filename)
        label, score = classify_image(filepath)
        results.append({
            "filename": filename,
            "predicted_label": label,
            "score": round(score * 100, 2)
        })
        print(f"{filename} → {label} ({score:.2f}%)")

# 결과 JSON 파일로 저장
with open("result.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("\nresult.json 파일이 생성되었습니다.")