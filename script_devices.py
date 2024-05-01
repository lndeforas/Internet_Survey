import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import argparse
parser=argparse.ArgumentParser()
parser.add_argument("why")
args=parser.parse_args()
why = args.why

df = pd.read_csv('IS_LD_N61_corrected23032020.csv', sep=';')

folder_csv="devices_csv"
folder_graphs="devices"

if ',' in why:
    why = "p4_anx"
    why2= "p4_dep"
    a_devices_df = df[(df[why]==1) | (df[why2] == 1)][["a1_gender","prim_sec","a4_mobile","a4_game","a4_comp","a4_laptop","a4_tablet"]]
    why=why[3:]+"_"+why2[3:]+"_"
elif (why in df.columns) :
    a_devices_df = df[df[why]==1][["a1_gender","prim_sec","a4_mobile","a4_game","a4_comp","a4_laptop","a4_tablet"]]
    why=why[3:]+"_"
else:
    a_devices_df = df[["a1_gender","prim_sec","a4_mobile","a4_game","a4_comp","a4_laptop","a4_tablet"]]
    why=""

a_devices_df = a_devices_df.rename(columns= {"a1_gender":"gender", "a4_mobile":"Mobile phone","a4_game":"Game Console",
                                             "a4_comp":"Computer","a4_laptop":"Laptop","a4_tablet":"Tablet"})

# All 

devices_df=a_devices_df

sum = devices_df.drop(columns=["gender","prim_sec"]).sum()
percentage = sum/devices_df.shape[0]

print(f"Number of children suffering from {why[:-1]} who use the devices")
print(sum)
print(f"Percentage of children suffering from {why[:-1]} who use the devices ({devices_df.shape[0]})")
print(percentage)

width=0.4
index=np.arange(len(percentage))
plt.close()
plt.bar(index, percentage, width=width, color = 'slateblue')
plt.xticks(index, percentage.index)
if why != "":
    plt.title(f"Percentage of children suffering from {why[:-1]} who use the devices ({devices_df.shape[0]})")
else:
    plt.title(f"Percentage of children who use the devices({devices_df.shape[0]})")
plt.savefig(f"{folder_graphs}/{why}devices")

# Gender 

boy_devices_df=a_devices_df[(a_devices_df["gender"]==1)]
girl_devices_df=a_devices_df[(a_devices_df["gender"]==2)]

boy_sum = boy_devices_df.drop(columns=["gender","prim_sec"]).sum()
girl_sum = girl_devices_df.drop(columns=["gender","prim_sec"]).sum()
boy_percentage = boy_sum/boy_devices_df.shape[0]
girl_percentage = girl_sum/girl_devices_df.shape[0]

print(f"Number of girls suffering from {why[:-1]} who use the devices")
print(girl_sum)
print(f"Number of boys suffering from {why[:-1]} who use the devices")
print(boy_sum)
print(f"Number of girls : {girl_devices_df.shape[0]} and boys : {boy_devices_df.shape[0]}")
print(f"Percentage of girls suffering from {why[:-1]} who use the devices")
print(girl_percentage)
print(f"Percentage of boys suffering from {why[:-1]} who use the devices")
print(boy_percentage)

device_usage = pd.DataFrame({
    'Device': girl_sum.index,
    'Girls': girl_sum.values,
    'Boys': boy_sum.values
})
device_usage['Total per Device'] = device_usage['Girls'] + device_usage['Boys']
total_per_column = device_usage[['Girls', 'Boys', 'Total per Device']].sum()
total_row = pd.DataFrame([['Total', total_per_column['Girls'], total_per_column['Boys'], total_per_column['Total per Device']]], columns=device_usage.columns)
device_usage = pd.concat([device_usage, total_row], ignore_index=True)

device_usage.to_csv(f"{folder_csv}/{why}gender_data.csv", index=False, sep=';')

device_p_usage = pd.DataFrame({
    'Device': girl_percentage.index,
    'Girls': girl_percentage.values,
    'Boys': boy_percentage.values
})
device_p_usage['Total per Device'] = device_p_usage['Girls'] + device_p_usage['Boys']
total_per_column = device_p_usage[['Girls', 'Boys', 'Total per Device']].sum()
total_row = pd.DataFrame([['Total', total_per_column['Girls'], total_per_column['Boys'], total_per_column['Total per Device']]], columns=device_p_usage.columns)
device_p_usage = pd.concat([device_p_usage, total_row], ignore_index=True)

