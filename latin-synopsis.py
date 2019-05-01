pres = input("Enter the first principal part of the Latin verb you wish to conjugate (no irregular verbs): ")
infinitive = input("Enter the infinitive of the Latin verb you wish to conjugate: ")
perfect = input("Enter the third principal part of the Latin verb you wish to conjugate: ")
participle = input("Enter the fourth principal part (m form) of the Latin verb you wish to conjugate: ")

conj = input("What conjugation is your verb? (1, 2, 3, 4, or 5 [3rd-io]) ")
syn = input("Would you like to make a synopsis (y or n)? (Otherwise you'll get the entire verb) ")
num1 = 25

if syn == "y" or syn == "Y":
    num = input("What form of the verb would you like? 1st person singular (1), 2nd person singular (2), 3rd person singular (3), 1st person plural (4), 2nd person plural (5), or 3rd person plural (6): ")
elif syn == "n" or syn == "N":
    num = 7
    num1 = 7

if num == "1":
    num1 = 0
elif num == "2":
    num1 = 1
elif num == "3":
    num1 = 2
elif num == "4":
    num1 = 3
elif num == "5":
    num1 = 4
elif num == "6":
    num1 = 5

length = len(pres)
length1 = len(perfect)
length2 = len(infinitive)
length3 = len(participle)
stem = pres[:length - 1]
perfect1 = perfect[:length1 - 1]
stem1 = infinitive[:length2 - 2]
part1 = participle[:length3 - 2]

def presEnds(stem, num1):
    if conj == "1":
        endings = ["o", "as", "at", "amus", "atis", "ant"]
        if num1 == 7:
            for i in range(6):
                print(stem + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem + endings[num1])
    elif conj == "2":
        endings = ["o", "s", "t", "mus", "tis", "nt"]
        if num1 == 7:
            for i in range(6):
                print(stem + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem + endings[num1])
    elif conj == "3":
        endings = ["o", "is", "it", "imus", "itis", "unt"]
        if num1 == 7:
            for i in range(6):
                print(stem + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem + endings[num1])
    elif conj == "4" or conj == "5":
        endings = ["o", "s", "t", "mus", "tis", "unt"]
        if num1 == 7:
            for i in range(6):
                print(stem + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem + endings[num1])
            
def imperfEnds(stem1, num1, stem):
    if conj in ("1", "2", "3"):
        endings = ["bam", "bas", "bat", "bamus", "batis", "bant"]
        if num1 == 7:
            for i in range(6):
                print(stem1 + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem1 + endings[num1])
    elif conj == "4" or conj == "5":
        endings = ["ebam", "ebas", "ebat", "ebamus", "ebatis", "ebant"]
        if num1 == 7:
            for i in range(6):
                print(stem + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem + endings[num1])

def perfEnds(perfect1, num1):
    endings = ["i", "isti", "it", "imus", "istis", "erunt"]
    if num1 == 7:
        for i in range(6):
            print(perfect1 + endings[i])
    elif num1 in (0, 1, 2, 3, 4, 5):
        print(perfect1 + endings[num1])

def pluPerfEnds(perfect1, num1):
    endings = ["eram", "eras", "erat", "eramus", "eratis", "erant"]
    if num1 == 7:
        for i in range(6):
            print(perfect1 + endings[i])
    elif num1 in (0, 1, 2, 3, 4, 5):
        print(perfect1 + endings[num1])

def imperfSubEnds(infinitive, num1):
    endings = ["m", "s", "t", "mus", "tis", "nt"]
    if num1 == 7:
        for i in range(6):
            print(infinitive + endings[i])
    elif num1 in (0, 1, 2, 3, 4, 5):
        print(infinitive + endings[num1])

def pluperfSubEnds(perfect, num1):
    endings = ["ssem", "sses", "sset", "ssemus", "ssetis", "ssent"]
    if num1 == 7:
        for i in range(6):
            print(perfect + endings[i])
    elif num1 in (0, 1, 2, 3, 4, 5):
        print(perfect + endings[num1])

