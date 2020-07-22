# 生成1000张学员海报
'''
需求：
1. 1000张海报名字不同，改在图片LTing处
2. 为每为同学的海报生成单独的2维码（选做）
'''
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img = Image.open('.\\1.png')

print(img.format)        # 输出图片基本信息
print(img.mode)
print(img.size)

# img.resize((600,800)).save("resize.jpg")

# img.rotate(45).save("rotate.jpg")

name = 'koopa'

draw = ImageDraw.Draw(img)
font = ImageFont.truetype('fonts\\simhei.ttf', 110)# 字体和文字大小均为自定
# print(img.size)
draw.text((785, 1090), name, fill=(0,0,0), font=font)# 图像宽/高像素比为1832/2774，可确定需更改的文字位置为785/1090
img.show()
img.save('koopa.jpg')


