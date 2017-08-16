import os.path

class Profile:
    def __init__(self):
        #The categories in the spending tracker are organized in a dictionary
        self.items = {'Food':0, 'Gas': 0, 'Shopping': 0}
        self.balance = 0
        
    def displayData(self):
        #Cycles through dictionary to display the categories with their costs
        #and percentage of total spending, as well as total spending itself
        dataDisplay = ""
        total = 0
        for value in self.items.values():
            total += value
        dataDisplay = "Total balance: $%.2f\n" % (self.balance)
        if total != 0:
            for key in self.items:
                dataDisplay += key+": $%.2f %.2f%%\n" % (self.items[key], (self.items[key]/total)*100)
        else:
            for key in self.items:
                dataDisplay += key+": $%.2f 0.00%%\n" % (self.items[key])
        dataDisplay += "Total spent: $%.2f\n" % (total)
        print(dataDisplay)
        return dataDisplay
    
    def updateItem(self,key, change):
        #Either adds or subtracts from a category
        if(key=="Balance"):
            self.balance += change
        else:
            self.items[key] += change
            self.balance -= change
            
    def newItem(self, key, value):
        self.items[key] = value
        self.balance -= value
        
    def delItem(self, key):
        if key in self.items:
            self.items.pop(key, None)
            
    def resetValues(self):
        for key in self.items:
            self.items[key] = 0
            
    def loadFile(self):
        dest = os.getcwd() + "\\"
        if not(os.path.isfile(dest+"memory.txt")):
            self.items = {'Food':0, 'Gas': 0, 'Shopping': 0}
            self.balance = 0
            with open("memory.txt", 'w') as f:
                f.write("Food 0\nGas 0\n Shopping 0\nBalance 0\n")
        else:
            with open("memory.txt", 'r') as f:
                self.items = {}
                self.balance = 0
                for line in f:
                    words = line.split()
                    if(words[0] == "Balance"):
                       self.balance = eval(words[1])
                    else:
                       key = words[0]
                       value = words[1]
                       self.items[key] = eval(value)
                       
    def saveFile(self):
        with open("memory.txt", 'w') as f:
            for key in self.items:
                    f.write(key + " " +str(self.items[key])+"\n")
        with open("memory.txt", 'a') as f:
            f.write("Balance "+str(self.balance) + "\n")
                       
    #For testing purposes, executes when this file is run.
    def run(self):
        print("Profile created")
        while(True):
            print("""Enter a number to make your choice.\n
    1. Create Category.\n
    2. Delete Category.\n
    3. Update Category.\n
    4. Update Balance.\n
    5. Display Data.\n
    6. Save File.\n
    7. Load File.\n
    8. Exit.\n""")
            self.choice = input("Your selection: ")
            if(self.choice=='1'):
                self.newKey = input("What is the name of the category? ")
                self.newValue = eval(input("What is the initial value of the category? "))
                self.newItem(self.newKey, self.newValue)
                print(self.newKey + " successfully created!")
            elif(self.choice=='2'):
                self.oldKey = input("What category would you like to delete? ")
                del self.items[self.oldKey]
                print(self.oldKey + " successfully deleted!")
            elif(self.choice=='3'):
                self.changedKey = input("Which category would you like to update? ")
                self.changedValue = eval(input("How much would you like to add?"
                                     " Place a negative sign to deduct. "))
                self.updateItem(self.changedKey, self.changedValue)
                print(self.changedKey + " successfully updated!")
            elif(self.choice=='4'):
                self.changedBal = eval(input("How much would you like to add?"
                                      " Place a negative sign to deduct. "))
                self.balance += self.changedBal
                print("$%d added to balance. Total is now $%d" % (self.changedBal, self.balance))
            elif(self.choice=='5'):
                self.displayData()
            elif(self.choice=='6'):
                self.saveFile()
            elif(self.choice=='7'):
                self.loadFile()
            elif(self.choice=='8'):
                break
            else:
                print("Invalid choice!")
        self.displayData()

if __name__ == "__main__":
    exc = Profile()
    exc.run()
