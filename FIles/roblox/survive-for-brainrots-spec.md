# SURVIVE FOR BRAINROTS — Game Design Spec v1

**Pivot from Brainrot Drop (Dropper) → Survival Field**

Mahmoud · February 2026 · Buildable Spec

---

## 1. One-Sentence Pitch

Run into a dangerous field, grab brainrots, survive, and make it back to base before you die — the deeper you go, the rarer the loot and the deadlier the threats.

**10-word loop:** Run deep, grab brainrots, survive hazards, bank at base.

---

## 2. Why This Works

The top Roblox games right now (Escape Tsunami 500K CCU, Survive Lava 100K+ CCU) all share one architecture:

- Spatial risk gradient (further = rarer + more dangerous)
- Simple repeating hazard on the field
- Base with slots generating passive income
- Speed/carry/rebirth progression

We keep the proven architecture but differentiate with **escalating multi-hazard zones** instead of one repeated threat. Each zone deeper introduces a new danger layer on top of everything before it. This gives us the "have you gotten past the meteor zone?" word-of-mouth that single-hazard games can't generate.

---

## 3. Core Play Loop

```
SPAWN AT BASE
  ↓
RUN INTO THE FIELD (voluntary — you choose when to go)
  Brainrots spawn on rocks/platforms across the field
  Further from base = rarer brainrots = more income/sec
  Hazards active everywhere, escalating with depth
  Grab brainrots (up to carry cap, default 5)
  ↓
CHOOSE: Push deeper or turn back?
  Greed vs. safety — pure player decision, no timer forcing you
  ↓
RETURN TO BASE (or die trying)
  ↓
BANK BRAINROTS → placed on base slots → generate passive income
  ↓
COLLECT COINS → upgrade speed, buy base slots, rebirth
  ↓
REPEAT (no cooldown, no rounds, no waiting — instant re-entry)
```

**If you die:**
- Drop ALL carried brainrots at your death location
- Other players can grab your dropped loot (feeding frenzy)
- You respawn at base with nothing from that run
- Brainrots already placed on your base are SAFE

---

## 4. The Field

### 4.1 Layout

One long continuous field extending outward from the base area. NOT instanced — all players share the same field on the server. Approximately **2000-3000 studs long**, divided into **8 rarity zones**.

The field is mostly flat terrain with rocks, platforms, and structures of varying heights scattered throughout. Taller structures appear in deeper zones (requiring jump height from rebirth to access). The field should feel like a dangerous wasteland that gets progressively more hostile-looking.

All players (6-10 per server) are on the field simultaneously. You see people running past you, dying, dropping loot. Every death is visible social content.

### 4.2 Rarity Zones

| Zone | Distance from Base | Rarity | Brainrot Income Range | Visual Identity |
|------|-------------------|--------|----------------------|-----------------|
| 1 | 0–250 studs | Common | $1–10/sec | Green grass, safe-looking, bright |
| 2 | 250–500 studs | Uncommon | $10–50/sec | Yellowing terrain, scattered debris |
| 3 | 500–800 studs | Rare | $50–250/sec | Rocky ground, darker sky |
| 4 | 800–1100 studs | Epic | $250–1K/sec | Cracked earth, purple-tinted fog |
| 5 | 1100–1500 studs | Legendary | $1K–10K/sec | Volcanic rock, red ambient light |
| 6 | 1500–1900 studs | Mythic | $10K–100K/sec | Floating islands, void below |
| 7 | 1900–2400 studs | Celestial | $100K–1M/sec | Crystal formations, ethereal glow |
| 8 | 2400–3000 studs | Divine | $1M–10M/sec | Pure void, single accent color, minimal geometry |

Zone boundaries should be visually obvious — terrain color changes, particle walls, signage. Players should always know which zone they're in.

### 4.3 Brainrot Spawning

- Brainrots spawn on rocks/platforms throughout each zone
- 15-25 active brainrots per zone at any time
- Despawn timer: 45-60 seconds per brainrot (creates urgency)
- Respawn: new brainrots continuously spawn to replace despawned/collected ones
- Rarity within zone: mostly that zone's rarity, small chance of one tier higher
- Mutations (Gold, Diamond, Rainbow) roll independently — same system as current BrainrotConfig
- Brainrot is visible from a distance with rarity-colored glow/aura
- Walk up and press interact (ProximityPrompt) to pick up

