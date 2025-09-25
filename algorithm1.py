#precondition: 
#
# 'n' and integer that is the number of disks inside the disks variable
# 'disks' a list that has multiple strings that include either 'black' or 'white'
#
#postconditions:
#
# 'm' an integer that represents the number of swaps occured
# 'disks' a list that contains all the 'black' on one side and 'white' on the other side
def algo1(n, disks):
    
    m = 0 #number of swaps
    swapped = True #boolean that keeps track if the swap occured or not
    
    while swapped: #while loop that loops until no more swaps occured
        swapped = False #turn boolean to false for while loop to loop once at least
        
        for i in range(len(disks) - 1): #for loop to loop through the disks list left to right
            if disks[i] == "black" and disks[i+1] == "white": #if statement to check if the current index is black and next index is white
                disks[i], disks[i+1] = disks[i+1], disks[i] #swaps current index with next index and next index with current index
                
                
                m+=1 #increment the number of swaps occured
                swapped = True #boolean flag is now true
                
    
        for i in range(len(disks) - 2, -1, -1): #for loop to iterate through disks list right to left
            if disks[i] == "black" and disks[i+1] == "white": #if statement to check if the current index is black and next index is white
                disks[i], disks[i+1] = disks[i + 1], disks[i] #swaps current index with next index and next index with current index
                
                m+=1 #increment the number of swaps occured
                swapped = True #boolean flag is now true
    
    return m, disks #return number of swaps and current list
            
            
number = 8 #number of strings in disks
list_disks = ["black", "white", "black", "white", "black", "white", "black", "white"] #list of black and white disks
swaps, list_disks = algo1(number, list_disks) #initialize 'swaps' and 'list_disks' to whatever algo1() returns
print("number of swaps:", swaps) #print num of swaps
print()
print(list_disks)#print new list_disks
