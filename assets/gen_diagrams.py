#!/usr/bin/env python3
"""Reproduzierbarer Generator der README-Diagramme (priframe-Stil, dunkel, enterprise).
Eine Quelle -> 3 SVGs. Danach via rsvg-convert zu PNG rastern.
Palette an das vorhandene Profil-Banner angelehnt (0b0f14 / 141820 / 2b3440 / 5f9bb0)."""
import html

# ---- Palette (gedämpft, enterprise) ----
BG     = "#0b0f14"
PANEL  = "#141820"
PANEL2 = "#1b2129"
LINE   = "#2b3440"
TEXT   = "#e6ebf0"
DIM    = "#8a94a3"
TEAL   = "#5f9bb0"   # Sonnet / Akzent
TEAL2  = "#38617a"
GOLD   = "#b08d57"   # Opus (denkt)
GREEN  = "#6b8f71"   # Haiku (sucht)
VIOLET = "#8f7fb0"   # QC / Härten

MONO = "JetBrains Mono, ui-monospace, monospace"
SANS = "DejaVu Sans, system-ui, sans-serif"

def esc(s): return html.escape(str(s), quote=True)

class SVG:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.e = []
    def rect(self, x, y, w, h, fill=PANEL, stroke=LINE, sw=1.5, rx=9, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.e.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
                      f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
    def line(self, x1, y1, x2, y2, stroke=LINE, sw=1.5, dash=None, marker=True):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        m = ' marker-end="url(#arr)"' if marker else ""
        self.e.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                      f'stroke="{stroke}" stroke-width="{sw}"{d}{m}/>')
    def path(self, d, stroke=LINE, sw=1.5, marker=True, dash=None):
        mk = ' marker-end="url(#arr)"' if marker else ""
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.e.append(f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}"{mk}{da}/>')
    def text(self, x, y, s, size=14, fill=TEXT, weight="400", family=SANS, anchor="start", ls="0"):
        self.e.append(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
                      f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
                      f'letter-spacing="{ls}">{esc(s)}</text>')
    def chip(self, x, y, label, color):
        w = 16 + len(label) * 7.3
        self.rect(x, y, w, 22, fill=BG, stroke=color, sw=1.3, rx=11)
        self.text(x + w/2, y + 15, label, size=11.5, fill=color, family=MONO, weight="600", anchor="middle")
        return w
    def render(self):
        defs = (f'<defs><marker id="arr" markerWidth="9" markerHeight="9" refX="7" refY="3" '
                f'orient="auto" markerUnits="userSpaceOnUse">'
                f'<path d="M0,0 L7,3 L0,6 Z" fill="{DIM}"/></marker></defs>')
        body = "\n".join(self.e)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
                f'width="{self.w}" height="{self.h}" font-family="{SANS}">\n{defs}\n'
                f'<rect width="{self.w}" height="{self.h}" fill="{BG}"/>\n{body}\n</svg>\n')

def panel_title(s, x, y):
    return s  # helper placeholder

