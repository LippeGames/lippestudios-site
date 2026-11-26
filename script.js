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
