Para essa atividade, foi necessário dividí-la em 3 principais etapas:

- Extrair todas as informações de cada tabela do Brasileirão, dos anos de 2012 a 2023;
- Captar essas informações e produzir um conjunto de dados com todas essas informações;
- Realizar a análise, respondendo todas as perguntas contidas no arquivo 'perguntas.txt' (que eu mesmo escrevi);

Na primeira etapa, eu utilizei como referência o site oficial da CBF (https://www.cbf.com.br/futebol-brasileiro). 
Nele, com o auxílio da biblioteca BeautifulSoup, foi possível desenvolver uma função para extrair as informações da tabela na página especificada, através do ano. A função está presente no arquivo 'adquirir_infos.py'.

Dessa forma, pude importar essa função para o arquivo da segunda etapa, o 'gerar_tabela.ipynb'. Nele, eu utilizei loops pra gerar as colunas das edições e das colocações, e também para captar as informações dos anos de 2012 a 2023, utilizando a função que criei.
Com isso, armazenei todas as informações num DataFrame e, com ele, gerei um arquivo CSV, o 'brasileirao_2012_a_2013.csv'.

E, com esse arquivo em mãos, pude partir para a terceira etapa e realizar a análise dele, dentro do arquivo 'analise.ipynb', respondendo, como dito anteriormente, algumas questões que desenvolvi para esse projeto. 
Dividi o notebook por seções pra cada enunciado para melhorar a organização, além do desenvolvimento de gráficos (utilizando a biblioteca Plotly) para uma visualização ainda melhor.
