# k-Means #

## I.	 INTRODUÇÃO ##
Esse projeto tem como objetivo exemplificar a aplicação do algorítimo k-Means. O k-Means é um algoritimo de clusterisalção
utilizado quando temos um dataset não rotulado, ou seja, não sabemos quais classes pertencem os dados no dataset, porém,
no caso do k-Means, é necessário saber quantas classes diferentes tem o dataset (valor do k).

## II.	FUNDAMENTAÇÃO TEÓRICA ##

### A.	K-MEANS ###
O K-Means é um algortimo de clusterização utilizado para achar clusters e seus centros dentro de uma base de dados
não rotulados, ou seja, uma base de dados que não se sabe quais são os dados pertencentes a cada classe, porém
deve-se saber quantas classes há dentro daquela base de dados.<br>
O algoritimo padrão foi proposto por Stuart Lloyd em 1957, porém apenas em 1967 que o termo "k-means" foi empregado
por James MacQueen.
De forma geral podemos dividir os passos do algoritimo da seguinte maneira:

1. Definição do número de cluster;
2. Inicialização dos centros de cada cluster;
3. Cálculo da distancia de cada ponto em relação aos centros escolhidos e escolha da menor distância;<br>

![Alt text](images/kmeans-equation01.png?)

4. Cálculo do ponto médio dos pontos dentro de cada classe;
5. Mover o centro do cluster para o ponto médio;
6. Retornar para 3. até que o valor do centro convirja;

Um dos desafios na utilização do k-Means é saber exatamente quantas classes tem dentro de um dataset não rotulado.
Caso não tenha-se essa informação, existe uma métrica capaz de estimar quantas classes um dataset pode ter.<br>

Segundo [7] podemos utilizar o Within Cluster Sum of Squares (WCSS) que é o somatório do quadrado da diferença do ponto ao
centroide, ou seja, o quao distante os dados estão dentro de uma mesma classe.<br>

![Alt text](images/kmeans-equation02.png?)

O valor de k ótimo se da próximo ao plato da função, como segue na imagem a seguir:

![Alt text](images/kmeans-graph09.png?)

## III.	METODOLOGIA ##
Para o projeto vigente foi utilizado python juntamente com o Notebook Jupyter para prototipar o modelo do
algorítimo. A base do algorítimo foi feita utilizando Numpy e o Pandas, todas as entradas de dados nos métodos da
classe é feito via DataFrames.
Tendo como base a fundamentação teórica abordada em II, o modelo do algorítimo esta proposto em <b>"./kmeans.py"</b>.
Para o teste e análise do algorítimo utilizou-se o dataset proposto em aula pelo Reinaldo Bianchi (encontra-se 
em ./data/bianchi.csv), na qual o objetivo é segmentar o dataset em três tipos de classes não rotuladas diferentes.<br>
A segunda proposta é analisar a segmentação do k-Means utilizando outros datasets. Para esta utilizaremos:
* Iris Dataset [4]
* Haberman's Survival Data Set [5]
* Wine Quality Data Set [6]

## IV. RESULTADOS ##
Os detalhes das implementações dos problemas propostos na metodologia pode ser analisados em <b>"./k-Means.ipynb"</b> 
ou <b>"k-Means.html"</b>.<br>
O Primeiro experimento foi feito utilizando o dataset proposto pelo Reinaldo Bianchi que continha três classes:<br>

![Alt text](images/kmeans-graph01.png?)

O segundo experimento foi feito utilizando o Iris Dataset [4], em que temos a análise dos dados aplicando PCA com dois
componentes principais:<br>

![Alt text](images/kmeans-graph02.png?)<br>
![Alt text](images/kmeans-graph03.png?)<br>

O terceiro experimento foi feito utilizando o Haberman's Survival Dataset [5], em que para essa análise aplicamos o LDA e
o reduzimos a um sistema bidimensional. A seguir temos os dados apresetados pelo problema e o resultado do k-Means.<br>

