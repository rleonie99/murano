import csv
import statistics

def main():
    caminho = r'C:\Users\Leonie\Desktop\MuranoEstagio\Output\planilha.csv'
    escreverDados(caminho)
    
# Escrita de Dados
def escreverDados(caminho):
    with open(caminho, 'w') as arquivo:
        writer = csv.writer(arquivo)

        print('Entre com os dados. Entradas iguais a 0 fecharao a aplicacao de entrada dos dados.')
        writer.writerow(["DRE", "Curso", "Nome", "Genero", "Data de Nascimento", "Altura", "Peso", "CRA", "Creditos Obtidos", "Renda"])

        i = 1
        e = 0
        somaEngenharia = 0
        somaFeminino = 0
        peso = []
        cra = []
        mediaIdade = 0
        mediaAltura = 0
        somaCreditos = 0
        mediaRenda = 0
        while True:
            dre = input('\nDRE Aluno %d: ' % i)
            if (dre == '0') :
                break
            
            curso = input('Curso Aluno %d: ' % i)
            if (curso == '0') :
                break
            if (curso == 'Engenharia'):
                somaEngenharia = somaEngenharia + 1
                e = e + 1
                
            nome = input('Nome Aluno %d: ' % i)
            if (nome == '0') :
                break
            
            genero = input('Genero Aluno %d: ' % i)
            if (genero == '0') :
                break
            if (genero == 'Feminino') :
                somaFeminino = somaFeminino + 1
                
            dataNasc = input('Data de Nascimento Aluno %d (DD/MM/AAAA): ' % i)
            if (dataNasc == '0') :
                break
            idade = 2020 - int(dataNasc[6:])
            mediaIdade = mediaIdade + idade

            altura = eval(input('Altura Aluno %d (m): ' % i))
            if (altura == 0) :
                break
            mediaAltura = mediaAltura + altura

            massa = eval(input('Massa Aluno %d (Kg): ' % i))
            if (massa == 0) :
                break
            peso.append(massa)

            cra = eval(input('CRA Aluno %d: ' % i))

            creditos = eval(input('Creditos Obtidos Aluno %d: ' % i))
            somaCreditos = somaCreditos + creditos

            renda = eval(input('Renda Aluno %d (R$): ' % i))
            mediaRenda = mediaRenda + renda

            writer.writerow([dre, curso, nome, genero, dataNasc, altura, massa, cra, creditos, renda])
            i = i + 1

        mediaIdade = mediaIdade / (i-1)
        mediaAltura = mediaAltura / (i-1)
        mediaRenda = mediaRenda / (i-1)

        print('\n%d alunos sao de Engenharia. ' % (somaEngenharia))
        print('%d alunas mulheres. ' % (somaFeminino))
        print('Media de idade: %.1f anos' % (mediaIdade))
        print('Media de altura (m): %.2f' % (mediaAltura))
        print('Total de Creditos de todos os alunos: %d' % (somaCreditos))
        print('Media de Renda de todos os alunos: R$ %.2f' % (mediaRenda))
