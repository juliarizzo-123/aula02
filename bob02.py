def med02(x,y):
    z=((x + y)/2)
    print('A media é: {}'.format(z))
    print('~'*20)
    return z
def med():
    print('Escolha dois numeros e veja sua media aritimetica!')
    
    x=int(input('digite um numero: '))
    y=int(input('digite um numero: '))
  
    z=((x + y)/2)
    print('A media é: {}'.format(z))
    print('~'*20)
    return z
    

#med()
#med()
#med()
#a = med()
#b = med()
#c = med()
#print(" {0} \n {1} \n {2}".format(a,b,c))
a=int(input('digite um numero: '))
b=int(input('digite um numero: '))
c=med02(a,b)