import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Músicas"

ws.append(["id", "title", "artist", "bpm", "energy"])

songs = [
    [1, "Strobe", "deadmau5", 128, 0.6],
    [2, "Around The World", "Daft Punk", 121, 0.8],
    [3, "One More Time", "Daft Punk", 123, 0.9],
    [4, "Levels", "Avicii", 126, 0.7],
    [5, "Blue (Da Ba Dee)", "Eiffel 65", 136, 0.85],
    [6, "Sandstorm", "Darude", 136, 0.92],
    [7, "Children", "Robert Miles", 132, 0.75],
    [8, "Insomnia", "Faithless", 128, 0.78],
    [9, "Flat Beat", "Mr. Oizo", 124, 0.65],
    [10, "Da Funk", "Daft Punk", 120, 0.72],
]

for song in songs:
    ws.append(song)

wb.save("songs.xlsx")
print("Ficheiro songs.xlsx criado com sucesso!")
