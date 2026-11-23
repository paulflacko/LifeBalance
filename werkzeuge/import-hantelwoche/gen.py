#!/usr/bin/env python3
"""Erzeugt inhalt/ aus der Daten-Ausgabe der Hantelwoche (data.json)."""
import json, os, re, sys, shutil, collections

DATA, OUT, SRC = sys.argv[1], sys.argv[2], sys.argv[3]  # data.json, repo root, hantelwoche-v1 root
d = json.load(open(DATA))
EX, TIPS = d['EX'], d['TIPS']
SEQX = d['EXTRA']['SEQX']

OWN_RE = re.compile(r'^(yoga-|aufwaermsaetze|unterarmstuetz|hueft|bws-|brust-dehnung|waden-dehnung|nacken-|schulterkreisen|worlds-greatest-stretch|band-pull-aparts|bird-dog)')

def w(path, text):
    p = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w') as f:
        f.write(text.rstrip() + '\n')

def y(v):
    """YAML-Wert (einfach, sicher gequotet)."""
    if v is None: return 'null'
    if isinstance(v, bool): return 'true' if v else 'false'
    if isinstance(v, (int, float)): return str(v)
    if isinstance(v, list): return '[' + ', '.join(y(x) for x in v) + ']'
    return json.dumps(str(v), ensure_ascii=False)

def front(fields):
    out = ['---']
    for k, v in fields.items():
        if v is None or v == '' or v == []: continue
        out.append(f'{k}: {y(v)}')
    out.append('---')
    return '\n'.join(out)

def fmt_sec(s):
    s = int(s or 0)
    if s >= 60 and s % 60 == 0: return f'{s//60} min'
    if s >= 60: return f'{s//60} min {s%60} s'
    return f'{s} s'

UNIT = {'kg': 'Gewicht und Wiederholungen', 'bw': 'Körpergewicht, Wiederholungen', 'band': 'Band, Wiederholungen',
        'sec': 'Sekunden (Halten)', 'carry': 'Gewicht und Meter'}
IMP = {'lh': 'Langhantel', 'sz': 'SZ-Stange', 'kh': 'eine Kurzhantel', 'kh2': 'zwei Kurzhanteln'}
MOBIL_KEYS = set(d['MOB_POS'].keys()) | {x['ex'] for x in d['YOGA_POOL']}

# ---------- Rückverweise sammeln ----------
used = collections.defaultdict(list)
def use(ex, where):
    if ex and ex in EX and where not in used[ex]: used[ex].append(where)

for t, wo in d['WORKOUTS'].items():
    for it in wo['items']:
        use(it['ex'], f'[{wo["name"]}](../ablaeufe/kraft-{t.lower()}.md)')
        if it.get('alt'): use(it['alt']['ex'], f'[{wo["name"]}](../ablaeufe/kraft-{t.lower()}.md) (Ersatz)')
        if it.get('v'): use(it['v']['ex'], f'[{wo["name"]}](../ablaeufe/kraft-{t.lower()}.md) (Variante)')
for e in d['EXAMPLES']:
    for it in e['items']: use(it['ex'], f'[Vorlage {e["name"]}](../ablaeufe/vorlagen/{e["id"]}.md)')
for k, steps in SEQX.items():
    if isinstance(steps, list):
        for s in steps: use(s.get('ex'), f'[{d["SEQ_TITLE"].get(k,k)}](../ablaeufe/gefuehrt/{k}.md)')
for a in d['MOB_AREAS']:
    for x in a['pool']: use(x['ex'], f'[Mobility nach Gefühl: {a["n"]}](../mobility/koerperbereiche.md)')
for x in d['YOGA_POOL']: use(x['ex'], '[Yoga nach Gefühl](../mobility/yoga-baukasten.md)')
for s in d['SKILLS']:
    for i, lv in enumerate(s['lv']):
        for x in lv['ex']: use(x.get('ex'), f'[Skill {s["n"]}, Stufe {i+1}](../skills/{s["id"]}.md)')

def exlink(k, base='../uebungen/'):
    if k and k in EX: return f'[{EX[k]["n"]}]({base}{k}.md)'
    return ''

# ---------- Medien ----------
fotos_used, anims_used = set(), set()
def media(e):
    ph = e.get('ph') or ''
    anim = e.get('anim') or ''
    foto = ph[5:] + '.webp' if ph.startswith('foto/') else ''
    own = anim + '.gif' if anim and OWN_RE.match(anim) else ''
    wl = anim if anim and not own else ''
    if foto: fotos_used.add(foto)
    if own: anims_used.add(own)
    return foto, own, wl

