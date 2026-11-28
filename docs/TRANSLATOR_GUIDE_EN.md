# The Fifth Choice: Translator Guide

Thank you for translating The Fifth Choice. This guide covers everything you need: the rules, how to
fill in the translation files, and the glossary (names, terms and how each character talks).

The game was written in Spanish. You translate **from the English version**: every line you have to fill
in already shows its English translation as a comment right above it.

To see each scene in context, download the game from its itch.io page and play it in English
(Options → Language → English).

---

## 1. Rules

1. **Only fill in the `translate turkish` blocks** of the files you receive. Do not change anything else:
   not the file names, not the indentation, not the lines outside the quotes.
2. **`[mc]` and every tag in curly braces `{…}` stay exactly as they are.** Same spelling, same number, same order
   in dialogue. See section 3 for the full list.
3. **About 100 characters per line at most** (two lines of the text box). Menu choices must fit their button:
   keep them no longer than the English.
4. **Follow the glossary** in section 5: names, no honorifics, and each character's voice.
5. The Turkish version is published only on the game's official itch.io page, free like the rest of the game.
6. You are credited in the game's credits and in the credits file, with the name you choose.

Save the files as **UTF-8** with a plain text editor (VS Code, Notepad++, Sublime Text…), never with Word.

---

## 2. How to fill in a block

Each file has two kinds of blocks. Lines starting with `#` are comments: the game ignores them.

### Dialogue

What you receive:

```renpy
# game/01_prologo.rpy:63
translate turkish prologo_13fe8e7a:

    # narrador "Hay dos clases de personas en este mundo."
    # english: narrador "There are two kinds of people in this world."
    narrador "Hay dos clases de personas en este mundo."
```

- `# narrador "Hay dos…"` is the Spanish original.
- `# english: narrador "There are two…"` is the English translation: translate from this one.
- The last line is yours. **Replace only the text inside the quotes.** Keep the speaker name in front of it
  (`narrador`, `mc`, `nino`…) exactly as it is.

When you are done:

```renpy
# game/01_prologo.rpy:63
translate turkish prologo_13fe8e7a:

    # narrador "Hay dos clases de personas en este mundo."
    # english: narrador "There are two kinds of people in this world."
    narrador "Bu dünyada iki tür insan vardır."
```

Do not touch the line `translate turkish prologo_13fe8e7a:`. That code links your line to the original one.

### Interface strings (`translate turkish strings:`)

At the end of most files there is a block with menu buttons, names, labels and short texts:

```renpy
translate turkish strings:

    # game/09_menus_sistema.rpy:528
    old "IDIOMA"
    # english: "LANGUAGE"
    new "IDIOMA"
```

- `old` is the Spanish original. **Never change it.**
- **Only change the `new` line:** `new "DİL"`.
- Each `old` text appears only once in the whole game, and its translation is used everywhere that text shows up.

### Good to know

- A quote inside a line is written `\"`: `"He said \"sure\"."` Keep the backslash.
- Lines that stay the same on purpose: `"..."`, a name on its own (`"Itsuki."`), units and keys.
- `common.rpy` holds the engine's own messages (quit confirmation, save errors…). Their original is already in
  English. Translate them too.
- Dates on save slots: keep `{#file_time}` and the `%` codes (`%d/%m/%Y`, `%A`, `%B`, `%H:%M`). You may reorder them.
- Labels ending in `_prueba` are developer test scenes. They never appear to players, so you can skip them.
- You may delete the `# english:` lines when you finish a block, or leave them. Both are fine.

---

## 3. Tags and variables

Copy these exactly. Translate only the words around them.

