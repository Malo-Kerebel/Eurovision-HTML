import pandas
import matplotlib.pyplot as plt
import numpy as np


def get_n_highestvalue(arr, n):
    sorted_arr = -np.sort(-arr)
    return sorted_arr[n]


colours = ["b", "r", "g", "k", "m"]
index_colours = 0               # To get different colours for the top 5
plt.rcParams['figure.figsize'] = [15, 8]
countries = open("countries.txt", 'r')

myReader = pandas.read_csv("eurovision.csv")

threshold = get_n_highestvalue(myReader.iloc[-1], 5)

for i in countries:
    tmp = []
    for j in myReader[i.replace('\n', '')]:
        tmp.append(j)  # Youtube adds a no break space in its html

    # We only show a legend for the five most viewed videos
    # print(tmp[-1], ">", threshold, "?", tmp[-1] > threshold)
    if (tmp[-1] > threshold):
        plt.plot(range(len(tmp)), tmp, colours[index_colours], label=i.replace('\n', ''))
        index_colours += 1
    else:
        plt.plot(range(len(tmp)), tmp)
plt.legend(loc='upper left')
# plt.show()
plt.savefig("view.png", format="png")
