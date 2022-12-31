import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set_theme()
import matplotlib.pyplot as plt

def read_infrared_data(file):
    lines=open(file,"r",encoding='utf-8')
    data=[]
    for line in lines:
        vs=line.strip().split(",")
        row=[float(v) for v in vs]
        data.append(row)
    return data

data=read_infrared_data("data/sample_data.csv")

ax = sns.heatmap(data,
                 cbar=False, # remove legend
                 xticklabels=False, # remove the labels
                 yticklabels=False
                 )

plt.show()

