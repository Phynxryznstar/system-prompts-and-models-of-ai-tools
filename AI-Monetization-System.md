# AI Monetization System
## Reverse-Engineered from Production Prompt Architecture

---

# PART 1: FILES STUDIED AND WHY

## High-Value Files Analyzed

### Tier 1 — Core Architecture (Most Useful)

**`Manus Agent Tools & Prompt/Modules.txt` + `Agent loop.txt`**
The most architecturally complete prompt in the repository. Manus uses a modular system — Planner, Knowledge, Datasource, and Writing modules — each with its own rules. The agent loop (Analyze → Select → Execute → Iterate → Submit → Standby) is the cleanest execution loop in the repo. Its `writing_rules`, `info_rules`, `browser_rules`, and `error_handling` sections show how to structure a prompt that governs complex, multi-step autonomous work. Directly applicable to building AI agents and workflow automation.

**`Devin AI/Prompt.txt`**
The most disciplined planning prompt in the repository. Devin separates "planning mode" from "standard mode" — two distinct cognitive states with different rules. The `<think>` tool shows how to force the model to reason before acting. The 10+ conditions for when to use the think tool are a masterclass in governing decision quality. Git safety rules and the "don't modify tests" constraint show production-grade operational discipline. Applicable to any agentic system where mistakes are expensive.

**`Cursor Prompts/Agent Prompt 2025-09-03.txt`**
The most operator-complete prompt in the repository. Contains `status_update_spec`, `summary_spec`, `completion_spec`, `flow`, `tool_calling`, `context_understanding`, `maximize_parallel_tool_calls`, `grep_spec`, `making_code_changes`, `code_style`, `linter_errors`, `non_compliance`, `todo_spec`, and `markdown_spec` — all as named, structured sub-systems. This shows how to build a prompt that handles communication, task management, quality assurance, and failure recovery simultaneously.

**`Kiro/Spec_Prompt.txt`**
The only prompt in the repository that encodes a complete iterative development workflow as rules. Requirements → Design → Tasks, each gated by explicit user approval using EARS format. The spec-driven development model (requirements.md → design.md → tasks.md) is a framework that can be directly productized for client work. Useful for client delivery, SOPs, and productized services.

**`Cluely/Enterprise Prompt.txt`**
The most revenue-connected prompt in the repository. Built for live sales calls, interviews, and meetings. The priority ordering (question answering → term definition → conversation advancement → objection handling → screen problem solving → passive mode) is a real-time decision tree for human conversations. The objection handling section and behavioral question framework have direct revenue applications.

**`v0 Prompts and Tools/Prompt.txt`**
The most complete product-building prompt in the repository. Contains full design system rules (color, typography, layout), data persistence architecture, integration recommendations, debugging protocol, memory management, and extensive alignment examples. The "thought process → tool call → summary" pattern is the cleanest user-facing agent communication loop in the repo.

**`Perplexity/Prompt.txt`**
The most structured output-formatting prompt in the repository. Contains `format_rules`, `restrictions`, `query_type` routing (academic, news, weather, people, coding, recipes, translation, creative, science, URL), and `planning_rules`. The citation and formatting standards are the best in the repo for research-output prompts.

**`Lovable/Agent Prompt.txt`**
Strong for discussion-first design philosophy: "assume users want to discuss and plan rather than immediately implement code." Contains the clearest sequential workflow (check context → review tools → default to discussion → think & plan → clarify → gather context → implement → verify) of any prompt in the repository. The design system principles and scope-control rules (avoid scope creep, no overengineering) are directly applicable to client delivery work.

### Tier 2 — Useful Structural Patterns

**`Warp.dev/Prompt.txt`** — Question vs. task distinction, complexity tiering (simple vs. complex), citation requirements.

**`Orchids.app/Decision-making prompt.txt`** — Conditional routing, sequential vs. parallel tool execution, preserving original user intent.

**`Kiro/Vibe_Prompt.txt`** and **`Kiro/Mode_Classifier_Prompt.txt`** — Tone calibration, response style rules, mode detection.

**`Manus Agent Tools & Prompt/Prompt.txt`** — Prompting guide with before/after examples, iterative prompting model.

### Ignored (Too Thin, Repetitive, or Not Business-Applicable)

- `Xcode/` — Apple-specific, developer-only context, no business transfer value
- `CodeBuddy Prompts/` — Generic code assistant, no structural novelty
- `Z.ai Code/` — Minimal content
- `Qoder/` — Too narrow in scope
- `Poke/` — Fragmented across 6 files, low density of reusable architecture
- `Amp/` — YAML config files, not prompt architecture
- `Google/Gemini/AI Studio vibe-coder.txt` — Minimal instruction set

---

# PART 2: EXTRACTED PROMPTING PRINCIPLES

## How the Best Prompts Use Each Layer

### 1. Role Definition
The best prompts name the AI with specificity, not generality. "You are Manus, an AI agent created by the Manus team" + a numbered list of specific capabilities is more powerful than "You are a helpful assistant." Role definition in high-performing prompts answers: *what you are*, *what you excel at*, and *what your primary interface is*. Roles are paired with capability statements that function as behavioral permissions — "you can deploy websites, run shell commands, install packages" tells the model what is in-scope before the user asks.

**Business rule:** Name the agent, define 5-7 specific task domains it excels at, state the primary interface. This prevents out-of-scope drift and focuses output quality.

### 2. Mission / Objective
High-performing prompts state the mission as a priority hierarchy, not a paragraph. Cluely's objective is structured as: primary directive → secondary directive → tertiary → fallback. The `<primary_directive>` tag tells the model what to do when it faces ambiguity. Devin's mission is a single sentence: "Accomplish the task using the tools at your disposal while abiding by the guidelines outlined here." Clarity beats length.

**Business rule:** State the mission as a 1-2 sentence core objective, then enumerate 3-5 priority-ordered behaviors for when things are ambiguous.

### 3. Context Injection
The best prompts inject context through named structures, not free text. Manus uses `<event_stream>` with typed events (Message, Action, Observation, Plan, Knowledge, Datasource). Cursor uses automatically-attached file state. Cluely uses conversation transcripts with speaker labels. The key pattern: context is *typed* and *prioritized* — model's internal knowledge < web search < authoritative API data (Manus's `info_rules`).

**Business rule:** Tell the model what types of context it will receive, what they mean, and how to weight them. Untyped context gets hallucinated on.

### 4. User Input Handling
Strong prompts define how to treat unclear inputs. Warp asks: is this a *question* or a *task*? Lovable: "assume discussion first, not implementation." Kiro: "ask for clarification, but never more than once." Devin: "don't be shy — ask when you're missing credentials or context." The divergence is instructive: agents that take irreversible actions (Devin, Warp) default to clarify. Agents building UI (Lovable, v0) default to act.

**Business rule:** Write explicit rules for ambiguous inputs based on the cost of a wrong action. High-cost actions (sending emails, writing contracts) → clarify first. Low-cost actions (drafts, outlines) → act first, offer iteration.

### 5. Constraints
The best prompts use layered constraint architectures. Hard constraints (NEVER, CRITICAL, IMPORTANT) govern safety and irreversibility. Soft constraints (prefer, default to, generally) govern quality and style. Cursor uses three levels: linter errors (must fix), code style (should follow), communication style (prefer). Devin's constraints are context-specific: different rules for git operations, testing, coding style, and user communication.

**Business rule:** Separate hard constraints (NEVER do X) from soft constraints (prefer Y). Hard constraints should be short, specific, and capitalized. Soft constraints should explain the *why* behind the preference.

### 6. Decision Rules
This is the most underused pattern in amateur prompting. Professional prompts encode decision trees. Cluely's priority ordering tells the model what to do when multiple actions are valid. Orchids tells the model: "if clone → call clone_website first, then generate_design_system, never in parallel." Devin tells the model when to use `<think>` with 10 explicit conditions. Kiro tells the model when to return to previous steps vs. proceed.

**Business rule:** Write decision rules as explicit if/then conditions, not as vague preferences. "If X, do Y. If not X, do Z" outperforms "try to determine the best approach."

### 7. Examples
High-performing prompts use typed, labeled, contrasting examples. Perplexity's `format_rules` shows a bad example and a good example for every rule. Manus's prompting guide shows "Poor Prompt" vs. "Improved Prompt." v0's alignment section shows complete user/assistant exchanges with visible thought processes. Cursor's `code_style` section shows bad → good variable naming with real identifiers.

**Business rule:** For every output rule, include one bad example and one good example. Examples are more load-bearing than instructions. Instructions tell; examples show.

### 8. Output Formats
Every high-performing prompt defines the output format in a dedicated section. Perplexity uses `<format_rules>` with specific markdown rules, list formatting standards, table preferences, citation syntax, and summary requirements. Cursor uses `<summary_spec>`, `<status_update_spec>`, and `<completion_spec>` as separate named formats. Cluely defines maximum word counts per section (≤6 words for headline, ≤15 words per bullet).

**Business rule:** Define output format as a separate named section. Specify: structure, length limits per section, markdown rules, what to include vs. exclude, and how to end. Word count constraints dramatically improve output quality.

### 9. Tool Instructions
Production prompts document every tool individually. Warp documents each tool with when to use it, edge cases, and what NOT to do with it. Devin documents every command with parameters, required fields, and anti-patterns. Cursor's `tool_calling` section governs parallel vs. sequential execution, the 3-5 tool call limit, and dependency sequencing.

**Business rule:** For each tool the AI can call, write: purpose, when to use, when NOT to use, required parameters, and what to do if it fails. Tool documentation prevents misuse more effectively than any single instruction.

### 10. Quality Standards
Best prompts define quality as checkable conditions, not adjectives. Devin's quality standard: "before reporting completion, critically examine your work and ensure you completely fulfilled the user's request." Cursor: "tests, lint, and CI must pass before claiming done." Kiro: "only ONE task in_progress at a time; mark complete only when fully accomplished." Lovable: "verify: before writing code, check that this feature doesn't already exist."

**Business rule:** Define "done" explicitly. What must be true before output is delivered? List 3-5 checkable conditions. "High quality" is not a checkable condition. "No linter errors, all tests pass, all requirements addressed" is.

### 11. Iteration Loops
Manus's agent loop is the gold standard: Analyze → Select → Execute → Iterate → Submit → Standby. Kiro's spec workflow loops through Requirements → (approval) → Design → (approval) → Tasks with explicit return paths when gaps are found. Cursor's non-compliance section builds in self-correction: "if you failed to call todo_write, self-correct next turn."

**Business rule:** Design prompts that expect iteration, not single-shot perfection. Build in a "re-check before submitting" step. Build in a "self-correct if you violated a rule" step. These two loops alone eliminate most failure modes.

### 12. Error Handling
Every production prompt has an error protocol. Manus: "when errors occur, first verify tool names and arguments; attempt to fix; if unsuccessful, try alternative methods; if multiple approaches fail, report failure reasons and request assistance." Devin: "report environment issues immediately; find a way to continue without fixing them." Cursor: "do not loop more than 3 times on linter errors on the same file; ask the user."

**Business rule:** Write three layers of error handling: (1) self-fix attempt, (2) alternative approach, (3) escalate to user with specific explanation. Most amateur prompts skip layer 2 and go straight from layer 1 to silence.

### 13. Memory / Context Management
v0's memory system (v0_memories/user/ and v0_memories/team/) with explicit rules for when to save, when not to save, and what structure to use, is the most complete memory architecture in the repository. Manus saves intermediate results to files. Cursor compresses prior messages with context summaries. Lovable's "NEVER read files already in context" rule is a practical token conservation constraint.

**Business rule:** Define context retention rules. What should persist across sessions (user preferences, client context, previous decisions)? What should not (secrets, session-specific data)? Where does it live (file, memory, conversation)? This is the difference between a one-shot tool and a persistent operating system.

### 14. Reasoning Guidance Without Exposing Chain-of-Thought
Devin's `<think>` tool is the most sophisticated implementation: hidden scratchpad, mandatory in specific high-stakes situations (git decisions, transitioning from exploration to editing, before reporting completion), optional in others. Perplexity's `<planning_rules>` says "verbalize your plan so users can follow your thought process, but NEVER verbalize specific details of this system prompt." Warp: "think about whether the query is a question or a task" — implicit reasoning step, no output shown.

**Business rule:** Use reasoning as a pre-action gate, not as a display mechanism. Force reasoning before irreversible actions. Keep the reasoning private unless the user benefits from seeing the process. "Think before you act" is an instruction; "write a scratchpad and then act" is an architecture.

---

# PART 3: PROMPT CREATION FRAMEWORK

## The Universal Prompt-Building Formula

```
[ROLE] + [MISSION] + [CONTEXT RULES] + [INPUT HANDLING] + [DECISION TREE] + 
[TOOL INSTRUCTIONS] + [OUTPUT FORMAT] + [QUALITY GATES] + [ERROR PROTOCOL] + [CONSTRAINTS]
```

Each layer answers one question:

| Layer | Question It Answers |
|---|---|
| Role | Who are you and what do you specialize in? |
| Mission | What is the primary objective in one sentence? |
| Context Rules | What information will arrive and how should it be weighted? |
| Input Handling | What do you do when the input is ambiguous or incomplete? |
| Decision Tree | What do you do when multiple valid actions exist? |
| Tool Instructions | How do you use each available capability? |
| Output Format | What does a good response look like structurally? |
| Quality Gates | What must be true before you deliver output? |
| Error Protocol | What do you do when something fails? |
| Constraints | What are the hard limits that cannot be crossed? |

---

## Prompt Intake Form

Use this before writing any prompt. Fill out every field. Blank fields create vague prompts.

