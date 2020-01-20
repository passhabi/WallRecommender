import tkinter
from tkinter import ttk


class Form:
    def __init__(self, root):
        self.root = root
        self.mainframe = tkinter.Frame(self.root, bg='gray')
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)
        self.build_grid()
        self.build_banner()
        self.build_buttons()

        self.combo1_text = tkinter.StringVar()
        self.combo2_text = tkinter.StringVar()
        self.combo3_text = tkinter.StringVar()
        self.combo4_text = tkinter.StringVar()
        self.combo5_text = tkinter.StringVar()
        self.combo6_text = tkinter.StringVar()
        self.combo7_text = tkinter.StringVar()
        self.combo8_text = tkinter.StringVar()

        self.build_combos()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)
        self.mainframe.rowconfigure(3, weight=0)

    def build_banner(self):
        label_title = tkinter.Label(
            self.mainframe,  # place for label
            text="نسخه نمایشی",
            bg='gray',
            fg='white',
            font=('Arial', 10)
        )
        label_title.grid(
            row=0, column=0,
            sticky='e',
            padx=3, pady=1
        )

        label_title = tkinter.Label(
            self.mainframe,  # place for label
            text="پیشبینی دیوار بهینه",
            bg='gray',
            fg='white',
            font=('Tahoma', 25)
        )
        label_title.grid(
            row=1, column=0,
            sticky='new',
            padx=10, pady=10
        )

    def build_buttons(self):
        buttons_frame = tkinter.Frame(self.mainframe, bg='gray')
        buttons_frame.grid(row=3, column=0, sticky='nsew', padx=20, pady=10)
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        button_predict = tkinter.Button(
            buttons_frame,
            text='پیشبینی کردن',
            command=self.button_predict_event
        )

        button_predict.grid(
            row=0, column=1,
            sticky='e',
        )

    def button_predict_event(self):
        print("predict button clicked")

    def build_combos(self):
        combos_frame = tkinter.Frame(self.mainframe, bg='gray')
        combos_frame.grid(row=1, column=0, sticky='ew', padx=10, pady=10)
        combos_frame.columnconfigure(0, weight=1)
        combos_frame.columnconfigure(1, weight=1)
        combos_frame.columnconfigure(2, weight=1)
        combos_frame.columnconfigure(3, weight=1)
        combos_frame.columnconfigure(4, weight=1)

        combos_frame.rowconfigure(0, weight=1)
        combos_frame.rowconfigure(1, weight=1)
        combos_frame.rowconfigure(2, weight=1)
        combos_frame.rowconfigure(3, weight=1)

        "اهمیت منطقه"
        label_combo1 = tkinter.Label(combos_frame, text="اهمیت منطقه", fg="white", bg="gray")
        combo1 = ttk.Combobox(combos_frame, textvariable=self.combo1_text, state="readonly")
        combo1.config(values=['بالا', 'پایین'])
        combo1.set("بالا")
        label_combo1.grid(row=0, column=0, sticky='ew')
        combo1.grid(row=1, column=0, sticky='ew')

        "سرعت اجرا"
        label_combo2 = tkinter.Label(combos_frame, text="سرعت اجرا", fg="white", bg="gray")
        combo2 = ttk.Combobox(combos_frame, textvariable=self.combo2_text, state="readonly")
        combo2.config(values=['زیاد', 'کوتاه'])
        combo2.set("زیاد")
        label_combo2.grid(row=0, column=1, sticky='ew')
        combo2.grid(row=1, column=1, sticky='ew')

        "توپوگرافی منطقه"
        label_combo3 = tkinter.Label(combos_frame, text="توپوگرافی منطقه", fg="white", bg="gray")
        combo3 = ttk.Combobox(combos_frame, textvariable=self.combo3_text, state="readonly")
        combo3.config(values=['دشت', 'کوهستانی', 'تپه ماهور'])
        combo3.set("دشت")
        label_combo3.grid(row=0, column=2, sticky='ew')
        combo3.grid(row=1, column=2, sticky='ew')

        "نوع خاک"
        label_combo4 = tkinter.Label(combos_frame, text="نوع خاک", fg="white", bg="gray")
        combo4 = ttk.Combobox(combos_frame, textvariable=self.combo4_text, state="readonly")
        combo4.config(values=['ضعیف', 'قوی'])
        combo4.set("قوی")
        label_combo4.grid(row=0, column=3, sticky='ew')
        combo4.grid(row=1, column=3, sticky='ew')

        "سطح آب"
        label_combo5 = tkinter.Label(combos_frame, text="سطح آب", fg="white", bg="gray")
        combo5 = ttk.Combobox(combos_frame, textvariable=self.combo5_text, state="readonly")
        combo5.config(values=['بالا', 'پایین'])
        combo5.set("بالا")
        label_combo5.grid(row=0, column=4, sticky='ew')
        combo5.grid(row=1, column=4, sticky='ew')

        "تعداد نیروی اجرایی"
        label_combo6 = tkinter.Label(combos_frame, text="تعداد نیروی اجرایی", fg="white", bg="gray")
        combo6 = ttk.Combobox(combos_frame, textvariable=self.combo6_text, state="readonly")
        combo6.config(values=['زیاد', 'کم'])
        combo6.set("زیاد")
        label_combo6.grid(row=2, column=2, sticky='ew')
        combo6.grid(row=3, column=2, sticky='ew')

        "پدافند"
        label_combo7 = tkinter.Label(combos_frame, text="پدافند", fg="white", bg="gray")
        combo7 = ttk.Combobox(combos_frame, textvariable=self.combo7_text, state="readonly")
        combo7.config(values=['زیاد', 'متوسط', 'کم'])
        combo7.set("متوسط")
        label_combo7.grid(row=2, column=3, sticky='ew')
        combo7.grid(row=3, column=3, sticky='ew')

        "دسترسی"
        label_combo8 = tkinter.Label(combos_frame, text="دسترسی", fg="white", bg="gray")
        combo8 = ttk.Combobox(combos_frame, textvariable=self.combo8_text, state="readonly")
        combo8.config(values=['سخت', 'آسان'])
        combo8.set("آسان")
        label_combo8.grid(row=2, column=4, sticky='ew')
        combo8.grid(row=3, column=4, sticky='ew')


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('Wall Prediction')
    root.geometry("500x350")
    Form(root)
    root.mainloop()
