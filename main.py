import sys
from file_manager import file_manager
from brute_force import brute_force
from round_robin import round_robin

#AM 3045 ONOMA: ALEXANDROS MILONAKIS

arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
arg4 = sys.argv[4]

#my input:
#"C:\\Users\\Alekos\\Desktop\\projects\\Diaxeirisi\\assignment3\\rnd.txt" "C:\\Users\\Alekos\\Desktop\\projects\\Diaxeirisi\\assignment3\\seq1.txt" "C:\\Users\\Alekos\\Desktop\\projects\\Diaxeirisi\\assignment3\\seq2.txt"
manager1 = file_manager(arg1)
R = manager1.create_structure()


round1 = round_robin(R,arg2,arg3,int(arg4))
Wk = round1.do_the_sequence()
Wk.sort(reverse=True)
print("Number of sequential accesses= ",round1.get_sequential_accesses())
print("Top k objects:")
for i in range(len(Wk)):
    print("{}: {}".format(Wk[i][1],Wk[i][0]))


brute_force1 = brute_force(R,arg2,arg3)
R_brute = brute_force1.calc_all()
R_brute.sort(reverse=True)
print("Brute force Top k objects:")
for i in range(int(arg4)):
    print("{}: {}".format(R_brute[i][1],R_brute[i][0],))
