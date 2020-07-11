from threading import Thread
import random
import sys

valido = True
while (valido):
    sequential_total = 0
    threaded_total = 0
    threads = []
    vector = []
    somaTotal = 0
    threadTotal = 0

    numElementos = eval(input('Entre com o numero de elementos do vetor: '))
    if (numElementos == 0):
        valido = False
    numThreads = eval(input('Entre com o numero de threads: ')) 

    class Th(Thread):
        acc = 0

        def __init__(self,threadID):
            sys.stdout.write('Iniciando thread %d...\n' % (threadID+1))
            sys.stdout.flush()
            Thread.__init__(self)
            self.threadID = threadID

        def run(self):
            inicioIntervalo = int(self.threadID * numElementos / numThreads)
            fimIntervalo = int(((self.threadID + 1) * numElementos / numThreads) - 1)

            for i in range(inicioIntervalo, fimIntervalo):
                self.acc += vector[i]

            sys.stdout.flush()

        def get_acc(self):
            return self.acc

    for i in range(numElementos):
        vector.append(random.randint(-50,50))
        somaTotal += vector[i]

    for threadID in range(numThreads):
        threads.insert(threadID, Th(threadID))
        threads[threadID].start()
        threads[threadID].join()
        threadTotal += threads[threadID].get_acc()

    print('Soma total: %d\n' % threadTotal)
