
import sys
debug = True
# def biSearch(mapping, start, finish, x):
#     if start == finish:
#         return start
#     mid = int((start+finish)/2)
#     if mapping[mid] > x:
#         if mapping[mid-1]<x:
#             return mid-1
#         else:
#             return biSearch(mapping, start, mid-1, x)
#     elif mapping[mid] <x:
#         if mapping[mid+1]>x:
#             return mid+1
#         else:
#             return biSearch(mapping, mid+1, finish, x)
#     else: return mid

def biSearch(mapping, start, finish, x):
    if mapping[start]<=x and mapping[start+1]>=x:
        return start
    mid = int((start+finish)/2)
    if(start==finish or mid==start): return -1
    if mapping[mid] > x:
        return biSearch(mapping, start, mid, x)
    elif mapping[mid] <= x:
        return biSearch(mapping, mid, finish, x)

def main():
    
    with open(sys.argv[1],'r') as infile:
        lines = infile.read().splitlines()

    numBoxes = int(lines[0])
    boxWeights = sorted([float(x) for x in lines[1].split()])
    truckCapacities = [float(x) for x in lines[2:]]
    mapping = [sum(boxWeights[:i]) for i in range(numBoxes+1)]

    outputs = []

    for x in truckCapacities:
        #binary search
        if x >= mapping[-1]: outputs.append(numBoxes)
        elif x==0: outputs.append(0)
        else:
            outputs.append((biSearch(mapping, 0, numBoxes, x)))
    
    print(outputs)

    with open(sys.argv[1].split('.')[0] + '.out','w') as outfile:
        outfile.write("\n".join(map(str,outputs)))

    if debug == True:
        #print(lines)
        #print(numBoxes)
        print(boxWeights)
        print(truckCapacities)
        print(mapping)
            
if __name__ == "__main__":
    main()

