#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy
import pandas

list_types = ("random", "sorted", "reverse_sorted", "unique", "similar")
# list_types = ("random",)
algorithms = ("heapsort", "radixsort")

plt.style.use('seaborn-v0_8-paper')
for algorithm in algorithms:
    file = f"./log/result_{algorithm}_100x1000000_noinput.csv"
    data = pandas.read_csv(file, sep=";")
    for list_type in list_types:
        times = numpy.array(data.loc[data["List type"] == list_type]["Time"])
        fig, ax = plt.subplots(1, 1)

        ax.hist(times, bins=100)
        ax.set_xlabel("Tijd (s)")
        ax.set_ylabel("Aantal voorvallen")
        ax.set_title(f"{algorithm.capitalize()} - {list_type}")

        # ax.set_xlim(4, 6)
        
        ax.set_ylim(0, 20)
        if algorithm == "radixsort" and list_type == "unique":
            ax.set_ylim(0, 50)
        ax.set_yticks(range(0, int(ax.get_ylim()[1]) + 1, 5))

        # print(plt.style.available)
        plt.savefig(f"./log/figuur_{algorithm}_{list_type}.svg")
