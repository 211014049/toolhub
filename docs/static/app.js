function initSearch() {
  const input = document.querySelector('.search-bar input');
  const results = document.querySelector('.search-results');
  if (!input || !results) return;

  input.addEventListener('input', () => {
    const tools = window.ALL_TOOLS || [];
    const q = input.value.trim().toLowerCase();
    if (!q) { results.style.display = 'none'; return; }
    const matches = tools.filter(t =>
      t.title.toLowerCase().includes(q) ||
      (t.keywords || '').toLowerCase().includes(q)
    ).slice(0, 8);
    if (matches.length === 0) { results.style.display = 'none'; return; }
    results.innerHTML = matches.map(t =>
      `<a href="${t.url}">${t.title}</a>`
    ).join('');
    results.style.display = 'block';
  });

  document.addEventListener('click', e => {
    if (!e.target.closest('.search-bar')) results.style.display = 'none';
  });
}

function copyToClipboard(text, btn) {
  navigator.clipboard.writeText(text).then(() => {
    const orig = btn.textContent;
    btn.textContent = 'Copied!';
    setTimeout(() => btn.textContent = orig, 1500);
  });
}

document.addEventListener('DOMContentLoaded', initSearch);
