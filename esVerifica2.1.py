import random

def spostamentoCasuale(lista):
    return random.choice(lista)

def tempoTotale(giorni):
    return 60*60*24*giorni

def sommaTotale(lista):
    somma = 0
    for i in lista:
        somma += i
    return somma 
    
def main():
    numeriCasuali = -1,1
    listaCasuale = [spostamentoCasuale(numeriCasuali) for _ in range(0, tempoTotale(5))]
    print(sommaTotale(listaCasuale))

if __name__ == "__main__":
    main()