import os
import pandas as pd

# 读取1800.xlsx文件
df = pd.read_excel('1800.xlsx')

# 获取ImageName列的所有值
image_names = df['ImageName'].tolist()

# 获取'All'文件夹下的所有图片文件名
all_images = os.listdir('AllDataResize')

# 找出不在ImageName列的图片名称，并排除"easy.png"和"complex.png"
not_in_excel = [img for img in all_images if img not in image_names and img not in ["easy.png", "complex.png"]]

# 将不在ImageName列的图片名称保存到txt文件
with open('not_in_excel.txt', 'w') as f:
    for img in not_in_excel:
        f.write(f"'{img}',\n")

print("不在ImageName列的图片名称（排除easy.png和complex.png）已保存到not_in_excel.txt文件中。")