def presPassEnds(stem, num1):
    if conj == "1":
        endings = ["or", "aris", "atur", "amur", "amini", "antur"]
        if num1 == 7:
            for i in range(6):
                print(stem + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem + endings[num1])
    elif conj == "2" or conj == "4":
        endings = ["or", "ris", "tur", "mur", "mini", "ntur"]
        if num1 == 7:
            for i in range(6):
                print(stem + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem + endings[num1])
    elif conj == "3":
        endings = ["or", "eris", "itur", "imur", "imini", "untur"]
        if num1 == 7:
            for i in range(6):
                print(stem + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem + endings[num1])
    elif conj == "5":
        length = len(stem)
        stem1 = stem[:length - 1]
        endings = ["ior", "eris", "itur", "imur", "imini", "iuntur"]
        if num1 == 7:
            for i in range(6):
                print(stem1 + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem1 + endings[num1])

def imperfPassEnds(stem1, num1, stem):
    if conj in ("1", "2", "3"):
        endings = ["bar", "baris", "batur", "bamur", "bamini", "bantur"]
        if num1 == 7:
            for i in range(6):
                print(stem1 + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem1 + endings[num1])
    elif conj in ("4", "5"):
        endings = ["ebar", "ebaris", "ebatur", "ebamur", "ebamini", "ebantur"]
        if num1 == 7:
            for i in range(6):
                print(stem + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem + endings[num1])

def presPassInfinitive(infinitive):
    if conj in ("1", "2", "4"):
        length = len(infinitive)
        infinitive1 = infinitive[:length - 1]
        print(infinitive1 + "i")
    elif conj == "3" or conj == "5":
        length = len(infinitive)
        infinitive1 = infinitive[:length - 3]
        print(infinitive1 + "i")

def perfActInfinitive(perfect):
    print(perfect + "sse")

def posImperative(stem1, pres):
    if conj in ("1", "2", "4"):
        print(stem1)
        print(stem1 + "te")
    elif conj == "3" or conj == "5":
        if pres == "duco":
            print("duc")
        elif pres == "dico":
            print("dic")
        elif pres == "facio":
            print("fac")
        else:
            print(stem1)
        length = len(stem1)
        stem2 = stem1[:length - 1]
        print(stem2 + "ite")

def presActPart(stem1):
    if conj in ("1", "2", "3"):
        print(stem1 + "ns")
        print(stem1 + "ntis (gen)")
    elif conj == "5" or conj == "4":
        length = len(stem1)
        stem2 = stem1[:length - 1]
        print(stem2 + "iens")
        print(stem2 + "ientis (gen)")

def futurePassPart(stem1):
    if conj in ("1", "2", "3"):
        print(stem1 + "ndus -a -um")
    elif conj in ("5", "4"):
        length = len(stem1)
        stem2 = stem1[:length - 1]
        print(stem2 + "iendus -a -um")

def perfPass(part1, num1):
    endings = ["us -a -um sum", "us -a -um es", "us -a -um est", "i -ae -a sumus", "i -ae -a estis", "i -ae -a sunt"]
    if num1 == 7:
        for i in range(6):
            print(part1 + endings[i])
    elif num1 in (0, 1, 2, 3, 4, 5):
        print(part1 + endings[num1])

def pluperfPass(part1, num1):
    endings = ["us -a -um eram", "us -a -um eras", "us -a -um erat", "i -ae -a eramus", "i -ae -a eratis", "i -ae -a erant"]
    if num1 == 7:
        for i in range(6):
            print(part1 + endings[i])
    elif num1 in (0, 1, 2, 3, 4, 5):
        print(part1 + endings[num1])

def negImperative(infinitive):
    print("noli " + infinitive + " ")
    print("nolite " + infinitive + " ")

def perfPassPart(part1):
    print(part1 + "us -a -um")

def perfPassInfin(part1):
    print(part1 + "us -a -um esse")

def futActPart(part1):
    print(part1 + "urus -a -um")

