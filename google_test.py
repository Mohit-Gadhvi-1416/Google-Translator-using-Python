from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Translator function
def change(text="type", src="English", dest="Hindi"):
    trans = Translator()
    trans1 = trans.translate(text, src=src, dest=dest)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='#f0f0f0')  # Light grey background for the main window

# Define new colors and fonts
bg_color = "#282c34"  # Dark background color for labels
fg_color = "#61dafb"  # Light blue text color for labels
text_bg_color = "#ffffff"  # White background for text boxes
text_fg_color = "#000000"  # Black text color for text boxes
button_bg_color = "#61dafb"  # Light blue background for button
button_fg_color = "#282c34"  # Dark text color for button
font_main = ("Helvetica", 24, "bold")
font_sub = ("Helvetica", 16, "bold")
font_textbox = ("Helvetica", 14)

# Main label
lab_txt = Label(root, text="Translator", font=font_main, fg=fg_color, bg=bg_color)
lab_txt.place(x=100, y=40, height=50, width=300)

# Source Text Label
lab_txt = Label(root, text="Source Text", font=font_sub, fg=fg_color, bg=bg_color)
lab_txt.place(x=100, y=100, height=20, width=300)

# Source Text Box
Sor_txt = Text(root, font=font_textbox, wrap=WORD, bg=text_bg_color, fg=text_fg_color)
Sor_txt.place(x=10, y=130, height=150, width=480)

# Language selection
list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(root, value=list_text)
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set("English")

button_change = Button(root, text="Translate", relief=RAISED, command=data, bg=button_bg_color, fg=button_fg_color, font=font_sub)
button_change.place(x=170, y=300, height=40, width=150)

comb_dest = ttk.Combobox(root, value=list_text)
comb_dest.place(x=330, y=300, height=40, width=150)
comb_dest.set("Hindi")

# Destination Text Label
lab_txt = Label(root, text="Dest Text", font=font_sub, fg=fg_color, bg=bg_color)
lab_txt.place(x=100, y=360, height=20, width=300)

# Destination Text Box
dest_txt = Text(root, font=font_textbox, wrap=WORD, bg=text_bg_color, fg=text_fg_color)
dest_txt.place(x=10, y=400, height=150, width=480)

root.mainloop()
