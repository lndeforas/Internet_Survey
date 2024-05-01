import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import argparse
parser=argparse.ArgumentParser()
parser.add_argument("why")
parser.add_argument("question")
args=parser.parse_args()
why = args.why
question = args.question

df = pd.read_csv('IS_LD_N61_corrected23032020.csv', sep=';')
df = df.drop(columns=["a7_num_types", "a7_dontknow", "a9_num_addiction_sx", "a9_other", "a10_other", "a11_other",
                      "p8_num_types", "p8_dontknow", "p9_other", "p10_other", "p10_num_addiction_sx", "p11_other", "p17_other",
                      "a5_num_locations", "a4_num_appliances", "p6_num_locations", "p5_num_appliances"])

folder_csv=f"all_questions/{why}"
folder_graphs=f"all_questions/{why}"

if (why in df.columns) :
    reduced_df = df[df[why]==1]
    why=why[3:]+"_"
else:
    reduced_df = df
    why=""

columns_to_select = [col for col in reduced_df.columns if col.startswith(question)] + ['a1_gender', 'prim_sec']
reduced_df = reduced_df[columns_to_select]
reduced_df = reduced_df.rename(columns= {"a1_gender":"gender"})

# All 

all_df=reduced_df

sum = all_df.drop(columns=["gender","prim_sec"]).sum()
percentage = sum/all_df.shape[0]

print(f"Number of children suffering from {why[:-1]} (Total = {all_df.shape[0]})")
print(sum)
print(f"Percentage of children suffering from {why[:-1]}")
print(percentage)

width=0.4
index=np.arange(len(percentage))
plt.close()
plt.bar(index, percentage, width=width, color = 'slateblue')
plt.xticks(index, percentage.index, rotation=30)

if why != "":
    plt.title(f"Percentage of children suffering from {why[:-1]} (Total = {all_df.shape[0]})")
else:
    plt.title(f"Percentage of children (Total = {all_df.shape[0]})")
plt.savefig(f"{folder_graphs}/{question}_all")

# Gender 

boy_df=reduced_df[(reduced_df["gender"]==1)]
girl_df=reduced_df[(reduced_df["gender"]==2)]

boy_sum = boy_df.drop(columns=["gender","prim_sec"]).sum()
girl_sum = girl_df.drop(columns=["gender","prim_sec"]).sum()
boy_percentage = boy_sum/boy_df.shape[0]
girl_percentage = girl_sum/girl_df.shape[0]

print(f"Number of girls suffering from {why[:-1]}")
print(girl_sum)
print(f"Number of boys suffering from {why[:-1]}")
print(boy_sum)
print(f"Number of girls : {girl_df.shape[0]} and boys : {boy_df.shape[0]}")
print(f"Percentage of girls suffering from {why[:-1]}")
print(girl_percentage)
print(f"Percentage of boys suffering from {why[:-1]}")
print(boy_percentage)

sum_df = pd.DataFrame({
    'Line': girl_sum.index,
    'Girls': girl_sum.values,
    'Boys': boy_sum.values
})
sum_df['Total per Line'] = sum_df['Girls'] + sum_df['Boys']
total_per_column = sum_df[['Girls', 'Boys', 'Total per Line']].sum()
total_row = pd.DataFrame([['Total', total_per_column['Girls'], total_per_column['Boys'], total_per_column['Total per Line']]], columns=sum_df.columns)
sum_df = pd.concat([sum_df, total_row], ignore_index=True)

sum_df.to_csv(f"{folder_csv}/{question}_gender_data.csv", index=False, sep=';')

percentage_df = pd.DataFrame({
    'Line': girl_percentage.index,
    'Girls': girl_percentage.values,
    'Boys': boy_percentage.values
})
percentage_df['Total per Line'] = percentage_df['Girls'] + percentage_df['Boys']
total_per_column = percentage_df[['Girls', 'Boys', 'Total per Line']].sum()
total_row = pd.DataFrame([['Total', total_per_column['Girls'], total_per_column['Boys'], total_per_column['Total per Line']]], columns=percentage_df.columns)
percentage_df = pd.concat([percentage_df, total_row], ignore_index=True)