![Alt text](images/kmeans-graph04.png?)<br>
![Alt text](images/kmeans-graph05.png?)<br>

O quarto experimento foi feito utilizando o Wine Quality Dataset [6], em que para essa análise aplicamos o PCA com duas
componentes principais. A seguir temos, os dados plotados sem distinção de classe, os dados com suas respectivas classes e
os dados segmentados pelo k-Means. 

![Alt text](images/kmeans-graph06.png?)<br>
![Alt text](images/kmeans-graph08.png?)<br>
![Alt text](images/kmeans-graph07.png?)<br>

## V. CONCLUSÃO ##
Dado os resultados vistos em IV podemos inferir que o k-Means chegou ao resultado esperado e graficamente é possível inferir
que o erro de classificação é relativamente baixo para o primeiro e segundo experimento, em que temos classes muito bem 
espaçadas.<br>

O experimento três tem-se uma curiosidade sobre o k-Means, analisando visualmente os dados há uma segmentação clara dos
mesmos, porém não é possível separa-los utilizando k-Means, visto no gráfico. Essa impossibilidade é causada devido ao
fato de o k-means trabalhar com os valores médios de um centroide e pela diferença dos dados no eixo X ser maior que a
diferença dos dados no eixo Y, o que faz com que ele não o segmente corretamente e trate segmentos das classes como a classe
correspondente. Uma outra análise a essa particularidade do k-Means vem que, por ser um algorítimo de clusterização, não
necessáriamente ele divida os grupos de dados da forma que queremos que ele faça, talvez haja uma correlação entre os dados,
ou seja, uma similaridade diferente da que estamos querendo propor que é mais forte para aquele grupo de dados do que as
classes propostas inicialmente.<br>

Para o quarto experimento foi utilizado PCA, porém é visto claramente que as classes dos dados quando aplica-se PCA se confundem
pela correlação das informações propostas, ou seja, é impossível de separar os dados da forma que foi apresentada, porém o
k-Means chega a uma segmentação superficial dos dados.<br>
Como não foi utilizado nenhum indicador de performance dos métodos abordados, podemos avaliar a difenreça entre os
experimentos apenas de forma visual.<br>

## VI. AGRADECIMENTOS ##

Agradecimentos especiais a CAPES e ao Centro Universitário FEI por financiar o mestrado que está em curso; 
ao professor Reinaldo Bianchi por proporcionar visões sobre o mundo acadêmico e orientar trabalhos científicos 
com o objetivo de lapidar os conhecimentos abordados em sala; aos meus pais e a minha família que sempre me 
apoiaram em meio a dificuldades.

## VII. REFERÊNCIAS ##

[1] S. Raschka, Linear Discriminant Analysis, 08/2014, link: https://sebastianraschka.com/Articles/2014_python_lda.html, acessado em 11/2019<br>
[2] S. Balakrishnama, A. Ganapathiraju, LINEAR DISCRIMINANT ANALYSIS - A BRIEF TUTORIAL, Institute for Signal and Information Processing, Department of Electrical and Computer Engineering.
[3]	R. Bianchi, Tópicos Especiais em Aprendizagem, 2019, ppt slide Centro Universitário FEI.
[4] UCI, Machine Learning Repository, link: https://archive.ics.uci.edu/ml/datasets/Iris, acessado em 11/2019
[5] UCI, Machine Learning Repository, link: http://archive.ics.uci.edu/ml/datasets/Haberman%27s+Survival, acessado em 11/2019
[6] UCI, Machine Learning Repository, link: http://archive.ics.uci.edu/ml/datasets/Wine+Quality, acessado em 11/2019
[7] C. Maklin, K-means Clustering Python Example, 12/2018, link: https://towardsdatascience.com/machine-learning-algorithms-part-9-k-means-example-in-python-f2ad05ed5203, acessado em 11/2019