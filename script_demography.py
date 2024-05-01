import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

folder="all_questions/demography"

df = pd.read_csv('IS_LD_N61_corrected23032020.csv', sep=';')
plt.rcParams["figure.figsize"] = (14,8)

demo_df = df[["a1_gender","prim_sec","p4_anx","p4_dep","p4_repet","p4_adhd","p4_ang","p4_beh","p4_eat",
              "p4_sleep","p4_emotion","p4_notschool","p4_sh","p4_meds","p4_interv"]]
demo_df = demo_df.rename(columns= {"a1_gender":"gender", "p4_anx": "Anxiety","p4_dep":"Depression",
                                   "p4_repet":"Repetitive","p4_adhd":"ADHD","p4_ang":"Anger",
                                   "p4_beh":"Behaviour","p4_eat":"Eat","p4_sleep":"Sleep",
                                   "p4_emotion":"Emotions","p4_notschool":"Not School","p4_sh":"Self-harm",
                                   "p4_meds":"Meds","p4_interv":"Intervention"})

# All 

sum = demo_df.drop(columns=["gender","prim_sec"]).sum()
percentage = sum/demo_df.shape[0]

print("Number of children suffering from these diseases/symptoms")
print(sum)
print(f"Percentage of children suffering from these diseases/symptoms ({demo_df.shape[0]})")
print(percentage)

width=0.4
index=np.arange(len(percentage))
plt.close()
plt.bar(index, percentage, width=width, color = 'slateblue')
plt.xticks(index, percentage.index)
plt.title(f"Percentage of children suffering from these disease/symptoms ({demo_df.shape[0]})")
plt.savefig(f"{folder}/demo")

# Gender 

boy_demo_df=demo_df[(demo_df["gender"]==1)]
girl_demo_df=demo_df[(demo_df["gender"]==2)]

boy_sum = boy_demo_df.drop(columns=["gender","prim_sec"]).sum()
girl_sum = girl_demo_df.drop(columns=["gender","prim_sec"]).sum()

boy_percentage = boy_sum/boy_demo_df.shape[0]
girl_percentage = girl_sum/girl_demo_df.shape[0]

print("Number of boys suffering from these diseases/symptoms")
print(boy_sum)
print(f"Percentage of boys suffering from these diseases/symptoms ({boy_demo_df.shape[0]})")
print(boy_percentage)
print("Number of girls suffering from these diseases/symptoms")
print(girl_sum)
print(f"Percentage of girls suffering from these diseases/symptoms ({girl_demo_df.shape[0]})")
print(girl_percentage)

disease_usage = pd.DataFrame({
    'disease': girl_sum.index,
    'Girls': girl_sum.values,
    'Boys': boy_sum.values
})
disease_usage['Total per disease'] = disease_usage['Girls'] + disease_usage['Boys']
total_per_column = disease_usage[['Girls', 'Boys', 'Total per disease']].sum()
total_row = pd.DataFrame([['Total', total_per_column['Girls'], total_per_column['Boys'], total_per_column['Total per disease']]], columns=disease_usage.columns)
disease_usage = pd.concat([disease_usage, total_row], ignore_index=True)

disease_usage.to_csv(f"{folder}/diseases_gender_data.csv", index=False, sep=';')

disease_p_usage = pd.DataFrame({
    'disease': girl_percentage.index,
    'Girls': girl_percentage.values,
    'Boys': boy_percentage.values
})
disease_p_usage['Total per disease'] = disease_p_usage['Girls'] + disease_p_usage['Boys']
total_per_column = disease_p_usage[['Girls', 'Boys', 'Total per disease']].sum()
total_row = pd.DataFrame([['Total', total_per_column['Girls'], total_per_column['Boys'], total_per_column['Total per disease']]], columns=disease_p_usage.columns)
disease_p_usage = pd.concat([disease_p_usage, total_row], ignore_index=True)

disease_p_usage.to_csv(f"{folder}/diseases_percentage_gender_data.csv", index=False, sep=';')


