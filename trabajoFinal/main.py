##file = open("read.py")

operadoresAritmeticos = {'++': 'suma', '--': 'resta', 'xx': 'multiplicacion', '//': 'division', '%%': 'division modular', '^^': 'exponencial'}
operadoresAritmeticos_key = operadoresAritmeticos.keys()

operadoresRelacionales = {'iguala': 'igual a', 'difa': 'diferente a', 'mayora': 'mayor a', 'mayoriguala': 'mayor o igual a', 'menora': 'menor a', 'menorigual': 'menor o igual a'}
operadoresRelacionales_keys = operadoresRelacionales.keys()

operadoresLogicos = {'yy': 'y', 'oo': 'o', 'no': 'no'}
operadoresLogicos_keys = operadoresLogicos.keys()

operadoresAsignacion = {'>': 'igual', '+>': '+=', '->': '-=', 'x>': '*=', '/>': '/=', '%>': '%='}
operadoresAsignacion_keys = operadoresAsignacion.keys()

data_type = {'ent': 'tipo integer', 'real': 'tipo real', 'cad': 'tipo cadena', 'char': 'tipo caracter'}
data_type_keys = data_type.keys()

simbolos_terminal_inicial = {'.,': 'Final', '&': 'Inicial'}
simbolos_terminal_inicial_keys = simbolos_terminal_inicial.keys()

palabrasReservadas = {'fol': 'ciclo for', 'elfe': 'ciclo else', 'il': 'if', 'ilelfe': 'ifelse', 'choose': 'case', 'cl': 'clase', 'inf': 'interfaz'}
palabrasReservadas_keys = palabrasReservadas.keys()

a = '''\
&a>1++2
x>a.,
14difa4.,
ent7.,
ent4.,
&5.,
'''

count = 0

def is_identifier(token):
    return token[0] == '&' and token[1:].isalpha()

def classify_token(token):
    if token in operadoresAritmeticos_key:
        return "operador aritmético"
    elif token in operadoresRelacionales_keys:
        return "operador relacional"
    elif token in operadoresLogicos_keys:
        return "operador lógico"
    elif token in operadoresAsignacion_keys:
        return "operador de asignación"
    elif token in data_type_keys:
        return "tipo de dato"
    elif token in palabrasReservadas_keys:
        return "palabra reservada"
    elif token.isdigit():
        return "número"
    elif is_identifier(token):
        return "variable válida"
    else:
        return "Palabra no identificada"

print("----------Analizador Lexico-------------")

program = a.split('\n')
for line in program:
    count += 1
    print("line #", count, "\n", line)

    # Check if the line ends with '.,'
    if not line.endswith('.,'):
        print("Error: no termina con '.,'")
        continue

    # Remove the '.,' from the end of the line
    line = line[:-2]

    # Verify the '.,' sequence in the dictionary
    if '.,' in simbolos_terminal_inicial_keys:
        print("., el operador es: ", simbolos_terminal_inicial['.,'])

    i = 0
    tokens = []
    while i < len(line):
        token = ''
        while i < len(line) and line[i].isspace():
            i += 1
        if i < len(line):
            if line[i].isalpha():
                while i < len(line) and line[i].isalpha():
                    token += line[i]
                    i += 1
            elif line[i].isdigit():
                while i < len(line) and line[i].isdigit():
                    token += line[i]
                    i += 1
            elif line[i] == '&':
                token += line[i]
                i += 1
                if i < len(line) and line[i].isalpha():
                    while i < len(line) and line[i].isalpha():
                        token += line[i]
                        i += 1
                if len(token) == 1:
                    tokens.append(token)
            else:
                if i + 1 < len(line) and line[i:i+2] in operadoresAritmeticos_key:
                    token = line[i:i+2]
                    i += 2
                elif i + 1 < len(line) and line[i:i+2] in operadoresLogicos_keys:
                    token = line[i:i+2]
                    i += 2
                elif i + 1 < len(line) and line[i:i+2] in operadoresAsignacion_keys:
                    token = line[i:i+2]
                    i += 2
                else:
                    token = line[i]
                    i += 1
            tokens.append(token)

    print("los tokens son: ", tokens)

    print("line #", count, "Propiedades \n")
    for token in tokens:
        print(token, classify_token(token))

        
    automata = ""
    for token in tokens:
      automata = automata, "-->", token
    print(automata)

    print("-------------------------")