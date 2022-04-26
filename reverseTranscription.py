import sys
import os

def endScript():
    os.system('pause')
    sys.exit()

originalGeneList = []

for x in range (1,14): #change second value as needed
    #opens the files containing the sequences
    ##inserts sequences into a list
    ###new lines are stripped out
    n = str(x)
    path = "C:\\<path>\\geneVariantX" + n
    #sequences must be labelled as geneVariantX where X is an integer
    geneFile = open(path,"r")
    contents = geneFile.read().replace('\n', '')
    geneFile.close()
    originalGeneList.append(contents)


reversedGene = ""
processedGeneList = []
reversedComplementedGene = ""

for gene in range (0,13):
    geneVariant = originalGeneList[gene]
    firstCodon = geneVariant[0:3]
    lastCodon = geneVariant[-3:]j

    if firstCodon == "ATG":
        processedGeneList.append(geneVariant)
    elif lastCodon == "CAT":
        #requires reverse complement
        for x in geneVariant:
            #reverses the string
            reversedGene = x + reversedGene
        for x in reversedGene:
            #obtains the complementary nucleotides
            if x == "A" or x == "a":
                complement = "T"
            elif x == "T" or x == "t":
                complement = "A"
            elif x == "C" or x == "c":
                complement = "G"
            elif x == "G" or x == "g":
                complement = "C"
            elif x == "U" or x == "u":
                print("mRNA transcript present, not DNA!")
                endScript()
            else:
                print("Invalid character present!")
                endScript()
            reversedComplementedGene = reversedComplementedGene + complement
        processedGeneList.append(reversedComplementedGene)
    else:
        print("String invalid!") #for debugging
        endScript()


processedGeneVariants = open("processedGeneVariants.txt","a")
for x in processedGeneList:
    processedGeneVariants.write(geneVariant + '\n')
processedGeneVariants.close() #saves memory

endScript()
