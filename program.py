from tkinter import *
from tkinter import ttk
import model_temp
from encode import Encode
from numpy import reshape
import time


def set_footer(master):
    """

    :param master:
    :return:
    """
    # master frame is a Label:
    footer_background = PhotoImage(file="img/footer.png")
    master.img = footer_background
    master.config(image=master.img)


def loading(master, t):
    # get all frames in list:
    frames = [PhotoImage(file="img/loading.gif", format='gif -index %i' % i) for i in range(8)]

    load_img_lbl = Label(master)
    load_img_lbl.image = frames  # prevent deleting by garbage collector.
    load_img_lbl.pack(pady=(60, 0))

    tic = time.time()

    def animate(idx):
        load_img_lbl.configure(image=frames[idx])

        idx = 0 if idx > 6 else idx + 1  # loop over i

        # remove the loading after 't':
        toc = time.time()
        elapsed_time = toc - tic
        if elapsed_time < t:
            load_img_lbl.after(100, animate, idx)  # loop animation.
        else:
            load_img_lbl.pack_forget()

    animate(0)


class Gui:
    def __init__(self, root, color, font1, font2):
        self.color = color
        self.font1 = font1
        self.font2 = font2

        # districting:
        header_frame = Frame(root, bg=color)
        header_frame.pack(fill=BOTH, ipady=5)
        self.set_header_content(header_frame)

        #   create a line:
        line = Canvas(root, height=5)
        line.create_line(0, 2, 1000, 2, fill='red')
        line.pack(fill=X)

        # variables:
        self.importance_combo_str = StringVar()
        self.speed_combo_str = StringVar()
        self.topography_combo_str = StringVar()
        self.soil_combo_str = StringVar()
        self.waterLevel_combo_str = StringVar()
        self.numForces_combo_str = StringVar()
        self.defence_combo_str = StringVar()
        self.accessibility_combo_str = StringVar()
        self.visibility_combo_str = StringVar()

        content_frame = Frame(root)
        content_frame.pack()
        self.set_content(content_frame)

        footer_frame = Label(root)
        set_footer(footer_frame)
        footer_frame.pack()

        # import images:
        # self.img1 = PhotoImage(file="img/pishsakhteh.png").subsample(2, 2)
        # self.img2 = PhotoImage(file="img/darjariz.png").subsample(2, 2)
        # self.img3 = PhotoImage(file="img/sim.png").subsample(2, 2)
        # self.img4 = PhotoImage(file="img/bedonhefaz.png").subsample(2, 2)

    def set_header_content(self, master):
        """
        Puts header widgets on the app frame.
        :param master: root holder for widgets.
        :return:
        """
        # parameters:
        font = 'Calibri'

        Label(
            master=master,
            text="پیش نمایش",
            font=font
        ).pack(side='right')

        logo = PhotoImage(file="img/logo.png").subsample(2, 2)
        title = ttk.Label(
            master=master,
            background=self.color,
            text="پیشنهاد دیوار انسدادی مرزی، مبتنی بر هوش مصنوعی",
            font=font,
            wraplength=200,
            image=logo,
            compound="left",
            justify=CENTER
        )
        title.logo = logo  # garbage collection
        title['image'] = title.logo
        title.pack()

    def set_content(self, master):
        """

        :param master:
        :return:
        """
        # right side:
        query_frame = Frame(master)
        # query_frame.grid(row=10, columns=1, padx=10, pady=10)

        # two columns:
        # query_frame.columnconfigure(0)
        # query_frame.columnconfigure(1)

        # row 1, importance:
        # query_frame.rowconfigure(0)
        label_combo1 = Label(query_frame, text="اهمیت منطقه", padx=10, font=self.font2)
        combo1 = ttk.Combobox(query_frame, textvariable=self.importance_combo_str, state="readonly",
                              font=self.font2)
        combo1.config(values=['بالا', 'پایین'], justify='right')
        combo1.set("بالا")
        label_combo1.grid(row=0, column=1, sticky='e', pady=(50, 8))
        combo1.grid(row=0, column=0, pady=(50, 8))

        # row 2, running speed:
        # query_frame.rowconfigure(1)
        label_combo2 = Label(query_frame, text="سرعت اجرا", pady=8, padx=10, font=self.font2)
        combo2 = ttk.Combobox(query_frame, textvariable=self.speed_combo_str, state="readonly", font=self.font2)
        combo2.config(values=['مدت دار', 'کوتاه مدت'], justify='right')
        combo2.set("مدت دار")
        label_combo2.grid(row=1, column=1, sticky='e')
        combo2.grid(row=1, column=0)

        # row 3, topography:
        # query_frame.rowconfigure(2)
        label_combo3 = Label(query_frame, text="توپوگرافی منطقه", pady=8, padx=10, font=self.font2)
        combo3 = ttk.Combobox(query_frame, textvariable=self.topography_combo_str, state="readonly",
                              font=self.font2)
        combo3.config(values=['دشت', 'کوهستانی', 'تپه ماهور'], justify='right')
        combo3.set("دشت")
        label_combo3.grid(row=2, column=1, sticky='e')
        combo3.grid(row=2, column=0)

        # row 4,  soil:
        # query_frame.rowconfigure(4)
        label_combo4 = Label(query_frame, text="نوع خاک", pady=8, padx=10, font=self.font2)
        combo4 = ttk.Combobox(query_frame, textvariable=self.soil_combo_str, state="readonly", font=self.font2)
        combo4.config(values=['سست', 'متراکم'], justify='right')
        combo4.set("متراکم")
        label_combo4.grid(row=3, column=1, sticky='e')
        combo4.grid(row=3, column=0)

        # row 5, water level:
        # query_frame.rowconfigure(5)
        label_combo5 = Label(query_frame, text="سطح آب", pady=8, padx=10, font=self.font2)
        combo5 = ttk.Combobox(query_frame, textvariable=self.waterLevel_combo_str, state="readonly",
                              font=self.font2)
        combo5.config(values=['بالا', 'پایین'], justify='right')
        combo5.set("بالا")
        label_combo5.grid(row=4, column=1, sticky='e')
        combo5.grid(row=4, column=0)

        # row 6, num_forces:
        # query_frame.rowconfigure(6)
        label_combo6 = Label(query_frame, text="تعداد نیروی اجرایی", pady=8, padx=10, font=self.font2)
        combo6 = ttk.Combobox(query_frame, textvariable=self.numForces_combo_str, state="readonly", font=self.font2)
        combo6.config(values=['زیاد', 'کم'], justify='right')
        combo6.set("زیاد")
        label_combo6.grid(row=5, column=1, sticky='e')
        combo6.grid(row=5, column=0)

        # row 7, explosion:
        # query_frame.rowconfigure(7)
        label_combo7 = Label(query_frame, text="مقاومت دربرابر انفجار", pady=8, padx=10, font=self.font2)
        combo7 = ttk.Combobox(query_frame, textvariable=self.defence_combo_str, state="readonly", font=self.font2)
        combo7.config(values=['بله', 'خیر'], justify='right')
        combo7.set("خیر")
        label_combo7.grid(row=6, column=1, sticky='e')
        combo7.grid(row=6, column=0)

        # row 8, accessibility:
        # query_frame.rowconfigure(8)
        label_combo8 = Label(query_frame, text="دسترسی", pady=8, padx=10, font=self.font2)
        combo8 = ttk.Combobox(query_frame, textvariable=self.accessibility_combo_str, state="readonly",
                              font=self.font2)
        combo8.config(values=['سخت', 'آسان'], justify='right')
        combo8.set("آسان")
        label_combo8.grid(row=7, column=1, sticky='e')
        combo8.grid(row=7, column=0)

        #   row 9, visibility:
        # query_frame.rowconfigure(9)
        label_combo9 = Label(query_frame, text="دیوار دید داشته باشد", pady=8, padx=10, font=self.font2)
        combo9 = ttk.Combobox(query_frame, textvariable=self.visibility_combo_str, state="readonly",
                              font=self.font2)
        combo9.config(values=['خیر', 'بله'], justify='right')
        combo9.set("خیر")
        label_combo9.grid(row=8, column=1, sticky='e')
        combo9.grid(row=8, column=0)

        #   row 10, predict button:
        button_predict = Button(query_frame, text='پیشنهاد کن', padx=17, pady=0, font=self.font2)
        # add command in the in the of in the end of function.
        button_predict.grid(row=9, column=0, columnspan=2, pady=(10, 0))

        query_frame.pack(side='right')
        # left side:
        predict_frame = LabelFrame(master, text="دیوار پیشنهادی", font=self.font1, fg='blue')

        recommended_wall_lbl = Label(
            predict_frame, font=self.font2,
            text="لطفا مقادیر ورودی را وارد کنید و سپس روی پیشنهاد کن کلیک نمایید",
            justify='right',
            wraplength=250,
        )

        wall_imag = PhotoImage(file="img/wall_frame.png")
        wall_imag_lbl = Label(predict_frame, image=wall_imag)
        wall_imag_lbl.imag = wall_imag

        # pack everything to show:
        loading(predict_frame, 2)
        wall_imag_lbl.pack(pady=5, padx=15)
        recommended_wall_lbl.pack(pady=5)

        predict_frame.pack(side=LEFT, pady=(38, 0), padx=(20, 20), anchor='n')

        # command button:
        from functools import partial
        action_with_arg = partial(self.predict_click_event, button_predict, recommended_wall_lbl)
        button_predict.config(command=action_with_arg)

    def predict_click_event(self, button, label):
        # order: accessibility, defence, numForces, visibility, waterLevel, soil, topography, speed, importance.
        wait = 100
        # label.pack_forget()  # unvisible
        label['text'] = ". . . "
        # label.after(wait, lambda: label.pack())
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

        encode = Encode()
        translated_list = encode.translate_list(entered_user_list)
        x_test = encode.encode_words(translated_list)
        # print(enterd_user_list)
        # print(translated_list)
        # print(x_test)
        x_test = reshape(x_test, [1, -1])
        y = model_temp.ml.predict(x_test)[0]

        string_msg = "با توجه به مقادیر ورودی دیوار "

        # get the name of the predicted wall and add to the output message string:
        wall_name = encode.decode_wall_name(y)
        string_msg += "\"" + wall_name + "\""
        string_msg += " پیشنهاد می‌شود"

        # change the labels text:
        def f():
            label['text'] = string_msg

        label.after(wait, f)
        # label.config(text=string_msg)


if __name__ == '__main__':
    # set main specifications:
    root = Tk()
    root.title('پیشنهاد دیوار انسدادی مرزی - سما')
    root.iconbitmap("img\\fav_e29_icon.ico")
    root.geometry("600x680")
    root.resizable(0, 0)  # no resizable

    # change the style:
    style = ttk.Style()
    style.theme_use('clam')  # 'winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative'

    # bg_lbl = Label(root, image=bg_photo)
    # bg_lbl.place(x=0, y=57, relwidth=1, relheight=1)
    # bg_lbl.image = bg_photo

    Gui(root, 'white', 'Nazanin', ('IRANSans', 9))
    root.mainloop()
