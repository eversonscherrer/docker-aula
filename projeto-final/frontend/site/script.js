const form = document.getElementById("form-mensagem");
const campoNome = document.getElementById("nome");
const campoMensagem = document.getElementById("mensagem");
const lista = document.getElementById("lista-mensagens");
const status = document.getElementById("status");

function criarItemMensagem(msg) {
  const item = document.createElement("li");

  const autor = document.createElement("strong");
  autor.textContent = msg.nome;

  // Usamos createTextNode em vez de innerHTML: o conteudo vem de outros
  // visitantes, entao nunca deve ser interpretado como HTML/JS (evita XSS).
  const texto = document.createTextNode(": " + msg.mensagem);

  const data = document.createElement("time");
  data.textContent = new Date(msg.criado_em).toLocaleString("pt-BR");

  item.appendChild(autor);
  item.appendChild(texto);
  item.appendChild(data);
  return item;
}

async function carregarMensagens() {
  const resposta = await fetch("/api/mensagens");
  const mensagens = await resposta.json();

  lista.innerHTML = "";
  mensagens.forEach((msg) => lista.appendChild(criarItemMensagem(msg)));
}

form.addEventListener("submit", async (evento) => {
  evento.preventDefault();
  status.textContent = "Enviando...";

  const resposta = await fetch("/api/mensagens", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      nome: campoNome.value,
      mensagem: campoMensagem.value,
    }),
  });

  if (resposta.ok) {
    form.reset();
    status.textContent = "Mensagem enviada!";
    carregarMensagens();
  } else {
    status.textContent = "Erro ao enviar mensagem. Tente de novo.";
  }
});

carregarMensagens();
