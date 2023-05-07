import os
import shutil
import random
from glob import glob

# 데이터셋 디렉토리
src_dirs = [
    "/home/uit-lim/vspython/directory/calamari", 
    "/home/uit-lim/vspython/directory/Cutlassfish", 
    "/home/uit-lim/vspython/directory/mackerel", 
    "/home/uit-lim/vspython/directory/Spanish mackerel"
]

# 저장할 기본 경로 설정
train_output_path = "/home/uit-lim/vspython/change_files/train"
val_output_path = "/home/uit-lim/vspython/change_files/val"

# 데이터셋 구조 생성
os.makedirs(os.path.join(train_output_path, "images"), exist_ok=True)
os.makedirs(os.path.join(train_output_path, "labels"), exist_ok=True)
os.makedirs(os.path.join(val_output_path, "images"), exist_ok=True)
os.makedirs(os.path.join(val_output_path, "labels"), exist_ok=True)

# 학습 및 검증 데이터 분할 비율 (예: 80% 학습, 20% 검증)
split_ratio = 0.8

for src_dir in src_dirs:
    # 이미지와 레이블 파일 경로 가져오기
    image_files = glob(os.path.join(src_dir, "new_images", "*"))
    label_files = [os.path.join(src_dir, "new_txt", os.path.splitext(os.path.basename(f))[0] + ".txt") for f in image_files]

    # 데이터셋을 학습 및 검증 세트로 분할
    num_train = int(len(image_files) * split_ratio)
    train_image_files = image_files[:num_train]
    train_label_files = label_files[:num_train]
    val_image_files = image_files[num_train:]
    val_label_files = label_files[num_train:]

    # 이미지와 레이블 파일을 적절한 폴더에 복사
    for img_f, lbl_f in zip(train_image_files, train_label_files):
        shutil.copy(img_f, os.path.join(train_output_path, "images", os.path.basename(img_f)))
        shutil.copy(lbl_f, os.path.join(train_output_path, "labels", os.path.basename(lbl_f)))

    for img_f, lbl_f in zip(val_image_files, val_label_files):
        shutil.copy(img_f, os.path.join(val_output_path, "images", os.path.basename(img_f)))
        shutil.copy(lbl_f, os.path.join(val_output_path, "labels", os.path.basename(lbl_f)))
