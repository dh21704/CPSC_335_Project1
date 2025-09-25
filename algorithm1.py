def algo1(n, disks):
    
    m = 0 #number of swaps
    swapped = True
    
    while swapped:
        swapped = False
        
        for i in range(len(disks) - 1):
            if disks[i] == "black" and disks[i+1] == "white":
                disks[i], disks[i+1] = disks[i+1], disks[i]
                
                
                m+=1
                swapped = True
                
    
        for i in range(len(disks) - 2, -1, -1):
            if disks[i] == "black" and disks[i+1] == "white":
                disks[i], disks[i+1] = disks[i + 1], disks[i]
                
                m+=1
                swapped = True
    
    return m, disks
            
            
number = 8
list_disks = ["black", "white", "black", "white", "black", "white", "black", "white"]
swaps, list_disks = algo1(number, list_disks)
print("number of swaps:", swaps)
print()
print(list_disks)
