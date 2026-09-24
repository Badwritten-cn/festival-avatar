#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 1600
FONT = "/System/Library/Fonts/Hiragino Sans GB.ttc"

def f(size, idx=0):
    try:
        return ImageFont.truetype(FONT, size, index=idx)
    except Exception:
        return ImageFont.truetype(FONT, size)

# 背景：红金渐变
img = Image.new("RGB", (W, H), "#8B1A1A")
d = ImageDraw.Draw(img)
top = (0xC8, 0x10, 0x2E)
bot = (0x6E, 0x0E, 0x14)
for y in range(H):
    t = y / H
    r = int(top[0] + (bot[0] - top[0]) * t)
    g = int(top[1] + (bot[1] - top[1]) * t)
    b = int(top[2] + (bot[2] - top[2]) * t)
    d.line([(0, y), (W, y)], fill=(r, g, b))

GOLD = "#F3D383"
CREAM = "#F7F1E3"

# 顶部装饰边框
d.rectangle([40, 40, W - 40, H - 40], outline=GOLD, width=4)
d.rectangle([56, 56, W - 56, H - 56], outline="rgba(243,211,131,120)", width=1)

def center_text(y, text, font, fill):
    bb = d.textbbox((0, 0), text, font=font)
    w = bb[2] - bb[0]
    d.text(((W - w) / 2 - bb[0], y), text, font=font, fill=fill)

# 标题
center_text(120, "月满山河", f(96, 1), GOLD)
center_text(250, "双节头像工坊", f(60, 1), CREAM)
center_text(345, "中秋 × 国庆  ·  专属节日头像生成器", f(30), "#E8C87A")

# 分隔线
d.line([(200, 420), (W - 200, 420)], fill=GOLD, width=2)

# 卖点
feats = [
    "上传一张照片，10 秒生成节日头像",
    "18 种节日场景 · 7 种整体模板",
    "诗词款相框：婵娟 / 海月 / 玉盘 / 望岳 / 多娇",
    "照片全程本地处理，不上传任何服务器",
]
fy = 470
ffont = f(34)
for ft in feats:
    bb = d.textbbox((0, 0), ft, font=ffont)
    w = bb[2] - bb[0]
    x = (W - w) / 2 - bb[0]
    d.text((x - 40, fy), "•", font=ffont, fill=GOLD)
    d.text((x, fy), ft, font=ffont, fill=CREAM)
    fy += 66

# 二维码
qr = Image.open("/Users/whs/Desktop/Lingma_Space/festival-avatar/qr.png").convert("RGB")
qs = 460
qr = qr.resize((qs, qs), Image.LANCZOS)
qx = (W - qs) // 2
qy = 800
# 白底卡片
pad = 30
d.rounded_rectangle([qx - pad, qy - pad, qx + qs + pad, qy + qs + pad], radius=24, fill="#FFFFFF")
img.paste(qr, (qx, qy))

# 二维码下文字
center_text(qy + qs + 70, "长按识别二维码 · 立即生成你的双节头像", f(34, 1), GOLD)
center_text(qy + qs + 130, "微信内长按图片即可保存到相册", f(26), "#E8C87A")

# 底部链接
center_text(H - 130, "badwritten-cn.github.io/festival-avatar", f(28), CREAM)

img.save("/Users/whs/Desktop/Lingma_Space/festival-avatar/share-card.png", "PNG")
print("saved share-card.png", img.size)
