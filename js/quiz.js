(function () {
  const PER_PAGE = 10;
  const TYPE_LABELS = {
    test: { title: "Çoktan Seçmeli (Test)", icon: "📝", desc: "4 şıklı klasik test soruları" },
    dogru: { title: "Doğru / Yanlış", icon: "✓✗", desc: "İfade doğru mu yanlış mı?" },
    bosluk: { title: "Boşluk Doldurma", icon: "___", desc: "Eksik kelimeyi yazın" },
    kod: { title: "Kod Kısa ↔ Uzun", icon: "{ }", desc: "Kısa/uzun kod eşleştirme" },
  };

  let data = null;
  let currentType = "test";
  let currentPage = 0;
  let answers = {};
  let shuffle = false;

  const el = {
    loading: document.getElementById("loading"),
    container: document.getElementById("questions-container"),
    tabs: document.querySelectorAll(".type-tab"),
    topicFilter: document.getElementById("topic-filter"),
    shuffleCheck: document.getElementById("shuffle"),
    btnCheckPage: document.getElementById("btn-check-page"),
    btnCheckAll: document.getElementById("btn-check-all"),
    btnReset: document.getElementById("btn-reset"),
    pagination: document.getElementById("pagination"),
    progressFill: document.getElementById("progress-fill"),
    scorePanel: document.getElementById("score-panel"),
    counts: {
      test: document.getElementById("count-test"),
      dogru: document.getElementById("count-dogru"),
      bosluk: document.getElementById("count-bosluk"),
      kod: document.getElementById("count-kod"),
    },
  };

  async function init() {
    try {
      if (window.QUIZ_DATA) {
        data = window.QUIZ_DATA;
      } else {
        const res = await fetch("data/questions.json");
        data = await res.json();
      }
      if (window.QUIZ_TEST_ONLY || data.meta?.testOnly) {
        currentType = "test";
        document.querySelectorAll(".type-tab").forEach((tab) => {
          tab.style.display = tab.dataset.type === "test" ? "" : "none";
        });
      }
      updateCounts();
      fillTopicFilter();
      bindEvents();
      render();
    } catch (e) {
      if (window.QUIZ_DATA) {
        data = window.QUIZ_DATA;
        updateCounts();
        fillTopicFilter();
        bindEvents();
        render();
        return;
      }
      el.loading.textContent = "Sorular yüklenemedi. js/questions-data.js dosyasını kontrol edin.";
      console.error(e);
    }
  }

  function updateCounts() {
    if (!data?.meta?.counts) return;
    if (window.QUIZ_TEST_ONLY || data.meta?.testOnly) {
      const n = data.meta.counts.test ?? (data.test || []).length;
      if (el.counts.test) el.counts.test.textContent = n;
      return;
    }
    Object.keys(el.counts).forEach((k) => {
      if (el.counts[k]) el.counts[k].textContent = data.meta.counts[k];
    });
  }

  function fillTopicFilter() {
    const topics = new Set();
    const types = window.QUIZ_TEST_ONLY || data.meta?.testOnly
      ? ["test"]
      : ["test", "dogru", "bosluk", "kod"];
    types.forEach((t) => {
      (data[t] || []).forEach((q) => topics.add(q.topic || "genel"));
    });
    el.topicFilter.innerHTML = '<option value="">Tüm konular</option>';
    [...topics].sort().forEach((t) => {
      const o = document.createElement("option");
      o.value = t;
      o.textContent = t;
      el.topicFilter.appendChild(o);
    });
  }

  function getFilteredQuestions() {
    let list = [...(data[currentType] || [])];
    const topic = el.topicFilter?.value;
    if (topic) list = list.filter((q) => (q.topic || "genel") === topic);
    if (shuffle || el.shuffleCheck?.checked) {
      list = shuffleArray(list);
    }
    return list;
  }

  function shuffleArray(arr) {
    const a = [...arr];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function bindEvents() {
    el.tabs.forEach((tab) => {
      tab.addEventListener("click", () => {
        currentType = tab.dataset.type;
        currentPage = 0;
        answers = {};
        el.tabs.forEach((t) => t.classList.toggle("active", t === tab));
        el.scorePanel?.classList.remove("visible");
        render();
      });
    });

    el.topicFilter?.addEventListener("change", () => {
      currentPage = 0;
      render();
    });

    el.shuffleCheck?.addEventListener("change", () => {
      currentPage = 0;
      render();
    });

    el.btnCheckPage?.addEventListener("click", () => checkPage(false));
    el.btnCheckAll?.addEventListener("click", () => checkAll());
    el.btnReset?.addEventListener("click", () => {
      answers = {};
      el.scorePanel?.classList.remove("visible");
      document.querySelectorAll(".question-card").forEach((c) => {
        c.classList.remove("answered-correct", "answered-wrong");
      });
      render();
    });
  }

  function render() {
    if (!data) return;
    el.loading.style.display = "none";
    const list = getFilteredQuestions();
    const totalPages = Math.max(1, Math.ceil(list.length / PER_PAGE));
    if (currentPage >= totalPages) currentPage = totalPages - 1;

    const slice = list.slice(currentPage * PER_PAGE, (currentPage + 1) * PER_PAGE);
    el.container.innerHTML = "";

    const typeInfo = TYPE_LABELS[currentType];
    const header = document.createElement("div");
    header.className = "type-intro";
    header.innerHTML = `<p style="color:var(--muted);margin-bottom:1rem;font-size:0.9rem"><strong>${typeInfo.title}</strong> — ${typeInfo.desc} · Toplam <strong>${list.length}</strong> soru</p>`;
    el.container.appendChild(header);

    slice.forEach((q, idx) => {
      const globalIdx = currentPage * PER_PAGE + idx;
      el.container.appendChild(renderQuestion(q, globalIdx, list));
    });

    renderPagination(totalPages);
    updateProgress(list);
  }

  function renderQuestion(q, index, list) {
    const card = document.createElement("div");
    card.className = "question-card";
    card.dataset.id = q.id;

    const header = `
      <div class="q-header">
        <span class="q-num">${q.id || index + 1}</span>
        <span class="q-topic">${q.topic || "genel"}</span>
      </div>`;

    if (currentType === "test") {
      card.innerHTML = header + `<p class="q-text">${escapeHtml(q.question)}</p>`;
      const ul = document.createElement("ul");
      ul.className = "options-list";
      q.options.forEach((opt, i) => {
        const li = document.createElement("li");
        li.innerHTML = `<label><input type="radio" name="${q.id}" value="${i}"> ${escapeHtml(opt)}</label>`;
        ul.appendChild(li);
      });
      card.appendChild(ul);
    } else if (currentType === "dogru") {
      card.innerHTML = header + `<p class="q-text">${escapeHtml(q.statement)}</p>`;
      const div = document.createElement("div");
      div.className = "tf-buttons";
      div.innerHTML = `
        <button type="button" class="tf-btn" data-val="true">Doğru</button>
        <button type="button" class="tf-btn" data-val="false">Yanlış</button>`;
      div.querySelectorAll(".tf-btn").forEach((btn) => {
        btn.addEventListener("click", () => {
          div.querySelectorAll(".tf-btn").forEach((b) => b.classList.remove("selected"));
          btn.classList.add("selected");
          answers[q.id] = btn.dataset.val === "true";
        });
      });
      card.appendChild(div);
    } else if (currentType === "bosluk") {
      const text = q.question.replace("___", '<input type="text" class="blank-input" autocomplete="off" placeholder="Cevabınız...">');
      card.innerHTML = header + `<p class="q-text">${text}</p>`;
      const inp = card.querySelector(".blank-input");
      inp?.addEventListener("input", () => {
        answers[q.id] = inp.value.trim();
      });
    } else if (currentType === "kod") {
      const dirLabel =
        q.direction === "to-short"
          ? "Aşağıdaki UZUN kodun kısa/eşdeğer hali hangisidir?"
          : "Aşağıdaki KISA kodun uzun/eşdeğer hali hangisidir?";
      card.innerHTML =
        header +
        `<p class="q-direction">${dirLabel}</p>` +
        `<pre class="q-code">${escapeHtml(q.prompt)}</pre>`;
      const ul = document.createElement("ul");
      ul.className = "options-list";
      q.options.forEach((opt, i) => {
        const li = document.createElement("li");
        li.innerHTML = `<label><input type="radio" name="${q.id}" value="${i}"><pre class="q-code" style="margin:0;padding:0.5rem;background:transparent;border:none;display:inline-block">${escapeHtml(opt)}</pre></label>`;
        ul.appendChild(li);
      });
      card.appendChild(ul);
    }

    const fb = document.createElement("div");
    fb.className = "feedback";
    fb.dataset.feedback = q.id;
    card.appendChild(fb);

    return card;
  }

  function normalizeAnswer(s) {
    return String(s)
      .toLowerCase()
      .trim()
      .replace(/ı/g, "i")
      .replace(/ğ/g, "g")
      .replace(/ü/g, "u")
      .replace(/ş/g, "s")
      .replace(/ö/g, "o")
      .replace(/ç/g, "c");
  }

  function checkAnswer(q, userAnswer) {
    if (currentType === "test" || currentType === "kod") {
      return Number(userAnswer) === q.correct;
    }
    if (currentType === "dogru") {
      return userAnswer === q.correct;
    }
    if (currentType === "bosluk") {
      const u = normalizeAnswer(userAnswer);
      const main = normalizeAnswer(q.answer);
      if (u === main) return true;
      return (q.alternatives || []).some((a) => normalizeAnswer(a) === u);
    }
    return false;
  }

  function getUserAnswer(q, card) {
    if (currentType === "test" || currentType === "kod") {
      const sel = card.querySelector(`input[name="${q.id}"]:checked`);
      return sel ? Number(sel.value) : undefined;
    }
    if (currentType === "dogru") {
      return answers[q.id];
    }
    if (currentType === "bosluk") {
      const inp = card.querySelector(".blank-input");
      return inp ? inp.value.trim() : answers[q.id];
    }
  }

  function showFeedback(card, q, ok) {
    const fb = card.querySelector(".feedback");
    if (!fb) return;
    fb.classList.add("show", ok ? "ok" : "err");
    if (ok) {
      fb.textContent = "✓ Doğru!";
      card.classList.add("answered-correct");
    } else {
      let correctText = "";
      if (currentType === "test" || currentType === "kod") {
        correctText = q.options[q.correct];
      } else if (currentType === "dogru") {
        correctText = q.correct ? "Doğru" : "Yanlış";
      } else {
        correctText = q.answer;
      }
      fb.textContent = `✗ Yanlış. Doğru cevap: ${correctText}`;
      card.classList.add("answered-wrong");
    }
  }

  function checkPage(showScore) {
    const list = getFilteredQuestions();
    const slice = list.slice(currentPage * PER_PAGE, (currentPage + 1) * PER_PAGE);
    let correct = 0;
    slice.forEach((q) => {
      const card = el.container.querySelector(`[data-id="${q.id}"]`);
      if (!card) return;
      const ua = getUserAnswer(q, card);
      if (ua === undefined || ua === "") return;
      const ok = checkAnswer(q, ua);
      if (ok) correct++;
      showFeedback(card, q, ok);
      if (currentType === "dogru") {
        card.querySelectorAll(".tf-btn").forEach((btn) => {
          const v = btn.dataset.val === "true";
          btn.classList.remove("correct-answer", "wrong-answer");
          if (v === q.correct) btn.classList.add("correct-answer");
          else if (btn.classList.contains("selected")) btn.classList.add("wrong-answer");
        });
      }
      if (currentType === "bosluk") {
        const inp = card.querySelector(".blank-input");
        if (inp) inp.classList.add(ok ? "correct" : "wrong");
      }
    });
    if (showScore !== false) {
      el.scorePanel.classList.add("visible");
      el.scorePanel.innerHTML = `Bu sayfa: <strong>${correct}</strong> / ${slice.length} doğru`;
    }
  }

  function checkAll() {
    const list = getFilteredQuestions();
    let correct = 0;
    let answered = 0;
    list.forEach((q) => {
      const card = el.container.querySelector(`[data-id="${q.id}"]`);
      if (!card) {
        // render all pages virtually - need to check all in data
        return;
      }
      const ua = getUserAnswer(q, card);
      if (ua !== undefined && ua !== "") {
        answered++;
        if (checkAnswer(q, ua)) correct++;
        showFeedback(card, q, checkAnswer(q, ua));
      }
    });

    // Check entire list by re-rendering not practical; score from stored answers
    correct = 0;
    answered = 0;
    list.forEach((q) => {
      let ua = answers[q.id];
      if (currentType === "test" || currentType === "kod") {
        const card = document.querySelector(`[data-id="${q.id}"]`);
        if (card) {
          const sel = card.querySelector(`input[name="${q.id}"]:checked`);
          if (sel) ua = Number(sel.value);
        }
      }
      if (currentType === "bosluk") {
        const card = document.querySelector(`[data-id="${q.id}"]`);
        const inp = card?.querySelector(".blank-input");
        if (inp) ua = inp.value.trim();
      }
      if (ua !== undefined && ua !== "") {
        answered++;
        if (checkAnswer(q, ua)) correct++;
      }
    });

    el.scorePanel.classList.add("visible");
    el.scorePanel.innerHTML = `
      <strong>Genel sonuç (${TYPE_LABELS[currentType].title})</strong><br>
      Doğru: <strong>${correct}</strong> / ${list.length}
      · Cevaplanan: ${answered}
      · Başarı: ${list.length ? Math.round((correct / list.length) * 100) : 0}%
      <br><small style="color:var(--muted)">Tüm soruları kontrol etmek için her sayfada "Bu Sayfayı Kontrol Et" kullanın veya sayfalar arasında gezinip cevaplayın.</small>`;
    checkPage(false);
  }

  function renderPagination(totalPages) {
    el.pagination.innerHTML = "";
    if (totalPages <= 1) return;

    const prev = document.createElement("button");
    prev.className = "page-btn";
    prev.textContent = "←";
    prev.disabled = currentPage === 0;
    prev.onclick = () => {
      currentPage--;
      render();
    };
    el.pagination.appendChild(prev);

    for (let i = 0; i < totalPages; i++) {
      const btn = document.createElement("button");
      btn.className = "page-btn" + (i === currentPage ? " active" : "");
      btn.textContent = i + 1;
      btn.onclick = () => {
        currentPage = i;
        render();
      };
      el.pagination.appendChild(btn);
    }

    const next = document.createElement("button");
    next.className = "page-btn";
    next.textContent = "→";
    next.disabled = currentPage >= totalPages - 1;
    next.onclick = () => {
      currentPage++;
      render();
    };
    el.pagination.appendChild(next);
  }

  function updateProgress(list) {
    const total = list.length;
    const start = currentPage * PER_PAGE + 1;
    const end = Math.min((currentPage + 1) * PER_PAGE, total);
    const pct = total ? (end / total) * 100 : 0;
    el.progressFill.style.width = pct + "%";
  }

  function escapeHtml(s) {
    const d = document.createElement("div");
    d.textContent = s;
    return d.innerHTML;
  }

  init();
})();