def futAct(stem1):
    if conj in ("1", "2"):
        endings = ["bo", "bis", "bit", "bimus", "bitis", "bunt"]
        if num1 == 7:
            for i in range(6):
                print(stem1 + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem1 + endings[num1])
    length = len(stem1)
    stem2 = stem1[:length - 1]
    if conj == "3":
        endings = ["am", "es", "et", "emus", "etis", "ent"]
        if num1 == 7:
            for i in range(6):
                print(stem2 + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem2 + endings[num1])
    if conj in ("4", "5"):
        endings = ["iam", "ies", "iet", "iemus", "ietis", "ient"]
        if num1 == 7:
            for i in range(6):
                print(stem2 + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem2 + endings[num1])

def futPerf(perfect1):
    endings = ["ero", "eris", "erit", "erimus", "eritis", "erint"]
    if num1 == 7:
        for i in range(6):
            print(perfect1 + endings[i])
    elif num1 in (0, 1, 2, 3, 4, 5):
        print(perfect1 + endings[num1])

def futPass(stem1, num1, stem):
    if conj in ("1", "2"):
        endings = ["bor", "beris", "bitur", "bimur", "bimini", "buntur"]
        if num1 == 7:
            for i in range(6):
                print(stem1 + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem1 + endings[num1])
    elif conj in ("3", "4", "5"):
        endings = ["ar", "eris", "etur", "emur", "emini", "entur"]
        if num1 == 7:
            for i in range(6):
                print(stem + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem + endings[num1])

def futInfin(part1):
    print(part1 + "urus -a -um esse")

def futPassInfin(part1):
    print(part1 + "um iri")

def futPerfPass(part1):
    endings = ["us -a -um ero", "us -a -um eris", "us -a -um erit", "i -ae -a erimus", "i -ae -a eritis", "i -ae -a erunt"]
    if num1 == 7:
        for i in range(6):
            print(part1 + endings[i])
    elif num1 in (0, 1, 2, 3, 4, 5):
        print(part1 + endings[num1])

def pluperfPassSub(part1):
    endings = ["us -a -um essem", "us -a -um esses", "us -a -um esset", "i -ae -a essemus", "i -ae -a essetis", "i -ae -a essent"]
    if num1 == 7:
        for i in range(6):
            print(part1 + endings[i])
    elif num1 in (0, 1, 2, 3, 4, 5):
        print(part1 + endings[num1])

def imperfPassSub(infinitive):
    endings = ["r", "ris", "tur", "mur", "mini", "ntur"]
    if num1 == 7:
        for i in range(6):
            print(infinitive + endings[i])
    elif num1 in (0, 1, 2, 3, 4, 5):
        print(infinitive + endings[num1])

def presSub(stem):
    if conj == "1":
        endings = ["em", "es", "et", "emus", "etis", "ent"]
        if num1 == 7:
            for i in range(6):
                print(stem + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem + endings[num1])
    elif conj in ("2", "3", "4", "5"):
        endings = ["am", "as", "at", "amus", "atis", "ant"]
        if num1 == 7:
            for i in range(6):
                print(stem + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem + endings[num1])
    #elif conj == "3":
        #endings = ["am", "as", "at", "amus", "atis", "ant"]
        #if num1 == 7:
            #for i in range(6):
                #print(stem + endings[i])
        #elif num1 in (0, 1, 2, 3, 4, 5):
            #print(stem + endings[num1])
    #elif conj in ("4", "5"):
        #endings = ["am", "as", "at", "amus", "atis", "ant"]
        #if num1 == 7:
            #for i in range(6):
                #print(stem + endings[i])
        #elif num1 in (0, 1, 2, 3, 4, 5):
            #print(stem + endings[num1])

def presPassSub(stem):
    if conj == "1":
        endings = ["er", "eris", "etur", "emur", "emini", "entur"]
        if num1 == 7:
            for i in range(6):
                print(stem + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem + endings[num1])
    elif conj in ("2", "3", "4", "5"):
        endings = ["ar", "aris", "atur", "amur", "amini", "antur"]
        if num1 == 7:
            for i in range(6):
                print(stem + endings[i])
        elif num1 in (0, 1, 2, 3, 4, 5):
            print(stem + endings[num1])


