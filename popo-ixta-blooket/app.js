const vocabItems = window.VOCAB_ITEMS;
const learningTargets = window.LEARNING_TARGETS;

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
  termCount: document.querySelector("#termCount"),
  questionCount: document.querySelector("#questionCount"),
  bestScore: document.querySelector("#bestScore"),
  playerName: document.querySelector("#playerName"),
  roundCount: document.querySelector("#roundCount"),
  timerToggle: document.querySelector("#timerToggle"),
  startBtn: document.querySelector("#startBtn"),
  nextBtn: document.querySelector("#nextBtn"),
  playAgainBtn: document.querySelector("#playAgainBtn"),
  reviewMissedBtn: document.querySelector("#reviewMissedBtn"),
  targetList: document.querySelector("#targetList"),
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
  const bank = buildQuestionBank(state.mode);
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
  const question = currentQuestion();
  state.locked = false;
  el.feedbackPanel.classList.add("hidden");
  el.answerGrid.classList.remove("hidden");
  el.categoryLabel.textContent = question.category;
  el.promptText.textContent = question.prompt;
  el.modeLabel.textContent = modeText(question.direction);
  el.meterFill.style.width = `${Math.min(state.streak * 12, 100)}%`;

  const choices = answerChoices(question);
  el.answerGrid.replaceChildren(...choices.map((choice) => answerButton(choice, question)));
  updateStatus();
}

function answerButton(choice, question) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = "answer-tile";
  button.textContent = choice.label;
  button.dataset.value = choice.value;
  button.addEventListener("click", () => submitAnswer(button, question));
  return button;
}

function submitAnswer(button, question) {
  if (state.locked) return;
  state.locked = true;

  const selected = button.dataset.value;
  const correct = selected === question.answer;
  const basePoints = question.direction === "es-en" ? 100 : 120;
  const streakBonus = correct ? Math.min(state.streak * 15, 150) : 0;
  const points = correct ? basePoints + streakBonus : 0;

  state.score += points;
  state.streak = correct ? state.streak + 1 : 0;
  state.history.push({
    prompt: question.prompt,
    answer: question.answer,
    selected,
    correct,
    direction: question.direction,
    category: question.category,
    points
  });

  document.querySelectorAll(".answer-tile").forEach((tile) => {
    const isCorrect = tile.dataset.value === question.answer;
    tile.disabled = true;
    tile.classList.toggle("correct", isCorrect);
    tile.classList.toggle("wrong", !isCorrect);
  });

  showFeedback(question, correct, points);
  updateStatus();
}

function showFeedback(question, correct, points) {
  el.feedbackKicker.textContent = correct ? `+${points} points` : "Missed";
  el.feedbackTitle.textContent = correct ? "Correct" : question.answer;
  el.feedbackText.textContent = `${question.prompt} = ${question.answer}`;
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

    const category = document.createElement("span");
    category.className = "review-category";
    category.textContent = `${entry.category} · ${modeText(entry.direction)}`;

    const prompt = document.createElement("strong");
    prompt.textContent = entry.prompt;

    const answer = document.createElement("span");
    answer.textContent = entry.answer;

    item.append(category, prompt, answer);
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

function currentQuestion() {
  return state.deck[state.currentIndex];
}

function buildQuestionBank(mode) {
  const bank = [];
  vocabItems.forEach((item) => {
    if (mode === "mixed" || mode === "es-en") {
      bank.push({
        id: `${item.id}-es-en`,
        category: item.category,
        prompt: item.spanish,
        answer: item.english,
        source: item,
        direction: "es-en"
      });
    }
    if (mode === "mixed" || mode === "en-es") {
      bank.push({
        id: `${item.id}-en-es`,
        category: item.category,
        prompt: item.english,
        answer: item.spanish,
        source: item,
        direction: "en-es"
      });
    }
  });
  return bank;
}

function answerChoices(question) {
  const answerKey = question.direction === "es-en" ? "english" : "spanish";
  const sameCategory = vocabItems.filter((item) => {
    return item.category === question.category && item.id !== question.source.id;
  });
  const otherItems = vocabItems.filter((item) => {
    return item.category !== question.category && item.id !== question.source.id;
  });

  const decoys = [];
  [...shuffle(sameCategory), ...shuffle(otherItems)].forEach((item) => {
    if (decoys.length >= 3) return;
    const value = item[answerKey];
    if (value !== question.answer && !decoys.includes(value)) {
      decoys.push(value);
    }
  });

  return shuffle([
    { value: question.answer, label: question.answer },
    ...decoys.map((value) => ({ value, label: value }))
  ]);
}

function renderStudyPanels() {
  el.targetList.replaceChildren(...learningTargets.map((target) => {
    const item = document.createElement("li");
    item.textContent = target;
    return item;
  }));

  const categories = [...new Set(vocabItems.map((item) => item.category))];
  el.deckList.replaceChildren(...categories.map((category) => {
    const section = document.createElement("section");
    section.className = "deck-category";

    const heading = document.createElement("h3");
    heading.textContent = category;

    const terms = document.createElement("div");
    terms.className = "term-grid";

    vocabItems
      .filter((item) => item.category === category)
      .forEach((item) => {
        const term = document.createElement("article");
        term.className = "term-card";

        const spanish = document.createElement("strong");
        spanish.textContent = item.spanish;

        const english = document.createElement("span");
        english.textContent = item.english;

        term.append(spanish, english);
        terms.append(term);
      });

    section.append(heading, terms);
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
  const total = state.deck.length || buildQuestionBank(state.mode).length;
  const round = state.deck.length ? Math.min(state.currentIndex + 1, total) : 0;
  el.round.textContent = `${round}/${total}`;
  el.meterFill.style.width = `${Math.min(state.streak * 12, 100)}%`;
}

function updateRoundBounds() {
  const max = buildQuestionBank(state.mode).length;
  el.roundCount.max = String(max);
  el.roundCount.value = String(clamp(Number(el.roundCount.value) || max, 5, max));
  el.questionCount.textContent = String(max);
  updateStatus();
}

function updateBestScore() {
  el.bestScore.textContent = Number(localStorage.getItem("volcanoClashBest") || 0).toLocaleString();
}

function saveBestScore(name, score, correct, total) {
  const previous = Number(localStorage.getItem("volcanoClashBest") || 0);
  if (score >= previous) {
    localStorage.setItem("volcanoClashBest", String(score));
    localStorage.setItem("volcanoClashBestSummary", `${name}: ${score} points, ${correct}/${total}`);
  }
}

function modeText(direction) {
  if (direction === "es-en") return "Spanish → English";
  if (direction === "en-es") return "English → Spanish";
  return "Mixed";
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

el.termCount.textContent = String(vocabItems.length);
renderStudyPanels();
updateBestScore();
updateRoundBounds();
