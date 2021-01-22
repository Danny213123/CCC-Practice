InitialPosition = input()
EndPosition = input()
Battery = int(input())

list1 = InitialPosition.split()
list2 = EndPosition.split()

distanceAvenue = abs(int(list1[0]) - int(list2[0]))
distanceStreet = abs(int(list1[1]) - int(list2[1]))

totaldistance = int(distanceAvenue) + int(distanceStreet)

if (totaldistance > Battery):
  print ("N")
elif (Battery % 2 == 1 and totaldistance % 2 == 1):
  print("Y")
elif(Battery % 2 == 0 and totaldistance %2 == 0):
  print("Y")
elif(Battery % 2 == 1 and totaldistance % 2 == 0):
  print("N")
elif(Battery % 2 == 0 and totaldistance % 2 == 1):
  print ("N")
else:
  print ("N")