def perfSub(perfect1):
    endings = ["erim", "eris", "erit", "erimis", "eritis", "erint"]
    if num1 == 7:
        for i in range(6):
            print(perfect1 + endings[i])
    elif num1 in (0, 1, 2, 3, 4, 5):
        print(perfect1 + endings[num1])

def perfPassSub(part1):
    endings = ["us -a -um sim", "us -a -um sis", "us -a -um sit", "i -ae -a simus", "i -ae -a sitis", "i -ae -a sint"]
    if num1 == 7:
        for i in range(6):
            print(part1 + endings[i])
    elif num1 in (0, 1, 2, 3, 4, 5):
        print(part1 + endings[num1])

def printVerb(stem, stem1, perfect1, infinitive, num1, part1, participle, pres, perfect):

    print(" ")

    print("Principal parts: " + pres + ", " + infinitive + ", " + perfect + ", " + participle + " ")

    print(" ")

    print("Present active indicative of " + infinitive + ": ")
    presEnds(stem, num1)
    print("Imperfect active indicative tense of " + infinitive + ": ")
    imperfEnds(stem1, num1, stem)
    print("Future active indicative of " + infinitive + ": ")
    futAct(stem1)
    print("Perfect active indicative of " + infinitive + ": ")
    perfEnds(perfect1, num1)
    print("Pluperfect active indicative of " + infinitive + ": ")
    pluPerfEnds(perfect1, num1)
    print("Future perfect active indicative of " + infinitive + ": ")
    futPerf(perfect1)

    print(" ")

    print("Present passive indicative of " + infinitive + ": ")
    presPassEnds(stem, num1)
    print("Imperfect passive indicative of " + infinitive + ": ")
    imperfPassEnds(stem1, num1, stem)
    print("Future passive indicative of " + infinitive + ": ")
    futPass(stem1, num1, stem)
    print("Perfect passive indicative of " + infinitive + ": ")
    perfPass(part1, num1)
    print("Pluperfect passive indicative of " + infinitive + ": ")
    pluperfPass(part1, num1)
    print("Future perfect passive indicative of " + infinitive + ": ")
    futPerfPass(part1)

    print(" ")

    print("Present active subjunctive of " + infinitive + ": ")
    presSub(stem)
    print("Imperfect active subjunctive of " + infinitive + ": ")
    imperfSubEnds(infinitive, num1)
    print("Perfect active subjunctive of " + infinitive + ": ")
    perfSub(perfect1)
    print("Pluperfect active subjunctive of " + infinitive + ": ")
    pluperfSubEnds(perfect, num1)

    print("Present passive subjunctive of " + infinitive + ": ")
    presPassSub(stem)
    print("Imperfect passive subjunctive of " + infinitive + ": ")
    imperfPassSub(infinitive)
    print("Perfect passive subjunctive of " + infinitive + ": ")
    perfPassSub(part1)
    print("Pluperfect passive subjunctive of " + infinitive + ": ")
    pluperfPassSub(part1)

    print(" ")

    print("Present active participle of " + infinitive + ": ")
    presActPart(stem1)
    print("Perfect passive participle of " + infinitive + ": ")
    perfPassPart(part1)
    print("Future active participle of " + infinitive + ": ")
    futActPart(part1)
    print("Future passive participle of " + infinitive + ": ")
    futurePassPart(stem1)

    print(" ")

    print("Positive imperative -singular and plural- of " + infinitive + ": ")
    posImperative(stem1, pres)
    print("Negative imperative -singular and plural- of " + infinitive + ": ")
    negImperative(infinitive)

    print(" ")

    print("Present active infinitive of " + infinitive + ": ")
    print(infinitive)
    print("Perfect active infinitive of " + infinitive + ": ")
    perfActInfinitive(perfect)
    print("Future active infinitive of " + infinitive + ": ")
    futInfin(part1)
    print("Present passive infinitive of " + infinitive + ": ")
    presPassInfinitive(infinitive)
    print("Perfect passive infinitive of " + infinitive + ": ")
    perfPassInfin(part1)
    print("Future passive infinitive of " + infinitive + ": ")
    futPassInfin(part1)


printVerb(stem, stem1, perfect1, infinitive, num1, part1, participle, pres, perfect)
