# Automação da Folha de Ponto com Selenium

Este projeto Python utiliza o Selenium para automatizar o lançamento de horas em um sistema de folha de ponto online. Ele foi desenvolvido para facilitar o processo de registro de horas, especialmente para aqueles que têm uma rotina de trabalho regular e previsível.

## Funcionalidades

* **Login automático:** O script realiza o login automaticamente no sistema de folha de ponto, armazenando as credenciais do usuário de forma segura e criptografada.
* **Lançamento de horas:** Lança automaticamente as horas trabalhadas para cada dia útil do mês, dividindo-as em períodos da manhã e da tarde, com um total de 8 horas de trabalho e 1 hora de intervalo para almoço.
* **Horários flexíveis:** Os horários de entrada, almoço e saída são gerados aleatoriamente dentro de intervalos predefinidos, tornando o lançamento mais realista.
* **Detalhamento da atividade:** Permite que o usuário insira o detalhamento da atividade e oferece a opção de repeti-lo para os demais dias.
* **Verificação de feriados:** Verifica se um dia é feriado nacional no Brasil e não lança atividades nesses dias.
* **Tratamento de erros:** Possui tratamento de exceções para lidar com possíveis erros durante o login, a navegação e o lançamento das atividades, tornando o script mais robusto.

## Como Executar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/wesleygurgel/pmdecision-automation.git
   ```

2. **Crie um ambiente virtual:**

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux/macOS
   source venv/bin/activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Gere a chave de criptografia:**
   * Execute o script `main.py` uma vez e a suas credenciais seram salvas de forma criptografada.
   * **Mantenha os arquivos `credentials.bin` e `chave.key` em um local seguro e não o adicione ao controle de versão!**

5. **Execute o script:**

   ```bash
   python main.py
   ```

   * Na primeira execução, o script solicitará suas credenciais de login.
   * Nas próximas execuções, o login será feito automaticamente.
   * O script perguntará o detalhamento da atividade e se você deseja repeti-lo para os outros dias.
   * O script lançará as atividades para todos os dias úteis do mês, desde o último dia lançado até o dia atual, considerando feriados.

## Observações

* **Adapte o código:**
    * Certifique-se de que os seletores CSS e XPath em `login.py` e `navigation.py` correspondem aos elementos da sua página de login e lançamento de horas. 
    * Adapte a lógica em `ponto.py` para preencher os campos específicos da sua folha de ponto.
* **Requisitos:**
    * Python 3.x
    * Selenium
    * Bibliotecas listadas em `requirements.txt`
* **Navegador:**
    * Certifique-se de ter o driver do seu navegador instalado e configurado corretamente (ChromeDriver, GeckoDriver, etc.).
* **Responsabilidade:**
    * Use este script com responsabilidade e ética.
    * Certifique-se de que o uso da automação está de acordo com as políticas da sua empresa.

**Contribuições**

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorar este projeto.