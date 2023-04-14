// For use in browser dev tools, output in Buckets-friendly format

html = document.documentElement.innerHTML;

transactions = '';
parser = new DOMParser();
doc = parser.parseFromString(html, "text/html");

doc.querySelectorAll('tr').forEach(function(i) {
  if (!i.innerText.includes('$')) return;
  let date = new Date(i.children[0].innerText.trim());
  transactions +=
    date.toLocaleDateString("en-US") + ";" +
    i.children[1].innerText.trim() + ";" +
    i.children[2].innerText.trim() + "\n";
});

transactions;