genome = input()
g_count = genome.upper().count("G")
c_count = genome.upper().count("C")
Percentage = ((g_count + c_count)/len(genome)) * 100
print(Percentage)