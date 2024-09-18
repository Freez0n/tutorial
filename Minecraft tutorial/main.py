from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

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
    # Очищаем Canvas перед добавлением нового текста
    canvas.delete("info_text")
    # Добавляем новый текст на Canvas
    canvas.create_text(0.5 * canvas.winfo_width(), 0.5 * canvas.winfo_height(),
                       text=info_texts[selected], font=("Arial", 24), fill="white", tags="info_text")

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

# Показать первую вкладку с информацией и скрыть кнопку
def show_first_info():
    selected_option.set(options[0])
    update_content()
    start_button.place_forget()
    prev_button.place(relx=0.4, rely=0.9, anchor='center')
    next_button.place(relx=0.6, rely=0.9, anchor='center')


root = Tk()
root.title("Туториал")


root.attributes('-fullscreen', True)
root.bind('<Escape>', exit_app)

# Фон окна
image = Image.open("fon.png")
background = ImageTk.PhotoImage(image)

# Создаие Canvas для расположение текста
canvas = Canvas(root)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=background)

# Кнопка переключение полноэкранного режима
toggle_button = Button(root, text="Полноэкранный", command=toggle_fullscreen, bg="#4B3D3D", fg="white", width=13, height=2, font=("Arial", 9))
toggle_button.place(x=10, y=10)

# Обозначния страниц для отображения информации
selected_option = StringVar(value='info1')
options = ['info1', 'info2', 'info3', 'info4']

# Содержимое информации
info_texts = {
    'info1': "Содержимое для информации 1",
    'info2': "Содержимое для информации 2",
    'info3': "Содержимое для информации 3",
    'info4': "Содержимое для информации 4",
}

# Кнопка для начала отображения первой информации
start_button = Button(root, text="Начать", command=show_first_info, bg="#4B3D3D", fg="white", width=16, height=2, font=("Arial", 16))
start_button.place(relx=0.5, rely=0.9, anchor='center')

# Кнопки для переключения информации
prev_button = Button(root, text="Назад", command=previous_info, bg="#4B3D3D", fg="white", width=10, height=2, font=("Arial", 16))
next_button = Button(root, text="Вперед", command=next_info, bg="#4B3D3D", fg="white", width=10, height=2, font=("Arial", 16))

# Иконка окна
root.iconbitmap("logo.ico")

root.mainloop()