# ---------- Übungen ----------
cats = d['CATS']; eqk = d['EQK']
ex_index = collections.defaultdict(list)
no_pic = []
for k, e in EX.items():
    foto, own, wl = media(e)
    is_mob = k in MOBIL_KEYS or e.get('cat') == 'mobil'
    art = 'yoga' if (own.startswith('yoga-') or k in {'cobra','seatfold','chair','garland','tree','triangle','butterfly','sun','dog','warrior','lowlunge','pigeon','pyramid','frog','twist','baby','sava','child','seiza'}) else ('mobility' if is_mob else 'kraft')
    if e.get('cat') == 'kondi': art = 'kondition'
    if e.get('cat') == 'core' and art == 'kraft': art = 'core'
    fm = {
        'id': k, 'name': e['n'], 'typ': 'uebung', 'saeule': 'koerper', 'art': art,
        'kategorie': e.get('cat'), 'equipment': e.get('eqk') or [], 'equipment_text': e.get('eq') if e.get('eq') not in ('–', '-') else None,
        'muskeln': e.get('mg'), 'einheit': e.get('unit'), 'steigerung_kg': e.get('step'),
        'hantel': e.get('imp'), 'pro_seite': True if e.get('sd') else None, 'braucht_klimmzugstange': True if e.get('bar') else None,
        'foto': f'../../medien/fotos/{foto}' if foto else None,
        'foto_hinweis': e.get('phn'),
        'animation': f'../../medien/animationen/{own}' if own else None,
        'bild_fehlt': True if not (foto or own) else None,
    }
    if not (foto or own): no_pic.append(k)
    L = [front(fm), '', f'# {e["n"]}', '']
    if foto: L += [f'![{e["n"]}: Start (1) und Ende (2)](../../medien/fotos/{foto})', '']
    if own: L += [f'![{e["n"]}: Animation](../../medien/animationen/{own})', '']
    if e.get('phn'): L += [f'*Hinweis zum Foto: {e["phn"]}.*', '']
    L += [f'> {e["cue"]}', '']
    info = [f'- **Muskeln/Bereich:** {e["mg"]}' if e.get('mg') else None,
            f'- **Equipment:** ' + ', '.join(eqk.get(x, x) for x in e.get('eqk') or []) if e.get('eqk') else None,
            f'- **Kategorie:** {cats.get(e.get("cat"), e.get("cat"))}' if e.get('cat') else None,
            f'- **Erfassung:** {UNIT.get(e["unit"], e["unit"])}' + (f', Steigerung {e["step"]} kg' if e.get('step') else '') if e.get('unit') else None,
            f'- **Hantel:** {IMP[e["imp"]]}' if e.get('imp') in IMP else None,
            '- **Pro Seite** ausführen' if e.get('sd') else None,
            '- **Braucht die Klimmzugstange**' if e.get('bar') else None]
    L += [x for x in info if x] + ['']
    t = TIPS.get(k)
    if t:
        L += ['## Ausführung', ''] + [f'- {x}' for x in t.get('a', [])] + ['']
        L += ['## Häufige Fehler', ''] + [f'- {x}' for x in t.get('f', [])] + ['']
        if t.get('b'): L += ['## Atmung', '', t['b'], '']
        if t.get('s'): L += ['## Wo du es spürst', '', t['s'], '']
    if used.get(k):
        L += ['## Kommt vor in', ''] + [f'- {u}' for u in used[k]] + ['']
    if wl and not foto and not own:
        L += ['*In der Hantelwoche gab es hierfür nur eine nicht frei lizenzierte Zeichnung, die hier bewusst fehlt. Bild noch offen.*', '']
    w(f'inhalt/uebungen/{k}.md', '\n'.join(L))
    ex_index[art].append(k)

ART_N = {'kraft': 'Kraft', 'core': 'Core', 'kondition': 'Kondition', 'mobility': 'Mobility und Dehnen', 'yoga': 'Yoga-Haltungen'}
L = ['# Übungen', '', f'{len(EX)} Übungen aus der Hantelwoche, eine Datei pro Übung. Der Dateiname ist die feste ID, auf die Abläufe, Skills und Vorlagen verweisen.', '',
     f'Mit Foto: {sum(1 for e in EX.values() if (e.get("ph") or "").startswith("foto/"))} · mit eigener Animation: {sum(1 for e in EX.values() if e.get("anim") and OWN_RE.match(e["anim"]))} · noch ohne freies Bild: {len(no_pic)}', '']
for art in ['kraft', 'core', 'kondition', 'mobility', 'yoga']:
    ks = sorted(ex_index[art], key=lambda k: EX[k]['n'].lower())
    L += [f'## {ART_N[art]} ({len(ks)})', '', '| Übung | Kategorie | Equipment | Bild |', '|---|---|---|---|']
    for k in ks:
        e = EX[k]; f, o, _ = media(e)
        L.append(f'| [{e["n"]}]({k}.md) | {cats.get(e.get("cat"), "")} | {", ".join(eqk.get(x,x) for x in e.get("eqk") or [])} | {"Foto" if f else ""}{" + " if f and o else ""}{"Animation" if o else ""}{"–" if not (f or o) else ""} |')
    L.append('')
