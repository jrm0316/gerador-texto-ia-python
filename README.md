# gerador-texto-ia-python

Propósito do projeto
- O propósito deste projeto é demonstrar, de forma simples e direta, como integrar um modelo de linguagem (LLM) em um script Python para geração automática de conteúdo textual, incluindo a persistência do resultado em arquivo.
- O projeto foca em mostrar o fluxo essencial de uma aplicação com IA:
prompt → modelo → resposta → armazenamento, servindo como base para automações, geração de documentação e scripts inteligentes.


Como a IA responde
A IA recebe um prompt fixo contendo uma solicitação objetiva e retorna uma explicação curta e clara voltada para iniciantes.
A resposta gerada:
- é exibida diretamente no terminal
- é capturada como texto puro
- é salva em um arquivo .txt com encoding UTF-8
- Esse comportamento simula o uso da IA como um gerador automático de conteúdo, sem depender de interfaces gráficas ou APIs externas.


Tecnologias e conceitos utilizados
- Python
- Groq (LLM)
- LangChain (integração com modelo de linguagem)
- Variáveis de ambiente (python-dotenv)
- File I/O (leitura e escrita de arquivos)
- Encoding UTF-8
- Automação de geração de texto com IA


📂 Estrutura do projeto
assistente-educacional-langchain/
│
├── main.py
├── resposta_python.txt
├── .env
└── README.md


Como executar o projeto
  1.) Clonar o repositório
git clone https://github.com/seu-usuario/assistente-educacional-langchain.git
cd assistente-educacional-langchain

  2.) Instalar as dependências
pip install langchain langchain-groq python-dotenv

  3.) Configurar a variável de ambiente
Crie um arquivo .env e adicione sua chave da Groq:

GROQ_API_KEY=SUA_CHAVE_AQUI

  4.) Executar o script
python main.py


Alterando o tema analisado
- Para alterar o conteúdo gerado pela IA, basta modificar o texto do prompt no código:

    prompt = "Explique o que é Python para iniciantes, em poucas linhas."

Exemplos de temas possíveis:
- JavaScript
- APIs REST
- SQL
- Docker
- Inteligência Artificial
- Redes de Computadores


Por que este projeto é relevante?
Este projeto é relevante porque demonstra, de forma objetiva:
- integração real com um modelo de linguagem
- uso de IA em scripts backend
- automação de geração de conteúdo
- persistência de resultados gerados por IA
- boas práticas no uso de variáveis de ambiente e encoding
Esses conceitos são amplamente utilizados em sistemas modernos que incorporam IA em fluxos internos.


Resumo profissional
- Script em Python que integra um modelo de linguagem (LLM) via LangChain e Groq para geração automática de conteúdo textual, com exibição em terminal e salvamento em arquivo, aplicando boas práticas de backend e automação.

Possíveis evoluções do projeto
- Uso de PromptTemplate para prompts dinâmicos
- Entrada de dados via terminal (CLI interativo)
- Salvamento em formatos .md ou .json
- Geração de múltiplos arquivos automaticamente
- Integração com API (FastAPI)
- Análise de arquivos externos

Licença
- Projeto desenvolvido para fins educacionais e demonstração técnica.
