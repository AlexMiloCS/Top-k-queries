import heapq
class round_robin:
    def __init__(self,R,path1,path2):
        self.R=R
        self.path1 = path1
        self.path2 = path2
        self.lower_bound = {}
        self.full_score = {}

    def do_the_sequence(self,k):
        with open(self.path1, 'r') as file1, open(self.path2, 'r') as file2:
            obj_counter=0
            while obj_counter<10: 
                line1 = file1.readline()
                line2 = file2.readline()
                split_line1 = line1.split()
                split_line2 = line2.split()               
                if split_line1[0] in self.lower_bound:
                    self.full_score[split_line1[0]]=self.lower_bound[split_line1[0]]+float(split_line1[1])
                else:
                    print((split_line1[1]),self.R[int(split_line1[0])])
                    self.lower_bound[split_line1[0]]=float(split_line1[1])+self.R[int(split_line1[0])]
                    obj_counter +=1
                if split_line2[0] in self.lower_bound:
                    self.full_score[split_line2[0]]=self.lower_bound[split_line2[0]]+float(split_line2[1])
                else:
                    print((split_line2[1]),self.R[int(split_line2[0])])
                    self.lower_bound[split_line2[0]]=float(split_line1[1])+self.R[int(split_line2[0])]
                    obj_counter +=1
            
        print(self.lower_bound)
        print(self.full_score)
            

                
