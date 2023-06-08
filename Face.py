"""# Define the dimensions of the face
face_width = 10
face_height = 8

# Print the top row of the face
print(" " + "-"*(face_width-2) + " ")

# Print the middle rows of the face
for i in range(face_height-2):
    print("|" + " "*(face_width-2) + "|")

# Print the bottom row of the face
print(" " + "-"*(face_width-2) + " ")

# Print the smile
print(" "*(face_width//2-1) + "^" + " "*(face_width//2-1))"""

# Define the dimensions of the image
image_width = 60
image_height = 40

# Print the top row of the image
print(" " + "-"*(image_width-2) + " ")

# Print the middle rows of the image
for i in range(image_height-2):
    print("|" + " "*(image_width-2) + "|")

# Print the bottom row of the image
print(" " + "-"*(image_width-2) + " ")

# Print the Mona Lisa's face
print(" "*(image_width//2-5) + "  o   o  " + " "*(image_width//2-5))
print(" "*(image_width//2-5) + "   ^   " + " "*(image_width//2-5))
print(" "*(image_width//2-5) + "  \\_/  " + " "*(image_width//2-5))

# Print the Mona Lisa's hair
print(" "*(image_width//2-5) + "/   \\ " + " "*(image_width//2-5))
print(" "*(image_width//2-5) + " \\___/" + " "*(image_width//2-5))