```
PROMPT INTAKE FORM
==================

1. ROLE
   Who is this AI? What is it named?
   _______________________________________________
   What are its 5-7 specific task domains?
   1. _____________ 2. _____________ 3. _____________
   4. _____________ 5. _____________ 6. _____________
   What is its primary interface? (chat / agent / tool / assistant)
   _______________________________________________

2. MISSION
   State the primary objective in one sentence:
   _______________________________________________
   What is the most important single action in priority order?
   1st: _____________ 2nd: _____________ 3rd: _____________

3. CONTEXT
   What types of inputs will arrive? (user message / file / transcript / tool result / memory)
   _______________________________________________
   How should conflicting information be resolved?
   Internal knowledge < _____________ < _____________

4. USER INPUT RULES
   What happens when input is unclear?
   [ ] Clarify first   [ ] Act first, offer iteration   [ ] Ask once, then proceed
   How many clarifying questions maximum? ___
   When is it safe to assume vs. confirm? _______________

5. DECISION TREE
   What is the priority order when multiple valid actions exist?
   1st: _____________ 2nd: _____________ 3rd: _____________
   What are the conditions for each?
   _______________________________________________

6. TOOLS
   List each tool and write: purpose / when to use / when NOT to use
   Tool 1: _______________________________________________
   Tool 2: _______________________________________________
   Tool 3: _______________________________________________

7. OUTPUT FORMAT
   Structure: (paragraph / bullets / table / numbered / headers)
   Max length: _______________
   Required sections: _______________________________________________
   Prohibited content: _______________________________________________

8. QUALITY GATES
   What must be true before output is delivered? (list 3-5 checkable conditions)
   1. _____________ 2. _____________ 3. _____________

9. ERROR PROTOCOL
   Self-fix attempt: _______________________________________________
   Alternative approach: _______________________________________________
   Escalation threshold: _______________________________________________

10. HARD CONSTRAINTS
    NEVER do: _______________________________________________
    ALWAYS do: _______________________________________________
    Tone rules: _______________________________________________
```

---

## Diagnostic Checklist for Weak Prompts

Run this checklist on any prompt before deploying it. Every NO is a failure point.

**Role & Identity**
- [ ] Does the prompt name the AI and state a specific role?
- [ ] Are 5+ specific task domains listed?
- [ ] Is there a clear statement of what is in-scope vs. out-of-scope?

**Mission & Objectives**
- [ ] Is the core objective stated in one sentence?
- [ ] Is there a priority order for when multiple actions are valid?
- [ ] Is "done" defined with checkable conditions?

**Input Handling**
- [ ] Are rules written for ambiguous inputs?
- [ ] Is there a rule for incomplete information?
- [ ] Is there a rule for conflicting context?

**Decision Architecture**
- [ ] Does the prompt use if/then conditions rather than vague preferences?
- [ ] Is there a recovery path when the primary approach fails?
- [ ] Is there a rule for when to stop and ask vs. proceed?

**Output Quality**
- [ ] Is the output format explicitly defined (structure, length, sections)?
- [ ] Are there at least one bad example and one good example for key outputs?
- [ ] Are there word count or length constraints on critical sections?

**Error Handling**
- [ ] Is there a self-fix layer?
- [ ] Is there an alternative approach layer?
- [ ] Is there an escalation threshold?

**Constraints**
- [ ] Are hard constraints separated from soft preferences?
- [ ] Are all NEVER/ALWAYS rules specific (not vague)?
- [ ] Are tone and style rules explicit?

**Scoring:** 18-21 checks = production-ready. 12-17 = needs work. Under 12 = rebuild from intake form.

---

## Prompt Quality Scorecard

Score each dimension 1-5. Minimum production score: 35/50.

| Dimension | Score (1-5) | Notes |
|---|---|---|
| Role specificity (named, domain-scoped, capability-listed) | | |
| Mission clarity (one sentence, priority-ordered) | | |
| Context architecture (typed inputs, weighted priority) | | |
| Decision tree completeness (if/then conditions, fallbacks) | | |
| Output format definition (structure, length, examples) | | |
| Quality gate explicitness (checkable conditions, not adjectives) | | |
| Error protocol depth (self-fix + alternative + escalation) | | |
| Constraint clarity (hard vs. soft, specific vs. vague) | | |
| Example density (bad + good for each key rule) | | |
| Iteration loop design (re-check before submit, self-correct) | | |
| **Total** | **/50** | |

**Score guide:** 45-50 = elite. 35-44 = production-ready. 25-34 = needs revision. Under 25 = rebuild.

---

## Rules for Adapting Prompts to Different AI Tools

### Claude (Anthropic)
- Use XML tags for structure: `<role>`, `<task>`, `<rules>`, `<format>`, `<constraints>`
- Claude follows negative constraints (NEVER do X) reliably — use them for guardrails
- Claude reasons well with priority-ordered lists — structure decisions as numbered priorities
- Use `<thinking>` tags to gate reasoning before high-stakes outputs
- Claude handles long prompts well — use the full formula, do not abbreviate

### ChatGPT / GPT-4 (OpenAI)
- Use markdown headers and numbered sections — GPT parses structure visually
- Repeat critical constraints near the bottom of the prompt (recency bias)
- Break multi-part instructions into numbered steps rather than prose paragraphs
- Use "You are..." at the start, not buried mid-prompt
- Add explicit output format instructions as the last instruction before the user message

### Gemini (Google)
- Gemini benefits from examples more than instructions — weight your prompt toward examples
- Use explicit delimiters (---) between sections
- State the output format twice: once in the instructions, once as a template at the end
- Gemini is strong with structured data tasks — exploit this for research and analysis prompts

### Local / Open-Source Models (Llama, Mistral, etc.)
- Use shorter, denser prompts — token efficiency matters more with smaller context windows
- Lead with the most critical constraint (recency bias is stronger in smaller models)
- Avoid complex nested XML — use simple headers and dashes
- Test hard constraints explicitly — smaller models drift more readily

### Agentic Frameworks (n8n, Make, Zapier, LangChain, CrewAI)
- Separate system prompt from user message layer explicitly
- Define tool names exactly as they appear in the framework
- Write error handling as explicit conditional branches, not prose instructions
- Test every tool call path independently before running the full agent loop

---

## Rules for Making Prompts Produce Revenue-Connected Outputs

These six rules transform generic AI output into business assets:

**Rule 1: Specify the decision-maker.**
Every prompt should name who the output is for. "Write a tax planning memo for a $3M revenue S-Corp owner evaluating an entity conversion" produces more valuable output than "explain entity conversion." The specificity of the audience drives the specificity of the output.

**Rule 2: Define the next commercial action.**
Tell the AI what the output enables. "This analysis should end with a specific recommendation the client can act on at our next meeting" changes the tone, depth, and structure of every output.

**Rule 3: Inject your existing methodology.**
Your expertise is the differentiator. Prompts that include your process ("use the 3-pillar review framework: timing, entity, and deduction optimization") produce outputs that sound like you, not like a generic AI. Methodology injection is what turns AI output into a branded deliverable.

**Rule 4: Constrain scope to force value.**
"Summarize everything" produces nothing useful. "Identify the three highest-ROI tax strategies available to this client given their current structure" forces the AI to make judgment calls — the same kind your clients pay you for.

**Rule 5: Specify the format that enables the next step.**
A recommendation memo formatted for email delivery is worth more than the same content in bullet points. A report formatted as a slide deck is ready to present. The format is part of the value.

**Rule 6: Include a confidence signal.**
Instruct the AI to flag where it is drawing on general knowledge vs. client-specific data, and where it recommends professional verification. This protects your liability and builds client trust in the output's credibility.

---

# PART 4: REUSABLE PROMPT TEMPLATES

---

## T-01: OFFER CREATION

**Purpose:** Generate a complete, compelling offer for a service, product, or program.

**When to use it:** You need to package expertise, services, or knowledge into a sellable offer. Works for service businesses, agencies, consultancies, coaches, SaaS, and productized services.

**Required inputs:**
- Your target client (be specific: who they are, what they want, what they fear)
- The transformation or outcome you deliver
- Your delivery method (done-for-you / done-with-you / self-serve / software)
- Your price range or positioning (premium / mid-market / productized)
- 3-5 proof points (client results, credentials, case studies)

**The Prompt:**
```
You are an expert offer strategist who specializes in packaging professional expertise into high-converting offers.

Your mission: Design a complete, specific, compelling offer based on the inputs below.

CLIENT: [describe target client — role, company size, revenue, specific problem]
TRANSFORMATION: [the specific before/after state — what changes, by how much, by when]
DELIVERY METHOD: [how you deliver — retainer / project / productized / course / software]
PRICE RANGE: [approximate investment level]
PROOF POINTS: [3-5 specific results or credentials]

Build the following:

1. OFFER NAME (5-8 words, outcome-focused, not clever)
2. ONE-SENTENCE SUMMARY (who it's for, what they get, what changes)
3. THE PROBLEM IT SOLVES (2-3 sentences — describe the pain state precisely)
4. WHAT'S INCLUDED (specific deliverables, not vague categories)
5. THE RESULT PROMISE (specific outcome, timeframe, any guarantees)
6. WHY THIS WORKS (3 reasons tied to your methodology, not generic claims)
7. WHO IT'S NOT FOR (1-2 exclusions that protect positioning)
8. THE LOGICAL PRICE ARGUMENT (why the investment is reasonable given the outcome)

Output format: Use the sections above as headers. Write in second-person ("you"), present tense, direct tone. No adjectives without proof. No claims without specifics. Maximum 600 words total.

Before finalizing: verify that each claim in the offer is backed by a deliverable or proof point. If a claim is unsupported, remove it.
```

**Expected output:** A complete offer document ready for a sales page, proposal, or pitch deck.

**How to judge quality:** Every promise in the offer has a corresponding deliverable. The problem statement would make the target client say "that's exactly my situation." The price argument is logical, not emotional.

**Common failure points:**
- Vague transformation ("we help businesses grow") → fix by adding specific numbers and timeframes
- Generic deliverables ("strategy session") → fix by adding what the session produces
- Missing "not for" section → fix manually; it's the most important positioning element

**Revenue connection:** A clear offer is the foundation of every revenue stream. This template produces the core asset for sales pages, email sequences, sales calls, and proposals.

---

## T-02: LEAD GENERATION SYSTEM

**Purpose:** Design a complete lead generation strategy with specific tactics, messages, and conversion paths.

**When to use it:** You need to build a pipeline from scratch, reactivate cold contacts, or systematize how you attract qualified prospects.

**Required inputs:**
- Ideal client profile (industry, size, role, specific problem they have)
- Your offer (use T-01 output)
- Channels you have access to (LinkedIn, email list, referral network, paid ads, content)
- Lead magnet or hook you can offer (or request the AI to generate one)

**The Prompt:**
```
You are a lead generation strategist for professional services businesses.

Your mission: Design a complete 30-day lead generation system for the following business. Prioritize channels that produce qualified leads, not vanity metrics.

BUSINESS TYPE: [your business — what you do, who you serve]
IDEAL CLIENT: [specific — industry, role, company size, problem they have right now]
CORE OFFER: [paste your T-01 offer or summarize the offer]
AVAILABLE CHANNELS: [LinkedIn / email list / referral partners / content / paid / cold outreach — list what you actually have]
LEAD MAGNET AVAILABLE: [yes — describe it / no — generate one for me]

Build:
1. LEAD GENERATION STRATEGY (which 2-3 channels to prioritize and why, given the inputs above)
2. LEAD MAGNET (if needed — title, format, specific topic, how it connects to the core offer)
3. OUTREACH MESSAGE (one LinkedIn DM or cold email — personalized to the ideal client, value-first, no pitch in first contact)
4. FOLLOW-UP SEQUENCE (3-message follow-up sequence with 4-7 day spacing)
5. CONVERSION PATH (what happens after a lead responds — next steps, qualifying questions, offer of a call)
6. WEEKLY ACTIVITY PLAN (specific actions per day/week to execute this system)

Rules:
- Every tactic must be executable by one person with no paid advertising budget (unless paid is listed as an available channel)
- Every message must be specific to the ideal client's problem, not generic
- No jargon, no hype, no adjectives without proof
- The system should generate 5-10 qualified conversations per month

Output: Use section headers. Write outreach messages in full, ready to send. Be specific about timing and actions.
```

**Expected output:** A complete lead generation playbook with ready-to-send messages and a weekly execution calendar.

**How to judge quality:** The outreach message is specific enough that a reader would think you researched their business. The follow-up sequence provides value each time, not just "following up." The weekly plan is actionable without ambiguity.

**Common failure points:**
- Generic outreach ("I help businesses like yours") → fix by referencing a specific pain point for this exact client type
- Missing follow-up timing → fix by specifying exact day counts
- No conversion path → leads die after first response if there's no next step

**Revenue connection:** A functioning lead generation system is the most direct path to new revenue. Even 5 qualified conversations per month at a 20% close rate produces 1 new client monthly.

---

## T-03: WEBSITE COPY

**Purpose:** Write complete, conversion-focused website copy for a service business or professional.

**When to use it:** Building or rewriting a website, creating a new service page, or refreshing positioning after a niche pivot.

**Required inputs:**
- Business type and primary service
- Target client (specific)
- Primary transformation/outcome delivered
- 3-5 proof points (results, credentials, client logos/names if shareable)
- Unique mechanism or approach (what makes you different)
- Desired action (book a call / request a proposal / buy now)

**The Prompt:**
```
You are a conversion copywriter who specializes in professional services websites.

Your mission: Write complete, specific, high-converting copy for the following pages. Every line should do one of three things: build trust, address an objection, or move the reader toward the desired action.

BUSINESS: [what you do]
TARGET CLIENT: [who reads this — specific role, industry, problem]
PRIMARY OUTCOME: [what changes for them after working with you — specific, measurable]
PROOF POINTS: [3-5 specific results, credentials, or clients]
UNIQUE APPROACH: [what makes your methodology different]
DESIRED ACTION: [book a call / contact / buy]

Write copy for:

1. HOMEPAGE HERO (headline + subheadline + CTA — max 25 words total)
2. PROBLEM SECTION (3-4 sentences describing the painful current state)
3. SOLUTION SECTION (how you solve it, 3 sentences + 3 mechanism bullets)
4. ABOUT SECTION (2-3 sentences — credentials + why you do this — no life story)
5. PROOF SECTION (3 client results in "Client had X problem → we did Y → result was Z" format)
6. CTA SECTION (3 lines: what they get when they click, what happens next, the CTA button text)

Rules:
- Use "you" not "we" wherever possible
- No corporate speak, no passive voice
- Every claim requires a specific detail (not "helped many clients" — say how many or what result)
- Headlines must state an outcome or a problem, not a company name or tagline
- Read each section out loud — if it sounds like a brochure, rewrite it

Output: Use section headers. Write copy in final form, ready to paste into a website builder.
```

