# fly_straight_sequence.py
# Andrew Lounsbury
# 23/3/23
# Purpose: generate the fly-straight sequence; https://www.youtube.com/watch?v=pAMgUB51XZA&t=95s

import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_fly_straight(m):
    sequence = [1, 1]
    n = 2
    while len(sequence) < m:
        if math.gcd(n, sequence[len(sequence) - 1]) == 1:
            sequence.append(sequence[len(sequence) - 1] + n + 1)
        else:
            sequence.append(
                int(sequence[len(sequence) - 1] / math.gcd(n, sequence[len(sequence) - 1]))
            )
        n += 1
    return sequence

sequence = generate_fly_straight(20)
print(sequence)

# Basic scatterplots
m = 10
sequence = generate_fly_straight(m)
df = pd.DataFrame(sequence, columns=["Number"])

indices = []
for i in range(m):
    indices.append(i)
df["index"] = indices

sns.scatterplot(x="index", y="Number", data=df)
plt.show()

m = 100
sequence = generate_fly_straight(m)
df = pd.DataFrame(sequence, columns=["Number"])

indices = []
for i in range(m):
    indices.append(i)
df["index"] = indices

sns.scatterplot(x="index", y="Number", data=df)
plt.show()

m = 1000
sequence = generate_fly_straight(m)
df = pd.DataFrame(sequence, columns=["Number"])

indices = []
for i in range(m):
    indices.append(i)
df["index"] = indices

sns.scatterplot(x="index", y="Number", data=df)
plt.show()

# Scatterplots of the average
m = 10
sequence = generate_fly_straight(m)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)
    
df = pd.DataFrame(average_sequence, columns=["Average"])

indices = []
for i in range(m):
    indices.append(i)
df["index"] = indices

sns.scatterplot(x="index", y="Average", data=df)
plt.show()

m = 100
sequence = generate_fly_straight(m)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)
    
df = pd.DataFrame(average_sequence, columns=["Average"])

indices = []
for i in range(m):
    indices.append(i)
df["index"] = indices

sns.scatterplot(x="index", y="Average", data=df)
plt.show()

m = 1000
sequence = generate_fly_straight(m)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)
    
df = pd.DataFrame(average_sequence, columns=["Average"])

indices = []
for i in range(m):
    indices.append(i)
df["index"] = indices

sns.scatterplot(x="index", y="Average", data=df)
plt.show()

m = 10000
sequence = generate_fly_straight(m)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)
    
df = pd.DataFrame(average_sequence, columns=["Average"])

indices = []
for i in range(m):
    indices.append(i)
df["index"] = indices

sns.scatterplot(x="index", y="Average", data=df)
plt.show()

m = 100000
sequence = generate_fly_straight(m)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)
    
df = pd.DataFrame(average_sequence, columns=["Average"])

indices = []
for i in range(m):
    indices.append(i)
df["index"] = indices

sns.scatterplot(x="index", y="Average", data=df)
plt.show()