import CoolProp.CoolProp as CP

# Remarque Q = titre, donc si Q = 1 vapeur sat et si Q =0 liquide sat

# Préliminaires (non spécifique aux situations):
Débitcompresseur = 0.00005 * 60

# a)
TL = 21 + 273.15 # (fixé)
# TEMPÉRATURE EN KELVIN
def a(TH):
    # État 1:
    T1 = TH - (8 + 273.15)
    h1 = CP.PropsSI('H', 'T', T1, 'Q', 1, 'R410A')
    s1 = CP.PropsSI('S', 'T', T1, 'Q', 1, 'R410A')
    D1 = CP.PropsSI('D', 'T', T1, 'Q', 1, 'R410A')
    P1 = CP.PropsSI('P', 'T', T1, 'Q', 1, 'R410A')
    m = Débitcompresseur * D1 # rép
    # État 3:
    T3 = TL + (20 + 273.15)
    h3 = CP.PropsSI('H', 'T', T3, 'Q', 0, 'R410A')
    s3 = CP.PropsSI('S', 'T', T3, 'Q', 0, 'R410A')
    D3 = CP.PropsSI('D', 'T', T3, 'Q', 0, 'R410A')
    P3 = CP.PropsSI('P', 'T', T3, 'Q', 0, 'R410A')
    # État 2:
    s2 = s1
    P2 = P3
    h2s = CP.PropsSI('H', 'S', s2, 'P', P2, 'R410A')
    h2 = 0.85(h2s-h1) + h1
    # État 4
    P4 = P1
    s4 = s3
    h4 = CP.PropsSI('H', 'S', s2, 'P', P2, 'R410A')
    # QH
    QH = m * (h3 - h2) # rép
    # wcomp
    wcomp = h2 - h1 # rép
    # Wcomp
    Wcomp = m(h2 - h1) # rép
    # COP
    COP = QH / Wcomp # rép
    return (m, QH, wcomp, Wcomp, COP)