# ============================================================
# A — ORCHESTRIERUNGS-MASCHINE
# ============================================================
def diagram_orchestration():
    W, H = 1200, 820
    s = SVG(W, H)
    s.text(40, 46, "DIE ORCHESTRIERUNGS-MASCHINE", size=20, fill=TEXT, weight="700", family=MONO, ls="1.5")
    s.text(40, 70, "ein Dirigent, viele Spezialisten — jedes Ergebnis geprüft, bevor es „fertig“ heißt",
           size=13.5, fill=DIM)

    # Showrunner panel
    sx, sy, sw, sh = 300, 96, 600, 70
    s.rect(sx, sy, sw, sh, fill=PANEL2, stroke=GOLD, sw=2)
    s.text(sx+sw/2, sy+30, "SHOWRUNNER / EXECUTIVE PRODUCER", size=15, fill=TEXT, weight="700", family=MONO, anchor="middle")
    s.text(sx+sw/2, sy+52, "zerlegt · weist zu · verkettet · härtet · verantwortet das Ganze", size=12.5, fill=DIM, anchor="middle")
    s.chip(sx+sw-96, sy+8, "Opus · denkt", GOLD)

    # 4-phase loop
    ly = 210
    phases = ["ZERLEGEN", "ZUWEISEN", "PARALLEL", "HÄRTEN"]
    pw, gap = 200, 48
    total = len(phases)*pw + (len(phases)-1)*gap
    startx = (W-total)/2
    boxes = []
    for i, p in enumerate(phases):
        x = startx + i*(pw+gap)
        col = VIOLET if p == "HÄRTEN" else TEAL
        s.rect(x, ly, pw, 54, fill=PANEL, stroke=col, sw=1.6)
        s.text(x+pw/2, ly+26, p, size=15, fill=TEXT, weight="600", family=MONO, anchor="middle")
        num = ["1","2","3","4"][i]
        s.text(x+14, ly+26, num, size=13, fill=col, family=MONO, weight="700")
        boxes.append((x, x+pw))
        if i>0:
            s.line(boxes[i-1][1], ly+27, x, ly+27, stroke=DIM, sw=1.6)
    # phase subtitles
    subs = ["in Teilaufgaben","Spezialist je Teil","unabhängige parallel","adversarial prüfen"]
    for i,(x0,x1) in enumerate(boxes):
        s.text((x0+x1)/2, ly+72, subs[i], size=11, fill=DIM, anchor="middle", family=MONO)
    # connector Showrunner -> loop
    s.line(W/2, sy+sh, W/2, ly, stroke=DIM, sw=1.6)
    # loop-back arrow HÄRTEN -> ZERLEGEN
    hx = boxes[-1][1]; zx = boxes[0][0]
    s.path(f"M {hx-pw/2} {ly+90} C {hx-pw/2} {ly+130}, {zx+pw/2} {ly+130}, {zx+pw/2} {ly+90}",
           stroke=VIOLET, sw=1.6, dash="5 4")
    s.text(W/2, ly+154, "Schleife bis alle Teile bestehen", size=11, fill=VIOLET, anchor="middle", family=MONO)
    # Nachlauf-Hinweis statt Stummel-Pfeil
    s.text(hx, ly-14, "→ LIVE-VERIFY · MEMORY", size=11, fill=GREEN, anchor="end", family=MONO, weight="600")

    # Delegation header
    dy = 400
    s.text(40, dy, "DELEGATION — das Modell folgt der Rolle", size=15, fill=TEXT, weight="700", family=MONO)
    s.line(40, dy+12, W-40, dy+12, stroke=LINE, sw=1, marker=False)

    cols = [
        (GOLD,  "LEADS — entscheiden", "Opus · denkt",
         ["pipeline-architekt","drehbuch-autor","motion-direktor","strategie-analyst","red-team-overseer","+ Architektur & Urteil"]),
        (TEAL,  "CRAFT — bauen", "Sonnet · baut",
         ["ffmpeg-meister","figuren-animator","komponist","audio-ingenieur","web-hunter · api-security","+ 40 weitere Hände"]),
        (GREEN, "RESEARCH — belegt", "Haiku · sucht",
         ["recherche-scout","surface-sweeper","recon-reader","osint-collector","+ Quelle statt Meinung",""]),
    ]
    cw, cgap = 360, 20
    cstart = (W - (3*cw + 2*cgap))/2
    cy = dy+28
    ch = 232
    for i,(col,title,model,items) in enumerate(cols):
        x = cstart + i*(cw+cgap)
        s.rect(x, cy, cw, ch, fill=PANEL, stroke=col, sw=1.6)
        s.rect(x, cy, cw, 36, fill=PANEL2, stroke=col, sw=0, rx=9)
        s.text(x+16, cy+23, title, size=13.5, fill=TEXT, weight="700", family=MONO)
        s.chip(x+cw-120, cy+7, model, col)
        yy = cy+62
        for it in items:
            if it:
                s.text(x+18, yy, "▸ "+it, size=12.5, fill=TEXT if not it.startswith("+") else DIM, family=MONO)
            yy += 27

    # QC gate
    qy = cy+ch+26
    s.rect(cstart, qy, 3*cw+2*cgap, 56, fill=PANEL2, stroke=VIOLET, sw=1.8)
    s.text(cstart+20, qy+24, "UNABHÄNGIGES QC-GATE", size=13.5, fill=VIOLET, weight="700", family=MONO)
    s.text(cstart+20, qy+44, "skeptical-validator · video-qc-pruefer · cold-witness — prüfen NUR fremde Arbeit",
           size=12.5, fill=TEXT)
    s.text(cstart+3*cw+2*cgap-20, qy+34, "maker ≠ checker", size=13, fill=VIOLET, family=MONO, weight="700", anchor="end")
    s.line(W/2, cy+ch, W/2, qy, stroke=DIM, sw=1.5)

    return s.render()