w('inhalt/uebungen/README.md', '\n'.join(L))

# ---------- Atemübungen ----------
BR_GOAL, BR_EV, BR_KIND, BR_USE = d['BR_GOAL'], d['BR_EV'], d['BR_KIND'], d['BR_USE']
goal_saeule = {'ruhe': 'erholung', 'fokus': 'geist', 'energie': 'koerper'}
uses_of = collections.defaultdict(list)
for uk, u in BR_USE.items():
    for i in u['ids']: uses_of[i].append(uk)
for b in d['BR']:
    fm = {'id': b['id'], 'name': b['n'], 'typ': 'atemuebung', 'saeule': 'erholung', 'ziel': b['goal'],
          'evidenz': b['ev'], 'einsatz': uses_of.get(b['id'], []), 'dauer_standard': b.get('len'), 'dauer_optionen': b.get('lens'),
          'dauer_einheit': b.get('unit'), 'sicherheitshinweis': True if b.get('warn') else None}
    L = [front(fm), '', f'# {b["n"]}', '', f'*{b["sub"]}*', '', f'> {b["tag"]}', '',
         f'- **Ziel:** {BR_GOAL.get(b["goal"])}', f'- **Belege:** {BR_EV[b["ev"]]["n"]}',
         f'- **Gut für:** ' + ', '.join(BR_USE[u]['n'] for u in uses_of.get(b['id'], [])) if uses_of.get(b['id']) else None, '']
    L = [x for x in L if x is not None]
    if b.get('warn'): L += [f'> **Achtung:** {b["warn"]}', '']
    L += ['## Wann', '', b['when'], '', '## So geht es', ''] + [f'{i+1}. {s}' for i, s in enumerate(b['how'])] + ['']
    L += ['## Varianten und Rhythmus', '']
    for v in b['vars']:
        if v.get('pat'):
            L.append(f'- **{v["n"]}:** ' + ' → '.join(f'{BR_KIND.get(p["k"], p["k"])} {p["s"]} s' + (f' ({p["h"]})' if p.get('h') else '') for p in v['pat']))
        elif v.get('b'):
            L.append(f'- **{v["n"]}:** {v["b"]} kräftige Atemzüge pro Runde, dann Luft anhalten nach Gefühl (Tipp beendet), 15 s Erholungsatem.')
        else:
            L.append(f'- **{v["n"]}**')
    L += ['', '## Wirkung', '', b['eff'], '', '## Quellen', ''] + [f'- {s}' for s in b['src']]
    w(f'inhalt/atmung/{b["id"]}.md', '\n'.join(L))
L = ['# Atemübungen', '', f'{len(d["BR"])} Techniken. Der Atem-Player (siehe [Abläufe und Logik](../../docs/06-logik.md)) spielt die Rhythmen aus „Varianten und Rhythmus“ ab.', '',
     '| Technik | Ziel | Belege |', '|---|---|---|']
L += [f'| [{b["n"]}]({b["id"]}.md) | {BR_GOAL[b["goal"]]} | {BR_EV[b["ev"]]["n"]} |' for b in d['BR']]
L += ['', '## Nach Einsatzzweck', ''] + [f'- **{u["n"]}:** ' + ', '.join(f'[{next(b["n"] for b in d["BR"] if b["id"]==i)}]({i}.md)' for i in u['ids']) for u in BR_USE.values()]
L += ['', '## Phasen im Rhythmus', ''] + [f'- `{k}`: {v}' for k, v in BR_KIND.items()]
w('inhalt/atmung/README.md', '\n'.join(L))

# ---------- Selbsthilfe ----------
PK, PU, PE = d['PSY_KAT'], d['PSY_USE'], d['PSY_EV']
help_txt = re.sub(r'<[^>]+>', '', d['PSY_HELP']).strip()
FT = {'text': 'Text, einzeilig', 'area': 'Text, mehrzeilig', 'num': 'Zahl'}
for p in d['PSY']:
    fm = {'id': p['id'], 'name': p['n'], 'typ': 'selbsthilfe', 'saeule': 'geist', 'methode': p['kat'], 'einsatz': p['use'],
          'dauer_min': p['min'], 'evidenz': p['ev'], 'hat_formular': True if p.get('form') else None}
    L = [front(fm), '', f'# {p["n"]}', '', f'> {p["kurz"]}', '',
         f'- **Methode:** {PK[p["kat"]]}', f'- **Hilft bei:** ' + ', '.join(PU[u]['n'] for u in p['use']),
         f'- **Dauer:** ca. {p["min"]} min', f'- **Belege:** {PE[p["ev"]]["n"]}', '',
         '## Warum es hilft', '', p['why'], '', '## Ablauf', '', '| Schritt | Zeit |', '|---|---|']
    L += [f'| {s["t"]} | {fmt_sec(s["s"]) if s.get("s") else "–"} |' for s in p['steps']]
    if p.get('form'):
        L += ['', '## Eintrag danach', '', 'Nach der Übung kann man festhalten:', ''] + [f'- **{f["l"]}** ({FT.get(f["type"], f["type"])})' for f in p['form']]
    if p.get('safe'): L += ['', f'> **Achtung:** {p["safe"]}']
    L += ['', '## Quelle', '', p['src'], '', '---', '', f'*{help_txt}*']
    w(f'inhalt/selbsthilfe/{p["id"]}.md', '\n'.join(L))
