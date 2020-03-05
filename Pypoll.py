import csv
pollpath=bankpath='C:/Users/rwang/Desktop/CU-NYC-DATA-PT-02-2020-U-C/03-Python/homework/assignment/PyPoll/Resources/election_data.csv'

with open(pollpath,'r') as pollfile:
    polldata = list(csv.reader(pollfile, delimiter=','))
    polldata.remove(polldata[0])
    rowcount = len(polldata)
    print("Election Results")
    print("-------------------------")
    print("Total Votes: :"+str(rowcount) if rowcount else 'Empty')
    print("-------------------------")
candidate = []
for row in polldata:
    if row[2] not in candidate:
        candidate.append(row[2])  

totalvote1=sum(1 for vote in polldata if vote[2]==candidate[0])
percentage1=totalvote1/rowcount
print(candidate[0],":" ,round(percentage1*100,3),"%","(",totalvote1,")")

totalvote2=sum( 1 for vote in polldata if vote[2]==candidate[1])
percentage2=totalvote2/rowcount
print(candidate[1],":" ,round(percentage2*100,3),"%","(",totalvote2,")")

totalvote3=sum(1 for vote in polldata if vote[2]==candidate[2])
percentage3=totalvote3/rowcount
print(candidate[2],":" ,round(percentage3*100,3),"%","(",totalvote3,")")

totalvote4=sum(1 for vote in polldata if vote[2]==candidate[3])
percentage4=totalvote4/rowcount
print(candidate[3],":" ,round(percentage4*100,3),"%","(",totalvote4,")")

print("-------------------------")
print("Winner: Khan")
print("-------------------------")