from PIL import Image

img = Image.open("departamento.webp")
cocina = img.crop((1240, 0, 1920, 1080))
cocina.save("cocina_referencia.png")