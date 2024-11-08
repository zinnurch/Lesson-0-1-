grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(students)
list_students=(list(students))
print(list_students)
list_students.sort()
print(list_students)
sum_1st=sum(grades[0])
print(sum_1st)
len_1st=len(grades[0])
print(len_1st)
Aaron=sum_1st/len_1st
print(Aaron)
Bilbo=sum(grades[1])/len((grades[1]))
Johnny=sum(grades[2])/len((grades[2]))
Khendrik=sum(grades[3])/len((grades[3]))
Steve=sum(grades[4])/len((grades[4]))
print(Khendrik, Steve)
median_bal={}
median_bal["Aaron"]=Aaron
median_bal["Bilbo"]=Bilbo
median_bal[Johnny]=Johnny
median_bal["Khendrik"]=Khendrik
median_bal["Steve"]=Steve
print(median_bal)