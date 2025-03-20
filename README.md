# Quantum Computing con Qiskit

## Installazione dei pacchetti necessari
```bash
pip install qiskit
pip install matplotlib
pip install pylatexenc
pip install numpy
```

## Parametrizzazione dei circuiti
Possiamo parametrizzare i circuiti quantistici utilizzando la classe `Parameter`.

Esempio:
```python
from qiskit.circuit import QuantumCircuit, Parameter

alpha = Parameter("alpha")
qc1 = QuantumCircuit(3)
qc1.rx(alpha, 2)  # Effettua una rotazione di alpha gradi intorno all'asse X
```

### Vettori di parametri
Possiamo creare vettori di parametri per raggrupparli:
```python
from qiskit.circuit import ParameterVector

beta = ParameterVector("beta", 3)  # Il parametro beta è un vettore che contiene 3 parametri
qc1.rx(beta[0], 2)
qc1.rx(beta[1], 2)
qc1.rx(beta[2], 2)
```

Oppure possiamo assegnare più valori con un unico comando:
```python
import numpy as np
qc1.assign_parameters({alpha: 0.0, beta: [np.pi, np.pi, np.pi]})
```

## Composizione di circuiti quantistici
Se abbiamo più circuiti quantistici possiamo "comporli":
```python
qc1.compose(qc2)  # Funziona solo se i circuiti hanno lo stesso numero di qbit
```

Se `qc2` ha 3 qbit e `qc1` ne ha 2:
```python
qc1.compose(qc2[0,1])
qc1.compose(qc2[0,1]).compose(qc2[1,2])
```

## Decomposizione dei circuiti
Possiamo decomporre un circuito in operazioni più semplici:
```python
qc3 = qc1.decompose(reps=1)
```

## Misurazione dello stato
Per misurare lo stato utilizziamo il comando:
```python
qc1.measure_all()  # Crea automaticamente un registro di bit classici della dimensione corretta
```

## Visualizzazione dello stato quantistico
Possiamo visualizzare lo stato di un circuito utilizzando la funzione `Statevector`:
```python
from qiskit.quantum_info import Statevector

state = Statevector(qc1)
print(state)
print(state.probabilities())
print(state.dict())
```

### Nota Bene
Nella notazione `statevector` (rappresentazione stringa) di Qiskit, il bit più in alto nel circuito è quello meno significativo nella stringa binaria. Se utilizziamo invece una rappresentazione a lista, il primo bit è quello più a destra.

## Disegno dello stato quantistico
Possiamo rappresentare lo stato quantistico sulla **sfera di Bloch**. Altri modi per visualizzare lo stato sono:
- `hinton`
- `city`

## Primitive in Qiskit per il sampling e la stima
Esistono delle primitive in Qiskit per effettuare campionamento e stime:
```python
from qiskit.primitives import BaseSamplerV2, BaseEstimatorV2  # Primitive base
from qiskit.primitives import StatevectorSampler, StatevectorEstimator  # Implementazioni specifiche
```
### Nota Bene
Esistono diverse implementazioni di `Sampler` e `Estimator`. Alcune funzionano meglio su GPU, altre su CPU.

## Eseguire un campionamento di un circuito
Quando vogliamo effettuare un sample di un circuito, dobbiamo creare una tupla con:
- **Circuito**
- **Eventuali valori dei parametri**
- **Numero di shots**

Quando si esegue il sampling, si passa un vettore di tuple (poiché lavora in parallelo). Se un parametro non è necessario (ad esempio, i parametri del circuito), bisogna passare il valore `None`.

## Strutture dati per la memorizzazione dei risultati
Dopo aver effettuato un sampling, possiamo utilizzare queste strutture per memorizzare i risultati:
```python
from qiskit.result import Counts, QuasiDistribution
```

## Definizione di osservabili con un sampler
Esempio su 3 qbit:
```python
from qiskit.opflow import SparsePauliOp

op1 = SparsePauliOp.from_list([
    ("IIZ", 1),
    ("IZI", -1),
    ("ZII", 1)
])
```
Le stringhe rappresentano l'operatore di Pauli di base utilizzato:
- `I` = Identità
- `Z` = Sigma
- Il secondo valore è il peso associato all'osservabile.

