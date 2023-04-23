import pandas as pd
df= {'col1': ['a1', 'a2', 'a3'],
        'col2': ['b1', 'b2', 'b3']}
df=pd.Dataframe(df)
print(df)

for i,j, in enumerate(df):
    print(i+" "+j)


import os,shutil
labels = ['Cardiomegaly','Emphysema','Effusion','Hernia','Nodule','Pneumothorax','Atelectasis','Pleural_Thickening','Mass','Edema','Consolidation','Infiltration','Fibrosis','Pneumonia', 'No Finding']
original = "inital path "
o=r'C:\Users\bijin\Downloads\archive\test'
for i,j, in enumerate(df):
    o1=os.path.join(o,i)
    if not os.path.exists(o1):
        print(0)
        os.mkdir(o1)
    o2=os.path.join(original,j)
    o3=o1.path.join(o3,j)
    shutil.copyfile(o2,o3)