| In the text | What it is |
|---|---|
| `[mc]` | The player's name (Futaro by default; players can change it). Never write "Futaro" yourself. |
| `[nombre_jugador]` | Also the player's name, used on places and labels ("[nombre_jugador]'s Room"). |
| `[tiempo_restante!t]`, `[nombre_h!t]`, `[e6_p1!t]`, `[e6_p2!t]` | A value that is translated in its own string. Keep the `!t`. |
| `[n]`, `[config.version!t]` and any other `[…]` | Values filled in by the game. |
| `{}` in an interface string | A slot the game fills in (`"Ending: {}"`). Keep the same number of `{}`. They may move inside the sentence. |
| `{i}…{/i}`, `{b}…{/b}` | Italic, bold. Keep both the opening and the closing tag. |
| `{w}`, `{w=0.5}`, `{nw}` | Pauses inside a line. Keep them in the same position in the sentence. |
| `{color=…}…{/color}`, `{size=…}…{/size}`, `{font=…}…{/font}` | Formatting. Keep them, around the matching words. |
| `{#…}` | A note for translators, never shown. Keep it as it is. |
| `{{` and `[[` | A literal `{` or `[` on screen. Keep them doubled. |
| `—` | A cut-off line ("I didn't mean—"). Keep the dash. |

**Turkish capitals.** Write the dotted capital **İ** yourself wherever it belongs (`İYİ`, `İki`). In English
the value `[tiempo_restante!tc]` uses `!tc` to capitalize its first letter; in Turkish use **`!t`** and write the
capital yourself, or phrase the line so the value does not open the sentence. Some short labels (place names,
section titles, school subjects) are shown in capitals by the game itself: write them normally, in sentence case.

---

## 4. Where to start

**Test file: `01_prologo.rpy` (the Prologue).** Translate it first and send it back. Once it is reviewed,
continue with the rest at your own pace.

Rough sizes in words, largest first: `02_cap1_evento6` (13,000), `02_cap1_conexiones` (8,800),
`02_cap1_beat_casa` (3,900), `01_prologo` (3,800), `02_cap1_final_malo` (3,200), `02_cap1_apertura` (2,200),
the five `02_cap1_<name>` events (about 1,500 each), `02_cap1_beat_Nino` (1,700), `02_cap1_beat_Itsuki` (1,000).
The other files are mostly short interface strings.

When you send files back, send the whole `tl/turkish/` folder as a zip.

---

## 5. Glossary

### 5.1 General style

- Natural Turkish, not a literal translation. Adapt jokes so they work in Turkish instead of translating them word for word.
- Numbers in dialogue: in words when short ("a hundred"); in digits in the interface.
- Sound effects between asterisks (`*Munch...*`): use a Turkish equivalent between asterisks.
- English uses “ ” for quotes inside the text; use whatever Turkish uses, but inside a line write a straight quote as `\"`.

### 5.2 Names

First name + family name (Western order). Almost everyone uses first names only.

| Name | Notes |
|---|---|
| **Futaro Uesugi** | The main character. Always `[mc]` in the text, never written out. |
| **Ichika, Nino, Miku, Yotsuba, Itsuki Nakano** | The quintuplets, from oldest to youngest. |
| **Raiha** | Futaro's little sister. |
| **Isanari** | Futaro's father. |
| **Maruo** | The quintuplets' father. Nobody calls him by name out loud; the name appears on his name tag. |
| **Teacher** | Name tag of the class teacher. The students call him "sir". |
| **New Student** | Itsuki's name tag before she introduces herself. |
| **The Quintuplets** | Name tag when all five speak at once. |
| **???** | Unknown speaker. Keep as is. |
| **Asaba High** | The school. Invented for the game; do not replace it with another school name. |
| **"Nakano."** | The teacher calls any of the five sisters just "Nakano." That is the joke: keep only the surname. |

### 5.3 No honorifics

The game uses **no honorifics at all**: never -kun, -san, -chan, -sama, senpai or sensei. The player can pick any name,
and "[mc]-kun" would look strange with many of them.

