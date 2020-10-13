import io                                                      #Using built in Python IO for dealing with Filez 
dictCommunities = {}                                           #Declare Community Dictionary (Blech! Globals)
finalList = []

def prepCommunityLookupTables():
#======================================================================
#Read communities file and build a really super cool dictionary thingy.
#======================================================================
    comFile = "g:/Community_resids.txt"                        #Point to community file
    resFile = "g:/apo-ner-diffP70.txt"
    with open(comFile, "r") as f:                              #Open file as Read
        line = f.readlines()                                   #Create a List of every single line
        q = 0
        while q < len(line):                                   #Loop through the list (Q Iterator) 
            if line[q].find(", ") > 0:                         #Make sure it contains comma's before splitting or go crashy.    
                r = line[q].split(", ")                        #Split comma seperated values into r
                s = 0                                          #Iterator for List of Comma Seperated Items (S)
                while s != len(r) :                            #Loop through comma seperated items
                    if r[s].find("-") >0:                      #Does the item contain a - (If so it's a Range)
                        t = r[s].split("-")                    #Break range into two pieces t[0] and t[1]
                        for u in range(int(t[0]),int(t[1])+1): #Dictionaries don't like RANGE. So we loop that too (sigh)
                            dictCommunities[u] = q + 1         #Add range to Dic, Return Val is community number
                        s+=1
                    else:
                        dictCommunities[int(r[s])] = q + 1     #It's not a range value, so just add it.
                        s +=1
            else:                                              #Pasta Alert : Does same as above, but antisocial groups with no comma.
                if line[q].find("-") >0:                       #Does the item contain a - (If so it's a Range)
                        
                        t = line[q].split("-")                 #Break range into two pieces t[0] and t[1]
                        for u in range(int(t[0]),int(t[1])+1): #Dictionaries don't like RANGE. So we loop that too (sigh)
                            dictCommunities[u] = q + 1         #Add range to Dic, Return Val is community number
                else:
                        dictCommunities[int(line[q])] = q + 1  #It's not a range value, so just add it.
                        s +=1
            q +=1
    with open(resFile, "r") as f:                              #Open file as Read
        line = f.readlines()                                   #Create a List of every single line
        q = 0
        print("==========================================")
        while q < len(line):                                   #Loop through Residue File
            t = line[q].split(" ")                             #Split each area into list
            isViable = 1                                       #Set new record to clean unless proven a dirty little record.
            tempA = int(t[1])                                  #Store Residue 1
            tempB = int(t[2])                                  #Store Reisude 2
            if dictCommunities.get(tempA,-1) == -1:
                isViable = 0                                   #Mark Dirty
            if dictCommunities.get(tempB,-1) == -1:
                isViable = 0                                   #Mark Dirty
            ansA = dictCommunities.get(tempA)
            ansB = dictCommunities.get(tempB)
            if ansA == ansB:
                isViable = 0                                   #Mark Dirty
            if isViable == 1:
                print(line[q])                                 #Record never got marked dirty. It's go time.
                finalList.append(line[q])
            q +=1
    with open('FinalOutput.txt', 'w') as fileHandle:
        for listitem in finalList:
            fileHandle.write('%s\n' % listitem)
    
    

def main():
#Because Main Functions es good!
    prepCommunityLookupTables()

if __name__ == "__main__":
#Ship out to Main Function
    main()