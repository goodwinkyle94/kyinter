# What is your name?
# Do you prefer sleeping in or waking up early?
# What are your favorite types of music?
# rock, jazz, classical, hiphop, rap, country, metal, pop


# from icecream import ic
import tkinter
from tkinter import ttk


def main() -> None:
    root = initiate_tk()

    mainframe = main_frame_func(root)
    drop_down_menu(mainframe, root)
    input_info(mainframe)
    usrinpt_entry = entry_field(mainframe)
    print(usrinpt_entry.get())
    radio_button1, radiobutton2 = radio_buttons_func(mainframe)
    check_box_list = check_boxes_func(mainframe)
    # display_choices(mainframe)
    submit_button(mainframe, usrinpt_entry, radio_button1, radiobutton2, check_box_list)
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)
    root.bind("<Return>")
    root.mainloop()


def initiate_tk():
    root = tkinter.Tk()
    root.title("Klgoodwin Gui Assignment")
    root.columnconfigure(0, weight=5)
    root.rowconfigure(0, weight=5)
    return root


def main_frame_func(root):
    mainframe = ttk.Frame(root, padding="10 10 10 10")
    mainframe.grid(row=0, column=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
    return mainframe


def drop_down_menu(mainframe, root):
    menu_bar = tkinter.Menu(root)
    root.config(menu=menu_bar)
    file_menu = tkinter.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Clear", command=lambda: clear_form(mainframe))
    file_menu.add_command(label="Exit", command=root.quit)


def input_info(mainframe):
    usr_instruction = ttk.Label(mainframe, text=f"Input info\n{'':-^14}")
    usr_instruction.grid(row=5, column=0, pady=10)


def entry_field(mainframe):
    entry_box_label = ttk.Label(mainframe, text="What is your name?", padding="5")
    entry_box_label.grid(row=6, column=0)
    usr_input1 = tkinter.StringVar()
    entry_box = ttk.Entry(mainframe, textvariable=usr_input1)
    entry_box.grid(row=7, column=0, pady=5)
    return usr_input1


def radio_buttons_func(mainframe):
    usr_radio1 = tkinter.StringVar()
    usr_radio2 = tkinter.StringVar()
    radio_label = ttk.Label(
        mainframe, text="Do you like sleeping in, or waking up early", padding="5"
    )
    radio_label.grid(row=8, column=0)
    entry_radio1 = ttk.Radiobutton(
        mainframe, text="Sleeping in!", variable=usr_radio1, padding="5", value="1"
    )
    entry_radio2 = ttk.Radiobutton(
        mainframe, text="Waking up early!", variable=usr_radio2, padding="5", value="1"
    )
    entry_radio1.grid(row=9, column=0)
    entry_radio2.grid(row=10, column=0)
    return usr_radio1, usr_radio2


def check_boxes_func(mainframe) -> list:
    # What are your favorite types of music?
    # rock, jazz, classical, hiphop, rap, country, metal, pop
    check_box_label = ttk.Label(
        mainframe, text="What are your favorite types of music?", padding="5"
    )

    check_box_label.grid(row=11, column=0)
    check_box_bool = [tkinter.IntVar() for x in range(8)]
    music_genres = [
        "Rock",
        "Jazz",
        "Classical",
        "Hiphop",
        "Rap",
        "Country",
        "Metal",
        "Pop",
    ]

    check_boxes = []

    for i in range(len(music_genres)):
        check_box_bool[i].set(False)
        check_box = ttk.Checkbutton(
            mainframe, text=music_genres[i], variable=check_box_bool[i], padding="5"
        )
        check_boxes.append(check_box)
        check_boxes[i].grid(row=i + 12, column=0)
    return check_box_bool


def submit_button(
    mainframe, usrinpt_entry, radio_button1, radio_button2, check_box_list
):
    usr_info = ttk.Label(mainframe, text="")
    usr_info.grid(row=25, column=0, pady=10)
    my_button = ttk.Button(
        mainframe,
        text="Submit",
        command=lambda: display_results(
            usr_info, usrinpt_entry, radio_button1, radio_button2, check_box_list
        ),
    )
    my_button.grid(row=26, column=0, padx=20, pady=20)


"""music_genres = [
        "Rock",
        "Jazz",
        "Classical",
        "Hiphop",
        "Rap",
        "Country",
        "Metal",
        "Pop",
    ]"""


def display_results(
    usr_info, usrinpt_entry, radio_button1, radiobutton2, check_box_list
):
    name = usrinpt_entry.get()
    rock = "Rock" if check_box_list[0].get() else ""
    jazz = "Jazz" if check_box_list[1].get() else ""
    classical = "Classical" if check_box_list[2].get() else ""
    Hiphop = "Hiphop" if check_box_list[3].get() else ""
    Rap = "Rap" if check_box_list[4].get() else ""
    Country = "Country" if check_box_list[5].get() else ""
    Metal = "Metal" if check_box_list[6].get() else ""
    Pop = "Pop" if check_box_list[7].get() else ""
    # ic(radio_button1.get())
    morning = "Early riser!!!!" if radio_button1.get() == "1" else ""
    sleep_in = "Night owl!!!" if radiobutton2.get() == "1" else ""
    result_text = f"Name: {name}\n"
    result_text += f"Preferred music generes: {rock} {jazz} {classical} {Hiphop} {Rap} {Country} {Metal} {Pop}\n"
    result_text += f"{morning} {sleep_in}\n"
    # result_text += f"Favorite Color: {favorite_color}"

    usr_info.config(text=result_text)


def clear_form(mainframe):
    for widget in mainframe.winfo_children():
        if isinstance(widget, ttk.Entry):
            widget.delete(0, tkinter.END)
        elif isinstance(widget, ttk.Checkbutton):
            widget.state(["!selected"])
        elif isinstance(widget, ttk.OptionMenu):
            widget.setvar(widget.cget("textvariable"), "")
        elif isinstance(widget, ttk.Label) and "Submit" not in widget.cget("text"):
            widget.config(text="")
        usr_instruction = ttk.Label(mainframe, text=f"Input info\n{'':-^14}")
        usr_instruction.grid(row=5, column=0, pady=10)


if __name__ == "__main__":
    main()
