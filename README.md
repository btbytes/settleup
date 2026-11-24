# Settle Up

**Settle Up** is a single-file, browser-based poker buy-in and final settlement ledger. It tracks home-game buy-ins and ending chip counts, fairly adjusts for missing or overcounted chips, calculates minimal who-pays-whom transfers, and keeps all data locally in your browser.

## What the App Does

- **Game setup**: Automatically selects today's date, lets you enter the game location, and defaults to `1 buy-in = 100 chips = $20.00` (with an editable dollar value per buy-in from `$1` to `$1,000`).
- **Interactive player ledger**: Add or remove player rows dynamically with validation for:
  - **Player Name** (required, unique per game)
  - **Buy-in Count** (whole numbers `1`–`50`)
  - **Cash-out Chip Count** (whole numbers `0`–`5000`)
- **Live calculations**: Displays each player's `In $`, exact `Out $`, and `Raw net` alongside live footer totals as you type.
- **Game summary & minimal settlements**: Clicking **Calculate settlement** produces:
  - **Game Summary**: `Buy-in Total`, `Cash-out Total`, and `Cash-out Difference` (in dollars and chips).
  - **Final Transactions**: Minimal `Payer` → `Pays` → `Receiver` transfers with interactive `Paid` / `Open` checkboxes and a **Copy summary** button.
  - **Player-by-player ledger breakdown**: Collapsible table showing each player's raw net, adjustment, and exact final net.
  - **Transparent explanation**: Step-by-step list under *How the final adjustment was done* plus an explicit **Rounding note** whenever payouts are rounded down or sub-`$1.00` transfers are removed.
- **Sample game & convenience tools**:
  - **Load sample** (at the top of the **Help** popup): Loads a realistic 8-player game (buy-ins from `1` to `6`, where total buy-ins are less than total cash-outs) to demonstrate overage adjustments, rounding down, and sub-`$1.00` payout removal.
  - **New game** and **Undo** bar for accidental deletions or resets.
  - Built-in **Help** modal explaining chip rates, rules, and a worked example.
- **Local browser persistence & dark theme**: Automatically saves the active game, results, `Paid` checkmarks, and light/dark theme preference to browser storage (`localStorage` / `sessionStorage`). No login or backend is used, and data never leaves the user's browser.

## How Settlement & Adjustments Work

1. **Keep initial cash-outs exact**: Initial cash-out chip values are converted to dollars to the penny without rounding down to whole dollars (e.g., `4` chips at `$0.20` stays `$0.80`).
2. **Distribute cash-out differences fairly to the penny**:
   - If cash-out chips differ from buy-in chips (missing chips or overcounted/unlogged buy-in chips), the difference is distributed across all winners proportionally to their winnings down to the exact cent (largest-remainder allocation) without forcing any winner below `$0.00`.
   - If no player finished ahead, the difference is shared equally across all participants to the penny.
3. **Compute minimal transactions down to the penny**: Exact payer-to-receiver balance matches settle first, followed by largest-to-largest matching down to the penny.
4. **Always round payouts down toward `$0.00`**:
   - After final transactions are computed to the penny, every payout is rounded **down** to the lower whole dollar (never rounded up to the higher dollar — e.g., `$30.80` becomes `$30.00`).
   - Any payout under `$1.00` rounds down to `$0.00` and that line is removed.
   - All rounded-down amounts and removed lines are explicitly noted in the transaction table, the rounding note banner, the adjustment steps, and the copied plain-text summary.

## Constraints & Instructions Used to Build the App

This app was built directly from [SPECIFICATION.md](SPECIFICATION.md) and the following refined instructions:

- **Hosting & technology**: Cloudflare-native static hosting friendly — plain HTML, CSS, and vanilla JavaScript in a single self-contained `index.html` with no build step, framework, or backend server.
- **No authentication & strict privacy**: Zero accounts, zero server calls, automatic browser storage persistence, and a footer notice confirming that data never leaves the user's browser.
- **Visual design & mobile-first layout**: Clean, attractive stationery-ledger UI paired with a high-contrast dark summary board, tabular monospace figures, a single-column vertical layout sized for easy phone scrolling (`640px` max width), mobile-friendly font sizes (`16px` inputs to prevent iOS zoom, `40–44px` touch targets), and accessible controls.
- **Input bounds & defaults**:
  - Auto-select current date; free-text place field.
  - Whole-number buy-ins (`1`–`50`) and chip cash-outs (`0`–`5000`); add/delete rows freely.
  - Default `1 buy-in = 100 chips = $20.00` (with an optional rate override in the ledger header).
- **Rounding & discrepancy rules**:
  - Do **not** round down initial cash-outs.
  - Calculate final transactions down to the penny first, then round down **Payouts**.
  - Always round down toward `$0.00` — never round up to the higher dollar.
  - Remove any payout line under `$1.00`.
  - Clearly note all rounding down and explain how the final adjustment was done.
- **Sample data**:
  - Provide an 8-player sample game with buy-ins ranging from `1` to `6` showing the common scenario where total buy-ins are less than total cash-outs.
- **License & footer**:
  - Include a footer note stating that the code is released under the public domain and that user data never leaves the browser.

## Usage & Deployment

- **Run locally**: Open `index.html` directly in any modern web browser.
- **Deploy**: Upload `index.html` to Cloudflare Pages, Cloudflare R2 static hosting, or any static file host.

## Repository Files

- `index.html` — Complete self-contained application (HTML, CSS, and JavaScript).
- `SPECIFICATION.md` — Original project specification.
- `README.md` — Overview, settlement rules, and build constraints.

## License

This code is released under the **public domain**.
