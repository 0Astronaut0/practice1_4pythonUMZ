#amirhossein askari
#40213160281828
def toFaren(i):
    Faren = (i * 1.8) + 32
    return Faren
def toCel(i):
    Cel = (i - 32)/1.8
    return Cel
temp = int(input("type the temperture: "))
select = input("for celsius to farenheit type F || farenheit to celsius type C: ")
if(select == 'F'):
    res = toFaren(temp) 
elif(select == 'C'):
    res = toCel(temp)
print(res)