Boa tarde, João!

Segue o desafio para a vaga de estágio.
Você pode responder esse e-mail para nos enviar seu código.

DESAFIO: Extração do diário oficial

O desafio consiste em extrair informações do Diário Oficial da União (DOU), disponível no link https://www.in.gov.br/leiturajornal, com os seguintes parâmetros:
secao: string que pode possuir somente um dos seguintes valores: dou1, dou2, dou3
data: string de data no formato DD-MM-AAAA

Na página da imprensa (HTML), existe um script do tipo application/json com os dados de cada seção. Estes dados incluem o objeto jsonArray com o campo urlTitle. Cada seção do DOU pode ser acessada a partir da concatenação do link https://www.in.gov.br/en/web/dou/-/ com urlTitle.

O projeto depende das bibliotecas cfscrape (para lidar com o Cloudflare) e BeautifulSoup (para parsear o HTML). É necessário instalá-las antes de executar o projeto.
Comandos para instalação:
pip install cfscrape
pip install beautifulsoup4

Requisitos:
Extrair todos os diários do dia em que o script é executado;
Criar um json com a listagem dos diários (o script na página inicial);
Acessar a página de detalhamento do diário individual e criar um json com o detalhamento;
Exemplo:
{
    "versao_certificada": "http://pesquisa.in.gov.br/imprensa/jsp/visualiza/index.jsp?data=25/01/2023&jornal=515&pagina=62",
    "publicado_dou_data": "25/01/2023",
    "edicao_dou_data": "18",
    "secao_dou_data": "62",
    "orgao_dou_data": "Entidades de Fiscalização do Exercício das Profissões Liberais/Conselho Federal de Enfermagem",
    "title": "ACÓRDÃO COFEN Nº 103, DE 27 DE SETEMBRO DE 2022",
    "paragrafos": [
        "ADMINISTRATIVO. PROCESSO ÉTICO COFEN Nº 068/2021. ORIGEM PROCESSO ÉTICO COREN-RR Nº 012/2020. 545ª REUNIÃO ORDINÁRIA DE PLENÁRIO. JULGAMENTO DE PRIMEIRA INSTÂNCIA. PRERROGATIVA DE FUNÇÃO. Unanimidade dos votos. Absolvição."
    ],
    "assina": "Osvaldo Albuquerque Souza Filho",
    "cargo": "Presidente da Mesa"
}
Caso utilize mais bibliotecas, incluir um arquivo README.md no projeto, descrevendo quais precisam ser instaladas;
Critérios de avaliação:
Escopo: se o projeto está extraindo os campos solicitados da totalidade dos diários do dia;
Qualidade do código: organização, simplicidade, sem repetição e com nomes de métodos, variáveis e classes intuitivas. Documentação é importante, mas é preferível um código fácil de entender;
Execução: incluir o passo-a-passo para rodar o projeto para obter o resultado esperado;
Desafio: uso de técnicas mais avançadas será um diferencial e contará pontos a mais para a vaga;
