
# ? https://www.engineeringtoolbox.com/specific-heat-capacity-water-d_660.html

from icecream import *
from math import log

U = 250

fluxo_o = .5
fluxo_a = .208
Cp_o = 2090

te_o = 375
te_a = 280
ts_o = 350

# * Ver temperatura da água
Cp_a = 4198 # | J/kg * K

C_o = fluxo_o * Cp_o
C_a = fluxo_a * Cp_a

ic(C_o)
ic(C_a)

if C_o > C_a:
  C_min = C_a
  C_max = C_o
else:
  C_min = C_o
  C_max = C_a

ic(C_min)
ic(C_max)

cMinSobrecMax = C_min/C_max

ic(cMinSobrecMax)

qmax = C_min * (te_o - te_a)

ic(qmax)

q = fluxo_o * Cp_o * (te_o - ts_o)

ic(q)

epsilon = q/qmax

ic(epsilon)

NUTContraCorrente = 1/((C_min/C_max) - 1) * log((epsilon - 1)/(epsilon * (C_min/C_max) - 1))

ic(NUTContraCorrente)

areaContraCorrente = (NUTContraCorrente * C_min)/U

ic(areaContraCorrente)