# ============================================================
# B — SELF-LEARNING MEMORY
# ============================================================
def diagram_memory():
    W, H = 1200, 560
    s = SVG(W, H)
    s.text(40, 46, "SELF-LEARNING MEMORY", size=20, fill=TEXT, weight="700", family=MONO, ls="1.5")
    s.text(40, 70, "523 Markdown-Dateien in git — das Gedächtnis lernt aus jeder Session und ruft gezielt ab",
           size=13.5, fill=DIM)

    # Nodes in a cycle
    nodes = [
        ("SESSION", "Arbeit am Target / Projekt", TEAL,   140, 150),
        ("REFLECT", "session_reflect.py\nextrahiert die Lektion", GOLD, 470, 150),
        ("MEMORY-DATEIEN", "523× .md · user/feedback/\nproject/reference · git-versioniert", GREEN, 800, 150),
        ("INDEX", "MEMORY.md + MEMORY_RULES\ntiered: warm / cold", VIOLET, 800, 360),
        ("HYBRIDRAG", "bge-m3 semantisch +\nKeyword · memory_retrieve.py", TEAL, 470, 360),
        ("NÄCHSTE SESSION", "startet NICHT bei null —\nkennt jede Lektion", TEAL2, 140, 360),
    ]
    nw, nh = 260, 92
    pos = {}
    for name, sub, col, cx, cy in nodes:
        x, y = cx-10, cy-10
        s.rect(x, y, nw, nh, fill=PANEL, stroke=col, sw=1.7)
        s.text(x+18, y+30, name, size=14, fill=TEXT, weight="700", family=MONO)
        for j, ln in enumerate(sub.split("\n")):
            s.text(x+18, y+52+j*17, ln, size=11.5, fill=DIM, family=MONO)
        pos[name] = (x, y, nw, nh)
    # arrows along the cycle
    order = ["SESSION","REFLECT","MEMORY-DATEIEN","INDEX","HYBRIDRAG","NÄCHSTE SESSION"]
    def center(n): x,y,w,h=pos[n]; return (x+w/2, y+h/2)
    # top row left->right
    s.line(pos["SESSION"][0]+nw, pos["SESSION"][1]+nh/2, pos["REFLECT"][0], pos["REFLECT"][1]+nh/2, stroke=DIM)
    s.line(pos["REFLECT"][0]+nw, pos["REFLECT"][1]+nh/2, pos["MEMORY-DATEIEN"][0], pos["MEMORY-DATEIEN"][1]+nh/2, stroke=DIM)
    # down right
    s.line(pos["MEMORY-DATEIEN"][0]+nw/2, pos["MEMORY-DATEIEN"][1]+nh, pos["INDEX"][0]+nw/2, pos["INDEX"][1], stroke=DIM)
    # bottom right->left
    s.line(pos["INDEX"][0], pos["INDEX"][1]+nh/2, pos["HYBRIDRAG"][0]+nw, pos["HYBRIDRAG"][1]+nh/2, stroke=DIM)
    s.line(pos["HYBRIDRAG"][0], pos["HYBRIDRAG"][1]+nh/2, pos["NÄCHSTE SESSION"][0]+nw, pos["NÄCHSTE SESSION"][1]+nh/2, stroke=DIM)
    # up left -> session (close loop)
    s.line(pos["NÄCHSTE SESSION"][0]+nw/2, pos["NÄCHSTE SESSION"][1], pos["SESSION"][0]+nw/2, pos["SESSION"][1]+nh, stroke=TEAL2, dash="5 4")
    s.text(W/2, H-24, "★ Fehler werden einmal gemacht — nicht zweimal.", size=13, fill=GOLD, anchor="middle", family=MONO, weight="600")
    return s.render()