L = ['# Kopf und Gefühle: Selbsthilfe-Übungen', '', f'{len(d["PSY"])} Übungen, alle in eigenen Worten beschrieben. Quellen siehe [LIZENZEN.md](../../LIZENZEN.md).', '', f'> {help_txt}', '',
     '| Übung | Methode | Hilft bei | Dauer |', '|---|---|---|---|']
L += [f'| [{p["n"]}]({p["id"]}.md) | {PK[p["kat"]]} | {", ".join(PU[u]["n"] for u in p["use"])} | {p["min"]} min |' for p in d['PSY']]
L += ['', '## Nach Anliegen', ''] + [f'- **{u["n"]}** ({u["d"]}): ' + ', '.join(f'[{p["n"]}]({p["id"]}.md)' for p in d['PSY'] if uk in p['use']) for uk, u in PU.items()]
w('inhalt/selbsthilfe/README.md', '\n'.join(L))

# ---------- Skills ----------
SK_CAT, SK_LOAD = d['SK_CAT'], d['SK_LOAD']
TEST = {'reps': 'Wiederholungen', 'hold': 'Sekunden halten', 'kgbw': '× Körpergewicht', 'kg': 'kg', 'cm': 'cm', 'sess': 'Einheiten', 'book': 'Bücher'}
br_names = {b['id']: b['n'] for b in d['BR']}
for s in d['SKILLS']:
    fm = {'id': s['id'], 'name': s['n'], 'typ': 'skill', 'saeule': 'wachstum', 'bereich': s['cat'], 'belastung': s['load'],
          'koerperbereich': s['area'], 'stufen': len(s['lv']), 'misst_automatisch': s.get('kind')}
    L = [front(fm), '', f'# {s["n"]}', '', s['intro'], '', f'- **Bereich:** {SK_CAT[s["cat"]]}', f'- **Belastung:** {SK_LOAD[str(s["load"])]}', f'- **Fordert:** {s["area"]}']
    if s.get('req'): L.append(f'- **Voraussetzung:** {s["req"]}')
    L += ['', '## Stufen', '']
    for i, lv in enumerate(s['lv']):
        t = lv['test']; tt = f'{t.get("target")} {TEST.get(t["type"], t["type"])}' + (f', je mindestens {t["min"]} min' if t.get('min') else '')
        L += [f'### Stufe {i+1}: {lv["n"]}', '', f'**Ziel:** {lv["goal"]}  ', f'**Test:** {tt}', '']
        if s.get('runs') and i < len(s['runs']):
            r = s['runs'][i]; L += [f'*Geführt mit: [{br_names.get(r[0], r[0])}](../atmung/{r[0]}.md), {r[2]} min*', '']
        for x in lv['ex']:
            L.append(f'- {exlink(x.get("ex")) or x["n"]}{"" if not exlink(x.get("ex")) or EX[x["ex"]]["n"]==x["n"] else " (" + x["n"] + ")"}: {x["d"]}')
        L += ['', f'> {lv["cue"]}', '']
    L += ['## Technik', ''] + [f'- {x}' for x in s['tech']] + ['', '## Häufige Fehler', ''] + [f'- {x}' for x in s['err']]
    L += ['', '## Hilfsübungen', '', '| Übung | Umfang | Wozu |', '|---|---|---|'] + [f'| {a} | {b} | {c} |' for a, b, c in s['drills']]
    L += ['', '## Einbau in die Woche', ''] + [f'- {x}' for x in s['plan']] + ['', '## Sicherheit', ''] + [f'- {x}' for x in s['safe']]
    w(f'inhalt/skills/{s["id"]}.md', '\n'.join(L))
