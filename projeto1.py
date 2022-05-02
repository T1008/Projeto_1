produto = float(input('Insira o valor do seu produto: '));
parcelas = int(input('Insira o número de parcelas: '))

if (parcelas <= 0):
    print('Seu pagamento será a vista')
    
elif (parcelas <= 3): 
    X1 = produto*0.1;
    x2 = produto + X1;
    x3 = x2/parcelas
    print("Print o valor do seu produto é igual à:",x2,"\n o valor da parcela:",x3)