# Image Compressor

#Firstly we need to install pillow module 
#pip install pillow

#now we can import that 
import PIL
from PIL import Image
from tkinter import filedialog


# after import the module 
# now we can create Image Compressor function 

file_path = filedialog.askopenfilename()
img = PIL.Image.open(file_path)
myHeight, myWidth = img.size

img = img.resize((myHeight, myWidth), Image.ANTIALIAS)

save_path = filedialog.asksaveasfilename()



#saving process
img.save(save_path+"_compressed.JPG")

