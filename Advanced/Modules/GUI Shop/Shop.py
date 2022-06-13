import tkinter as tk
from auth_service import register, login


def clear_window(window):
    for child in window.winfo_children():
        child.destroy()


def render_main_screen(window):
    tk.Button(
        window,
        text="Login",
        bg="green",
        fg="white",
        command=lambda: render_login_screen(window)
    ).grid(row=0, column=0)
    tk.Button(
        window,
        text="Register",
        bg="yellow",
        fg="black",
        command= lambda: render_register_screen(window)
    ).grid(row=0, column=1)


def render_login_screen(window):
    clear_window(window)

    tk.Label(window, text="Enter username: ").grid(row=0, column=0)
    username = tk.Entry(window)
    username.grid(row=0, column=1)

    tk.Label(window, text="Enter password: ").grid(row=1, column=0)
    password = tk.Entry(window, show="*")
    password.grid(row=1, column=1)

    def on_login():
        username_value = username.get()
        password_value = password.get()

        result = login(username_value, password_value)

        if result:
            pass
        else:
            tk.Label(window, text="Invalid username or password.", fg="red").grid(row=2, column=1)


    tk.Button(
        window,
        text="Login",
        bg="green",
        fg="black",
        command= on_login
    ).grid(row=3, column=1)



def render_register_screen(window):
    clear_window(window)
    tk.Label(window, text="Enter username: ").grid(row=0, column=0)
    username = tk.Entry(window)
    username.grid(row=0, column=1)

    tk.Label(window, text="Enter email: ").grid(row=1, column=0)
    email = tk.Entry(window)
    email.grid(row=1, column=1)

    tk.Label(window, text="Enter password: ").grid(row=2, column=0)
    password = tk.Entry(window, show="*")
    password.grid(row=2, column=1)

    tk.Label(window, text="Confirm password: ").grid(row=3, column=0)
    confirmed_password = tk.Entry(window, show="*")
    confirmed_password.grid(row=3, column=1)

    def on_register():
        username_value = username.get()
        email_value = email.get()
        password_value = password.get()
        confirmed_password_value = confirmed_password.get()

        if password_value != confirmed_password_value:
            tk.Label(window, text="password must match", fg="red").grid(row=4, column=1)
        else:
            result = register(username_value, email_value, password_value)
            if result:
                render_login_screen(window)
            else:
                tk.Label(window, text="Username is already taken.", fg="red").grid(row=4, column=1)



    tk.Button(
        window,
        text="Register",
        bg="yellow",
        fg="black",
        command=on_register
    ).grid(row=5, column=1)

if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("700x700")
    window.title("My GUI Shop")
    render_main_screen(window)
    window.mainloop()
