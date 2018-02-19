C=0.0
G=0.0
DNA=open("helo.txt").read();
total = len(DNA)

for i in range(len(DNA)):
    if DNA[i] == "C":
        C = C+1.0

    if DNA[i] == "G":
        G = G+1.0

print "Number of C: ", C
print "Number of G: ", G
print "Total number of C+G: ", C+G
print "Total length of DNA: ", len(DNA)
print "Percentage: ", (((C+G)/total)*100)