percentage_df.to_csv(f"{folder_csv}/{question}_percentage_gender_data.csv", index=False, sep=';')

width=0.2
index=np.arange(len(boy_percentage))
plt.close()
plt.bar(index-width/2, boy_percentage, width=width, label = f"Boys ({boy_df.shape[0]})", color = 'dodgerblue')
plt.bar(index+width/2, girl_percentage, width=width, label = f"Girls ({girl_df.shape[0]})", color = 'deeppink')
plt.xticks(index, boy_percentage.index, rotation=30)
plt.legend()
if why != "":
    plt.title(f"Percentage of gender suffering from {why[:-1]}")
else:
    plt.title("Percentage of gender")
plt.savefig(f"{folder_graphs}/{question}_gender")

# Prim/sec school

prim_df=reduced_df[(reduced_df["prim_sec"]==1)]
sec_df=reduced_df[(reduced_df["prim_sec"]==2)]

prim_sum = prim_df.drop(columns=["gender","prim_sec"]).sum()
sec_sum = sec_df.drop(columns=["gender","prim_sec"]).sum()

prim_percentage = prim_sum/prim_df.shape[0]
sec_percentage = sec_sum/sec_df.shape[0]

print(f"Number of primary students suffering from {why[:-1]}")
print(prim_df.drop(columns=["gender","prim_sec"]).sum())
print(f"Number of secondary students suffering from {why[:-1]}")
print(sec_df.drop(columns=["gender","prim_sec"]).sum())
print(f"Number of primary students : {prim_df.shape[0]} and secondary students : {sec_df.shape[0]}")
print(f"Percentage of primary students suffering from {why[:-1]}")
print(prim_percentage)
print(f"Percentage of secondary students suffering from {why[:-1]}")
print(sec_percentage)

sum_df = pd.DataFrame({
    'Line': prim_sum.index,
    'Primary School': prim_sum.values,
    'Secondary School': sec_sum.values
})
sum_df['Total per Line'] = sum_df['Primary School'] + sum_df['Secondary School']
total_per_column = sum_df[['Primary School', 'Secondary School', 'Total per Line']].sum()
total_row = pd.DataFrame([['Total', total_per_column['Primary School'], total_per_column['Secondary School'], total_per_column['Total per Line']]], columns=sum_df.columns)
sum_df = pd.concat([sum_df, total_row], ignore_index=True)

sum_df.to_csv(f"{folder_csv}/{question}_school_data.csv", index=False, sep=';')

percentage_df = pd.DataFrame({
    'Line': prim_percentage.index,
    'Primary School': prim_percentage.values,
    'Secondary School': sec_percentage.values
})
percentage_df['Total per Line'] = percentage_df['Primary School'] + percentage_df['Secondary School']
total_per_column = percentage_df[['Primary School', 'Secondary School', 'Total per Line']].sum()
total_row = pd.DataFrame([['Total', total_per_column['Primary School'], total_per_column['Secondary School'], total_per_column['Total per Line']]], columns=percentage_df.columns)
percentage_df = pd.concat([percentage_df, total_row], ignore_index=True)

percentage_df.to_csv(f"{folder_csv}/{question}_percentage_school_data.csv", index=False, sep=';')

width=0.2
index=np.arange(len(prim_percentage))
plt.close()
plt.bar(index-width/2, prim_percentage, width=width, label = f"Children in primary ({prim_df.shape[0]})",color = 'slateblue')
plt.bar(index+width/2, sec_percentage, width=width, label = f"Children in secondary ({sec_df.shape[0]})",color = 'indigo')
plt.xticks(index, prim_percentage.index, rotation=30)
plt.legend()
if why != "":
    plt.title(f"Percentage of children in primary or secondary school \nsuffering from {why[:-1]}")
else:
    plt.title(f"Percentage of children in primary or secondary school")