L = ['# Skillbank', '', f'{len(d["SKILLS"])} Skills mit Stufenpfad. Jede Stufe hat ein Ziel, einen Test und passende Übungen. In 2.0 ist ein Skill ein [Ziel](../../docs/04-bausteine.md#ziel) vom Typ Stufenpfad.', '']
for c, cn in SK_CAT.items():
    L += [f'## {cn}', '', '| Skill | Stufen | Belastung |', '|---|---|---|'] + [f'| [{s["n"]}]({s["id"]}.md) | {len(s["lv"])} | {SK_LOAD[str(s["load"])]} |' for s in d['SKILLS'] if s['cat'] == c] + ['']
w('inhalt/skills/README.md', '\n'.join(L))

# ---------- Abläufe ----------
def item_line(it):
    r = it.get('r') or []
    reps = it.get('lab') or (f'{r[0]}–{r[1]}' if len(r) == 2 and r[0] != r[1] else (str(r[0]) if r else ''))
    unit = EX.get(it['ex'], {}).get('unit')
    reps += ' s' if unit == 'sec' else (' m' if unit == 'carry' else ' Wdh.')
    return f'{it["sets"]} × {reps}' + (' pro Seite' if it.get('side') else '') + (f', Pause {fmt_sec(it["rest"])}' if it.get('rest') else '')

for t, wo in d['WORKOUTS'].items():
    fm = {'id': f'kraft-{t.lower()}', 'name': wo['name'], 'typ': 'ablauf', 'art': 'krafttraining', 'saeule': 'koerper', 'modus': 'saetze', 'mit_einstieg': True}
    L = [front(fm), '', f'# {wo["name"]}', '', wo['sub'], '', 'Vor dem Training: [Einstieg](gefuehrt/warmup.md). Sätze enden bei RIR 2 (noch etwa 2 saubere Wiederholungen möglich). Gleiche Nummer mit a/b = im Wechsel (Supersatz).', '',
         '| Nr. | Übung | Sätze × Wdh. | Hinweis |', '|---|---|---|---|']
    for it in wo['items']:
        note = it.get('wt', '')
        if it.get('alt'): note += (' ' if note else '') + f'Ohne Klimmzugstange: {exlink(it["alt"]["ex"])} {item_line({**it, **it["alt"]})}.'
        if it.get('v'): note += (' ' if note else '') + f'In geraden Wochen: {exlink(it["v"]["ex"])}.'
        L.append(f'| {it["g"]} | {exlink(it["ex"])} | {item_line(it)} | {note} |')
    w(f'inhalt/ablaeufe/kraft-{t.lower()}.md', '\n'.join(L))

for e in d['EXAMPLES']:
    fm = {'id': e['id'], 'name': e['name'], 'typ': 'ablauf', 'art': d['TPL_CLS'][e['cls']], 'saeule': 'koerper',
          'modus': 'runden' if e['mode'] == 'timer' else 'saetze', 'mit_einstieg': e.get('warm'),
          'runden': e.get('rounds'), 'arbeit_s': e.get('work'), 'pause_s': e.get('rest'), 'rundenpause_s': e.get('rrest')}
    L = [front(fm), '', f'# {e["name"]}', '', e['note'], '']
    if e['mode'] == 'timer':
        L += [f'**Zirkel:** {e.get("rounds")} Runden, {e.get("work")} s Arbeit, {e.get("rest")} s Pause, {e.get("rrest")} s Pause zwischen den Runden.', '', '| Übung |', '|---|'] + [f'| {exlink(it["ex"], '../../uebungen/')} |' for it in e['items']]
    else:
        L += ['| Übung | Sätze × Wdh. | Supersatz mit nächster |', '|---|---|---|'] + [f'| {exlink(it["ex"], '../../uebungen/')} | {item_line(it)} | {"ja" if it.get("ss") else ""} |' for it in e['items']]
    w(f'inhalt/ablaeufe/vorlagen/{e["id"]}.md', '\n'.join(L))

SEQ_NOTE = {'circuit': 'Arbeitszeit einstellbar (40 oder 45 s pro Minute), hier mit 40 s.', 'med': 'Dauer wächst mit dem Plan: Woche 1–2 5 min, danach 10 min. Hier mit 10 min.', 'z2': 'Woche 1–4 30 min, ab Woche 5 40 min.'}
for k, steps in SEQX.items():
    fm = {'id': k, 'name': d['SEQ_TITLE'][k], 'typ': 'ablauf', 'art': 'gefuehrt', 'saeule': 'geist' if k == 'med' else 'koerper', 'schritte': len(steps), 'dauer_s': sum(s.get('sec') or 0 for s in steps)}
    L = [front(fm), '', f'# {d["SEQ_TITLE"][k]}', '', f'Geführter Ablauf mit Timer, gesamt ca. {round(fm["dauer_s"]/60)} min.' + (' ' + SEQ_NOTE[k] if k in SEQ_NOTE else ''), '',
         '| # | Schritt | Dauer | Übung | Hinweis |', '|---|---|---|---|---|']
    for i, s in enumerate(steps):
        L.append(f'| {i+1} | {s["n"]}{" *(Pause)*" if s.get("kind")=="rest" else ""} | {fmt_sec(s["sec"]) if s.get("sec") else "bis Weiter"} | {exlink(s.get("ex"), '../../uebungen/') if s.get("ex") else ""} | {s.get("note") or ""} |')
    w(f'inhalt/ablaeufe/gefuehrt/{k}.md', '\n'.join(L))