width=0.2
index=np.arange(len(boy_percentage))
plt.close()
plt.bar(index-width/2, boy_percentage, width=width, label = f"Boys ({boy_demo_df.shape[0]})", color = 'dodgerblue')
plt.bar(index+width/2, girl_percentage, width=width, label = f"Girls ({girl_demo_df.shape[0]})", color = 'deeppink')
plt.xticks(index, boy_percentage.index)
plt.legend()
plt.title(f"Percentage of gender suffering from these diseases")
plt.savefig(f"{folder}/gender_demo")

# Prim/sec school

prim_demo_df=demo_df[(demo_df["prim_sec"]==1)]
sec_demo_df=demo_df[(demo_df["prim_sec"]==2)]

prim_sum = prim_demo_df.drop(columns=["gender","prim_sec"]).sum()
sec_sum = sec_demo_df.drop(columns=["gender","prim_sec"]).sum()

prim_percentage = prim_sum/prim_demo_df.shape[0]
sec_percentage = sec_sum/sec_demo_df.shape[0]

print("Number of prims suffering from these diseases/symptoms")
print(prim_sum)
print(f"Percentage of prims suffering from these diseases/symptoms ({prim_demo_df.shape[0]})")
print(prim_percentage)
print("Number of secs suffering from these diseases/symptoms")
print(sec_sum)
print(f"Percentage of secs suffering from these diseases/symptoms ({sec_demo_df.shape[0]})")
print(sec_percentage)

disease_usage = pd.DataFrame({
    'disease': prim_sum.index,
    'Primary School': prim_sum.values,
    'Secondary School': sec_sum.values
})
disease_usage['Total per disease'] = disease_usage['Primary School'] + disease_usage['Secondary School']
total_per_column = disease_usage[['Primary School', 'Secondary School', 'Total per disease']].sum()
total_row = pd.DataFrame([['Total', total_per_column['Primary School'], total_per_column['Secondary School'], total_per_column['Total per disease']]], columns=disease_usage.columns)
disease_usage = pd.concat([disease_usage, total_row], ignore_index=True)

disease_usage.to_csv(f"{folder}/diseases_school_data.csv", index=False, sep=';')

disease_p_usage = pd.DataFrame({
    'disease': prim_percentage.index,
    'Primary School': prim_percentage.values,
    'Secondary School': sec_percentage.values
})
disease_p_usage['Total per disease'] = disease_p_usage['Primary School'] + disease_p_usage['Secondary School']
total_per_column = disease_p_usage[['Primary School', 'Secondary School', 'Total per disease']].sum()
total_row = pd.DataFrame([['Total', total_per_column['Primary School'], total_per_column['Secondary School'], total_per_column['Total per disease']]], columns=disease_p_usage.columns)
disease_p_usage = pd.concat([disease_p_usage, total_row], ignore_index=True)

disease_p_usage.to_csv(f"{folder}/disease_percentage_school_data.csv", index=False, sep=';')

width=0.2
index=np.arange(len(prim_percentage))
plt.close()
plt.bar(index-width/2, prim_percentage, width=width, label = f"Children in primary ({prim_demo_df.shape[0]})",color = 'slateblue')
plt.bar(index+width/2, sec_percentage, width=width, label = f"Children in secondary ({sec_demo_df.shape[0]})",color = 'indigo')
plt.xticks(index, prim_percentage.index)
plt.legend()
plt.title(f"Percentage of children in primary or secondary school \nsuffering from these diseases")
plt.savefig(f"{folder}/prim_sec_demo")

# Gender and prim/sec school

boy_prim_demo_df=demo_df[(demo_df["gender"]==1) & (demo_df["prim_sec"]==1)]
girl_prim_demo_df=demo_df[(demo_df["gender"]==2) & (demo_df["prim_sec"]==1)]
boy_sec_demo_df=demo_df[(demo_df["gender"]==1) & (demo_df["prim_sec"]==2)]
girl_sec_demo_df=demo_df[(demo_df["gender"]==2) & (demo_df["prim_sec"]==2)]

boy_prim_sum = boy_prim_demo_df.drop(columns=["gender","prim_sec"]).sum()
girl_prim_sum = girl_prim_demo_df.drop(columns=["gender","prim_sec"]).sum()
boy_sec_sum = boy_sec_demo_df.drop(columns=["gender","prim_sec"]).sum()
girl_sec_sum = girl_sec_demo_df.drop(columns=["gender","prim_sec"]).sum()

