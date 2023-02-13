

def find_multiplication(n, positions):
    elements = [i for i in range(-n, n+1)]
    print(elements)
    product = 1
    for pos in positions:
        index = pos - 1
        if index < 0 or index >=len(elements):
            print(f"Error: position {pos} is out of range.")
            return None
        product *= elements[index]
    return product




n = int(input("Enter the value of N: "))
positions = list(map(int, input("enter the positions: ").strip().split()))
result = find_multiplication(n, positions)
if result is not None:
    print("the result of multiplication at the specified positions is: ", result)
    
