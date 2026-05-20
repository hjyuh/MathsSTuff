# Honors Geometry Problem Database

This workspace contains an original 800-problem database generated from the scope in `hshonorsgeometryally.pdf`.

## Deliverables

- `index.html`, `styles.css`, `app.js` - local website for browsing and filtering the database.
- `data/honors_geometry_problem_database.json` - the full problem database.
- `data/honors_geometry_problem_database.js` - browser-loadable copy of the database for opening `index.html` directly.
- `data/imagegen/unit_01` through `data/imagegen/unit_08` - internal ImageGen PNG images, one per problem.
- `data/imagegen_manifest` - prompts and destination paths used for internal ImageGen generation.
- `tools/build_geometry_database.py` - deterministic generator for the database and visuals.
- `tools/verify_geometry_database.py` - verifier for counts, schema, visuals, explanations, proofs, and difficulty distribution.

## Coverage

- 8 units total.
- 100 problems per unit.
- 800 problems total.
- 800 internal ImageGen PNG images total after `tools/use_imagegen_assets.py` is run.
- Difficulty mix in every unit: 25 easy, 30 moderate, 25 challenging, 20 honors.
- Proof-required problems in every unit, with proof solutions.
- Step-by-step explanations for every problem.

## Database Fields

Each problem includes:

- `id`
- `unit`
- `unit_title`
- `unit_problem_number`
- `standard`
- `topic`
- `difficulty`
- `problem_type`
- `question`
- `answer`
- `explanation`
- `proof_required`
- `proof`
- `visual_required`
- `visual_alt_text`
- `visual_path`
- `tags`
- `source_alignment`

## Regenerate

```powershell
python .\tools\build_geometry_database.py
```

## Verify

```powershell
python .\tools\verify_geometry_database.py
python .\tools\verify_imagegen_assets.py
```

## Switch Database To Internal ImageGen Assets

```powershell
python .\tools\use_imagegen_assets.py
```

## Open Website

Open `index.html` directly in a browser.

## Run Website With A Local Server

```powershell
python -m http.server 8000
```

Then open `http://localhost:8000/`.
