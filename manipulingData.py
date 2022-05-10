# Importations

# Definitions
def initData(fileToRead) :
    """Reads the data in the "data.txt" file, which includes the user's level and more. 
    fileToRead possible values : 'userdata.txt', or 'achievements.txt'."""
    with open(fileToRead, encoding = 'utf-8') as f :
        pass
    printVal = 1
    return printVal

def printingData (printVal) :
    """Prints all the data to be shown to the user depending on the "printVal" value.
    0 = null; 1 = init; 2 = level up"""
    if printVal == 0 :
        pass
    elif printVal == 1 :
        pass
    elif printVal == 2 :
        pass

def levelUp(newLvl) :
    """Reads the data in the "data.txt" file, then updates it to the new user's level.
    Tells the user he leveled up in life."""
    with open ('data.txt', encoding='utf-8') as f :
        pass
    with open ('data.txt', 'w', encoding='utf-8') as f :
        pass
    print ('You just leveled up to level', newLvl, '!')
    printVal = 2
    return printVal