class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        arr=[]
        if celsius <0:
            return False
        else:
            kelvin=celsius+273.15
            Fahrenheit =celsius*1.80 +32.00
            arr.append(kelvin)
            arr.append(Fahrenheit)
        return arr