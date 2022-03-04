from flask import Flask, jsonify
app=Flask(__name__)

@app.route('/formulas/<string:numeros>')
def resultados(numeros):
    listanumeros = getLista(numeros.split('-'))

    return jsonify({"Media": media(listanumeros),
    "Moda":moda(listanumeros), "Mediana":mediana(listanumeros),
    "Rango":rango(listanumeros), "Varianza":varianza(listanumeros),
    "DesviaciónEstandar":desviacion(listanumeros)})

def getLista(numeros):
    lista=[]
    for n in numeros:
        lista.append(int(n))
    return lista

def media(numeros):
    suma=0
    for n in numeros:
        suma+=n
    return suma/len(numeros)

def moda(numeros):
    lista = {}
    for n in numeros:
        if n in lista:
            lista[n]+=1
        else:
            lista[n]=1
    maxi=0
    index=0        
    for i,j in lista.items():
        if maxi<j:
            maxi=j
            index=i
    return index

def mediana(numeros):
    numeros.sort()
    mediana=0
    index=0
    if len(numeros)%2==0:
        index=int((len(numeros)-1)/2)
        mediana=(numeros[index]+numeros[index+1])/2
    else:
        index=int((len(numeros)-1)/2)
        mediana=numeros[index]
    return mediana

def rango(numeros):
    return max(numeros)-min(numeros)

def varianza(numeros):
    promedio=media(numeros)
    varResultado=0
    for n in numeros:
        varResultado+=(n-promedio)*(n-promedio)
    return varResultado/len(numeros)

def desviacion(numeros):
    return varianza(numeros)**(0.5)

if __name__ == '__main__':
    app.run(debug=True)