boy_prim_percentage = boy_prim_sum/boy_prim_demo_df.shape[0]
girl_prim_percentage = girl_prim_sum/girl_prim_demo_df.shape[0]
boy_sec_percentage = boy_sec_sum/boy_sec_demo_df.shape[0]
girl_sec_percentage = girl_sec_sum/girl_sec_demo_df.shape[0]

print("Number of boys in primary school suffering from these diseases/symptoms")
print(boy_prim_sum)
print(f"Percentage of boys in primary school suffering from these diseases/symptoms ({boy_prim_demo_df.shape[0]})")
print(boy_prim_percentage)
print("Number of girls in primary school suffering from these diseases/symptoms")
print(girl_prim_sum)
print(f"Percentage of girls in primary school suffering from these diseases/symptoms ({girl_prim_demo_df.shape[0]})")
print(girl_prim_percentage)
print("Number of boys in secondary school suffering from these diseases/symptoms")
print(boy_sec_sum)
print(f"Percentage of boys in secondary school suffering from these diseases/symptoms ({boy_sec_demo_df.shape[0]})")
print(boy_sec_percentage)
print("Number of girls in secondary school suffering from these diseases/symptoms")
print(girl_sec_sum)
print(f"Percentage of girls in secondary school suffering from these diseases/symptoms ({girl_sec_demo_df.shape[0]})")
print(girl_percentage)

width=0.1
index=np.arange(len(boy_prim_percentage))
plt.close()
plt.bar(index-3*width/2, boy_prim_percentage, width=width, label = f"Boys in primary ({boy_prim_demo_df.shape[0]})",color = 'dodgerblue')
plt.bar(index-width/2, boy_sec_percentage, width=width, label = f"Boys in secondary ({boy_sec_demo_df.shape[0]})",color = 'blue')
plt.bar(index+width/2, girl_prim_percentage, width=width, label = f"Girls in primary ({girl_prim_demo_df.shape[0]})",color = 'deeppink')
plt.bar(index+3*width/2, girl_sec_percentage, width=width, label = f"Girls in secondary ({girl_sec_demo_df.shape[0]})",color = 'purple')
plt.xticks(index, boy_prim_percentage.index)
plt.legend()
plt.title(f"Percentage of gender in primary or secondary school \nsuffering from these diseases")
plt.savefig(f"{folder}/gender_prim_sec_demo")

# How many diseases

plt.close()
sum_diseases = demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","Eat","Sleep","Anger","Behaviour","Emotions","Not School"]).sum(axis=1)
max_value = sum_diseases.max()
min_value = sum_diseases.min()

print("Number of diseases per child")
print(sum_diseases)

plt.hist(sum_diseases, bins=range(min_value, max_value + 2), rwidth=0.8, align='left')
plt.title("Number of diseases per child")
plt.savefig(f"{folder}/nb_diseases")

# How many problems

plt.close()
sum_problems = demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","ADHD","Self-harm","Anxiety","Depression","Repetitive"]).sum(axis=1)
max_value = sum_problems.max()
min_value = sum_problems.min()

print("Number of problems per child")
print(sum_problems)

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

print(adhd_demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","ADHD","Self-harm","Anxiety","Depression","Repetitive"]).sum())
print(selfharm_demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","ADHD","Self-harm","Anxiety","Depression","Repetitive"]).sum())
print(anxiety_demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","ADHD","Self-harm","Anxiety","Depression","Repetitive"]).sum())
print(depression_demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","ADHD","Self-harm","Anxiety","Depression","Repetitive"]).sum())
print(repetitive_demo_df.drop(columns=["gender", "prim_sec","Intervention","Meds","ADHD","Self-harm","Anxiety","Depression","Repetitive"]).sum())
print(f"Nb of adhd : {adhd_demo_df.shape[0]}, Nb of sh : {selfharm_demo_df.shape[0]}, Nb of anxiety : {anxiety_demo_df.shape[0]}, Nb of depression : {depression_demo_df.shape[0]}, Nb of repetitive : {repetitive_demo_df.shape[0]}")
print(adhd_sum,selfharm_sum,anxiety_sum,depression_sum,repetitive_sum)

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