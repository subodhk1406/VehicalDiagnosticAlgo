import os
import pandas as pd

df_Pipeline = pd.read_csv("Running_Pipline.csv")
f = open("Running_Function.sh", "w")
for i in df_Pipeline.index:
	f.write("cd "+str(df_Pipeline["FileName"][i])+"\n")
	f.write("python Test*.py\n")
	f.write("coverage run --source=.  Test*.py\n")
	f.write("coverage report \n")
	f.write("coverage html \n")
	t1=str(df_Pipeline["FileName"][i]).split('/')
	for k in range(0,len(t1)):
		f.write("cd ..\n")

f.close()
