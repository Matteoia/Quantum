from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from qiskit.quantum_info import SparsePauliOp
from qiskit_aer.primitives import Estimator

#Lo stato di Greenberger-Horne-Zeilinger è una "generalizzazione" degli stati di Bell
#In questo caso creo un circuito quantistico nella quale metto in entaglement n qbit
def get_qc_GHZ_state(n):
    qc = QuantumCircuit(n)
    qc.h(0)
    for i in range(n-1):
        qc.cx(i, i+1)
    return qc

if __name__ == "__main__":
    n = 10
    qc = get_qc_GHZ_state(n)
 
    #Creo una serie di osservabili
    #In particolare voglio vedere come aumenta il rumore tra qbit lontani andando ad osservare
    #il valore atteso, procedo quindi andando a "misurare" il primo e il secondo, poi il primo
    #e il terzo, poi il primo e il quarto e così via...
    operators_strings = ['Z' + 'I' * i + 'Z' + 'I' * (n-2-i) for i in range(n-1)]
    #Ora creo i veri e proprio operatori utilizzando le stringhe appena create
    operators = [SparsePauliOp(operator_string) for operator_string in operators_strings]
    #Mi aspetto che il rumore tra il primo qbit e il secondo sia piccolo mentre quello tra
    #il primo qbit e l'ultimo sia grande

    #Utilizzo per questo esempio l'Estimator nella versione 1
    estimator = Estimator()
    #Per ogni osservabile passo un circuito, in questo modo ogni osservabile
    #effettuerà un operazione su un circuito diverso
    job = estimator.run([qc]*len(operators), operators)
    values = job.result().values  

    #Effettuo il plotting
    plt.plot(operators_strings, values, "-o")
    plt.xlabel("Osservabile")
    plt.ylabel("Valore Atteso")
    plt.show()
    #Poichè sto effettuando una simulazione i valori attesi sono tutti uguali
    #al valore ideale