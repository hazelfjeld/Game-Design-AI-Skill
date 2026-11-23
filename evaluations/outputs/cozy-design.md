This is a design proposal produced for a fictional scenario; no playable prototype or human playtest was performed during evaluation.

## Recommendation: make a small sanctuary visit

Build **one quiet lagoon with three individually recognizable rays of one fictional species**. Give players about ten minutes of things to discover, then let them linger.

**Design hypothesis:** learning a ray’s habits, inviting it closer, and receiving a familiar response may create attachment without making care feel obligatory. Your first playable should investigate that hypothesis. It cannot establish long-term appeal yet.

Assume two four-hour afternoons and an engine you already know.

| Direction | What it emphasizes | Tradeoff for this prototype |
|---|---|---|
| **Personal sanctuary — recommended** | Recognition, companionship, gentle interaction | Depends on convincing movement and responses; offers little progression |
| Breeding hatchery | Anticipation, inheritance, collection | Needs generations, readable traits, and many outcomes before its decisions become meaningful |
| Small ocean expedition | Discovery and returning home | Adds navigation, environments, and encounter work before testing attachment |

Keep 200 species, breeding, trading, and exploration in the future vision. They are separate design questions. A market also raises the question of whether players value rays as companions or exchangeable assets.

## Concrete rules

Use a fixed camera and simple 2D movement. A shared manta silhouette can support different markings and motion patterns.

**Three residents:**

- **Pip:** spotted fins; swims short circles; approaches promptly.
- **Moss:** crescent marking; rests beside a shell; pauses before approaching.
- **Ribbon:** striped back; swims broad arcs; makes one loop before approaching.

These are fictional character habits, not claims about manta biology.

**The interaction loop:** notice a resident → select it → offer a snack → watch its characteristic approach and response → return later and receive a familiar greeting.

Implement these rules:

1. **Selection:** clicking a ray opens a small card with its name and an **Offer snack** button. Use a generous click area. Distinguish residents through markings, movement, and names, rather than color alone.
2. **Inviting:** the snack appears at a fixed, clear spot beside the selected ray. Pip begins immediately; Moss pauses for two seconds; Ribbon makes one loop. Each then approaches, eats, and performs a brief fin flutter. Treat these timings as starting values to adjust.
3. **State:** each ray has `swimming`, `approaching`, `responding`, and `resting` states. A complete interaction takes roughly six to ten seconds. Further snack clicks during that interaction do not restart or queue it. Players can select another ray immediately.
4. **Recognition:** after its first completed interaction, that resident becomes familiar. Subsequent invitations begin with a distinct greeting: Pip twirls, Moss peeks out, Ribbon rolls gently. Keep this as one flag per ray, with no affection bar.
5. **Care:** snacks are unlimited. There is no hunger decay, illness, failure, currency, daily obligation, or punishment for leaving. Rays remain content when ignored. Feeding is a shared ritual.
6. **A small personal choice:** if the core works in time, allow one decorative shell to move between three preset positions. Moss rests beside it. Clicking a new position replaces the previous choice; nothing can be lost.
7. **Pacing:** show one invitation—“Choose a ray and offer a snack”—then remove it after the first interaction. Include pause and mute. Avoid timers and completion checklists.

The deliberate limitation is that the player has few actions. The prototype asks whether the responses make those actions worth repeating. If they do not, extra species would multiply an unresolved problem.

## Spend the two afternoons deliberately

**Afternoon one: complete the smallest loop.**

- First hour: one lagoon, one ray, selection, and a runnable build.
- Next two hours: swimming, inviting, response, and recovery to swimming.
- Final hour: duplicate the ray through data, adding the three markings and movement routines.

**Afternoon two: make the interaction readable.**

- First two hours: improve silhouettes, fin motion, response timing, and quiet feedback; add greetings and the first prompt.
- Next hour: verify repeated clicks, switching residents, pause, and boundaries. Add the shell only if the core is reliable.
- Final hour: package the build and run or prepare the first human sessions.

Cut the movable shell first, then extra visual effects. Preserve recognizable residents and responsive interaction. Give AI coding help bounded tasks with explicit states and completion conditions; you retain responsibility for playing the integrated result.

## What to test

Invite a few people who enjoy creature care or relaxed games. A first round of three to five people is a practical discovery exercise, not a statistical guarantee.

Say: **“Spend a few minutes here however you like. You can stop whenever you want.”** Avoid announcing that they should become attached.

Record whether they understand the first action without help, revisit a particular ray voluntarily, and distinguish residents by behavior. Afterwards ask:

- “What differences did you notice?”
- “Was there anyone you wanted to visit again? Why?”
- “Did anything feel like an obligation?”

Recognition alone does not establish affection; staying longer does not establish relaxation. Combine observed actions with participants’ explanations.

If residents blur together, strengthen behavioral differences. If care feels compulsory, revise its framing and feedback. If interactions feel pleasant but empty, test one additional expressive choice before expanding collection.

**Next action:** build Pip’s complete interaction today. There are no human results or inspected build observations yet; this proposal remains a set of design hypotheses. The next decision is whether a responsive individual is compelling enough to justify building the wider sanctuary around it.