# ============================================================
# C — VIDEO-STUDIO-PIPELINE (Schaltplan)
# ============================================================
def diagram_pipeline():
    W, H = 1200, 540
    s = SVG(W, H)
    s.text(40, 46, "PRODUKTIONS-PIPELINE  ·  VIDEO-STUDIO", size=20, fill=TEXT, weight="700", family=MONO, ls="1.5")
    s.text(40, 70, "13 Spezialisten als Fließband — vom Drehbuch bis zum geprüften Video, reproduzierbar",
           size=13.5, fill=DIM)

    def stage(x, y, w, label, col, sub=""):
        s.rect(x, y, w, 50, fill=PANEL, stroke=col, sw=1.6)
        s.text(x+w/2, y+26 if not sub else y+21, label, size=12.5, fill=TEXT, weight="600", family=MONO, anchor="middle")
        if sub:
            s.text(x+w/2, y+39, sub, size=10, fill=DIM, family=MONO, anchor="middle")

    # Row 1: drehbuch -> parallel trio
    y1 = 110
    stage(40, y1+40, 150, "drehbuch-autor", GOLD, "Story + szenenplan.json")
    # parallel trio
    tx = 250
    trio = [("figuren-animator",TEAL),("komponist",TEAL),("recherche-scout",GREEN)]
    for i,(lab,col) in enumerate(trio):
        stage(tx, y1+i*70, 210, lab, col)
        s.line(190, y1+65, tx, y1+i*70+25, stroke=DIM)
    s.rect(tx-12, y1-12, 234, 3*70, fill="none", stroke=LINE, sw=1, rx=10, dash="4 4")
    s.text(tx+105, y1-20, "PARALLEL", size=10.5, fill=DIM, anchor="middle", family=MONO, ls="2")

    # merge -> chain
    mx = 500
    chain1 = [("TTS · 2 Stimmen",TEAL2),("Rhubarb · Lippensync",TEAL),("motion-direktor",GOLD)]
    for i,(lab,col) in enumerate(chain1):
        stage(mx, y1+i*70, 200, lab, col)
        if i==0:
            for j in range(3):
                s.line(tx+210, y1+j*70+25, mx, y1+25, stroke=DIM, marker=(j==1))
        else:
            s.line(mx+100, y1+(i-1)*70+50, mx+100, y1+i*70, stroke=DIM)

    # chain2
    cx = 740
    chain2 = [("audio-ingenieur",TEAL),("untertitel + farb",TEAL),("QC-GATE + Kinder-Sicherheit",VIOLET)]
    for i,(lab,col) in enumerate(chain2):
        stage(cx, y1+i*70, 230, lab, col)
        if i==0:
            s.line(mx+200, y1+2*70+25, cx, y1+25, stroke=DIM)
        else:
            s.line(cx+115, y1+(i-1)*70+50, cx+115, y1+i*70, stroke=DIM)

    # output
    ox = 1010
    stage(ox, y1+2*70, 150, "Metadaten +", GREEN, "SEO-Titel · Video")
    s.line(cx+230, y1+2*70+25, ox, y1+2*70+25, stroke=DIM)

    s.text(W/2, H-28, "Dieselbe Mechanik baut Marken-Videos, Erklär-Clips, Motion-Grafiken und den Kinderkanal.",
           size=12.5, fill=DIM, anchor="middle")
    return s.render()