### 4.4 Carrying

- Default carry capacity: **5 brainrots**
- Upgradable to 10 with Robux game pass ("+5 Carry" — permanent)
- While carrying, brainrots are displayed as small icons on the HUD showing what you're holding
- Carrying is the vulnerability — everything in your hands is at risk until banked

---

## 5. Hazard System — Escalating Danger

This is the core differentiator. The field has a BASE HAZARD active everywhere, and each deeper zone ADDS a new hazard layer. By zone 5+, players are dealing with 4-5 simultaneous threats. This creates natural difficulty scaling without any artificial gates.

### 5.1 Hazard Layers

| Introduced At | Hazard | Behavior | Active In |
|--------------|--------|----------|-----------|
| Zone 1 (everywhere) | **Lava Eruptions** | Floor sections glow red for 2 sec warning, then erupt with damage. Random positions, periodic cycle (every 15-20 sec). Jump or move off to survive. | ALL zones |
| Zone 2+ | **Toxic Gas Clouds** | Green fog patches that drift slowly across the field. Walking through deals damage over time. Visible from distance, predictable movement. | Zones 2-8 |
| Zone 3+ | **Falling Meteors** | Shadows appear on ground 1.5 sec before impact. Small AOE damage zone. Frequency increases with depth. | Zones 3-8 |
| Zone 4+ | **Roaming Monsters** | NPC enemies that patrol zones. Touch = instant kill. Visible, avoidable with awareness. More monsters + faster in deeper zones. | Zones 4-8 |
| Zone 5+ | **Lightning Strikes** | Random targeted strikes on players. Brief warning flash, then bolt. Harder to dodge than meteors. Frequency increases deeper. | Zones 5-8 |
| Zone 6+ | **Void Pits** | Sections of ground randomly open into void for 3-4 seconds. Fall in = death. Ground cracks as warning. | Zones 6-8 |
| Zone 7+ | **Homing Projectiles** | Slow-tracking projectiles that follow nearest player. Must be outrun or dodged around obstacles. | Zones 7-8 |
| Zone 8 | **All of the above + Darkness** | Reduced visibility. Can only see ~30 studs around you. All other hazards at maximum frequency. | Zone 8 only |

### 5.2 Hazard Design Principles

- **Every hazard has a visual/audio warning.** No unfair deaths. The kid who dies should know WHY and feel like they COULD have dodged it.
- **Hazards stack, not replace.** Zone 5 has lava + gas + meteors + monsters + lightning. That's 5 things to track simultaneously. Overwhelming but learnable.
- **Hazard frequency/intensity increases with depth.** Zone 3 might get a meteor every 8 seconds. Zone 7 might get one every 2 seconds.
- **All hazards are server-side.** Same hazard positions for all players. If you see someone dodge a meteor, you know where it hit.

### 5.3 Death

- Any lethal hazard contact = death
- Character ragdolls dramatically (comedic splat, lean into absurdity)
- ALL carried brainrots drop at death location as glowing pickups
- Dropped brainrots persist for **15 seconds** — ANY player can grab them
- Dead player respawns at base immediately
- Death location is briefly marked with a skull particle effect (visible to all)

**The death → loot drop → feeding frenzy cycle is the social engine.** When someone dies deep in the legendary zone carrying 5 brainrots, every nearby player faces a choice: risk going to the loot pile (which is in a dangerous area where someone just died) or play it safe. This creates emergent social drama every time someone dies.

---

## 6. Base System

### 6.1 What Transfers From Current Build

**Everything.** The base system we've already built IS this game's base:
- Slot system with floors (Floors/Floor1/Slots/Slot1-N)
- Brainrot placement with slam animation
- Income ticks (passive coin generation)
- Collect zone (step on to collect accumulated coins)
- Offline income accumulation + splash screen
- DataStore persistence
- HUD (coins + income display)

### 6.2 Modifications Needed

- **Claiming flow changes:** Instead of "claim then buy," brainrots you bring back are placed directly into empty slots (no coin cost to place). Income comes from placing, coins come from collecting — coins spent on upgrades, not on buying brainrots. This matches the tsunami/lava pattern and removes friction.
- **Base upgrades:** Coin-purchasable base expansion (more slots). Current floor/slot structure already supports this — just gate floor unlocks behind coin costs instead of rebirth level.

