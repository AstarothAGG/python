altura = float(input ('Qual sua altura?'))
peso = float(input('Qual seu peso?'))

IMC = peso / (altura/100)**2

print(IMC)

if IMC < 18.5:
  print(f'Seu IMC é de {IMC}, e é classicado como magreza! Vai comer filho da puta!')

elif IMC >= 18.5 and IMC < 24.9:
    print(f'Seu IMC é de {IMC}, e é classicado como normal! Vai comer seu frango!')

elif IMC >= 25.0 and IMC < 29.9:
    print(f'Seu IMC é de {IMC}, e é classicado como sobrepeso! Ta ficando gordo!')

elif IMC >= 30.0 and IMC < 39.9:
    print(f'Seu IMC é de {IMC}, e é classicado como obesidade! Tá bolota hein!')

else:
    print(f'Seu IMC é de {IMC}, e é classicado como OBESIDADE GRAVE! TU VAI MORRER!')