def tile(s, x, y, w, h, title, color, items, badge=None):
    s.rect(x, y, w, h, fill=PANEL, stroke=color, sw=1.6)
    s.rect(x, y, w, 36, fill=PANEL2, stroke=color, sw=0, rx=9)
    s.text(x+16, y+23, title, size=13, fill=TEXT, weight="700", family=MONO)
    if badge:
        bw = 16 + len(badge)*7.3
        s.rect(x+w-bw-12, y+7, bw, 22, fill=BG, stroke=color, sw=1.2, rx=11)
        s.text(x+w-bw/2-12, y+22, badge, size=11, fill=color, family=MONO, weight="600", anchor="middle")
    yy = y+60
    for it in items:
        s.text(x+16, yy, "▸ "+it, size=12, fill=TEXT, family=MONO)
        yy += 25

# ============================================================
# ARSENAL-LANDKARTE (1600x950)
# ============================================================
def arsenal():
    W, H = 1600, 950
    s = SVG(W, H)
    s.text(40, 46, "DAS ARSENAL — AUF EINEN BLICK", size=20, fill=TEXT, weight="700", family=MONO, ls="1.5")
    s.text(40, 70, "autorisierte offensive & defensive Fähigkeiten, in Werkzeuge und reproduzierbare Verfahren gegossen",
           size=13.5, fill=DIM)
    cats = [
        ("RECON & OSINT", TEAL, "Phase 1", ["nmap_max · masscan","subfinder · amass","httpx · katana · gau","shodan · censys (MCP)","exa · firecrawl","target-radar · asset-monitor"]),
        ("WEB-APPSEC", TEAL, "aktiv", ["ffuf · gobuster · feroxbuster","caido / burp (MCP-Bridge)","nuclei · dalfox · arjun","desync · cache-deception","authrecon · elite-auth-hunt"]),
        ("EXPLOIT & CHAIN", GOLD, "20 Klassen", ["vuln-* : IDOR·SQLi·SSRF","SSTI·RCE·XXE·JWT·XSS","mass-assign·path-traversal","chaining · variant-hunt","poc-validator · cold-witness"]),
        ("AD & LATERAL", VIOLET, "intern", ["Kerberoast · AS-REP","DCSync · delegation-abuse","BloodHound · shortest-path","Certipy ESC1-16 · coerce→relay","impacket · NetExec · dsniff"]),
        ("CLOUD & K8S", GREEN, "", ["IAM-privesc-Graph","S3-enum · bucket-misconfig","SSRF → IMDS","K8s-attack · container-escape","serverless-surface"]),
        ("MOBILE & RE", TEAL2, "statik", ["apktool · jadx (MCP)","frida · cert-pinning-bypass","ghidra · radare2 · angr","re_triage · capa · floss","smali · firmware/binwalk"]),
        ("PURPLE & DETECTION", VIOLET, "blue", ["Sigma · Falco · Sysmon","detection-gap-mapping","telemetry-timeline","offsec-lab · chains","evasion-analysis"]),
        ("AI / LLM RED-TEAM", GOLD, "fresh", ["garak · PyRIT","prompt-injection-psychologie","ai-surface-hunt · RAG-bleed","MCP/tool-calling-abuse","vulnhuntr-scan"]),
        ("SAFETY-HOOKS", TEAL, "gate", ["injection_scanner","scope_authz_gate","kill_switch · loop_detection","safe_hook (anti-lockout)","prompt_prefilter"]),
    ]
    cols, rows = 3, 3
    mx, gap = 40, 24
    tw = (W - 2*mx - (cols-1)*gap)/cols
    th = 258
    y0 = 100
    for i,(title,col,badge,items) in enumerate(cats):
        r, c = divmod(i, cols)
        x = mx + c*(tw+gap)
        y = y0 + r*(th+gap)
        tile(s, x, y, tw, th, title, col, items, badge or None)
    return s.render()

