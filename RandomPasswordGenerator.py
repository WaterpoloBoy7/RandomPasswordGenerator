import random
import time
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print("Welcome to Random Password Generator.")
#print("You can choose between word-password and number-password.")
#mode =input("Which one w/N?: ")
#if mode == "N" or "n":
use = input("Do you want to repeat using the program? n/Y: ")
while use == "y" or "Y":
    mod = input("E[asy] or M[edium] or H[ard] to crack: ")

    if mod == "E":
        print("")
        print("This is a random password generator")
        print("")
        print("Use CAPITALS and non-capitals, numbers are random automated!")
        print("")
        name = input("Enter a word: ")
        print("")
        randy = random.randint(0, 2)
        if randy == 0:
            print("{0}{1}".format(name, (raise_to_power(random.randint(1, 6), random.randint(2, 6)))))
            print("")
        else:
            remy = random.randint(0, 120)
            print("{0}{1}".format(name, remy))
        print("")
        print("Your new password")
        print("")
        time.sleep(100000)

    elif mod == "M":
        print("")
        print("This is a random password generator")
        print("")
        print("Use CAPITALS and non-capitals, numbers are random automated!")
        print("")
        name = input("Enter a word: ")
        print("")
        randy = random.randint(0, 2)
        if randy == 0:
            print("{0}{1}".format(name, (raise_to_power(random.randint(1, 11), random.randint(2, 20)))))
            print("")
        else:
            remy = random.randint(10, 10000)
            print("{0}{1}".format(name, remy))
        print("")
        print("Your new password")
        print("")
        time.sleep(10)

    elif mod == "H":
        print("")
        print("This is a random password generator")
        print("")
        print("Use CAPITALS and non-capitals, numbers are random automated!")
        print("")
        name = input("Enter a word: ")
        print("")
        randy = random.randint(0, 2)
        if randy == 0:
            print("{0}{1}".format(name, (raise_to_power(random.randint(1, 92), random.randint(2, 100)))))
            print("")
        else:
            remy = random.randint(10000, 1000000000)
            print("{0}{1}".format(name, remy))
        print("")
        print("Your new password")
        print("")

if use == "n" or "N":
    mod = input("E[asy] or M[edium] or H[ard] to crack: ")

    if mod == "E":
        print("")
        print("This is a random password generator")
        print("")
        print("Use CAPITALS and non-capitals, numbers are random automated!")
        print("")
        name = input("Enter a word: ")
        print("")
        randy = random.randint(0, 2)
        if randy == 0:
            print("{0}{1}".format(name, (raise_to_power(random.randint(1, 6), random.randint(2, 6)))))
            print("")
        else:
            remy = random.randint(0, 120)
            print("{0}{1}".format(name, remy))
        print("")
        print("Your new password")
        print("")
        time.sleep(100000)

    elif mod == "M":
        print("")
        print("This is a random password generator")
        print("")
        print("Use CAPITALS and non-capitals, numbers are random automated!")
        print("")
        name = input("Enter a word: ")
        print("")
        randy = random.randint(0, 2)
        if randy == 0:
            print("{0}{1}".format(name, (raise_to_power(random.randint(1, 11), random.randint(2, 20)))))
            print("")
        else:
            remy = random.randint(10, 10000)
            print("{0}{1}".format(name, remy))
        print("")
        print("Your new password")
        print("")
        time.sleep(10)

    elif mod == "H":
        print("")
        print("This is a random password generator")
        print("")
        print("Use CAPITALS and non-capitals, numbers are random automated!")
        print("")
        name = input("Enter a word: ")
        print("")
        randy = random.randint(0, 2)
        if randy == 0:
            print("{0}{1}".format(name, (raise_to_power(random.randint(1, 92), random.randint(2, 100)))))
            print("")
        else:
            remy = random.randint(10000, 1000000000)
            print("{0}{1}".format(name, remy))
        print("")
        print("Your new password")
        print("")
        time.sleep(100000)
        exit()
