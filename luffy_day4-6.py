# 生成1000张学员海报
'''
需求：
1. 1000张海报名字不同，改在图片LTing处
2. 为每为同学的海报生成单独的2维码（选做）
'''
from PIL import Image,ImageDraw,ImageFont
from MyQR import myqr

# print(img.size) # 1832*2774

# 创建1000个名字，姓*名*中间名 = 10*10*10 == 1000
def creat_names():
    last_name = '绫波 碇 明日 葛城 渚 庵野 绪方 三石 宫村 林原'
    first_name = '丽 真嗣 香  美里 薰 秀明 慧美 琴乃 优子 惠美'
    middle_name = '` ! @ # $ % ^ & _ +'
    last_name, first_name, middle_name, name_list = last_name.split(), first_name.split(), middle_name.split(), []

    for x in last_name:
        for y in middle_name:
            for z in first_name:
                name_list.append(x+y+z)
    return name_list

name_list = creat_names()

# 图像处理
n = 0 # 计数变量，用在二维码命名、二维码内容
for _ in name_list[:5]: # 测试用，只生成5张图片。
# for _ in name_list: # 强烈不建议直接执行程序，文件夹中会多出2000张图片。
    img = Image.open('.\\poster.png')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('fonts\\simhei.ttf', 110)# 字体和文字大小均为自定。

    draw.text((700, 1090), _, fill=(0,0,0), font=font)# 添加名字
    draw.text((700, 1110), '__'*(len(_)-1)+'_', fill=(225,171,104), font=font) # 添加下划线，中文占两个字符，符号占一个字符，所以下划线个数为2n*len(n)-1个。
    # 生成二维码
    myqr.run(words='{}'.format(n),version=6,picture=".\\qrcode.png",colorized=True,save_name='{}.png'.format(n)) # 生成二维码
    img2 = Image.open('.\\{}.png'.format(n)) # 使用刚生成的二维码
    n += 1
    img2 = img2.resize((210, 210)) # 二维码调整到适合图片的大小

    img.paste(img2, (210, 2085)) # 合并两图片
    img.save('.\\海报 {}.png'.format(_)) # 保存新图片，命名为本图片上的名字。
    # img.show()

'''
所需图片：
1.poster.png——海报模板
2.qrcode.png——二维码背景图片

遇到的问题：
1.windows中文件命名不能有*，中间名用*之后报错
2.如果没有本地文件，img和img2可以替换为：
img1_url = 'https://img-blog.csdnimg.cn/20200612223403525.png'
img2_url = 'https://bkimg.cdn.bcebos.com/pic/8ad4b31c8701a18b40a118a5902f07082938fe96?'
img1 = Image.open(BytesIO(requests.get(img1_url).content))
img2 = Image.open(BytesIO(requests.get(img2_url).content)).resize((210,210)).convert('L')
3.由于用MyQR库生成二维码必须保存至本地，二维码中的信息不能有中文，而且返回的不是二维码图片对象而是元组，无法简单的合并图片，放弃
'''
import qrcode

# 创建1000个名字
def creat_names():
    last_name = '绫波 碇 明日 葛城 渚 庵野 绪方 三石 宫村 林原'
    first_name = '丽 真嗣 香  美里 薰 秀明 慧美 琴乃 优子 惠美'
    middle_name = '` ! @ # $ % ^ & _ +'
    last_name, first_name, middle_name, names = last_name.split(), first_name.split(), middle_name.split(), []
    # 姓*名*中间名 = 10*10*10 = 1000
    for x in last_name:
        for y in middle_name:
            for z in first_name:
                names.append(x+y+z)
    return names

# 选作题二维码部分
def qrcode_generate(info):
    # 生成二维码
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
    )
    qr.add_data(info)# 二维码中的信息为各个名字
    qr_img = qr.make_image(fill_color="black", back_color='white').resize((210, 210))
    return qr_img


# 生成优秀学员海报的图像处理
def poster_generate(name):
    img = Image.open('.\\poster.png')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('fonts\\simhei.ttf', 110)# 字体和文字大小
    # 添加名字和下划线
    draw.text((700, 1090), name, fill=(0,0,0), font=font)
    draw.text((700, 1110), '__'*(len(name)-1)+'_', fill=(225,171,104), font=font) # 中文占两个字符，符号占一个字符，所以下划线个数为2n*len(n)-1个。
    # 合并二维码和海报图片
    img.paste(qrcode_generate(name), (210, 2085))
    # 保存新图片，命名为本图片上的名字。
    img.save('.\\海报 {}.png'.format(name))
    # img.show()

def main():
    name_list = creat_names()
    # for _ in name_list[:5]: # 只生成5幅海报图片
    for _ in name_list:
        poster_generate(_)

if __name__ == "__main__":
    main()