L = ['# Abläufe', '', 'Alles, was man starten kann. In 2.0 ist jeder dieser Einträge ein [Ablauf](../../docs/04-bausteine.md#ablauf).', '',
     '## Krafttraining aus dem Wochenplan', ''] + [f'- [{wo["name"]}](kraft-{t.lower()}.md): {wo["sub"]}' for t, wo in d['WORKOUTS'].items()]
L += ['', '## Vorlagen', ''] + [f'- [{e["name"]}](vorlagen/{e["id"]}.md) ({d["TPL_CLS"][e["cls"]]}): {e["note"]}' for e in d['EXAMPLES']]
L += ['', '## Geführte Abläufe', ''] + [f'- [{d["SEQ_TITLE"][k]}](gefuehrt/{k}.md)' for k in SEQX]
L += ['', '## Nach Gefühl zusammengestellt', '', '- [Mobility nach Gefühl](../mobility/koerperbereiche.md)', '- [Yoga nach Gefühl](../mobility/yoga-baukasten.md)']
w('inhalt/ablaeufe/README.md', '\n'.join(L))

# ---------- Mobility ----------
L = ['---', 'typ: baukasten', 'saeule: koerper', '---', '', '# Mobility nach Gefühl: Körperbereiche', '',
     'Man wählt Bereiche (Gewicht 1 oder 2), ein Gefühl und eine Dauer. Die App stellt daraus einen Ablauf zusammen (Logik in [docs/06-logik.md](../../docs/06-logik.md#mobility-nach-gefühl)).', '',
     '## Gefühl', '', '| Gefühl | Wirkung | Haltezeit-Faktor |', '|---|---|---|']
L += [f'| {v["n"]} | {v["d"]}{" · " + v["tip"] if v.get("tip") else ""} | {v["hold"]} |' for v in d['MOB_FEEL'].values()]
L += ['', '## Bereiche und ihre Übungen', '']
for a in d['MOB_AREAS']:
    L += [f'### {a["n"]} (`{a["k"]}`)', '', '| Übung | Zeit | Hinweis |', '|---|---|---|']
    L += [f'| {exlink(x["ex"])} | {fmt_sec(x["sec"])}{" pro Seite" if x.get("side") else ""}{", bewegt" if x.get("dyn") else ""} | {x.get("note","")} |' for x in a['pool']]
    L.append('')
L += ['## Position der Übungen', '', 'Für eine sinnvolle Reihenfolge (erst stehen, dann Boden, zuletzt liegen): 0 stehend, 1 Ausfallschritt, 2 Vierfüßler, 3 sitzend/kniend, 4 liegend.', '',
      '| Übung | Position |','|---|---|'] + [f'| {exlink(k)} | {v} |' for k, v in d['MOB_POS'].items() if k in EX]
L += ['', '## Belastung aus dem Training', '', 'Welche Bereiche nach welchen Muskeln Regeneration brauchen (Stichwort aus „Muskeln“ → Bereich mit Gewicht):', '']
PATS=['unterer rücken','nacken, trapez','brust','schulter, rotatoren','trizeps, bizeps, arme, unterarm, griff','rücken, lat (nicht „unterer“)','po','beinbeuger, rückseite','oberschenkel innen, adduktor','oberschenkel, beine','waden, schienbein','hüft…','core','ganzkörper, kondition, schnellkraft']
AREA={a['k']:a['s'] for a in d['MOB_AREAS']}
L += ['| Stichwort in „Muskeln“ | Belastete Bereiche (Gewicht) |','|---|---|']
for pat, (_, m) in zip(PATS, d['LOAD_MAP']):
    L.append(f'| {pat} | ' + ', '.join(f'{AREA.get(a,a)} {v}' for a, v in m.items()) + ' |')
w('inhalt/mobility/koerperbereiche.md', '\n'.join(L))

L = ['---', 'typ: baukasten', 'saeule: koerper', '---', '', '# Yoga nach Gefühl: Baukasten', '', 'Haltungen, aus denen „Yoga nach Gefühl“ (Dienstag) zusammengestellt wird.', '',
     '## Stile', ''] + [f'- **{v["n"]}:** {v["d"]}' for v in d['YOGA_STYLE'].values()]
