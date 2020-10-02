Este é um projeto referente a disciplina de Geometria Analítica na Universidade Federal de São Paulo ofertada no primeiro semestre de 2020.

Este projeto está em desenvolvimento e poderá ter novas funcionalidades adicionadas com o passar do tempo.

Esta biblioteca é uma ferramenta para estudantes de Geometria Analítica que visa facilitar o aprendizado dos conceito abordados na matéria por meio da validação dos resultados obtidos.
Com essa ferramenta o estudante pode validar os resultados obtidos em seu estudo comparando-os com os resultados retornados das funções presentes nesta biblioteca.

Note que, mesmo com uma biblioteca como essa que visa simplificar o aprendizado, competências de traduzir notações de planos e retas ainda se fazem necessárias para a sua plena utilização.

A biblioteca GA_lib não apresenta resultados intermediários para se obter o resultado final, entretando, pode-se consultar sua documentação para entendimento das etapas necessárias para a obtenção dos resultados.

INSTALAÇÃO

Certifique-se de ter a biblioteca numpy instalada. Por via das dúvidas, o comando para instalação de numpy é

$ pip install numpy

Outra biblioteca importante para plotagem dos gráficos é a matplotlib, que pode ser instalada por 

$ pip install matplotlib

Agora vá até o diretório que deseja instalar a biblioteca e execute

$ git clone https://github.com/Almeidadm/GA_lib.git
 
 Acesse a pasta "GA_lib" e então
 
 $ pip install ./dist/GA_lib-0.1.0-py3-none-any.whl
 
 E agora você pode usar a biblioteca em qualquer programa utilizando a linguagem python3 a partir da importação
 
 \>\> from GA_lib import GA
 
 CONSIDERAÇÕES SOBRE FORMATOS
 
 Como essa ferramenta visa facilitar o aprendizado do aluno algumas representações são simplificadas e podem gerar ambiguidades em sua utilização. 
 Dessa forma um ponto p = (x, y, z) será representado como uma lista simples 
 >[x, y, z]
 E de maneira similar, um vetor v = (x, y, z) será
 >[x, y, z]
 
 Isso exige que o aluno saiba qual o tipo de resultado que deverá ser esperado no retorno daquela dada função.
 
EXEMPLOS DE USO

 Distância entre um ponto e uma linha
 
   A distância entre um ponto e uma linha é definida por
   
   ![img1](https://user-images.githubusercontent.com/47041221/94879427-8d484180-0436-11eb-8648-87ffbb223738.jpg)
 
   Onde M1 é um ponto na linha s e M0 é o ponto de interesse. A função em GA_lib para resolver este problema exige que você insira dois pontos pertencentes a reta em questão, e também o ponto de interesse. Os parâmetros Lponto1 e Lponto2 são os pontos que permitem a construção da reta.
   
   Entrada:
   
   \>\> GA.distancia_ponto_linha(Lponto1=[1,2,5], Lponto2=[-3, -1, -2], ponto=[-2, 8, -1], plot=True)
   
   Saída:
   
   ![Figure_1](https://user-images.githubusercontent.com/47041221/94928448-15136780-049a-11eb-8e01-f4db2552aaa0.png)

   
   \>\> 7.967840766888259
   
  Distância entre um ponto e um plano
   
   A distância entre um ponto P e um plano pi:X=A+B+C+D é definido por

   ![img2](https://user-images.githubusercontent.com/47041221/94880006-35123f00-0438-11eb-9b78-61692a09df38.jpg)
   
   Note, porém, que a entrada desta função não requer o vetor v=[A, B, C] normal ao plano pi, mas apenas dois vetores LI que construam o plano em questão e um ponto pertencente a este plano. Assim, vetor1 e vetor2 são LI que constroem o plano pi e ponto_plano é um ponto pertencente ao plano pi. Análogamente, o parâmetro ponto é o ponto de interesse.
   
   Para isso, temos a  Entrada:
   
   \>\> GA.distancia_ponto_plano(vetor1=[-3, -6, -1], vetor2=[-5, -3, -5], ponto_plano=[1, 5, 3], ponto=[3, -5, 2], plot=True)
   
   Saída:
   
   ![Figure_2](https://user-images.githubusercontent.com/47041221/94928977-da5dff00-049a-11eb-9fc1-303c509f871c.png)

   
   \>\> 4.910618416080245
    
  Ângulo entre dois vetores 
   
   O cosseno do ângulo entre dois vetores v1 e v2 é definido pelo módulo do produto escalar entre v1 e v2 dividido pelo módulo de v1 vezes o módulo de v2, isto é
   
   ![img3](https://user-images.githubusercontent.com/47041221/94880628-db127900-0439-11eb-8632-a9f4db4bbf2c.jpg)
  
   A ferramenta retorna o valor do ângulo entre os vetores em graus. 

   Entrada:
 
   \>\> GA.angulo_entre_vetores(vetor1=[ 5, -30, 25], vetor2=[25, -15, -15])
   
   Saída:
   
   \>\> 81.08675878843925
   
 Distância entre dois planos paralelos
 
  Como os planos são paralelos, podemos representar pi1: X1 = A + B + C + D1 e pi2: X2 = A + B + C + D2, dessa forma temos que a distância entre eles é de
  
  ![img4](https://user-images.githubusercontent.com/47041221/94880938-d39f9f80-043a-11eb-891c-8a2fd28948fe.jpg)

  Neste caso, os parâmetros necessários são A, B, C, D1 e D2, veja:
  
  Entrada
  
  \>\> GA.distancia_entre_planos(A=-9, B=-4, C=2, D1=20, D2=54)
  
  Saída
  
  \>\> 3.383126446713963
  
 Produto escalar
  
  O produto escalar entre dois vetores v e u é definido por
  
  ![img5](https://user-images.githubusercontent.com/47041221/94881385-b7503280-043b-11eb-8b8e-d8b20a773ec0.jpg)

  Logo, os únicos parâmetros necessários para essa ferramenta são v e u.
  
  Entrada:
  
  \>\> GA.produto_escalar([1,1,1], [1,1,1])
  
  Saída
  
  \>\> 3
  
 Produto vetorial
 
  O produto vetorial exige uma explicação mais elaborada, apesar de comumente não ser um desafio aos estudantes regulares. Uma abordagem didática sobre esta operação pode ser encontrada em qualquer livro de Geometria Analítica. Ainda assim, para a obtenção do produto vetorial entre dois vetores, basta que façamos
  
  Entrada:
  
  \>\> GA.produto_vetorial(vetor1=[-7, -2, -1], vetor2=[-5, -5, -5])
  
  Saída:
  
  \>\> [5, -30,  25]
  
 Adicionais
 
  Para facilitar as operações acima, ainda foram implemetados métodos responsáveis por, por exemplo, instanciar um vetor a partir de dois pontos
  
  Entrada:
  
  \>\> GA.vetor([1,2], [7, 10])
  
  Saída:
  
  \>\> [6, 8]
  
  E também uma responsável pelo módulo de um dado vetor
  
  Entrada:
  
  \>\> GA.modulo(vetor=[5, 0])
  
  \>\> 5.0
 
  ...
