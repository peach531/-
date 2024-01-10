from PIL import Image

fruit_img = Image.open("fruit.png")
fruit_rotate = fruit_img.rotate(270)
fruit_convert = fruit_img.convert('L')

fruit_rotate.show()
fruit_convert.show()
fruit_rotate.save("fruit_rotate.png")
fruit_convert.save("fruit_convert.png")
