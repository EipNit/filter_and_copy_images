import os
import shutil

# 数据文件夹路径
data_dir = "data_mouse_time"
images_dir = os.path.join(data_dir, "images")
labels_dir = os.path.join(data_dir, "labels")
output_dir = "data_mouse_labels"
output_images_dir = os.path.join(output_dir, "images")
output_labels_dir = os.path.join(output_dir, "labels")

# 创建输出目录和子目录，如果已存在则不创建
os.makedirs(output_images_dir, exist_ok=True)
os.makedirs(output_labels_dir, exist_ok=True)

# 遍历标签文件夹中的所有文件
for label_file in os.listdir(labels_dir):
    # 构建完整的标签文件路径
    label_path = os.path.join(labels_dir, label_file)
    # 根据标签文件名构建对应的图片文件名
    image_file = label_file.replace('.txt', '.jpg')  # 假设图片文件是.jpg格式
    image_path = os.path.join(images_dir, image_file)

    # 检查对应的图片文件是否存在
    if os.path.exists(image_path):
        # 复制图片文件到输出目录的images子文件夹
        shutil.copy2(image_path, os.path.join(output_images_dir, image_file))
        # 同时复制标签文件到输出目录的labels子文件夹
        shutil.copy2(label_path, os.path.join(output_labels_dir, label_file))

print(f"标签对应的图片和标签文件已分别复制到 {output_images_dir} 和 {output_labels_dir}")
