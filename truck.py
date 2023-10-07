
import sys
debug = False

#this one might be easier to explain
def biSearch(mapping, start, finish, x):
    if mapping[start]<= x < mapping[start+1]:
        return start
    mid = int((start+finish)/2)
    if mapping[mid] > x:
        return biSearch(mapping, start, mid, x)
    elif mapping[mid] < x:
        return biSearch(mapping, mid, finish, x)
    else: return mid
    
# def biSearch(mapping, low, high, x):
#     if low >= high:
#         if x >= mapping[low]: return low
#         else: return low-1
#     mid = int((low+high)/2)
#     if mapping[mid] > x:
#         return biSearch(mapping, low, mid-1, x)
#     elif mapping[mid] < x:
#         return biSearch(mapping, mid+1, high, x)
#     else: return mid

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
    
    with open(sys.argv[1].split('.')[0] + '.out','w') as outfile:
        outfile.write("\n".join(map(str,outputs)))

    if debug:
        #print(lines)
        #print(numBoxes)
        #print(boxWeights)
        # print(truckCapacities)
        # print(mapping)
        # print(outputs)
        #print ("done. total lines outputted: " + str(len(outputs)))
        pass
            
if __name__ == "__main__":
    main()

