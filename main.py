import CoolProp.CoolProp as CP
import numpy as np
import matplotlib as mpl

# Remarque Q = titre, donc si Q = 1 vapeur sat et si Q =0 liquide sat

# Préliminaires (non spécifique aux situations):
Débitcompresseur = 0.00005 * 60

# a)
TL = 21 + 273.15 # (fixé)
# TEMPÉRATURE EN KELVIN
def a(TH):
    # État 1:
    T1 = TH - 8
    h1 = CP.PropsSI('H', 'T', T1, 'Q', 1, 'R410A')
    s1 = CP.PropsSI('S', 'T', T1, 'Q', 1, 'R410A')
    D1 = CP.PropsSI('D', 'T', T1, 'Q', 1, 'R410A')
    P1 = CP.PropsSI('P', 'T', T1, 'Q', 1, 'R410A')
    m = Débitcompresseur * D1 # rép
    # État 3:
    T3 = TL + 20
    h3 = CP.PropsSI('H', 'T', T3, 'Q', 0, 'R410A')
    s3 = CP.PropsSI('S', 'T', T3, 'Q', 0, 'R410A')
    D3 = CP.PropsSI('D', 'T', T3, 'Q', 0, 'R410A')
    P3 = CP.PropsSI('P', 'T', T3, 'Q', 0, 'R410A')
    # État 2:
    s2 = s1
    P2 = P3
    h2s = CP.PropsSI('H', 'S', s2, 'P', P2, 'R410A')
    h2 = 0.85 * (h2s-h1) + h1
    # État 4
    P4 = P1
    s4 = s3
    h4 = CP.PropsSI('H', 'S', s4, 'P', P4, 'R410A')
    # QH
    QH = m * (h2 - h3) # rép
    # wcomp
    wcomp = h2 - h1 # rép
    # Wcomp
    Wcomp = m * (h2 - h1) # rép
    # COP
    COP = QH / Wcomp # rép
    return (m, QH, wcomp, Wcomp, COP)

mL = []
QHL = []
wL = []
WL = []
COPL = []
for Tc in range(-30, 16, 5):
    TH = Tc + 273.15
    print(TH, a(TH))
    res = a(TH)
    mL.append(res[0])
    QHL.append(res[1])
    wL.append(res[2])
    WL.append(res[3])
    COPL.append(res[4])

# Création de liste:
THL = [243.15, 248.15, 253.15, 258.15, 263.15, 268.15, 273.15, 278.15, 283.15, 288.15]

# = [0.022833708278694118, 0.02807341292378092, 0.034223124442314866, 
   # 0.04139863976231401, 0.04972887361342295,0.05935851898902331,
    #0.07045152403408475, 0.08319566738433593, 0.0978086434246237,
   # 0.11454627147055088]

mpl.figure()
mpl.plot()

