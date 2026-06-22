print("DNA Base Counter")

dna = input("Enter DNA sequence (A, T, G, C only): ")
a_count = dna.count("A")
t_count = dna.count("T")
g_count = dna.count("G")
c_count = dna.count("C")
print("A: ", a_count)
print("T: ", t_count)
print("G: ", g_count)
print("C: ", c_count)

first_base = dna[0]
last_base = dna[-1]
print("First base: ", first_base)
print("Last base: ", last_base)

if any(base not in "ATGC" for base in dna):
    print("Invalid DNA sequence detected")
else:
    a_count = dna.count("A")
    t_count = dna.count("T")
    g_count = dna.count("G")
    c_count = dna.count("C")

    print("A: ", a_count)
    print("T: ", t_count)
    print("G: ", g_count)
    print("C: ", c_count)
    first_base = dna[0]
    last_base = dna[-1]
    print("First base: ", first_base)
    print("Last base: ", last_base)
