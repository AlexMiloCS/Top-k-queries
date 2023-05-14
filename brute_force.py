

class brute_force:
    def __init__(self,R,path1,path2):
        self.R = R
        self.path1 = path1
        self.path2 = path2

    def calc_all(self):
        with open(self.path1, 'r') as f:
             contents = f.read()
        lines = contents.splitlines()

        for i in range(len(lines)):
            split_line = lines[i].split()
            x=split_line[0]
            self.R[int(x)] += float(split_line[1])

        with open(self.path2, 'r') as f:
             contents2 = f.read()
        lines2 = contents2.splitlines()

        for i in range(len(lines2)):
            split_line2 = lines2[i].split()
            self.R[int(split_line2[0])] += float(split_line2[1])                  
        
        return self.R
    
