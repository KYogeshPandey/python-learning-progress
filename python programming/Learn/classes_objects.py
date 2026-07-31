class person:
    name = "Yogesh"
    occupation = "software developer"
    networth = 10
    def info(self):   #self means the current object
        print(f"{self.name} is a {self.occupation} with a net worth of {self.networth}")

a = person()
a.name = "shubham"
a.occupation = "data scientist"
# print(a.name,a.occupation,a.networth)
a.info()
