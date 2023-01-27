import seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from numpy import *


kashti = sns.load_dataset("titanic")
# print(kashti)
## Numerical values are placed mostly on x-axis, Categorial values mostly placed of y-axis or hue.

                            # LinePlot
# sns.barplot(x="sex", y="alone",hue='who', data=kashti, order=["female","male"])
# plt.show()


# sns.barplot(x="sex", y="alone",hue='who', data=kashti, order=["female","male"], ci=None)
# plt.show()

# sns.barplot(x="class", y="fare",hue='sex', data=kashti, estimator=median)
# plt.show()

                            # Horizontal Line Plot
# sns.barplot(x="fare", y="class",hue='sex', data=kashti, estimator=median)
# plt.show()

# sns.barplot(x='class',y='fare',data=kashti,
#             linewidth=5, facecolor=(1,1,1,0),errcolor=".2",edgecolor=".2")
# plt.show()


                            # BoxPlot

# canvas (Baloon Board) : Used for background
# seaborn.set(style='whitegrid')
#
# seaborn.boxplot(x='class',y='fare',data=kashti)
# plt.show()

tip = sns.load_dataset('tips')
# print(tip)

# sns.boxplot(x='sex',y='tip',data=tip)
# plt.show()

# sns.boxplot(x='day',y='tip',data=tip)
# plt.show()

# print(tip.describe())

# sns.boxplot(x=tip['total_bill'])
# plt.show()

# sns.boxplot(y=tip['total_bill'])
# plt.show()

# sns.boxplot(x='tip',y='day',hue='smoker' , data=tip, palette='Set2')
# plt.show()

# sns.boxplot(x='tip',y='day',hue='smoker' , data=tip, palette='Set2',dodge=False)
# plt.show()
# sns.boxplot(x='tip',y='day',hue='smoker' , data=tip, palette='Set2',dodge=True)
# plt.show()

# sns.boxplot(x='survived',y='age',showmeans=True,meanprops={"marker":"+",
#                                                             "markersize":"12",
#                                                             "markeredgecolor":"red"},
#             data=kashti)
# plt.xlabel("How many Survived", size=14),
# plt.ylabel( "Age (Years)", size=12),
# plt.title("Box Plot Doobay and bachay kitnay",size=16)
# plt.show()

## Question:
## what is facet wrap and facet grip and use it on dataset.

# ......Solution
# nuqta = sns.load_dataset('dots')
# sns.set_theme(style='ticks')
# pallete = sns.color_palette('rocket_r')
# sns.relplot(data=nuqta,x='time', y='firing_rate', hue='coherence', size='choice', col="align", kind='line',
#             size_order=['T1','T2'], palette=pallete,height=5,aspect=.75,facet_kws=dict(sharex=False),)
# plt.show()
