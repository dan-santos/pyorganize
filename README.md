# Pyorganize
Você já se deparou com sua pasta de "Downloads" ou "Documentos" cheia de arquivos que não necessariamente deveriam estar "soltos" ali? Tenho certeza que sim.
Por causa disso, resolvi escrever esse script em Python que vai separar esses arquivos da pasta em subdiretórios de acordo com a extensão dos mesmos.

## Como usar
#### Instalando
Primeiramente, você precisa ter o interpretador Python instalado na sua máquina.
Se você usa sistemas operacionais baseados em UNIX (Linux/Mac), é provável que você já tenha ele instalado. Para verificar isso 
independente de seu SO, abra o terminal/shell/cmd e digite o seguinte comando:

    python --version

Ele deve retornar a versão do interpretador Python do seu computador. Se ele retornar algum erro, é bem provável que você ainda não tenha ele instado.

- Se você usa Windows, [aqui](https://python.org.br/instalacao-linux/) está o tutorial de como você deve instalá-lo.</br>
- Se você usa Linux, [aqui](https://python.org.br/instalacao-linux/) está o tutorial de como você deve instalá-lo.</br>
- Se você usa Mac, [aqui](https://python.org.br/instalacao-mac/) está o tutorial de como você deve instalá-lo.</br>

#### Atualizando
Mas se você já tem ele instalado, assegure-se de que está usando uma versão igual ou superior a 3.5.
Para verificar se está tudo funcionando, você pode abrir o seu terminal/shell/cmd e digitar o mesmo comando da seção anterior.

#### Só falta mais uma coisinha que você precisa saber... eu prometo!
Agora, com o interpretador Python devidamente instalado no seu computador, você só precisa pegar o arquivo `organize.py` deste repositório e adicioná-lo
<strong>no mesmo nível</strong> da pasta que você deseja organizar. Isto é, se você quer organizar a pasta `C:\Users\seu-user\Downloads`, você precisa deixar o 
script no caminho `C:\Users\seu-user\organize.py`.

#### Finalmente, organizando tudo!
Depois de ter seguido os passos anteriores, esta é a parte mais fácil :)</br>
- Se você está no <strong>Windows</strong>, dê duplo clique no arquivo `organize.py`, ele vai abrir o seu terminal perguntando qual pasta você quer organizar 
daquele diretório que o script está. Basta você digitar o nome da pasta sem aspas que o algoritmo será executado e mostrará para você a origem/destino de 
cada arquivo.</br>
- Se você está no <strong>Linux/Mac</strong>, abra o seu terminal e digite o comando: `python organize.py`.</br>
Após isso, ele irá te perguntar qual das pastas presentes naquele diretório você quer organizar. Basta você digitar o nome da pasta sem aspas que o algoritmo será 
executado e mostrará para você a origem/destino de cada arquivo.</br>
> Se você usa o <strong>Linux Mint</strong> ou outra distribuição GNU/Linux que depende do Python 2, é bem provável que o comando acima não vá funcionar, pois 
mesmo você tendo instalado alguma versão do Python 3, o comando `python` do seu terminal ainda se referencia ao interpretador do Python 2. Mas, para resolver isso é bem simples :)</br>
Basta você criar um ambiente virtual (venv) na pasta atual do nosso aquivo `organize.py` ou usar o interpretador de algum venv já criado. Para fazer isso, 
siga os passos da [documentação oficial do Python](https://docs.python.org/pt-br/3/tutorial/venv.html).
---

> <strong>OBSERVAÇÃO: </strong> Se ao executar o comando seu terminal indicar que o algoritmo precisa de permissões especiais de administrador/root/sudo para 
acessar ou manipular uma pasta, eu recomendo fortemente que você <strong>NÃO</strong> dê essa permissão a ele (a menos que você realmente saiba o que está fazendo),
pois é provável que você esteja querendo organizar uma pasta do sistema que possui referências de outros programas. Logo, uma vez movido, essa ação não pode 
ser desfeita, o que pode acarretar em problemas irreversíveis de diversas origens na sua máquina.



## Como contribuir
Inclui apenas as extensões mais usadas de cada "tipo" de arquivo para não sobrecarregar o script de maneira desnecessária. No entanto, se você sentiu falta de 
algum tipo de arquivo ou extensão no algoritmo e acha que ela pode ser útil (ou apenas deseja contribuir no repositório para aprimorá-lo), sinta-se a vontade 
para criar uma pull request minimamente explicativa/documentada :)



