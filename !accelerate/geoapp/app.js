const state = {
  database: null,
  problems: [],
  filtered: [],
  selectedId: null,
};

const elements = {
  sourceSummary: document.querySelector("#sourceSummary"),
  totalCount: document.querySelector("#totalCount"),
  visibleCount: document.querySelector("#visibleCount"),
  proofCount: document.querySelector("#proofCount"),
  searchInput: document.querySelector("#searchInput"),
  unitSelect: document.querySelector("#unitSelect"),
  difficultySelect: document.querySelector("#difficultySelect"),
  typeSelect: document.querySelector("#typeSelect"),
  standardSelect: document.querySelector("#standardSelect"),
  proofOnly: document.querySelector("#proofOnly"),
  unitStrip: document.querySelector("#unitStrip"),
  resetButton: document.querySelector("#resetButton"),
  listTitle: document.querySelector("#listTitle"),
  problemList: document.querySelector("#problemList"),
  detailUnit: document.querySelector("#detailUnit"),
  detailDifficulty: document.querySelector("#detailDifficulty"),
  detailType: document.querySelector("#detailType"),
  detailTitle: document.querySelector("#detailTitle"),
  detailStandard: document.querySelector("#detailStandard"),
  detailVisual: document.querySelector("#detailVisual"),
  detailAlt: document.querySelector("#detailAlt"),
  detailQuestion: document.querySelector("#detailQuestion"),
  detailAnswer: document.querySelector("#detailAnswer"),
  detailExplanation: document.querySelector("#detailExplanation"),
  proofSection: document.querySelector("#proofSection"),
  detailProof: document.querySelector("#detailProof"),
  detailAlignment: document.querySelector("#detailAlignment"),
};

function titleCase(value) {
  return String(value)
    .split(/[_\s-]+/)
    .filter(Boolean)
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(" ");
}

function uniqueSorted(values) {
  return [...new Set(values)].sort((a, b) => String(a).localeCompare(String(b), undefined, { numeric: true }));
}

function fillSelect(select, values, formatter = (value) => value) {
  for (const value of values) {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = formatter(value);
    select.append(option);
  }
}

function buildControls() {
  const units = state.database.metadata.units;
  for (const unit of units) {
    const option = document.createElement("option");
    option.value = String(unit.unit);
    option.textContent = `Unit ${unit.unit}: ${unit.title}`;
    elements.unitSelect.append(option);

    const button = document.createElement("button");
    button.type = "button";
    button.className = "unit-button";
    button.dataset.unit = String(unit.unit);
    button.textContent = `U${unit.unit}`;
    button.addEventListener("click", () => {
      elements.unitSelect.value = String(unit.unit);
      applyFilters();
    });
    elements.unitStrip.append(button);
  }

  fillSelect(elements.difficultySelect, ["easy", "moderate", "challenging", "honors"], titleCase);
  fillSelect(elements.typeSelect, uniqueSorted(state.problems.map((problem) => problem.problem_type)), titleCase);
  fillSelect(elements.standardSelect, uniqueSorted(state.problems.map((problem) => problem.standard)));
}

function problemMatches(problem) {
  const search = elements.searchInput.value.trim().toLowerCase();
  const unit = elements.unitSelect.value;
  const difficulty = elements.difficultySelect.value;
  const type = elements.typeSelect.value;
  const standard = elements.standardSelect.value;

  if (unit !== "all" && String(problem.unit) !== unit) return false;
  if (difficulty !== "all" && problem.difficulty !== difficulty) return false;
  if (type !== "all" && problem.problem_type !== type) return false;
  if (standard !== "all" && problem.standard !== standard) return false;
  if (elements.proofOnly.checked && !problem.proof_required) return false;

  if (!search) return true;

  const haystack = [
    problem.id,
    problem.unit_title,
    problem.standard,
    problem.topic,
    problem.problem_type,
    problem.difficulty,
    problem.question,
    problem.answer,
    problem.explanation,
    problem.proof || "",
    problem.source_alignment,
  ]
    .join(" ")
    .toLowerCase();

  return haystack.includes(search);
}

function applyFilters() {
  state.filtered = state.problems.filter(problemMatches);
  elements.visibleCount.textContent = state.filtered.length.toLocaleString();
  elements.listTitle.textContent = `${state.filtered.length.toLocaleString()} problem${state.filtered.length === 1 ? "" : "s"}`;

  updateUnitButtons();
  renderList();

  const selectedStillVisible = state.filtered.some((problem) => problem.id === state.selectedId);
  if (!selectedStillVisible) {
    selectProblem(state.filtered[0]?.id || null);
  } else {
    markActiveRow();
  }
}

function updateUnitButtons() {
  const activeUnit = elements.unitSelect.value;
  for (const button of elements.unitStrip.querySelectorAll(".unit-button")) {
    button.classList.toggle("active", button.dataset.unit === activeUnit);
  }
}

