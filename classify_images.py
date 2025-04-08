import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()
API_KEY = os.getenv("API_KEY")
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

BASE_URL = "https://api-inference.huggingface.co/models/facebook/deit-base-patch16-224"

if not API_KEY:
    raise ValueError("API_KEY를 불러올 수 없습니다. .env 파일을 확인하세요.")
if not BASE_URL.startswith("https://"):
    raise ValueError("BASE_URL이 잘못되었습니다.")

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

input_dir = "input_images"
results = []

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

with open("result.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("\nresult.json 파일이 생성되었습니다.")