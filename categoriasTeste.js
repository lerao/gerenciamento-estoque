// Carregar categorias do localStorage se elas existirem
var categorias = JSON.parse(localStorage.getItem('categorias')) || [];

function adicionarCategoria() {
    var nomeCategoria = document.getElementById('nomeCategoria').value;
    var idCategoria = categorias.length + 1;
    categorias.push({ id: idCategoria, nome: nomeCategoria });

    // Salvar as categorias no localStorage
    localStorage.setItem('categorias', JSON.stringify(categorias));

    atualizarTabelaCategorias();
    document.getElementById('nomeCategoria').value = '';
}

// Função para inicializar a tabela com as categorias existentes
function inicializarTabelaCategorias() {
    var tabela = document.getElementById('tabelaCategorias');
    categorias.forEach(function(categoria) {
        var newRow = tabela.insertRow();
        var cell1 = newRow.insertCell(0);
        var cell2 = newRow.insertCell(1);
        cell1.innerHTML = categoria.id;
        cell2.innerHTML = categoria.nome;
    });
}

// Inicializar a tabela quando a página carrega
document.addEventListener('DOMContentLoaded', function() {
    inicializarTabelaCategorias();
});

document.getElementById('categoriaForm').addEventListener('submit', function(event) {
    event.preventDefault();
    adicionarCategoria();
});
