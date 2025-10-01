print("Farenheit to Celcius Converter:")
F=int(input("Enter the temperature (℉):"))
def convert_temp(F):
    C=(F-32)/1.8
    return C
print( F ,"℉ = ",convert_temp(F),"℃")