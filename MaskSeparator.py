from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np


def SelectFile():
    x = filedialog.askopenfilename(title="Seleccionar Imagen", filetypes=[("img files", "*.png")])
    img = Image.open(x)
    img.save("Image - Original.png")
    img = img.resize((350, 350))
    img = ImageTk.PhotoImage(img)
    panel = Label(ventana, image=img)
    panel.image = img
    panel.place(x=20, y=40)

    img2 = Image.open("Image - Original.png")
    width, height = img2.size
    Result1 = Image.open("Image - Original.png")
    Result2 = Image.open("Image - Original.png")
    Result3 = Image.open("Image - Original.png")

    for x in range(width):
        for y in range(height):
            if len(img2.getpixel((x, y))) == 4:
                r, g, b, a = img2.getpixel((x, y))
            else:
                r, g, b = img2.getpixel((x, y))

            Result1.putpixel( (x, y), tuple([ r, r, r]))
            Result2.putpixel( (x, y), tuple([ g, g, g]))
            Result3.putpixel( (x, y), tuple([ b, b, b]))

    Result1.save("Image - Red.png")
    Result1 = Result1.resize((350, 350))
    Result1 = ImageTk.PhotoImage(Result1)
    panel1 = Label(ventana, image=Result1)
    panel1.image = Result1
    panel1.place(x=380, y=40)
    panel1.image = Result1

    Result2.save("Image - Blue.png")
    Result2 = Result2.resize((350, 350))
    Result2 = ImageTk.PhotoImage(Result2)
    panel2 = Label(ventana, image=Result2)
    panel2.image = Result2
    panel2.place(x=20, y=400)
    panel2.image = Result2

    Result3.save("Image - Green.png")
    Result3 = Result3.resize((350, 350))
    Result3 = ImageTk.PhotoImage(Result3)
    panel3 = Label(ventana, image=Result3)
    panel3.image = Result3
    panel3.place(x=380, y=400)
    panel3.image = Result3

ventana = Tk()
ventana.title("Mask Separator")
ventana.geometry("750x770")
ventana.config(bg="black")

boton_Cargar = Button(ventana, text="Select File", width=101, command=SelectFile).place(x=20, y=8)

ventana.mainloop()