device_p_usage.to_csv(f"{folder_csv}/{why}percentage_gender_data.csv", index=False, sep=';')

width=0.2
index=np.arange(len(boy_percentage))
plt.close()
plt.bar(index-width/2, boy_percentage, width=width, label = f"Boys ({boy_devices_df.shape[0]})", color = 'dodgerblue')
plt.bar(index+width/2, girl_percentage, width=width, label = f"Girls ({girl_devices_df.shape[0]})", color = 'deeppink')
plt.xticks(index, boy_percentage.index)
plt.legend()
if why != "":
    plt.title(f"Percentage of gender suffering from {why[:-1]} \nwho use the devices")
else:
    plt.title("Percentage of gender who use the devices")
plt.savefig(f"{folder_graphs}/{why}gender_devices")

# Prim/sec school

prim_devices_df=a_devices_df[(a_devices_df["prim_sec"]==1)]
sec_devices_df=a_devices_df[(a_devices_df["prim_sec"]==2)]

prim_sum = prim_devices_df.drop(columns=["gender","prim_sec"]).sum()
sec_sum = sec_devices_df.drop(columns=["gender","prim_sec"]).sum()

prim_percentage = prim_sum/prim_devices_df.shape[0]
sec_percentage = sec_sum/sec_devices_df.shape[0]

print(f"Number of primary students suffering from {why[:-1]} who use the devices")
print(prim_devices_df.drop(columns=["gender","prim_sec"]).sum())
print(f"Number of secondary students suffering from {why[:-1]} who use the devices")
print(sec_devices_df.drop(columns=["gender","prim_sec"]).sum())
print(f"Number of primary students : {prim_devices_df.shape[0]} and secondary students : {sec_devices_df.shape[0]}")
print(f"Percentage of primary students suffering from {why[:-1]} who use the devices")
print(prim_percentage)
print(f"Percentage of secondary students suffering from {why[:-1]} who use the devices")
print(sec_percentage)

device_usage = pd.DataFrame({
    'Device': prim_sum.index,
    'Primary School': prim_sum.values,
    'Secondary School': sec_sum.values
})
device_usage['Total per Device'] = device_usage['Primary School'] + device_usage['Secondary School']
total_per_column = device_usage[['Primary School', 'Secondary School', 'Total per Device']].sum()
total_row = pd.DataFrame([['Total', total_per_column['Primary School'], total_per_column['Secondary School'], total_per_column['Total per Device']]], columns=device_usage.columns)
device_usage = pd.concat([device_usage, total_row], ignore_index=True)

device_usage.to_csv(f"{folder_csv}/{why}school_data.csv", index=False, sep=';')

device_p_usage = pd.DataFrame({
    'Device': prim_percentage.index,
    'Primary School': prim_percentage.values,
    'Secondary School': sec_percentage.values
})
device_p_usage['Total per Device'] = device_p_usage['Primary School'] + device_p_usage['Secondary School']
total_per_column = device_p_usage[['Primary School', 'Secondary School', 'Total per Device']].sum()
total_row = pd.DataFrame([['Total', total_per_column['Primary School'], total_per_column['Secondary School'], total_per_column['Total per Device']]], columns=device_p_usage.columns)
device_p_usage = pd.concat([device_p_usage, total_row], ignore_index=True)

device_p_usage.to_csv(f"{folder_csv}/{why}percentage_school_data.csv", index=False, sep=';')

width=0.2
index=np.arange(len(prim_percentage))
plt.close()
plt.bar(index-width/2, prim_percentage, width=width, label = f"Children in primary ({prim_devices_df.shape[0]})",color = 'slateblue')
plt.bar(index+width/2, sec_percentage, width=width, label = f"Children in secondary ({sec_devices_df.shape[0]})",color = 'indigo')
plt.xticks(index, prim_percentage.index)
plt.legend()
if why != "":
    plt.title(f"Percentage of children in primary or secondary school \nsuffering from {why[:-1]} who use the devices")
else:
    plt.title(f"Percentage of children in primary or secondary school who use the devices")
