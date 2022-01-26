# list of productions.
productions = [
    [],
    ["empezar", "BLOQUE", "terminar"],
    ["VARIABLES", "INSTRUCCIONES"],
    ["*[", "DECLARACION", "*]", "VARIABLES"],
    [],
    ["VARS", "DECLARACION"],
    [],
    ["/(", "LISTA",  ":", "TIPO", "/)"],
    ["entero"],
    ["real"],
    ["cadena"],
    ["identificador", "LISTAPRIMA"],
    ["LISTA"],
    [],
    ["*[", "ESTATUTO", "*]",  "INSTRUCCIONES"],
    [],
    ["condicion",  "CONDICION",  "/{", "INSTRUCCIONES", "/}"],
    ["ciclo_for", "/(", "DETALLE-FOR", "/)", "/{",  "INSTRUCCIONES", "/}"],
    ["identificador", "==", "EXPRESION", ";", "identificador",
        "OPERADOR", "EXPRESION", ";", "INCREDECRE"],
    ["ciclo_while", "CONDICION", "/{", "INSTRUCCIONES", "/}"],
    ["ciclo_repeat", "/{", "INSTRUCCIONES", "/}", "CONDICION"],
    ["casos", "identificador", "/{", "LISTACASES", "/}"],
    ["identificador", "==", "EXPRESION"],
    ["salida", "(", "identificador", ")"],
    ["Lectura", "(", "identificador", ")"],
    ["identificador", "SIGNO"],
    ["++"],
    ["--"],
    ["caso", "numero", "/{", "INSTRUCCIONES", "/}", "LISTACASES"],
    [],
    ["/(", "EXPRESION", "OPERADOR", "EXPRESION", "/)"],
    ["!", "/(", "EXPRESION", "OPERADOR", "EXPRESION", "/)"],
    ["%=%"],
    ["*>"],
    ["*<"],
    ["*>="],
    ["*<="],
    ["%%"],
    ["/&"],
    ["TERMINO", "EXPPRIMA"],
    ["+", "TERMINO", "EXPPRIMA"],
    ["-", "TERMINO", "EXPPRIMA"],
    [],
    ["FACTOR", "TERMPRIMO"],
    ["^*", "FACTOR", "TERMPRIMO"],
    ["*/", "FACTOR", "TERMPRIMO"],
    [],
    ["/(", "EXPRESION", "/)"],
    ["identificador"],
    ["numero"],
]
# Grammar table built with our First and Follow based on our Grammar.
grammar_table = [
    {"P": {"empezar": 1, "terminar": 250, "*[": 250, "*]": 250, "/(": 250, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 250, "caso": 250, "numero": 250, "condicion": 250,
           "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 250, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"BLOQUE": {"empezar": 250, "terminar": 2, "*[": 2, "*]": 250, "/(": 250, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 250, "caso": 250, "numero": 250, "condicion": 250,
                "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 250, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"VARIABLES": {"empezar": 250, "terminar": 4, "*[": 3, "*]": 250, "/(": 250, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 250, "caso": 250, "numero": 250, "condicion": 250,
                   "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 250, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"DECLARACION": {"empezar": 250, "terminar": 250, "*[": 250, "*]": 6, "/(": 5, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 250, "caso": 250, "numero": 250, "condicion": 250,
                     "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 250, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"VARS": {"empezar": 250, "terminar": 250, "*[": 250, "*]": 250, "/(": 7, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 250, "caso": 250, "numero": 250, "condicion": 250,
              "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 250, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"TIPO": {"empezar": 250, "terminar": 250, "*[": 250, "*]": 250, "/(": 250, "/)": 250, "entero": 8, "real": 9, "cadena": 10, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 250, "caso": 250, "numero": 250, "condicion": 250,
              "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 250, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"LISTA": {"empezar": 250, "terminar": 250, "*[": 250, "*]": 250, "/(": 250, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 11, "caso": 250, "numero": 250, "condicion": 250,
               "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 250, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"LISTAPRIMA": {"empezar": 250, "terminar": 250, "*[": 250, "*]": 250, "/(": 250, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 13, "identificador": 12, "caso": 250, "numero": 250, "condicion": 250,
                    "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 250, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"INSTRUCCIONES": {"empezar": 250, "terminar": 15, "*[": 14, "*]": 250, "/(": 250, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 250, "caso": 250, "numero": 250, "condicion": 250,
                       "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 250, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"ESTATUTO": {"empezar": 250, "terminar": 250, "*[": 250, "*]": 250, "/(": 250, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 22, "caso": 250, "numero": 250, "condicion": 16,
                  "ciclo_for": 17, "ciclo_while": 19, "ciclo_repeat": 20, "casos": 21, "salida": 23, "lectura": 24, "++": 250, "--": 250, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 250, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"DETALLE-FOR": {"empezar": 250, "terminar": 250, "*[": 250, "*]": 250, "/(": 250, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 18, "caso": 250, "numero": 250, "condicion": 250,
                     "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 250, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"INCREDECRE": {"empezar": 250, "terminar": 250, "*[": 250, "*]": 250, "/(": 250, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 25, "caso": 250, "numero": 250, "condicion": 250,
                    "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 250, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"SIGNO": {"empezar": 250, "terminar": 250, "*[": 250, "*]": 250, "/(": 250, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 250, "caso": 250, "numero": 250, "condicion": 250,
               "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 26, "--": 27, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 250, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"LISTACASES": {"empezar": 250, "terminar": 250, "*[": 250, "*]": 250, "/(": 250, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 29, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 250, "caso": 28, "numero": 250, "condicion": 250,
                    "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 250, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"CONDICION": {"empezar": 250, "terminar": 250, "*[": 250, "*]": 250, "/(": 30, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 250, "caso": 250, "numero": 250, "condicion": 250,
                   "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 31, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"OPERADOR": {"empezar": 250, "terminar": 250, "*[": 250, "*]": 250, "/(": 250, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 250, "caso": 250, "numero": 250, "condicion": 250,
                  "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 32, "*>": 33, "*<": 34, "*>=": 35, "*<=": 36, "!": 250, "%%": 37, "/&": 38, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"EXPRESION": {"empezar": 250, "terminar": 250, "*[": 250, "*]": 39, "/(": 250, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 39, "caso": 250, "numero": 39, "condicion": 250,
                   "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 250, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"EXPPRIMA": {"empezar": 250, "terminar": 250, "*[": 250, "*]": 42, "/(": 250, "/)": 42, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 42, "(": 250, ")": 250, ":": 250, "identificador": 250, "caso": 250, "numero": 250, "condicion": 250,
                  "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 42, "*>": 42, "*<": 42, "*>=": 42, "*<=": 42, "!": 250, "%%": 42, "/&": 42, "+": 40, "-": 41, "^*": 250, "*/": 250, "$": 250}},
    {"TERMINO": {"empezar": 250, "terminar": 250, "*[": 250, "*]": 250, "/(": 43, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 43, "caso": 250, "numero": 43, "condicion": 250,
                 "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 250, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
    {"TERMINOPRIMO": {"empezar": 250, "terminar": 250, "*[": 250, "*]": 46, "/(": 250, "/)": 46, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 46, "(": 250, ")": 250, ":": 250, "identificador": 250, "caso": 250, "numero": 250, "condicion": 250,
                      "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 46, "*>": 46, "*<": 46, "*>=": 46, "*<=": 46, "!": 250, "%%": 46, "/&": 46, "+": 46, "-": 46, "^*": 44, "*/": 45, "$": 250}},
    {"FACTOR": {"empezar": 250, "terminar": 250, "*[": 250, "*]": 250, "/(": 47, "/)": 250, "entero": 250, "real": 250, "cadena": 250, "/{": 250, "/}": 250, "==": 250, ";": 250, "(": 250, ")": 250, ":": 250, "identificador": 48, "caso": 250, "numero": 49, "condicion": 250,
                "ciclo_for": 250, "ciclo_while": 250, "ciclo_repeat": 250, "casos": 250, "salida": 250, "lectura": 250, "++": 250, "--": 250, "%=%": 250, "*>": 250, "*<": 250, "*>=": 250, "*<=": 250, "!": 250, "%%": 250, "/&": 250, "+": 250, "-": 250, "^*": 250, "*/": 250, "$": 250}},
]


# function to handle missing tokens and return those missing tokens as an error.
def find_expected_tokens(last_element_stack: str) -> list:

    expected_list = []

    # iterate over grammar_table
    for index in range(len(grammar_table)):
        # print(grammar_table[dictionary["P"]])
        for key in grammar_table[index]:
            # print("Fila es: ", key)
            if key == last_element_stack:
                # print("grammar_table[index][key] es: \n", grammar_table[index][key])
                for elem in grammar_table[index][key]:
                    # print(elem)
                    num = grammar_table[index][key][elem]
                    if num != 250:
                        expected_list.append(elem)

    return expected_list


# function to find the number of production we need to add to our stack
def find_production_number(last_element_stack: str, token_to_search: str) -> int:
    # print("last_element_stack: ", last_element_stack)
    # print("Token a buscar es: \n", token_to_search)

    # iterate over grammar_table
    for index in range(len(grammar_table)):

        for key in grammar_table[index]:

            if key == last_element_stack:

                for elem in grammar_table[index][key]:

                    if elem == token_to_search:
                        num_production_to_use = grammar_table[index][key][elem]
                        # print("Numero encontrado es: ", num_production_to_use)
                        if num_production_to_use == 250:
                            expected_tokens = find_expected_tokens(
                                last_element_stack)
                            print("Syntax Error. Tokens expected:\n",
                                  expected_tokens)
                        return num_production_to_use

    # print("Not found anything")
    expected_tokens = find_expected_tokens(last_element_stack)
    print("Syntax Error. Tokens expected:\n", expected_tokens)
    return 250


# function to iterate through the stack comparing values with the list of tokens
# and using the syntax table and productions
def stack_process(tokens_list: list) -> list:

    print("\n", "Initializing stack process...\n")
    stack = ["P"]
    list_of_found = []

    while len(stack) > 0:

        # print("Stack al inicio es: \n", stack)
        if stack[-1] == tokens_list[0]:
            found = stack.pop()
            tokens_list.pop(0)
            print("FOUND: ", found, "\n")
            list_of_found.append(found)
            # print("Ahora el stack es: \n", stack)
            if len(stack) == 0:
                print("Empty stack! :D\n")
                return list_of_found

            continue

        last_element_stack = stack[-1]
        production_num = find_production_number(
            last_element_stack, tokens_list[0])
        # print("\n")
        if production_num == 250:
            return list_of_found

        # print("production_num es:", production_num)
        # print(type(production_num))
        row_copied = productions[production_num]
        # print("row_copied es: ", row_copied)
        # print("Productions es:\n", productions)
        stack.pop()

        for elem in reversed(row_copied):
            stack.append(elem)
