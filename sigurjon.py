def Set_game():
    collect = []
    num= row*column
    for i in range(row):
        collect.append([])
        for letter in range(column):
            collect[i].insert(0, num)
            num -= 1
    return collect

start_game = input("Input dimension of the board:")

row = int(start_game)
column = int(start_game)

The_list = Set_game()
The_list.sort()
print(The_list)

#########################################################
#HÉR KEMUR INPUTIÐ
X_postion = int(input("X position:"))
#O_position = input("O position:")

#Hvernig á að prenta út:
print("How to print out position [1][1] in the list",The_list[1][1])

#X = -100

###############################################################
#FIND INDEX OF A LIST
def index_of_an_list(mylist, char):
    for under_list in mylist:
        if char in under_list:
            return (mylist.index(under_list), under_list.index(char))

Find_index = (index_of_an_list(The_list,X_postion))
print(Find_index)
#lenght = len(Find_index)
first_index_taken = (Find_index[0])    #hér er búið að leita að tölunni og finna indexinn þ.e.a.s fyrri
second_index_taken = (Find_index[1])   #hér er búið að leita að tölunni og finna indexinn þ.e.a.s seinni

print(The_list[first_index_taken][second_index_taken])  #hér ætti talan að prentast út    FUNDINN



#Listed_index = list(Find_index)
#print(Listed_index)
######################################################
#SET X wher it belongs or replace
The_list[first_index_taken][second_index_taken] = "X"
print(The_list)