| Term | Who says it | How |
|---|---|---|
| `[mc]` / **big brother** | Raiha | `[mc]` when she calls him or gives orders ("[mc]! Dinner!"); "big brother" when she is tender, worried or teasing. Never "Onii-chan". |
| **tutor** | Nino, Yotsuba, Itsuki | How the sisters address Futaro ("Thirty days, tutor."). |
| **sir** | Futaro, the students | To the teacher and to Maruo. |
| **Dad / my father** | Several | "Dad" when talking to or about one's own father casually; "my father" when formal. |

### 5.4 School subjects and exams

Five subjects, one per sister (exam week, Monday to Friday):

| English | Sister | Notes |
|---|---|---|
| **Japanese** | Yotsuba | Japanese language and literature: one single subject. Includes reading comprehension. |
| **Math** | Ichika | |
| **English** | Nino | Her minigame is an English exam: see 5.6. |
| **Science** | Itsuki | |
| **Social Studies** | Miku | History is part of it ("History's your thing."). |

Other terms: subject · syllabus / the material · practice exam · finals / the exams · pass / fail ·
grade / score · top of the class · **report card** (the sheet with the grades; its header is **THE TALLY**).

### 5.5 Recurring terms

Use one translation for each of these and keep it everywhere.

| English | Notes |
|---|---|
| **"Contract"** | Ichika's dragon. A proper name, capitalized. |
| **"Team Quintuplets + Tutor!"** | The group chat's name. Identical in every string. |
| sixth member · free afternoon · tutor's **contract** / **rate** ("five times the going rate") | |
| **AFTERNOON {} OF 3** · **"[tiempo_restante!t] left"** | Map and notebook labels. |
| **ENCOUNTER** · **KEY SCENE** · **DECISION** · **TIME TO DECIDE** | On-screen labels. |
| **ending** · **BAD ENDING** · **Early Dismissal** | "Ichika's Ending". "early dismissal" in lower case inside narration. |
| **warm / lukewarm / cold** | The three ways each sister's event can go (Extras menu). |
| **Rehearsal Room** · **Shopping Mall** · **Library** · **Track** · **Empty Classroom** · **Rooftop** | The five afternoon locations and the rooftop. |
| **Apartment** / **Nakano Apartment** · **The Nakanos' Building** · **Uesugi House** · **[nombre_jugador]'s Room** / **[nombre_jugador]'s House** | Places. Never write "Futaro's House": the player's name can change. |
| curry · aquarium · matcha soda · headphones (Miku) · stopwatch (Yotsuba) | |
| **"hahaha"** | Laughter in the chat. Adapt it to who writes it (dry "haha", or "HAHAHA" when Yotsuba is excited). |
| **Perfect / Good / Early / Late / Miss** | Hit ratings in Miku's rhythm minigame. |
| **Quintuplet Relay** · **The Mask Grows Tired** · **Shopping for Six** · **Conversion Chain** · **The Beat** | Minigame titles. |
| **Try again** · **Skip it** · **Let her do it** | Options after failing a minigame. |

### 5.6 Nino's minigame (English exam)

The products on the shopping list stay **in English** ("honey", "maple syrup"…): they are not in the translation
files. Next to each product the game shows a note with its meaning. In the original that note is in Spanish, so a
Spanish player has to match the English word to its meaning.

In the English version those notes are written in Japanese romaji ("hachimitsu"), because English = English would
leave nothing to match. **In Turkish, write the notes in Turkish** (`old "miel"` → `new "bal"`). Ignore the romaji
`# english:` reference in that file (`10_mj_nino.rpy`).

### 5.7 Lines that repeat

