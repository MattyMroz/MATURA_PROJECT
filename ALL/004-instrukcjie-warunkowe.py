light = input("Jakie jest światło? (red, green, yellow) ")
if str(light).startswith("r"):
    print("Czekaj!")
elif light == 'yellow':
    print("Przygotuj się!")
elif light == 'green':
    print("Jedź!")
else:
    print("Niewłaściwa wartość")

print("Czekaj!" if light == 'red' else "Przygotuj się!" if light == 'yellow' else "Jedź!" if light == 'green' else "Niewłaściwa wartość")

# zalecane przedziały, możliwość zagnieżdżania, możliwość wykorzystania w jednej linii