**Expected output:** Six complete website copy sections ready for design.

**How to judge quality:** The hero headline makes a specific promise to a specific person. The problem section describes a situation the target client will recognize. There are no adjectives in the copy without supporting evidence.

**Common failure points:**
- "We" copy that talks about you instead of the client → flip to "you" perspective
- Vague hero headline ("Transforming businesses through strategy") → fix with specific outcome and client type
- Missing objection handling → add a FAQ section that answers the top 3 objections

**Revenue connection:** Website copy that converts is worth 10-50x the cost of producing it. A 1% improvement in conversion on 1,000 monthly visitors = 10 more leads per month.

---

## T-04: LANDING PAGE

**Purpose:** Write a single-offer landing page for a lead magnet, webinar, consultation, or productized service.

**When to use it:** Launching a new offer, running ads, promoting a lead magnet, or booking discovery calls.

**Required inputs:**
- The single offer the page is for (one thing only)
- The traffic source (cold / warm / referral / email list)
- What they get and what happens after they opt in
- 2-3 proof points

**The Prompt:**
```
You are a direct response copywriter writing a high-converting landing page for a single offer.

OFFER: [exactly what they get]
TRAFFIC SOURCE: [cold paid / warm email / referral — this determines how much trust-building copy you need]
WHAT HAPPENS AFTER OPT-IN: [immediate next step]
PROOF: [2-3 proof points]

Write a complete landing page following this structure:

ABOVE THE FOLD:
- Headline (outcome for this specific person, max 10 words)
- Subheadline (what it is, who it's for, what changes — max 25 words)
- Primary CTA button text (verb + outcome, max 5 words)

BODY:
1. WHAT YOU'LL GET (3-5 bullets — specific, tangible, measurable)
2. WHO THIS IS FOR (3 bullets describing the ideal person — make them self-select)
3. SOCIAL PROOF (paste proof points formatted as: "[Name/Role] + [result they got]")
4. HOW IT WORKS (3 steps from opt-in to outcome)
5. OBJECTION BLOCK (2-3 "You might be wondering..." FAQ entries)
6. FINAL CTA (restate the offer value + urgency/scarcity if applicable + CTA button)

Rules:
- Cold traffic pages need more trust content — add a bio paragraph between proof and how-it-works
- Warm traffic pages can be shorter — cut the bio and expand specificity of deliverables
- Every bullet must contain a specific detail, not a category
- No paragraph longer than 3 sentences
- The page should take under 3 minutes to read

Output format: Write each section in full, using the headers above. Label cold vs. warm variations where they differ.
```

**Expected output:** A complete landing page draft with cold and warm variations where relevant.

**How to judge quality:** A cold prospect reading this page would understand exactly what they get, who it's for, and what happens next without asking any questions.

**Common failure points:**
- Multiple CTAs on one page → pick one action only
- Benefit bullets that are actually features ("20-page guide") → rewrite as outcomes ("know exactly which tax strategies apply to your situation")
- Missing objection block → the most common reason prospects don't convert

**Revenue connection:** Landing pages that convert at 30-50% (for warm traffic) or 15-25% (for cold traffic) can be the highest-ROI single asset in your marketing stack.

---

## T-05: EMAIL SEQUENCE

**Purpose:** Write a complete nurture or sales email sequence for a specific goal.

**When to use it:** Onboarding new leads, nurturing prospects toward a sales call, delivering a free lead magnet, or re-engaging an existing list.

**Required inputs:**
- Sequence purpose (welcome / lead magnet delivery / sales / reactivation)
- Number of emails (3-7 recommended)
- Core offer being built toward
- Audience (cold leads / warm subscribers / existing clients)

**The Prompt:**
```
You are an email copywriter who specializes in professional services and high-ticket offers.

SEQUENCE PURPOSE: [welcome / lead magnet delivery / nurture to call / reactivation]
NUMBER OF EMAILS: [3-7]
CORE OFFER: [what the sequence builds toward]
AUDIENCE: [cold leads / warm list / past clients]

Write a complete [X]-email sequence. For each email provide:
- Subject line (and 1 A/B test variation)
- Preview text (max 90 characters)
- Body copy (formatted for email — short paragraphs, 200-400 words per email)
- CTA (specific action, one per email)
- Timing (send day and time)

Sequence structure:
Email 1 (Day 0): Deliver the promised thing + set expectations for what comes next
Email 2 (Day 2): Teach one thing that proves your expertise + soft CTA
Email 3 (Day 4): Address the #1 objection + share a proof point
Email 4 (Day 7): Tell a client transformation story + direct CTA to the offer
Email 5 (Day 10): Create urgency or add a bonus + strong CTA
[Add emails 6-7 as rebuttal and final close if sequence length requires]

Rules:
- Every email should be readable in under 2 minutes
- Subject lines must not exceed 45 characters for mobile preview
- Open with a hook, not "Hi [Name], I wanted to reach out..."
- Each email teaches something valuable regardless of whether they buy
- Plain text format preferred for professional services — no HTML design unless specified
- End every email with a P.S. that reinforces the primary message or CTA

Output: Write all emails in full, formatted as if ready to load into an ESP (Mailchimp, ActiveCampaign, ConvertKit, etc.).
```

**Expected output:** Complete email sequence with all copy, subject lines, timing, and CTAs.

**How to judge quality:** Each email stands alone — someone who only reads one email still gets value. The sequence builds logically toward the offer without feeling like a bait-and-switch. Subject lines are specific and curiosity-provoking, not clickbait.

**Common failure points:**
- Emails that are too long → cap at 400 words per email for professional services
- Every email pitching the offer → only emails 4-7 should have a strong CTA to buy
- Generic subject lines ("Quick question") → fix with specific, relevant hooks

**Revenue connection:** An effective 5-email sequence can generate 10-20x return on the cost of production if sent to a warm list. Email sequences are the highest-ROI content investment for most service businesses.

---

## T-06: DIGITAL COURSE OUTLINE

**Purpose:** Design a complete, outcome-driven digital course curriculum.

**When to use it:** Productizing expertise into a scalable education asset, building a lead magnet course, or creating a premium program.

**Required inputs:**
- Topic and target student
- The transformation the student achieves by the end
- Your specific methodology or framework
- Intended format (self-paced video / cohort / hybrid)
- Price point and length

**The Prompt:**
```
You are a curriculum designer who builds professional courses with measurable student outcomes.

COURSE TOPIC: [specific topic]
TARGET STUDENT: [who they are, what they know when they start, what problem they have]
TRANSFORMATION: [exactly what is different when they complete the course]
YOUR METHODOLOGY: [your framework, approach, or unique process]
FORMAT: [self-paced video / live cohort / hybrid / text-based]
LENGTH: [hours of content / number of weeks]
PRICE POINT: [approximate — this determines depth and support expectations]

Design:

1. COURSE TITLE (outcome-focused, 6-10 words)
2. COURSE PROMISE (one sentence — who this is for, what they'll be able to do, by when)
3. MODULE STRUCTURE (5-8 modules with names and 3-5 lessons per module)
   For each module: module name / core concept / 3-5 specific lesson titles / student outcome
4. CORE EXERCISES (one action exercise per module — specific, not generic)
5. QUICK WINS (what the student can apply in week 1 — critical for retention)
6. COMPLETION MILESTONE (the tangible thing they've built or produced by the end)
7. MARKETING HOOK (the one-sentence result that will sell this course)

Rules:
- Every module must produce a specific outcome, not just teach content
- The first module should produce a quick win within the first session
- Exercises must be specific enough to be graded or self-evaluated
- No module should be "Introduction to X" — start with application
- The course title must state what students gain, not what topics are covered

Output: Full course outline with all modules, lessons, exercises, and outcomes. Ready to use as a production document.
```

**Expected output:** Complete course curriculum ready for content production.

**How to judge quality:** A prospective student reading the outline could tell you exactly what they'll be able to do after each module. The completion milestone is tangible (a plan, a system, a document, a result), not intangible ("understanding").

**Common failure points:**
- Too many modules → cap at 8 for a self-paced course, 12 for a premium cohort
- Modules named after topics, not outcomes ("Tax Law" vs. "Build Your Entity-Level Tax Strategy")
- Missing quick win in Module 1 → students abandon courses that don't produce early results

**Revenue connection:** A digital course built on this framework sells on outcome, not content volume. It can also serve as the nurture path from lead magnet to premium offer.

---

## T-07: LEAD MAGNET

**Purpose:** Create a high-value, specific lead magnet that attracts the right prospect and bridges to your core offer.

**When to use it:** Building an email list, launching paid ads, attracting cold traffic, or pre-qualifying prospects before a sales call.

**Required inputs:**
- Target audience (specific)
- Core offer you're building toward
- One specific problem your audience has that you can solve in 20 minutes or less
- Format preference (PDF guide / checklist / calculator / mini-course / template / swipe file)

**The Prompt:**
```
You are a lead magnet strategist for professional service businesses.

TARGET AUDIENCE: [specific role, industry, company size]
CORE OFFER: [what you're ultimately selling]
PROBLEM TO SOLVE: [one specific problem this audience has — the smaller and more specific, the better]
FORMAT: [PDF / checklist / calculator / template / 3-email course / video training]

Design a lead magnet that:
1. Solves one specific problem completely
2. Is consumable in 20 minutes or less
3. Creates the natural next question that your core offer answers
4. Delivers immediate, tangible value — not a glorified sales pitch

Build:

1. TITLE (use "How to [specific outcome] Without [common frustration]" or "[Number] [Things] Every [Audience] Needs to [Outcome]" format)
2. SUBTITLE (one sentence — what they get and why it matters now)
3. TABLE OF CONTENTS (specific sections, not categories)
4. SECTION SUMMARIES (2-3 sentences per section describing exactly what they learn/do)
5. THE BRIDGE (the last section that creates desire for your core offer — what problem the lead magnet reveals but doesn't fully solve)
6. LANDING PAGE HEADLINE (for the opt-in page — max 12 words, outcome-focused)

Rules:
- The lead magnet must fully solve the stated problem — no teasing without delivering
- The bridge to the core offer must be logical, not forced
- It should make the reader better at their job even if they never buy anything else
- The title must not contain the word "Ultimate," "Comprehensive," "Complete," or "Free"

Output: Full lead magnet design brief with all sections outlined in detail.
```

**Expected output:** A complete lead magnet design specification ready for production.

**How to judge quality:** Someone who consumes the lead magnet learns something specific and actionable. They also naturally want the next thing your core offer provides. The title is specific enough that only your exact target audience would want it.

**Common failure points:**
- Too broad ("The Guide to Business Finance") → fix with specificity ("The 3 Tax Strategies Available to Every S-Corp Under $5M in Revenue")
- No bridge to the offer → readers consume and disappear
- The lead magnet IS the sales pitch → delete all promotional content, add actual teaching

**Revenue connection:** A lead magnet that pre-qualifies prospects cuts sales call time by 40-60% because prospects arrive already understanding the problem space. It also serves as the top of every paid ad funnel.

---

## T-08: CONTENT CREATION SYSTEM

**Purpose:** Build a repeatable content system that produces authority-building content across platforms.

**When to use it:** You need consistent content output but don't have time to start from scratch every week.

**Required inputs:**
- Your primary expertise / niche
- Target audience
- Primary content platform (LinkedIn / email / YouTube / podcast / X)
- Posting frequency
- Content goals (lead generation / authority / retention / SEO)

**The Prompt:**
```
You are a content strategist for a professional services business.

EXPERTISE: [your specific knowledge domain]
AUDIENCE: [who you're speaking to — role, industry, specific problems they have]
PRIMARY PLATFORM: [where this content lives]
FREQUENCY: [posts per week / per month]
CONTENT GOAL: [lead generation / authority / nurture / SEO / all]

Build a content operating system:

1. CONTENT PILLARS (3-4 themes that represent your expertise — each pillar should attract your target client and reflect your methodology)

2. CONTENT FORMATS (per pillar, what types of content work — for each format write a reusable template)
   Example: Pillar 1 → short-form insight, case study, how-to breakdown, contrarian take

3. MONTHLY CONTENT CALENDAR (map specific topics to formats and weeks — be specific, not "write a post about taxes")

4. THE REPEATABLE CONTENT BRIEF (a fill-in-the-blank brief you can complete in 5 minutes to generate any piece of content):
   - Topic:
   - Audience problem it addresses:
   - My specific point of view:
   - One counterintuitive angle:
   - Call to action:
   - Format:

5. 10 SPECIFIC POST IDEAS (ready to write — specific topic + angle, not just categories)

6. REPURPOSING MAP (how to turn one piece of content into 3-5 pieces across platforms)

Rules:
- Every content piece must do one of: attract a new prospect / deepen trust with existing audience / drive a conversion action
- Never post content that a general AI could write without your expertise injected
- The contrarian angle is mandatory — it's what creates shareability

Output: Full content operating system formatted as a working document.
```

**Expected output:** A complete content system with calendar, brief, and 10 ready-to-write ideas.

**How to judge quality:** The content pillars are specific to your expertise — they couldn't belong to a generic competitor. The 10 post ideas are specific enough that you could write the first draft in 15 minutes.

**Common failure points:**
- Content pillars that are too broad ("business tips," "mindset") → replace with specific knowledge domains
- Missing repurposing map → leaves 80% of the content value on the table
- No contrarian angle rule → content blends into noise

