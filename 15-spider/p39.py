import pytesseract as pt
from PIL import Image

# 生成图片实例
image = Image.open('/home/dz/桌面/3.jpg')

# 调用 pytesseract，将图片转换为文字
# 返回结果结束转换后的结果
text = pt.image_to_string(image)
print(text)