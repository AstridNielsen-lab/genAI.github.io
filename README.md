```markdown
# Projeto GenAI

## Descrição

Este projeto utiliza uma API para gerar imagens a partir de prompts fornecidos pelo usuário.
Ele é desenvolvido em Python usando o framework Flask e possui uma interface web simples.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework para desenvolvimento web.
- **HTML/CSS**: Para estruturação e estilização da interface.
- **API**: Utilizada para gerar imagens a partir de prompts.

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/AstridNielsen-lab/genAI.github.io.git
   cd genAI
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o aplicativo:**
   ```bash
   python app.py
   ```

5. **Acesse o aplicativo:**
   Abra um navegador e acesse `http://127.0.0.1:5000`.

## Estrutura do Projeto

```
genAI/
│
├── app.py              # Código principal do aplicativo Flask
├── templates/          # Diretório para arquivos HTML
│   └── index.html      # Página principal
├── static/             # Diretório para arquivos estáticos (CSS, JS)
└── requirements.txt     # Dependências do projeto
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
```