Some lines are quoted again later (Futaro's notebook, callbacks between scenes). Translate each one **the same way
every time** it appears. For example: "Head-on, all five at once, I always lose." · "It links together, you don't
chop it up." · "You won't last a week." · "Battles are won by whoever moves the rice." · "I run and cheer." ·
"As long as it takes." · "Forget what I said." · "I don't have to handle everything." · "Sure, hand it over." ·
"Only time will prove it." The three group-chat messages that Futaro can choose on Saturday are also shown as
chat bubbles: same text in both places.

---

## 6. Character voices

### Futaro: `mc`, `mc_pensamiento` (thoughts, shown on a notebook page) and `narrador` (narration)
- **All three are Futaro.** The narration is first person, past tense ("That's when I saw her.").
- Dry, short, logical. Sentences of 2 to 8 words. No decoration, no jokes out loud, but his irony shows in his
  thoughts ("The details are what ruin the math.").
- Thoughts are notes to himself, sometimes without a verb ("Five notebooks, a syllabus split by subject, and zero expectations.").
- Narration: clean, young-adult novel rhythm, no flourishes.
- No slang, no swearing. Futaro is correct even when he is rude. "I didn't say to do it." · "Fine. Noted."

### Ichika (the oldest)
- An actress. Playful, teases Futaro, always ready with a joke or a theater metaphor (script, role, audition, scene).
- Underneath: tiredness and fear. When the mask slips, her sentences break off and get quieter.
- Light, teasing, stage rhythm. "Well, well…" · "Exclusive offer, just for you, [mc]." · "Actress multitasking!" · "And that's off-script."

### Nino (the second)
- The most hostile to the tutor at first. Sharp, defensive, orders and reproaches. Fiercely protective of her sisters.
  Exclamations and capitals when she explodes.
- Tsundere: she denies what she feels ("Don't think it bothers me."). Calls him **idiot**.
- Sarcastic and cutting, short sentences, no vulgarity. "Thirty days, tutor. Let's see how many of us you find."

### Miku (the third)
- Quiet, flat, and almost every line **starts with "..."**. Very few exclamations.
- Loves history (battles, trade, salt): when she talks about it she opens up and speaks in longer sentences.
- Keep the leading "...": "...Hi." · "...It's my favorite." · "...Correct. ...I checked." Plain words, flat tone.

### Yotsuba (the fourth)
- Pure energy: **double exclamations**, "Tutor!", sports metaphors (race, laps, relay, warming up).
- Optimistic even when it hurts. When she runs out of energy, her sentences get short and lose the "!", and it shows.
- Cheerful and enthusiastic. "Let's go!" · "Full team! Legs and brains!" Capitals only where the English has them.

### Itsuki (the fifth): `itsuki` and `itsuki_inicio` (their first meeting)
- Formal, proud, very proper, with a slightly elevated vocabulary. Loves food (*Munch...*). Argues with Futaro as an equal.
- In `itsuki_inicio` she is more haughty and offended.
- Proper and slightly stiff, no contractions when she gets dignified ("I do not accept food from my tutor."),
  softer when she lowers her guard. "Hardly a dignified look for a tutor."

### Inner voices during the exams (`ichika_int`, `nino_int`, `miku_int`, `yotsuba_int`, `itsuki_int`)
- Each sister's thoughts while taking her exam. Same voice, but barer: present tense, very short sentences, lists
  ("Question four. Trains. Four thirty-five.").
- Miku's inner voice also starts with "...". Itsuki's stays formal.

### Raiha (Futaro's little sister)
- Cheerful, bossy at home, affectionate. Exclamations, questions one after another. Quotes her teacher ("Teacher said so!").
- "[mc]! I made curry." · "Big brother... are you okay?" (see 5.3).

### Isanari (Futaro's father)
- Relaxed, a joker, a bit irresponsible; talks about money with no shame. When he gets serious: short, sincere dad lines.
- Casual, dad-joke energy. "Don't sound so dramatic." · "Five times the rate doesn't fall from the sky twice." · "Pop quiz passed."

### Maruo (the quintuplets' father)
- Cold, precise, very short sentences. Never raises his voice, never jokes. Speaks to Futaro like an employer.
- Clipped and formal, almost never contractions. "Very well." · "I have seen enough." · "I did not ask you to be kind to my daughters."

### The teacher
- Neutral classroom tone, polite with the students. "Nakano. Wake up." · "You may begin."
