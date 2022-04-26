import sys
import os
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
#requires install using <pip install biopython>

def endScript():
    os.system('pause')
    sys.exit()

sequenceList = []

#opens the files containing the sequences
for x in range (2):
    n = str(x)
    path = "C:\\<path>\\sequenceX" + n +".txt"
    #sequences must be labelled as sequenceX where X is 1 or 2
    sequenceFile = open(path,"r")
    contents = sequenceFile.read().replace('\n', '')
    #new lines are stripped out if present
    sequenceFile.close()
    sequenceList.append(contents)

sequenceOne = sequenceList[0]
sequenceTwo = sequenceList[1]
#easier than iterating variable names within the for loop

alignmentType = "global" #switch between global and local
alignmentArgs = "ms" #matching arguments -> pairwise alignment requires different numbers of args based on these args
alignmentAttributes = alignmentType+alignmentArgs
matchScore = 2
mismatchScore = -1
gapPenalty = -0.5
extendedGapPenalty = -0.1
possibleAlignments = getattr(pairwise2.align, alignmentAttributes)(sequenceOne, sequenceTwo, matchScore, mismatchScore, gapPenalty, extendedGapPenalty)


printAlignments = False

if printAlignments == True:
    for x in possibleAlignments:
        print(format_alignment(*x))
        #clearer way to print the list of alignments, although less so for longer alignments
elif printAlignments == False:
    pass
else:
    "Error!"
    endScript()

#identifies best match
bestScore = round(possibleAlignments[0][2], 1)
print("Highest score ("+alignmentType+"):", bestScore)

#finds shortest sequence and determines the match against other sequence
globalAlignment = pairwise2.align.globalxx(sequenceOne, sequenceTwo) #can use local but args must be xx not ms
shortestSequence = min(len(sequenceOne), len(sequenceTwo))
matches = globalAlignment[0][2]

percentMatch = round(((matches / shortestSequence) * 100),1)
print("Percent alignment:", str(percentMatch)+"%")
print()

endScript()
