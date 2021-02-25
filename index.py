
#read a file 
inputFile = open('./input.txt', 'r')
data = []
inputFile.readline()
inputText = inputFile.readline()

while(inputText):#Extract,separate and convert the data
    inputSplit = inputText.split(' ')
    j1,j2 = inputSplit # using desturcturing 
    advantage = int(j1) - int(j2)
    
    data.append(advantage)
    inputText = inputFile.readline()


varMax = max(data)
varMin = min(data)
absVarMin = abs(varMin)

winningScore = varMax + (varMin)#get a winner
#written a result file
if winningScore > 0 :
    winner = ('1 ' + str(varMax))
    outputFile = open('./output', 'w')
    outputFile.write(winner)

else:
    winner =('2 ' +  str(abs(varMin)))
    outputFile = open('./output', 'w')
    outputFile.write(winner)


