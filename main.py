import random
import tkinter as tk
from tkinter import messagebox


def new_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    number_entry.config(state="normal")
    number_entry.delete(0, tk.END)
    check_button.config(state="normal")
    result_label.config(text="Введите число от 1 до 100")
    attempts_label.config(text="Попыток: 0")
    number_entry.focus_set()


def check_number():
    global attempts
    if number_entry.cget("state") == "disabled":
        return

    try:
        number = int(number_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целое число.")
        return

    if number < 1 or number > 100:
        messagebox.showerror("Ошибка", "Число должно быть от 1 до 100.")
        return

    attempts += 1
    attempts_label.config(text=f"Попыток: {attempts}")
    if number < secret_number:
        result_label.config(text="Загаданное число больше")
    elif number > secret_number:
        result_label.config(text="Загаданное число меньше")
    else:
        result_label.config(text=f"Вы угадали число {secret_number}!")
        number_entry.config(state="disabled")
        check_button.config(state="disabled")


def small_window():
    window.geometry("420x320")


def large_window():
    window.geometry("600x450")


def show_rules():
    """Открыть окно с правилами игры."""
    messagebox.showinfo(
        "Правила",
        "Компьютер загадал целое число от 1 до 100.\n"
        "Введите число и нажмите «Проверить».\n"
        "Подсказки помогут найти ответ.\n"
        "Количество попыток не ограничено.",
    )


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Угадай число")
    window.geometry("420x320")
    window.minsize(420, 320)
    window.resizable(True, True)


    menu = tk.Menu(window)
    window.config(menu=menu)

    game_menu = tk.Menu(menu, tearoff=0)
    game_menu.add_command(label="Новая игра", command=new_game)
    game_menu.add_separator()
    game_menu.add_command(label="Выход", command=window.destroy)
    menu.add_cascade(label="Игра", menu=game_menu)

    settings_menu = tk.Menu(menu, tearoff=0)
    settings_menu.add_command(label="420 × 320", command=small_window)
    settings_menu.add_command(label="600 × 450", command=large_window)
    menu.add_cascade(label="Размер окна", menu=settings_menu)
    help_menu = tk.Menu(menu, tearoff=0)
    help_menu.add_command(label="Правила", command=show_rules)
    menu.add_cascade(label="Помощь", menu=help_menu)

    tk.Label(window, text="Угадай число", font=("Arial", 18)).pack(pady=15)
    tk.Label(window, text="Компьютер загадал число от 1 до 100").pack()

    number_entry = tk.Entry(window, justify="center", font=("Arial", 14))
    number_entry.pack(pady=10)

    check_button = tk.Button(window, text="Проверить", command=check_number)
    check_button.pack()

    result_label = tk.Label(window)
    result_label.pack(pady=10)
    attempts_label = tk.Label(window)
    attempts_label.pack()
    tk.Button(window, text="Новая игра", command=new_game).pack(pady=10)

    new_game()
    window.mainloop()
