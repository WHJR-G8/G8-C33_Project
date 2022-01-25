class Bus():
    
    def __init__(self, pass_no, fare):
        self.pass_no = pass_no
        self.fare = fare
        
    def revenue(self):
        income = 30 * self.pass_no * self.fare
        print("The monthly income is : ", income)

bus = Bus(50,100)
bus.revenue()
