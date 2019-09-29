from PIL import Image, ImageFilter, ImageDraw, ImageFont

im = Image.open('G:/Users/yang/Desktop/jpg/test.jpg')

# 过滤图片
im2 = im.filter(ImageFilter.BLUR)
im.save('G:/Users/yang/Desktop/jpg/blur.jpg', 'jpeg')

w, h = im.size
print('test jpg image size %s %s' % (w, h))

# 更改图片宽度
im.thumbnail((w // 2, h // 2))

print('resize test jpg image size %s %s' % (w // 2, h // 2))

im.save('G:/Users/yang/Desktop/jpg/resize.jpg', 'jpeg')

print("-----------------生成验证码测试-------------------")

import random


def rndChar():
    return chr(random.randint(65, 90))


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 60 * 4
height = 60
num = 0
while num <= 10:
    image3 = Image.new('RGB', (width, height), (255, 255, 255))

    font = ImageFont.truetype('G:/Windows/Fonts/Arial.ttf', 36)

    draw = ImageDraw.Draw(image3)

    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())

    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

    image3 = image3.filter(ImageFilter.BLUR)
    name = 'G:/Users/yang/Desktop/jpg/code' + str(num) + '.jpg'
    print(name)
    image3.save(name, 'jpeg')
    num = num + 1
