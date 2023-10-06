
import sys
debug = True
def biSearch(mapping, start, finish, x):
    if start == finish:
        return start
    mid = int((start+finish)/2)
    if mapping[mid] > x:
        if mapping[mid-1]<x:
            return mid-1
        else:
            return biSearch(mapping, start, mid-1, x)
    elif mapping[mid] <x:
        if mapping[mid+1]>x:
            return mid+1
        else:
            return biSearch(mapping, mid+1, finish, x)
    else: return mid
def main():
    
    with open(sys.argv[1],'r') as infile:
        lines = infile.read().splitlines()

    numBoxes = int(lines[0])
    boxWeights = sorted([float(x) for x in lines[1].split()])
    truckCapacities = [float(x) for x in lines[2:]]
    mapping = [sum(boxWeights[:i]) for i in range(len(boxWeights)+1)]

    outputs = []

    for x in truckCapacities:
        #binary search
        if x >= mapping[-1]: outputs.append(len(mapping)-1)
        elif x==0: outputs.append(0)
        else:
            lower = 0
            upper = len(mapping)-1

            outputs.append((biSearch(mapping, 0, len(mapping), x)))
    
    print(outputs)

    if debug == True:
        print(lines)
        print(numBoxes)
        print(boxWeights)
        print(truckCapacities)
        print(mapping)
            
if __name__ == "__main__":
    main()