plt.savefig(f"{folder_graphs}/{question}_prim_sec")

# Gender and prim/sec school

boy_prim_df=reduced_df[(reduced_df["gender"]==1) & (reduced_df["prim_sec"]==1)]
girl_prim_df=reduced_df[(reduced_df["gender"]==2) & (reduced_df["prim_sec"]==1)]
boy_sec_df=reduced_df[(reduced_df["gender"]==1) & (reduced_df["prim_sec"]==2)]
girl_sec_df=reduced_df[(reduced_df["gender"]==2) & (reduced_df["prim_sec"]==2)]

boy_prim_sum = boy_prim_df.drop(columns=["gender","prim_sec"]).sum()
girl_prim_sum = girl_prim_df.drop(columns=["gender","prim_sec"]).sum()
boy_sec_sum = boy_sec_df.drop(columns=["gender","prim_sec"]).sum()
girl_sec_sum = girl_sec_df.drop(columns=["gender","prim_sec"]).sum()

boy_prim_percentage = boy_prim_sum/boy_prim_df.shape[0]
girl_prim_percentage = girl_prim_sum/girl_prim_df.shape[0]
boy_sec_percentage = boy_sec_sum/boy_sec_df.shape[0]
girl_sec_percentage = girl_sec_sum/girl_sec_df.shape[0]

print(f"Number of girls in primary suffering from {why[:-1]}")
print(girl_prim_sum)
print(f"Number of girls in secondary suffering from {why[:-1]}")
print(girl_sec_sum)
print(f"Number of boys in primary suffering from {why[:-1]}")
print(boy_prim_sum)
print(f"Number of boys in secondary suffering from {why[:-1]}")
print(boy_sec_sum)
print(f"Number of boys in primary : {boy_prim_df.shape[0]} and girls in primary : {girl_prim_df.shape[0]}\n",
      f"Number of boys in secondary : {boy_sec_df.shape[0]} and girls in secondary : {girl_sec_df.shape[0]}")
print(f"Percentage of girls in primary suffering from {why[:-1]}")
print(girl_prim_percentage)
print(f"Percentage of girls in secondary suffering from {why[:-1]}")
print(girl_sec_percentage)
print(f"Percentage of boys in primary suffering from {why[:-1]}")
print(boy_prim_percentage)
print(f"Percentage of boys in secondary suffering from {why[:-1]}")
print(boy_sec_percentage)

width=0.1
index=np.arange(len(boy_prim_percentage))
plt.close()
plt.bar(index-3*width/2, boy_prim_percentage, width=width, label = f"Boys in primary ({boy_prim_df.shape[0]})",color = 'dodgerblue')
plt.bar(index-width/2, boy_sec_percentage, width=width, label = f"Boys in secondary ({boy_sec_df.shape[0]})",color = 'blue')
plt.bar(index+width/2, girl_prim_percentage, width=width, label = f"Girls in primary ({girl_prim_df.shape[0]})",color = 'deeppink')
plt.bar(index+3*width/2, girl_sec_percentage, width=width, label = f"Girls in secondary ({girl_sec_df.shape[0]})",color = 'purple')
plt.xticks(index, boy_prim_percentage.index, rotation=30)
plt.legend()
if why != "":
    plt.title(f"Percentage of gender in primary or secondary school \nsuffering from {why[:-1]}")
else:
    plt.title(f"Percentage of gender in primary or secondary school")
plt.savefig(f"{folder_graphs}/{question}_prim_sec_gender")

# Number of devices per child
plt.close()
sum_lines = reduced_df.drop(columns=["gender", "prim_sec"]).sum(axis=1)
max_value = sum_lines.max()
min_value = sum_lines.min()
plt.hist(sum_lines, bins=range(min_value, max_value + 2), rwidth=0.8, align='left')

if why != "":
    plt.title(f"Number of lines=1 per child \nsuffering from {why[:-1]}")
else:
    plt.title(f"Number of lines=1 per child")
plt.savefig(f"{folder_graphs}/{question}_nb_lines")