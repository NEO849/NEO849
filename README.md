<p align="center">
  <img src="assets/readme-banner.png" alt="KI-Infrastruktur, die sich selbst orchestriert — Agent-Orchestrierung · MCP · Lokale LLMs · Self-Learning Memory · On-Device-Privacy" width="900">
</p>

<p align="center">
  <b>Ich baue Systeme, die sich selbst orchestrieren — und sichere sie mit Angreifer-Blick.</b><br>
  <em>Ein orchestrierter Verbund aus Spezialisten-Agenten, lokalen LLMs, selbst-lernendem Gedächtnis,<br>
  eigenen MCP-Servern und reproduzierbaren Pipelines — auf eigenem, gehärtetem Server.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Agent_Orchestration-141820?style=for-the-badge&labelColor=0b0f14" alt="Agent Orchestration">
  <img src="https://img.shields.io/badge/MCP_Server-141820?style=for-the-badge&labelColor=0b0f14" alt="MCP">
  <img src="https://img.shields.io/badge/On--Device_Privacy-141820?style=for-the-badge&labelColor=0b0f14" alt="On-Device Privacy">
  <img src="https://img.shields.io/badge/Offensive_Security-141820?style=for-the-badge&labelColor=0b0f14" alt="Offensive Security">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-2b3440?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/TypeScript-2b3440?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/Three.js-2b3440?style=flat-square&logo=threedotjs&logoColor=white" alt="Three.js">
  <img src="https://img.shields.io/badge/Swift-2b3440?style=flat-square&logo=swift&logoColor=white" alt="Swift">
  <img src="https://img.shields.io/badge/Linux-2b3440?style=flat-square&logo=linux&logoColor=white" alt="Linux">
  <img src="https://img.shields.io/badge/Docker-2b3440?style=flat-square&logo=docker&logoColor=white" alt="Docker">
  <a href="https://priframe.com"><img src="https://img.shields.io/badge/priframe-live-38617a?style=flat-square&labelColor=0b0f14" alt="priframe live"></a>
</p>

<p align="center">
  <a href="#das-system">System</a> &nbsp;·&nbsp;
  <a href="#die-orchestrierungs-maschine">Orchestrierung</a> &nbsp;·&nbsp;
  <a href="#das-claude-setup">Claude-Setup</a> &nbsp;·&nbsp;
  <a href="#self-learning-memory">Memory</a> &nbsp;·&nbsp;
  <a href="#produktions-pipelines">Pipelines</a> &nbsp;·&nbsp;
  <a href="#was-uns-abhebt">Was uns abhebt</a> &nbsp;·&nbsp;
  <a href="#projekte">Projekte</a>
</p>

---

<a id="das-system"></a>