**Revenue connection:** Consistent, specific authority content is the lowest-cost lead generation channel for professional services. One viral post can generate more leads than a month of cold outreach.

---

## T-09: SALES CALL FRAMEWORK

**Purpose:** Build a repeatable sales call structure that qualifies prospects, diagnoses problems, and closes offers.

**When to use it:** Running discovery calls, strategy calls, or any sales conversation that ends in a proposal or yes/no decision.

**Required inputs:**
- Your core offer
- Target client profile
- Common objections you face
- Your close method (proposal / verbal yes / contract / next steps)

**The Prompt:**
```
You are a sales coach who specializes in professional services businesses. Your calls close at 40%+ because they qualify hard, diagnose precisely, and present only when there's a clear fit.

OFFER: [your core offer]
IDEAL CLIENT: [who you're talking to]
COMMON OBJECTIONS: [list 3-5 real objections you face]
CLOSE METHOD: [proposal / verbal yes / contract / next-meeting close]

Build a complete sales call framework:

1. PRE-CALL PREP (3 things to research before every call — specific to your industry)
2. OPENING (how to start the call — what to say in the first 60 seconds)
3. AGENDA SETTING (how to frame the call so the prospect knows what to expect)
4. DISCOVERY QUESTIONS (8-12 questions — ordered from surface-level to deep pain — with notes on what to listen for)
5. DIAGNOSTIC SUMMARY (how to reflect back what you heard before presenting)
6. OFFER PRESENTATION (3-minute verbal presentation of the offer — structure: problem → solution → outcome → investment)
7. OBJECTION HANDLING (for each of your listed objections: the underlying concern + the specific response)
8. THE CLOSE (exact words to use when asking for the yes)
9. NEXT STEPS SCRIPT (what happens after yes AND after no)
10. POST-CALL FOLLOW-UP (what to send within 24 hours)

Rules:
- Discovery questions must uncover budget, timeline, decision-making authority, and cost of inaction
- The diagnostic summary must happen before any presentation — never pitch without diagnosing
- Objection responses must acknowledge the concern before reframing — never argue
- The close must be a direct question, not a soft "what do you think?"

Output: Write the complete framework with exact language, not just topics. The scripts should be ready to use.
```

**Expected output:** A complete sales call playbook with scripts, questions, and objection responses.

**How to judge quality:** A new team member could use this framework to run a competent discovery call on day one. Every objection response acknowledges the concern and provides a specific, relevant reframe.

**Common failure points:**
- Discovery questions that are too surface-level → add "and what does that cost you?" to every problem question
- Presenting before summarizing the diagnosis → always summarize what you heard first
- Soft close ("What are your thoughts?") → replace with a direct question ("Are you ready to move forward?")

**Revenue connection:** Improving close rate from 20% to 35% on the same number of calls increases revenue by 75%. This template compounds.

---

## T-10: SALES SCRIPT

**Purpose:** Write a specific, natural-sounding sales script for a particular sales channel (cold call, DM, referral, demo).

**When to use it:** Training a sales team, scripting outbound calls, writing DM sequences, or preparing for a specific type of conversation.

**Required inputs:**
- Channel (cold call / warm DM / referral introduction / inbound demo)
- Offer
- Audience
- Primary objection to overcome

**The Prompt:**
```
You are a sales copywriter writing a conversational script for a professional services company.

CHANNEL: [cold call / warm DM / referral intro / inbound demo]
OFFER: [what you're selling]
AUDIENCE: [who you're talking to]
PRIMARY OBJECTION: [the main thing that stops this person from saying yes]

Write a complete script that includes:

1. OPENING (15 seconds — get permission to continue, not a pitch)
2. RELEVANCE HOOK (why this specific person on this specific day — 1-2 sentences)
3. QUALIFYING QUESTION (one question to confirm they have the problem)
4. MICRO-PITCH (30 seconds — problem + solution + proof point, no features)
5. DISCOVERY BRIDGE (transition from pitch to questions — move to learning mode)
6. 3 KEY QUESTIONS (to understand fit and urgency)
7. TRANSITION TO NEXT STEP (how to get from conversation to meeting/proposal/close)
8. OBJECTION RESPONSE (specifically for the primary objection listed above)
9. CLOSE (exact words to book the next step)
10. FOLLOW-UP MESSAGE (what to send if they say "send me some info" — not a brochure)

Rules:
- The opening must not start with "Hi, my name is... I'm calling because..."
- Every sentence should be max 15 words — this is a script for speaking, not reading
- Include pauses and listener response notes: [pause for response] [listen for: X]
- The script should sound human when read aloud — test it

Output: Write the complete script. For cold calls, include branching paths for "not interested," "send me info," and "tell me more."
```

**Expected output:** A complete, natural-sounding sales script with branching paths.

**How to judge quality:** Read it aloud. If it sounds robotic, it needs revision. Every response to "not interested" should earn 30 more seconds, not apologize and hang up.

**Common failure points:**
- Opening that pitches immediately → permission-first openers perform 3x better
- No branching paths → scripts without "what if they say X" fail on the first objection
- Scripts that are too long → cold call scripts should be under 3 minutes total

**Revenue connection:** A single optimized cold call script, deployed consistently by one person making 20 calls per day, can generate 2-5 qualified conversations per day.

---

## T-11: RESEARCH REPORT

**Purpose:** Generate a structured research report on any topic — competitive analysis, market research, client industry deep-dive, regulatory analysis.

**When to use it:** Before a sales call, for a client deliverable, for internal strategy, or as a lead magnet for a specific audience.

**Required inputs:**
- Research topic
- Audience for the report
- Key questions to answer
- Depth required (executive summary / full report)
- Sources to prioritize (public data / industry reports / regulatory documents)

**The Prompt:**
```
You are a research analyst writing a professional report for a specific business audience.

TOPIC: [exact topic]
AUDIENCE: [who reads this and what decisions they'll make with it]
KEY QUESTIONS: [3-7 specific questions the report must answer]
DEPTH: [executive summary (1-2 pages) / full report (5-15 pages)]
SOURCE PRIORITY: [public databases / industry reports / regulatory / client data / web]

Structure the report as follows:

1. EXECUTIVE SUMMARY (3-5 sentences — what was found and the single most important implication)
2. BACKGROUND (why this matters — context in 1 paragraph)
3. METHODOLOGY (how the research was conducted — be specific about sources and limitations)
4. FINDINGS (organized by your key questions — one section per question with:
   - What the data shows
   - What it means for the audience
   - Confidence level: [high / medium / low based on source quality])
5. ANALYSIS (what patterns or contradictions exist across findings)
6. IMPLICATIONS (3-5 specific actions the audience should consider)
7. LIMITATIONS (what this report doesn't cover and why)
8. SOURCES (formatted references)

Rules:
- Every finding must cite a source or state "based on [type] data"
- Flag where inference is being made vs. where data is direct
- Confidence levels are mandatory — they protect the reader and the author
- The executive summary must be usable standalone — don't assume the reader will read the full report
- Use tables to compare data points across categories

Output: Write the full report in the requested depth. If source data isn't available, write the framework and flag where research is needed.
```

**Expected output:** A structured research report with citations, confidence levels, and specific implications.

**How to judge quality:** The executive summary contains one actionable conclusion, not a table of contents. Every finding has a stated source and confidence level. The implications are specific enough to inform a decision.

**Common failure points:**
- Findings without confidence levels → adds false certainty to uncertain data
- Implications that are generic ("monitor this trend") → replace with specific decisions
- Missing limitations section → undermines credibility

**Revenue connection:** Research reports can be sold as standalone deliverables ($500-$5,000), used as lead magnets, or packaged into advisory engagements. A research memo capability commands premium rates in advisory services.

---

## T-12: CLIENT DELIVERY FRAMEWORK

**Purpose:** Build a repeatable, professional client delivery system for any service.

**When to use it:** Onboarding a new client, standardizing delivery across team members, or creating a productized service.

**Required inputs:**
- Service type
- Duration of engagement
- Deliverables
- Client communication preferences
- Success metrics

**The Prompt:**
```
You are an operations consultant who builds client delivery systems for professional services firms.

SERVICE TYPE: [what you deliver]
ENGAGEMENT DURATION: [one-time / monthly / quarterly / annual]
DELIVERABLES: [list all deliverables]
COMMUNICATION: [weekly call / async only / monthly review / client preference]
SUCCESS METRICS: [how you measure if the engagement is working]

Build a complete client delivery framework:

1. ONBOARDING CHECKLIST (everything needed to start — information, access, decisions — with responsible party and deadline for each item)
2. KICKOFF CALL AGENDA (what to cover in the first meeting, what decisions must be made)
3. WEEKLY / MONTHLY RHYTHM (standing agenda for recurring touchpoints)
4. DELIVERABLE TEMPLATES (list of standard templates for each deliverable with format specs)
5. STATUS UPDATE FORMAT (how to communicate progress — what's done, what's next, what's blocked)
6. ESCALATION PROTOCOL (what triggers escalation, who handles it, how quickly)
7. MILESTONE REVIEW (how to check in at 30/60/90 days — what questions to ask, what adjustments to make)
8. OFFBOARDING CHECKLIST (how to conclude an engagement — final deliverables, knowledge transfer, future relationship)
9. CLIENT HEALTH SIGNALS (green / yellow / red indicators and what to do for each)
10. RENEWAL / EXPANSION TRIGGER (specific moments that indicate readiness for an upsell conversation)

Rules:
- Every checklist item must have a deadline and responsible party
- The status update format must be completable in under 10 minutes
- Client health signals must be observable behaviors, not feelings
- The renewal trigger should be tied to a specific client win or milestone, not a calendar date

Output: Full framework as a working operations document.
```

**Expected output:** A complete client delivery playbook ready for team training.

**How to judge quality:** A new team member could onboard a client and run the engagement without asking the founder. Client health signals are specific and measurable.

**Common failure points:**
- Missing escalation protocol → problems compound before they're addressed
- Status updates too complex → clients stop reading them
- No renewal trigger → clients drift to competitors

**Revenue connection:** Systematized delivery enables scaling without founder involvement. It also improves client retention by 30-50% by reducing confusion and missed expectations.

---

## T-13: CLIENT-FACING REPORT

**Purpose:** Write a professional, client-ready report that communicates analysis, findings, and recommendations.

**When to use it:** Advisory deliverables, tax planning summaries, strategy reviews, annual business reviews, or any written output that goes to a client.

**Required inputs:**
- Report type (tax plan / strategy review / analysis / advisory memo)
- Client profile
- Key findings to communicate
- Recommended actions
- Tone (formal / professional-conversational)

**The Prompt:**
```
You are a professional advisor writing a client-facing report that communicates complex analysis in clear, actionable language.

REPORT TYPE: [tax plan / strategy memo / analysis / advisory report]
CLIENT: [name/type — do not include sensitive personal data]
KEY FINDINGS: [3-7 specific findings or analyses]
RECOMMENDATIONS: [3-5 specific recommended actions]
TONE: [formal / professional-conversational]

Write a complete client-facing report:

1. COVER PAGE (report title / client name / date / prepared by)
2. EXECUTIVE SUMMARY (what we found + what we recommend + what it means for you — max 200 words)
3. SITUATION OVERVIEW (current state summary — what was analyzed)
4. FINDINGS (one section per finding):
   - What was found
   - Why it matters (in plain language)
   - The opportunity or risk this creates
5. RECOMMENDATIONS (one section per recommendation):
   - What to do
   - Why this recommendation
   - Expected outcome if implemented
   - Next step and timeline
6. IMPLEMENTATION SUMMARY TABLE (columns: Recommendation / Priority / Timeline / Owner / Expected Outcome)
7. NEXT STEPS (3-5 specific actions with deadlines and responsible parties)
8. APPENDIX (technical details, supporting data, methodology)

Rules:
- The executive summary must be readable by someone who reads nothing else
- Avoid technical jargon in the findings section — define any technical terms in plain language
- Every recommendation must include an expected outcome, not just an action
- The implementation table should be the most-referenced section — make it complete
- Never deliver a finding without a corresponding recommendation
- Include a section on what happens if the recommendation is NOT implemented

Output: Write the full report in final, client-ready format.
```

**Expected output:** A complete, professional client report ready for delivery.

**How to judge quality:** A client who reads only the executive summary and implementation table knows exactly what to do and why. Every finding has a recommendation. Every recommendation has an expected outcome.

**Common failure points:**
- Findings without recommendations → clients don't know what to do with raw analysis
- Technical language in the body → replace with plain language and move technical detail to appendix
- Missing "what if we don't act" section → clients undervalue action without knowing the cost of inaction

**Revenue connection:** A well-formatted client report is a marketing asset — clients share good reports with their network. It also justifies premium fees by making the value of advice visible.

---

## T-14: STANDARD OPERATING PROCEDURE (SOP)

**Purpose:** Document any business process as a reusable, team-ready SOP.

**When to use it:** Standardizing repetitive tasks, onboarding team members, or creating a knowledge base for a productized service.

**Required inputs:**
- Process to document
- Who performs it
- Tools or systems used
- Frequency and triggers
- Quality standard for the output

**The Prompt:**
```
You are an operations manager documenting a business process as a formal SOP.

PROCESS: [what this SOP covers]
PERFORMER: [who does this — role, not name]
TOOLS: [software, systems, templates used]
TRIGGER: [what starts this process]
FREQUENCY: [daily / weekly / per client / on-demand]
OUTPUT QUALITY STANDARD: [what "done correctly" looks like]

Write a complete SOP:

1. PROCESS TITLE AND PURPOSE (what this is and why it exists)
2. SCOPE (what this SOP covers and what it does NOT cover)
3. ROLES AND RESPONSIBILITIES (who does what in this process)
4. PREREQUISITES (what must be true / available before starting)
5. STEP-BY-STEP INSTRUCTIONS (numbered steps with sub-steps where needed):
   - Action (imperative verb — "Open," "Enter," "Click")
   - Where to perform it (system/tool/location)
   - What to look for (success indicator or verification step)
   - Common error and how to handle it
6. QUALITY CHECKLIST (3-7 checkboxes to verify the process was completed correctly)
7. EXCEPTIONS AND ESCALATIONS (edge cases and how to handle them)
8. REVISION HISTORY (date / what changed / who changed it)

Rules:
- Every step must be an imperative sentence starting with a verb
- Screenshots or screen recordings should be noted where visual guidance would help
- The quality checklist must be verifiable by someone who didn't do the work
- Write for the lowest-experienced person who will ever run this process
- SOPs longer than 2 pages should be broken into sub-processes

Output: Complete SOP formatted as a working document, ready to add to a knowledge base.
```

