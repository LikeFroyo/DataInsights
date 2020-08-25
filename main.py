import csv
dataMap = {}
with open("data.txt", 'r') as csvFile:
  csvRead = csv.reader(csvFile)
  next(csvRead)
  for dataRow in csvRead:
    key = dataRow[0].split('-')[1]
    dataMap.setdefault(key,[])
    dataMap[key].append(dataRow)

#Question 1 Total Sales Of The Stores
def TotalResult(dataMap):
  totalSales = 0
  for monthKey in dataMap.keys():
    for monthDataRow in dataMap[monthKey]:
      totalSales += int(monthDataRow[4])
  print("Total Sales: "+str(totalSales))
  print("----------------------------------------------\n")

#Question 2 Month Wise Sales Total
def MonthWiseTotal(dataMap):
  for monthKey in dataMap.keys():
    monthTotalSales = 0
    for monthDataRow in dataMap[monthKey]:
      monthTotalSales += int(monthDataRow[4])
    print("Monthly Sales for "+monthKey+": "+str(monthTotalSales))
  print("----------------------------------------------\n")

#Question 3 Most Popular Item In Each Month
def MostPopularItemInEachMonth(dataMap):
  for monthKey in dataMap.keys():
    dataItemMap = {}
    for monthDataRow in dataMap[monthKey]:
      key = monthDataRow[1]
      dataItemMap.setdefault(key,0)
      dataItemMap[key] += int(monthDataRow[3])

    ansKey = ""
    max = 0
    for itemKey in dataItemMap.keys():
      if(dataItemMap[itemKey]>=max):
        max = dataItemMap[itemKey]
        ansKey = itemKey
    print("For "+monthKey+" :"+ ansKey +" :"+ str(max))
  print("----------------------------------------------\n")

#Question 4 Most Revenue Generating Each Month
def MostRevenueItemInEachMonth(dataMap):
  for monthKey in dataMap.keys():
    dataItemMap = {}
    for monthDataRow in dataMap[monthKey]:
      key = monthDataRow[1]
      dataItemMap.setdefault(key,0)
      dataItemMap[key] += int(monthDataRow[4])

    ansKey = ""
    max = 0
    for itemKey in dataItemMap.keys():
      if(dataItemMap[itemKey]>=max):
        max = dataItemMap[itemKey]
        ansKey = itemKey
    print("For "+monthKey+" :"+ ansKey +" :"+ str(max))
  print("----------------------------------------------\n")

#Most Popular With min, max & avg
def MostPopularItem(data):
  dataItemMap = {}
  dayDataMap = {}
  for monthKey in dataMap.keys():
    for monthDataRow in dataMap[monthKey]:
      key = monthDataRow[1]
      dataItemMap.setdefault(key,0)
      dataItemMap[key] += int(monthDataRow[3])

      dayDataMap.setdefault(monthKey,{})
      dayKey = monthDataRow[0].split('-')[2]
      dayDataMap[monthKey].setdefault(dayKey,[])
      dayDataMap[monthKey][dayKey].append(dataRow)

  ansKey = ""
  max = 0
  for itemKey in dataItemMap.keys():
    if(dataItemMap[itemKey]>=max):
      max = dataItemMap[itemKey]
      ansKey = itemKey
  print("Most Popular "+ ansKey +" :"+ str(max))


  for monthKey in dayDataMap.keys():
    minPerMonth = max+1
    maxPerMonth = -1
    for dayKey in dayDataMap[monthKey].keys():
      for dayDataRow in dayDataMap[monthKey][dayKey]:
        itemCount = 0
        print(dayDataRow)
        if(dayDataRow[1]==ansKey):
          itemCount += 1
        minPerMonth = minPerMonth if minPerMonth < itemCount else itemCount
        maxPerMonth = itemCount if itemCount >= maxPerMonth else maxPerMonth
    print("Most Popular Min Value "+monthKey+" " +ansKey +" :"+ str(minPerMonth))
    print("Most Popular Max Value "+monthKey+" " + ansKey +" :"+ str(maxPerMonth))
  print("----------------------------------------------\n")

TotalResult(dataMap)
MonthWiseTotal(dataMap)
MostPopularItemInEachMonth(dataMap)
MostRevenueItemInEachMonth(dataMap)
MostPopularItem(dataMap)