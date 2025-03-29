# 🤖 AI 이미지 분석기

이 프로젝트는 **Hugging Face API**를 활용하여 이미지를 분류하고, 결과를 JSON 파일로 저장한 뒤, 예측된 라벨에 따라 이미지를 폴더에 정리하고, 리포트를 생성하는 이미지 분석 프로젝트입니다.

---

## 👤 MADE BY

- **김현민**

---
## ✅ 주요 기능

- Hugging Face의 **ViT 모델**(`facebook/deit-base-patch16-224`)을 사용하여 이미지를 분류
- 이미지를 예측한 라벨에 따라 **자동으로 정리** (폴더별 분류)
- 예측 결과를 **`result.json`** 파일에 저장하고, 예측 분포 차트를 **`class_distribution.png`**로 생성
- **정확도 계산** 및 **잘못 분류된 이미지**는 **`wrong_predictions/`** 폴더로 이동
- 대화형 인터페이스 제공 (`main.py`)

---

## 📦 설치 방법

1. 레포 클론

```bash
git clone https://github.com/your-username/ai-image-analyzer.git
cd ai-image-analyzer
```

2. 필수 패키지 설치

```bash
pip install -r requirements.txt
```

---

## ⚙️ 환경 설정 (.env 파일)

1. `.env.example` 파일을 복사하여 `.env` 파일 생성

```bash
cp .env.example .env
```

2. 아래 정보를 입력

```env
API_KEY=your_huggingface_api_key_here
```

---

## ▶️ 실행 방법

1. 이미지를 **`input_images/`** 폴더에 넣고, 아래 명령어로 실행합니다.

```bash
python main.py
```

2. 명령어를 입력하면 대화형 인터페이스가 나타납니다.  
   `Enter` 키를 눌러 전체 실행을 시작하거나, `reset` 명령어로 결과를 초기화할 수 있습니다.  
   `exit` 또는 `quit`을 입력하면 종료됩니다.

---

## 📂 GitHub에 포함되지 않는 파일

`.gitignore`에 의해 아래 파일은 업로드되지 않습니다:

- `.env` (API 키 보안)
- `result.json` (분석 결과)
- `sorted_images/` (정리된 이미지들)
- `wrong_predictions/` (잘못 분류된 이미지들)
- `class_distribution.png` (예측 분포 차트)

---

## 💡 확장 아이디어

- **웹 인터페이스** 추가 (Gradio, Streamlit 등)
- **다양한 모델 지원**: 다른 이미지 분류 모델 사용 (예: ResNet, CLIP 등)
- **결과 대시보드** 구현: 예측 결과와 정확도를 보여주는 웹 대시보드

---

## 🧠 라이선스 & 출처

- 모델 제공: [Hugging Face](https://huggingface.co/)
- 모델 링크: [facebook/deit-base-patch16-224](https://huggingface.co/facebook/deit-base-patch16-224)

---
