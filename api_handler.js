// js/api_handler.js

const formProduto = document.getElementById('form-produto');
const feedback = document.getElementById('feedback-mensagem');

formProduto.addEventListener('submit', async (e) => {
    e.preventDefault(); // Impede o recarregamento da página

    // Captura os valores dos inputs do seu HTML
    const dadosParaEnviar = {
        nome: document.getElementById('nome-produto').value,
        marca: document.getElementById('marca-produto').value,
        preco: parseFloat(document.getElementById('preco-produto').value),
        descricao: document.getElementById('descricao-produto').value
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/api/produtos/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dadosParaEnviar) // Transforma em JSON para o Serializer ler
        });

        const data = await response.json();

        if (response.ok) {
            feedback.innerHTML = '<p style="color: green;">Produto cadastrado com sucesso!</p>';
            formProduto.reset();
        } else {
            // Aqui o JavaScript exibe os erros que você configurou no Django Serializer
            // Ex: "O preço deve ser maior que zero."
            feedback.innerHTML = `<p style="color: red;">Erro: ${Object.values(data)[0]}</p>`;
        }
    } catch (error) {
        feedback.innerHTML = '<p style="color: red;">Erro ao conectar com o servidor.</p>';
    }
});