import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data import Data

d = Data()

# All 
d.plot("children")

# Gender 
d.plot("gender")

# Prim/sec school
d.plot("school")

# Gender and prim/sec school
d.plot("school_gender")

# How many diseases
demo_df = d.df
folder = d.folder_save

plt.close()
sum_diseases = demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","Eat","Sleep","Anger","Behaviour","Emotions","Not School"]).sum(axis=1)
max_value = sum_diseases.max()
min_value = sum_diseases.min()

# print("Number of diseases per child")
# print(sum_diseases)

plt.hist(sum_diseases, bins=range(min_value, max_value + 2), rwidth=0.8, align='left')
plt.title("Number of diseases per child")
plt.savefig(f"{folder}/nb_diseases")

# How many problems

plt.close()
sum_problems = demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","ADHD","Self-harm","Anxiety","Depression","Repetitive"]).sum(axis=1)
max_value = sum_problems.max()
min_value = sum_problems.min()

# print("Number of problems per child")
# print(sum_problems)

plt.hist(sum_problems, bins=range(min_value, max_value + 2), rwidth=0.8, align='left')
plt.title("Number of problems per child")
plt.savefig(f"{folder}/nb_problems")

# Problems per disease

adhd_demo_df=demo_df[(demo_df["ADHD"]==1)]
selfharm_demo_df=demo_df[(demo_df["Self-harm"]==1)]
anxiety_demo_df=demo_df[(demo_df["Anxiety"]==1)]
depression_demo_df=demo_df[(demo_df["Depression"]==1)]
repetitive_demo_df=demo_df[(demo_df["Repetitive"]==1)]

adhd_sum = adhd_demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","ADHD","Self-harm","Anxiety","Depression","Repetitive"]).sum()/adhd_demo_df.shape[0]
selfharm_sum = selfharm_demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","ADHD","Self-harm","Anxiety","Depression","Repetitive"]).sum()/selfharm_demo_df.shape[0]
anxiety_sum = anxiety_demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","ADHD","Self-harm","Anxiety","Depression","Repetitive"]).sum()/anxiety_demo_df.shape[0]
depression_sum = depression_demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","ADHD","Self-harm","Anxiety","Depression","Repetitive"]).sum()/depression_demo_df.shape[0]
repetitive_sum = repetitive_demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","ADHD","Self-harm","Anxiety","Depression","Repetitive"]).sum()/repetitive_demo_df.shape[0]

# print(adhd_demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","ADHD","Self-harm","Anxiety","Depression","Repetitive"]).sum())
# print(selfharm_demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","ADHD","Self-harm","Anxiety","Depression","Repetitive"]).sum())
# print(anxiety_demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","ADHD","Self-harm","Anxiety","Depression","Repetitive"]).sum())
# print(depression_demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","ADHD","Self-harm","Anxiety","Depression","Repetitive"]).sum())
# print(repetitive_demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","ADHD","Self-harm","Anxiety","Depression","Repetitive"]).sum())
# print(f"Nb of adhd : {adhd_demo_df.shape[0]}, Nb of sh : {selfharm_demo_df.shape[0]}, Nb of anxiety : {anxiety_demo_df.shape[0]}, Nb of depression : {depression_demo_df.shape[0]}, Nb of repetitive : {repetitive_demo_df.shape[0]}")
# print(adhd_sum,selfharm_sum,anxiety_sum,depression_sum,repetitive_sum)

width=0.1
index=np.arange(len(adhd_sum))
plt.close()
plt.bar(index-3*width/2, adhd_sum, width=width, label = f"ADHD ({adhd_demo_df.shape[0]})",color = 'limegreen')
plt.bar(index-width/2, selfharm_sum, width=width, label = f"Self Harm ({selfharm_demo_df.shape[0]})",color = 'maroon')
plt.bar(index+width/2, anxiety_sum, width=width, label = f"Anxiety ({anxiety_demo_df.shape[0]})",color = 'mediumpurple')
plt.bar(index+3*width/2, depression_sum, width=width, label = f"Depression ({depression_demo_df.shape[0]})",color = 'darkblue')
plt.bar(index+5*width/2, repetitive_sum, width=width, label = f"Repetitive ({repetitive_demo_df.shape[0]})",color = 'yellow')
plt.xticks(index, adhd_sum.index)
plt.gca().set_ylim(0,1)
plt.legend()
plt.title(f"Percentage of children who have a disease, that have a problem")
plt.savefig(f"{folder}/problem_per_disease")