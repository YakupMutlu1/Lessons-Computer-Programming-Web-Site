document.addEventListener("DOMContentLoaded", () => {
  const sidebar = document.querySelector(".sidebar");
  const menuToggle = document.querySelector(".menu-toggle");
  const searchInput = document.getElementById("search");
  const navLinks = document.querySelectorAll(".nav-links a");
  const sections = document.querySelectorAll(".section[id]");

  // Mobil menü
  menuToggle?.addEventListener("click", () => sidebar.classList.toggle("open"));

  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      if (window.innerWidth <= 768) sidebar.classList.remove("open");
    });
  });

  // Modül aç/kapa
  document.querySelectorAll(".nav-module-title").forEach((title) => {
    title.addEventListener("click", () => {
      title.parentElement.classList.toggle("collapsed");
    });
  });

  // Aktif bölüm vurgusu
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const id = entry.target.id;
          navLinks.forEach((a) => {
            a.classList.toggle("active", a.getAttribute("href") === `#${id}`);
          });
        }
      });
    },
    { rootMargin: "-20% 0px -70% 0px" }
  );
  sections.forEach((s) => observer.observe(s));

  // Arama
  searchInput?.addEventListener("input", (e) => {
    const q = e.target.value.toLowerCase().trim();
    sections.forEach((section) => {
      const text = section.textContent.toLowerCase();
      const match = !q || text.includes(q);
      section.classList.toggle("hidden", !match);
      if (match && q) highlightText(section, q);
      else removeHighlights(section);
    });
    document.querySelectorAll(".module").forEach((mod) => {
      const visible = mod.querySelectorAll(".section:not(.hidden)").length;
      mod.classList.toggle("hidden", visible === 0 && q.length > 0);
    });
  });

  function highlightText(el, query) {
    removeHighlights(el);
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach((node) => {
      const parent = node.parentElement;
      if (parent.tagName === "SCRIPT" || parent.tagName === "STYLE" || parent.tagName === "MARK") return;
      const idx = node.textContent.toLowerCase().indexOf(query);
      if (idx === -1) return;
      const before = node.textContent.slice(0, idx);
      const match = node.textContent.slice(idx, idx + query.length);
      const after = node.textContent.slice(idx + query.length);
      const frag = document.createDocumentFragment();
      if (before) frag.appendChild(document.createTextNode(before));
      const mark = document.createElement("mark");
      mark.textContent = match;
      frag.appendChild(mark);
      if (after) frag.appendChild(document.createTextNode(after));
      parent.replaceChild(frag, node);
    });
  }

  function removeHighlights(el) {
    el.querySelectorAll("mark").forEach((m) => {
      const t = document.createTextNode(m.textContent);
      m.parentNode.replaceChild(t, m);
      t.parentNode.normalize();
    });
  }
});