# ============================================================
# AUTONOMER BETRIEB (1520x640)
# ============================================================
def betrieb():
    W, H = 1520, 660
    s = SVG(W, H)
    s.text(40, 46, "AUTONOMER BETRIEB — SELBST-BEWACHT, MELDET AUFS HANDY", size=20, fill=TEXT, weight="700", family=MONO, ls="1")
    s.text(40, 70, "läuft ohne Aufsicht weiter — jede Aktion abgesichert, jedes Ereignis gemeldet, alles rückgekoppelt ins Gedächtnis",
           size=13.5, fill=DIM)
    # Left: every action -> hooks gate
    s.rect(40, 120, 300, 54, fill=PANEL, stroke=DIM, sw=1.4)
    s.text(190, 152, "JEDE TOOL-AKTION", size=14, fill=TEXT, weight="600", family=MONO, anchor="middle")
    s.rect(40, 210, 300, 150, fill=PANEL2, stroke=TEAL, sw=1.8)
    s.text(60, 238, "SAFETY-HOOKS", size=14, fill=TEAL, weight="700", family=MONO)
    for j,ln in enumerate(["injection_scanner","scope_authz_gate","kill_switch · loop_detection","safe_hook · prompt_prefilter","über 16 Lifecycle-Events"]):
        s.text(60, 264+j*20, "▸ "+ln, size=11.5, fill=TEXT if j<4 else DIM, family=MONO)
    s.line(190, 174, 190, 210, stroke=DIM, sw=1.5)

    # Middle: radars + health
    s.rect(400, 150, 320, 110, fill=PANEL, stroke=GREEN, sw=1.7)
    s.text(420, 178, "AUTONOME RADARS", size=13.5, fill=GREEN, weight="700", family=MONO)
    for j,ln in enumerate(["target-radar · trend-radar","asset-monitor · hacktivity-stream"]):
        s.text(420, 202+j*20, "▸ "+ln, size=11.5, fill=TEXT, family=MONO)
    s.text(420, 246, "scannen rund um die Uhr", size=11, fill=DIM, family=MONO)
    s.rect(400, 290, 320, 90, fill=PANEL, stroke=VIOLET, sw=1.7)
    s.text(420, 318, "HEALTH · SELF-AUDIT", size=13.5, fill=VIOLET, weight="700", family=MONO)
    for j,ln in enumerate(["Heartbeat · Token-Rot-Check","OnFailure-Netz · Selbstheilung"]):
        s.text(420, 342+j*20, "▸ "+ln, size=11.5, fill=TEXT, family=MONO)
    s.line(340, 285, 400, 210, stroke=DIM, sw=1.4)
    s.line(340, 285, 400, 330, stroke=DIM, sw=1.4)

    # Right: ntfy + phone
    s.rect(790, 150, 320, 110, fill=PANEL2, stroke=GOLD, sw=1.8)
    s.text(810, 178, "ntfy  ·  SELF-HOSTED :8936", size=13, fill=GOLD, weight="700", family=MONO)
    for j,ln in enumerate(["Tailscale-only + Token","Topics bb-urgent · radar · health"]):
        s.text(810, 202+j*20, "▸ "+ln, size=11.5, fill=TEXT, family=MONO)
    s.text(810, 246, "Push in Sekunden", size=11, fill=DIM, family=MONO)
    s.rect(790, 290, 320, 90, fill=PANEL, stroke=TEAL2, sw=1.7)
    s.text(810, 318, "HANDY · ACTION-BUTTONS", size=13, fill=TEAL2, weight="700", family=MONO)
    s.text(810, 342, "▸ ntfy-webhook :8939", size=11.5, fill=TEXT, family=MONO)
    s.text(810, 362, "▸ Knopfdruck → Server-Aktion", size=11.5, fill=TEXT, family=MONO)
    s.line(720, 205, 790, 205, stroke=DIM, sw=1.5)
    s.line(720, 335, 790, 335, stroke=DIM, sw=1.5)
    # feedback phone -> action back to left (RemoteTrigger)
    s.path(f"M 950 380 C 950 440, 190 460, 190 405", stroke=TEAL2, sw=1.5, dash="5 4")
    s.text(W/2, 452, "Knopf am Handy löst serverseitig aus  ·  RemoteTrigger", size=11.5, fill=TEAL2, anchor="middle", family=MONO)

    # bottom memory bar
    s.rect(40, 500, W-80, 64, fill=PANEL2, stroke=GOLD, sw=1.6)
    s.text(64, 528, "RÜCKKOPPLUNG", size=13, fill=GOLD, weight="700", family=MONO)
    s.text(64, 550, "jedes Ereignis → session-reflect → 523-Datei-Memory — das System lernt aus seinem eigenen Betrieb",
           size=13, fill=TEXT)
    for sxp in (190, 560, 950):
        s.line(sxp, 380 if sxp!=190 else 360, sxp, 500, stroke="#232b35", sw=1.2, marker=False)
    return s.render()

