class BMICalc:
    def __init__(self, data):
        self.data = data
        
    def calculator(self, h, w):
        h = round(float(h / 100), 2)
        return round(float(w / (h * h)), 1)
    
    def healthRisk(self):
        count = self.helperBmi()
        print("total number of overweight person are : {}".format(count))
        
    def helperBmi(self):
        count = 0
        for i in range(len(self.data)):
            height = self.data[i]['HeightCm']
            weight = self.data[i]['WeightKg']
            val = self.calculator(height, weight)
            if val >= 25.0 and val <= 29.9:
                count += 1
        return count
            
            