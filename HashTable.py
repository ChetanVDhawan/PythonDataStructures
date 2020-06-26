class Table:

    def __init__(self):
        self.table = []
        self.table= [[] for x in range(100)]

    def hashing_function(self,data):
        num = 0
        for c in data:
            num+=ord(c)
        num = int(num/10)
        return num



    def __setitem__(self, key, value):
        keyvaluelist = [key,value]
        position  = int(self.hashing_function(key))
        self.table[position].append(keyvaluelist)




    def __getitem__(self,key):
        position = self.hashing_function(key)
        for k,value in self.table[position]:
            if k == key:
                print(value)
                return
        print("Key Not Found")

    def print(self):
        count = 0
        for enrty in self.table:
            print(f'{count} : {enrty}')
            count+=1




if __name__ == "__main__":
    t1 = Table()
    t1["Chetan"]="1"
    t1["Dhawan"] ="2"
    t1.print()
    t1["Dhawan"]
    t1["Cashd"]


