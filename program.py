from tkinter import *
from tkinter import ttk


class Gui:
    def __init__(self, root, color, font):
        self.color = color
        self.font = font

        # districting:
        header_frame = Frame(root, bg=color)
        header_frame.pack(fill=BOTH)
        self.set_header_content(header_frame)

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
            text="نسخه آزمایشی",
            font=font
        ).pack(side='right')

        logo = PhotoImage(file="img/logo.png").subsample(2, 2)
        title = ttk.Label(
            master=master,
            background=self.color,
            text="پیشنهاد دیوار انسدادی مرز جنوب شرقی (ایران پاکستان)، مبتنی بر هوش مصنوعی",
            font=font,
            wraplength=280,
            image=logo,
            compound="left"
        )
        title.logo = logo  # garbage collection
        title['image'] = title.logo
        title.pack()


if __name__ == '__main__':
    # set main specifications:
    root = Tk()
    root.title('پیشنهاد دیوار انسدادی مرزی - سما')
    root.iconbitmap("img\\fav_e29_icon.ico")
    root.geometry("500x100")
    # root.resizable(0, 0)  # no resizable

    Gui(root, 'white', 'Nazanin')
    root.mainloop()
