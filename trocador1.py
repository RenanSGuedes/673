from icecream import *
from math import log

cp_o = 2090
cp_a = 4182
te_o = 375
ts_o = 350
fluxo_o = .5

te_a = 280
fluxo_a = .208
u = 250

q = fluxo_o * cp_o * (te_o - ts_o)

ts_a = (q)/(fluxo_a * cp_a) + te_a

deltaTlmContracorrente = ((te_o - ts_a) - (ts_o - te_a))/(log((te_o - ts_a)/(ts_o - te_a)))

areaFluxoContracorrente = q/(u * deltaTlmContracorrente)

ic(q)
ic(ts_a)
ic(deltaTlmContracorrente)
ic(areaFluxoContracorrente)

deltaTlmParalelo =  ((te_o - te_a) - (ts_o - ts_a))/(log((te_o - te_a)/(ts_o - ts_a)))

areaFluxoParalelo = q/(u * deltaTlmParalelo)

ic(areaFluxoParalelo)

