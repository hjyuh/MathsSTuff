const studyCards = window.STUDY_CARDS;
const packetSections = window.PACKET_SECTIONS;
const authoredItems = window.GAME_ITEMS;

const state = {
  mode: "mixed",
  deck: [],
  currentIndex: 0,
  score: 0,
  streak: 0,
  startedAt: 0,
  timerId: 0,
  timed: true,
  locked: false,
  history: []
};

const el = {
  setupPanel: document.querySelector("#setupPanel"),
  studyPanel: document.querySelector("#studyPanel"),
  gamePanel: document.querySelector("#gamePanel"),
  endPanel: document.querySelector("#endPanel"),
  score: document.querySelector("#score"),
  streak: document.querySelector("#streak"),
  round: document.querySelector("#round"),
  timer: document.querySelector("#timer"),
  cardCount: document.querySelector("#cardCount"),
  questionCount: document.querySelector("#questionCount"),
  sectionCount: document.querySelector("#sectionCount"),
  bestScore: document.querySelector("#bestScore"),
  playerName: document.querySelector("#playerName"),
  roundCount: document.querySelector("#roundCount"),
  timerToggle: document.querySelector("#timerToggle"),
  startBtn: document.querySelector("#startBtn"),
  nextBtn: document.querySelector("#nextBtn"),
  playAgainBtn: document.querySelector("#playAgainBtn"),
  reviewMissedBtn: document.querySelector("#reviewMissedBtn"),
  packetList: document.querySelector("#packetList"),
  deckList: document.querySelector("#deckList"),
  categoryLabel: document.querySelector("#categoryLabel"),
  promptText: document.querySelector("#promptText"),
  modeLabel: document.querySelector("#modeLabel"),
  meterFill: document.querySelector("#meterFill"),
  answerGrid: document.querySelector("#answerGrid"),
  feedbackPanel: document.querySelector("#feedbackPanel"),
  feedbackKicker: document.querySelector("#feedbackKicker"),
  feedbackTitle: document.querySelector("#feedbackTitle"),
  feedbackText: document.querySelector("#feedbackText"),
  finalScore: document.querySelector("#finalScore"),
  finalSummary: document.querySelector("#finalSummary"),
  reviewList: document.querySelector("#reviewList")
};

document.querySelectorAll(".segment").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelectorAll(".segment").forEach((segment) => segment.classList.remove("active"));
    button.classList.add("active");
    state.mode = button.dataset.mode;
    updateRoundBounds();
  });
});

el.startBtn.addEventListener("click", startGame);
el.nextBtn.addEventListener("click", nextRound);
el.playAgainBtn.addEventListener("click", resetToSetup);
el.reviewMissedBtn.addEventListener("click", reviewMissed);

function startGame() {
  const bank = questionBank(state.mode);
  const requestedRounds = clamp(Number(el.roundCount.value) || bank.length, 5, bank.length);

  state.deck = shuffle(bank).slice(0, requestedRounds);
  state.currentIndex = 0;
  state.score = 0;
  state.streak = 0;
  state.startedAt = Date.now();
  state.timed = el.timerToggle.checked;
  state.locked = false;
  state.history = [];

  el.setupPanel.classList.add("hidden");
  el.studyPanel.classList.add("hidden");
  el.endPanel.classList.add("hidden");
  el.gamePanel.classList.remove("hidden");
  startTimer();
  renderRound();
}

function renderRound() {
  const item = currentItem();
  state.locked = false;
  el.feedbackPanel.classList.add("hidden");
  el.answerGrid.classList.remove("hidden");
  el.categoryLabel.textContent = item.category;
  el.promptText.textContent = item.prompt;
  el.modeLabel.textContent = labelForMode(item.type);
  el.meterFill.style.width = `${Math.min(state.streak * 12, 100)}%`;

  el.answerGrid.replaceChildren(...answerChoices(item).map((choice) => answerButton(choice, item)));
  updateStatus();
}

function answerButton(choice, item) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = "answer-tile";
  button.textContent = choice;
  button.dataset.value = choice;
  button.addEventListener("click", () => submitAnswer(button, item));
  return button;
}

