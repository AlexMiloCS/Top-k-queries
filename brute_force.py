#AM 3045 ONOMA: ALEXANDROS MILONAKIS

from decimal import Decimal


class brute_force:
    def __init__(self,R,path1,path2):
        self.R = R
        self.path1 = path1
        self.path2 = path2
        self.lower_bound = {}
        self.final_list = []

    def calc_all(self):
        with open(self.path1, 'r') as f:
             contents = f.read()
        lines = contents.splitlines()

        for i in range(len(lines)):
            split_line = lines[i].split()
            value = self.R[int(split_line[0])] + Decimal(split_line[1])
            self.lower_bound[int(split_line[0])]   =  value   

        with open(self.path2, 'r') as f:
             contents2 = f.read()
        lines2 = contents2.splitlines()

        for i in range(len(lines2)):
            split_line2 = lines2[i].split()
            self.R[int(split_line2[0])] += Decimal(split_line2[1])    
            value =  self.lower_bound[int(split_line2[0])] + Decimal(split_line2[1])            
            self.final_list.append([value,int(split_line2[0])])
        
        return self.final_list
    
