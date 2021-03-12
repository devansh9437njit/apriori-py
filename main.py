from utils import confidence, dataSetStats, getSets, getUniqueItems, readFile, support
# values = readFile("dataset2.csv")


def iterateDataset(values):
    uniqueItems = getUniqueItems(values)
    sets = getSets(uniqueItems)
    confidenceList = []
    supportList = []

    for item in uniqueItems:
        temp = support(item, values)
        if temp >= minSupp:
            supportList.append({"support": temp, "item": item})


    dataSetStats(values)

    print("\nSupport\n")
    if len(supportList) > 0:
        for item in supportList:
            print(f'Support: {item["support"]} \tItem Name: {item["item"]}')

    else:
        print("No items match minimmum support criterria")

    for item in sets:
        temp = confidence(item, values)
        if temp >= minConf:
            confidenceList.append({"conf": temp, "item": item})

    print("\nConfidence\n")
    if len(confidenceList) > 0:
        for item in confidenceList:
            print(f'Confidence: {item["conf"]}\t Itemset : {item["item"]}')

    else:
        print("No items match minimmum confidence criterria")



if __name__ == "__main__":

    numberOfDatasets = 4
    minConf = float(input("Enter minimum confidence: "))
    minSupp = float(input("Enter minimum support: "))

    for i in range(1, numberOfDatasets+1):
        print("\n\nDataset " + str(i)+":\n\n")
        values = readFile("dataset" + str(i) + ".csv")
        iterateDataset(values)
