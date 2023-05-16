#AM 3045 ONOMA: ALEXANDROS MILONAKIS
import heapq
from decimal import Decimal
class round_robin:
    def __init__(self,R,path1,path2,k):
        self.R=R
        self.k=k
        self.path1 = path1
        self.path2 = path2
        self.lower_bound = {}
        self.full_score = {}
        self.val1 = 0
        self.val2= 0
        self.sequential_accesses = 0
        self.Wk = []



    def check_dicts(self,index,val,file_index):
        if file_index == 1:
            self.val1 = val
        else:
            self.val2 = val
        if index in self.lower_bound:
            self.full_score[index]=self.lower_bound[index][0]+val
            del self.lower_bound[index]
            in_full_score = True
        else:         
            lower_bound = val+self.R[index]         
            self.lower_bound[index]= [lower_bound,file_index]
            in_full_score=False
        return in_full_score

    def split_line(self,line):
        split_line = line.split()   
        val = Decimal(split_line[1]) 
        index = int(split_line[0])
        return index,val
          

    def create_min_heap(self):
        for key, value in self.lower_bound.items():
            self.Wk.append([value[0],key])
        if len(self.full_score)>0:
            for key , value in self.full_score:
                self.Wk.append([value,key])

    
    def check_heap(self,index):
        heapq.heapify(self.Wk)
        if index in self.full_score:
            value = self.full_score[index]
        else:
            value = self.lower_bound[index][0]
        if self.Wk[0][0] < value:
            heapq.heappop(self.Wk)
            heapq.heappush(self.Wk,[value,index])

    def check_loop(self):
        threshold_T = self.val1 + self.val2 + 5
        if threshold_T > self.Wk[0][0]:
            return True
        elif len(self.lower_bound)>0: 
            for key,value in self.lower_bound.items():                
                if value[1] == 1:
                    if self.Wk[0][0] < value[0]+self.val2:
                        return True
                if value[1] == 2:
                    if self.Wk[0][0] < value[0]+self.val1:
                        return True
        return False

    def do_the_sequence(self):
        obj_counter = 0
        file_index = 1
        with open(self.path1, 'r') as file1, open(self.path2, 'r') as file2:
            while obj_counter<self.k: 
                if file_index == 1:
                    line = file1.readline()
                    if not line:
                        line = file2.readline()
                        if not line:
                            break
                    file_index = 2
                else:
                    line = file2.readline()
                    if not line:
                        line = file1.readline()
                    file_index = 1
                index,val = self.split_line(line)
                in_full_score =self.check_dicts(index,val,file_index)
                if not in_full_score:
                    obj_counter+=1
                self.sequential_accesses +=1
            self.create_min_heap()  

            while self.check_loop():
                if file_index == 1:
                    line = file1.readline()
                    if not line:
                        line = file2.readline()
                        if not line:
                            break
                    file_index = 2
                else:
                    line = file2.readline()
                    if not line:
                        line = file1.readline()
                        if not line:
                            break
                    file_index = 1
                index,val = self.split_line(line)
                self.check_dicts(index,val,file_index)
                self.check_heap(index)   
                self.sequential_accesses +=1           
        return self.Wk
    
    def get_sequential_accesses(self):
        return self.sequential_accesses

                


                