# ============================================================
# MCP-GRID (1600x470)
# ============================================================
def mcp():
    W, H = 1600, 470
    s = SVG(W, H)
    s.text(40, 46, "22 MCP-SERVER — DIE WERKZEUG-SCHNITTSTELLEN", size=20, fill=TEXT, weight="700", family=MONO, ls="1")
    s.text(40, 70, "jeder Server ist ein scharfes Werkzeug am selben Steuerpult — gruppiert nach Zweck",
           size=13.5, fill=DIM)
    groups = [
        ("RECON & OSINT", TEAL,  ["shodan","censys","exa","brave-search","firecrawl","fetch"]),
        ("CODE & STATIK", GOLD,  ["codegraph","claude-context","semgrep","repomix","filesystem"]),
        ("APPSEC & MOBILE", VIOLET, ["caido","chrome-devtools","apktool","writeup-search"]),
        ("WISSEN & STEUERUNG", GREEN, ["memory-graph","sequential-thinking","todo-server","youtube","time"]),
        ("DEV & BEFUNDE", TEAL2, ["github","findings-db"]),
    ]
    y = 100
    for title,col,servers in groups:
        s.rect(40, y, 250, 46, fill=PANEL2, stroke=col, sw=1.5)
        s.text(56, y+28, title, size=12.5, fill=col, weight="700", family=MONO)
        cx = 310
        for sv in servers:
            w = 20 + len(sv)*8.6
            s.rect(cx, y+9, w, 28, fill=PANEL, stroke=col, sw=1.3, rx=6)
            s.text(cx+w/2, y+28, sv, size=12.5, fill=TEXT, family=MONO, anchor="middle")
            cx += w + 14
        y += 62
    return s.render()

