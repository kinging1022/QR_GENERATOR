import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image, ImageTk
import qrcode


class APP(ctk.CTk):
    def __init__(self):
        # window set up
        ctk.set_appearance_mode('light')
        super().__init__(fg_color='white')

        # customization
        self.geometry('400x400')
        self.title('')
        self.iconbitmap('empty.ico')

        # entry field
        self.entry_string = ctk.StringVar()
        self.entry_string.trace('w', self.create_qr)
        EntryField(self, self.entry_string, self.save_qr)
        self.bind('<Return>', self.save_qr)

        # QR CODE
        self.image = None
        self.tk_image = None
        self.qr_image = QrImage(self)


        self.mainloop()

    def create_qr(self, *args):
        current_text = self.entry_string.get()
        if current_text:
            self.image = qrcode.make(current_text).resize((200, 200))
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.qr_image.update_image(self.tk_image)
        else:
            self.qr_image.clear()
            self.image = None
            self.tk_image = None

    def save_qr(self, event=''):
        if self.image:
            file_path = filedialog.asksaveasfilename()
            if file_path:
                self.image.save(file_path+'.jpg')



class EntryField(ctk.CTkFrame):
    def __init__(self, parent, entry_string,save_func):
        super().__init__(parent, corner_radius=20, fg_color='#021FB3')

        self.place(relx=0.5, rely=1, relwidth=1, relheight=0.4, anchor='center')

        # grid layout
        self.rowconfigure((0, 1), weight=1, uniform='a')
        self.columnconfigure(0, weight=1, uniform='a')

        # widgets
        self.frame = ctk.CTkFrame(self, fg_color='transparent')
        self.frame.columnconfigure(0, weight=1, uniform='b')
        self.frame.columnconfigure(1, weight=4, uniform='b')
        self.frame.columnconfigure(2, weight=1, uniform='b')
        self.frame.columnconfigure(3, weight=1, uniform='b')
        self.frame.grid(row=0, column=0)

        entry = ctk.CTkEntry(self.frame,
                             fg_color='#2E54E8',
                             border_width=0,
                             text_color='white',
                             textvariable=entry_string)
        entry.grid(row=0, column=1, sticky='nsew', padx=10)

        button = ctk.CTkButton(self.frame, fg_color='#2E54E8', hover_color='#4266f1', command=save_func, text='save')
        button.grid(row=0, column=2, sticky='nsew')


class QrImage(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, background='white', bd=0, highlightthickness=0, relief='ridge')
        self.place(relx=0.5, rely=0.4, width=200, height=200,  anchor='center')

    def clear(self):
        self.delete('all')

    def update_image(self, image_tk):
        self.clear()
        self.create_image(0, 0, image=image_tk, anchor='nw')


APP()