![Das System](https://img.shields.io/badge/Das_System-141820?style=for-the-badge&labelColor=0b0f14)

Ich betreibe keine Sammlung von Skripten, sondern eine **durchgehend orchestrierte KI-/Security-Plattform**
auf eigenem, gehärtetem Server — entworfen für ein Prinzip: **überprüfbare, belastbare Ergebnisse statt
Black-Box-Automatik.** Nichts gilt als „fertig", bevor es ein unabhängiger Prüfer gegengecheckt und ein
echter Lauf es bestätigt hat.

Was auf dem Server tatsächlich steht — gezählt, nicht geschätzt:

| Baustein | Umfang | Was es ist |
|---|---:|---|
| **Spezialisten-Agenten** | **57** | eigenständige Experten-Rollen (Recon, Web-AppSec, Business-Logic, Exploit-Chaining, Validierung, Video-Produktion, Business/Legal …), geführt von einem Overseer |
| **Fach-Professoren** | **3** | Protokoll-/RFC-Korrektheit, Mathematik/Krypto, Computer-Vision-Modelle — im adversarialen Review-Loop |
| **Modulare Skills** | **104** | wiederverwendbare Verfahren, die als Playbook in den Kontext geladen werden |
| **Slash-Commands** | **22** | Ein-Wort-Auslöser für ganze Abläufe (`/master-welle`, `/director`, `/submit-gate` …) |
| **MCP-Server** | **22** | Werkzeug-Schnittstellen (Code-Graph, Semgrep, Filesystem, Repomix, Browser-Steuerung, OSINT u. a.) |
| **Self-Learning Memory** | **523** | versioniertes Markdown-Gedächtnis mit semantischem Abruf — lernt aus jeder Session |
| **Automations-Skripte** | **84** | Hooks, Pipelines, Health-Heartbeats, Reflektions-Schleifen |

**Modell-Disziplin:** schweres Denken, Bauen und Suchen laufen auf passend gewählten Modellen —
*Opus denkt · Sonnet baut · Haiku sucht* — statt alles teuer über ein Modell zu jagen.

---

<a id="die-orchestrierungs-maschine"></a>

![Die Orchestrierungs-Maschine](https://img.shields.io/badge/Die_Orchestrierungs--Maschine-141820?style=for-the-badge&labelColor=0b0f14)

Der Kern ist nicht *ein* Agent, sondern ein **Dirigent über vielen Spezialisten**. Jede nicht-triviale
Aufgabe durchläuft denselben Vier-Phasen-Loop — **Zerlegen → Zuweisen → Parallel → Härten** — und erst
danach kommt Live-Verify und das Gedächtnis. Kein Agent ruft von sich aus den nächsten; die Verkettung
führt der Showrunner anhand maschinen-lesbarer Übergaben.

<div align="center">
  <img src="assets/orchestrierung.png" alt="Die Orchestrierungs-Maschine: Showrunner führt den Zerlegen-Zuweisen-Parallel-Härten-Loop; Delegation nach Modell-Ebene (Opus-Leads, Sonnet-Craft, Haiku-Research); unabhängiges QC-Gate nach dem Prinzip maker ≠ checker" width="900">
  <br><sub>Vektor-Download: <a href="assets/orchestrierung.svg">orchestrierung.svg</a></sub>
</div>

**Das entscheidende Detail — `maker ≠ checker`:** Wer etwas baut, darf es nie selbst abnehmen. Ein
unabhängiges QC-Gate (`skeptical-validator`, `cold-witness`, `video-qc-pruefer`) prüft **nur fremde Arbeit**
und versucht aktiv, das Ergebnis zu widerlegen. Das tötet die teuerste Fehlerklasse: das zu früh geglaubte
„passt schon".

---

<a id="das-claude-setup"></a>

![Das Claude-Setup](https://img.shields.io/badge/Das_Claude--Setup-141820?style=for-the-badge&labelColor=0b0f14)

Alles ist Datei — versioniert, lesbar, reproduzierbar. Keine verborgene Magie, keine Cloud-Abhängigkeit
für die Steuerung. Die gesamte Intelligenz liegt als Text auf der Platte und lässt sich auditieren:

```
~/.claude/
├── agents/        57 Spezialisten + 3 Professoren  ·  gemeinsame Charta (_elite-charter, _scope-guard)
│                  und ein Schaltplan (_orchestration.md) als Quelle der Wahrheit für Auswahl & Verkettung
├── skills/        104 modulare Verfahren  ·  je ein SKILL.md, bei Bedarf in den Kontext geladen
├── commands/      22 Slash-Commands  ·  /master-welle /director /submit-gate /elite-prompt …
├── scripts/       84 Python-Automationen  ·  Session-Hooks, Memory-Reflektion, Health-Heartbeat
├── projects/      Self-Learning Memory  ·  523 Markdown-Fakten in git, tiered index + HybridRAG
├── output-styles/ Antwort-Modi  ·  z. B. „Lern-Modus" (Erklär-Layer über jeder Antwort)
└── workflows/     reproduzierbare pipeline/parallel-Abläufe (garantierter Fan-out)
```

**Warum Datei-basiert gewinnt:** Ein Agent, ein Skill, eine Lektion ist jeweils *eine* versionierte Datei.
Man sieht im `git log`, *wann* eine Fähigkeit dazukam und *warum* — und kann jede Änderung zurückrollen.
Das ist der Unterschied zwischen einem auditierbaren System und einem Prompt-Haufen.

---

<a id="self-learning-memory"></a>

![Self-Learning Memory](https://img.shields.io/badge/Self--Learning_Memory-141820?style=for-the-badge&labelColor=0b0f14)

Der eigentliche Burggraben. Die meisten KI-Setups starten jede Sitzung bei null. Dieses nicht: Am Ende
jeder Session wird die **Lektion extrahiert** und als versionierte Markdown-Datei abgelegt. Beim nächsten
Start steht sie wieder zur Verfügung — gezielt abgerufen über semantische Suche (**bge-m3**) plus Keyword.

<div align="center">
  <img src="assets/memory.png" alt="Self-Learning Memory: Session → Reflektion → 523 versionierte Markdown-Dateien → tiered Index → HybridRAG-Abruf → nächste Session startet nicht bei null" width="900">
  <br><sub>Vektor-Download: <a href="assets/memory.svg">memory.svg</a></sub>
</div>

**523 Fakten**, sortiert nach Typ (`user` / `feedback` / `project` / `reference`), in git versioniert, über
einen schlanken Index warm/cold gestaffelt. Das Ergebnis in einem Satz:

> **★ Ein Fehler wird einmal gemacht — nicht zweimal.** Jede Korrektur wird zur dauerhaften Regel.

---

<a id="produktions-pipelines"></a>

![Produktions-Pipelines](https://img.shields.io/badge/Produktions--Pipelines-141820?style=for-the-badge&labelColor=0b0f14)

Pipelines sind kein Diagramm an der Wand, sondern laufender Code. Beispiel **Video-Studio**: 13 Spezialisten
greifen wie Zahnräder ineinander — vom Drehbuch über datengetriebene Motion-Grafik (Remotion), Offline-
Lippensync (Rhubarb) und Audio-Mastering nach Broadcast-Norm bis zur unabhängigen Qualitätskontrolle.
**Alles lokal, reproduzierbar, ohne externe Render-Cloud.**

<div align="center">
  <img src="assets/pipeline.png" alt="Video-Studio-Pipeline: drehbuch-autor, dann parallel figuren-animator/komponist/recherche-scout, dann TTS, Rhubarb-Lippensync, motion-direktor, audio-ingenieur, untertitel+farb, QC-Gate mit Kinder-Sicherheit, Metadaten" width="900">
  <br><sub>Vektor-Download: <a href="assets/pipeline.svg">pipeline.svg</a></sub>
</div>

Dieselbe Mechanik erzeugt Marken-Videos, Erklär-Clips, Motion-Grafiken und Diagramme — **die drei
Diagramme oben auf dieser Seite sind damit gebaut.** Daneben laufen Security-Wellen nach demselben Prinzip
(`/master-welle`: breit fächern, eng führen, adversarial härten) und Recon-/OSINT-Automationen.

---

<a id="was-uns-abhebt"></a>

![Was uns abhebt](https://img.shields.io/badge/Was_uns_abhebt-141820?style=for-the-badge&labelColor=0b0f14)

| Die meisten Setups | Dieses System |
|---|---|
| Ein Modell für alles | **Modell folgt der Rolle** — Opus denkt, Sonnet baut, Haiku sucht (Kosten- & Qualitäts-Disziplin) |
| „Der Agent sagt, es passt" | **`maker ≠ checker`** — unabhängiges QC-Gate widerlegt jedes Ergebnis, bevor es zählt |
| Behauptet „funktioniert" | **Live-Verify** — erst der echte Lauf / gebrannte Frame gilt, nicht die Behauptung |
| Vergisst nach jeder Session | **523-Datei-Gedächtnis** — lernt dauerhaft, Fehler nur einmal |
| Prompt-Haufen, Black-Box | **alles als Datei in git** — auditierbar, rückrollbar, nachvollziehbar |
| Cloud-abhängig | **eigener gehärteter Server** · On-Device-Inferenz · privates Tailscale-Mesh |

★ Der rote Faden: **Prüfbarkeit vor Bequemlichkeit.** Das System ist langsamer als blindes Auto-Pilot —
und genau deshalb belastbar.

---

<a id="stack"></a>

![Schnittstellen & Stack](https://img.shields.io/badge/Schnittstellen_%26_Stack-141820?style=for-the-badge&labelColor=0b0f14)

```
KI-Systeme    Agent-Orchestrierung · 22 MCP-Server · lokale LLMs (Ollama) · Self-Learning Memory · HybridRAG · Pipelines
Security      Web-AppSec (IDOR/BOLA, Auth, Info-Disclosure) · Recon-Automation · Caido/Burp · Nuclei · Semgrep
Medien        Remotion (datengetriebene Motion-Grafik) · FFmpeg · SVG→Vektor-Diagramme · Rhubarb-Lippensync · WhisperX
Engineering   Python · TypeScript/React · Three.js/WebGL · Swift/SwiftUI · Kotlin
Infrastruktur Linux (gehärtet) · Docker · Bash · git · Cloudflare · Tailscale (privates Mesh)
Privacy       On-Device-Inferenz (ONNX-Runtime-Web / WebGPU) · Redaktion im Browser, kein Upload
```

---

<a id="projekte"></a>

![Projekte](https://img.shields.io/badge/Projekte-141820?style=for-the-badge&labelColor=0b0f14)

| Projekt | Worum es geht | Stack |
|---|---|---|
| **[priframe](https://priframe.com)** | On-Device-Gesichtsschutz: Redaktion zu 100 % im Browser, kein Upload, kein Konto | TS · WebGL · ONNX |
| [qwen-memory-agent](https://github.com/NEO849/qwen-memory-agent) | Regress-Guard — selbst-korrigierendes Gedächtnis für KI-Coding-Agenten | Python |
| [markmem](https://github.com/NEO849/markmem) | Selbst-lernendes, selbst-tunendes KI-Gedächtnis auf Markdown + git | Python |
| [agentdeck](https://github.com/NEO849/agentdeck) | Ein-Befehl-Integration einer tmux-Agenten-Sidebar in Claude Code | Shell |
| [aria-password-tester](https://github.com/NEO849/aria-password-tester) | Passwortstärke-Tester: zxcvbn, Shannon-Entropie, k-Anonymity-HIBP | Python |
| [neo-portfolio](https://github.com/NEO849/neo-portfolio) | Portfolio + live betriebene OSINT-Intelligence-Suite | TS · FastAPI |

---

<p align="center"><em>Offen für Projekte & Zusammenarbeit — sichere KI-Automation, Privacy-Engineering, offensive Security.</em></p>
