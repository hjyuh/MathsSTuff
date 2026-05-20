const items = window.QUIZ_ITEMS;
const tenseChoices = [
  { value: "preterite", label: "Pretérito: completed event" },
  { value: "imperfect", label: "Imperfecto: description or ongoing background" }
];

const state = {
  mode: "translation",
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
  gamePanel: document.querySelector("#gamePanel"),
  endPanel: document.querySelector("#endPanel"),
  score: document.querySelector("#score"),
  streak: document.querySelector("#streak"),
  round: document.querySelector("#round"),
  timer: document.querySelector("#timer"),
  playerName: document.querySelector("#playerName"),
  roundCount: document.querySelector("#roundCount"),
  timerToggle: document.querySelector("#timerToggle"),
  startBtn: document.querySelector("#startBtn"),
  nextBtn: document.querySelector("#nextBtn"),
  playAgainBtn: document.querySelector("#playAgainBtn"),
  reviewMissedBtn: document.querySelector("#reviewMissedBtn"),
  questionImage: document.querySelector("#questionImage"),
  answerImage: document.querySelector("#answerImage"),
  promptText: document.querySelector("#promptText"),
  modeLabel: document.querySelector("#modeLabel"),
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
  });
});

el.startBtn.addEventListener("click", startGame);
el.nextBtn.addEventListener("click", nextRound);
el.playAgainBtn.addEventListener("click", resetToSetup);
el.reviewMissedBtn.addEventListener("click", reviewMissed);

function startGame() {
  const requestedRounds = clamp(Number(el.roundCount.value) || items.length, 5, items.length);
  state.deck = shuffle([...items]).slice(0, requestedRounds);
  state.currentIndex = 0;
  state.score = 0;
  state.streak = 0;
  state.startedAt = Date.now();
  state.timed = el.timerToggle.checked;
  state.locked = false;
  state.history = [];

  el.setupPanel.classList.add("hidden");
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
  el.questionImage.src = item.questionImage;
  el.questionImage.alt = item.prompt;
  el.answerImage.src = item.answerImage;
  el.answerImage.alt = item.answer;
  el.promptText.textContent = item.prompt;
  el.modeLabel.textContent = state.mode === "translation" ? "Translation" : "Tense";

  const choices = state.mode === "translation" ? translationChoices(item) : tenseChoices;
  el.answerGrid.replaceChildren(...choices.map((choice) => answerButton(choice, item)));
  updateStatus();
}

function answerButton(choice, item) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = "answer-tile";
  button.textContent = choice.label || choice.answer;
  button.dataset.value = choice.value || choice.answer;
  button.addEventListener("click", () => submitAnswer(button, item));
  return button;
}

function submitAnswer(button, item) {
  if (state.locked) return;
  state.locked = true;

  const selected = button.dataset.value;
  const correctValue = state.mode === "translation" ? item.answer : item.tense;
  const correct = selected === correctValue;
  const basePoints = state.mode === "translation" ? 100 : 70;
  const streakBonus = correct ? Math.min(state.streak * 10, 80) : 0;
  const points = correct ? basePoints + streakBonus : 0;

  state.score += points;
  state.streak = correct ? state.streak + 1 : 0;
  state.history.push({
    slide: item.slide,
    prompt: item.prompt,
    answer: item.answer,
    selected,
    correct,
    mode: state.mode,
    points
  });

  document.querySelectorAll(".answer-tile").forEach((tile) => {
    const isCorrect = tile.dataset.value === correctValue;
    tile.disabled = true;
    tile.classList.toggle("correct", isCorrect);
    tile.classList.toggle("wrong", !isCorrect);
  });

  showFeedback(item, correct, points);
  updateStatus();
}

function showFeedback(item, correct, points) {
  const tenseLabel = item.tense === "preterite" ? "Pretérito" : "Imperfecto";
  el.feedbackKicker.textContent = correct ? `+${points} points` : "Missed";
  el.feedbackTitle.textContent = correct ? "Correct" : item.answer;
  el.feedbackText.textContent = `${item.answer} · ${tenseLabel}`;
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
  el.finalScore.textContent = state.score.toLocaleString();
  el.finalSummary.textContent = `${name}: ${correctCount}/${total} correct`;
  renderReview(state.history);
  saveBestScore(name, state.score, correctCount, total);
}

function renderReview(history) {
  el.reviewList.replaceChildren(...history.map((entry) => {
    const item = document.createElement("article");
    item.className = `review-item ${entry.correct ? "correct" : "missed"}`;
    const title = document.createElement("strong");
    title.textContent = entry.prompt;
    const answer = document.createElement("span");
    answer.textContent = entry.answer;
    item.append(title, answer);
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
  state.score = 0;
  state.streak = 0;
  state.currentIndex = 0;
  state.history = [];
  updateStatus();
}

function currentItem() {
  return state.deck[state.currentIndex];
}

function translationChoices(item) {
  const decoys = shuffle(items.filter((candidate) => candidate.answer !== item.answer))
    .slice(0, 3)
    .map((candidate) => ({ answer: candidate.answer }));
  return shuffle([{ answer: item.answer }, ...decoys]);
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
  const total = state.deck.length || items.length;
  const round = state.deck.length ? Math.min(state.currentIndex + 1, total) : 0;
  el.round.textContent = `${round}/${total}`;
}

function saveBestScore(name, score, correct, total) {
  const previous = Number(localStorage.getItem("cookieClashBest") || 0);
  if (score >= previous) {
    localStorage.setItem("cookieClashBest", String(score));
    localStorage.setItem("cookieClashBestSummary", `${name}: ${score} points, ${correct}/${total}`);
  }
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

updateStatus();
