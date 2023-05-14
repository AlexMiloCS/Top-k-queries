import heapq
from decimal import Decimal
class round_robin:
    def __init__(self,R,path1,path2):
        self.R=R
        self.path1 = path1
        self.path2 = path2
        self.lower_bound = {}
        self.full_score = {}
        self.Wk = []


    def check_dicts(self,index1,index2,val1,val2,obj_counter):
        if index1 in self.lower_bound:
            self.full_score[index1]=self.lower_bound[index1]+val1
        else:                    
            self.lower_bound[index1]=val1+self.R[index1]
            obj_counter +=1
        if index2 in self.lower_bound:
            self.full_score[index2]=self.lower_bound[index2]+val2
        else:                  
            self.lower_bound[index2]=val2+self.R[index2]
            obj_counter +=1
        return obj_counter  

    def create_min_heap(self):
        for key, value in self.lower_bound.items():
            if key in self.full_score:
                true_value = self.full_score[key]
                self.Wk.append([key,true_value])
                continue
            self.Wk.append([key,value])
        


    def do_the_sequence(self,k):
        with open(self.path1, 'r') as file1, open(self.path2, 'r') as file2:
            obj_counter=0
            while obj_counter<10: 
                line1 = file1.readline()
                line2 = file2.readline()
                split_line1 = line1.split()
                split_line2 = line2.split()    
                val1 = float(split_line1[1]) 
                index1 = int(split_line1[0])
                val2 = float(split_line1[1])                 
                index2 = int(split_line2[0])
                obj_counter = self.check_dicts(index1,index2,val1,val2,obj_counter)
            self.create_min_heap() 
            print(self.Wk)
            heapq.heapify(self.Wk)
            print(self.Wk)           
        print(self.lower_bound)
        print(self.full_score)
            

                
