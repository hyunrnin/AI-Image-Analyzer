import subprocess
import time
import os
import shutil

# 결과물 삭제 함수
def reset_outputs():
    targets = [
        "result.json",  # JSON 파일도 삭제하도록 추가
        "result.csv",   # 만약 CSV도 필요 없으면 여기에 추가
        "class_distribution.png",
        "sorted_images",
        "wrong_predictions"
    ]

    print("\n결과물 초기화를 시작합니다.")
    for target in targets:
        if os.path.isdir(target):
            shutil.rmtree(target)
            print(f"폴더 삭제: {target}")
        elif os.path.isfile(target):
            os.remove(target)
            print(f"파일 삭제: {target}")
    print("초기화가 완료되었습니다.\n")

# 전체 실행 함수
def run_all_steps():
    print("\n이미지 분석을 시작합니다.")
    start_time = time.time()

    subprocess.run(["python", "classify_images.py"])
    subprocess.run(["python", "sort_by_label.py"])
    subprocess.run(["python", "generate_report.py"])

    end_time = time.time()
    print(f"\n모든 작업이 완료되었습니다. (총 소요 시간: {end_time - start_time:.2f}초)\n")

# 대화형 실행 루프
while True:
    print("\n명령 선택:")
    print("Enter 키          → 전체 실행")
    print("reset 입력        → 결과 초기화 (JSON 파일 포함)")
    print("exit 또는 quit 입력 → 프로그램 종료")

    command = input("\n입력: ").strip().lower()

    if command == "":
        run_all_steps()
    elif command in ("quit", "exit"):
        print("프로그램을 종료합니다.")
        break
    elif command == "reset":
        reset_outputs()
    else:
        print("알 수 없는 명령입니다. 다시 입력하세요.")