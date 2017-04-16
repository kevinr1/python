#Collatz    chapter 3 exercise
print ('Enter a number')

try:
    enteredNumber = int(input())
    
    
    def collatz(enteredNumber):
        while enteredNumber != 1:      
            if enteredNumber % 2 == 0:
                enteredNumber = (enteredNumber // 2)
                print(int(enteredNumber))
            
            elif enteredNumber % 2 == 1:
                enteredNumber = (enteredNumber * 3 + 1)
                print(int(enteredNumber))
                    

    collatz(enteredNumber)


except ValueError:
    print('Enter an interger only!')
    enteredNumber = int(input())