#elif mode == "W" or "w":
    word_list1 = [
        [antidynasty,
        alkyne,
        alehouses,
        auge,
        airway,
        amphiaraus,
        acrolein,
        antiatheism,
        ameboid,
        artisanal,
        aryan,
        antiquaries,
        altai,
        antliliae,
        angelica,
        ailurophilic,
        acidimetric,
        alum,
        asherah,
        appositionally,
        alayne,
        arleen,
        atrocity,
        acidly,
        apsidally,
        acenesthesia,
        alfa,
        allheal,
        animalization,
        actinon,
        arthropodal,
        amber,
        actinodermatitis,
        achromate,
        affined,
        autobiography,
        ablepsia,
        allergen,
        aldous,
        amu,
        acockbill,
        analyst,
        abbey,
        anthropophagite,
        acerous,
        armiger,
        adessive,
        ascomycete,
        ananias,
        affectingly,
        apophonic,
        attributing,
        abominableness,
        agriology,
        alburnous,
        amphigoric,
        am,
        awner,
        ampullula,
        antipestilential,
        affreight,
        apelles,
        auroral,
        aias,
        appoggiaturas,
        adventitiousness,
        apparently,
        allegorical,
        amap,
        anchorless,
        adv,
        ansate,
        ado,
        appointer,
        amboceptor,
        anticorrosiveness,
        accoucheuse,
        anhidrosis,
        abjectedness,
        annulate,
        argumentative,
        apriorism,
        amblingly,
        amagasaki,
        amphisbaenid,
        ablaut,
        adjudicative,
        anabatic,
        anathematic,
        annihilation,
        antic,
        alibi,
        ashake,
        amorality,
        ametropic,
        acocotl,
        abrogated,
        albigensian,
        axinomancy,
        autarchically,

    burgenland,
    brassier,
    banshee,
    bloke,
    blindly,
    benefit,
    bibliophily,
    ballast,
    bivalent,
    bood,
    bruja,
    barchan,
    beachless,
    borneo,
    bordered,
    blurt,
    bitterly,
    bladder,
    bushel,
    broach,
    bryant,
    biotypic,
    bezant,
    baetyl,
    bransle,
    bondless,
    brahmanee,
    biadice,
    bressummer,
    bioluminescence,
    bola,
    beggiatoa,
    beneficiary,
    belcher,
    bolshevistically,
    brattle,
    block,
    beardlessness,
    burlesque,
    bishopbird,
    bowenite,
    barroom,
    bluebird,
    bisect,
    brecknockshire,
    bootlegged,
    brisket,
    bromius,
    bier,
    bestiarist,
    bronzy,
    brasque,
    brahmanism,
    banecroft,
    barthianism,
    blarney,
    bundle,
    befog,
    bicornate,
    bestializing,
    balthazar,
    bardolater,
    blockiest,
    boleti,
    baronetize,
    bacchii,
    basset,
    belt,
    briarroot,
    boxball,
    babette,
    basest,
    buchanan,
    bedmaking,
    bowl,
    bloodier,
    beehive,
    boatload,
    barefooted,
    borg,
    buries,
    bayam,
    becomingly,
    braccio,
    bardy,
    brevard,
    backdown,
    bilboes,
    brassiest,
    binnacle,
    buckler,
    biak,
    bruteness,
    bucolically,
    brainwork,
    biot,
    bridey,
    borak,
    beheadal,
    bustard,


            eternised,
        ectosarcous,
        exultation,
        eutaxy,
        eminescu,
        excoriate,
        exoergic,
        endolymph,
        everyday,
        esophageal,
        extension,
        endangeitis,
        epitheliomas,
        euphoric,
        evacuant,
        enlargeable,
        evocatively,
        establish,
        experiencer,
        epistemic,
        espy,
        emulsoidal,
        exaggeratory,
        eccl,
        erectly,
        electrothermal,
        epha,
        entoblastic,
        ephemeras,
        europeanize,
        erythroblastosis,
        encapsulation,
        errorless,
        erechtheus,
        errable,
        ethelee,
        eisenstadt,
        epigenous,
        expansionary,
        elamitic,
        expiration,
        empalement,
        etiquette,
        elt,
        ethicalness,
        ecru,
        explicative,
        esophagus,
        expansibility,
        expressage,
        elevs,
        easylike,
        electrocuting,
        emunctory,
        exch,
        eunuchized,
        elasticized,
        exclamational,
        epoch,
        encapsule,
        etymologizing,
        expiscatory,
        epexegetic,
        effervesced,
        epirogeny,
        evangelizer,
        exultingly,
        euplotid,
        epistolise,
        esculent,
        elisabeth,
        exerciser,
        enddamaged,
        enigmas,
        erective,
        electrovalent,
        erie,
        expeditionary,
        espaol,
        equilateral,
        effeminization,
        entablement,
        escapeless,
        enfeoff,
        ecclesiology,
        ecotype,
        envoi,
        esrog,
        ebonist,
        exor,
        epididydidymides,
        emilio,
        episematic,
        equably,
        embarrassedly,
        ermalinda,
        excommunicated,
        extinctive,
        elutriate,
        exclusivity,
        ]
    ]
    rand = random.randint(0,301)
    print(word_list1[rand])
    print("Your new password!")
else:
    print("You have an error or the program has ended, you can rerun the program!")
    rate = input("Do you want to rate the program?: ")
    if rate == "y" or "Y" or "yes" or "Yes":
        rating = input("A[super] | B[really good] | C[good] | D[bad] | E[really bad]?: ")
    else:
        exit()