plt.savefig(f"{folder_graphs}/{why}prim_sec_devices")

# Gender and prim/sec school

boy_prim_devices_df=a_devices_df[(a_devices_df["gender"]==1) & (a_devices_df["prim_sec"]==1)]
girl_prim_devices_df=a_devices_df[(a_devices_df["gender"]==2) & (a_devices_df["prim_sec"]==1)]
boy_sec_devices_df=a_devices_df[(a_devices_df["gender"]==1) & (a_devices_df["prim_sec"]==2)]
girl_sec_devices_df=a_devices_df[(a_devices_df["gender"]==2) & (a_devices_df["prim_sec"]==2)]

boy_prim_sum = boy_prim_devices_df.drop(columns=["gender","prim_sec"]).sum()
girl_prim_sum = girl_prim_devices_df.drop(columns=["gender","prim_sec"]).sum()
boy_sec_sum = boy_sec_devices_df.drop(columns=["gender","prim_sec"]).sum()
girl_sec_sum = girl_sec_devices_df.drop(columns=["gender","prim_sec"]).sum()

boy_prim_percentage = boy_prim_sum/boy_prim_devices_df.shape[0]
girl_prim_percentage = girl_prim_sum/girl_prim_devices_df.shape[0]
boy_sec_percentage = boy_sec_sum/boy_sec_devices_df.shape[0]
girl_sec_percentage = girl_sec_sum/girl_sec_devices_df.shape[0]

print(f"Number of girls in primary suffering from {why[:-1]} who use the devices")
print(girl_prim_sum)
print(f"Number of girls in secondary suffering from {why[:-1]} who use the devices")
print(girl_sec_sum)
print(f"Number of boys in primary suffering from {why[:-1]} who use the devices")
print(boy_prim_sum)
print(f"Number of boys in secondary suffering from {why[:-1]} who use the devices")
print(boy_sec_sum)
print(f"Number of boys in primary : {boy_prim_devices_df.shape[0]} and girls in primary : {girl_prim_devices_df.shape[0]}\n",
      f"Number of boys in secondary : {boy_sec_devices_df.shape[0]} and girls in secondary : {girl_sec_devices_df.shape[0]}")
print(f"Percentage of girls in primary suffering from {why[:-1]} who use the devices")
print(girl_prim_percentage)
print(f"Percentage of girls in secondary suffering from {why[:-1]} who use the devices")
print(girl_sec_percentage)
print(f"Percentage of boys in primary suffering from {why[:-1]} who use the devices")
print(boy_prim_percentage)
print(f"Percentage of boys in secondary suffering from {why[:-1]} who use the devices")
print(boy_sec_percentage)

width=0.1
index=np.arange(len(boy_prim_percentage))
plt.close()
plt.bar(index-3*width/2, boy_prim_percentage, width=width, label = f"Boys in primary ({boy_prim_devices_df.shape[0]})",color = 'dodgerblue')
plt.bar(index-width/2, boy_sec_percentage, width=width, label = f"Boys in secondary ({boy_sec_devices_df.shape[0]})",color = 'blue')
plt.bar(index+width/2, girl_prim_percentage, width=width, label = f"Girls in primary ({girl_prim_devices_df.shape[0]})",color = 'deeppink')
plt.bar(index+3*width/2, girl_sec_percentage, width=width, label = f"Girls in secondary ({girl_sec_devices_df.shape[0]})",color = 'purple')
plt.xticks(index, boy_prim_percentage.index)
plt.legend()
if why != "":
    plt.title(f"Percentage of gender in primary or secondary school \nsuffering from {why[:-1]} who use the devices")
else:
    plt.title(f"Percentage of gender in primary or secondary school who use the devices")
plt.savefig(f"{folder_graphs}/{why}gender_prim_sec_devices")

# Number of devices per child
plt.close()
sum_problems = a_devices_df.drop(columns=["gender", "prim_sec"]).sum(axis=1)
max_value = sum_problems.max()
min_value = sum_problems.min()
plt.hist(sum_problems, bins=range(min_value, max_value + 2), rwidth=0.8, align='left')

if why != "":
    plt.title(f"Number of devices per child \nsuffering from {why[:-1]}")
else:
    plt.title(f"Number of devices per child")
#plt.savefig("devices/nb_devices")