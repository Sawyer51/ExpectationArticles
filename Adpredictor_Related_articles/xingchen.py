#coding:gbk
import re
fin=open("AdpredictorLogs","r")
fout1=open("sigma.csv","w")
fout2=open("mean.csv","w")
fout3=open("var.csv","w")

for line in fin:
	if line.startswith("trainStageIndex"):
		fout1.write(",".join(re.findall(":([-0-9.]+)",line))+"\n")
	if line.startswith("wPriorMean"):
		fout2.write(",".join(re.findall("([-0-9.]+)",line))+"\n")
	if line.startswith("wPriorVariance"):
		fout3.write(",".join(re.findall("([-0-9.]+)",line))+"\n")
fout1.close()
fout2.close()
fout3.close()
