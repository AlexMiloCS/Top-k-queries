import sys
from file_manager import file_manager
from brute_force import brute_force
import heapq

"""
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
"""
"C:\\Users\\Alekos\\Desktop\\projects\\Diaxeirisi\\assignment3\\rnd.txt"
manager1 = file_manager("C:\\Users\\Alekos\\Desktop\\projects\\Diaxeirisi\\assignment3\\rnd.txt")

R = manager1.create_structure()
brute_force1 = brute_force(R,"C:\\Users\\Alekos\\Desktop\\projects\\Diaxeirisi\\assignment3\\seq1.txt","C:\\Users\\Alekos\\Desktop\\projects\\Diaxeirisi\\assignment3\\seq2.txt")
values = brute_force1.calc_all()
greatest_indices = heapq.nlargest(10, range(len(values)), key=values.__getitem__)

# Sort the indices in a heap ordered from bigger to smaller
heap = [(values[i], i) for i in greatest_indices]
heapq.heapify(heap)
sorted_indices = [heapq.heappop(heap)[1] for _ in range(len(heap))]

# Print the sorted indices
print(sorted_indices)

