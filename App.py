from qiskit import QuantumCircuit
import numpy as np
import matplotlib.pyplot as plt
from qiskit.quantum_info import Statevector
from qiskit.primitives import StatevectorSampler, StatevectorEstimator
from qiskit.result import Counts, QuasiDistribution

if __name__ == "__main__":
    qc1 = QuantumCircuit(2)
    qc1.h(0)
    qc1.cx(0,1)
    state = Statevector(qc1)
    qc1.draw(output="mpl")
    #state.draw(output="bloch")
    plt.show()
    #qc1.measure_all()
    #sampler = StatevectorSampler()
    #pub = (qc1, None, 10)
    #job = sampler.run([pub])
    #result = job.result().quasi_dists[0]
    #print(result)

    #resul[0].data.meas <- risultati su bit classici