L += ['', '## Intensität', ''] + [f'- **{v["n"]}:** Zeiten × {v["f"]}' for v in d['YOGA_INT'].values()]
L += ['', '## Haltungen', '', '| Haltung | Zeit | Aktivität | Bereiche | Hinweis |', '|---|---|---|---|---|']
L += [f'| {exlink(x["ex"])} | {fmt_sec(x["sec"])}{" pro Seite" if x.get("side") else ""} | {["ruhig","mittel","kräftig"][x.get("act",0)]} | {", ".join(x.get("r") or [])} | {x.get("note","")} |' for x in d['YOGA_POOL']]
w('inhalt/mobility/yoga-baukasten.md', '\n'.join(L))

# ---------- Wochenplan ----------
order = [1, 2, 3, 4, 5, 6, 0]
L = ['---', 'typ: wochenvorlage', 'name: "Hantelwoche Standardwoche"', '---', '', '# Wochenvorlage', '', 'Die bisherige Standardwoche: drei Krafttage (Mo, Mi, Fr), aktive Erholung dazwischen, jeden Abend Meditation.', '']
for i in order:
    day = d['DAYS'][i]
    L += [f'## {day["name"]}: {day["title"]}', '', '| Zeit | Block | Details | Startet |', '|---|---|---|---|']
    for b in day['blocks']:
        start = ''
        if b.get('train'): start = f'[{d["WORKOUTS"][b["train"]]["name"]}](../ablaeufe/kraft-{b["train"].lower()}.md)'
        elif b.get('pick'): start = ('[Yoga nach Gefühl](../mobility/yoga-baukasten.md) oder ' if b.get('key') == 'yoga' else '[Mobility nach Gefühl](../mobility/koerperbereiche.md) oder ') + f'[{b.get("seqLabel")}](../ablaeufe/gefuehrt/{b["seq"]}.md)'
        elif b.get('seq') and b['seq'] in SEQX: start = f'[{d["SEQ_TITLE"][b["seq"]]}](../ablaeufe/gefuehrt/{b["seq"]}.md)'
        elif b.get('go'): start = f'Ansicht „{b["go"]}“'
        L.append(f'| {b["t"]} | {"**" + b["n"] + "**" if b.get("main") else b["n"]} | {b.get("d","")} | {start} |')
    L.append('')
w('inhalt/wochenplan/standardwoche.md', '\n'.join(L))

# ---------- Ernährung ----------
tk = sum(m['kcal'] for m in d['MEALS']); tp = sum(m['p'] for m in d['MEALS'])
L = ['---', 'typ: beispieltag', 'saeule: ernaehrung', f'kcal: {tk}', f'eiweiss_g: {tp}', '---', '', '# Beispieltag Ernährung', '',
     'Vegetarisch geprägt (kein Fisch, kaum Fleisch), Ziel Muskel- und Gewichtsaufbau.', '', '| Zeit | Mahlzeit | Zutaten | kcal | Eiweiß |', '|---|---|---|---|---|']
L += [f'| {m["t"]} | {m["n"]} | {m["d"]} | {m["kcal"]} | {m["p"]} g |' for m in d['MEALS']]
L += [f'| | **Summe** | | **{tk}** | **{tp} g** |', '', '## Schnelle Ergänzungen', '', '| Snack | Inhalt | kcal | Eiweiß |', '|---|---|---|---|']
L += [f'| {q["n"]} | {q.get("d","")} | {q["kcal"]} | {q["p"]} g |' for q in d['QUICK']]
w('inhalt/ernaehrung/beispieltag.md', '\n'.join(L))
L = ['---', 'typ: supplementplan', 'saeule: ernaehrung', '---', '', '# Supplements', '', '| Zeit | Supplement | Hinweis | Optional |', '|---|---|---|---|']
L += [f'| {s["t"]} | {s["n"]} | {s["d"]} | {"ja, in den Einstellungen" if s.get("opt") else ""} |' for s in d['SUPPS']]
L += ['', 'Whey steckt im Quark-Müsli, Isoclear gibt es auf der Arbeit (siehe [Beispieltag](beispieltag.md)).']
w('inhalt/ernaehrung/supplements.md', '\n'.join(L))

# ---------- Check-in ----------
CQ = d['CK_Q']
L = ['---', 'id: tagesampel', 'typ: check-in-skript', 'saeule: erholung', 'zeitpunkt: morgens', '---', '', '# Check-in-Skript: Tagesampel', '',
     'Morgendlicher Check-in mit Verzweigungen. Ergebnis: Punktzahl 0–100 und Ampel. Die Auswertung steht in [docs/06-logik.md](../../docs/06-logik.md#tagesampel).', '',
     '## Ablauf', '', '```mermaid', 'flowchart TD', '  rec[Wie erholt?] -->|1-2| cause[Woran liegt es?]', '  rec -->|3-5| sleep', '  cause -->|krank| sick[Wo sitzen die Beschwerden?]',
     '  cause -->|sonst| sleep[Schlaf und Ruhepuls, optional]', '  sick --> sleep', '  sleep --> sore[Muskelkater oder Schmerzen?]', '  sore -->|1-3| areas[Wo spürst du es?]',
     '  sore -->|0| stress', '  areas -->|Schmerz anders| pain[Stärker bei Belastung?]', '  areas -->|sonst| stress', '  pain --> stress[Stress?]', '  stress --> motiv[Lust auf Bewegung?]', '  motiv --> result[Ergebnis: Ampel]', '```', '', '## Fragen', '']
