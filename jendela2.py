import PySimpleGUI as sg
window = sg.Window(title="Profile", layout=[
    [sg.Text("NPM    : 2210010360")],
    [sg.Text("Nama   : Akhmad Alfi")],
    [sg.Text("Kelas  : 5P Reguler Pagi Banjarmasin")],
    [sg.Text("Matkul : Pemprograman Visual 3")]
    ],
    size=(400, 200)
)
window.read()
window.close()