# ============================================================
# BANNER (1600x500) — Profil-Kopf
# ============================================================
def banner():
    import math
    W, H = 1600, 500
    s = SVG(W, H)
    # dezenter Rahmen (User-Vorliebe: nur farbige dezente Rahmen)
    s.rect(14, 14, W-28, H-28, fill=BG, stroke=LINE, sw=1.5, rx=14)
    s.rect(14, 14, W-28, H-28, fill="none", stroke=TEAL2, sw=1.0, rx=14)
    # feines Raster im rechten Drittel (Tiefe, sehr dezent)
    for gx in range(980, 1560, 40):
        s.line(gx, 40, gx, 460, stroke="#161b22", sw=1, marker=False)
    for gy in range(40, 470, 40):
        s.line(980, gy, 1560, gy, stroke="#161b22", sw=1, marker=False)

    # ---- Konstellation rechts (Orchestrierungs-Motiv) ----
    hx, hy = 1290, 200
    sats = [(-160, GREEN, 14), (-115, TEAL, 18), (-60, VIOLET, 13),
            (-20, TEAL2, 16), (35, TEAL, 20), (80, GREEN, 14),
            (130, VIOLET, 16), (175, TEAL2, 13), (210, TEAL, 17)]
    import math as _m
    # Ringe hinter dem Hub
    for rr in (150, 108):
        s.e.append(f'<circle cx="{hx}" cy="{hy}" r="{rr}" fill="none" stroke="#1b222c" stroke-width="1"/>')
    pts = []
    for i,(ang,col,r) in enumerate(sats):
        a = _m.radians(ang)
        dist = 150 if i % 2 == 0 else 108
        x = hx + dist*_m.cos(a); y = hy + dist*_m.sin(a)
        pts.append((x,y,col,r))
        s.line(hx, hy, x, y, stroke="#2b3440", sw=1.2, marker=False)
    for x,y,col,r in pts:
        s.e.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{PANEL}" stroke="{col}" stroke-width="2"/>')
        s.e.append(f'<circle cx="{x}" cy="{y}" r="{max(2,r-9)}" fill="{col}" opacity="0.55"/>')
    # Hub (Showrunner)
    s.e.append(f'<circle cx="{hx}" cy="{hy}" r="40" fill="{PANEL2}" stroke="{GOLD}" stroke-width="2.6"/>')
    s.text(hx, hy-2, "EP", size=20, fill=GOLD, weight="700", family=MONO, anchor="middle")
    s.text(hx, hy+16, "Opus", size=10, fill=DIM, family=MONO, anchor="middle")

    # ---- Text links ----
    s.text(80, 96, "NEO849  ·  MICHAEL FLEPS", size=16, fill=DIM, family=MONO, weight="600", ls="3")
    s.text(78, 178, "Systeme, die sich selbst", size=56, fill=TEXT, weight="700")
    s.text(78, 244, "orchestrieren.", size=56, fill=TEAL, weight="700")
    s.text(80, 292, "— gesichert mit Angreifer-Blick.", size=22, fill=DIM)
    s.text(80, 336, "KI-Orchestrierung · Self-Learning Memory · Privacy-Engineering · Offensive Security",
           size=16, fill=TEXT, family=MONO)
    # Modell-Disziplin-Chips
    cx = 80
    for lab,col in [("Opus · denkt",GOLD),("Sonnet · baut",TEAL),("Haiku · sucht",GREEN)]:
        cx += s.chip(cx, 356, lab, col) + 12

    # ---- Stat-Strip unten ----
    s.line(80, 410, 920, 410, stroke=LINE, sw=1, marker=False)
    stats = [("57","Agenten"),("3","Professoren"),("104","Skills"),
             ("22","MCP-Server"),("523","Memories"),("84","Scripts")]
    sx = 80
    for val,lab in stats:
        s.text(sx, 452, val, size=30, fill=TEXT, weight="700", family=MONO)
        w = len(val)*19
        s.text(sx+w+8, 446, lab, size=13, fill=DIM, family=MONO)
        sx += w + 8 + len(lab)*8.7 + 34
    return s.render()


if __name__ == "__main__":
    import os
    out = os.path.dirname(os.path.abspath(__file__))
    for name, fn in [("orchestrierung", diagram_orchestration),
                     ("memory", diagram_memory),
                     ("pipeline", diagram_pipeline),
                     ("arsenal", arsenal),
                     ("betrieb", betrieb),
                     ("mcp", mcp),
                     ("banner", banner)]:
        p = os.path.join(out, f"{name}.svg")
        with open(p, "w") as f:
            f.write(fn())
        print("wrote", p)
