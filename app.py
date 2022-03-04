
from flask import Flask, jsonify, request

app = Flask(__name__)

from medidas import medidas


@app.route('/medidas',methods=['GET'])
def getMedida():
    n1 = float(request.args.get('n1'))
    n2 = float(request.args.get('n2'))
    n3 = float(request.args.get('n3'))
    n4 = float(request.args.get('n4'))

    n5 = (((n1*n2*n3)/12)*4.5)*n4
    return jsonify({"resultado": n5})    


if __name__ == '__main__':
    app.run(debug=True)

