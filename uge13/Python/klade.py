x = [16.6, 17.4, 18.3, 18.2, 19.6, 20.2, 21.7, 22.0, 22.7, 23.2] 
y = [100, 94, 88, 82, 76, 70, 64, 58, 52, 46]


x_mean = sum(x)/len(x)
y_mean = sum(y)/len(y)	
SAK = sum(float(x-x_mean)**2)
SAP = sum(float(x-x_mean))*sum(y)
#a = SAP/SAK


print x_mean
print y_mean
print SAP
print SAK
#print a
