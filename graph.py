import pandas
import matplotlib.pyplot as plt
import numpy as np


def get_n_highestvalue(arr, n):
    np_arr = np.array(arr)
    sorted_arr = -np.sort(-np_arr)
    return sorted_arr[n]


colours = ["b", "r", "g", "k", "m"]
index_colours = 0               # To get different colours for the top 5
plt.rcParams['figure.figsize'] = [15, 8]

countries = open("countries.txt", 'r')
countries = countries.readlines()

myReader = pandas.read_csv("eurovision.csv")

threshold = get_n_highestvalue(myReader.iloc[-1], 5)
max_value = threshold
max_country = countries[0].replace('\n', '')

for i in countries:
    tmp = []
    for j in myReader[i.replace('\n', '')]:
        tmp.append(j)  # Youtube adds a no break space in its html

    # We only show a legend for the five most viewed videos
    # print(tmp[-1], ">", threshold, "?", tmp[-1] > threshold)
    if (tmp[-1] > threshold):
        if tmp[-1] > max_value:
            max_value = tmp[-1]
            max_country = i
        plt.plot(range(len(tmp)), tmp,
                 colours[index_colours], label=i.replace('\n', ''))
        index_colours += 1
    else:
        plt.plot(range(len(tmp)), tmp)

plt.legend(loc='upper left')
# plt.show()
plt.savefig("view.png", format="png")
done = open("done.txt", 'w')
done.write(max_country)
done.close()

plt.figure()

tmp = []
for i in countries:
    length = len(myReader[i.replace('\n', '')])
    views_now = myReader[i.replace('\n', '')][length-1]
    views_previous = myReader[i.replace('\n', '')][length-2]
    tmp.append((views_now - views_previous) / views_previous)

index_colours = 0

threshold = get_n_highestvalue(tmp, 5)
max_value = threshold
max_country = countries[0].replace('\n', '')

for i in countries:
    tmp = []
    arr = myReader[i.replace('\n', '')]
    for j in range(1, len(arr[1:]) + 1):
        tmp.append((arr[j] - arr[j-1]) / arr[j-1])

    # We only show a legend for the five most viewed videos
    # print(tmp[-1], ">", threshold, "?", tmp[-1] > threshold)
    if (tmp[-1] > threshold):
        print(tmp[-1], threshold)
        if tmp[-1] > max_value:
            max_value = tmp[-1]
            max_country = i
        plt.plot(range(len(tmp)), tmp,
                 colours[index_colours], label=i.replace('\n', ''))
        index_colours += 1
    else:
        plt.plot(range(len(tmp)), tmp)
plt.legend(loc='upper left')
# plt.show()
plt.savefig("rate.png", format="png")
done = open("done.txt", 'a')
done.write(max_country)
done.close()
