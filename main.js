document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('cadastroForm');
    const senha = document.getElementById('senha');
    const confirmarSenha = document.getElementById('confirmarSenha');
    const cep = document.getElementById('cep');
    const erroMensagem = document.getElementById('erro-mensagem');

    // Função para exibir mensagem de erro
    function exibirErro(mensagem) {
        erroMensagem.textContent = mensagem;
        erroMensagem.style.display = 'block';
    }

    // Função para limpar a mensagem de erro
    function limparErro() {
        erroMensagem.textContent = '';
        erroMensagem.style.display = 'none';
    }

    // 1. Tratamento e validação do CEP (máscara e formato)
    cep.addEventListener('input', (e) => {
        let valor = e.target.value.replace(/\D/g, ''); // Remove tudo que não for dígito
        e.target.value = valor; // Reinsere o valor limpo

        limparErro();
    });

    // 2. Validação da Confirmação de Senha
    function validarSenhas() {
        if (senha.value !== confirmarSenha.value) {
            exibirErro('As senhas não coincidem. Por favor, verifique.');
            // Adiciona borda de erro nos campos
            senha.style.borderColor = '#c40000';
            confirmarSenha.style.borderColor = '#c40000';
            return false;
        } else {
            // Remove a borda de erro se estiver OK
            senha.style.borderColor = '';
            confirmarSenha.style.borderColor = '';
            limparErro();
            return true;
        }
    }

    // Adiciona validação em tempo real ao digitar a confirmação
    confirmarSenha.addEventListener('blur', validarSenhas);
    confirmarSenha.addEventListener('input', limparErro);
    senha.addEventListener('input', limparErro);

    // 3. Submissão do Formulário
    form.addEventListener('submit', (e) => {
        e.preventDefault(); // Impede o envio padrão do formulário

        if (!validarSenhas()) {
            // Se as senhas não coincidirem, para a submissão
            return;
        }

        // Validação adicional do CEP (8 dígitos)
        if (cep.value.length !== 8) {
            exibirErro('O CEP deve conter exatamente 8 dígitos numéricos.');
            cep.focus();
            return;
        }

        // Se todas as validações de front-end passarem
        limparErro();

        // Coleta dos dados do formulário
        const dadosCadastro = {
            nome: document.getElementById('nome').value,
            email: document.getElementById('email').value,
            senha: senha.value, // A senha confirmada é igual a esta
            cep: cep.value
        };

        // --- SIMULAÇÃO DA CHAMADA À API (Futura Integração) ---

        console.log('Dados prontos para envio ao Backend:', dadosCadastro);
        
        // Nesta etapa, você faria a requisição POST para sua API:
        /*
        fetch('SUA_URL_DA_API/cadastro', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dadosCadastro),
        })
        .then(response => response.json())
        .then(data => {
            if (data.sucesso) {
                alert('Cadastro realizado com sucesso! Redirecionando...');
                // window.location.href = '/login';
            } else {
                exibirErro('Erro no cadastro. ' + (data.mensagem || 'Tente novamente.'));
            }
        })
        .catch(error => {
            console.error('Erro na requisição:', error);
            exibirErro('Não foi possível conectar ao servidor. Verifique sua rede.');
        });
        */

        // Para a simulação, mostra um alerta de sucesso
        alert('Simulação: Dados validados e prontos para serem enviados ao backend!');
    });
});