for k, q in CQ.items():
    L += [f'### `{k}`: {q["q"]}', '']
    if q.get('sub'): L += [f'*{q["sub"]}*', '']
    if q.get('opts'): L += [f'- `{o[0]}` {o[1]}' for o in q['opts']] + ['']
    elif k == 'areas': L += ['Körperbereiche aus [Mobility](../mobility/koerperbereiche.md) plus Oberschenkel vorne, Knie, Arme und Ellbogen, Handgelenke.', '']
    elif k == 'sleep': L += ['- Schlaf in Stunden (Zahl)', '- Ruhepuls (Zahl)', '']
L += ['## Ampel', ''] + [f'- **{v["n"]}:** {v["t"]}' for v in d['CK_LIGHT'].values()]
L += ['', 'Bei Gelb kann man „leichte Variante“ wählen: 2/3 der Sätze mit 90 % des Gewichts.']
w('inhalt/check-ins/tagesampel.md', '\n'.join(L))

# ---------- Verzeichnisse ----------
L = ['# Verzeichnisse', '', 'Feste Schlüssel, die in den Kopfzeilen (Frontmatter) der Inhalte vorkommen.', '',
     '## Säulen (`saeule`)', '', '- `koerper` Körper', '- `erholung` Erholung', '- `ernaehrung` Ernährung', '- `geist` Geist', '- `wachstum` Wachstum', '',
     '## Übungs-Kategorie (`kategorie`)', ''] + [f'- `{k}` {v}' for k, v in cats.items()]
L += ['', '## Equipment (`equipment`)', ''] + [f'- `{k}` {v}' for k, v in eqk.items()]
L += ['', '## Hantel (`hantel`)', ''] + [f'- `{k}` {v}' for k, v in IMP.items()]
L += ['', '## Erfassung (`einheit`)', ''] + [f'- `{k}` {v}' for k, v in UNIT.items()]
L += ['', '## Skill-Bereich (`bereich`)', ''] + [f'- `{k}` {v}' for k, v in SK_CAT.items()]
L += ['', '## Selbsthilfe-Methode (`methode`)', ''] + [f'- `{k}` {v}' for k, v in PK.items()]
L += ['', '## Selbsthilfe-Anliegen (`einsatz`)', ''] + [f'- `{k}` {v["n"]}: {v["d"]}' for k, v in PU.items()]
L += ['', '## Atem-Ziel (`ziel`)', ''] + [f'- `{k}` {v}' for k, v in BR_GOAL.items()]
L += ['', '## Atem-Einsatz (`einsatz`)', ''] + [f'- `{k}` {v["n"]}' for k, v in BR_USE.items()]
L += ['', '## Belege (`evidenz`)', ''] + [f'- `{k}` {v["n"]}' for k, v in BR_EV.items()]
w('inhalt/verzeichnisse.md', '\n'.join(L))

# ---------- Medien kopieren ----------
for f in sorted(fotos_used):
    os.makedirs(f'{OUT}/medien/fotos', exist_ok=True); shutil.copy2(f'{SRC}/img/foto/{f}', f'{OUT}/medien/fotos/{f}')
for f in sorted(os.listdir(f'{SRC}/img')):
    if OWN_RE.match(f):
        os.makedirs(f'{OUT}/medien/animationen', exist_ok=True); shutil.copy2(f'{SRC}/img/{f}', f'{OUT}/medien/animationen/{f}')
extra_fotos = sorted(set(os.listdir(f'{SRC}/img/foto')) - fotos_used)
for f in extra_fotos: shutil.copy2(f'{SRC}/img/foto/{f}', f'{OUT}/medien/fotos/{f}')

print('uebungen', len(EX), 'ohne bild', len(no_pic), 'fotos', len(fotos_used), 'extra', extra_fotos, 'anim', len(os.listdir(f'{OUT}/medien/animationen')))
print('ohne bild:', ', '.join(EX[k]['n'] for k in no_pic))
json.dump({'no_pic': no_pic, 'counts': {a: len(v) for a, v in ex_index.items()}}, open(os.path.join(os.path.dirname(DATA), 'stats.json'), 'w'))
