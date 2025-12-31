import qrcode

url = "https://iamniharika.github.io/newyeargreeting/"

qrcode.make(url).save("qrcode.png")