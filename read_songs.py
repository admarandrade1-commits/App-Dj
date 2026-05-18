import openpyxl

def read_songs_sequentially(filename="songs.xlsx"):
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    
    print("A ler músicas do Excel sequencialmente...\n")
    print(f"{'ID':<5} {'Título':<25} {'Artista':<20} {'BPM':<8} {'Energia'}")
    print("-" * 70)
    
    for row in ws.iter_rows(min_row=2, values_only=True):
        id, title, artist, bpm, energy = row
        print(f"{id:<5} {title:<25} {artist:<20} {bpm:<8} {energy}")
    
    print("\nLeitura concluída!")

read_songs_sequentially()
