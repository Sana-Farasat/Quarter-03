import qrcode

image = qrcode.make("https://www.youtube.com/@panaverse")

print(type(image))

image.save("panaversity.png")

print("Qr Code has been generated successfully ..")