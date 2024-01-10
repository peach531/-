from PIL import Image

area = (230,155,1110,770)
size = (640,200)

lion_img = Image.open("Lion.jpg")
fruit_img = Image.open("Fruit.png")

print(lion_img.size, lion_img.format, lion_img.mode)
print(fruit_img.size, fruit_img.format, fruit_img.mode)

fruit_resz = fruit_img.resize(size)
lion_cropped = lion_img.crop(area)
lion_img.show()

lion_cropped.save("lion_cropped.jpg")
fruit_resz.save("fruit_resized.png")
