
class file_manager:
    def __init__(self,path):
        self.path = path
    
    def create_structure(self):
        R = []
        with open(self.path, 'r') as f:
            contents = f.read()
        lines = contents.splitlines()

        for i in range(len(lines)):
            split_line = lines[i].split()
            R.append(float(split_line[1]))
        return R