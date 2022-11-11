# Day 18 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Turtle and the Graphical User Interface (GUI) - Color Extractor

# import colorgram

rgb_colors = []

# Extract 11 colors from an image.
# Note: Need containing folder included in path for this to work properly.
colors = colorgram.extract('day19/logo.jpg', 11)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)