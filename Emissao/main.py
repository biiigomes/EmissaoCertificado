
from datetime import date
from PIL import Image, ImageFont, ImageDraw

#informações sobre o que irá no certificado
pessoa = (356,330)
responsavel = (438, 634)
tipoTreinamento = (711, 416)
horasTreinamento = (500, 445)
cdata = (478, 473)

#fazendo as informações serem escritas no certificado
imagem = Image.open(r'Certificado.png')
caminho_fonte = r'C:Windows\Fonts\ARIALN.TTF'
font = ImageFont.truetype(caminho_fonte, 30)
rgb_preto = (0,0,0)

#input das informações que serão escritas
nome_pessoa = str(input("Digite o nome do aluno: "))
nome_responsavel = str(input("Digite o nome do responsável: "))
Treinamento = str(input("Digite o tipo do treinamento: "))
hTreinamento = str(input("Digite as horas de duração do treinamento: "))
data = date.today().strftime('%d/%m/%y')

#escreve no certificado
desenho = ImageDraw.Draw(imagem)
desenho.text(pessoa, nome_pessoa, font = font, fill = rgb_preto)
desenho.text(tipoTreinamento, Treinamento, font = font, fill = rgb_preto)
desenho.text(horasTreinamento, hTreinamento, font = font, fill = rgb_preto)
desenho.text(cdata, data, font = font, fill = rgb_preto)
desenho.text(responsavel, nome_responsavel, font = font, fill = rgb_preto)
imagem.save(f'{nome_pessoa}.png')
Image.show()

