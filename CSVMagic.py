
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/sdeka/Desktop/ParticlePhysicsBaselineSpot.csv', low_memory=False)
print df.head()
print df.columns.tolist()  # it's a good idea to check the column names instead of writing what you see in the csv because you could be missing a leading space as in the case of ' CsInvocations'!!
# df.set_index("sample#")
df2 = df[['sample#', ' DRAMReads', ' DRAMWrites', 'gam_l3_tlb_hit', 'gam_l3_tlb_miss', ' SLM_Read', ' SLM_Write',' GPU_endSampleTime_nSec']]
df2.set_index('sample#')
# df2.plot()
# plt.show()
df3 = df2.loc[1:250:2, :]
print df3
df3.plot()
plt.show()

dfEU = df[['sample#', ' EU_STALL_PER_SUBSLICE', ' EU_NOT_IDLE_PER_SUBSLICE' ]]
dfEU.set_index('sample#')
# df2.plot()
# plt.show()
df4 = dfEU.loc[1:250:2, :]
print df4
df4.plot()
plt.show()
# print df.loc[5:10, "CsInvocations": "GTRequestsDRAM"]