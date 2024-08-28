import tkinter as tk
import rotatescreen 


def Screen_rotation(temp):
	screen = rotatescreen.get_primary_display()
	if temp == "up":
		screen.set_landscape()
	elif temp == "right":
		screen.set_portrait_flipped()
	elif temp == "down":
		screen.set_landscape_flipped()
	elif temp == "left":
		screen.set_portrait()


root=tk.Tk()
root.geometry("200x200")
root.title("Screen Rotation")
root.configure(bg='light grey')

result = tk.StringVar()

b1=tk.Button(root, text="Up", command=lambda: Screen_rotation("up"), bg="white")
b1.grid(row=0, column=3)
b2=tk.Button(root, text="Right", command=lambda: Screen_rotation("right"), bg="white")
b2.grid(row=1, column=6)
b3=tk.Button(root, text="Left", command=lambda: Screen_rotation("left"), bg="white")
b3.grid(row=1, column=2)
b4=tk.Button(root, text="Down", command=lambda: Screen_rotation("down"), bg="white")
b4.grid(row=3, column=3)

root.mainloop()


