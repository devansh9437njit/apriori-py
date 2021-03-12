def getUniqueItems(values:list):
    items = set()
    for row in values:
        for item in row:
            items.add(item)

    return list(items)


def readFile(filename):
    file = open(filename)

    values = []
    for i in file.readlines():
        line = i
        line = line.strip()
        line = line.replace(" ","")
        line = line.replace("\t","")
        values.append(line.split(","))

    file.close()
    return values


def support(item, values):
    count = 0
    for row in values:
        if item in row:
            count+=1
    
    support = count/len(values)
    # support *= 100
    # support = int(support)

    return support

def getSets(uniqueItems):

    sets = []

    l = len(uniqueItems)
    for i in range(l):
        for j in range(l):
            if i!=j:
                sets.append([uniqueItems[i], uniqueItems[j]])

    return sets


def confidence(itemPair, values):
    a, b = itemPair
    
    count = 0
    for row in values:
        if a in row and b in row:
            count += 1

    bSupport = support(b, values)
    conf = float(count/bSupport)
    conf = round(conf, 2)

    return conf



def lift(itemPair, values):
    conf = confidence(itemPair, values)
    supp = support(itemPair[1], values)

    return round(conf/supp,2)


def dataSetStats(values):
    items = 0
    for i in values:
        items += len(i)

    transactions = len(values)

    print("------------------------")
    print("---Dataset Statistics---")
    print("------------------------")
    print("Number of transactions: " + str(transactions))
    print("Number of total items: " + str(items))
