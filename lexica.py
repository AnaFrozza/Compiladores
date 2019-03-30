#-------------------------------------------------------------------------
# Analisador léxico para a linguagem T++
# Autor: Ana Carolina Frozza
#-------------------------------------------------------------------------

import ply.lex as lex

class AnaliseLexica:

    def __init__(self):
        self.lexer = lex.lex(debug=False, module=self, optimize=False)
    
    #Palavras Reservadas
    reservadas = {
		'se': 'SE',
		'senão': 'SENAO',
        'então': 'ENTAO',
		'repita': 'REPITA',
		'até': 'ATE',
        'escreva': 'ESCREVE',
        'leia': 'LEIA',
        'inteiro': 'INTEIRO',
		'flutuante': 'FLUTUANTE',
		'vazio': 'VAZIO',
        'retorna' : 'RETORNA',
        'fim': 'FIM',
		'principal': 'PRINCIPAL',
	}

    #Lista de Tokens
    tokens = ['ADICAO', 'SUBTRACAO', 'MULTIPLICACAO', 'DIVISAO', 'IGUAL', 'DIFERENTE', 
			    'MAIOR', 'MENOR', 'MAIORIGUAL', 'MENORIGUAL', 'VIRGULA', 'ATRIBUICAO',
				'ABREPARENTESES', 'FECHAPARENTESES', 'ABRECOLCHETE', 'FECHACOLCHETE', 
                'DOISPONTOS', 'UNDERLINE', 'ID', 'NEGACAO', 'E', 'OU', 'COMENTARIO',] + list(reservadas.values())


    t_INTEIRO = r'[0-9]+'
    t_FLUTUANTE = r'[0-9]+(\.[0-9]+)'
    t_ADICAO = r'\+'
    t_SUBTRACAO = r'\-'
    t_MULTIPLICACAO = r'\*'
    t_DIVISAO = r'/'
    t_IGUAL = r'='
    t_DIFERENTE = r'<>'
    t_MAIOR = r'>'
    t_MENOR = r'<'
    t_MAIORIGUAL = r'>='
    t_MENORIGUAL = r'<='
    t_VIRGULA = r'\,'
    t_ATRIBUICAO = r':=' 
    t_ABREPARENTESES = r'\('
    t_FECHAPARENTESES = r'\)'
    t_ABRECOLCHETE = r'\['
    t_FECHACOLCHETE = r'\]'
    t_DOISPONTOS = r':'
    t_UNDERLINE = r'_'
    t_NEGACAO = r'\!'
    t_E = r'\&\&'
    t_OU = r'\|\|'
    t_ignore_COMENTARIO = r'\{[^\}]*[^\{]|\n*?\}'
    # r'\{[^\}]*[^\{]|\n*\}'
    # r'({(.|\n)*?\})'
    # r'\{[^}]*[^{]*\}'
    # r'{.*}'


    #Identificador de ID
    def t_ID(self, t):
        r'[a-zA-Zà-ÿÀ-Ÿ][a-zA-Zà-ÿÀ-Ÿ0-9]*'
        t.type = self.reservadas.get(t.value, 'ID')
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    #Expressao ignorada
    t_ignore = ' \t'
    
    #Expressao de erro
    def t_error(self,t):
        print("Caractere ilegal: '%s', linha %d, coluna %d" % (t.value[0], t.lineno, t.lexpos))
        t.lexer.skip(1)

    def test(self, code):
        lex.input(code)
        while True:
            tok = lex.token()
            if not tok:
                break
            print("|%3d |%3d | %s %s" % (tok.lineno, tok.lexpos, tok.type, tok.value))

    
if __name__ == '__main__':
    from sys import argv
    lexer = AnaliseLexica()
    f = open(argv[1])
    conteudo = f.readlines()
    print("|Line|Colu| TYPE value")
    print("-----------------------------")
    for linha in conteudo:
        lexer.test(linha)
    print("\nConcluido!")