### 6.3 Banking

When a player returns to their base area (crosses back into the safe zone), carried brainrots auto-deposit into empty slots with the existing slam animation. If no empty slots, overflow brainrots are lost (incentive to upgrade base). This should be instant and satisfying — the payoff moment for the entire run.

---

## 7. Progression

### 7.1 Stats (Upgrade Shop)

Three stats, purchased with coins at the upgrade shop NPC (already built):

| Stat | Effect Per Tier | Max Tier | Why It Matters |
|------|----------------|----------|----------------|
| **Speed** | +10% movement speed | 10 | Reach deeper zones, outrun hazards, get back alive |
| **Health** | +1 hit point (base = 1 HP, die in one hit) | 10 | Survive a mistake. At tier 5, you can tank 6 hits before dying |
| **Jump** | +8% jump height | 10 | Access brainrots on taller platforms in deeper zones |

**Speed** is already wired to Humanoid.WalkSpeed.
**Health** needs a health system (damage from hazards reduces HP, 0 = death + loot drop).
**Jump** replaces Grab from previous spec. Applied to Humanoid.JumpHeight on spawn + purchase.

Cost curve: same exponential progression already in BrainrotConfig.StatUpgrades.

### 7.2 Carry Capacity

- Base carry: **5 brainrots**
- **Robux game pass: "+5 Carry Capacity"** — permanent, increases to 10
- This is the primary monetization lever. Every run, the free player banks 5 max. The paying player banks 10. Not pay-to-win (same brainrots available), just fewer trips.
- NOT upgradable with coins — Robux only. This keeps it as a clean monetization item.

### 7.3 Rebirth

Same architecture as current spec + matching what tsunami/lava games do:

- **Resets:** Speed stat (back to tier 0), Jump stat (back to tier 0)
- **Keeps:** Coins, placed brainrots, base upgrades, carry capacity, game passes
- **Gains:** Permanent income multiplier (1.5x → 2x → 3x → ... stacking)
- **Requirements:** Must reach specific speed tier + sacrifice a specific brainrot
- **Why rebirth matters:** The income multiplier means each subsequent playthrough is faster. A rebirth 5 player earning 3x income upgrades speed 3x faster than a fresh player.

12-15 rebirth levels. Each requires a higher speed threshold and a rarer sacrificed brainrot.

---

## 8. Monetization

### 8.1 Game Passes (Robux)

| Pass | Price | Effect |
|------|-------|--------|
| +5 Carry Capacity | 99 Robux | Carry 10 brainrots instead of 5 (permanent) |
| 2x Income | 149 Robux | All placed brainrots earn double (permanent) |
| Auto-Collect | 49 Robux | Coins auto-collect, no need to step on collect zone |
| VIP Base | 199 Robux | Cosmetic base upgrade + 5 extra slots |

### 8.2 Lucky Blocks

- Craftable: combine 3 brainrots + coins to create a lucky block
- Lucky blocks give a random brainrot with boosted rarity odds
- Robux lucky blocks available with even better odds
- Recipes rotate periodically (check back daily)

### 8.3 Spin Wheel

- Free spin daily (or earned through playtime milestones)
- Robux spins available
- Rewards: brainrots, coins, temporary boosts, cosmetics

### 8.4 Cosmetics

- Trails (visible while running)
- Death effects (custom ragdoll particles)
- Base themes (visual skins for your plot)
- All purely cosmetic, all visible to other players

---

## 9. What We Keep vs. What Changes

### Keep (Already Built)
- ✅ Base slot system (Floors/Slots/placement/slam animation)
- ✅ Income ticks + collect zone
- ✅ DataStore persistence (coins, stats, placed brainrots, offline income)
- ✅ BrainrotConfig (rarity tiers, income ranges, mutations, models)
- ✅ Stat shop UI + NPC ProximityPrompt
- ✅ Speed stat application (WalkSpeed)
- ✅ Claim UI (repurpose for banking confirmation or loot summary)
- ✅ HUD (coins + income display)
- ✅ Offline income + splash screen
- ✅ Animation system (idle animations for placed brainrots)

