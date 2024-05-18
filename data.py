import pandas as pd
import argparse
import numpy as np
import matplotlib.pyplot as plt

class Data:
    def __init__(self):
        parser=argparse.ArgumentParser()
        parser.add_argument("disease")
        parser.add_argument("question")
        parser.add_argument("folder")
        args=parser.parse_args()
        self.disease = args.disease
        self.question = args.question
        self.folder = args.folder
        self.folder_save = f"{self.folder}/{self.disease}"
        if self.question == "demography":
            self.df = self.demog_df()
        else:
            self.df = self.questions_df()

    def args(self):
        return self.disease, self.question, self.folder_save

    def preprocess(self):
        df = pd.read_csv('Internet_Survey_v2.csv', sep=';')
        df = df.drop(columns=["clinic_ori", "p4_MH", "p4_other", "p5_TECH", "p5_mobilediff", "p5_gamediff", 
                            "p5_compdiff", "p5_laptopdiff", "p5_tabletdiff", "p5_num_appliances", "a5_num_appliances", 
                            "p5_appliancesdiff", 
                            "p6_bedroomdiff", "p6_homediff", "p6_frienddiff", "p6_schooldiff", "p6_num_locations", 
                            "a6_num_locations", "p6_WHERE",
                            "p6_publicdiff", "p6_num_locationsdiff", "p7_WHEN",  "p8_dontknow", 
                            "a8_dontknow", "p8_num_types", "a8_num_types", "p9_INTERPER", "p9_other", 
                            "p10_HABIT", "p10_other", "a10_other", "p10_num_addiction_sx", 
                            "a10_num_addiction_sx", "p11_TALK", "p11_other", "a11_other","p12_GOOD",
                            "p_OTHERS"]) #"p8_disease",
        return df

    def questions_df(self):
        disease, question = self.disease, self.question
        df = self.preprocess()
        if (disease in df.columns) :
            reduced_df = df[df[disease]==1]
            disease=disease[3:]+"_"
        else:
            reduced_df = df
            disease=""

        question_adult='p'+question
        question_child='a'+question

        columns_to_select = [col for col in reduced_df.columns if col.startswith(question_child)]+[col for col in reduced_df.columns if col.startswith(question_adult)] + ['a1_gender', 'prim_sec']
        reduced_df = reduced_df[columns_to_select]
        reduced_df = reduced_df.rename(columns= {"a1_gender":"gender"})
        return reduced_df

    def demog_df(self):
        df = self.preprocess()
        demo_df = df[["a1_gender","prim_sec","p4_anx","p4_dep","p4_repet","p4_adhd","p4_ang","p4_beh","p4_eat",
              "p4_sleep","p4_emotion","p4_notschool","p4_sh","p4_meds","p4_interv"]]
        demo_df = demo_df.rename(columns= {"a1_gender":"gender", "p4_anx": "Anxiety","p4_dep":"Depression",
                                   "p4_repet":"Repetitive","p4_adhd":"ADHD","p4_ang":"Anger",
                                   "p4_beh":"Behaviour","p4_eat":"Eat","p4_sleep":"Sleep",
                                   "p4_emotion":"Emotions","p4_notschool":"Not School","p4_sh":"Self-harm",
                                   "p4_meds":"Meds","p4_interv":"Intervention"})
        return demo_df
    
    def plot(self, group):
        df = self.df
        if group == "children":
            dico_df = {"children" : (df,'blue')}
        elif group == "gender":
            dico_df={"boys":(df[df["gender"]==1],'dodgerblue'), 
                     "girls":(df[df["gender"]==2],'deeppink')}
        elif group == "school":
            dico_df = {"primary":(df[(df["prim_sec"]==1)],'slateblue'), 
                       "secondary":(df[(df["prim_sec"]==2)],'indigo')}
        else:
            dico_df = {"boys in primary": (df[(df["gender"]==1) & (df["prim_sec"]==1)],'dodgerblue'),
                       "girls in primary": (df[(df["gender"]==2) & (df["prim_sec"]==1)],'blue'),
                       "boys in secondary": (df[(df["gender"]==1) & (df["prim_sec"]==2)],'deeppink'),
                       "girls in secondary": (df[(df["gender"]==2) & (df["prim_sec"]==2)],'purple')}
        sum_df = pd.DataFrame()
        percentage_df = pd.DataFrame()
        i = 0
        plt.close()
        for gp, (df,color) in dico_df.items():
            sum = df.drop(columns=["gender","prim_sec"]).sum()
            sum_df = self.df_csv(sum_df, gp, sum)

            percentage = sum/df.shape[0]
            percentage_df = self.df_csv(percentage_df, gp, percentage)
            
            width=0.4/len(dico_df)
            offset = width*(len(dico_df)-1)/2
            index=np.arange(len(percentage))
            plt.bar(index - offset + i*width, percentage, width=width, color = color)
            i+=1
        plt.xticks(index - offset, percentage.index, rotation=30)
        if self.disease != "everyone":
            plt.title(f"Percentage of {group} suffering from {self.disease[:-1]} (Total = {df.shape[0]})")
        else:
            plt.title(f"Percentage of {group} (Total = {df.shape[0]})")
        sum_df['Total'] = sum_df.sum(axis=1)
        percentage_df['Total'] = percentage_df.sum(axis=1)
        sum_df.reset_index(inplace=True)
        percentage_df.reset_index(inplace=True)
        sum_df.to_csv(f"{self.folder_save}/{self.question}_{group}_data.csv", index=False, sep=';')
        percentage_df.to_csv(f"{self.folder_save}/{self.question}_{group}_percentage.csv", index=False, sep=';')
        plt.savefig(f"{self.folder_save}/{self.question}_{group}")
    
    def df_csv(self, df_csv, gp, tab):
        df_gp = pd.DataFrame({'Line' : tab.index,
                                gp : tab.values})
        total_column = df_gp[[gp]].sum().item()
        total_row = pd.DataFrame([['Total', total_column]], columns=df_gp.columns)
        df_gp = pd.concat([df_gp, total_row], ignore_index=True)
        df_gp.set_index('Line', inplace=True)
        df_csv = df_csv.combine_first(df_gp)
        return df_csv