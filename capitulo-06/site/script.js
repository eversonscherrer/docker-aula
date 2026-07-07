let cliques = 0;

const botao = document.getElementById("botao");
const contador = document.getElementById("contador");

botao.addEventListener("click", () => {
  cliques++;
  contador.textContent = `${cliques} clique${cliques === 1 ? "" : "s"}`;
});
