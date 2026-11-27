// Só a lógica do seletor de idioma. Os textos ficam em lang/<idioma>.json
// (para mudar um texto ou acrescentar um idioma, não precisa mexer aqui).
// Sem o arquivo de idioma, a página fica em inglês (o texto que já está no HTML).
var RTL = { ar: true, he: true, fa: true, ur: true };
var select = document.getElementById("lang");
var codes = [];

function getJSON(path) {
  return fetch(path).then(function (r) {
    if (!r.ok) throw new Error(path);
    return r.json();
  });
}

function pickLang() {
  var q = /[?&]lang=([a-z]{2})/.exec(location.search);
  if (q && codes.indexOf(q[1]) >= 0) return q[1];
  try {
    var s = localStorage.getItem("lang");
    if (s && codes.indexOf(s) >= 0) return s;
  } catch (e) {}
  var list = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || "en"];
  for (var i = 0; i < list.length; i++) {
    var c = String(list[i]).slice(0, 2).toLowerCase();
    if (codes.indexOf(c) >= 0) return c;
  }
  return "en";
}

function apply(code) {
  return getJSON("lang/" + code + ".json").then(function (t) {
    var nodes = document.querySelectorAll("[data-i18n]");
    for (var i = 0; i < nodes.length; i++) {
      var v = t[nodes[i].getAttribute("data-i18n")];
      if (v) nodes[i].textContent = v;
    }
    document.documentElement.lang = code === "pt" ? "pt-BR" : code === "zh" ? "zh-Hans" : code;
    document.documentElement.dir = RTL[code] ? "rtl" : "ltr";
    select.value = code;
    try { localStorage.setItem("lang", code); } catch (e) {}
  }).catch(function () { /* fica em inglês */ });
}

// Janela de vídeo: os botões com data-video abrem o vídeo por cima do site.
// Sem JavaScript, o link continua levando ao YouTube (href normal).
// Com data-playlist (a playlist do jogo no YouTube), as setinhas ‹ › passam
// pelos vídeos do mesmo jogo e, quando um acaba, o próximo começa sozinho.
// Vídeo novo entra na playlist do jogo no YouTube e aparece aqui sem mexer no site.
var modal = document.getElementById("video-modal");
var frame = modal.querySelector(".vmodal-frame");
var lastBtn = null;
var player = null;
var apiPromise = null;

// O programa do YouTube que deixa as setinhas mandarem no vídeo.
// Só é baixado quando alguém abre um vídeo com playlist.
function loadYouTubeApi() {
  if (apiPromise) return apiPromise;
  apiPromise = new Promise(function (resolve, reject) {
    if (window.YT && window.YT.Player) { resolve(); return; }
    var prev = window.onYouTubeIframeAPIReady;
    var s = document.createElement("script");
    function fail() {
      window.onYouTubeIframeAPIReady = prev;
      if (s.parentNode) s.parentNode.removeChild(s);
      apiPromise = null; // tenta de novo no próximo vídeo
      reject();
    }
    var timer = setTimeout(fail, 10000);
    window.onYouTubeIframeAPIReady = function () { clearTimeout(timer); if (prev) prev(); resolve(); };
    s.onerror = function () { clearTimeout(timer); fail(); };
    s.src = "https://www.youtube.com/iframe_api";
    document.head.appendChild(s);
  });
  return apiPromise;
}

function dropPlayer() {
  if (player) { try { player.destroy(); } catch (e) {} }
  player = null;
}

function openVideo(id, vertical, list) {
  dropPlayer();
  frame.innerHTML = "";
  var src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0&playsinline=1";
  if (list) {
    // list + loop: o YouTube toca a playlist do jogo em sequência e recomeça no fim
    src += "&list=" + encodeURIComponent(list) + "&loop=1&enablejsapi=1";
    if (/^https?:/.test(location.origin)) src += "&origin=" + encodeURIComponent(location.origin);
  }
  var f = document.createElement("iframe");
  f.src = src;
  f.title = "YouTube";
  f.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
  f.allowFullscreen = true;
  frame.appendChild(f);
  modal.classList.toggle("vertical", !!vertical);
  modal.classList.toggle("has-list", !!list);
  modal.hidden = false;
  document.body.classList.add("no-scroll");
  modal.querySelector(".vmodal-close").focus();
  if (list) {
    loadYouTubeApi().then(function () {
      if (f.parentNode !== frame) return; // a janela já foi fechada ou trocada
      player = new YT.Player(f);
    }, function () {
      // sem o programa do YouTube (bloqueador, rede): o vídeo e a playlist
      // continuam tocando sozinhos, só as setinhas somem
      if (f.parentNode === frame) modal.classList.remove("has-list");
    });
  }
}

function stepVideo(dir) {
  if (!player) return;
  try {
    if (dir > 0 && player.nextVideo) player.nextVideo();
    if (dir < 0 && player.previousVideo) player.previousVideo();
  } catch (e) { /* player ainda carregando */ }
}

function closeVideo() {
  if (modal.hidden) return;
  modal.hidden = true;
  dropPlayer();
  frame.innerHTML = ""; // tira o player: o vídeo para de tocar
  document.body.classList.remove("no-scroll");
  if (lastBtn) lastBtn.focus();
}

document.addEventListener("click", function (e) {
  var b = e.target.closest ? e.target.closest("[data-video]") : null;
  if (b) {
    e.preventDefault();
    lastBtn = b;
    openVideo(b.getAttribute("data-video"), b.hasAttribute("data-vertical"), b.getAttribute("data-playlist"));
  }
});
modal.addEventListener("click", function (e) {
  if (e.target.closest(".vmodal-prev")) { stepVideo(-1); return; }
  if (e.target.closest(".vmodal-next")) { stepVideo(1); return; }
  if (e.target === modal || e.target.closest(".vmodal-close")) closeVideo();
});
document.addEventListener("keydown", function (e) {
  if (modal.hidden) return;
  if (e.key === "Escape") closeVideo();
  // setas do teclado = setinhas da tela (‹ à esquerda, › à direita).
  // Alt+seta é o "voltar" do navegador; segurar a tecla não pula vários vídeos.
  if (e.altKey || e.ctrlKey || e.metaKey || e.repeat) return;
  if (e.key === "ArrowRight") stepVideo(1);
  if (e.key === "ArrowLeft") stepVideo(-1);
});

getJSON("lang/index.json").then(function (idx) {
  select.innerHTML = "";
  idx.languages.forEach(function (l) {
    codes.push(l.code);
    var o = document.createElement("option");
    o.value = l.code;
    o.textContent = l.name;
    select.appendChild(o);
  });
  select.value = "en";
  var start = pickLang();
  if (start !== "en") apply(start);
  select.addEventListener("change", function () { apply(select.value); });
}).catch(function () { select.style.display = "none"; });
