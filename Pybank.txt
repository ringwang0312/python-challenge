import csv
bankpath='C:/Users/rwang/Desktop/CU-NYC-DATA-PT-02-2020-U-C/03-Python/homework/assignment/PyBank/Resources/budget_data.csv'
with open(bankpath,'r') as bankfile:
    bankdata = list(csv.reader(bankfile, delimiter=','))
    bankdata.remove(bankdata[0])
    rowcount = len(bankdata)
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:"+str(rowcount) if rowcount else 'Empty')

value=[int(row[1]) for row in bankdata]
total=sum(value)
print("Total :$",total)

changedata=[]
for i in range(len(bankdata)-1):
        currentrow=(bankdata[i])
        nextrow=(bankdata[i+1])
        currentvalue=int(currentrow[1])
        nextvalue=int(nextrow[1])
        month=nextrow[0]
        changevalue=nextvalue-currentvalue
        changedata.append([month,changevalue])

totalchange=[changevalue[1] for changevalue in changedata]
avg=sum(totalchange)/len(changedata)
print("Average  Change: $",round(avg,2))

max_val = 0
max_mon = ''
for data in changedata:
    cur_val = data[1]
    cur_mon = data[0]
    if cur_val > max_val:
        max_val = cur_val
        max_mon = cur_mon
print("Greatest Increase in Profits :",max_mon, "($",max_val,")")

min_val = int(bankdata[1][1])
min_mon = bankdata[1][0]
for data in changedata:
    cur_val = int(data[1])
    cur_mon = data[0]
    if cur_val < min_val:
        min_val = cur_val
        min_mon = cur_mon
print("Greatest Dncrease in Profits :",min_mon, "($",min_val,")")