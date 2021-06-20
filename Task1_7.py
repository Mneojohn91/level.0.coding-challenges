list1= [11,21,33,15]
list2= [1,2,3,2]
#covert int list to string list
new_list1= map(str,list1)
new_list2= map(str,list2)
conv_list1 = (list(new_list1))
conv_list2 = (list(new_list2))

list3 = []
def combined_list(list3):
   #combining 2 lists in list 3
   for i in range(len(list1)):

      list3.append(conv_list1.pop(0))
      list3.append(conv_list2.pop(0))
      i = len(list3)
      if i == (len(list1)+len(list2)):
         list3 = list(map(int,list3))  # converting str list back to int list
         print (list3)




print()
combined_list(list3)
