import sys
from file_manager import file_manager
from brute_force import brute_force
from round_robin import round_robin


"""
arg0 = sys.argv[1]
arg1 = sys.argv[2]
arg2 = sys.argv[3]
arg3 = sys.argv[4]
"""
"C:\\Users\\Alekos\\Desktop\\projects\\Diaxeirisi\\assignment3\\rnd.txt"
manager1 = file_manager("C:\\Users\\Alekos\\Desktop\\projects\\Diaxeirisi\\assignment3\\rnd.txt")

R = manager1.create_structure()
#brute_force1 = brute_force(R,"C:\\Users\\Alekos\\Desktop\\projects\\Diaxeirisi\\assignment3\\seq1.txt","C:\\Users\\Alekos\\Desktop\\projects\\Diaxeirisi\\assignment3\\seq2.txt")
#R_brute = brute_force1.calc_all()

round1 = round_robin(R,"C:\\Users\\Alekos\\Desktop\\projects\\Diaxeirisi\\assignment3\\seq1.txt","C:\\Users\\Alekos\\Desktop\\projects\\Diaxeirisi\\assignment3\\seq2.txt")
round1.do_the_sequence(10)
