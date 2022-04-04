class OSes:
    def __init__(self,display,processor,ram,memory):
        self.display=display
        self.processor=processor
        self.ram=ram
        self.memory=memory
    def function(self):
        print("Display:"+self.display)
    def function1(self):
        print("Processor:"+self.processor)
    def function2(self):
        print("Ram:"+self.ram)
    def function3(self):
        print("Memory:"+self.memory)
    #object
windows=OSes("16 inches","Intel Core i5","8 GB","512 GB")
mac=OSes("16 inches","A1 chip","6 GB","1 TB")
linux=OSes("14 inches","unknown","4 GB","256 GB")
print(windows.function())
print(mac.function1())
print(linux.function3())
print(windows.function2())