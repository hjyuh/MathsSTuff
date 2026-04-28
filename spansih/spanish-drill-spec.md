# Spanish Preterite & Imperfect Drill Game — Build Spec

## Context

Building a study game for a Spanish test tomorrow on preterite and imperfect conjugation. Target user is an intermediate Spanish student who knows the regular patterns but struggles with irregulars and with *producing* forms from scratch (recognition is stronger than recall). The game should bridge that gap.

Inspired by Blooket — quick-hit conjugation questions with a light game layer for motivation. Not trying to build the full Blooket game-mode system; just need a fun drill wrapper around a good question bank.

## Build requirements

- **Single HTML file** (HTML + CSS + JS all inline). Must work when opened locally by double-clicking. No build step, no server, no npm install.
- Vanilla JS. No React, no framework. Tailwind via CDN is fine if needed but not required.
- Works offline once opened.
- Responsive enough to use on both desktop and phone.

## Question bank (build into the JS)

Two question types, both covering both tenses.

### Type A: Multiple choice

Prompt format: "Conjugate **[verb]** in the **[tense]**, **[subject]** form."
Example: "Conjugate **tener** in the **preterite**, **yo** form."

Four options, one correct. Distractors should be plausible wrong answers — specifically:
1. Right tense, wrong person (e.g. "tuvimos" for yo/preterite/tener)
2. Right person, wrong tense (e.g. "tenía" for yo/preterite/tener)
3. Regular ending applied to irregular stem (e.g. "tení" for yo/preterite/tener)
4. Correct answer ("tuve")

Shuffle the four options so correct is not always in the same position.

### Type B: Free response (FRQ)

