import pandas as pd
import matplotlib.pyplot as plt
import glob
import sys

sys.path.insert(0, "../data")

for filename in glob.iglob("../data/Roofline_Model.csv", recursive = True):
    dataframe = pd.read_csv(filename)
    
    x = dataframe["FLOPS/Input Byte over DDR"]
    y = dataframe["Achievable CH TFLOPS/sec"]
    
    fig, ax = plt.subplots()
    ax.plot(x.head(8), y.head(8), '^k:', label='CH Roofline')
    ax.set(xlabel='Operational Intensity (Ops/Byte)', ylabel='Throughput (TFLOPS)')
    ax.legend(loc='best')
    
    estimated_perf = {'op_intensity': 10000, 'TFLOPS': 130}
    ax.plot(estimated_perf['op_intensity'], estimated_perf['TFLOPS'], 'gx', label='Estimated (from MA)')
    ax.legend(loc='best')
    ax.grid()
    
    ax.plot(5000, 50, 'rx', label='Measured (from CH run)')
    ax.legend(loc='best')
    

    fig.savefig("../data/roofline.png")
    plt.show()