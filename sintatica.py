#-------------------------------------------------------------------------
# Analisador Sintático para a linguagem T++
# Autor: Ana Carolina Frozza
#-------------------------------------------------------------------------
import ply.yacc as yacc
from lexica import AnaliseLexica

class Arvore:
    def __init__(self, tipo, filho=[], valor=None):
        self.tipo = tipo
        self.valor = valor
        if filho:
            self.filho = filho
        else:
            self.filho = []

    def __str__(self):
        self.tipo

    def __str__(self, nivel):
        retorno = "| " * nivel + self.tipo + "\n"
        nivel += 1
        for filho in self.filho:
            retorno += filho.__str__(nivel)
        return retorno

class AnaliseSintatica:
    def p_programa_1(self, p):
        'programa: declaracao programa'
        p[0] = Arvore('declaracao_loop', [p[1], p[2]])

    
    def p_programa_2(self, p):
        'programa: declaracao'
        p[0] = Arvore('declaracao_sem_loop', [p[1]])


    def p_declaracao_1(self, p):
        'declaracao: declaracao_funcao'
        p[0] = Arvore('declaracao_de_funcao', [p[1]])


    def p_declaracao_2(self, p):
        'declaracao: declaracao_var'
        p[0] = Arvore('declaracao_de_var', [p[1]])


    def p_declaracao_funcao_1(self, p):
        'declaracao_funcao: tipo ID ABREPARENTESES declaracao_parametro FECHAPARENTESES sequencia_declaracao FIM'
        p[0] = Arvore('declaracao_de_funcao_com_corpo', [p[1], p[4], p[6]], p[2])


    def p_declaracao_funcao_2(self, p):
        'declaracao_funcao: tipo ID ABREPARENTESES declaracao_parametro FECHAPARENTESES FIM'
        p[0] = Arvore('declaracao_de_funcao_sem_corpo', [p[1], p[4]], p[2])


    def p_declaracao_funcao_3(self, p):
        'declaracao_funcao: tipo ID ABREPARENTESES FECHAPARENTESES sequencia_declaracao FIM'
        p[0] = Arvore('declaracao_de_funcao_sem_parametros_com_corpo', [p[1], p[5]], p[2])


    def p_declaracao_funcao_4(self, p):
        'declaracao_funcao: tipo ID ABREPARENTESES FECHAPARENTESES FIM'
        p[0] = Arvore('declaracao_de_funcao_sem_parametros_sem_corpo', [p[1]], p[2])


    def p_declaracao_parametro_1(self, p):
        'declaracao_parametro: tipo DOISPONTOS ID VIRGULA declaracao_parametro'
        p[0] = Arvore('declaracao_de_parametro_loop', [p[1], p[5]], p[3])

    
    def p_declaracao_parametro_2(self, p):
        'declaracao_parametro: tipo DOISPONTOS ID'
        p[0] = Arvore('declaracao_de_parametro', [p[1]], p[3])

    
    def p_sequencia_declaracao_1(self, p):
        'sequencia_declaracao: declaracao_codigo'
        p[0] = Arvore('sequencia_de_declaracao', [p[1]])

    
    def p_sequencia_declaracao_2(self, p):
        'sequencia_declaracao: sequencia_declaracao declaracao_codigo'
        p[0] = Arvore('sequencia_de_declaracao_loop', [p[1], p[2]])

    def p_declaracao_codigo_1(self, p):
        'declaracao_codigo: declaracao_funcao'
        p[0] = Arvore('declaracao_de_declaracao_funcao', [p[1]])

    def p_declaracao_codigo_2(self, p):
        'declaracao_codigo: expressao_condicional'
        p[0] = Arvore('declaracao_de_expressao_condicional', [p[1]])

    def p_declaracao_codigo_3(self, p):
        'declaracao_codigo : expressao_interacao'
        p[0] = Arvore('declaracao_de_expressao_interacao', [p[1]])

    def p_declaracao_codigo_4(self, p):
        'declaracao_codigo: expressao_atribuicao'
        p[0] = Arvore('declaracao_de_expressao_atribuicao', [p[1]])
    
    def p_declaracao_codigo_5(self, p):
        'declaracao_codigo: expressao_leia'
        p[0] = Arvore('declaracao_de_expressao_leia', [p[1]])

    def p_declaracao_codigo_6(self, p):
        'declaracao_codigo: expressao_escreva'
        p[0] = Arvore('declaracao_de_expressao_escreva', [p[1]])

    def p_declaracao_codigo_7(self, p):
        'declaracao_codigo: declara_var'
        p[0] = Arvore('declaracao_de_variavel', [p[1]])

    def p_declaracao_codigo_8(self, p):
        'declaracao_codigo: retorna'
        p[0] = Arvore('declaracao_de_retorna', [p[1]])

    def p_declaracao_codigo_9(self, p):
        'declaracao_codigo: chamada_funcao'
        p[0] = Arvore('declaracao_de_chamada_de_funcao', [p[1]])

    def p_expressao_condicional_1(self, p):
        'expressao_condicional: SE expressao ENTAO sequencia_de_declaracao SENAO sequencia_de_declaracao FIM'
        p[0] = Arvore('declaracao_expressao_condicional_com_senao', [p[2], p[4], p[6]])

    def p_expressao_condicional_2(self, p):
        'expressao_condicional: SE expressao ENTAO sequencia_de_declaracao FIM'
        p[0] = Arvore('declaracao_expressao_condicional_com_senao', [p[2], p[4]])

    def p_expressao_interacao_1(self, p):
        'expressao_interacao: REPITA sequencia_de_declaracao ATE expressao'
        p[0] = Arvore('declaracao_expressao_interacao', [p[2, p[4]]])

    def p_expressao_atribuicao_1(self, p):
        'expressao_atribuicao: ID ATRIBUICAO expressao'
        p[0] = Arvore('declaracao_expressao_atribuicao', [p[3]])

    def p_expressao_leia_1(self, p):
        'expressao_leia: LEIA ABREPARENTESES expressao FECHAPARENTESES'
        p[0] = Arvore('declaracao_expressao_leia', [p[3]])

    def p_expressao_escreva_1(self, p):
        'expressao_escreva: ESCREVA ABREPARENTESES expressap FECHAPARENTESES'
        p[0] = Arvore('declaracao_expressao_escreva', [p[3]])

    def p_declara_var_1(self, p):
        'declara_var: tipo DOISPONTOS ID VIGULA declara_var_loop'
        p[0] = Arvore('declaracao_var_loop', [p[1], p[5]], p[3])

    def p_declara_var_2(self, p):
        'declara_var: tipo DOISPONTOS ID'
        p[0] = Arvore('declaracao_var', [p[1]], p[3])

    def p_declara_var_loop_1(self, p):
        'declara_var_loop: ID VIRGULA declara_var_loop'
        p[0] = Arvore('declaracao_var_var_loop', [p[3]], p[1])

    def p_declara_var_loop_2(self, p):
        'declara_var_loop: ID'
        p[0] = Arvore('declaracao_var_var', [], p[1])

    def p_retorna_1(self, p):
        'retorna: ABREPARENTESES expressao FECHAPARENTESES'
        p[0] = Arvore('declaracao_retorna', [p[2]])

    def p_chamada_funcao_1(self, p):
        'chamada_funcao: ID ABREPARENTESES parametros_chamada FECHAPARENTESES'
        p[0] = Arvore('declaracao_chamada_funcao', [p[3]], p[1])

    def p_parametros_chamada_1(self, p):
        'parametros_chamada: expressao VIRGULA parametros_chamada'
        p[0] = Arvore('parametros_chamada_expressao_loop', [p[1], p[3]])

    def p_parametros_chamada_2(self, p):
        'parametros_chamada: expressao'
        p[0] = Arvore('parametros_chamada_expressao', [p[1]])

    def p_expressao_1(self, p):
        'expressao: expressao_simples'
        p[0] = Arvore('expressao_simples', [p[1]])

    def p_expressao_2(self, p):
        'expressao: expressao_simples operadores_comparacao expressao_simples'
        p[0] = Arvore('expressao_simples_composta', [p[1], p[2], p[3]])

    def p_expressao_simples_1(self, p):
        'expressao_simples: expressao_simples operadores_atribuicao termo'
        p[0] = Arvore('expressao_simples_atribuicao', [p[1], p[2], p[3]])
    
    def p_expressao_simples_2(self, p):
        'expressao_simples: expressao_simples operadores_multiplicacao termo'
        p[0] = Arvore('expressao_simples_multiplicacao', [p[1], p[2], p[3]])

    def p_expressao_simples_3(self, p):
        'expressao_simples: termo'
        p[0] = Arvore('expressao_simples_termo', [p[1]])

    def p_termo_1(self, p):
        'termo: fator'
        p[0] = Arvore('termo_fator', [p[1]])

    def p_fator_1(self, p):
        'fator : ABREPARENTESES expressao FECHAPARENTESES'
        p[0] = Arvore('termo_fator_expressao',[p[2]])

    def p_fator_2(self, p):
        'fator: chamada_funcao'
        p[0] = Arvore('termo_fator_chamada_funcao', [p[1]])

    def p_fator_3(self, p):
        'fator: expressao_numerica'
        p[0] = Arvore('termo_fator_expressao_numerica', [p[1]])

    def p_fator_4(self, p):
        'fator: expressao_id'
        p[0] = Arvore('termo_fator_expressao_id', [p[1]])

    def p_expressao_numerica_1(self, p):
        'expressao_numerica: numero'
        p[0] = Arvore('expressao_numerica_numero', [p[1]])

    def p_expressao_id_1(self, p):
        'expressao_id: ID'
        p[0] = Arvore('expressao_id_id', [], p[1])

    def p_operadores_comparacao(self, p):
        '''
            operadores_comparacao: MAIOR
                                | MAIORIGUAL
                                | MENOR
                                | MENORIGUAL
                                | IGUALDADE
        '''
        p[0] = Arvore('operador_comparacao',[],p[1])

    def p_operadores(self, p):
        '''
        operadores: NEGACAO
                    | E
                    | OU
        '''
        p[0] = Arvore('operador', [], p[1])

    def p_operadores_atribuicao(self, p):
        '''
        operadores_atribuicao: SOMA
                            | SUBTRACAO
        '''
        p[0] = Arvore('operador_atribuicao', [], p[1])

    def p_operadores_multiplicacao(self, p):
        '''
        operadores_multiplicacao: MULTIPLICACAO
                                | DIVISAO
        '''
        p[0] = Arvore('operador_multiplicacao', [], p[1])

    def p_tipo(self, p):
        '''
        tipo: INTEIRO
            | FLUTUANTE
        '''
        p[0] = Arvore('tipo', [], p[1])

    def p_numero(self, p):
        '''
        numero: INTEIRO
                | FLUTUANTE
        '''
        p[0] = Arvore('numero', [], p[1])


    def p_vazio(self, p):
        'vazio:'

    def p_erro(self, p):
        if p:
            print("Erro Sintático: %s, linha %d \n" % (p.valor, p.lineno))
        else:
            yacc.restart()
            print("Erro Sintático: definições incompletas!")
        exit(1)
    

    def parse(self, codigo):
        lexica = AnaliseLexica()
        self.tokens = lexica.tokens
        self.precedencia = (
            ('left', 'ATRIBUICAO', 'MENORIGUAL', 'MAIORIGUAL', 'MENOR', 'MAIOR', 'IGUAL')
            ('left', 'ADICAO', 'SUBITRACAO')
            ('left', 'MULTIPLICACAO', 'DIVISAO')
            ('left', 'ABREPARENTESES', 'FECHAPARENTESES')
        )


if __name__ == '__main__':
    from sys import argv
    f = open(argv[1])
    AnaliseSintatica(f.read())
    
    print("\nConcluido!")