function renderList() {
  elements.problemList.innerHTML = "";

  if (state.filtered.length === 0) {
    const empty = document.createElement("div");
    empty.className = "empty-state";
    empty.textContent = "No problems match the current filters.";
    elements.problemList.append(empty);
    return;
  }

  const fragment = document.createDocumentFragment();
  for (const problem of state.filtered) {
    const row = document.createElement("button");
    row.type = "button";
    row.className = "problem-row";
    row.dataset.id = problem.id;
    row.innerHTML = `
      <span class="row-top">
        <span class="problem-id">${problem.id}</span>
        <span class="chip ${problem.difficulty}">${titleCase(problem.difficulty)}</span>
      </span>
      <span class="problem-topic">${problem.topic}</span>
      <span class="problem-preview">${problem.question}</span>
      <span class="chips">
        <span class="chip">Unit ${problem.unit}</span>
        <span class="chip">${problem.standard}</span>
        <span class="chip">${titleCase(problem.problem_type)}</span>
        ${problem.proof_required ? '<span class="chip honors">Proof</span>' : ""}
      </span>
    `;
    row.addEventListener("click", () => selectProblem(problem.id));
    fragment.append(row);
  }

  elements.problemList.append(fragment);
  markActiveRow();
}

function markActiveRow() {
  for (const row of elements.problemList.querySelectorAll(".problem-row")) {
    row.classList.toggle("active", row.dataset.id === state.selectedId);
  }
}

function selectProblem(problemId) {
  state.selectedId = problemId;
  markActiveRow();

  const problem = state.problems.find((item) => item.id === problemId);
  if (!problem) {
    elements.detailTitle.textContent = "No problem selected";
    elements.detailStandard.textContent = "";
    elements.detailVisual.removeAttribute("src");
    elements.detailVisual.alt = "";
    elements.detailAlt.textContent = "";
    elements.detailQuestion.textContent = "";
    elements.detailAnswer.textContent = "";
    elements.detailExplanation.textContent = "";
    elements.proofSection.hidden = true;
    elements.detailAlignment.textContent = "";
    return;
  }

  elements.detailUnit.textContent = `Unit ${problem.unit}: ${problem.unit_title}`;
  elements.detailDifficulty.textContent = titleCase(problem.difficulty);
  elements.detailType.textContent = titleCase(problem.problem_type);
  elements.detailTitle.textContent = `${problem.id} - ${problem.topic}`;
  elements.detailStandard.textContent = `${problem.standard} | Problem ${problem.unit_problem_number} of Unit ${problem.unit}`;
  elements.detailVisual.src = `data/${problem.visual_path}`;
  elements.detailVisual.alt = problem.visual_alt_text;
  elements.detailAlt.textContent = problem.visual_alt_text;
  elements.detailQuestion.textContent = problem.question;
  elements.detailAnswer.textContent = problem.answer;
  elements.detailExplanation.textContent = problem.explanation;
  elements.detailAlignment.textContent = problem.source_alignment;

  if (problem.proof_required && problem.proof) {
    elements.proofSection.hidden = false;
    elements.detailProof.textContent = problem.proof;
  } else {
    elements.proofSection.hidden = true;
    elements.detailProof.textContent = "";
  }
}

function resetFilters() {
  elements.searchInput.value = "";
  elements.unitSelect.value = "all";
  elements.difficultySelect.value = "all";
  elements.typeSelect.value = "all";
  elements.standardSelect.value = "all";
  elements.proofOnly.checked = false;
  applyFilters();
}

function bindEvents() {
  for (const control of [
    elements.searchInput,
    elements.unitSelect,
    elements.difficultySelect,
    elements.typeSelect,
    elements.standardSelect,
    elements.proofOnly,
  ]) {
    control.addEventListener("input", applyFilters);
    control.addEventListener("change", applyFilters);
  }

  elements.resetButton.addEventListener("click", resetFilters);
}

async function init() {
  try {
    if (window.HONORS_GEOMETRY_DATABASE) {
      state.database = window.HONORS_GEOMETRY_DATABASE;
    } else {
      const response = await fetch("data/honors_geometry_problem_database.json");
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }
      state.database = await response.json();
    }
    state.problems = state.database.problems;

    elements.sourceSummary.textContent = `${state.database.metadata.source_pdf} | ${state.database.metadata.problem_count} aligned problems | ${state.database.metadata.problems_per_unit} per unit`;
    elements.totalCount.textContent = state.problems.length.toLocaleString();
    elements.proofCount.textContent = state.problems.filter((problem) => problem.proof_required).length.toLocaleString();

    buildControls();
    bindEvents();
    applyFilters();
  } catch (error) {
    elements.sourceSummary.textContent = "Could not load data/honors_geometry_problem_database.json. Run a local web server from this folder.";
    elements.problemList.innerHTML = `<div class="empty-state">Database load failed: ${error.message}</div>`;
  }
}

init();
