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


1. O que aconteceu ao executar o código com Lock?
O estoque foi atualizado corretamente, e apenas 5 dos 8 clientes conseguiram comprar, sem deixar o estoque negativo.
    
2. O que mudou ao retirar o Lock?
Sem o Lock, vários clientes podem acessar e modificar o estoque ao mesmo tempo, causando inconsistências nos resultados.
    
3. Mais clientes conseguiram encontrar a mesma quantidade disponível?
Sim, sem a proteção, vários clientes podem ler a mesma quantidade antes de ela ser atualizada, gerando uma condição de corrida.

4. Por que uma loja virtual não pode deixar todas as requisições alterarem o estoque sem coordenação?
Porque vários clientes poderiam comprar a mesma unidade, causando vendas acima do estoque disponível e inconsistências no sistema.
    
5. Se os processos estiverem em máquinas diferentes, como saber quem pode acessar um recurso primeiro?
É necessário utilizar mecanismos de coordenação distribuída, como locks distribuídos, transações ou filas, para controlar o acesso ao recurso compartilhado.