### Modify
- 🔄 **Stat definitions:** Health = HP system (new), Grab → Jump = JumpHeight application (simple)
- 🔄 **Brainrot acquisition:** Remove dropper portal + dropper spawning. Replace with field spawning (brainrots on ProximityPrompts across zones)
- 🔄 **Claiming flow:** Skip coin-cost claiming. Brainrots auto-place on return to base.
- 🔄 **Carry system:** New — track what player is currently holding (array of brainrot data, max 5/10)

### Build New
- 🆕 **The Field** (terrain + rocks + platforms across 8 zones) — Studio build
- 🆕 **Hazard system** (lava eruptions, gas, meteors, monsters, lightning, void, projectiles, darkness)
- 🆕 **HP system** (health stat, damage from hazards, death + loot drop)
- 🆕 **Carry HUD** (show what you're holding, how many slots used)
- 🆕 **Loot drop system** (death drops brainrots as pickups, 15 sec timer, other players can grab)
- 🆕 **Zone boundary detection** (track which zone player is in)
- 🆕 **Base expansion shop** (coin-purchasable slot unlocks)
- 🆕 **Lucky block machine** (combine brainrots + coins for random better one)
- 🆕 **Spin wheel UI**

### Remove
- ❌ Dropper shaft (Workspace.Dropper — no longer needed)
- ❌ Dropper portal
- ❌ Chunk system / chunk boundaries
- ❌ Glass seal mechanic
- ❌ Troll items (replaced by the hazard system creating natural chaos)

---

## 10. Build Order

| Phase | What | Days |
|-------|------|------|
| 1 | **Field blockout** — Terrain, 8 zones with visual identity, rocks/platforms, zone boundaries. Brainrot spawn points placed. | 2-3 |
| 2 | **Field spawning + carry system** — Brainrots spawn on field points, ProximityPrompt pickup, carry HUD, auto-bank on return to base | 1-2 |
| 3 | **Base hazard: Lava eruptions** — Floor warning + eruption cycle across all zones. Damage/kill on contact. | 1 |
| 4 | **HP + death system** — Health stat functional, damage from hazards, death ragdoll, loot drop for others | 1 |
| 5 | **Jump stat** — Apply to JumpHeight, taller platforms in deeper zones require it | 0.5 |
| 6 | **Zone 2-4 hazards** — Toxic gas, falling meteors, roaming monsters | 2-3 |
| 7 | **Zone 5-8 hazards** — Lightning, void pits, homing projectiles, darkness | 2-3 |
| 8 | **Rebirth system** — Reset speed/jump, income multiplier, specific brainrot sacrifice | 1 |
| 9 | **Monetization** — Game passes, lucky blocks, spin wheel, base expansion shop | 2-3 |
| 10 | **Polish + Launch** — Balance, VFX, sound, thumbnail, description | 2-3 |

**Total: ~15-20 days.** Phases 1-4 produce a playable core loop. Everything after layers onto a working game.

---

## 11. Critical Design Notes

### Why Voluntary Return (No Timer)

Tsunami/Lava games force you back on a timer. We don't. Why? Because **pure greed is a stronger psychological driver than external pressure.** When a timer kills you, you blame the game. When your own greed kills you, you blame yourself — and "I should have turned back" is the thought that triggers "one more run." Every death is the player's fault, which means every death is a learning moment, not a frustration moment.

### Why Loot Drops (Not Despawn)

When your brainrots drop and another player grabs them, that's personal. You SAW them take YOUR legendary. Grudges form. "I need to get a better one than what they stole from me." Social competition emerges without any built system. Also: a death in the legendary zone becomes a server-wide event. Everyone nearby converges on the loot pile. That's emergent content.

### Why Stacking Hazards (Not Swapping)

If each zone had a different single hazard, zone 8 would just be "the projectile zone." By stacking, zone 8 is "everything at once" — which means the skill you built dodging lava in zone 1 is still relevant 2000 studs deeper. Every skill compounds. Players never feel like previous learning was wasted.

### The Carry Cap Monetization

Making carry capacity Robux-only (not coin-upgradable) is deliberate. It's the one purchase that affects EVERY single run. A 2x Income pass only matters when you're at base. Extra slots only matter when you're banking. But carry capacity changes the fundamental risk calculation of every trip into the field. That's why it's the premium purchase — it has the highest perceived value per run.