function submitAnswer(button, item) {
  if (state.locked) return;
  state.locked = true;

  const selected = button.dataset.value;
  const correct = selected === item.answer;
  const basePoints = item.type === "Math" ? 140 : item.type === "Vocab" ? 100 : 120;
  const streakBonus = correct ? Math.min(state.streak * 15, 180) : 0;
  const points = correct ? basePoints + streakBonus : 0;

  state.score += points;
  state.streak = correct ? state.streak + 1 : 0;
  state.history.push({
    category: item.category,
    type: item.type,
    prompt: item.prompt,
    answer: item.answer,
    selected,
    correct,
    points
  });

  document.querySelectorAll(".answer-tile").forEach((tile) => {
    const isCorrect = tile.dataset.value === item.answer;
    tile.disabled = true;
    tile.classList.toggle("correct", isCorrect);
    tile.classList.toggle("wrong", !isCorrect);
  });

  showFeedback(item, correct, points);
  updateStatus();
}

function showFeedback(item, correct, points) {
  el.feedbackKicker.textContent = correct ? `+${points} points` : "Missed";
  el.feedbackTitle.textContent = correct ? "Correct" : item.answer;
  el.feedbackText.textContent = `${item.prompt} = ${item.answer}`;
  el.feedbackPanel.classList.remove("hidden");
}

function nextRound() {
  state.currentIndex += 1;
  if (state.currentIndex >= state.deck.length) {
    finishGame();
    return;
  }
  renderRound();
}

function finishGame() {
  clearInterval(state.timerId);
  const correctCount = state.history.filter((entry) => entry.correct).length;
  const total = state.history.length;
  const name = el.playerName.value.trim() || "Player";

  el.gamePanel.classList.add("hidden");
  el.endPanel.classList.remove("hidden");
  el.studyPanel.classList.remove("hidden");
  el.finalScore.textContent = state.score.toLocaleString();
  el.finalSummary.textContent = `${name}: ${correctCount}/${total} correct`;
  renderReview(state.history);
  saveBestScore(name, state.score, correctCount, total);
  updateBestScore();
}

function renderReview(history) {
  el.reviewList.replaceChildren(...history.map((entry) => {
    const item = document.createElement("article");
    item.className = `review-item ${entry.correct ? "correct" : "missed"}`;

    const tag = document.createElement("span");
    tag.className = "review-category";
    tag.textContent = `${entry.category} - ${entry.type}`;

    const prompt = document.createElement("strong");
    prompt.textContent = entry.prompt;

    const answer = document.createElement("span");
    answer.textContent = entry.answer;

    item.append(tag, prompt, answer);
    return item;
  }));
}

function reviewMissed() {
  const missed = state.history.filter((entry) => !entry.correct);
  renderReview(missed.length ? missed : state.history);
}

function resetToSetup() {
  clearInterval(state.timerId);
  el.endPanel.classList.add("hidden");
  el.gamePanel.classList.add("hidden");
  el.setupPanel.classList.remove("hidden");
  el.studyPanel.classList.remove("hidden");
  state.score = 0;
  state.streak = 0;
  state.currentIndex = 0;
  state.history = [];
  updateRoundBounds();
  updateStatus();
}

function currentItem() {
  return state.deck[state.currentIndex];
}

function questionBank(mode) {
  const vocabItems = studyCards.map((card) => ({
    category: card.category,
    type: "Vocab",
    prompt: `What is ${card.term}?`,
    answer: card.definition
  }));

  const all = [...vocabItems, ...authoredItems];
  if (mode === "vocab") return vocabItems;
  if (mode === "math") return authoredItems.filter((item) => item.type === "Math");
  if (mode === "packet") return authoredItems.filter((item) => item.type === "Packet");
  return all;
}

