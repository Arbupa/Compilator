from enum import unique
import re

from syntactic import stack_process

# final list to show the char with their states
final_list = []
# global variable to add the letters found and compare if it's a reserved word
message_print = ""
# token_list = []

# global list cotaining states found in our lexical analysis and returning their respective token.
get_token_from_list = {
    101: "entero",
    102: "numero",
    103: "real",
    104: "numero",
    105: "identificador",
    106: "%%",
    107: "%=%",
    108: "==",
    109: "-",
    110: "--",
    111: "+",
    112: "++",
    130: "cadena",
    113: "^*",
    114: "*/",
    115: "*[",
    116: "*]",
    117: "*>=",
    118: "*>",
    119: "*<=",
    120: "*<",
    121: "/{",
    122: "/}",
    123: "/(",
    124: "/)",
    125: "/&",
    132: ";",
    134: "$",
    140: ":",
    141: "!",
}


# function to identify the processing char using the state_matrix and the state.
def get_column(char, state):

    state_matrix = [[{"double_quote": 22}, {"single_quote": 24}, {';': 132}, {'.': 133},
                     {'$': 134}, {
                         '@': 135}, {'back_slash': 26}, {'space': 138}, {',': 139}, {':': 140},
                     {"!": 141}, {"line_break": 136}, {
                         'letter': 9}, {'digit': 200},
                     {'e': 9}, {'_': 211}, {'>': 211}, {
                         '<': 211}, {'+': 13}, {'-': 12},
                     {"/": 18}, {"*": 15}, {'^': 14}, {'{': 211},
                     {'}': 211}, {'(': 211}, {')': 211},
                     {'%': 10}, {'&': 211}, {'[': 211},
                     {']': 211}, {'#': 1}, {'=': 11}
                     ],
                    # state 1
                    [{"double_quote": 200}, {"single_quote": 200}, {';': 200}, {'.': 200},
                     {'$': 200}, {
                        '@': 200}, {'back_slash': 200}, {'space': 200}, {',': 200}, {':': 200},
                     {"!": 200}, {"line_break": 200}, {
                        'letter': 200}, {'digit': 2},
                     {'e': 200}, {'_': 200}, {'>': 200}, {
                        '<': 200}, {'+': 200}, {'-': 200},
                     {"/": 200}, {"*": 200}, {'^': 200}, {'{': 200},
                     {'}': 200}, {'(': 200}, {')': 200},
                     {'%': 200}, {'&': 200}, {'[': 200},
                     {']': 200}, {'#': 200}, {'=': 200}
                     ],
                    # state 2
                    [{"double_quote": 200}, {"single_quote": 200}, {';': 200}, {'.': 5},
                     {'$': 200}, {
                        '@': 200}, {'back_slash': 200}, {'space': 200}, {',': 200}, {':': 200},
                     {"!": 200}, {"line_break": 200}, {
                        'letter': 200}, {'digit': 2},
                     {'e': 3}, {'_': 200}, {'>': 200}, {
                        '<': 200}, {'+': 200}, {'-': 200},
                     {"/": 200}, {"*": 200}, {'^': 200}, {'{': 200},
                     {'}': 200}, {'(': 200}, {')': 200},
                     {'%': 200}, {'&': 200}, {'[': 200},
                     {']': 200}, {'#': 101}, {'=': 200}
                     ],
                    # state 3
                    [{"double_quote": 201}, {"single_quote": 201}, {';': 201}, {'.': 201},
                     {'$': 201}, {
                        '@': 201}, {'back_slash': 201}, {'space': 201}, {',': 201}, {':': 201},
                     {"!": 201}, {"line_break": 201}, {
                        'letter': 201}, {'digit': 4},
                     {'e': 201}, {'_': 201}, {'>': 201}, {
                        '<': 201}, {'+': 201}, {'-': 201},
                     {"/": 201}, {"*": 201}, {'^': 201}, {'{': 201},
                     {'}': 201}, {'(': 201}, {')': 201},
                     {'%': 201}, {'&': 201}, {'[': 201},
                     {']': 201}, {'#': 201}, {'=': 201}
                     ],

                    # state 4
                    [{"double_quote": 202}, {"single_quote": 202}, {';': 202}, {'.': 202},
                     {'$': 202}, {
                        '@': 202}, {'back_slash': 202}, {'space': 202}, {',': 202}, {':': 202},
                     {"!": 202}, {"line_break": 202}, {
                        'letter': 202}, {'digit': 4},
                     {'e': 202}, {'_': 202}, {'>': 202}, {
                        '<': 202}, {'+': 202}, {'-': 202},
                     {"/": 202}, {"*": 202}, {'^': 202}, {'{': 202},
                     {'}': 202}, {'(': 202}, {')': 202},
                     {'%': 202}, {'&': 202}, {'[': 202},
                     {']': 202}, {'#': 102}, {'=': 202}
                     ],

                    # state 5
                    [{"double_quote": 203}, {"single_quote": 203}, {';': 203}, {'.': 203},
                     {'$': 203}, {
                        '@': 203}, {'back_slash': 203}, {'space': 203}, {',': 203}, {':': 203},
                     {"!": 203}, {"line_break": 203}, {
                        'letter': 203}, {'digit': 6},
                     {'e': 203}, {'_': 203}, {'>': 203}, {
                        '<': 203}, {'+': 203}, {'-': 203},
                     {"/": 203}, {"*": 203}, {'^': 203}, {'{': 203},
                     {'}': 203}, {'(': 203}, {')': 203},
                     {'%': 203}, {'&': 203}, {'[': 203},
                     {']': 203}, {'#': 203}, {'=': 203}
                     ],

                    # state 6
                    [{"double_quote": 204}, {"single_quote": 204}, {';': 204}, {'.': 204},
                     {'$': 204}, {
                        '@': 204}, {'back_slash': 204}, {'space': 204}, {',': 204}, {':': 204},
                     {"!": 204}, {"line_break": 204}, {
                        'e': 7}, {'digit': 6},
                     {'letter': 204}, {'_': 204}, {'>': 204}, {
                        '<': 204}, {'+': 204}, {'-': 204},
                     {"/": 204}, {"*": 204}, {'^': 204}, {'{': 204},
                     {'}': 204}, {'(': 204}, {')': 204},
                     {'%': 204}, {'&': 204}, {'[': 204},
                     {']': 204}, {'#': 103}, {'=': 204}
                     ],

                    # state 7
                    [{"double_quote": 205}, {"single_quote": 205}, {';': 205}, {'.': 205},
                     {'$': 205}, {
                        '@': 205}, {'back_slash': 205}, {'space': 205}, {',': 205}, {':': 205},
                     {"!": 205}, {"line_break": 205}, {
                        'letter': 205}, {'digit': 8},
                     {'e': 205}, {'_': 205}, {'>': 205}, {
                        '<': 205}, {'+': 205}, {'-': 205},
                     {"/": 205}, {"*": 205}, {'^': 205}, {'{': 205},
                     {'}': 205}, {'(': 205}, {')': 205},
                     {'%': 205}, {'&': 205}, {'[': 205},
                     {']': 205}, {'#': 205}, {'=': 205}
                     ],

                    # state 8
                    [{"double_quote": 206}, {"single_quote": 206}, {';': 206}, {'.': 206},
                     {'$': 206}, {
                        '@': 206}, {'back_slash': 206}, {'space': 206}, {',': 206}, {':': 206},
                     {"!": 206}, {"line_break": 206}, {
                        'letter': 206}, {'digit': 8},
                     {'e': 206}, {'_': 206}, {'>': 206}, {
                        '<': 206}, {'+': 206}, {'-': 206},
                     {"/": 206}, {"*": 206}, {'^': 206}, {'{': 206},
                     {'}': 206}, {'(': 206}, {')': 206},
                     {'%': 206}, {'&': 206}, {'[': 206},
                     {']': 206}, {'#': 104}, {'=': 206}
                     ],

                    # state 9
                    [{"double_quote": 105}, {"single_quote": 105}, {';': 105}, {'.': 105},
                     {'$': 9}, {
                        '@': 105}, {'back_slash': 105}, {'space': 105}, {',': 105}, {':': 105},
                     {"!": 105}, {"line_break": 105}, {
                        'letter': 9}, {'digit': 9},
                     {'e': 105}, {'_': 9}, {'>': 105}, {
                        '<': 105}, {'+': 105}, {'-': 105},
                     {"/": 105}, {"*": 105}, {'^': 105}, {'{': 105},
                     {'}': 105}, {'(': 105}, {')': 105},
                     {'%': 105}, {'&': 105}, {'[': 105},
                     {']': 105}, {'#': 105}, {'=': 105}
                     ],

                    # state 10
                    [{"double_quote": 207}, {"single_quote": 207}, {';': 207}, {'.': 207},
                     {'$': 207}, {
                        '@': 207}, {'back_slash': 207}, {'space': 207}, {',': 207}, {':': 207},
                     {"!": 207}, {"line_break": 207}, {
                        'letter': 207}, {'digit': 207},
                     {'e': 207}, {'_': 207}, {'>': 207}, {
                        '<': 207}, {'+': 207}, {'-': 207},
                     {"/": 207}, {"*": 207}, {'^': 207}, {'{': 207},
                     {'}': 207}, {'(': 207}, {')': 207},
                     {'%': 106}, {'&': 207}, {'[': 207},
                     {']': 207}, {'#': 207}, {'=': 27}
                     ],

                    # state 11
                    [{"double_quote": 208}, {"single_quote": 208}, {';': 208}, {'.': 208},
                     {'$': 208}, {
                        '@': 208}, {'back_slash': 208}, {'space': 208}, {',': 208}, {':': 208},
                     {"!": 208}, {"line_break": 208}, {
                        'letter': 208}, {'digit': 208},
                     {'e': 208}, {'_': 208}, {'>': 208}, {
                        '<': 208}, {'+': 208}, {'-': 208},
                     {"/": 208}, {"*": 208}, {'^': 208}, {'{': 208},
                     {'}': 208}, {'(': 208}, {')': 208},
                     {'%': 208}, {'&': 208}, {'[': 208},
                     {']': 208}, {'#': 208}, {'=': 108}
                     ],

                    # state 12
                    [{"double_quote": 109}, {"single_quote": 109}, {';': 109}, {'.': 109},
                     {'$': 109}, {
                        '@': 109}, {'back_slash': 109}, {'space': 109}, {',': 109}, {':': 109},
                     {"!": 109}, {"line_break": 109}, {
                        'letter': 109}, {'digit': 109},
                     {'e': 109}, {'_': 109}, {'>': 109}, {
                        '<': 109}, {'+': 109}, {'-': 110},
                     {"/": 109}, {"*": 109}, {'^': 109}, {'{': 109},
                     {'}': 109}, {'(': 109}, {')': 109},
                     {'%': 109}, {'&': 109}, {'[': 109},
                     {']': 109}, {'#': 109}, {'=': 109}
                     ],

                    # state 13
                    [{"double_quote": 111}, {"single_quote": 111}, {';': 111}, {'.': 111},
                     {'$': 111}, {
                        '@': 111}, {'back_slash': 111}, {'space': 111}, {',': 111}, {':': 111},
                     {"!": 111}, {"line_break": 111}, {
                        'letter': 111}, {'digit': 111},
                     {'e': 111}, {'_': 111}, {'>': 111}, {
                        '<': 111}, {'+': 112}, {'-': 111},
                     {"/": 111}, {"*": 111}, {'^': 111}, {'{': 111},
                     {'}': 111}, {'(': 111}, {')': 111},
                     {'%': 111}, {'&': 111}, {'[': 111},
                     {']': 111}, {'#': 111}, {'=': 111}
                     ],

                    # state 14
                    [{"double_quote": 209}, {"single_quote": 209}, {';': 209}, {'.': 209},
                     {'$': 209}, {
                        '@': 209}, {'back_slash': 209}, {'space': 209}, {',': 209}, {':': 209},
                     {"!": 209}, {"line_break": 209}, {
                        'letter': 209}, {'digit': 209},
                     {'e': 209}, {'_': 209}, {'>': 209}, {
                        '<': 209}, {'+': 209}, {'-': 209},
                     {"/": 209}, {"*": 113}, {'^': 209}, {'{': 209},
                     {'}': 209}, {'(': 209}, {')': 209},
                     {'%': 209}, {'&': 209}, {'[': 209},
                     {']': 209}, {'#': 209}, {'=': 209}
                     ],

                    # state 15
                    [{"double_quote": 214}, {"single_quote": 214}, {';': 214}, {'.': 214},
                     {'$': 214}, {
                        '@': 214}, {'back_slash': 214}, {'space': 214}, {',': 214}, {':': 214},
                     {"!": 214}, {"line_break": 214}, {
                        'letter': 214}, {'digit': 214},
                     {'e': 214}, {'_': 214}, {'>': 16}, {
                        '<': 17}, {'+': 214}, {'-': 214},
                     {"/": 18}, {"*": 214}, {'^': 214}, {'{': 214},
                     {'}': 214}, {'(': 214}, {')': 214},
                     {'%': 214}, {'&': 214}, {'[': 115},
                     {']': 116}, {'#': 214}, {'=': 214}
                     ],

                    # state 16
                    [{"double_quote": 118}, {"single_quote": 118}, {';': 118}, {'.': 118},
                     {'$': 118}, {
                        '@': 118}, {'back_slash': 118}, {'space': 118}, {',': 118}, {':': 118},
                     {"!": 118}, {"line_break": 118}, {
                        'letter': 118}, {'digit': 118},
                     {'e': 118}, {'_': 118}, {'>': 118}, {
                        '<': 118}, {'+': 118}, {'-': 118},
                     {"/": 118}, {"*": 118}, {'^': 118}, {'{': 118},
                     {'}': 118}, {'(': 118}, {')': 118},
                     {'%': 118}, {'&': 118}, {'[': 118},
                     {']': 118}, {'#': 118}, {'=': 117}
                     ],

                    # state 17
                    [{"double_quote": 120}, {"single_quote": 120}, {';': 120}, {'.': 120},
                     {'$': 120}, {
                        '@': 120}, {'back_slash': 120}, {'space': 120}, {',': 120}, {':': 120},
                     {"!": 120}, {"line_break": 120}, {
                        'letter': 120}, {'digit': 120},
                     {'e': 120}, {'_': 120}, {'>': 120}, {
                        '<': 120}, {'+': 120}, {'-': 120},
                     {"/": 120}, {"*": 120}, {'^': 120}, {'{': 120},
                     {'}': 120}, {'(': 120}, {')': 120},
                     {'%': 120}, {'&': 120}, {'[': 120},
                     {']': 120}, {'#': 120}, {'=': 119}
                     ],

                    # state 18
                    [{"double_quote": 128}, {"single_quote": 128}, {';': 128}, {'.': 128},
                     {'$': 128}, {
                        '@': 128}, {'back_slash': 128}, {'space': 114}, {',': 128}, {':': 128},
                     {"!": 128}, {"line_break": 128}, {
                        'letter': 128}, {'digit': 128},
                     {'e': 128}, {'_': 128}, {'>': 128}, {
                        '<': 128}, {'+': 128}, {'-': 128},
                     {"/": 126}, {"*": 19}, {'^': 128}, {'{': 121},
                     {'}': 123}, {'(': 123}, {')': 124},
                     {'%': 128}, {'&': 125}, {'[': 128},
                     {']': 128}, {'#': 128}, {'=': 128}
                     ],



                    # state 19
                    [{"double_quote": 210}, {"single_quote": 210}, {';': 210}, {'.': 210},
                     {'$': 210}, {
                        '@': 210}, {'back_slash': 210}, {'space': 20}, {',': 210}, {':': 210},
                     {"!": 210}, {"line_break": 210}, {
                        'letter': 20}, {'digit': 20},
                     {'e': 210}, {'_': 210}, {'>': 210}, {
                        '<': 210}, {'+': 210}, {'-': 210},
                     {"/": 210}, {"*": 21}, {'^': 210}, {'{': 210},
                     {'}': 210}, {'(': 210}, {')': 210},
                     {'%': 210}, {'&': 210}, {'[': 210},
                     {']': 210}, {'#': 210}, {'=': 210}
                     ],



                    # state 20
                    [{"double_quote": 210}, {"single_quote": 210}, {';': 210}, {'.': 210},
                     {'$': 210}, {
                        '@': 210}, {'back_slash': 210}, {'space': 20}, {',': 210}, {':': 210},
                     {"!": 210}, {"line_break": 210}, {
                        'letter': 20}, {'digit': 20},
                     {'e': 210}, {'_': 210}, {'>': 210}, {
                        '<': 210}, {'+': 210}, {'-': 210},
                     {"/": 210}, {"*": 21}, {'^': 210}, {'{': 210},
                     {'}': 210}, {'(': 210}, {')': 210},
                     {'%': 210}, {'&': 210}, {'[': 210},
                     {']': 210}, {'#': 210}, {'=': 210}
                     ],


                    # state 21
                    [{"double_quote": 210}, {"single_quote": 210}, {';': 210}, {'.': 210},
                     {'$': 210}, {
                         '@': 210}, {'back_slash': 210}, {'space': 210}, {',': 210}, {':': 210},
                     {"!": 210}, {"line_break": 210},
                     {'letter': 210}, {'digit': 210},
                     {'e': 210}, {'_': 210}, {'>': 210},
                     {'<': 210}, {'+': 210}, {'-': 210},
                     {"/": 127}, {"*": 210}, {'^': 210}, {'{': 210},
                     {'}': 210}, {'(': 210}, {')': 210},
                     {'%': 210}, {'&': 210}, {'[': 210},
                     {']': 210}, {'#': 210}, {'=': 210}
                     ],


                    # state 22
                    [{"double_quote": 130}, {"single_quote": 129}, {';': 129}, {'.': 129},
                     {'$': 129}, {
                         '@': 129}, {'back_slash': 129}, {'space': 129}, {',': 129}, {':': 129},
                     {"!": 129}, {"line_break": 129},
                     {'letter': 23}, {'digit': 23},
                     {'e': 129}, {'_': 129}, {'>': 129},
                     {'<': 129}, {'+': 129}, {'-': 129},
                     {"/": 129}, {"*": 129}, {'^': 129}, {'{': 129},
                     {'}': 129}, {'(': 129}, {')': 129},
                     {'%': 129}, {'&': 129}, {'[': 129},
                     {']': 129}, {'#': 129}, {'=': 129}
                     ],


                    # state 23
                    [{"double_quote": 130}, {"single_quote": 129}, {';': 129}, {'.': 129},
                     {'$': 129}, {
                         '@': 129}, {'back_slash': 129}, {'space': 23}, {',': 129}, {':': 129},
                     {"!": 129}, {"line_break": 129},
                     {'letter': 23}, {'digit': 23},
                     {'e': 129}, {'_': 129}, {'>': 129},
                     {'<': 129}, {'+': 129}, {'-': 129},
                     {"/": 129}, {"*": 129}, {'^': 129}, {'{': 129},
                     {'}': 129}, {'(': 129}, {')': 129},
                     {'%': 129}, {'&': 129}, {'[': 129},
                     {']': 129}, {'#': 129}, {'=': 129}
                     ],


                    # state 24
                    [{"double_quote": 129}, {"single_quote": 131}, {';': 129}, {'.': 129},
                     {'$': 129}, {
                         '@': 129}, {'back_slash': 129}, {'space': 25}, {',': 129}, {':': 129},
                     {"!": 129}, {"line_break": 129},
                     {'letter': 25}, {'digit': 25},
                     {'e': 129}, {'_': 129}, {'>': 129},
                     {'<': 129}, {'+': 129}, {'-': 129},
                     {"/": 129}, {"*": 129}, {'^': 129}, {'{': 129},
                     {'}': 129}, {'(': 129}, {')': 129},
                     {'%': 129}, {'&': 129}, {'[': 129},
                     {']': 129}, {'#': 129}, {'=': 129}
                     ],


                    # state 25
                    [{"double_quote": 129}, {"single_quote": 131}, {';': 129}, {'.': 129},
                     {'$': 129}, {
                         '@': 129}, {'back_slash': 129}, {'space': 129}, {',': 129}, {':': 129},
                     {"!": 129}, {"line_break": 129},
                     {'letter': 129}, {'digit': 129},
                     {'e': 129}, {'_': 129}, {'>': 129},
                     {'<': 129}, {'+': 129}, {'-': 129},
                     {"/": 129}, {"*": 129}, {'^': 129}, {'{': 129},
                     {'}': 129}, {'(': 129}, {')': 129},
                     {'%': 129}, {'&': 129}, {'[': 129},
                     {']': 129}, {'#': 129}, {'=': 129}
                     ],


                    # state 26
                    [{"double_quote": 137}, {"single_quote": 137}, {';': 137}, {'.': 137},
                     {'$': 137}, {
                         '@': 137}, {'back_slash': 137}, {'space': 137}, {',': 137}, {':': 137},
                     {"!": 137}, {"line_break": 136},
                     {'letter': 137}, {'digit': 137},
                     {'e': 137}, {'_': 137}, {'>': 137},
                     {'<': 137}, {'+': 137}, {'-': 137},
                     {"/": 137}, {"*": 137}, {'^': 137}, {'{': 137},
                     {'}': 137}, {'(': 137}, {')': 137},
                     {'%': 137}, {'&': 137}, {'[': 137},
                     {']': 137}, {'#': 137}, {'=': 137}
                     ],


                    # state 27
                    [{"double_quote": 207}, {"single_quote": 207}, {';': 207}, {'.': 207},
                     {'$': 207}, {
                        '@': 207}, {'back_slash': 207}, {'space': 207}, {',': 207}, {':': 207},
                     {"!": 207}, {"line_break": 207}, {
                        'letter': 207}, {'digit': 207},
                     {'e': 207}, {'_': 207}, {'>': 207}, {
                        '<': 207}, {'+': 207}, {'-': 207},
                     {"/": 207}, {"*": 207}, {'^': 207}, {'{': 207},
                     {'}': 207}, {'(': 207}, {')': 207},
                     {'%': 107}, {'&': 207}, {'[': 207},
                     {']': 207}, {'#': 207}, {'=': 207}
                     ],

                    ]

    number = ""
    result = ""

    try:
        number = re.findall(r'[0-9]', char)
        int(number[0])
        result = "digit"
        number = 0
        # print("Char it's a digit")

    except:
        # regular expression to compare if it's a letter
        a_z = re.findall('[a-zA-Z]', char)
        # if to validate if a_z has a value, therefore it is a letter
        if len(a_z) > 0:
            # print("char is a letter")
            if a_z[0] == 'e' and len(message_print) != 0:
                try:
                    numberTest = re.findall(r'[0-9]', message_print[-1])
                    int(numberTest[0])
                    result = 'e'

                except:
                    result = "letter"
            if result != 'e':
                result = "letter"

            a_z = ""

        else:
            if (char == '.'):
                result = char
            elif (char == '+'):
                result = char
            elif (char == '"'):
                result = "double_quote"
            elif (char == "'"):
                result = "single_quote"
            elif (char == ';'):
                result = char
            elif (char == '$'):
                result = char
            elif (char == '@'):
                result = char
            elif (char == '\\'):
                result = "back_slash"
            elif (char == ' '):
                result = "space"
            elif (char == ','):
                result = char
            elif (char == ':'):
                result = char
            elif (char == '!'):
                result = char
            elif (char == 'n'):
                result = "line_break"
            elif (char == '_'):
                result = char
            elif (char == '/'):
                result = char
            elif (char == '*'):
                result = char
            elif (char == '{'):
                result = char
            elif (char == '}'):
                result = char
            elif (char == '('):
                result = char
            elif (char == ')'):
                result = char
            elif (char == '%'):
                result = char
            elif (char == '&'):
                result = char
            elif (char == '['):
                result = char
            elif (char == ']'):
                result = char
            elif (char == '#'):
                result = char
            elif (char == '>'):
                result = char
            elif (char == '<'):
                result = char
            elif (char == '='):
                result = char
            elif (char == '-'):
                result = char
            elif (char == '^'):
                result = char
            else:
                return 211

    # loop over the multidimensional matrix state
    for i in range(len(state_matrix)):
        for j in range(len(state_matrix[i])):
            for k in state_matrix[i][j]:

                if i == state and k == result:
                    print(
                        f"Char processing is: {result}\n Value found: {state_matrix[i][j][k]}")
                    final_list.append({char: state_matrix[i][j][k]})

                    return state_matrix[i][j][k]