Same prompt, but user types the answer into a text input. Accept answer with or without accent marks for FRQ (this is a study tool, and accent-typing on keyboards without Spanish layout is a pain that shouldn't block learning). Display correct answer with accents after submission so they still see the proper form.

## Verb & form coverage

### All six subject persons

yo, tú, él/ella/usted, nosotros, vosotros, ellos/ellas/ustedes

### Verbs to include

**Regular verbs (for pattern practice):**
- -ar: hablar, caminar, estudiar, trabajar, cantar, bailar, mirar, escuchar, comprar, llegar*, buscar*, pagar*, empezar*
- -er: comer, beber, aprender, correr, vender, leer, comprender
- -ir: vivir, escribir, recibir, abrir, subir, decidir

*The starred verbs have spelling changes in the yo preterite (llegué, busqué, pagué, empecé) — include these and make sure the conjugator gets them right.

**Irregular preterite (critical):**
- Tier 1: ser, ir (same forms: fui, fuiste...), tener, estar, hacer, decir, dar
- Tier 2: poder, poner, saber, venir, querer, traer
- Tier 3 (stretch): andar, conducir, producir
- Stem-changing -ir (3rd person only): dormir, pedir, sentir, servir, morir, preferir, repetir

**Irregular imperfect (only three verbs total):**
- ser (era, eras, era, éramos, erais, eran)
- ir (iba, ibas, iba, íbamos, ibais, iban)
- ver (veía, veías, veía, veíamos, veíais, veían)

### Conjugation logic

Build a conjugator function rather than hardcoding every single form. Something like:

```js
conjugate(verb, tense, person)
```

Where the function:
1. Looks up the verb in an IRREGULARS table first. If present, returns the irregular form directly.
2. Otherwise applies regular endings based on the infinitive ending (-ar / -er / -ir).
3. Handles the -car/-gar/-zar yo-preterite spelling changes.
4. Handles -ir stem-changers in preterite 3rd person (él/ellos).

Irregulars table entries look like:

```js
IRREGULARS = {
  tener: {
    preterite: { yo: "tuve", tú: "tuviste", él: "tuvo", nosotros: "tuvimos", vosotros: "tuvisteis", ellos: "tuvieron" }
  },
  ser: {
    preterite: { yo: "fui", tú: "fuiste", él: "fue", nosotros: "fuimos", vosotros: "fuisteis", ellos: "fueron" },
    imperfect: { yo: "era", tú: "eras", él: "era", nosotros: "éramos", vosotros: "erais", ellos: "eran" }
  },
  // ... etc
}
```

(Full irregulars table needs to be filled in. Use the authoritative forms — verify against WordReference or SpanishDict if in doubt.)

## Game mechanics

Light game layer, not full Blooket. Two modes:

### Mode 1: Multiple Choice Gauntlet
- 20 questions per round.
- Running score, timer per question (10 seconds soft — it shows a countdown but doesn't auto-submit; just for urgency).
- Streak counter: consecutive correct answers show a multiplier (×2 at 5 streak, ×3 at 10 streak).
- End-of-round screen: score, accuracy %, list of missed questions with correct answers.
- "Retry missed only" button to drill the specific forms that were wrong.

### Mode 2: FRQ Mode
- Same 20-question format but text input instead of multiple choice.
- No timer (user can think).
- Accept answer with or without accents (normalize before comparing).
- Show correct answer with accents after each submission.
- Same end-of-round + retry-missed features.

### Mode toggle
- User picks mode at start screen.
- Plan: start with multiple choice to warm up, switch to FRQ when consistently scoring 80%+.

### Difficulty filter (start screen)
- Checkboxes to include/exclude: Regular verbs, Tier 1 irregulars, Tier 2 irregulars, Tier 3 stretch irregulars, Stem-changers
- Checkboxes for tenses: Preterite, Imperfect, or both
- Default: all checked except Tier 3 stretch.

### Stats (persistent if possible)
- Per-verb accuracy stored in memory for the session. If browser storage is OK in this environment, localStorage is fine; if not, just session-level.
- At end of session, show "weakest verbs" list — the verbs with the lowest accuracy. Those are tomorrow's priority.

## Visual design

Clean and minimal. Doesn't need to look like Blooket. A dark theme with a bright accent color for correct answers (green) and a muted red for wrong answers. Big readable font for the prompt. Keep the game chrome light — the focus is on the conjugation, not the game.

Show the question prominently, options/input below, running score + streak in a corner.

## Acceptance criteria

1. Opens by double-clicking the .html file.
2. Mode selection + difficulty filter work.
3. Multiple choice mode generates questions from the selected pool with proper distractors.
4. FRQ mode accepts answers with or without accents.
5. Conjugator returns correct forms for all listed verbs in all 6 persons × 2 tenses.
6. End-of-round screen lists missed questions; "retry missed" feature works.
7. No crashes on empty difficulty selection (maybe disable Start button until at least one category is selected).

## Non-goals

- Multiplayer
- Accounts / login
- Blooket-style mascots or skins (keep it clean)
- Additional tenses (no subjunctive, future, etc.)
- Present tense (already covered)
- Vocabulary / translation — this is a pure conjugation drill

## Known gotchas for the conjugator

1. **-car/-gar/-zar yo preterite:** buscar → busqué (NOT buscé), llegar → llegué (NOT llegé), empezar → empecé (NOT empezé).
2. **hacer él-form preterite:** hizo (z not c, to preserve soft sound before o).
3. **decir / traer / conducir ellos-form:** dijeron / trajeron / condujeron (-eron, NOT -ieron, because of j-stem).
4. **-ir stem-changers only in 3rd person preterite:** dormir → dormí, dormiste, **durmió**, dormimos, dormisteis, **durmieron**. Only él and ellos change; the rest use the regular stem.
5. **ver imperfect keeps the e:** veía (not vía). It's technically "regular" in imperfect but you need the stem "ve" not just "v".
6. **Regular -ar nosotros preterite = nosotros present:** hablamos is both "we speak" and "we spoke". Same for -ir (vivimos). For -er they differ (comemos vs comimos).
7. **ser and ir preterite are identical.** Same six forms for both verbs. Don't accidentally differentiate them.

Make sure these are all tested with at least one question in the generated pool before shipping.

## Starter file name

Suggested: `spanish-preterite-imperfect-drill.html`

Output directory: wherever the user specifies. If no preference, put it alongside this spec file.
