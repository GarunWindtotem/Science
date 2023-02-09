import tkinter as tk
import random
import tkinter.messagebox

def show_text():
    label.config(text="Hey Jürgen :)")
    root.config(bg='green')
    message = random.choice(messages)
    tkinter.messagebox.showinfo("Christian Message", message)

root = tk.Tk()
root.title("Smiley Button")
root.geometry("300x200")

messages = [
    "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life. - John 3:16",
    "Do not be afraid, for I am with you; I will bring your children from the east and gather you from the west. - Isaiah 43:5",
    "Trust in the Lord with all your heart and lean not on your own understanding; in all your ways submit to him, and he will make your paths straight. - Proverbs 3:5-6",
    "I can do all this through him who gives me strength. - Philippians 4:13",
    "Come to me, all you who are weary and burdened, and I will give you rest. - Matthew 11:28"
]

label = tk.Label(root, text="", font=("Helvetica", 16))
label.pack()

button = tk.Button(root, text="😊", command=show_text, font=("Helvetica", 16))
button.pack()

root.mainloop()
