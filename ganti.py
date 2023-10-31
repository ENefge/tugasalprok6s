import tkinter as tk
from tkinter import ttk, messagebox

# Fungsi untuk menampilkan beranda setelah login berhasil
def show_home():
    def save_tabungan():
        try:
            jumlah = float(entry_tabungan.get())
            with open("tabungan.txt", "w") as file:
                file.write(str(jumlah))
            lbl_tabungan.config(text=f"Tabungan saat ini: {jumlah}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Masukkan jumlah tabungan yang valid.")

    def show_riwayat_pengeluaran():
        riwayat_window = tk.Toplevel(home_window)
        riwayat_window.title("Riwayat Pengeluaran")
        with open("pengeluaran.txt", "r") as file:
            for line in file:
                tk.Label(riwayat_window, text=line.strip()).pack()

    home_window = tk.Tk()
    home_window.title("Beranda Aplikasi Keuangan")

    tab_control = ttk.Notebook(home_window)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Tabungan')
    tab_control.add(tab2, text='Riwayat Pengeluaran')

    # Tab Tabungan
    tk.Label(tab1, text="Masukkan Jumlah Tabungan:").pack(pady=10)
    entry_tabungan = tk.Entry(tab1)
    entry_tabungan.pack(pady=10)
    tk.Button(tab1, text="Simpan", command=save_tabungan).pack(pady=10)

    with open("tabungan.txt", "r") as file:
        tabungan = file.readline()
    lbl_tabungan = tk.Label(tab1, text=f"Tabungan saat ini: {tabungan}")
    lbl_tabungan.pack(pady=10)

    # Tab Riwayat Pengeluaran
    tk.Button(tab2, text="Lihat Riwayat Pengeluaran", command=show_riwayat_pengeluaran).pack(pady=20)

    tab_control.pack(expand=1, fill='both')
    home_window.mainloop()

# Fungsi untuk menghandle login
def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    with open("users.txt", "r") as file:
        users = file.readlines()
        for user in users:
            uname, pwd = user.strip().split(",")
            if uname == username and pwd == password:
                login_window.destroy()
                show_home()
                return
    messagebox.showerror("Login Failed", "Username atau Password salah")

login_window = tk.Tk()
login_window.title("Login Aplikasi Keuangan")

tk.Label(login_window, text="Username:").pack(pady=10)
username_entry = tk.Entry(login_window)
username_entry.pack(pady=10)

tk.Label(login_window, text="Password:").pack(pady=10)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack(pady=10)

tk.Button(login_window, text="Login", command=handle_login).pack(pady=20)

login_window.mainloop()