# function to open, read and process a file with our automaton by each character.
def check_file(file: str):
    token_list = []
   # list of the special (reserved) words that this compilator use.
    special_words = {
        "condicion ": "condicion", "ciclo_while ": "ciclo_while", "ciclo_repeat ": "ciclo_repeat", "ciclo_for ": "ciclo_for", "empezar ": "empezar",
        "terminar ": "terminar", "salida ": "salida", "lectura ": "lectura", "entero ": "entero", "real ": "real", "cadena ": "cadena", "caso ": "caso", "casos ": "casos", "identificador ": "identificador"}

    # errors list with all the states
    # P.S.: not all of them are errors also they're all states.
    errors_list = {
        101: "DÍGITO CON DECIMAL",
        102: "DÍGITO CON NOTACIÓN CIENTÍFICA",
        200: "DIGITO MAL FORMADO: ",
        201: "DÍGITO CON NOTACIÓN CIENTÍFICA MAL FORMADO",
        211: "SE ENCONTRÓ: ",
        202: "DÍGITO CON NOTACIÓN CIENTÍFICA MAL FORMADO",
        203: "DECIMAL MAL FORMADO",
        103: "DECIMAL",
        204: "DECIMAL MAL FORMADO",
        205: "DECIMAL CON NOTACIÓN CIENTÍFICA MAL FORMADO",
        104: "DECIMAL CON NOTACIÓN CIENTÍFICA",
        206: "DECIMAL CON NOTACIÓN CIENTÍFICA MAL FORMADO",
        105: "VARIABLE",
        106: "OR",
        207: "OR/COMPARACION MAL FORMADO",
        107: "IGUAL(COMPARACION)",
        108: "IGUAL(ASIGNACION)",
        208: "ASIGNACION MAL FORMADO",
        109: "DECREMENTO MAL FORMADO",
        110: "DECREMENTO",
        111: "SUMA",
        112: "INCREMENTO",
        209: "MULTIPLICACION MAL FORMADO",
        113: "MULTIPLICACION",
        212: "DIVISION|CORCHETE|MENOR|MAYOR MAL FORMADO",
        114: "DIVISION",
        115: "CORCHETE ABIERTO",
        116: "CORCHETE CERRADO",
        117: "MAYOR IGUAL QUE",
        118: "MAYOR QUE",
        119: "MENOR IGUAL QUE",
        120: "MENOR QUE",
        121: "LLAVE ABIERTA",
        122: "LLACE CERRADA",
        123: "PARENTESIS ABIERTO",
        124: "PARENTESIS CERRADO",
        125: "AND",
        126: "COMENTARIO",
        210: "COMENTARIO MULTILINEA MAL FORMADO",
        127: "COMENTARIO MULTILINEA",
        128: "SE ENCONTRÓ SLASH",
        129: "COMENTARIO MAL FORMADO",
        130: "COMENTARIO DOBLE COMILLA",
        131: "COMENTARIO COMILLA SIMPLE",
        132: "PUNTO Y COMA",
        133: "PUNTO",
        134: "SIGNO $",
        135: "ARROBA",
        136: "SALTO DE LINEA",
        137: "DIAGONAL INVERSA",
        138: "ESPACIO",
        139: "COMA",
        140: "DOS PUNTOS",
        141: "NEGACION",
        142: "TAB",
    }

    # open the file
    with open(file, encoding="utf-8") as f:
        # read it by line
        lines = f.readlines()
      #   print(lines)

        # iterate over the list of strings
        for elem in lines:
            i = 0
            state = 0
            # message_print = ""
            # iterate over every char in the string
            while i < len(elem):

                char = elem[i]
                # print(len(char))
                state = get_column(char, state)
                global message_print
                message_print = message_print + char
                added = False
                # print("Char processing is: ", char)
                # print("The state is: ", state)
                if state > 99:
                    # seek for the number of error inside our errors_list and print the value
                    # here what I need is to add what is printing (besides the message) and that's all.
                    if state in errors_list:
                        # global token_list
                        global get_token_from_list
                        # print("message_print es: ", message_print)
                        # print("al inicio del ciclo esto es token_list: ", token_list)

                        if state == 211 and message_print == '(':
                           #  print("Entrando al if ( ")
                           #  print("Lo que me llega es: ", message_print)
                            token_list.append("(")
                           #  continue
                        if state == 211 and message_print == ')':
                           #  print("Entrando al if ) ")
                            token_list.append(")")
                           #  continue
                          # agregar if para comprobar si la palabra encontrada estaba en special_words
                        if message_print in special_words:
                           #  print("PALABRA RESERVADA " + message_print + "\n")
                            print("La palabra res que se agrega es: \n",
                                  token_list.append(special_words[message_print]))
                            added = True

                        else:
                            print(errors_list[state] +
                                  " " + message_print + "\n")

                        if state in get_token_from_list and added == False:
                           #  print("State que se usa es: ", state)
                            token_list.append(get_token_from_list[state])

                        message_print = ""

                    state = 0

                i = i+1

      #   print("token_list es: ", token_list)

        return token_list
        # print(final_list)


if __name__ == "__main__":
    list_of_tokens = check_file("test2.txt")
    tokens_recognized = stack_process(list_of_tokens)
   #  if len(tokens_recognized) > 0:
    print("Tokens recognized:\n", tokens_recognized)
