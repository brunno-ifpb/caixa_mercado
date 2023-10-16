"""

from datetime import date

# Obtém a data atual
data_atual = date.today().strftime('%Y-%m-%d')

# Imprime a data atual no formato AAAA-MM-DD
print(data_atual)"""

if __name__ == '__main__':
    names = []
    escores = []
    for _ in range(int(input())):
        names.append(input())
        escores.append(float(input()))
        
    
    a = escores.copy()
    a.remove(min(escores))
    segunda_menor = min(a)
    
    menores = []
    
    [menores.append(names[i]) for i in range(len(names)) if escores[i] == segunda_menor]
    print('\n'.join(sorted(menores)))