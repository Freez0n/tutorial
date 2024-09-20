from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw


# Закрытие приложения на ESC
def exit_app(event=None):
    root.destroy()


# Переключение полноэкранного режима
def toggle_fullscreen():
    is_fullscreen = root.attributes('-fullscreen')
    root.attributes('-fullscreen', not is_fullscreen)
    if root.attributes('-fullscreen'):
        toggle_button.config(text="Полноэкранный")
    else:
        toggle_button.config(text="Оконный")


# Обновление информации при нажатии кнопок
def update_content(*args):
    selected = selected_option.get()
    canvas.delete("info_text")

    width, height = canvas.winfo_width(), canvas.winfo_height()
    image = Image.open("fon.png").resize((width, height))
    draw = ImageDraw.Draw(image)
    text = info_texts[selected]

    # Шрифта из майнкрафта
    font = ImageFont.truetype("minecraft.ttf", 24)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Расположение текста
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    draw.text((x, y), text, font=font, fill="white")

    img_tk = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=img_tk, tags="info_text")
    canvas.image = img_tk


# Переход к следующей информации
def next_info():
    current_index = options.index(selected_option.get())
    next_index = (current_index + 1) % len(options)
    selected_option.set(options[next_index])
    update_content()


# Переход к предыдущей информации
def previous_info():
    current_index = options.index(selected_option.get())
    prev_index = (current_index - 1) % len(options)
    selected_option.set(options[prev_index])
    update_content()


# Показать первую вкладку
def show_first_info():
    selected_option.set(options[0])
    update_content()
    start_button.place_forget()
    prev_button.place(relx=0.4, rely=0.9, anchor='center')
    next_button.place(relx=0.6, rely=0.9, anchor='center')


def create_minecraft_button(master, text, command):
    button = Button(
        master, text=text, command=command,
        bg="#A0A0A0", fg="white",
        activebackground="#6E6E6E",
        activeforeground="white",
        font=minecraft_font,
        width=12, height=1,
        relief="ridge", bd=3,
        highlightthickness=1, highlightbackground="black"
    )
    return button


root = Tk()
root.title("Туториал")
root.attributes('-fullscreen', True)
root.bind('<Escape>', exit_app)

# Фон и иконка окна
image = Image.open("fon.png")
background = ImageTk.PhotoImage(image)
root.iconbitmap("logo.ico")

# Создание Canvas
canvas = Canvas(root)
canvas.pack(fill="both", expand=True)

# Изначальный фон
canvas.create_image(0, 0, anchor="nw", image=background, tags="background")

# Шрифт для кнопок
minecraft_font = ("minecraft.ttf", 16)

# Кнопка переключения полноэкранного режима
toggle_button = create_minecraft_button(root, "Полноэкранный", toggle_fullscreen)
toggle_button.place(x=10, y=10)

# Обозначения страниц для отображения информации
selected_option = StringVar(value='info1')
options = ['info1', 'info2', 'info3', 'info4','info5', 'info6', 'info7', 'info8']

# Содержимое информации
info_texts = {
    'info1': "Собрать верстак. Для этого нужно собрать 16 блоков дерева и превратить их в доски. \n\nПосле чего из 4 досок можно сделать верстак.\n\nОставшееся дерево пригодится потом.",
    'info2': "Собрать инструменты. На верстаке можно создавать \n\nразные инструменты, такие как кирка и лопата. \n\nОни пригодятся для добычи ресурсов.",
    'info3': "Построить убежище. Самый простой вариант — это небольшая землянка, \n\nгде можно спокойно дождаться наступления рассвета.",
    'info4': "Позаботиться о пище. Источниками пищи выступают животные, \n\nтакие как коровы, свиньи и курицы, а также овощи и фрукты.",
    'info5': "Сделайте кровать. После сбора достаточного количества еды \n\nнайдите овец, чтобы скрафтить себе кровать.",
    'info6': "Отмечайте путь до дома. Чтобы избежать подобных неприятностей, \n\nрасставьте факела по пути, \n\nчтобы можно было легко вернуться назад.",
    'info7': "Избегайте пещер. Делать шахту с лестницей лучше и безопаснее,\n\nчем лезть в темную пещеру без брони \n\nили дополнительного снаряжения.",
    'info8': "Так что сделайте шахту прямо под своим убежищем. \n\nЕсли вы не можете найти средства для обустройства ночлега, \n\nоставайтесь в доме и сделайте вход в шахту, \n\nподкопавшись под землю.",
}

# Кнопка для начала отображения первой вкладки
start_button = create_minecraft_button(root, "Начать", show_first_info)
start_button.place(relx=0.5, rely=0.5, anchor='center')

# Кнопки для переключения информации
prev_button = create_minecraft_button(root, "Назад", previous_info)
next_button = create_minecraft_button(root, "Вперед", next_info)

root.mainloop()