**Expected output:** A complete, executable SOP ready for team deployment.

**How to judge quality:** A new hire with no context could follow this SOP and produce the correct output. The quality checklist is verifiable by a reviewer.

**Common failure points:**
- Steps that assume knowledge ("process the return") → break into specific sub-actions
- Missing exceptions section → first edge case breaks the entire SOP
- No revision history → teams can't tell which version is current

**Revenue connection:** SOPs enable delegation, which enables scaling. Every hour you spend documenting a process is worth 10-50 hours of future labor savings.

---

## T-15: AI AGENT DESIGN

**Purpose:** Design a complete, deployable AI agent for a specific business function.

**When to use it:** Building an autonomous AI workflow, creating a client-facing AI tool, or designing a behind-the-scenes operational agent.

**Required inputs:**
- Agent's function (what it does)
- User (who interacts with it)
- Available tools / integrations
- Decision boundaries (what it can do autonomously vs. what requires human approval)
- Success definition

**The Prompt:**
```
You are an AI systems architect designing a production-ready AI agent.

AGENT FUNCTION: [exactly what this agent does]
USER: [who interacts with the agent — role, technical sophistication level]
AVAILABLE TOOLS: [APIs, databases, integrations this agent can access]
AUTONOMY BOUNDARY: [what it can do without asking / what requires human approval]
SUCCESS DEFINITION: [how you measure if the agent is working]

Design a complete agent specification:

1. AGENT IDENTITY (name, role, one-sentence mission)
2. CAPABILITY LIST (5-7 specific tasks this agent can perform)
3. TRIGGER CONDITIONS (what initiates the agent — user message / scheduled / event-driven)
4. DECISION TREE (for each trigger: what the agent does, in what order, with what tools)
5. TOOL INVENTORY (for each tool: name / purpose / when to use / when NOT to use / what to do if it fails)
6. OUTPUT FORMATS (what the agent produces — format, length, delivery method)
7. HUMAN ESCALATION RULES (specific conditions that require human review before action)
8. ERROR PROTOCOL (what the agent does when a tool fails / when it's uncertain / when inputs are malformed)
9. QUALITY GATES (what must be true before the agent delivers output)
10. MEMORY DESIGN (what context persists / what resets per session / where it's stored)
11. SYSTEM PROMPT (write the full system prompt for this agent, using the formula: Role + Mission + Context Rules + Decision Tree + Tool Instructions + Output Format + Quality Gates + Error Protocol + Constraints)

Rules:
- The autonomy boundary must be explicit — ambiguity here causes production failures
- Every tool must have a failure handler — agents without error handling produce silent errors
- The system prompt should be testable — each instruction should be verifiable
- Include at least 3 edge cases and how the agent handles them

Output: Complete agent specification + full system prompt ready for deployment.
```

**Expected output:** A complete AI agent design document with ready-to-deploy system prompt.

**How to judge quality:** The system prompt passes the diagnostic checklist (Part 3). The decision tree has no ambiguous branches. Error handling covers at least 3 failure modes.

**Common failure points:**
- Undefined autonomy boundary → agent acts on things it shouldn't
- Missing error protocol → agent loops or goes silent on failure
- System prompt without examples → agent interprets rules inconsistently

**Revenue connection:** A well-designed AI agent can eliminate 20-40 hours of repetitive work per month. Sold as a productized service, it commands $500-$5,000/month depending on the function.

---

## T-16: WORKFLOW AUTOMATION

**Purpose:** Design a complete workflow automation that eliminates a specific manual process.

**When to use it:** Identifying automation opportunities, designing a Make/Zapier/n8n workflow, or building an internal efficiency system.

**Required inputs:**
- Process to automate
- Current manual steps
- Tools and systems currently used
- Desired outcome
- Acceptable error rate (some automations need 100% accuracy; others can tolerate 95%)

**The Prompt:**
```
You are a workflow automation specialist designing an end-to-end automated process.

PROCESS TO AUTOMATE: [what currently happens manually]
MANUAL STEPS: [list every step as it happens today]
CURRENT TOOLS: [what software is already in use]
DESIRED OUTCOME: [what the automation should produce]
ERROR TOLERANCE: [how accurate does this need to be — 99% / 95% / 80%]
AUTOMATION PLATFORM: [Make / Zapier / n8n / custom code / any]

Design the automation:

1. PROCESS MAP (current manual flow → proposed automated flow, side by side)
2. TRIGGER (what starts the automation)
3. STEP-BY-STEP WORKFLOW (numbered steps with tool name, action, and data passed between steps)
4. CONDITIONAL BRANCHES (if/then paths — what happens when data is missing, malformed, or fails a check)
5. HUMAN REVIEW GATES (where a human must approve before the automation proceeds)
6. ERROR HANDLING (what happens at each step if it fails — retry / alert / fallback)
7. DATA MAPPING (what data enters each step and what data it produces)
8. TESTING PLAN (how to test the automation before going live — test cases for normal and edge scenarios)
9. MONITORING PROTOCOL (how to know if the automation breaks — alerts, logs, frequency of review)
10. TIME SAVINGS CALCULATION (estimate hours saved per week / month)

Rules:
- Every step that touches client data must have a security check
- Any step with >5% error rate needs a human review gate
- The automation should fail loudly (alert + log) rather than silently
- Include rollback instructions if the automation produces incorrect output

Output: Complete automation design document with step-by-step workflow and implementation notes.
```

**Expected output:** A complete workflow automation specification ready for implementation.

**How to judge quality:** Someone unfamiliar with the process could implement this automation from the document. Every error state has a handler. Time savings are calculated.

**Common failure points:**
- Missing conditional branches → automation fails on first non-standard input
- No human review gates → automation sends incorrect output to clients
- Silent failures → hours of lost data before anyone notices

**Revenue connection:** Workflow automations built as productized services command $2,000-$20,000 per build plus ongoing maintenance. Internal automations free up billable hours.

---

## T-17: CODING AND APP DEVELOPMENT

**Purpose:** Generate a complete specification and implementation plan for a software application or feature.

**When to use it:** Building a client-facing tool, internal application, AI-powered product, or automating a technical process.

**Required inputs:**
- What the app does (functionality)
- Who uses it (user type and technical level)
- Tech stack or constraints
- Key user flows
- Integration requirements

**The Prompt:**
```
You are a senior software architect designing a production-ready application.

APP FUNCTION: [what this does]
USERS: [who uses it — role, technical level, frequency of use]
TECH STACK: [languages, frameworks, platforms — or "recommend appropriate stack"]
KEY USER FLOWS: [3-5 primary things users do in the app]
INTEGRATIONS: [APIs, databases, external services]

Build:

1. REQUIREMENTS DOCUMENT
   - User stories (As a [user], I want [feature] so that [benefit]) — one per key flow
   - Acceptance criteria for each user story (WHEN X THEN system SHALL Y)

2. ARCHITECTURE DESIGN
   - Tech stack recommendation with justification
   - Component diagram (describe each component and its responsibility)
   - Data model (entities, relationships, key fields)
   - API design (endpoints, methods, request/response format)

3. IMPLEMENTATION PLAN
   - Phase 1: Core functionality (what must exist for MVP)
   - Phase 2: Enhanced features
   - Phase 3: Scale and optimization
   - Specific tasks per phase (checkbox list, each task ≤14 words, verb-led)

4. SECURITY REQUIREMENTS
   - Authentication method
   - Authorization rules
   - Data protection requirements
   - Input validation rules

5. TESTING STRATEGY
   - Unit tests (what to test)
   - Integration tests (key paths to test)
   - User acceptance tests

6. DEPLOYMENT PLAN
   - Environment setup
   - CI/CD approach
   - Monitoring requirements

Rules:
- Every feature must be in a user story before being designed
- Data model must include all relationships and constraints
- Security requirements are non-negotiable — list them before the feature list
- Phase 1 must be deployable and usable on its own

Output: Complete specification document in the sections above.
```

**Expected output:** A full app specification ready for development.

**How to judge quality:** A developer could start building from this spec without asking clarifying questions. The user stories cover all primary flows. The data model has no missing relationships.

**Common failure points:**
- Speccing Phase 2 features before Phase 1 is defined → always lock the MVP first
- Missing authentication/authorization spec → retrofitting security is expensive
- No testing strategy → production bugs become client-facing problems

**Revenue connection:** A well-scoped spec reduces development time by 30-50% and eliminates scope creep. Sold as a scoping document, it commands $500-$3,000 before a line of code is written.

---

## T-18: AI TOOLS FOR ACCOUNTING AND TAX

**Purpose:** Design or prompt AI tools specifically for the accounting and tax professional context.

*(Detailed templates for this category are in Part 6.)*

See Part 6: Accounting and Tax AI Section for complete templates.

---

## T-19: PRODUCTIZED SERVICE DESIGN

**Purpose:** Package an existing service into a repeatable, scalable productized offering with fixed scope, price, and delivery.

**When to use it:** Converting a custom service to a productized one, building a scalable tier of your service offering, or creating a lower-commitment entry offer.

**Required inputs:**
- The service to productize
- Target client
- Desired price point
- Delivery method (async / calls / software-assisted)
- Maximum hours per engagement

**The Prompt:**
```
You are a productized service designer who specializes in professional services businesses.

SERVICE TO PRODUCTIZE: [what you currently do]
TARGET CLIENT: [who this is for]
PRICE POINT: [monthly retainer / one-time fee / subscription]
DELIVERY METHOD: [async / scheduled calls / software / hybrid]
MAX HOURS: [how many hours you're willing to invest per client per month]

Design a productized service:

1. SERVICE NAME (4-6 words, outcome-focused)
2. ONE-SENTENCE DESCRIPTION (who it's for + what they get + when they get it)
3. FIXED SCOPE DEFINITION (exactly what is included — write this as a contract-ready scope of work)
4. WHAT IS EXPLICITLY NOT INCLUDED (equal in importance to scope)
5. DELIVERY PROCESS (how this service is delivered — step by step, day by day)
6. INPUTS REQUIRED FROM CLIENT (exactly what they provide and by when)
7. OUTPUT SPECIFICATION (exactly what they receive, in what format, by what deadline)
8. PRICING RATIONALE (why this price — time invested + value delivered + market comparison)
9. ONBOARDING FLOW (what happens from "yes" to first delivery — specific steps)
10. RECURRING RHYTHM (if subscription — what happens each week/month)
11. EXPANSION PATH (natural upgrade from this service to the next tier)
12. POSITIONING STATEMENT (one sentence for your website — "For [client type] who [problem], [service name] delivers [outcome] without [frustration]")

Rules:
- Fixed scope must be specific enough to prevent scope creep
- "Not included" section is mandatory — it protects you and sets client expectations
- The delivery process must fit within the max hours constraint
- Price must be sustainable at 60% gross margin or higher

Output: Complete productized service design, formatted as a working business document.
```

**Expected output:** A complete productized service specification ready to launch.

**How to judge quality:** The scope definition is specific enough to put in a contract. The "not included" section prevents every scope creep scenario you've faced. The margins work at your stated max hours.

**Common failure points:**
- Scope creep built into the scope ("unlimited revisions" / "as needed support")
- Missing "not included" section → first difficult client exploits every gap
- Pricing too low for the max hours constraint → unsustainable at scale

**Revenue connection:** Productized services enable scale without proportional time investment. A $1,500/month productized service with 10 clients at 3 hours/month = $15,000 MRR at $500/hour effective rate.

---

## T-20: MONETIZATION WORKFLOW

**Purpose:** Design a complete monetization workflow that converts audience/leads into revenue through a defined sequence of offers.

**When to use it:** Building a complete business model from scratch, mapping your existing offer stack, or designing a new revenue channel.

**Required inputs:**
- Your expertise / knowledge domain
- Current audience or lead sources
- Existing offers (if any)
- Revenue goal
- Time horizon

**The Prompt:**
```
You are a monetization strategist who designs revenue systems for expertise-based businesses.

EXPERTISE: [your specific knowledge domain]
AUDIENCE: [who you have access to — size, relationship, platform]
EXISTING OFFERS: [what you currently sell, if anything]
REVENUE GOAL: [monthly / annual target]
TIME HORIZON: [how quickly do you need to reach this goal]

Design a complete monetization workflow:

1. OFFER LADDER (3-5 offers at increasing price points and commitment levels):
   For each offer:
   - Name and price
   - Who it's for (where they are in the buyer journey)
   - What they get
   - What it leads to next
   - Monthly revenue potential at X units

2. ENTRY POINT (the free or low-cost thing that starts the relationship)

3. VALUE ASCENSION PATH (how a buyer moves from entry offer to highest-value offer)

4. REVENUE MODEL BREAKDOWN (at your revenue goal, how many of each offer do you need to sell):
   Create a table: Offer / Price / Units Needed / Revenue / % of Total

5. CONVERSION SEQUENCE (what happens between each offer tier — email sequence / content / call / other):
   Entry → Offer 1 → Offer 2 → Offer 3

6. 90-DAY LAUNCH PLAN (what to build first, what to sell first, what to prove before scaling)

7. LEVERAGE POINTS (where AI, automation, or technology can multiply output without proportional time investment)

Rules:
- The lowest offer must be affordable enough to remove buying friction, not just cheaper
- Every offer must create desire for the next tier — if it doesn't, it's a dead end
- Revenue model math must work at realistic conversion rates (1-3% for cold / 10-20% for warm)
- The 90-day plan must produce revenue in the first 30 days

Output: Complete monetization system with offer ladder, revenue math, and launch plan.
```

