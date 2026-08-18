// Aguarda o pywebview carregar antes de permitir chamadas
window.addEventListener('pywebviewready', function() {
    console.log("Pywebview está pronto!");
});

function EnviaSenha() {
    let senha_digitada = document.getElementById('visor').value;

    // Garante que o pywebview e a api existem antes de chamar
    if (window.pywebview && window.pywebview.api) {
        pywebview.api.verifica_recebeu(senha_digitada).then(function(resposta) {
            document.getElementById('resultado').innerText = resposta;
        });
    } else {
        console.error("API do pywebview ainda não foi carregada.");
    }
}