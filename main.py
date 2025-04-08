import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from PIL import Image, ImageTk
from find_motion import find_motion
from identify import maincall
import time


def show_splash():
    splash = tk.Tk()
    splash.title("Loading...")

    
    splash_width, splash_height = 500, 300
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    x_coord = (screen_width - splash_width) // 2
    y_coord = (screen_height - splash_height) // 2
    splash.geometry(f"{splash_width}x{splash_height}+{x_coord}+{y_coord}")
    splash.overrideredirect(True)

    
    splash_img = Image.open('icons/splash2.png').resize((500, 300), Image.Resampling.LANCZOS)
    splash_photo = ImageTk.PhotoImage(splash_img)
    splash_label = tk.Label(splash, image=splash_photo)
    splash_label.pack()

    
    splash.after(3000, splash.destroy)
    splash.mainloop()


show_splash()


window = tk.Tk()
window.title("Smart CCTV")
window.iconphoto(False, tk.PhotoImage(file='icons/mn.png'))
window.geometry('1080x700')
window.configure(bg='#2c3e50')  # Dark background


title_font = font.Font(size=35, weight='bold', family='Helvetica')
button_font = font.Font(size=20, weight='bold')


header_frame = tk.Frame(window, bg='#34495e')
header_frame.pack(fill='x', pady=10)

label_title = tk.Label(header_frame, text="Smart CCTV Camera", font=title_font, fg='white', bg='#34495e')
label_title.pack(pady=10)

icon = Image.open('icons/spy.png').resize((100, 100), Image.Resampling.LANCZOS)
icon_img = ImageTk.PhotoImage(icon)
label_icon = tk.Label(header_frame, image=icon_img, bg='#34495e')
label_icon.pack()


button_frame = tk.Frame(window, bg='#2c3e50')
button_frame.pack(pady=20)


def create_button(frame, text, image_path, command, row, col, fg_color):
    btn_image = Image.open(image_path).resize((40, 40), Image.Resampling.LANCZOS)
    btn_img = ImageTk.PhotoImage(btn_image)
    button = tk.Button(
        frame,
        text=text,
        command=command,
        font=button_font,
        image=btn_img,
        compound='left',
        height=90,
        width=220,
        fg=fg_color,
        bg='#34495e',
        activebackground='#3e4f5c',
        bd=0
    )
    button.image = btn_img  
    button.grid(row=row, column=col, padx=20, pady=15)
    return button


create_button(button_frame, 'Monitor', 'icons/lamp.png', find_motion, 0, 0, 'green')
create_button(button_frame, 'Rectangle', 'icons/rectangle-of-cutted-line-geometrical-shape.png', rect_noise, 0, 1, 'orange')
create_button(button_frame, 'Noise', 'icons/security-camera.png', noise, 1, 0, 'green')
create_button(button_frame, 'Record', 'icons/recording.png', record, 1, 1, 'orange')
create_button(button_frame, 'In Out', 'icons/incognito.png', in_out, 2, 0, 'green')
create_button(button_frame, 'Identify', 'icons/recording.png', maincall, 2, 1, 'orange')


quit_btn = tk.Button(
    window,
    text='Exit',
    command=window.quit,
    font=button_font,
    height=3,
    width=20,
    fg='white',
    bg='#e74c3c',
    activebackground='#c0392b',
    bd=0
)
quit_btn.pack(pady=20)


window.mainloop()