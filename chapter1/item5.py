resultList = []
tempList = []
startIndex = 0
currentIndex = 0

def countdown(currentCount):
  global tempList
  global currentIndex
  
  if currentCount < len(inputList)-1:
    if inputList[currentCount+1] == inputList[currentCount]-1:
      tempList.append(inputList[currentCount])
      currentCount += 1
      countdown(currentCount)
    elif inputList[currentCount] == 1:
      tempList.append(inputList[currentCount])
      currentIndex = currentCount+1
    else:
      tempList = []
      currentIndex = currentCount+1
  elif currentCount == len(inputList)-1:
    if inputList[currentCount] == 1:
      tempList.append(inputList[currentCount])
      currentIndex = currentCount+1
    else:
      tempList = []
      currentIndex = currentCount+1

print("*** Fun with countdown ***")
print("Enter List : ", end = '')
inputList = [int(n) for n in input().split()]

while currentIndex < len(inputList):
  countdown(currentIndex)
  if len(tempList) > 0:
    resultList.append(tempList)
  tempList = []

total = len(resultList)
print([total, resultList])


# def countdown(list):
#     cnt = 0
#     total = []
#     merge = []

#     for item in list:
#         temp = []
#         if cnt < len(list) - 1:
#         #     if item == 1 or list[cnt+1] == item-1:
#         #         # print("stage1 item" + str(item))
#         #         temp.append(item)
#         #     else:
#         #         # print("stage2 item" + str(item))
#         #         temp.clear()
#             if item == 1:
#                 temp.append(item)
#             elif list[cnt+1] == item-1:
#                 temp.append(item)
#             else:
#                 temp.clear()
#         elif cnt == len(list)-1:
#             if list[cnt] == list[cnt-1]-1:
#                 temp.append(item)
#             else:
#                 temp.clear()
#         if len(temp) > 0 and temp[len(temp)-1] == 1:
#             total.append(temp)
#         cnt += 1
#     merge.append(len(total))
#     merge.append(total)
#     return merge

# print("*** Fun with countdown ***")
# print("Enter List : ", end = '')
# list = [int(n) for n in input().split()]
# print(countdown(list))

