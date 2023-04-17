from flask import Flask, request

app = Flask(__name__)

@app.route('/')


def exibir_numeros_primos():
    qtd = 100
    primos = [2]
    num = 3

    while len(primos) < 100:
        for p in primos:
            if num % p == 0:
                break
            else:
                primos.append(num)

            num += 2


    for p in primos:
        print(p,',')