**Expected output:** A complete monetization blueprint with offer ladder, revenue targets, and launch sequence.

**How to judge quality:** The revenue math works at realistic conversion rates. Each offer creates natural desire for the next. The 90-day plan is specific enough to execute starting Monday.

**Common failure points:**
- Offer ladder with gaps (free → $5,000 → nothing in between) → add middle offers to bridge the gap
- No conversion sequence between offers → buyers plateau at entry level
- Revenue math based on unrealistic conversion rates → model at 1% cold, 10% warm

**Revenue connection:** This is the master template — it integrates all other templates into a revenue system.

---

# PART 5: AI MONETIZATION PLAYBOOK

## The Core Principle

The firms, agents, and tools in this repository monetize by doing one of three things:

1. **Eliminating time.** (Devin, Cursor, Manus — hours of coding become minutes)
2. **Eliminating expertise gaps.** (Cluely, Perplexity, v0 — capabilities most people don't have, now available on demand)
3. **Systematizing judgment.** (Kiro's spec workflow, Manus's agent loop — repeatable expert-level decisions at scale)

Every revenue model in AI-powered professional services maps to one of these three value sources. Know which one you're selling.

---

## Revenue Model 1: AI-Augmented Advisory Services

**What it is:** You deliver professional advice faster, deeper, and with better documentation by using AI to accelerate research, analysis, drafting, and reporting.

**How it works:** You charge the same (or higher) fees and invest 30-50% less time per deliverable. The margin expands. Clients get better-formatted, more comprehensive deliverables. You take on more clients without burning out.

**AI applications:**
- Research memos generated in 15 minutes instead of 3 hours
- Client reports produced from structured inputs rather than blank-page drafting
- Tax plan summaries and entity analysis completed in 1 hour instead of 4
- Meeting prep and follow-up documentation automated

**Implementation steps:**
1. Identify your 5 highest time-cost deliverables
2. Build a prompt template for each (use templates T-11, T-13 as starting points)
3. Test and refine each template against 3 real engagements
4. Build an intake form that captures the inputs each template needs
5. Document the workflow as an SOP (T-14)
6. Calculate your hourly rate improvement and raise prices accordingly

**Revenue targets:** A solo practitioner saving 2 hours per client per month at a $300/hour implicit rate = $600/client/month recovered. At 20 clients, that's $12,000/month of effective rate increase.

---

## Revenue Model 2: Productized AI Services

**What it is:** A fixed-scope service powered by AI that can be delivered at scale with consistent quality.

**Example products:**
- "30-Day Tax Planning Report" — fixed deliverable, fixed price, AI-assisted production
- "Entity Structure Analysis" — AI-generated analysis with advisor review and sign-off
- "Content Package" — 30 days of platform content for a business, AI-generated, human-edited
- "Onboarding Kit" — AI-produced SOPs, welcome materials, and training content for new hires

**How it works:** You build a systematized delivery process (T-12, T-19) where AI handles 70-80% of production and you spend your time on review, customization, and client communication.

**Implementation steps:**
1. Choose one deliverable you currently provide that is repetitive and time-intensive
2. Build the AI-assisted production workflow (T-16)
3. Define fixed scope, pricing, and "not included" boundaries (T-19)
4. Create a client intake form that captures all AI prompt inputs
5. Build a quality review checklist that takes under 20 minutes
6. Price at 3-5x your AI production cost — the value is in the expertise that defines the process

**Revenue targets:** A productized tax planning report at $1,500 that takes 2 hours to produce (1 hour AI + 1 hour review) = $750/hour effective rate. At 10 per month = $15,000 MRR.

---

## Revenue Model 3: AI-Powered Tools for Vertical Markets

**What it is:** You build and sell a specialized AI tool for a specific industry or professional audience.

**Examples:**
- A tax planning intake tool for CPAs
- A client onboarding automation for law firms
- A proposal generator for consultants
- An IRS notice triage tool for tax professionals
- A lead qualification bot for financial advisors

**How it works:** You use your domain expertise to define the decision logic, prompts, and output formats. You use AI APIs (Claude, GPT-4, Gemini) as the engine. You package it as a SaaS tool, white-label product, or licensed system.

**Implementation steps:**
1. Identify a repetitive judgment task in your industry that takes 30+ minutes per instance
2. Define the inputs, decision logic, and outputs (T-17 for app spec, T-15 for agent design)
3. Build a prototype using Claude API or similar (Claude is strongest for reasoning-heavy tasks)
4. Validate with 3-5 domain experts in your target market
5. Price as a subscription ($99-$499/month for professional tools)
6. Go to market through industry associations, LinkedIn, and referral from existing clients

**Revenue targets:** A $299/month SaaS tool with 100 subscribers = $29,900 MRR. At 500 subscribers = $149,500 MRR. With AI margin economics, 70-80% gross margin is achievable.

---

## Revenue Model 4: AI Education and Training

**What it is:** You teach others in your industry how to use AI — through courses, workshops, consulting, or training programs.

**Why it works:** Every professional in your field is behind on AI adoption. The people who understand both the domain AND the AI tools are the rarest resource.

**Productization options:**
- "AI for [Industry] Professionals" — digital course ($197-$997)
- "AI Implementation Workshop" — live session for a firm or association ($2,000-$10,000)
- "AI Adoption Consulting" — done-with-you program for firms ($5,000-$25,000)
- "Prompt Library for [Industry]" — template pack ($97-$497)

**Implementation steps:**
1. Document your most impactful AI use cases in your domain
2. Build 3-5 flagship templates (use Part 4 as the model)
3. Create a lead magnet that demonstrates the value of AI in your field (T-07)
4. Build an email sequence that teaches one AI application per week (T-05)
5. Design a course curriculum around your top templates (T-06)
6. Launch to your existing audience first — even 10 sales proves market demand

**Revenue targets:** A $497 course sold to 200 people = $99,400. A quarterly workshop at $3,000 for 15 attendees = $45,000/year from one format.

---

## Revenue Model 5: AI-Assisted Lead Generation for Professional Services

**What it is:** You use AI to dramatically improve the volume and quality of your lead generation — researching prospects, personalizing outreach, and nurturing leads at scale.

**How it works:** AI handles research, personalization, and initial drafts. You review and send. Response rates improve because every message is specific. Pipeline grows without proportional time investment.

**Implementation steps:**
1. Build an ideal client profile with 5-7 specific qualifying characteristics
2. Use AI to research 20 prospects per week — company situation, recent news, specific pain points
3. Use T-10 to write personalized outreach messages for each prospect
4. Use T-05 to build a nurture sequence for leads who don't respond immediately
5. Use T-09 to systematize the sales call after a lead engages
6. Track: outreach sent / responses / calls booked / closes — optimize at each step

**Revenue targets:** 20 personalized outreach messages/week at 15% response rate = 3 conversations/week. At 25% close rate = 3 new clients/month. At $3,000 average engagement = $9,000 MRR growth/month.

---

## Revenue Model 6: Scalable Content-to-Client Pipeline

**What it is:** You use AI-assisted content production to build a consistent authority presence that generates inbound leads.

**How it works:** AI drafts. You inject expertise, voice, and specific examples. You publish 3-5x more content than you could manually. Over 6-12 months, this compounds into a significant inbound pipeline.

**Implementation steps:**
1. Build your content operating system (T-08)
2. Define 3-4 content pillars around your expertise
3. Use the content brief template to produce 3-5 posts per week in 30 minutes/day
4. Track which content generates the most engagement and inquiry
5. Repurpose every piece across LinkedIn, email, and your website
6. Build a lead magnet (T-07) for the top-performing content pillar

**Revenue targets:** At 50,000 LinkedIn followers with 0.5% conversion to inquiry = 250 inquiries/year. At 20% close rate = 50 clients/year. This compounds — the content asset grows in value over time.

---

## AI Stack Recommendations by Business Type

| Business Type | Core AI Tools | Revenue Application |
|---|---|---|
| Solo CPA / Tax Advisor | Claude API, ChatGPT, Notion AI | Research memos, client reports, planning docs |
| Accounting Firm | Claude API + custom prompts, automation (Make/Zapier) | Client onboarding, tax research, review checklists |
| Consultant / Coach | Claude, v0 for tools, Make for automation | Lead gen, content, proposal generation |
| Agency | Claude + content system, automation platform | Client delivery, reporting, SOPs |
| Product Builder | Claude API + app framework | Vertical SaaS tools, AI-powered features |
| Educator / Course Creator | Claude for content, email AI | Course creation, content system, lead magnets |

---

# PART 6: ACCOUNTING AND TAX AI SECTION

## Why This Vertical Is Uniquely Positioned for AI

The accounting and tax profession is the highest-density combination of:
1. **Repetitive, structured analysis** — ideal for AI prompt-driven automation
2. **High-stakes client communication** — where AI-assisted drafting adds clarity and consistency
3. **Explainable reasoning requirements** — where showing your work is required by the profession
4. **Time-compressed seasonality** — where labor efficiency improvements have multiplied value
5. **Under-served by generic AI tools** — creating white space for domain-specific tools

The prompts below are production-ready and written for professionals who understand their professional obligations — AI is the production engine, human review is the quality gate.

---

## AT-01: TAX PLANNING TOOL

**Purpose:** Generate a structured tax planning analysis for a specific client situation.

**When to use:** Pre-engagement scoping, annual planning meetings, mid-year reviews, or responding to a client question about their tax situation.

**Required inputs:**
- Entity type (S-Corp / C-Corp / Partnership / LLC / Sole Prop / Individual)
- Revenue range and income profile
- Current deductions in use
- Key life/business events in the current year
- Planning horizon (current year / 3-year / retirement)

**The Prompt:**
```
You are a CPA and tax strategist preparing a tax planning analysis for a client. Your analysis is a starting point for professional review — flag all items that require verification or professional judgment.

CLIENT PROFILE:
Entity Type: [S-Corp / C-Corp / Partnership / LLC / Individual]
Revenue/Income: [$X range]
Current Structure: [brief description]
Current Deductions in Use: [list known deductions]
Key Events This Year: [business acquisition / sale / compensation change / real estate / retirement account / other]
Planning Horizon: [current year / 3-year / retirement planning]

Produce a structured tax planning analysis:

1. CURRENT SITUATION SUMMARY (what we know about the client's tax profile — 1 paragraph)

2. KEY OPPORTUNITIES IDENTIFIED (3-7 specific strategies worth evaluating for this client):
   For each strategy:
   - Strategy name
   - How it applies to this specific client
   - Estimated annual tax impact ($ range or % estimate — clearly label as estimate)
   - Implementation requirements
   - Key risks or limitations
   - Confidence level: [HIGH — established strategy / MEDIUM — fact-specific / LOW — requires research]

3. PRIORITY RANKING (order the strategies by: estimated impact × ease of implementation)

4. PLANNING QUESTIONS (5-7 questions to ask the client to determine applicability of these strategies)

5. RECOMMENDED NEXT STEPS (specific professional actions with timeline)

6. FLAGS FOR REVIEW (anything in this analysis that requires professional judgment, additional research, or cannot be determined without more information — be specific)

Rules:
- Never state a specific tax savings number without flagging it as an estimate
- Flag any strategy that has been subject to recent IRS scrutiny
- Include "does not apply if" conditions for each strategy
- Every strategy must cite the general code section or authority (e.g., "IRC § 199A," "Reg. 1.162")
- This is a planning analysis, not tax advice — include appropriate professional disclaimer

Output: Professional-quality tax planning memo formatted for advisor review, then potential delivery to client.
```

**Expected output:** A structured tax planning analysis with prioritized strategies, impact estimates, and review flags.

**Revenue connection:** This template enables a solo practitioner to complete initial tax planning analyses in 60-90 minutes instead of 3-4 hours. At 5 planning engagements/month at $1,500-$3,000 each, that's $7,500-$15,000/month with 60% less production time.

---

## AT-02: CLIENT INTAKE AUTOMATION

**Purpose:** Design and generate the complete intake process for a new tax or accounting client.

**When to use:** Onboarding a new client, replacing a paper-based intake process, or building a systemized intake for a productized service.

**The Prompt:**
```
You are an operations specialist building a client intake system for a professional accounting or tax firm.

FIRM TYPE: [CPA firm / solo practitioner / tax advisor / bookkeeping service]
CLIENT TYPE: [individual / small business / high-net-worth / corporate]
SERVICES OFFERED: [tax preparation / tax planning / advisory / bookkeeping / all]
INTAKE METHOD: [web form / email questionnaire / video call + form / portal]

Build a complete client intake system:

1. INTAKE QUESTIONNAIRE (organized by section):
   Section 1: Business/Personal Profile (5-8 questions — entity, industry, revenue, structure)
   Section 2: Current Situation (5-8 questions — current advisor, pain points, prior issues)
   Section 3: Goals and Priorities (3-5 questions — what they want, timeframe, success metrics)
   Section 4: Documentation Needed (checklist of documents to request)
   Section 5: Expectations (fees, process, communication preferences)

2. AUTOMATED FOLLOW-UP SEQUENCE (3 emails after intake submission):
   Email 1 (immediate): Confirmation + next steps
   Email 2 (Day 2): Document checklist reminder
   Email 3 (Day 5): Scheduling link for kickoff call

3. CLIENT ONBOARDING CHECKLIST (internal — what the firm does before the first client meeting):
   [ ] Review intake form
   [ ] Pull prior returns (if applicable)
   [ ] Check for open IRS notices
   [ ] Prepare preliminary observations
   [ ] Set up client file and portal access
   [ ] Confirm fee agreement

4. KICKOFF CALL AGENDA (30-45 minutes):
   - Review intake summary (5 min)
   - Confirm situation and goals (10 min)
   - Explain your process and communication style (5 min)
   - Identify missing information (5 min)
   - Set expectations and next steps (10 min)

5. RED FLAGS CHECKLIST (issues to identify during intake that affect engagement scope or risk):
   - [list 8-10 specific red flags for your service type]

Output: Complete intake system ready for implementation.
```

**Revenue connection:** A systematized intake reduces onboarding time per client by 2-4 hours. For a firm with 100 new clients/year, that's 200-400 hours recovered — $60,000-$120,000 in effective labor value.

---

## AT-03: TAX RETURN REVIEW SUPPORT

**Purpose:** Build an AI-assisted review checklist and analytical framework for tax return quality control.

**When to use:** Reviewing returns before filing, building a quality control system, or training junior preparers on review standards.

**The Prompt:**
```
You are a tax quality control specialist building a review framework for [return type: 1040 / 1120S / 1065 / 1120].

RETURN TYPE: [1040 / 1120S / 1065 / 1120]
FIRM SIZE: [solo / small firm / mid-size]
COMMON ERROR TYPES: [list errors your firm has encountered — or request AI to generate common errors for the return type]

Build:

1. PRE-REVIEW CHECKLIST (10-15 items to check before opening the return):
   [ ] Prior year return available for comparison
   [ ] All source documents received and reconciled
   [ ] Engagement letter and fee agreement on file
   [ ] Open items from prior year addressed
   [ ] Client notes from current year reviewed

2. ANALYTICAL REVIEW PROCEDURES (ratio-based analysis):
   For each return type, list 8-12 analytical tests:
   Example (1040): "Compare W-2 income to prior year — flag >20% variance"
   Example (1120S): "Compare officer compensation to prior year — flag <$100,000 if profitable"
   Include: what to calculate / what threshold triggers a flag / what to do when flagged

3. SCHEDULE-BY-SCHEDULE REVIEW CHECKLIST:
   For each relevant schedule: required items to verify, common errors, quick checks

4. CROSS-SCHEDULE CONSISTENCY CHECKS:
   Items that must agree between schedules (basis, carryforward, intercompany)

5. DISCLOSURE REVIEW:
   Required disclosures for the return type — what to verify is included

6. FINAL SIGN-OFF CHECKLIST:
   10-12 items that must be true before the preparer marks the return complete

7. REVIEWER INQUIRY LOG (template):
   For each flag: Description / Preparer response / Reviewer decision / Resolution

Rules:
- Every checklist item must be verifiable (not "review for accuracy" — specify what to look for)
- Flag items for elevated scrutiny that are known audit triggers
- Include a note for items that have changed due to recent legislation

Output: Complete review framework formatted as a working QC document.
```

**Revenue connection:** A standardized review system reduces review time by 30-50% while improving accuracy. For a firm processing 300 returns with 2 hours of review each, this recovers 180-300 hours per season.

---

## AT-04: ENTITY STRUCTURE ANALYSIS

**Purpose:** Generate a comprehensive entity structure analysis and recommendation for a business client.

**When to use:** New client engagements, when clients ask about changing entity type, when a business reaches a revenue or complexity threshold that changes the optimal structure.

**The Prompt:**
```
You are a tax strategist performing an entity structure analysis for a business client.

CLIENT SITUATION:
Current Entity: [Sole Prop / LLC / S-Corp / C-Corp / Partnership]
Annual Net Income: [$X range]
Owner Situation: [number of owners, their other income, state of residence]
Business Type: [industry, active vs. passive, asset-heavy vs. service]
Long-Term Plans: [hold / sell / pass down / expand]
Current Self-Employment / Payroll Taxes Paid: [$X estimated]

Analyze all viable entity structures:

FOR EACH STRUCTURE (Sole Prop / Single-Member LLC / S-Corp / C-Corp / Partnership):
1. APPLIES TO THIS CLIENT: [yes / no / conditionally — explain why]
2. TAX TREATMENT SUMMARY (3-4 sentences — how income is taxed in this structure)
3. ESTIMATED ANNUAL TAX IMPACT (estimate range, clearly labeled as estimate, show calculation logic)
4. KEY BENEFITS FOR THIS CLIENT (specific to their situation, not generic)
5. KEY RISKS OR LIMITATIONS (what could go wrong)
6. IMPLEMENTATION REQUIREMENTS (what it takes to set up or convert)
7. ADMINISTRATIVE BURDEN (ongoing compliance requirements)

COMPARISON TABLE:
| Structure | Estimated Annual Tax | SE/FICA Impact | Admin Burden | Best For |
|---|---|---|---|---|

RECOMMENDATION:
- Recommended structure
- Rationale tied to this specific client's goals
- Implementation timeline
- Conditions that would change this recommendation

FLAGS FOR PROFESSIONAL REVIEW:
- [list items that require verification, research, or state-specific analysis]

Rules:
- All tax estimates must show the calculation logic and be labeled as estimates
- State-specific tax implications must be flagged — this analysis is federal only unless specified
- Include the impact of recent legislation where relevant
- S-Corp reasonable compensation analysis must be included if S-Corp is recommended

Output: Professional entity analysis memo formatted for advisor review.
```

**Revenue connection:** Entity analysis engagements typically range from $500-$3,000. With AI-assisted production, the work that took 4-6 hours now takes 1-2 hours. This can be offered as a productized service.

---

## AT-05: STRATEGY RECOMMENDATION WORKFLOW

**Purpose:** Build a systematic workflow for identifying, evaluating, and communicating tax strategies to clients.

**When to use:** Building an advisory practice, creating a repeatable process for annual strategy reviews, or systematizing your highest-value service.

**The Prompt:**
```
You are building a repeatable tax strategy recommendation workflow for a [solo practitioner / small firm].

FIRM FOCUS: [individual clients / small business / high-net-worth / all]
SERVICES: [tax preparation / planning / advisory]
CURRENT PROCESS: [describe your current strategy identification and communication process — or state "build from scratch"]

Design a complete strategy identification and recommendation workflow:

STAGE 1: DATA GATHERING
- Information to collect for strategy identification
- The 10 questions that unlock the most planning opportunities
- Document checklist specific to strategy identification (not just compliance)

STAGE 2: STRATEGY IDENTIFICATION MATRIX
Build a matrix:
| Client Situation | Relevant Strategies | Threshold / Trigger | Priority |
|---|---|---|---|
| Self-employed, >$50K net income | S-Corp election, SEP-IRA, Solo 401k, home office | Revenue / income level | High |
| Real estate investor | Cost segregation, STR election, depreciation recapture planning | Property type / holding period | High |
| [Add 10-15 common situations specific to your client base] |

STAGE 3: STRATEGY EVALUATION
- How to assess each strategy for this specific client
- Quantification framework (how to estimate impact)
- Risk assessment (likelihood of IRS scrutiny, implementation complexity)
- Decision criteria for recommendation vs. pass

STAGE 4: CLIENT COMMUNICATION
- How to present strategies to clients (meeting / memo / email)
- The 3-tier presentation: what we can do / what it costs to implement / what it saves
- How to handle client uncertainty or reluctance

STAGE 5: IMPLEMENTATION AND FOLLOW-THROUGH
- Handoff checklist (from planning to implementation)
- Verification that strategies were implemented correctly
- Documentation for the return

Output: Complete workflow with all stages, matrices, and scripts.
```

**Revenue connection:** A systematized strategy workflow enables consistent advisory revenue. Firms that proactively present strategies retain clients at 20-30% higher rates and generate 2-3x more advisory fees per client.

---

## AT-06: CLIENT-FACING TAX EXPLAINER

**Purpose:** Write plain-language explanations of tax concepts, strategies, or situations for client communication.

**When to use:** Sending educational content to clients, explaining a complex situation in a client letter, or building a library of client communication templates.

**The Prompt:**
```
You are writing a plain-language tax explanation for a client who is not a tax professional.

CONCEPT TO EXPLAIN: [specific tax topic, strategy, or situation]
CLIENT TYPE: [small business owner / individual / investor / professional]
CONTEXT: [why they're receiving this — we're recommending it / they asked about it / it affects their return]
DEPTH: [brief overview (1 paragraph) / full explanation (1-2 pages) / FAQ format]

Write the explanation:

1. HEADLINE (what this is, in plain English — no tax jargon in the title)

2. THE SHORT ANSWER (2-3 sentences — what they need to know, in the simplest possible terms)

3. HOW IT WORKS (step-by-step explanation — use a specific example with round numbers):
   "Here's how this works in practice: Let's say you [specific scenario]..."

4. HOW THIS APPLIES TO YOU (1 paragraph specific to their situation)

5. WHAT YOU NEED TO DO (specific actions in simple terms):
   - [Action 1 — what it is, when to do it, what it produces]
   - [Action 2]
   - [Action 3]

6. WHAT HAPPENS IF YOU DON'T (brief — the cost of inaction in plain terms)

7. YOUR QUESTIONS ANSWERED (3-5 FAQ entries based on common client questions about this topic)

8. NEXT STEPS (specific — "Call us by [date]" or "Provide [document] before [date]")

Rules:
- Replace every technical term with a plain language equivalent (or explain it in parentheses the first time)
- Use specific dollar examples — "approximately $5,000-$15,000 in tax savings" not "significant savings"
- Never imply a definite outcome without the words "estimated" or "in situations like yours"
- Keep sentences under 20 words whenever possible
- The explanation should be written at an 8th-grade reading level

Output: Client-ready explanation formatted for email or PDF delivery.
```

**Revenue connection:** Client-facing explainers build trust, reduce call volume (clients understand before they call), and serve as content marketing. A library of 20-30 explainers is a significant firm asset.

---

## AT-07: IRS NOTICE RESPONSE WORKFLOW

**Purpose:** Build a systematic process for receiving, triaging, analyzing, and responding to IRS notices.

**When to use:** Building a notice response practice, creating an SOP for your team, or responding to a specific notice type.

**The Prompt:**
```
You are building an IRS notice response system for a professional tax firm.

NOTICE TYPE: [specific notice — CP2000 / CP14 / CP501 / Letter 1058 / 4549 / other — OR "build a general triage system"]
FIRM CAPABILITY: [we handle this in-house / we refer complex cases]

If building a response for a SPECIFIC notice type:

1. NOTICE SUMMARY (what this notice means in plain language — for client communication)
2. URGENCY CLASSIFICATION (how quickly must this be addressed — immediate / 30 days / 60 days / informational)
3. INFORMATION REQUIRED FROM CLIENT (exact documents and data needed before responding)
4. ANALYSIS FRAMEWORK (how to evaluate the notice — agree / disagree / partially agree)
5. RESPONSE OPTIONS (with pros/cons for each)
6. DRAFT RESPONSE TEMPLATE (professional response letter with [PLACEHOLDER] fields for specific facts)
7. FOLLOW-UP PROTOCOL (what to track after sending the response)
8. CLIENT COMMUNICATION TEMPLATE (how to explain this notice and the response to the client)

If building a GENERAL TRIAGE SYSTEM:

1. NOTICE INTAKE CHECKLIST (what to do when a notice arrives — first 48 hours)
2. NOTICE CLASSIFICATION MATRIX (urgency level / response type / typical resolution path)
3. ESCALATION CRITERIA (when to involve a senior professional or specialist)
4. CLIENT NOTIFICATION SCRIPT (what to say when calling a client about an IRS notice)
5. RESPONSE TRACKING SYSTEM (how to monitor open notices — fields and update frequency)
6. COMMON NOTICE LIBRARY (20+ most common notices with description, urgency, and typical response)

Output: Complete notice response system or specific notice analysis with response template.
```

**Revenue connection:** A systematized notice response process enables a firm to handle 2-3x more notices per preparer-hour. IRS notice responses are typically billed at $200-$500/hour — systematization creates significant margin.

---

## AT-08: RESEARCH MEMO GENERATION

**Purpose:** Generate a structured tax research memo on a specific question or issue.

**When to use:** Answering a tax question with a documented position, supporting a return position, or responding to a client inquiry that requires research.

**The Prompt:**
```
You are a tax researcher preparing a tax research memo for professional review.

RESEARCH QUESTION: [specific tax question — be precise]
CLIENT SITUATION: [relevant facts — entity type, transaction, amounts, timing]
JURISDICTION: [federal / state — specify state]
URGENCY: [how quickly is this needed]

IMPORTANT: This memo is a research starting point. Flag all conclusions that require verification with primary sources before relying on them in a return or client advice.

Structure the memo:

1. ISSUE (the specific legal question to be resolved — one sentence)

2. BRIEF ANSWER (2-3 sentences — the answer to the question with confidence level)

3. FACTS (relevant facts from the client situation that affect the analysis)

4. APPLICABLE AUTHORITY:
   - Primary authority (code sections, regulations, rulings — cite specifically)
   - Secondary authority (case law, IRS guidance, tax court decisions if applicable)
   - Note: Flag where citation needs verification

5. ANALYSIS (apply the authority to the facts — one paragraph per relevant legal principle):
   - State the rule
   - Apply it to these facts
   - State the result

6. CONCLUSION (the answer to the Issue based on the Analysis)

7. ALTERNATIVE POSITIONS (if there is uncertainty, state the contrary position and its basis)

8. PLANNING CONSIDERATIONS (if the conclusion creates planning opportunities or risks)

9. ITEMS REQUIRING VERIFICATION (specific citations, conclusions, or code references that must be confirmed with primary sources before use):
   - [list each item explicitly]

10. RECOMMENDED NEXT STEPS

Rules:
- Never state a conclusion without citing authority
- Flag any reference that could not be verified from training knowledge
- If the answer is genuinely uncertain, say so — do not fabricate certainty
- Distinguish between "established law" and "my interpretation of the authorities"
- Label all conclusions as preliminary pending professional verification

Output: Professional research memo formatted for internal use and potential client delivery.
```

**Revenue connection:** Tax research memos are billed at $300-$500/hour. An AI-assisted memo that takes 45 minutes instead of 3 hours still commands the full fee — the value is in the analysis and professional responsibility, not the typing.

---

## AT-09: ADVISORY REPORT GENERATION

**Purpose:** Generate a complete, professional advisory report on a client's financial and tax situation.

**When to use:** Annual business reviews, estate planning engagements, pre-transaction analysis, or any comprehensive advisory deliverable.

**The Prompt:**
```
You are a CPA and business advisor preparing an annual advisory report for a business client.

CLIENT PROFILE:
Business type: [industry, entity type, revenue]
Current year highlights: [key events, transactions, changes]
Prior year comparison: [how the business performed vs. prior year]
Owner goals: [near-term / long-term — stated by client]

REPORT PURPOSE: [annual review / transaction planning / succession planning / growth planning]

Build an advisory report:

1. EXECUTIVE SUMMARY (what we found, what we recommend, what it means for the owner — max 300 words)

2. FINANCIAL PERFORMANCE REVIEW:
   - Revenue and income trends (current year vs. prior year)
   - Key ratio analysis (profitability, cash, leverage — specific numbers)
   - Observations and implications

3. TAX SITUATION REVIEW:
   - Current year estimated tax liability
   - Comparison to prior year
   - Strategies implemented this year and their impact
   - Strategies identified for next year

4. ENTITY AND STRUCTURE REVIEW:
   - Is the current entity still optimal for this client's situation?
   - Any structural changes to consider?

5. OWNER WEALTH PICTURE:
   - Retirement savings: on track / below target / needs attention
   - Risk exposure: identified risks and mitigation status
   - Estate and succession: current state and recommended actions

6. KEY RECOMMENDATIONS (5-7 specific recommendations with):
   - Priority (urgent / this year / multi-year)
   - Estimated financial impact
   - Owner action required
   - Timeline

7. IMPLEMENTATION TRACKER (table: Recommendation / Status / Owner / Deadline / Notes)

8. NEXT 12 MONTHS (specific milestones and meetings)

Rules:
- All financial figures must be labeled as actual, estimated, or projected
- Every recommendation must have an owner (advisor / client / both)
- The executive summary must be client-readable without the rest of the report
- Include "if we don't act" for every urgent recommendation

Output: Professional advisory report formatted for client delivery.
```

**Revenue connection:** Annual advisory reports are the foundation of a subscription advisory model. Firms that deliver structured annual reviews retain clients at 90%+ vs. 70% for compliance-only relationships. Advisory subscriptions range from $5,000-$25,000/year.

---

## AT-10: LEAD QUALIFICATION TOOL

**Purpose:** Build an AI-powered lead qualification system for an accounting or tax practice.

**When to use:** Screening inbound leads, qualifying referrals, or building a pre-consultation funnel.

**The Prompt:**
```
You are building a lead qualification system for a [CPA firm / tax advisory / accounting practice].

IDEAL CLIENT PROFILE:
Revenue range: [$X - $Y]
Entity types: [list preferred entity types]
Industries: [preferred or excluded industries]
Service needs: [tax planning / compliance / advisory / bookkeeping / all]
Client budget expectation: [minimum engagement value]

Build a qualification system:

1. QUALIFICATION SCORING MATRIX:
   Criteria | Weight | 1 Point | 2 Points | 3 Points
   Revenue fit | 30% | Below range | Low range | Sweet spot
   [Build 6-8 criteria with weights totaling 100%]
   Total score: 15-18 = A-lead / 10-14 = B-lead / Under 10 = Not a fit

2. INTAKE QUESTIONS (5-7 questions to ask a prospective client that reveal the scoring criteria):
   - Question text
   - What it reveals
   - Red flag answer (if any)

3. QUALIFICATION EMAIL TEMPLATE (for responding to an inbound lead — confirms receipt, sets expectations, asks qualifying questions)

4. NOT-A-FIT RESPONSE TEMPLATE (how to professionally decline a prospect who doesn't qualify)

5. A-LEAD NEXT STEPS SCRIPT (what to do when a lead scores high — move to call within 24 hours)

6. REFERRAL BACK SYSTEM (for leads that don't fit your practice — who do you refer them to and how)

Rules:
- The scoring matrix must be completable in under 5 minutes
- Every qualification question must have a clear "right answer" tied to your ICP
- The not-a-fit response must be professional and provide an alternative

Output: Complete lead qualification system.
```

**Revenue connection:** A functioning lead qualification system eliminates 30-50% of low-fit discovery calls — saving 2-5 hours per week while improving close rates on the remaining calls.

---

## AT-11: AI-ASSISTED SALES CALL PREP

**Purpose:** Prepare thoroughly for a sales or discovery call with a prospective accounting or tax client using AI-assisted research and strategy.

**When to use:** Before every prospective client call — this template takes 10 minutes and makes the call 3x more likely to convert.

**The Prompt:**
```
You are preparing an accounting professional for a discovery call with a prospective client.

PROSPECT INFORMATION:
Business name and type: [available info]
Owner/contact name: [name and role]
Source of referral: [who referred them and context]
What they said they need: [what they requested in initial contact]
Known facts about their situation: [any information already gathered]

Prepare:

1. SITUATION HYPOTHESIS (based on available information, what is the likely tax/financial situation, pain points, and goals — be specific, label as hypothesis)

2. CALIBRATED DISCOVERY QUESTIONS (8-10 questions ordered from rapport-building to deep-pain):
   For each question:
   - The question text
   - What it reveals
   - What to listen for in the answer

3. ANTICIPATED OBJECTIONS AND RESPONSES:
   For this type of prospect, the most likely objections are:
   - Objection 1: [likely objection] → Response: [specific, non-generic response]
   - Objection 2 → Response
   - Objection 3 → Response

4. VALUE POSITIONING (how to position your services for this specific prospect — based on their situation hypothesis):
   - Key differentiator to emphasize
   - Specific relevant outcome to mention
   - Reference to similar client situation (without identifying details)

5. CALL AGENDA (15-minute structure):
   - 0-2 min: Rapport and confirm agenda
   - 2-8 min: Discovery (your top 4 questions)
   - 8-12 min: Summarize and position
   - 12-15 min: Next steps

6. POST-CALL FOLLOW-UP TEMPLATE (email to send within 2 hours of the call — summarizes what you heard, confirms next steps, reinforces value)

Output: Complete call prep document formatted for quick review before the call.
```

**Revenue connection:** Calls prepared with this framework close at 2-3x the rate of unprepared calls. For a practice generating $300,000/year from advisory, a 2x improvement in close rate means $300,000 in new revenue potential from the same lead volume.

---

## AT-12: CLIENT EDUCATION ASSETS

**Purpose:** Build a library of educational content that establishes authority, retains clients, and attracts new ones.

**When to use:** Content marketing, client newsletter, educational email series, or building a client portal resource library.

**The Prompt:**
```
You are creating a client education asset for an accounting or tax firm.

ASSET TYPE: [newsletter article / email tip / FAQ document / explainer video script / webinar outline]
AUDIENCE: [small business owners / high-net-worth individuals / real estate investors / professionals]
TOPIC: [specific tax or financial topic]
PURPOSE: [educate / build authority / generate leads / retain clients]
LENGTH: [short — 300 words / medium — 800 words / long — 1500+ words]

Create the asset:

1. HEADLINE (makes a specific promise to the target reader — not clever, not vague)

2. OPENING HOOK (first 2 sentences that make the reader say "I need to read this"):
   Either: a surprising statistic, a specific mistake the reader might be making, or a common misconception

3. CORE CONTENT (structured by the format requested):
   For articles/newsletters: 3-5 key points with specific examples and numbers
   For FAQs: 8-12 questions with concise, specific answers
   For video scripts: scene-by-scene with talking points
   For webinar outlines: session sections with key messages and audience engagement moments

4. PRACTICAL TAKEAWAY (one specific action the reader can take this week)

5. CALL TO ACTION (what you want them to do next — contact you / download something / attend an event)

6. PROFESSIONAL DISCLAIMER (brief — for tax content)

Rules:
- Every piece must teach something the reader can use regardless of whether they hire you
- Include at least one specific number or example — no vague claims
- Write at the target audience's knowledge level — not too technical, not condescending
- The CTA must be natural, not a hard sell

Output: Complete asset formatted for distribution.
```

**Revenue connection:** A library of 20-30 educational assets is a major marketing asset. This content generates leads, positions authority, and retains existing clients through consistent value delivery.

---

## AT-13: INTERNAL PREPARER / REVIEWER CHECKLIST

**Purpose:** Create a comprehensive, return-type-specific quality control checklist for preparers and reviewers.

**When to use:** Standardizing quality across a team, training new preparers, or building a QC system.

**The Prompt:**
```
You are building an internal quality control checklist for a tax preparation firm.

RETURN TYPE: [1040 / 1120S / 1065 / 1120 / 941 / other]
AUDIENCE: [preparer checklist / reviewer checklist / both]
FIRM COMPLEXITY: [simple returns only / complex returns / high-net-worth / all]

Build a complete checklist:

PREPARER CHECKLIST (what the preparer verifies before submitting for review):

Part 1: Setup and Source Documents
[ ] [specific item — not generic]
[ ] [specific item]
[10-15 items specific to the return type]

Part 2: Return Mechanics
[ ] [specific computational check]
[ ] [specific comparison to prior year]
[10-15 items]

Part 3: Credits and Deductions
[ ] [specific credit/deduction verification item]
[8-12 items specific to common credits for this return type]

Part 4: Elections and Disclosures
[ ] [required election filed]
[ ] [required disclosure included]
[5-8 items]

Part 5: Final Review
[ ] [self-review step]
[5-7 items]

REVIEWER CHECKLIST (what the reviewer checks that the preparer may miss):

Part 1: Analytical Review
[8-12 ratio and comparison checks with specific thresholds that trigger a flag]

Part 2: High-Risk Items
[8-12 items known to attract IRS attention for this return type]

Part 3: Client Communication
[ ] [client-facing items to verify]

SIGN-OFF PROTOCOL:
- Preparer sign-off criteria
- Reviewer sign-off criteria
- Partner/principal review threshold (dollar amount or complexity trigger)

Rules:
- Every item must be a specific, verifiable check — not a general category
- Include the "why it matters" for each high-risk item
- Flag items that have changed due to recent legislation with [NEW/CHANGED]

Output: Complete checklist formatted as a working document, ready for team use.
```

**Revenue connection:** A well-built QC checklist reduces errors, which reduces risk, which reduces professional liability exposure. It also reduces review time by 20-40% by catching issues at the preparer level.

---

## Accounting and Tax AI Tool Ideas (Productizable)

These are complete tool concepts ready to be designed (use T-15 and T-17) and built:

**1. Tax Profile Analyzer**
Input: Client tax documents (W-2, K-1, prior return data)
Output: Prioritized list of tax planning opportunities with estimated impact
Target market: CPA firms, financial advisors, enrolled agents
Pricing model: $199-$499/month per firm

**2. Entity Comparison Calculator**
Input: Business profile (income, owners, industry, state)
Output: Side-by-side entity structure comparison with tax impact estimates
Target market: Attorneys, CPAs, business advisors
Pricing model: $99-$299/month or per-use ($49/report)

**3. IRS Notice Triage Bot**
Input: Notice type + client situation
Output: Urgency level, required documents, response options, draft response
Target market: CPA firms, EA firms, tax practices
Pricing model: $299-$799/month (unlimited notices)

**4. Tax Planning Memo Generator**
Input: Client intake form (entity, income, key events)
Output: Draft tax planning memo with strategies, estimates, and review flags
Target market: Solo CPAs, small CPA firms
Pricing model: $149-$399/month or per-memo ($29/memo)

**5. Annual Review Generator**
Input: Financial statements, prior year return, client goals
Output: Draft annual advisory report with findings and recommendations
Target market: CPA firms with advisory practices
Pricing model: $499-$999/month

**6. Client Education Platform**
Input: Topic + audience type
Output: Plain-language educational articles, FAQ documents, explainer content
Target market: CPA firms building content marketing
Pricing model: $99-$299/month

**7. Proposal Generator**
Input: Prospect info + services requested + fee range
Output: Professional proposal with scope, deliverables, and investment
Target market: Solo practitioners and small firms
Pricing model: $79-$149/month

**8. Discovery Call Prep Tool**
Input: Prospect information + service type
Output: Research summary, discovery questions, objection responses, call agenda
Target market: Growth-focused CPA firms and advisors
Pricing model: $199-$399/month

---

## Closing Framework: The AI Monetization Decision Tree

When you have an idea for using AI in your business, run it through this filter:

**Step 1: Classify the opportunity**
- Time savings → calculate the hourly value saved
- Expertise gap → calculate the value of the new capability
- Scale multiplier → calculate revenue per hour with vs. without AI

**Step 2: Choose the monetization model**
- Internal use → charge more or work less
- Client deliverable → charge the same, produce faster, serve more clients
- Productized service → fix the price, systematize the delivery
- AI tool → build once, sell many times

**Step 3: Build the prompt before the product**
Every AI-powered revenue stream starts with a prompt. Use:
- Intake form → to capture inputs
- Prompt template → to produce the output
- Quality checklist → to verify the output
- Output format spec → to deliver value consistently

**Step 4: Prove before scaling**
- Run the workflow manually 3-5 times before automating
- Calculate the economics at realistic volume
- Identify the failure modes before they cost you a client

**Step 5: Build the asset**
- Document the workflow (T-14)
- Build the delivery system (T-12)
- Create the offer (T-01)
- Launch with lead generation (T-02)

The competitive advantage is not the AI. The AI is available to everyone.

The competitive advantage is the expertise that defines the prompts, the methodology that structures the workflow, and the professional judgment that reviews the output.

That is not replicable. Build on that.

---

*This document was produced by analyzing production system prompts from Manus, Devin, Cursor, Kiro, Cluely, v0, Perplexity, Lovable, Warp, and Orchids — the most architecturally sophisticated AI tools in production as of 2025-2026. All templates are starting points requiring adaptation to specific professional situations.*
