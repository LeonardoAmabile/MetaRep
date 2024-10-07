import argparse  # Per gestire gli argomenti della riga di comando
import string  # Per accedere alle lettere dell'alfabeto
import matplotlib.pyplot as plt  # Per creare il grafico a barre
import time  # Per avere info riguardo il tempo di esecuzione
from loguru import logger  # Per gestire i log del programma

# Funzione che conta i caratteri e opzionalmente fa altre cose
def count_characters(file_path, plot_histogram, return_info, line_slice=None):
    start_time = time.time()

    # Inizializza un dizionario con tutte le lettere minuscole dell'alfabeto
    counts = {char: 0 for char in string.ascii_lowercase}

    # Apertura del file indicato
    with open(file_path) as input_file:
        # Leggi tutte le righe in una lista
        lines = input_file.readlines()

        # Se line_slice è fornito, seleziona solo le righe specificate
        if line_slice:
            start, end = line_slice
            lines = lines[start:end]  # Slicing delle righe

    # Conta delle occorrdisegna un istogrammaenze di ogni lettera
    words_number = 0
    for line in lines:  # Itera su ogni riga
        words_number += len(line.split())  # Conta le parole nella riga
        for char in line.lower():  # Converte tutti i caratteri in minuscolo per la coerenza
            if char in counts:  # Incrementa solo se il carattere è una lettera
                counts[char] += 1

    # Calcolo del numero totale di caratteri rilevanti (solo lettere)
    num_characters = sum(counts.values())
    lines_number = len(lines)  # Ottieni il numero totale di righe

    # Calcola la frequenza percentuale di ogni carattere
    for key, value in counts.items():
        counts[key] = value / num_characters if num_characters > 0 else 0

    # Se richiesto, disegna un grafico a barre
    if plot_histogram:
        # Estrazione delle lettere e delle rispettive frequenze
        letters = list(counts.keys())
        values = list(counts.values())

        # Creazione del grafico a barre
        plt.bar(letters, values)
        plt.title('Frequency of characters')
        plt.xlabel('Characters')
        plt.ylabel('Frequency')
        plt.show()

    # Se richiesto, stampa le info del libro
    if return_info:
        print(f'The number of characters is: {num_characters}')
        print(f'The number of words is: {words_number}')
        print(f'The number of lines is: {lines_number}')

    end_time = time.time()
    execution_time = end_time - start_time
    print(f'Execution time: {execution_time*1000:.1f} ms')


# Punto di ingresso dello script
if __name__ == '__main__':
    # Definizione di un parser per gestire gli argomenti da riga di comando
    parser = argparse.ArgumentParser(description='Count the characters in a text file')

    # Argomento obbligatorio: il file da analizzare
    parser.add_argument('file')

    # Argomento opzionale: se indicato, crea un istogramma delle frequenze
    parser.add_argument('--histogram', action='store_true',
                        help='plot a histogram of the character frequencies')
    parser.add_argument('--info', action='store_true',
                        help='return infos about the file')

    # Questo comando analizza gli argomenti passati alla riga di comando quando lo script viene eseguito, 
    # e li memorizza nell'oggetto args
    args = parser.parse_args()

    # Leggi l'intero file per la prima volta
    with open(args.file) as f:
        full_lines = f.readlines()

# Loop principale per gestire le richieste
while True:

    use_full_file = input("Do you want to use the entire file? (y/n): ")
    if use_full_file.lower() == 'y':
        count_characters(args.file, args.histogram, args.info)
    elif use_full_file.lower() == 'n': 
        start = int(input("From which line do you want to start? "))
        end = int(input("Until which line do you want to end? "))
        count_characters(args.file, args.histogram, args.info, line_slice=(start, end))
    else:
        print('Not a valid answer')        
    break # Continua il ciclo per ripetere la domanda



