// Lista vazia que será preenchida automaticamente durante o processo de cadastro
var categorias = [];

// Função para adicionar uma nova categoria
function adicionarCategoria() {
    var nomeCategoria = document.getElementById('nomeCategoria').value;
    var idCategoria = categorias.length + 1; // Gera um ID simples para a categoria

    // Adiciona a nova categoria na lista
    categorias.push({ id: idCategoria, nome: nomeCategoria });

    atualizarTabelaCategorias();

    // Limpa o campo de entrada para poder adicionar uma nova categoria sem precisar apagar tudo sempre
    document.getElementById('nomeCategoria').value = '';
}

// Função para atualizar a tabela de categorias
function atualizarTabelaCategorias() {
    var tabela = document.getElementById('tabelaCategorias');
    tabela.innerHTML = ''; // Limpa a tabela antes de atualizar

    // Adiciona as categorias na tabela
    categorias.forEach(function(categoria) {
        var newRow = tabela.insertRow();
        var cell1 = newRow.insertCell(0);
        var cell2 = newRow.insertCell(1);
        cell1.innerHTML = categoria.id;
        cell2.innerHTML = categoria.nome;
    });
}

// Adiciona um evento de envio ao formulário
document.getElementById('categoriaForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio do formulário padrão
    adicionarCategoria();
});
