isFibonacci = int(input("Input number = "))
fibNum = 1
container1 = 0
container2 = 0
while fibNum < isFibonacci:
    container2 = container1
    container1 = fibNum
    fibNum = container1 + container2
if isFibonacci == fibNum:
    print(isFibonacci,"is a fibonacci number")
    print("Previous fibonacci number is", container1)
    container2 = container1
    container1 = fibNum
    fibNum = container1 + container2
    print("Next fibonacci number is", fibNum)
else:
    print(isFibonacci,"is not a fibonacci number")