function answerChoices(item) {
  const bank = questionBank("mixed");
  const sameType = bank.filter((candidate) => {
    return candidate.type === item.type && candidate.answer !== item.answer;
  });
  const sameCategory = sameType.filter((candidate) => candidate.category === item.category);
  const pool = [...shuffle(sameCategory), ...shuffle(sameType)];
  const decoys = [];

  pool.forEach((candidate) => {
    if (decoys.length >= 3) return;
    if (!decoys.includes(candidate.answer)) {
      decoys.push(candidate.answer);
    }
  });

  if (decoys.length < 3) {
    shuffle(bank).forEach((candidate) => {
      if (decoys.length >= 3) return;
      if (candidate.answer !== item.answer && !decoys.includes(candidate.answer)) {
        decoys.push(candidate.answer);
      }
    });
  }

  return shuffle([item.answer, ...decoys]);
}

function renderStudyPanels() {
  el.packetList.replaceChildren(...packetSections.map((section) => {
    const article = document.createElement("article");
    article.className = "packet-section";

    const heading = document.createElement("h3");
    heading.textContent = `Page ${section.page}: ${section.title}`;

    const list = document.createElement("ul");
    list.append(...section.bullets.map((bullet) => {
      const item = document.createElement("li");
      item.textContent = bullet;
      return item;
    }));

    article.append(heading, list);
    return article;
  }));

  const categories = [...new Set(studyCards.map((card) => card.category))];
  el.deckList.replaceChildren(...categories.map((category) => {
    const section = document.createElement("section");
    section.className = "deck-category";

    const heading = document.createElement("h3");
    heading.textContent = category;

    const cards = document.createElement("div");
    cards.className = "term-grid";

    studyCards
      .filter((card) => card.category === category)
      .forEach((card) => {
        const article = document.createElement("article");
        article.className = "term-card";

        const term = document.createElement("strong");
        term.textContent = card.term;

        const definition = document.createElement("span");
        definition.textContent = card.definition;

        article.append(term, definition);
        cards.append(article);
      });

    section.append(heading, cards);
    return section;
  }));
}

function startTimer() {
  clearInterval(state.timerId);
  updateTimer();
  state.timerId = setInterval(updateTimer, 1000);
}

function updateTimer() {
  if (!state.timed || !state.startedAt) {
    el.timer.textContent = "0:00";
    return;
  }
  const elapsed = Math.floor((Date.now() - state.startedAt) / 1000);
  const minutes = Math.floor(elapsed / 60);
  const seconds = String(elapsed % 60).padStart(2, "0");
  el.timer.textContent = `${minutes}:${seconds}`;
}

function updateStatus() {
  el.score.textContent = state.score.toLocaleString();
  el.streak.textContent = String(state.streak);
  const total = state.deck.length || questionBank(state.mode).length;
  const round = state.deck.length ? Math.min(state.currentIndex + 1, total) : 0;
  el.round.textContent = `${round}/${total}`;
  el.meterFill.style.width = `${Math.min(state.streak * 12, 100)}%`;
}

function updateRoundBounds() {
  const max = questionBank(state.mode).length;
  el.roundCount.max = String(max);
  el.roundCount.value = String(clamp(Number(el.roundCount.value) || max, 5, max));
  el.questionCount.textContent = String(questionBank("mixed").length);
  updateStatus();
}

function updateBestScore() {
  el.bestScore.textContent = Number(localStorage.getItem("waveQuestBest") || 0).toLocaleString();
}

function saveBestScore(name, score, correct, total) {
  const previous = Number(localStorage.getItem("waveQuestBest") || 0);
  if (score >= previous) {
    localStorage.setItem("waveQuestBest", String(score));
    localStorage.setItem("waveQuestBestSummary", `${name}: ${score} points, ${correct}/${total}`);
  }
}

function labelForMode(type) {
  if (type === "Math") return "Wave Math";
  if (type === "Vocab") return "Vocabulary";
  return "Packet Practice";
}

function shuffle(source) {
  const result = [...source];
  for (let index = result.length - 1; index > 0; index -= 1) {
    const swapIndex = Math.floor(Math.random() * (index + 1));
    [result[index], result[swapIndex]] = [result[swapIndex], result[index]];
  }
  return result;
}

function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}

el.cardCount.textContent = String(studyCards.length);
el.sectionCount.textContent = `${packetSections.length} sections`;
renderStudyPanels();
updateBestScore();
updateRoundBounds();
