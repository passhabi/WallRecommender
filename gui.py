import tkinter
from tkinter import ttk
import model


class Form:
    def __init__(self, root):
        self.root = root
        self.mainframe = tkinter.Frame(self.root, bg='black')
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        self.build_grid()
        self.build_banner()
        self.build_buttons()

        self.importance_combo_str = tkinter.StringVar()
        self.speed_combo_str = tkinter.StringVar()
        self.topography_combo_str = tkinter.StringVar()
        self.soil_combo_str = tkinter.StringVar()
        self.waterLevel_combo_str = tkinter.StringVar()
        self.numForces_combo_str = tkinter.StringVar()
        self.defence_combo_str = tkinter.StringVar()
        self.accessibility_combo_str = tkinter.StringVar()
        self.visibility_combo_str = tkinter.StringVar()
        self.build_combos()

        self.build_footer()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)
        self.mainframe.rowconfigure(3, weight=0)
        self.mainframe.rowconfigure(4, weight=0)

    def build_banner(self):
        label_title = tkinter.Label(
            self.mainframe,  # place for label
            text="نسخه نمایشی",
            bg='black',
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
            bg='black',
            fg='white',
            font=('Tahoma', 25)
        )
        label_title.grid(
            row=1, column=0,
            sticky='new',
            padx=10, pady=10
        )

    def build_buttons(self):
        frame = tkinter.Frame(self.mainframe, bg='black')
        frame.grid(row=3, column=0, sticky='nsew', padx=20, pady=10)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        button_predict = tkinter.Button(
            frame,
            text='پیشبینی کردن',
        )
        button_predict.grid(
            row=0, column=2,
            sticky='e'
            # add command in the in the of build_button function.
        )

        tkinter.Label(
            frame,
            text=":دیوار پیشنهادی",
            bg='black',
            fg='white',
            font=('Arial', 10)
        ).grid(
            row=0, column=1,
            sticky='new',
            padx=10, pady=10
        )

        label = tkinter.Label(frame, bg='black', fg='white', font=('Arial', 10))
        label.grid(row=0, column=0, sticky='new', padx=10, pady=10)

        from functools import partial
        action_with_arg = partial(self.predict_click_event, button_predict, label)
        button_predict.config(command=action_with_arg)

    def predict_click_event(self, button, label):
        # order: accessibility, defence, numForces, visibility, waterLevel, soil, topography, speed, importance.
        import random
        wait = random.randint(100, 3000)
        label.grid_remove()  # unvisible
        label.after(wait, lambda: label.grid())
        button.config(state="disabled")
        button.after(wait, lambda: button.config(state="normal"))

        entered_user_list = [
            self.accessibility_combo_str.get(),
            self.defence_combo_str.get(),
            self.numForces_combo_str.get(),
            self.visibility_combo_str.get(),
            self.waterLevel_combo_str.get(),
            self.soil_combo_str.get(),
            self.topography_combo_str.get(),
            self.speed_combo_str.get(),
            self.importance_combo_str.get()
        ]
        from encode import Encode
        import numpy as np

        encode = Encode()
        translated_list = encode.translate_list(entered_user_list)
        x_test = encode.encode_words(translated_list)
        # print(enterd_user_list)
        # print(translated_list)
        # print(x_test)
        x_test = np.reshape(x_test, [1, -1])
        y = model.ml.predict(x_test)[0]

        if y == 1:
            label.config(text="دیوار پیش ساخته")
        if y == 2:
            label.config(text="دیوار درجاریز")
        if y == 3:
            label.config(text="سیم خاردار")
        if y == 4:
            label.config(text="بدون حفاظ")

    def build_combos(self):
        combos_frame = tkinter.Frame(self.mainframe, bg='black')
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

        # importance:
        label_combo1 = tkinter.Label(combos_frame, text="اهمیت منطقه", fg="white", bg="black")
        combo1 = ttk.Combobox(combos_frame, textvariable=self.importance_combo_str, state="readonly")
        combo1.config(values=['بالا', 'پایین'])
        combo1.set("بالا")
        label_combo1.grid(row=0, column=0, sticky='ew')
        combo1.grid(row=1, column=0, sticky='ew')

        # running speed:
        label_combo2 = tkinter.Label(combos_frame, text="سرعت اجرا", fg="white", bg="black")
        combo2 = ttk.Combobox(combos_frame, textvariable=self.speed_combo_str, state="readonly")
        combo2.config(values=['بلند', 'کوتاه'])
        combo2.set("بلند")
        label_combo2.grid(row=0, column=1, sticky='ew')
        combo2.grid(row=1, column=1, sticky='ew')

        # topography:
        label_combo3 = tkinter.Label(combos_frame, text="توپوگرافی منطقه", fg="white", bg="black")
        combo3 = ttk.Combobox(combos_frame, textvariable=self.topography_combo_str, state="readonly")
        combo3.config(values=['دشت', 'کوهستانی', 'تپه ماهور'])
        combo3.set("دشت")
        label_combo3.grid(row=0, column=2, sticky='ew')
        combo3.grid(row=1, column=2, sticky='ew')

        # soil:
        label_combo4 = tkinter.Label(combos_frame, text="نوع خاک", fg="white", bg="black")
        combo4 = ttk.Combobox(combos_frame, textvariable=self.soil_combo_str, state="readonly")
        combo4.config(values=['ضعیف', 'قوی'])
        combo4.set("قوی")
        label_combo4.grid(row=0, column=3, sticky='ew')
        combo4.grid(row=1, column=3, sticky='ew')

        # water level:
        label_combo5 = tkinter.Label(combos_frame, text="سطح آب", fg="white", bg="black")
        combo5 = ttk.Combobox(combos_frame, textvariable=self.waterLevel_combo_str, state="readonly")
        combo5.config(values=['بالا', 'پایین'])
        combo5.set("بالا")
        label_combo5.grid(row=0, column=4, sticky='ew')
        combo5.grid(row=1, column=4, sticky='ew')

        # num_forces:
        label_combo6 = tkinter.Label(combos_frame, text="تعداد نیروی اجرایی", fg="white", bg="black")
        combo6 = ttk.Combobox(combos_frame, textvariable=self.numForces_combo_str, state="readonly")
        combo6.config(values=['زیاد', 'کم'])
        combo6.set("زیاد")
        label_combo6.grid(row=2, column=2, sticky='ew')
        combo6.grid(row=3, column=2, sticky='ew')

        # Defence:
        label_combo7 = tkinter.Label(combos_frame, text="پدافند", fg="white", bg="black")
        combo7 = ttk.Combobox(combos_frame, textvariable=self.defence_combo_str, state="readonly")
        combo7.config(values=['زیاد', 'متوسط', 'کم'])
        combo7.set("متوسط")
        label_combo7.grid(row=2, column=3, sticky='ew')
        combo7.grid(row=3, column=3, sticky='ew')

        # accessibility
        label_combo8 = tkinter.Label(combos_frame, text="دسترسی", fg="white", bg="black")
        combo8 = ttk.Combobox(combos_frame, textvariable=self.accessibility_combo_str, state="readonly")
        combo8.config(values=['سخت', 'آسان'])
        combo8.set("آسان")
        label_combo8.grid(row=2, column=4, sticky='ew')
        combo8.grid(row=3, column=4, sticky='ew')

        # visibility:
        label_combo9 = tkinter.Label(combos_frame, text="دید", fg="white", bg="black")
        label_combo9.grid(row=2, column=1, sticky='ew')
        combo9 = ttk.Combobox(combos_frame, textvariable=self.visibility_combo_str, state="readonly")
        combo9.config(values=['خیر', 'بله'])
        combo9.set("خیر")
        combo9.grid(row=3, column=1, sticky='ew')

    def build_footer(self):
        footer_lablel = tkinter.Label(
            self.mainframe,
            text="S A M A",
            bg='black',
            fg='white',
            font=('Verdana', 6)
        ).grid(
            row=4, column=0,
            sticky='new',
            padx=10, pady=10
        )


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('Wall Prediction')
    root.geometry("500x350")
    form = Form(root)  # create an object.
    root.mainloop()
