import threading
import time

saldo = 1000

def sacar(valor):
    global saldo

    saldo_atual = saldo
    time.sleep(0.01)
    saldo = saldo_atual - valor

threads = []

for i in range(10):
    t = threading.Thread(target=sacar, args=(50,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

print("Saldo esperado: 500")
print("Saldo obtido:", saldo)

python corrida.py

# Se python não funcionar no Windows:
py corrida.py

# Execute novamente:
python corrida.py
python corrida.py
python corrida.py

import threading
import time

saldo = 1000
lock = threading.Lock()

def sacar(valor):
    global saldo

    with lock:
        saldo_atual = saldo
        time.sleep(0.01)
        saldo = saldo_atual - valor

threads = []


print("Saldo esperado: 500")
print("Saldo obtido:", saldo)
for i in range(10):
    t = threading.Thread(target=sacar, args=(50,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
import threading
import time

estoque = 5
lock = threading.Lock()

def comprar(cliente):
    global estoque

    with lock:
        if estoque > 0:
            print(cliente, "encontrou", estoque, "unidade(s)")
            time.sleep(0.5)
            estoque -= 1
            print(cliente, "comprou. Restam:", estoque)
        else:
            print(cliente, "não conseguiu comprar: estoque esgotado")
clientes = []

for i in range(1, 9):
    t = threading.Thread(target=comprar, args=(f"Cliente {i}",))
    clientes.append(t)
    t.start()

for t in clientes:
    t.join()

print("Estoque final:", estoque)


1. Execute o estoque com Lock e registre o resultado.

print("Estoque final:", estoque)

Cliente 1 encontrou 5 unidade(s)
Cliente 1 comprou. Restam: 4
Cliente 2 encontrou 4 unidade(s)
Cliente 2 comprou. Restam: 3
Cliente 3 encontrou 3 unidade(s)
Cliente 3 comprou. Restam: 2
Cliente 4 encontrou 2 unidade(s)
Cliente 4 comprou. Restam: 1
Cliente 5 encontrou 1 unidade(s)
Cliente 5 comprou. Restam: 0
Cliente 6 não conseguiu comprar: estoque esgotado
Cliente 7 não conseguiu comprar: estoque esgotado
Cliente 8 não conseguiu comprar: estoque esgotado
Estoque final: 0

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

2. Retire temporariamente a proteção e ajuste a indentação do bloco.

PS C:\Users\aluno\AppData\Local\Programs\Microsoft VS Code> & "C:\Program Files\Python313\python.exe" c:/Users/aluno/Desktop/corrida.py
Saldo esperado: 500
Saldo obtido: 950
Saldo esperado: 500
Saldo obtido: 1000
Saldo esperado: 500
Saldo obtido: 950
PS C:\Users\aluno\AppData\Local\Programs\Microsoft VS Code>

3. Execute novamente algumas vezes.

PS C:\Users\aluno\AppData\Local\Programs\Microsoft VS Code> & "C:\Program Files\Python313\python.exe" c:/Users/aluno/Desktop/corrida.py
Saldo esperado: 500
Saldo obtido: 950
Saldo esperado: 500
Saldo obtido: 1000
Saldo esperado: 500
Saldo obtido: 950
PS C:\Users\aluno\AppData\Local\Programs\Microsoft VS Code> & "C:\Program Files\Python313\python.exe" c:/Users/aluno/Desktop/corrida.py
Saldo esperado: 500
Saldo obtido: 950
Saldo esperado: 500
Saldo obtido: 1000
Saldo esperado: 500
Saldo obtido: 950
PS C:\Users\aluno\AppData\Local\Programs\Microsoft VS Code> & "C:\Program Files\Python313\python.exe" c:/Users/aluno/Desktop/corrida.py
Saldo esperado: 500
Saldo obtido: 950
Saldo esperado: 500
Saldo obtido: 1000
Saldo esperado: 500
Saldo obtido: 950
PS C:\Users\aluno\AppData\Local\Programs\Microsoft VS Code> & "C:\Program Files\Python313\python.exe" c:/Users/aluno/Desktop/corrida.py
Saldo esperado: 500
Saldo obtido: 950
Saldo esperado: 500
Saldo obtido: 1000
Saldo esperado: 500
Saldo obtido: 950
PS C:\Users\aluno\AppData\Local\Programs\Microsoft VS Code> & "C:\Program Files\Python313\python.exe" c:/Users/aluno/Desktop/corrida.py
Saldo esperado: 500
Saldo obtido: 950
Saldo esperado: 500
Saldo obtido: 1000
Saldo esperado: 500
Saldo obtido: 950
PS C:\Users\aluno\AppData\Local\Programs\Microsoft VS Code>

4. O estoque final ficou coerente?

Não, O estoque final pode não ficar coerente com o esperado, devido à condição de corrida.
Conclusão: sem o Lock, diferentes threads podem ler o mesmo valor e sobrescrever as atualizações umas das outras. Portanto, o saldo final pode não representar corretamente todos os saques realizados.



5. Mais clientes conseguiram 'encontrar' a mesma quantidade disponível?
Sim, Mais de um cliente (thread) conseguiu “encontrar” a mesma quantidade disponível ao mesmo tempo.


6. Explique por que uma loja virtual não pode simplesmente deixar todas as requisições alterarem o estoque sem coordenação.
Uma loja virtual não pode deixar todas as requisições alterarem o estoque sem coordenação porque isso pode causar condições de corrida (race conditions), levando a inconsistências na quantidade de produtos disponíveis.
