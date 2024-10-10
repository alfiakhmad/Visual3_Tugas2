import PySimpleGUI as sg
sg.theme("DarkTeal1")
sg.theme_text_color("#ffffff")
window = sg.Window(title="Profile", layout=[
    [sg.Text("SELAMAT DATANG DI KELAS", font=("Arial", 25, "italic", "bold", "underline"))],
    [sg.Text("NPM    : 2210010360")],
    [sg.Text("Nama   : Akhmad Alfi")],
    [sg.Text("Kelas  : 5P Reguler Pagi Banjarmasin")],
    [sg.Text("Matkul : Pemprograman Visual 3")]
    ],
    size=(510,200),
    font=("Times", 18)
)
window.read()
window.close()
