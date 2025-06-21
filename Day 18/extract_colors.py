import colorgram

extracted_colors = colorgram.extract('colors.jpg', 30)
colors = []

for col in extracted_colors:
    red = col.rgb.r
    green = col.rgb.g
    blue = col.rgb.b
    rgb = (red, green, blue)
    colors.append(rgb)

print(colors)