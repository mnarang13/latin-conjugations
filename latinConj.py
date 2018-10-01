pres = input("Enter the first principal part of the Latin verb you wish to conjugate (no 3rd-ios or irregular verbs): ")
infinitive = input("Enter the infinitive of the Latin verb you wish to conjugate: ")
perfect = input("Enter the third principal part of the Latin verb you wish to conjugate: ")
conj = input("What conjugation is your verb? (1, 2, 3, or 4) ")

length = len(pres)
length1 = len(perfect)
stem = pres[:length - 1]
perfect1 = perfect[:length - 1]

def presEnds1(stem):
    endings = ["o", "as", "at", "amus", "atis", "ant"]
    for i in range(6):
        print(stem + endings[i])

def presEnds2(stem):
    endings = ["o", "s", "t", "mus", "tis", "nt"]
    for i in range(6):
        print(stem + endings[i])

def presEnds3(stem):
    endings = ["o", "is", "it", "imus", "itus", "unt"]
    for i in range(6):
        print(stem + endings[i])

def presEnds4(stem):
    endings = ["o", "s", "t", "mus", "tis", "unt"]
    for i in range(6):
        print(stem + endings[i])

def imperfEnds1(stem):
    endings = ["abam", "abas", "abat", "abamus", "abatis", "abant"]
    for i in range(6):
        print(stem + endings[i])

def imperfEnds34(stem):
    endings = ["ebam", "ebas", "ebat", "ebamus", "ebatis", "ebant"]
    for i in range(6):
        print(stem + endings[i])

def imperfEnds2(stem):
    endings = ["bam", "bas", "bat", "bamus", "batis", "bant"]
    for i in range(6):
        print(stem + endings[i])

def perfEnds(perfect1):
    endings = ["i", "isti", "it", "imus", "istis", "erunt"]
    for i in range(6):
        print(perfect1 + endings[i])

def pluPerfEnds(perfect1):
    endings = ["eram", "eras", "erat", "eramus", "eratis", "erant"]
    for i in range(6):
        print(perfect1 + endings[i])

def imperfSubEnds(infinitive):
    endings = ["m", "s", "t", "mus", "tis", "nt"]
    for i in range(6):
        print(infinitive + endings[i])

def pluperfSubEnds(perfect):
    endings = ["ssem", "sses", "sset", "ssemus", "ssetis", "ssent"]
    for i in range(6):
        print(perfect + endings[i])

if conj == "1":
    print("Present active tense of " + infinitive + ": ")
    presEnds1(stem)
    print("Imperfect active indicative tense of " + infinitive + ": ")
    imperfEnds1(stem)
    print("Perfect active tense of " + infinitive + ": ")
    perfEnds(perfect1)
    print("Pluperfect active indicative tense of " + infinitive + ": ")
    pluPerfEnds(perfect1)
    print("Imperfect active subjunctive tense of " + infinitive + ": ")
    imperfSubEnds(infinitive)
    print("Pluperfect active subjunctive tense of " + infinitive + ": ")
    pluperfSubEnds(perfect)
elif conj == "2":
    print("Present tense of " + infinitive + ": ")
    presEnds2(stem)
    print("Imperfect tense of " + infinitive + ": ")
    imperfEnds2(stem)
    print("Perfect tense of " + infinitive + ": ")
    perfEnds(perfect1)
    print("Pluperfect active indicative tense of " + infinitive + ": ")
    pluPerfEnds(perfect1)
    print("Imperfect active subjunctive tense of " + infinitive + ": ")
    imperfSubEnds(infinitive)
    print("Pluperfect active subjunctive tense of " + infinitive + ": ")
    pluperfSubEnds(perfect)
elif conj == "3":
    print("Present tense of " + infinitive + ": ")
    presEnds3(stem)
    print("Imperfect tense of " + infinitive + ": ")
    imperfEnds34(stem)
    print("Perfect tense of " + infinitive + ": ")
    perfEnds(perfect1)
    print("Pluperfect active indicative tense of " + infinitive + ": ")
    pluPerfEnds(perfect1)
    print("Imperfect active subjunctive tense of " + infinitive + ": ")
    imperfSubEnds(infinitive)
    print("Pluperfect active subjunctive tense of " + infinitive + ": ")
    pluperfSubEnds(perfect)
elif conj == "4":
    print("Present tense of " + infinitive + ": ")
    presEnds4(stem)
    print("Imperfect tense of " + infinitive + ": ")
    imperfEnds34(stem)
    print("Perfect tense of " + infinitive + ": ")
    perfEnds(perfect1)
    print("Pluperfect active indicative tense of " + infinitive + ": ")
    pluPerfEnds(perfect1)
    print("Imperfect active subjunctive tense of " + infinitive + ": ")
    imperfSubEnds(infinitive)
    print("Pluperfect active subjunctive tense of " + infinitive + ": ")
    pluperfSubEnds(perfect)
