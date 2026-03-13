console.log(import.meta.env.VITE_HOST) // "123"

const BASE = `api`;
const tabs = ["get", "post", "put"];

document.querySelector(".load-trading").addEventListener("click", loadTradings)
document.querySelector(".load-filtered").addEventListener("click", loadFiltered)
document.querySelector(".post-trading").addEventListener("click", postTrading)
document.querySelector(".put-trading").addEventListener("click", putTrading)

document.querySelector(".show-get").addEventListener("click", () => showTab("get"))
document.querySelector(".show-post").addEventListener("click", () =>  showTab("post"))
document.querySelector(".show-put").addEventListener("click", () =>  showTab("put"))

function showTab(name) {
    tabs.forEach(t => {
    document.getElementById(`tab-${t}`).style.display = t === name ? "block" : "none";
    document.getElementById(`nav-${t}`).classList.toggle("active", t === name);
    });
    return false;
}

function renderTable(data) {
  const container = document.getElementById("get_result");
  if (!data.length) { container.textContent = "No results."; return; }
  const cols = ["id", "insider_trading", "relationship", "date", "transaction", "cost", "shares", "value", "shares_total", "sec_form_4"];
  const header = cols.map(c => `<th>${c}</th>`).join("");
  const rows = data.map(row =>
    `<tr>${row.map(cell => `<td title="${cell ?? ""}">${cell ?? ""}</td>`).join("")}</tr>`
  ).join("");
  container.innerHTML = `<table><thead><tr>${header}</tr></thead><tbody>${rows}</tbody></table>`;
}

async function loadTradings() {
  const res = await fetch(`${BASE}/tradings`);
  renderTable(await res.json());
}

async function loadFiltered() {
  const col = document.getElementById("filterCol").value;
  const val = document.getElementById("filterVal").value;
  const res = await fetch(`${BASE}/tradings?${col}=${val}`);
  renderTable(await res.json());
}

function collectTrading(prefix) {
    return {
    insider_trading: document.getElementById(`${prefix}_insider`).value,
    relationship:    document.getElementById(`${prefix}_relationship`).value,
    date:            document.getElementById(`${prefix}_date`).value,
    transaction:     document.getElementById(`${prefix}_transaction`).value,
    cost:            parseFloat(document.getElementById(`${prefix}_cost`).value),
    shares:          document.getElementById(`${prefix}_shares`).value,
    value:           document.getElementById(`${prefix}_value`).value,
    shares_total:    document.getElementById(`${prefix}_shares_total`).value,
    sec_form_4:      document.getElementById(`${prefix}_sec_form_4`).value,
    };
}

async function postTrading() {
    const res = await fetch(`${BASE}/tradings`, {
    method: "POST",
    body: JSON.stringify(collectTrading("p"))
    });
    document.getElementById("post_result").textContent = await res.text();
}

async function putTrading() {
    const id = document.getElementById("u_id").value;
    const res = await fetch(`${BASE}/tradings/${id}`, {
    method: "PUT",
    body: JSON.stringify(collectTrading("u"))
    });
    document.getElementById("put_result").textContent = await res.text();
}