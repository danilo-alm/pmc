# PMC

Este programa foi criado para pesquisar PMCs(Preços Máximos ao Consumidor) de remédios. Ele utiliza o arquivo .xls que pode ser encontrado no site da [Anvisa](https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/cmed/precos).

## Uso
Mova o arquivo .xls para o diretório do programa e, apenas uma vez, execute "converter.py". Após isso, quando quiser pesquisar o PMC de algum remédio, execute "pesquisar.py" e forneça o nome ou código de barras do medicamento. A tabela é atualizada mensalmente, então se desejar, faça sempre o download da tabela mais atual, mova-a para o diretório e execute "converter.py" novamente.

## Exemplo de uso:

./converter.py:
```
python converter.py
Procurando arquivo .xls...
Criando arquivo .data...
Lendo .xls...
Remedios comecam na fileira 49
Convertendo dados...
Organizando remedios...
Escrevendo dados...
Convertido com sucesso!
Tempo total: 16 segundos
```

./pesquisar.py:
```
python pesquisar.py
----------------------------------------------
Remédio: annita
Laboratório (opcional):

Resultados:
####################################################################################################

Nome: ANNITA 20 MG/ML (FARMOQUÍMICA S/A)
Substância: NITAZOXANIDA
Apresentação: 20 MG/ML PÓ SUS OR CT FR VD AMB X 100 ML + SER DOS
Tipo de Produto: Novo
Tarja: Tarja Vermelha(*)
PMC: 86,37

####################################################################################################

Nome: ANNITA 20 MG/ML (FARMOQUÍMICA S/A)
Substância: NITAZOXANIDA
Apresentação: 20 MG/ML PÓ SUS OR CT FR VD AMB X 45 ML + SER DOS
Tipo de Produto: Novo
Tarja: Tarja Vermelha(*)
PMC: 41,71

####################################################################################################

Nome: ANNITA 500 MG (FARMOQUÍMICA S/A)
Substância: NITAZOXANIDA
Apresentação: 500 MG COM REV CT BL AL PLAS PVC TRANS X 6\xa0
Tipo de Produto: Novo
Tarja: Tarja Vermelha(*)
PMC: 99,73

----------------------------------------------------------------------------------------------------
Ultima Pesquisa:
Remédio: ANNITA
Laboratório:
----------------------------------------------------------------------------------------------------
Remédio:
```
