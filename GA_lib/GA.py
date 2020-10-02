import math
import numpy as np
import matplotlib.pyplot as plt

def distancia_ponto_linha(Lponto1, Lponto2, ponto, plot=False):
    P1_P3 = vetor(Lponto1, ponto)
    P1_P2 = vetor(Lponto1, Lponto2)
        
    u = produto_escalar(P1_P3, P1_P2)/(modulo(P1_P2)**2)
    
    new_P = []
    
    for i_comp in range(len(ponto)):
        new_P.append(Lponto1[i_comp]+(u*(P1_P2[i_comp])))

    if(plot==True and len(Lponto1)==3):
        lineX = [Lponto1[0], Lponto2[0]]
        lineY = [Lponto1[1], Lponto2[1]]
        lineZ = [Lponto1[2], Lponto2[2]]

        fig = plt.figure()
        sub = fig.add_subplot(1, 1, 1, projection="3d")
        sub.plot(lineX, lineY, lineZ, '-')
        sub.plot(ponto[0], ponto[1], ponto[2], 'o', label="Distância:%.3f"%(modulo(vetor(new_P, ponto))))
        plt.legend(loc="upper right")
        plt.show()
        plt.clf()

    return modulo(vetor(new_P, ponto))

def produto_vetorial(vetor1, vetor2):
    return list(np.cross(vetor1, vetor2))

def produto_escalar(vetor1, vetor2):
    sum = 0
    for i, j in zip(vetor1, vetor2):
        sum += i*j
    return sum

def vetor(ponto1, ponto2):
    vector = []
    for i_comp in range(len(ponto1)):
        vector.append(ponto2[i_comp]-ponto1[i_comp])
    return vector

def modulo(vetor):
    sum = 0
    for component in vetor:
        sum += component**2
    return math.sqrt(sum)

def distancia_ponto_plano(vetor1, vetor2, ponto_plano, ponto, plot=False):
    n = produto_vetorial(vetor1, vetor2)
    D = 0
    for i, j in zip(n, ponto_plano):
        D += i*j
    sum = -D
    for i, j in zip(n, ponto):
        sum += i*j

    if(plot==True and len(vetor1)==3):
        x = np.linspace(2*np.min(ponto), 2*np.max(ponto), 10)
        y = np.linspace(2*np.min(ponto), 2*np.max(ponto), 10)

        X, Y = np.meshgrid(x, y)
        Z = ponto_plano[0] * X + ponto_plano[1] * Y + ponto_plano[2]

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        surf = ax.plot_surface(X, Y, Z)

        ax.plot(ponto[0], ponto[1], ponto[2], "o", label="Dist: %.3f" % abs(sum)/modulo(n))
        plt.legend(loc="upper right")
        plt.show()
        plt.clf()

    return abs(sum)/modulo(n)

def angulo_entre_vetores(vetor1, vetor2):
    v = abs(produto_escalar(vetor1, vetor2)/ (modulo(vetor1)*modulo(vetor2)))
    return math.degrees(math.acos(v))

def distancia_entre_planos(A, B, C, D1, D2):
    plane = [A, B, C]

    return abs(D2-D1)/modulo(plane)

