# AI Monetization Prompt Operating System
### Reverse-Engineered from Production AI Tool Architecture

**Repository:** `Phynxryznstar/system-prompts-and-models-of-ai-tools`
**Branch:** `claude/prompt-engineering-monetization-VVWwP`
**Built from:** Manus, Devin, Cursor, Kiro, Cluely, v0, Perplexity, Lovable, Warp, Orchids

---

# PART 1 — PROMPT ARCHITECTURE ANALYSIS

## Files Studied and Why

### Tier 1 — High Signal Architecture (Analyzed in Full)

**`Manus Agent Tools & Prompt/Modules.txt` + `Agent loop.txt`**
The most complete agent architecture in the repo. Manus uses a modular system: Planner, Knowledge, Datasource, and Writing modules, each with explicit rules. The 6-step agent loop (Analyze → Select → Execute → Iterate → Submit → Standby) is the cleanest execution loop in the repo. The `writing_rules`, `info_rules`, and `error_handling` sections show how to structure prompts governing complex, multi-step autonomous work. Directly applicable to agent design, workflow automation, and productized service delivery.

**`Devin AI/Prompt.txt`**
The most disciplined planning prompt in the repo. Devin separates "planning mode" from "standard mode" — two distinct cognitive states with different rules. The `<think>` tool with 10+ explicit trigger conditions is the best reasoning-gate architecture in the repo. Git safety rules and "never modify tests" constraints show production-grade operational discipline. Directly applicable to any high-stakes agentic workflow.

**`Cursor Prompts/Agent Prompt 2025-09-03.txt`**
The most complete operator prompt in the repo. Contains `status_update_spec`, `summary_spec`, `completion_spec`, `flow`, `tool_calling`, `context_understanding`, `maximize_parallel_tool_calls`, `code_style`, `linter_errors`, `non_compliance`, `todo_spec`, and `markdown_spec` as named sub-systems. The model for how to build a prompt that manages communication, task tracking, quality assurance, and failure recovery simultaneously.

**`Kiro/Spec_Prompt.txt`**
The only prompt in the repo that encodes a complete iterative development workflow as rules. Requirements → Design → Tasks, each phase gated by explicit user approval. EARS format for acceptance criteria. Spec-driven development (requirements.md → design.md → tasks.md) is directly productizable for client delivery and professional services SOPs.

**`Cluely/Enterprise Prompt.txt`**
The most revenue-connected prompt in the repo. Built for live sales calls and meetings. Priority ordering (question answering → term definition → conversation advancement → objection handling → passive mode) is a real-time decision tree with direct sales application. The objection handling section is the best in the repo.

**`v0 Prompts and Tools/Prompt.txt`**
The most complete product-building prompt in the repo. Full design system rules, data persistence architecture, integration recommendations, debugging protocol, and memory management. The "thought → tool call → summary" loop is the cleanest agent communication pattern in the repo.

**`Perplexity/Prompt.txt`**
The best output-formatting prompt in the repo. Contains `format_rules`, `restrictions`, `query_type` routing (academic, news, coding, creative, science, URL lookup), and `planning_rules`. The citation and formatting standards are the highest bar in the repo.

**`Lovable/Agent Prompt.txt`**
Best for discussion-first design philosophy and scope control. Contains the clearest sequential workflow: check context → review tools → default to discussion → think & plan → clarify → gather → implement → verify. The scope-control rules (avoid overengineering, no "nice-to-have" features) are directly applicable to client delivery.

### Tier 2 — Useful Structural Patterns

- **`Warp.dev/Prompt.txt`** — Question vs. task distinction, complexity tiering, citation requirements
- **`Orchids.app/Decision-making prompt.txt`** — Conditional routing, sequential vs. parallel tool sequencing
- **`Kiro/Vibe_Prompt.txt`** — Tone calibration, response style rules

### Ignored (Too Thin or No Business Transfer Value)

`Xcode/`, `CodeBuddy/`, `Z.ai Code/`, `Qoder/`, `Poke/`, `Amp/`, `Google/Gemini/AI Studio vibe-coder.txt`

---

# PART 2 — REUSABLE PROMPTING PRINCIPLES

## 14 Principles Extracted from Production Prompts

### Principle 1: Role Definition
Name the AI with specificity. "You are Manus, an AI agent — you excel at: (1) information gathering, (2) data analysis, (3) multi-chapter research reports, (4) creating applications, (5) programming to solve problems" outperforms "You are a helpful assistant." Role definitions in production prompts answer: *what you are*, *what you excel at*, and *what your primary interface is*.

**Business rule:** Name the agent. List 5-7 specific task domains. State the primary interface. This prevents scope drift and focuses output quality.

### Principle 2: Mission as Priority Hierarchy
State the mission as a priority-ordered list, not a paragraph. Cluely's objective is: primary directive → secondary → tertiary → fallback. Each directive has explicit conditions. Devin's mission is one sentence: "accomplish the task using the tools at your disposal while abiding by the guidelines outlined here."

**Business rule:** 1-2 sentence core objective + 3-5 priority-ordered behaviors for ambiguity. Priority ordering replaces 80% of vague instructions.

### Principle 3: Typed Context Injection
Best prompts inject context through named, typed structures. Manus uses `<event_stream>` with typed events (Message, Action, Observation, Plan, Knowledge, Datasource). Cluely uses speaker-labeled transcripts with explicit mislabeling-correction rules. The key pattern: context is *typed* and *priority-weighted* — internal knowledge < web search < authoritative API data.

**Business rule:** Tell the model what types of context it receives, what each means, and how to weight conflicting sources. Untyped context gets hallucinated on.

### Principle 4: Input Handling Rules
Strong prompts define rules for unclear inputs. Warp: is this a question or a task? Lovable: assume discussion first, not implementation. Kiro: ask for clarification, but never more than once. The divergence is instructive — agents taking irreversible actions default to clarify; agents building low-cost drafts default to act.

**Business rule:** Write explicit rules for ambiguous inputs based on the cost of a wrong action. High-cost actions → clarify. Low-cost actions → act and iterate.

### Principle 5: Layered Constraints
Best prompts use three constraint levels: hard (NEVER — safety/irreversibility), soft (prefer — quality/style), and contextual (in X situation, do Y). Cursor uses three levels: linter errors (must fix), code style (should follow), communication style (prefer). Hard constraints are short, capitalized, and specific.

**Business rule:** Separate NEVER/ALWAYS from "prefer/generally." Hard constraints must be verifiable. Soft constraints must explain the why.

### Principle 6: Decision Trees as If/Then Conditions
This is the most underused pattern in non-production prompts. Cluely's priority ordering tells the model what to do when multiple actions are valid. Orchids tells the model: if clone request → call clone_website first, then generate_design_system, never in parallel. Devin defines 10 explicit conditions for when to use the think tool.

**Business rule:** Write decision rules as explicit if/then conditions, not preferences. "If X, do Y. If not X, do Z" outperforms "determine the best approach."

### Principle 7: Example Density
Production prompts use typed, contrasting, labeled examples. Perplexity shows bad vs. good formatting for every rule. Manus's prompting guide shows "Poor Prompt" vs. "Improved Prompt" with specific rewrites. v0's alignment section shows complete user/assistant exchanges with visible thought processes. Cursor's code_style section shows bad → good variable naming with real identifiers.

**Business rule:** For every output rule, include one bad example and one good example. Examples are more load-bearing than instructions. Instructions tell; examples show.

### Principle 8: Output Format as Named Sections
Every high-performing prompt defines output format in a dedicated, named section. Perplexity uses `<format_rules>` with markdown standards, list rules, table preferences, citation syntax, and summary requirements. Cursor uses `<summary_spec>`, `<status_update_spec>`, `<completion_spec>`. Cluely defines maximum word counts per element (≤6 words for headline, ≤15 words per bullet).

**Business rule:** Define output format as a separate named section. Specify: structure, length limits per section, markdown rules, what to include vs. exclude, how to end. Word count constraints dramatically improve output quality.

### Principle 9: Tool Documentation Per Tool
Production prompts document each tool individually. Warp documents each tool with when to use, edge cases, and what NOT to do. Devin documents every command with parameters, required fields, and anti-patterns. Cursor's tool_calling section governs parallel vs. sequential execution, the 3-5 tool call limit, and dependency sequencing.

**Business rule:** For each tool: purpose / when to use / when NOT to use / required parameters / what to do if it fails. Tool documentation prevents misuse more effectively than any single instruction.

### Principle 10: Quality as Checkable Conditions
Best prompts define quality as verifiable conditions, not adjectives. Devin: "before reporting completion, critically examine your work and ensure you completely fulfilled the user's request." Cursor: "tests, lint, and CI must pass before claiming done." Kiro: "ONLY mark a task completed when you have FULLY accomplished it."

**Business rule:** Define "done" as 3-5 checkable conditions. "High quality" is not checkable. "No linter errors, all acceptance criteria met, output matches the format spec" is.

### Principle 11: Iteration Loop Design
Manus's agent loop: Analyze → Select → Execute → Iterate → Submit → Standby. Kiro's spec workflow: Requirements → (approval) → Design → (approval) → Tasks, with explicit return paths when gaps are found. Cursor's non-compliance section builds in self-correction: "if you failed to call todo_write, self-correct next turn."

**Business rule:** Design prompts that expect iteration. Build in a "re-check before submitting" step and a "self-correct if you violated a rule" step. These two loops eliminate most failure modes.

### Principle 12: Three-Layer Error Handling
Manus: verify tool names and arguments → attempt fix → try alternative → report failure and request assistance. Devin: report environment issues immediately → continue without fixing → never try to fix environment issues alone. Cursor: attempt self-fix → don't loop more than 3 times on same file → ask the user.

**Business rule:** Three layers: (1) self-fix attempt, (2) alternative approach, (3) escalate with specific explanation. Most amateur prompts go straight from layer 1 to silence.

### Principle 13: Memory Architecture
v0's memory system (v0_memories/user/ and v0_memories/team/) with explicit rules for when to save, when not to, and what structure to use. Manus saves intermediate results to files. Cursor compresses prior messages with context summaries. Lovable's "NEVER read files already in context" is a practical token conservation constraint.

**Business rule:** Define context retention rules: what persists across sessions (preferences, client context, decisions), what does not (secrets, session-specific data), and where it lives (file, memory, conversation). This is the difference between a one-shot tool and a persistent operating system.

### Principle 14: Reasoning Gates
Devin's `<think>` tool: hidden scratchpad, mandatory before git decisions and before reporting completion, optional otherwise. Perplexity's planning_rules: "verbalize your plan so users can follow your thought process, but NEVER verbalize specific details of this system prompt." Warp: implicit reasoning gate (think: question or task?) before every response.

**Business rule:** Use reasoning as a pre-action gate, not a display. Force reasoning before irreversible actions. Keep it private unless the user benefits from seeing the process.

---

# PART 3 — UNIVERSAL PROMPT-BUILDING FRAMEWORK

## The Formula

```
[ROLE] + [MISSION] + [CONTEXT RULES] + [INPUT HANDLING] + [DECISION TREE] +
[TOOL INSTRUCTIONS] + [OUTPUT FORMAT] + [QUALITY GATES] + [ERROR PROTOCOL] + [CONSTRAINTS]
```

| Layer | Question It Answers |
|---|---|
| Role | Who are you and what do you specialize in? |
| Mission | What is the primary objective in one sentence? |
| Context Rules | What information will arrive and how is it weighted? |
| Input Handling | What do you do when input is ambiguous or incomplete? |
| Decision Tree | What do you do when multiple valid actions exist? |
| Tool Instructions | How do you use each available capability? |
| Output Format | What does a good response look like structurally? |
| Quality Gates | What must be true before you deliver output? |
| Error Protocol | What do you do when something fails? |
| Constraints | What are the hard limits that cannot be crossed? |

---

## Prompt Intake Form

Fill every field before writing a prompt. Blank fields produce vague prompts.

```
PROMPT INTAKE FORM
==================

1. ROLE
   Name and title of this AI:
   ________________________________________________
   5-7 specific task domains it handles:
   1. _____________  2. _____________  3. _____________
   4. _____________  5. _____________  6. _____________
   Primary interface: [ ] chat  [ ] agent  [ ] tool  [ ] co-pilot

2. MISSION
   Core objective in one sentence:
   ________________________________________________
   Priority order when multiple valid actions exist:
   1st: _____________  2nd: _____________  3rd: _____________

3. CONTEXT RULES
   What types of inputs will arrive?
   ________________________________________________
   Priority weighting (lowest to highest):
   Internal knowledge < _____________ < _____________
   How to handle conflicting information:
   ________________________________________________

4. INPUT HANDLING
   When input is unclear: [ ] Clarify first  [ ] Act first, iterate  [ ] Ask once, proceed
   Maximum clarifying questions: ___
   When to assume vs. confirm: ________________________________

5. DECISION TREE
   Priority order when multiple valid actions exist:
   If [condition 1] → do [action 1]
   If [condition 2] → do [action 2]
   If [none of the above] → do [fallback]

6. TOOLS
   Tool 1: name / purpose / when to use / when NOT to use
   Tool 2: name / purpose / when to use / when NOT to use
   Tool 3: name / purpose / when to use / when NOT to use

7. OUTPUT FORMAT
   Structure: ________________________________
   Max length: ________________________________
   Required sections: ________________________________
   Prohibited content: ________________________________
   Must include at least one: bad example / good example per key rule

8. QUALITY GATES
   What must be true before output is delivered? (3-5 checkable conditions)
   1. _____________  2. _____________  3. _____________

9. ERROR PROTOCOL
   Self-fix attempt: ________________________________
   Alternative approach: ________________________________
   Escalation threshold: ________________________________

10. HARD CONSTRAINTS
    NEVER: ________________________________
    ALWAYS: ________________________________
    Tone: ________________________________
```

---

## Weak Prompt Diagnostic Checklist

Every NO is a failure point. Run this before deploying any prompt.

**Role & Identity**
- [ ] Does the prompt name the AI and state a specific role?
- [ ] Are 5+ specific task domains listed?
- [ ] Is there a clear statement of what is in-scope vs. out-of-scope?

**Mission & Objectives**
- [ ] Is the core objective stated in one sentence?
- [ ] Is there a priority order for when multiple actions are valid?
- [ ] Is "done" defined with checkable conditions (not adjectives)?

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
- [ ] Is there at least one bad example and one good example for key outputs?
- [ ] Are word count or length constraints stated?

**Error Handling**
- [ ] Is there a self-fix layer?
- [ ] Is there an alternative approach layer?
- [ ] Is there an escalation threshold?

**Constraints**
- [ ] Are hard constraints separated from soft preferences?
- [ ] Are all NEVER/ALWAYS rules specific, not vague?
- [ ] Are tone and style rules explicit?

**Score:** 18-21 = production-ready. 12-17 = needs work. Under 12 = rebuild.

---

## Prompt Quality Scorecard

Score each dimension 1-5. Minimum production score: 35/50.

| Dimension | Score (1-5) |
|---|---|
| Role specificity (named, domain-scoped, capability-listed) | |
| Mission clarity (one sentence, priority-ordered) | |
| Context architecture (typed inputs, weighted priority) | |
| Decision tree completeness (if/then conditions, fallbacks) | |
| Output format definition (structure, length, examples) | |
| Quality gate explicitness (checkable conditions, not adjectives) | |
| Error protocol depth (self-fix + alternative + escalation) | |
| Constraint clarity (hard vs. soft, specific vs. vague) | |
| Example density (bad + good for each key rule) | |
| Iteration loop design (re-check before submit, self-correct) | |
| **Total** | **/50** |

**Guide:** 45-50 = elite. 35-44 = production-ready. 25-34 = revise. Under 25 = rebuild.

---

## Adapting Prompts to Different AI Tools

| Tool | Key Structural Rule |
|---|---|
| Claude | Use XML tags (`<role>`, `<task>`, `<rules>`, `<format>`). Priority-ordered lists work well. Repeat nothing — Claude reads the full prompt. |
| GPT-4 / ChatGPT | Use markdown headers and numbered steps. Repeat critical constraints near the bottom (recency bias). Start with "You are..." |
| Gemini | Weight toward examples over instructions. State output format twice: in instructions and as a template at the end. |
| Local / OSS models | Shorter, denser prompts. Lead with the most critical constraint. Avoid complex nested XML. |
| Agentic frameworks (n8n / Make / LangChain) | Separate system prompt from user message. Define tool names exactly. Write error handling as explicit conditional branches. |

---

## Rules for Revenue-Connected Prompt Output

**Rule 1: Specify the decision-maker.**
"Write a tax planning memo for a $3M revenue S-Corp owner evaluating entity conversion" produces more valuable output than "explain entity conversion." Audience specificity drives output specificity.

**Rule 2: Define the next commercial action.**
Tell the AI what the output enables: "This analysis should end with a specific recommendation the client can act on at our next meeting."

**Rule 3: Inject your methodology.**
Prompts that include your process ("use the 3-pillar framework: timing, entity, and deduction optimization") produce outputs that sound like you, not a generic AI. Methodology injection is what turns AI output into a branded deliverable.

**Rule 4: Constrain scope to force value.**
"Summarize everything" produces nothing useful. "Identify the three highest-ROI tax strategies for this client given their current structure" forces judgment — the same kind clients pay for.

**Rule 5: Specify the format that enables the next step.**
A recommendation memo formatted for email is worth more than bullet points. The format is part of the value.

**Rule 6: Include a confidence signal.**
Instruct the AI to flag where it draws on general knowledge vs. client-specific data, and where professional verification is recommended. This protects liability and builds client trust.

---

# PART 4 — REUSABLE PROMPT TEMPLATES

---

## T-01: OFFER CREATION

**Purpose:** Generate a complete, compelling offer for a service, product, or program.
**When to use:** Packaging expertise into a sellable offer for a service business, agency, consultancy, or productized service.

**Required inputs:** Target client · Transformation delivered · Delivery method · Price range · 3-5 proof points

```
You are an expert offer strategist who packages professional expertise into high-converting offers.

Mission: Design a complete, specific offer based on the inputs below. Every claim must be backed by a deliverable or proof point.

CLIENT: [describe target client — role, company size, revenue, specific problem]
TRANSFORMATION: [specific before/after state — what changes, by how much, by when]
DELIVERY METHOD: [done-for-you / done-with-you / self-serve / software]
PRICE RANGE: [approximate investment level]
PROOF POINTS: [3-5 specific results or credentials]

Build:
1. OFFER NAME (5-8 words, outcome-focused, not clever)
2. ONE-SENTENCE SUMMARY (who it's for, what they get, what changes)
3. THE PROBLEM IT SOLVES (2-3 sentences — describe the pain state precisely)
4. WHAT'S INCLUDED (specific deliverables, not vague categories)
5. THE RESULT PROMISE (specific outcome, timeframe, any guarantees)
6. WHY THIS WORKS (3 reasons tied to your methodology)
7. WHO IT'S NOT FOR (1-2 exclusions that protect positioning)
8. THE LOGICAL PRICE ARGUMENT (why the investment is reasonable given the outcome)

Output rules:
- Use "you" not "we" wherever possible
- No adjectives without proof
- No claims without specifics
- Maximum 600 words total
- Before finalizing: verify every claim is backed by a deliverable or proof point. Remove unsupported claims.
```

**Expected output:** Complete offer document ready for a sales page, proposal, or pitch deck.
**Quality check:** Every promise has a corresponding deliverable. The problem statement would make the target client say "that's exactly my situation."
**Common failures:** Vague transformation → add numbers and timeframes. Generic deliverables → specify what each produces. Missing "not for" section → add it; it's the most important positioning element.
**Revenue connection:** Every revenue stream — sales page, email sequence, sales call, proposal — requires a clear offer at its core.

---

## T-02: LEAD GENERATION SYSTEM

**Purpose:** Design a complete 30-day lead generation system with specific tactics, messages, and conversion paths.
**When to use:** Building pipeline from scratch, reactivating cold contacts, or systematizing prospect attraction.

**Required inputs:** Ideal client profile · Core offer · Available channels · Lead magnet status

```
You are a lead generation strategist for professional services businesses.

Mission: Design a complete 30-day lead generation system. Prioritize channels that produce qualified leads, not vanity metrics.

BUSINESS TYPE: [what you do, who you serve]
IDEAL CLIENT: [industry, role, company size, specific problem they have right now]
CORE OFFER: [paste or summarize your offer]
AVAILABLE CHANNELS: [LinkedIn / email list / referrals / content / paid / cold outreach]
LEAD MAGNET: [describe it / or "generate one for me"]

Build:
1. CHANNEL STRATEGY (which 2-3 channels to prioritize and why)
2. LEAD MAGNET (if needed — title, format, specific topic, bridge to core offer)
3. OUTREACH MESSAGE (one LinkedIn DM or cold email — personalized, value-first, no pitch in first contact)
4. FOLLOW-UP SEQUENCE (3 messages, 4-7 day spacing)
5. CONVERSION PATH (what happens after a lead responds — qualifying questions, offer of call)
6. WEEKLY ACTIVITY PLAN (specific daily/weekly actions)

Rules:
- Every tactic must be executable by one person
- Every message must be specific to the ideal client's problem
- The system should generate 5-10 qualified conversations per month
- Write all messages in full, ready to send

Output: Full playbook with messages, calendar, and qualifying questions.
```

**Revenue connection:** A functioning lead gen system producing 5 qualified conversations/month at 20% close rate = 1 new client/month.

---

## T-03: WEBSITE COPY

**Purpose:** Write complete, conversion-focused website copy for a service business.
**When to use:** Building or rewriting a website, creating a new service page.

**Required inputs:** Business type · Target client · Primary transformation · 3-5 proof points · Unique approach · Desired action

```
You are a conversion copywriter specializing in professional services websites.

Mission: Write complete, specific, high-converting copy for the following pages. Every line must do one of three things: build trust, address an objection, or move the reader toward the desired action.

BUSINESS: [what you do]
TARGET CLIENT: [specific role, industry, problem]
PRIMARY OUTCOME: [what changes for them — specific and measurable]
PROOF POINTS: [3-5 specific results or credentials]
UNIQUE APPROACH: [what makes your methodology different]
DESIRED ACTION: [book a call / contact / buy]

Write:
1. HOMEPAGE HERO (headline + subheadline + CTA — max 25 words total)
2. PROBLEM SECTION (3-4 sentences describing the painful current state)
3. SOLUTION SECTION (how you solve it — 3 sentences + 3 mechanism bullets)
4. ABOUT SECTION (2-3 sentences — credentials + why you do this — no life story)
5. PROOF SECTION (3 client results: "[Client] had [X problem] → we did [Y] → result was [Z]")
6. CTA SECTION (what they get when they click + what happens next + CTA button text)

Rules:
- No corporate speak, no passive voice
- Every claim requires a specific detail
- Headlines must state an outcome or a problem, not a company name or tagline
- Read each section aloud — if it sounds like a brochure, rewrite it

Output: Each section in final form, ready to paste into a website builder.
```

**Revenue connection:** Copy that converts 1% better on 1,000 monthly visitors = 10 more leads/month. Compounding asset.

---

## T-04: LANDING PAGE

**Purpose:** Write a single-offer landing page for a lead magnet, consultation, or productized service.
**When to use:** Launching a new offer, running ads, promoting a lead magnet, booking discovery calls.

**Required inputs:** The single offer · Traffic source (cold/warm) · What happens after opt-in · 2-3 proof points

```
You are a direct response copywriter building a high-converting landing page for a single offer.

OFFER: [exactly what they get]
TRAFFIC SOURCE: [cold paid / warm email / referral — this determines trust-building copy needed]
POST OPT-IN: [what happens immediately after]
PROOF: [2-3 proof points]

Structure:

ABOVE THE FOLD:
- Headline (outcome for this specific person, max 10 words)
- Subheadline (what it is, who it's for, what changes — max 25 words)
- CTA button text (verb + outcome, max 5 words)

BODY:
1. WHAT YOU'LL GET (3-5 bullets — specific, tangible, measurable)
2. WHO THIS IS FOR (3 bullets — make the reader self-select)
3. SOCIAL PROOF (format: "[Name/Role] — [result they got]")
4. HOW IT WORKS (3 steps from opt-in to outcome)
5. OBJECTIONS (2-3 "You might be wondering..." FAQ entries)
6. FINAL CTA (restate value + urgency if applicable + button)

Rules:
- Cold traffic: add a bio paragraph between proof and how-it-works
- Warm traffic: cut bio, expand deliverable specificity
- Every bullet must contain a specific detail
- No paragraph longer than 3 sentences
- One CTA action only — never split attention

Output: Full page draft with cold/warm variations labeled.
```

**Revenue connection:** Landing pages converting at 30-50% (warm) or 15-25% (cold) are the highest-ROI single asset in most marketing stacks.

---

## T-05: EMAIL SEQUENCE

**Purpose:** Write a complete nurture or sales email sequence for a specific goal.
**When to use:** Onboarding new leads, nurturing toward a sales call, delivering a lead magnet, re-engaging a list.

**Required inputs:** Sequence purpose · Number of emails (3-7) · Core offer being built toward · Audience (cold/warm/existing)

```
You are an email copywriter specializing in professional services and high-ticket offers.

SEQUENCE PURPOSE: [welcome / lead magnet delivery / nurture to call / reactivation]
NUMBER OF EMAILS: [3-7]
CORE OFFER: [what the sequence builds toward]
AUDIENCE: [cold leads / warm list / past clients]

For each email provide:
- Subject line (+ 1 A/B test variation)
- Preview text (max 90 characters)
- Body copy (200-400 words, short paragraphs)
- CTA (one specific action per email)
- Timing (send day)

Standard structure:
Email 1 (Day 0): Deliver the promised thing + set expectations for what comes next
Email 2 (Day 2): Teach one thing that proves your expertise + soft CTA
Email 3 (Day 4): Address the #1 objection + share a proof point
Email 4 (Day 7): Client transformation story + direct CTA to offer
Email 5 (Day 10): Urgency/bonus + strong CTA
[Emails 6-7: Rebuttal and final close if sequence length requires]

Rules:
- Every email readable in under 2 minutes
- Subject lines max 45 characters for mobile
- Open with a hook, not "Hi [Name], I wanted to reach out..."
- Each email teaches something valuable regardless of purchase
- End every email with a P.S. reinforcing the primary message
- Only Emails 4-7 should have a strong CTA to buy

Output: All emails written in full, ready to load into an ESP.
```

**Revenue connection:** An effective 5-email sequence to a warm list can generate 10-20x return on production cost.

---

## T-06: DIGITAL COURSE OUTLINE

**Purpose:** Design a complete, outcome-driven digital course curriculum.
**When to use:** Productizing expertise into a scalable education asset, building a premium program.

**Required inputs:** Topic · Target student · Transformation · Your methodology · Format · Length · Price point

```
You are a curriculum designer who builds professional courses with measurable student outcomes.

COURSE TOPIC: [specific topic]
TARGET STUDENT: [who they are, what they know when they start, what problem they have]
TRANSFORMATION: [exactly what is different when they complete the course]
YOUR METHODOLOGY: [your framework or unique process]
FORMAT: [self-paced video / live cohort / hybrid / text-based]
LENGTH: [hours of content / number of weeks]
PRICE POINT: [approximate — determines depth and support expectations]

Design:
1. COURSE TITLE (outcome-focused, 6-10 words)
2. COURSE PROMISE (one sentence — who this is for, what they'll be able to do, by when)
3. MODULE STRUCTURE (5-8 modules):
   For each module: name / core concept / 3-5 lesson titles / student outcome at module end
4. CORE EXERCISES (one action exercise per module — specific enough to self-evaluate)
5. QUICK WINS (what students can apply in week 1 — critical for retention)
6. COMPLETION MILESTONE (the tangible thing they've built or produced by the end)
7. MARKETING HOOK (one sentence result that sells this course)

Rules:
- Every module must produce a specific outcome, not just teach content
- Module 1 must produce a quick win in the first session
- No module named "Introduction to X" — start with application
- Course title must state what students gain, not what topics are covered

Output: Full course outline with all modules, lessons, exercises, and outcomes.
```

**Revenue connection:** A course built on outcomes sells on transformation, not content volume. Also serves as the nurture path from lead magnet to premium offer.

---

## T-07: LEAD MAGNET

**Purpose:** Create a high-value, specific lead magnet that attracts the right prospect and bridges to your core offer.
**When to use:** Building an email list, launching paid ads, pre-qualifying prospects.

**Required inputs:** Target audience · Core offer you're building toward · Specific problem to solve · Format preference

```
You are a lead magnet strategist for professional service businesses.

TARGET AUDIENCE: [specific role, industry, company size]
CORE OFFER: [what you're ultimately selling]
PROBLEM TO SOLVE: [one specific problem this audience has — smaller and more specific is better]
FORMAT: [PDF / checklist / calculator / template / 3-email course / video training]

Design a lead magnet that:
1. Solves one specific problem completely
2. Is consumable in 20 minutes or less
3. Creates the natural next question that your core offer answers
4. Delivers immediate value — not a glorified sales pitch

Build:
1. TITLE (use "How to [outcome] Without [common frustration]" or "[Number] [Things] Every [Audience] Needs to [Outcome]")
2. SUBTITLE (what they get and why it matters now)
3. TABLE OF CONTENTS (specific sections, not categories)
4. SECTION SUMMARIES (2-3 sentences per section — exactly what they learn/do)
5. THE BRIDGE (last section that creates desire for core offer — what problem the lead magnet reveals but doesn't fully solve)
6. LANDING PAGE HEADLINE (max 12 words, outcome-focused)

Rules:
- Fully solve the stated problem — no teasing without delivering
- The bridge to the core offer must be logical, not forced
- Title must not contain "Ultimate," "Comprehensive," "Complete," or "Free"
- Only your exact target audience should want this lead magnet

Output: Full lead magnet design brief with all sections outlined.
```

**Revenue connection:** A lead magnet that pre-qualifies prospects cuts sales call time by 40-60% because prospects arrive understanding the problem space.

---

## T-08: CONTENT CREATION SYSTEM

**Purpose:** Build a repeatable content system that produces authority-building content across platforms.
**When to use:** When you need consistent content output without starting from scratch weekly.

**Required inputs:** Expertise / niche · Target audience · Primary platform · Posting frequency · Content goals

```
You are a content strategist for a professional services business.

EXPERTISE: [your specific knowledge domain]
AUDIENCE: [who you're speaking to — role, industry, specific problems]
PRIMARY PLATFORM: [LinkedIn / email / YouTube / podcast / X]
FREQUENCY: [posts per week / month]
CONTENT GOAL: [lead generation / authority / nurture / SEO / all]

Build a content operating system:

1. CONTENT PILLARS (3-4 themes that represent your expertise — each must attract your target client and reflect your methodology)

2. CONTENT FORMATS (per pillar — what types of content work):
   For each format, write a reusable template (e.g., Pillar 1 → insight, case study, how-to, contrarian take)

3. MONTHLY CONTENT CALENDAR (specific topics mapped to formats and weeks — not categories, specific topics)

4. THE REPEATABLE CONTENT BRIEF (fill-in-the-blank, completable in 5 minutes):
   - Topic:
   - Audience problem it addresses:
   - My specific point of view:
   - One counterintuitive angle:
   - Call to action:
   - Format:

5. 10 SPECIFIC POST IDEAS (ready to write — specific topic + angle, not just categories)

6. REPURPOSING MAP (how to turn one piece of content into 3-5 pieces across platforms)

Rules:
- Every content piece must: attract a new prospect / deepen trust / drive a conversion action
- Never post content a general AI could write without your expertise injected
- The contrarian angle is mandatory — it creates shareability
- Content pillars must be specific to your expertise — not "business tips"

Output: Full content operating system formatted as a working document.
```

**Revenue connection:** Consistent authority content is the lowest-cost lead generation channel for professional services. One viral post can outperform a month of cold outreach.

---

## T-09: SALES CALL FRAMEWORK

**Purpose:** Build a repeatable sales call structure that qualifies, diagnoses, and closes.
**When to use:** Running discovery calls, strategy calls, or any sales conversation ending in a yes/no decision.

**Required inputs:** Core offer · Target client profile · Common objections · Close method

```
You are a sales coach who specializes in professional services. Your calls close at 40%+ because they qualify hard, diagnose precisely, and present only when there's a clear fit.

OFFER: [your core offer]
IDEAL CLIENT: [who you're talking to]
COMMON OBJECTIONS: [list 3-5 real objections you face]
CLOSE METHOD: [proposal / verbal yes / contract / next-meeting close]

Build:
1. PRE-CALL PREP (3 things to research before every call)
2. OPENING (what to say in the first 60 seconds — get permission to continue, not a pitch)
3. AGENDA SETTING (frame the call so the prospect knows what to expect)
4. DISCOVERY QUESTIONS (8-12 questions ordered from surface to deep pain — with notes on what to listen for)
5. DIAGNOSTIC SUMMARY (how to reflect back what you heard before presenting — never pitch without this)
6. OFFER PRESENTATION (3-minute verbal: problem → solution → outcome → investment)
7. OBJECTION HANDLING (for each listed objection: underlying concern + specific response — acknowledge before reframing)
8. THE CLOSE (direct question, not "what do you think?")
9. NEXT STEPS (what happens after yes AND after no)
10. POST-CALL FOLLOW-UP (what to send within 24 hours)

Rules:
- Discovery must uncover budget, timeline, decision-making authority, cost of inaction
- Never pitch before summarizing the diagnosis
- Objection responses must acknowledge the concern before reframing — never argue
- The close must be a direct question

Output: Complete framework with exact language, not just topics. Ready to use.
```

**Revenue connection:** Improving close rate from 20% to 35% on the same call volume increases revenue by 75%. This template compounds.

---

## T-10: SALES SCRIPT

**Purpose:** Write a specific, natural-sounding sales script for a particular channel.
**When to use:** Training a sales team, scripting outbound calls, writing DM sequences.

**Required inputs:** Channel (cold call / warm DM / referral / demo) · Offer · Audience · Primary objection

```
You are a sales copywriter writing a conversational script for a professional services company.

CHANNEL: [cold call / warm DM / referral intro / inbound demo]
OFFER: [what you're selling]
AUDIENCE: [who you're talking to]
PRIMARY OBJECTION: [the main thing that stops this person from saying yes]

Write:
1. OPENING (15 seconds — get permission to continue, not a pitch)
2. RELEVANCE HOOK (why this specific person, today — 1-2 sentences)
3. QUALIFYING QUESTION (one question to confirm they have the problem)
4. MICRO-PITCH (30 seconds — problem + solution + proof point, no features)
5. DISCOVERY BRIDGE (transition from pitch to learning mode)
6. 3 KEY QUESTIONS (to understand fit and urgency)
7. TRANSITION TO NEXT STEP (conversation to meeting/proposal/close)
8. OBJECTION RESPONSE (specifically for the primary objection listed)
9. CLOSE (exact words to book the next step)
10. FOLLOW-UP MESSAGE (what to send if they say "send me some info")

Rules:
- Opening must NOT start with "Hi, my name is... I'm calling because..."
- Every sentence max 15 words — this is spoken, not read
- Include pauses: [pause for response] [listen for: X]
- For cold calls: include branching paths for "not interested," "send me info," and "tell me more"
- Test it by reading aloud — if robotic, rewrite

Output: Complete script with branching paths.
```

---

## T-11: RESEARCH REPORT

**Purpose:** Generate a structured research report — competitive analysis, market research, regulatory analysis.
**When to use:** Before a sales call, for a client deliverable, for internal strategy, or as a lead magnet.

**Required inputs:** Topic · Audience and decisions they'll make · Key questions · Depth level · Source priorities

```
You are a research analyst writing a professional report for a specific business audience.

TOPIC: [exact topic]
AUDIENCE: [who reads this and what decisions they'll make with it]
KEY QUESTIONS: [3-7 specific questions the report must answer]
DEPTH: [executive summary (1-2 pages) / full report (5-15 pages)]
SOURCE PRIORITY: [public databases / industry reports / regulatory / client data / web]

Structure:
1. EXECUTIVE SUMMARY (3-5 sentences — what was found + the single most important implication)
2. BACKGROUND (why this matters — context, 1 paragraph)
3. METHODOLOGY (how research was conducted — sources and limitations)
4. FINDINGS (one section per key question):
   - What the data shows
   - What it means for the audience
   - Confidence level: HIGH / MEDIUM / LOW (based on source quality)
5. ANALYSIS (patterns or contradictions across findings)
6. IMPLICATIONS (3-5 specific actions the audience should consider)
7. LIMITATIONS (what this report doesn't cover and why)
8. SOURCES (formatted references)

Rules:
- Every finding must cite a source or state "based on [type] data"
- Confidence levels are mandatory — they protect the reader and the author
- The executive summary must be usable standalone
- Use tables to compare data across categories
- Flag where inference is being made vs. where data is direct

Output: Full report in requested depth. If source data is unavailable, write the framework and flag where research is needed.
```

**Revenue connection:** Research reports can be sold as standalone deliverables ($500-$5,000), used as lead magnets, or packaged into advisory engagements.

---

## T-12: CLIENT DELIVERY FRAMEWORK

**Purpose:** Build a repeatable, professional client delivery system for any service.
**When to use:** Onboarding a new client, standardizing delivery across team members, building a productized service.

**Required inputs:** Service type · Engagement duration · Deliverables · Communication preferences · Success metrics

```
You are an operations consultant building a client delivery system for a professional services firm.

SERVICE TYPE: [what you deliver]
ENGAGEMENT DURATION: [one-time / monthly / quarterly / annual]
DELIVERABLES: [list all deliverables]
COMMUNICATION: [weekly call / async / monthly review]
SUCCESS METRICS: [how you measure if the engagement is working]

Build:
1. ONBOARDING CHECKLIST (everything needed to start — information, access, decisions — with responsible party and deadline)
2. KICKOFF CALL AGENDA (what to cover in first meeting, what decisions must be made)
3. WEEKLY/MONTHLY RHYTHM (standing agenda for recurring touchpoints)
4. DELIVERABLE TEMPLATES (list of standard templates for each deliverable)
5. STATUS UPDATE FORMAT (completable in under 10 minutes — what's done, next, blocked)
6. ESCALATION PROTOCOL (what triggers escalation, who handles it, how quickly)
7. MILESTONE REVIEW (30/60/90 day check-in — questions to ask, adjustments to make)
8. OFFBOARDING CHECKLIST (final deliverables, knowledge transfer, future relationship)
9. CLIENT HEALTH SIGNALS (green / yellow / red indicators and actions for each)
10. RENEWAL/EXPANSION TRIGGER (specific moments that indicate readiness for upsell)

Rules:
- Every checklist item must have a deadline and responsible party
- Status update must be completable in under 10 minutes
- Health signals must be observable behaviors, not feelings
- Renewal trigger should be tied to a specific client win, not a calendar date

Output: Full framework as a working operations document.
```

**Revenue connection:** Systematized delivery enables scaling without founder involvement. Improves client retention by 30-50%.

---

## T-13: CLIENT-FACING REPORT

**Purpose:** Write a professional, client-ready report communicating analysis, findings, and recommendations.
**When to use:** Advisory deliverables, strategy reviews, annual business reviews, any written output going to a client.

**Required inputs:** Report type · Client profile · Key findings · Recommendations · Tone

```
You are a professional advisor writing a client-facing report that communicates complex analysis in clear, actionable language.

REPORT TYPE: [tax plan / strategy memo / analysis / advisory report]
CLIENT: [name/type — no sensitive personal data]
KEY FINDINGS: [3-7 specific findings]
RECOMMENDATIONS: [3-5 specific recommended actions]
TONE: [formal / professional-conversational]

Write:
1. COVER PAGE (title / client / date / prepared by)
2. EXECUTIVE SUMMARY (what we found + what we recommend + what it means — max 200 words)
3. SITUATION OVERVIEW (current state — what was analyzed)
4. FINDINGS (one section per finding):
   - What was found
   - Why it matters (plain language)
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
- Executive summary must be readable standalone
- Avoid technical jargon in findings — define terms in plain language, move technical detail to appendix
- Every recommendation must include expected outcome, not just an action
- Include "what happens if we don't act" for every urgent recommendation
- Never deliver a finding without a corresponding recommendation

Output: Full report in final, client-ready format.
```

**Revenue connection:** A well-formatted client report is a marketing asset — clients share good reports. It also justifies premium fees by making the value of advice visible.

---

## T-14: STANDARD OPERATING PROCEDURE

**Purpose:** Document any business process as a reusable, team-ready SOP.
**When to use:** Standardizing repetitive tasks, onboarding team members, building a knowledge base.

**Required inputs:** Process to document · Who performs it · Tools used · Trigger · Quality standard

```
You are an operations manager documenting a business process as a formal SOP.

PROCESS: [what this SOP covers]
PERFORMER: [role, not name]
TOOLS: [software, systems, templates used]
TRIGGER: [what starts this process]
FREQUENCY: [daily / weekly / per client / on-demand]
OUTPUT QUALITY STANDARD: [what "done correctly" looks like]

Write:
1. PROCESS TITLE AND PURPOSE (what this is and why it exists)
2. SCOPE (what this SOP covers and what it does NOT cover)
3. ROLES AND RESPONSIBILITIES (who does what)
4. PREREQUISITES (what must be true / available before starting)
5. STEP-BY-STEP INSTRUCTIONS (numbered steps):
   - Action (imperative verb: "Open," "Enter," "Click")
   - Where to perform it
   - Success indicator
   - Common error and how to handle it
6. QUALITY CHECKLIST (3-7 checkboxes — verifiable by someone who didn't do the work)
7. EXCEPTIONS AND ESCALATIONS (edge cases and how to handle them)
8. REVISION HISTORY (date / what changed / who changed it)

Rules:
- Every step must start with an imperative verb
- Quality checklist must be verifiable by a reviewer, not self-assessment only
- Write for the lowest-experienced person who will ever run this process
- SOPs longer than 2 pages should be broken into sub-processes

Output: Complete SOP formatted as a working document.
```

**Revenue connection:** SOPs enable delegation, which enables scaling. Every hour spent documenting a process is worth 10-50 hours in future labor savings.

---

## T-15: AI AGENT DESIGN

**Purpose:** Design a complete, deployable AI agent for a specific business function.
**When to use:** Building an autonomous AI workflow, creating a client-facing AI tool, designing an operational agent.

**Required inputs:** Agent function · User type · Available tools · Decision boundaries · Success definition

```
You are an AI systems architect designing a production-ready AI agent.

AGENT FUNCTION: [exactly what this agent does]
USER: [who interacts with the agent — role, technical level]
AVAILABLE TOOLS: [APIs, databases, integrations]
AUTONOMY BOUNDARY: [what it can do without asking / what requires human approval — be explicit]
SUCCESS DEFINITION: [how you measure if the agent is working]

Design:
1. AGENT IDENTITY (name, role, one-sentence mission)
2. CAPABILITY LIST (5-7 specific tasks this agent can perform)
3. TRIGGER CONDITIONS (what initiates the agent — user message / scheduled / event-driven)
4. DECISION TREE (for each trigger: what the agent does, in order, with what tools)
5. TOOL INVENTORY (for each tool: name / purpose / when to use / when NOT to use / failure handler)
6. OUTPUT FORMATS (what the agent produces — format, length, delivery method)
7. HUMAN ESCALATION RULES (specific conditions that require human review before action)
8. ERROR PROTOCOL (what the agent does when a tool fails / when uncertain / when inputs are malformed)
9. QUALITY GATES (what must be true before the agent delivers output)
10. MEMORY DESIGN (what context persists / what resets / where it's stored)
11. SYSTEM PROMPT (write the full system prompt using: Role + Mission + Context Rules + Decision Tree + Tool Instructions + Output Format + Quality Gates + Error Protocol + Constraints)

Rules:
- Autonomy boundary must be explicit — ambiguity causes production failures
- Every tool must have a failure handler — agents without error handling produce silent errors
- Include at least 3 edge cases and how the agent handles them
- System prompt must pass the Diagnostic Checklist from Part 3

Output: Complete agent specification + full system prompt ready for deployment.
```

**Revenue connection:** A well-designed AI agent eliminates 20-40 hours of repetitive work/month. Sold as a productized service: $500-$5,000/month.

---

## T-16: WORKFLOW AUTOMATION

**Purpose:** Design a complete workflow automation that eliminates a specific manual process.
**When to use:** Identifying automation opportunities, designing a Make/Zapier/n8n workflow, or building an internal efficiency system.

**Required inputs:** Process to automate · Current manual steps · Tools in use · Desired outcome · Acceptable error rate

```
You are a workflow automation specialist designing an end-to-end automated process.

PROCESS TO AUTOMATE: [what currently happens manually]
MANUAL STEPS: [list every step as it happens today]
CURRENT TOOLS: [software already in use]
DESIRED OUTCOME: [what the automation should produce]
ERROR TOLERANCE: [99% / 95% / 80%]
AUTOMATION PLATFORM: [Make / Zapier / n8n / custom code / any]

Design:
1. PROCESS MAP (current manual flow → proposed automated flow, side by side)
2. TRIGGER (what starts the automation)
3. STEP-BY-STEP WORKFLOW (numbered steps: tool name / action / data passed between steps)
4. CONDITIONAL BRANCHES (if/then paths — what happens when data is missing, malformed, or fails a check)
5. HUMAN REVIEW GATES (where a human must approve before automation proceeds)
6. ERROR HANDLING (at each step: retry / alert / fallback)
7. DATA MAPPING (what data enters each step, what it produces)
8. TESTING PLAN (test cases for normal and edge scenarios)
9. MONITORING PROTOCOL (how to know if automation breaks — alerts, logs, review frequency)
10. TIME SAVINGS CALCULATION (hours saved per week / month)

Rules:
- Every step touching client data must have a security check
- Any step with >5% error rate needs a human review gate
- Automation should fail loudly (alert + log) not silently
- Include rollback instructions if automation produces incorrect output

Output: Complete automation design document with step-by-step workflow and implementation notes.
```

**Revenue connection:** Workflow automations built as productized services command $2,000-$20,000 per build plus ongoing maintenance.

---

## T-17: CODING AND APP DEVELOPMENT

**Purpose:** Generate a complete specification and implementation plan for a software application or feature.
**When to use:** Building a client-facing tool, internal application, or AI-powered product.

**Required inputs:** App function · Users · Tech stack · Key user flows · Integration requirements

```
You are a senior software architect designing a production-ready application.

APP FUNCTION: [what this does]
USERS: [who uses it — role, technical level, frequency]
TECH STACK: [languages, frameworks, platforms — or "recommend appropriate stack"]
KEY USER FLOWS: [3-5 primary things users do in the app]
INTEGRATIONS: [APIs, databases, external services]

Build:
1. REQUIREMENTS DOCUMENT
   - User stories (As a [user], I want [feature] so that [benefit])
   - Acceptance criteria (WHEN X THEN system SHALL Y)

2. ARCHITECTURE DESIGN
   - Tech stack recommendation with justification
   - Component diagram (each component and its responsibility)
   - Data model (entities, relationships, key fields)
   - API design (endpoints, methods, request/response format)

3. IMPLEMENTATION PLAN
   - Phase 1: Core functionality (MVP — deployable and usable on its own)
   - Phase 2: Enhanced features
   - Phase 3: Scale and optimization
   - Specific tasks per phase (checkbox list, verb-led, ≤14 words each)

4. SECURITY REQUIREMENTS
   - Authentication method
   - Authorization rules
   - Data protection requirements
   - Input validation rules

5. TESTING STRATEGY
   - Unit tests / Integration tests / User acceptance tests

6. DEPLOYMENT PLAN
   - Environment setup / CI/CD approach / Monitoring requirements

Rules:
- Every feature must be in a user story before being designed
- Security requirements listed before feature list
- Phase 1 must be deployable and usable on its own
- Data model must include all relationships and constraints

Output: Complete specification document in the sections above.
```

**Revenue connection:** A well-scoped spec reduces development time by 30-50% and eliminates scope creep. Sold as a scoping document: $500-$3,000 before a line of code is written.

---

# PART 5 — AI MONETIZATION PLAYBOOK

## The Three Sources of AI-Powered Revenue

Every profitable AI revenue model in professional services maps to one of three value sources:

| Value Source | What It Does | Example from the Repo |
|---|---|---|
| **Eliminates time** | Hours of work become minutes | Devin/Cursor coding agents |
| **Eliminates expertise gaps** | Capabilities most people don't have, on demand | Cluely for live calls, Perplexity for research |
| **Systematizes judgment** | Repeatable expert-level decisions at scale | Kiro's spec workflow, Manus's agent loop |

Know which one you're selling before designing the product or pricing the service.

---

## Revenue Model 1: AI-Augmented Advisory Services

Deliver professional advice faster and with better documentation by using AI to accelerate research, analysis, drafting, and reporting. Charge the same or higher fees. Invest 30-50% less time per deliverable. Take on more clients without burning out.

**AI applications:** Research memos in 15 minutes instead of 3 hours · Client reports from structured inputs · Tax plan summaries in 1 hour instead of 4 · Meeting prep and follow-up automated

**Implementation:**
1. Identify your 5 highest time-cost deliverables
2. Build a prompt template for each (T-11, T-13)
3. Test each template against 3 real engagements
4. Build an intake form capturing the inputs each template needs
5. Document the workflow as an SOP (T-14)
6. Calculate hourly rate improvement and raise prices

**Revenue target:** Saving 2 hours/client/month at $300/hour implicit rate = $600/client/month recovered. At 20 clients = $12,000/month effective rate increase.

---

## Revenue Model 2: Productized AI Services

Fixed-scope service powered by AI, delivered at scale with consistent quality.

**Examples:**
- "30-Day Tax Planning Report" — fixed deliverable, fixed price, AI-assisted production
- "Entity Structure Analysis" — AI-generated analysis with advisor review and sign-off
- "Content Package" — 30 days of platform content, AI-generated, human-edited

**Implementation:**
1. Choose one repetitive, time-intensive deliverable
2. Build the AI-assisted production workflow (T-16)
3. Define fixed scope, pricing, and "not included" boundaries (T-19)
4. Create a client intake form capturing all AI prompt inputs
5. Build a quality review checklist taking under 20 minutes
6. Price at 3-5x your AI production cost — the value is in the expertise that defines the process

**Revenue target:** A $1,500 tax planning report taking 2 hours to produce = $750/hour effective rate. At 10/month = $15,000 MRR.

---

## Revenue Model 3: AI-Powered Vertical Tools

Build and sell a specialized AI tool for a specific industry or professional audience.

**Examples:** Tax planning intake tool for CPAs · Client onboarding automation for law firms · Proposal generator for consultants · IRS notice triage tool · Lead qualification bot for financial advisors

**Implementation:**
1. Identify a repetitive judgment task in your industry taking 30+ minutes per instance
2. Define inputs, decision logic, and outputs (T-17 for app spec, T-15 for agent design)
3. Build a prototype using Claude API or similar
4. Validate with 3-5 domain experts in your target market
5. Price as a subscription ($99-$499/month for professional tools)
6. Go to market through industry associations, LinkedIn, and referral

**Revenue target:** $299/month × 100 subscribers = $29,900 MRR. At 70-80% gross margin, this is the highest-leverage revenue model in the stack.

---

## Revenue Model 4: AI Education and Training

Teach others in your industry how to use AI — through courses, workshops, consulting, or training programs.

**Products:**
- "AI for [Industry] Professionals" course: $197-$997
- "AI Implementation Workshop" for a firm or association: $2,000-$10,000
- "AI Adoption Consulting" done-with-you program: $5,000-$25,000
- "Prompt Library for [Industry]" template pack: $97-$497

**Implementation:**
1. Document your most impactful AI use cases in your domain
2. Build 3-5 flagship prompt templates (Part 4 is the model)
3. Create a lead magnet demonstrating AI value in your field (T-07)
4. Build an email sequence teaching one AI application per week (T-05)
5. Design a course around your top templates (T-06)
6. Launch to your existing audience first — 10 sales proves market demand

**Revenue target:** $497 course × 200 buyers = $99,400. Quarterly workshop at $3,000 for 15 attendees = $45,000/year from one format.

---

## Revenue Model 5: AI-Assisted Lead Generation

Use AI to dramatically improve volume and quality of lead generation — researching prospects, personalizing outreach, and nurturing leads at scale.

**Implementation:**
1. Build an ideal client profile with 5-7 specific qualifying characteristics
2. Use AI to research 20 prospects/week — company situation, recent news, specific pain points
3. Use T-10 to write personalized outreach messages for each prospect
4. Use T-05 to build a nurture sequence for non-responders
5. Use T-09 to systematize the sales call after a lead engages
6. Track: outreach sent / responses / calls booked / closes — optimize at each step

**Revenue target:** 20 personalized outreach messages/week at 15% response rate = 3 conversations/week. At 25% close rate and $3,000 average engagement = $9,000 MRR growth/month.

---

## Revenue Model 6: Scalable Content-to-Client Pipeline

Use AI-assisted content production to build a consistent authority presence that generates inbound leads.

**Implementation:**
1. Build your content operating system (T-08)
2. Use the content brief template to produce 3-5 posts/week in 30 minutes/day
3. Track which content generates the most engagement and inquiry
4. Repurpose every piece across LinkedIn, email, and your website
5. Build a lead magnet (T-07) for the top-performing content pillar

**Revenue target:** At 50,000 LinkedIn followers with 0.5% conversion to inquiry = 250 inquiries/year. At 20% close rate = 50 clients/year. This compounds — the content asset grows in value over time.

---

## AI Stack by Business Type

| Business Type | Core AI Tools | Revenue Application |
|---|---|---|
| Solo CPA / Tax Advisor | Claude API, ChatGPT | Research memos, client reports, planning docs |
| Accounting Firm | Claude API + Make/Zapier | Client onboarding, tax research, review checklists |
| Consultant / Coach | Claude, v0, Make | Lead gen, content, proposal generation |
| Agency | Claude + content system | Client delivery, reporting, SOPs |
| Product Builder | Claude API + app framework | Vertical SaaS tools, AI-powered features |
| Educator / Course Creator | Claude for content | Course creation, content system, lead magnets |

---

# PART 6 — ACCOUNTING AND TAX AI SECTION

## Why This Vertical Is Uniquely Positioned

The accounting and tax profession combines:
- **Repetitive, structured analysis** — ideal for prompt-driven automation
- **High-stakes client communication** — where AI-assisted drafting adds clarity and consistency
- **Explainable reasoning requirements** — where showing your work is required by the profession
- **Time-compressed seasonality** — where efficiency gains have multiplied value
- **Under-served by generic AI tools** — creating white space for domain-specific tools

All prompts below use AI as the production engine with human professional review as the quality gate.

---

## AT-01: TAX PLANNING TOOL

```
You are a CPA and tax strategist preparing a tax planning analysis for a client.
This analysis is a starting point for professional review — flag all items requiring verification or professional judgment.

CLIENT PROFILE:
Entity Type: [S-Corp / C-Corp / Partnership / LLC / Individual]
Revenue/Income: [$X range]
Current Deductions in Use: [list known deductions]
Key Events This Year: [acquisition / sale / compensation change / real estate / retirement account]
Planning Horizon: [current year / 3-year / retirement]

Produce:
1. CURRENT SITUATION SUMMARY (what we know about the client's tax profile — 1 paragraph)
2. KEY OPPORTUNITIES (3-7 specific strategies worth evaluating):
   For each:
   - Strategy name
   - How it applies to this specific client
   - Estimated annual tax impact ($ range — label as estimate)
   - Implementation requirements
   - Key risks or limitations
   - Confidence level: HIGH (established) / MEDIUM (fact-specific) / LOW (requires research)
3. PRIORITY RANKING (order by: estimated impact × ease of implementation)
4. PLANNING QUESTIONS (5-7 questions to ask the client)
5. RECOMMENDED NEXT STEPS (professional actions with timeline)
6. FLAGS FOR REVIEW (items requiring professional judgment, additional research, or missing information)

Rules:
- Never state specific tax savings without labeling as estimate
- Flag strategies subject to recent IRS scrutiny
- Include "does not apply if" conditions for each strategy
- Cite general code section for each strategy (e.g., "IRC § 199A")
- Include professional disclaimer — this is planning analysis, not tax advice

Output: Professional tax planning memo formatted for advisor review.
```

**Revenue connection:** Enables completing initial tax planning analyses in 60-90 minutes instead of 3-4 hours. At 5 planning engagements/month at $1,500-$3,000 each = $7,500-$15,000/month with 60% less production time.

---

## AT-02: CLIENT INTAKE AUTOMATION

```
You are building a client intake system for a professional accounting firm.

FIRM TYPE: [CPA firm / solo practitioner / tax advisor]
CLIENT TYPE: [individual / small business / high-net-worth]
SERVICES: [tax preparation / tax planning / advisory / bookkeeping]
INTAKE METHOD: [web form / email questionnaire / portal]

Build:
1. INTAKE QUESTIONNAIRE (organized by section):
   Section 1: Business/Personal Profile (5-8 questions)
   Section 2: Current Situation (5-8 questions — pain points, prior issues)
   Section 3: Goals and Priorities (3-5 questions)
   Section 4: Documentation Needed (checklist)
   Section 5: Expectations (fees, process, communication preferences)

2. AUTOMATED FOLLOW-UP SEQUENCE (3 emails post-submission):
   Email 1 (immediate): Confirmation + next steps
   Email 2 (Day 2): Document checklist reminder
   Email 3 (Day 5): Scheduling link for kickoff call

3. INTERNAL ONBOARDING CHECKLIST (what the firm does before the first client meeting):
   [ ] Review intake form
   [ ] Pull prior returns (if applicable)
   [ ] Check for open IRS notices
   [ ] Prepare preliminary observations
   [ ] Set up client file and portal access
   [ ] Confirm fee agreement

4. KICKOFF CALL AGENDA (30-45 minutes):
   - Review intake summary (5 min)
   - Confirm situation and goals (10 min)
   - Explain your process (5 min)
   - Identify missing information (5 min)
   - Set expectations and next steps (10 min)

5. RED FLAGS CHECKLIST (8-10 issues to identify during intake affecting scope or risk)

Output: Complete intake system ready for implementation.
```

**Revenue connection:** Systematized intake reduces onboarding time per client by 2-4 hours. For a firm with 100 new clients/year = 200-400 hours recovered.

---

## AT-03: TAX RETURN REVIEW SUPPORT

```
You are a tax quality control specialist building a review framework.

RETURN TYPE: [1040 / 1120S / 1065 / 1120]
FIRM SIZE: [solo / small firm / mid-size]

Build:
1. PRE-REVIEW CHECKLIST (10-15 items to check before opening the return)

2. ANALYTICAL REVIEW PROCEDURES (8-12 ratio-based tests):
   For each: what to calculate / threshold that triggers a flag / what to do when flagged
   Example (1040): "Compare W-2 income to prior year — flag >20% variance"
   Example (1120S): "Compare officer compensation to prior year — flag <$100,000 if profitable"

3. SCHEDULE-BY-SCHEDULE REVIEW CHECKLIST:
   For each relevant schedule: required items to verify, common errors, quick checks

4. CROSS-SCHEDULE CONSISTENCY CHECKS:
   Items that must agree between schedules (basis, carryforward, intercompany)

5. DISCLOSURE REVIEW:
   Required disclosures for the return type

6. FINAL SIGN-OFF CHECKLIST (10-12 items — must be true before preparer marks complete)

7. REVIEWER INQUIRY LOG TEMPLATE:
   Description / Preparer response / Reviewer decision / Resolution

Rules:
- Every item must be verifiable — not "review for accuracy" — specify what to look for
- Flag known audit triggers for elevated scrutiny
- Mark items changed by recent legislation [NEW/CHANGED]

Output: Complete review framework as a working QC document.
```

**Revenue connection:** Standardized review reduces review time 30-50% while improving accuracy. For a firm processing 300 returns with 2 hours review each, this recovers 180-300 hours per season.

---

## AT-04: ENTITY STRUCTURE ANALYSIS

```
You are a tax strategist performing an entity structure analysis.

CLIENT SITUATION:
Current Entity: [Sole Prop / LLC / S-Corp / C-Corp / Partnership]
Annual Net Income: [$X range]
Owner Situation: [number of owners, other income, state of residence]
Business Type: [industry, active vs. passive, asset-heavy vs. service]
Long-Term Plans: [hold / sell / pass down / expand]
Current SE/Payroll Taxes Paid: [$X estimated]

For each structure (Sole Prop / SMLLC / S-Corp / C-Corp / Partnership):
1. APPLIES TO THIS CLIENT: [yes / no / conditionally — explain why]
2. TAX TREATMENT SUMMARY (3-4 sentences — how income is taxed)
3. ESTIMATED ANNUAL TAX IMPACT (range, labeled as estimate, show calculation logic)
4. KEY BENEFITS FOR THIS CLIENT (specific to their situation)
5. KEY RISKS OR LIMITATIONS
6. IMPLEMENTATION REQUIREMENTS (what it takes to set up or convert)
7. ADMINISTRATIVE BURDEN (ongoing compliance requirements)

COMPARISON TABLE:
| Structure | Est. Annual Tax | SE/FICA Impact | Admin Burden | Best For |

RECOMMENDATION:
- Recommended structure + rationale
- Implementation timeline
- Conditions that would change this recommendation

FLAGS FOR PROFESSIONAL REVIEW:
- Items requiring verification, research, or state-specific analysis

Rules:
- All estimates must show calculation logic and be labeled as estimates
- State-specific implications must be flagged — this is federal only unless specified
- S-Corp reasonable compensation analysis must be included if S-Corp is recommended

Output: Professional entity analysis memo formatted for advisor review.
```

**Revenue connection:** Entity analysis engagements typically range $500-$3,000. AI-assisted, the work that took 4-6 hours now takes 1-2. Can be offered as a productized service.

---

## AT-05: IRS NOTICE RESPONSE WORKFLOW

```
You are building an IRS notice response system for a professional tax firm.

NOTICE TYPE: [CP2000 / CP14 / CP501 / Letter 1058 / 4549 / other] OR ["build a general triage system"]

For a SPECIFIC notice type:
1. NOTICE SUMMARY (what this means in plain language — for client communication)
2. URGENCY CLASSIFICATION (immediate / 30 days / 60 days / informational)
3. INFORMATION REQUIRED FROM CLIENT (exact documents and data needed before responding)
4. ANALYSIS FRAMEWORK (how to evaluate: agree / disagree / partially agree)
5. RESPONSE OPTIONS (pros/cons for each)
6. DRAFT RESPONSE TEMPLATE (professional letter with [PLACEHOLDER] fields)
7. FOLLOW-UP PROTOCOL (what to track after sending)
8. CLIENT COMMUNICATION TEMPLATE (how to explain this notice and response to client)

For a GENERAL TRIAGE SYSTEM:
1. NOTICE INTAKE CHECKLIST (what to do when a notice arrives — first 48 hours)
2. NOTICE CLASSIFICATION MATRIX (urgency / response type / typical resolution path)
3. ESCALATION CRITERIA (when to involve a senior professional)
4. CLIENT NOTIFICATION SCRIPT (what to say when calling a client about an IRS notice)
5. RESPONSE TRACKING SYSTEM (fields and update frequency)
6. COMMON NOTICE LIBRARY (20+ most common notices with description, urgency, and typical response)

Output: Complete notice response system or specific notice analysis with response template.
```

**Revenue connection:** A systematized notice response process enables a firm to handle 2-3x more notices per preparer-hour. Billed at $200-$500/hour — systematization creates significant margin.

---

## AT-06: RESEARCH MEMO GENERATION

```
You are a tax researcher preparing a research memo for professional review.

RESEARCH QUESTION: [specific tax question — be precise]
CLIENT SITUATION: [relevant facts — entity type, transaction, amounts, timing]
JURISDICTION: [federal / state — specify state]

IMPORTANT: This memo is a research starting point. Flag all conclusions requiring verification with primary sources before relying on them in a return or client advice.

Structure:
1. ISSUE (the specific legal question — one sentence)
2. BRIEF ANSWER (2-3 sentences + confidence level)
3. FACTS (relevant client situation facts)
4. APPLICABLE AUTHORITY:
   - Primary authority (code sections, regulations, rulings — cite specifically)
   - Secondary authority (case law, IRS guidance if applicable)
   - Flag: where citation needs verification
5. ANALYSIS (apply authority to facts — one paragraph per legal principle):
   - State the rule → Apply to these facts → State the result
6. CONCLUSION (answer to the Issue based on Analysis)
7. ALTERNATIVE POSITIONS (if uncertainty exists, state the contrary position and basis)
8. PLANNING CONSIDERATIONS (opportunities or risks created by the conclusion)
9. ITEMS REQUIRING VERIFICATION (specific citations or conclusions that must be confirmed with primary sources — list explicitly)
10. RECOMMENDED NEXT STEPS

Rules:
- Never state a conclusion without citing authority
- Flag any reference that could not be verified from training knowledge
- If genuinely uncertain, say so — do not fabricate certainty
- Distinguish "established law" from "my interpretation of the authorities"
- Label all conclusions as preliminary pending professional verification

Output: Professional research memo formatted for internal use.
```

**Revenue connection:** Tax research memos billed at $300-$500/hour. AI-assisted, 45 minutes instead of 3 hours — the value is in the analysis and professional responsibility, not the typing.

---

## AT-07: ADVISORY REPORT GENERATION

```
You are a CPA and business advisor preparing an annual advisory report for a business client.

CLIENT PROFILE:
Business type: [industry, entity type, revenue]
Current year highlights: [key events, transactions, changes]
Prior year comparison: [performance vs. prior year]
Owner goals: [near-term / long-term]
REPORT PURPOSE: [annual review / transaction planning / succession / growth planning]

Build:
1. EXECUTIVE SUMMARY (what we found + what we recommend + what it means for the owner — max 300 words)
2. FINANCIAL PERFORMANCE REVIEW:
   - Revenue and income trends (current vs. prior year)
   - Key ratio analysis (profitability, cash, leverage)
   - Observations and implications
3. TAX SITUATION REVIEW:
   - Current year estimated liability / Comparison to prior year
   - Strategies implemented and impact / Strategies for next year
4. ENTITY AND STRUCTURE REVIEW:
   - Is the current entity still optimal?
   - Structural changes to consider?
5. OWNER WEALTH PICTURE:
   - Retirement savings status / Risk exposure / Estate and succession status
6. KEY RECOMMENDATIONS (5-7 specific, each with):
   - Priority (urgent / this year / multi-year)
   - Estimated financial impact
   - Owner action required
   - Timeline
7. IMPLEMENTATION TRACKER (Recommendation / Status / Owner / Deadline / Notes)
8. NEXT 12 MONTHS (specific milestones and meetings)

Rules:
- All financial figures labeled as actual, estimated, or projected
- Every recommendation must have an owner (advisor / client / both)
- Executive summary must be client-readable standalone
- Include "if we don't act" for every urgent recommendation

Output: Professional advisory report formatted for client delivery.
```

**Revenue connection:** Annual advisory reports are the foundation of a subscription advisory model. Firms delivering structured annual reviews retain clients at 90%+ vs. 70% for compliance-only. Advisory subscriptions: $5,000-$25,000/year.

---

## AT-08: CLIENT-FACING TAX EXPLAINER

```
You are writing a plain-language tax explanation for a non-professional client.

CONCEPT TO EXPLAIN: [specific tax topic, strategy, or situation]
CLIENT TYPE: [small business owner / individual / investor / professional]
CONTEXT: [why they're receiving this]
DEPTH: [brief overview (1 paragraph) / full explanation (1-2 pages) / FAQ format]

Write:
1. HEADLINE (what this is, in plain English — no jargon in the title)
2. THE SHORT ANSWER (2-3 sentences — what they need to know, simplest possible terms)
3. HOW IT WORKS (step-by-step with a specific example using round numbers):
   "Here's how this works in practice: Let's say you [specific scenario]..."
4. HOW THIS APPLIES TO YOU (1 paragraph specific to their situation)
5. WHAT YOU NEED TO DO (specific actions in simple terms):
   - [Action + when to do it + what it produces]
6. WHAT HAPPENS IF YOU DON'T (brief — cost of inaction in plain terms)
7. YOUR QUESTIONS ANSWERED (3-5 FAQ entries — common questions about this topic)
8. NEXT STEPS (specific — "Call us by [date]" or "Provide [document] before [date]")

Rules:
- Replace every technical term with plain language equivalent (or explain in parentheses on first use)
- Use specific dollar examples — not "significant savings"
- Never imply definite outcome without "estimated" or "in situations like yours"
- Sentences under 20 words wherever possible
- Write at 8th-grade reading level

Output: Client-ready explanation formatted for email or PDF delivery.
```

**Revenue connection:** Client-facing explainers build trust, reduce call volume, and serve as content marketing. A library of 20-30 explainers is a significant firm asset.

---

## AT-09: LEAD QUALIFICATION TOOL

```
You are building a lead qualification system for an accounting or tax practice.

IDEAL CLIENT PROFILE:
Revenue range: [$X - $Y]
Entity types: [list preferred entity types]
Industries: [preferred or excluded]
Service needs: [tax planning / compliance / advisory / bookkeeping]
Minimum engagement value: [$X]

Build:
1. QUALIFICATION SCORING MATRIX:
   Criteria | Weight | 1 Point | 2 Points | 3 Points
   Revenue fit | 30% | Below range | Low range | Sweet spot
   [Build 6-8 criteria with weights totaling 100%]
   Scoring: 15-18 = A-lead / 10-14 = B-lead / Under 10 = Not a fit

2. INTAKE QUESTIONS (5-7 questions that reveal the scoring criteria):
   - Question text / what it reveals / red flag answer (if any)

3. QUALIFICATION EMAIL TEMPLATE (for responding to an inbound lead)

4. NOT-A-FIT RESPONSE TEMPLATE (how to professionally decline a prospect who doesn't qualify)

5. A-LEAD NEXT STEPS SCRIPT (what to do when a lead scores high)

6. REFERRAL BACK SYSTEM (for leads that don't fit — who to refer them to and how)

Rules:
- Scoring matrix completable in under 5 minutes
- Every qualification question must have a clear "right answer" tied to your ICP
- The not-a-fit response must be professional and provide an alternative

Output: Complete lead qualification system.
```

**Revenue connection:** Eliminates 30-50% of low-fit discovery calls — saving 2-5 hours/week while improving close rates on remaining calls.

---

## AT-10: AI-ASSISTED SALES CALL PREP

```
You are preparing an accounting professional for a discovery call with a prospective client.

PROSPECT INFORMATION:
Business name and type: [available info]
Contact name and role: [name and role]
Source of referral: [who referred them and context]
What they said they need: [from initial contact]
Known facts about their situation: [any information already gathered]

Prepare:
1. SITUATION HYPOTHESIS (likely tax/financial situation, pain points, goals — label as hypothesis)
2. CALIBRATED DISCOVERY QUESTIONS (8-10 questions ordered from rapport to deep pain):
   For each: question text / what it reveals / what to listen for
3. ANTICIPATED OBJECTIONS AND RESPONSES:
   For this type of prospect:
   - Objection 1 → specific, non-generic response
   - Objection 2 → response
   - Objection 3 → response
4. VALUE POSITIONING (how to position your services for this specific prospect):
   - Key differentiator to emphasize
   - Specific relevant outcome to mention
5. CALL AGENDA (15-minute structure):
   0-2 min: Rapport and confirm agenda
   2-8 min: Discovery (top 4 questions)
   8-12 min: Summarize and position
   12-15 min: Next steps
6. POST-CALL FOLLOW-UP TEMPLATE (email within 2 hours — summarizes what you heard, confirms next steps, reinforces value)

Output: Complete call prep document formatted for quick pre-call review.
```

**Revenue connection:** Calls prepared with this framework close at 2-3x the rate of unprepared calls.

---

## AT-11: INTERNAL PREPARER / REVIEWER CHECKLIST

```
You are building an internal quality control checklist for a tax preparation firm.

RETURN TYPE: [1040 / 1120S / 1065 / 1120 / other]
AUDIENCE: [preparer / reviewer / both]

PREPARER CHECKLIST (verify before submitting for review):

Part 1: Setup and Source Documents
[ ] [specific item]
[ ] [specific item]
[10-15 items specific to return type]

Part 2: Return Mechanics
[ ] [specific computational check]
[ ] [specific comparison to prior year]
[10-15 items]

Part 3: Credits and Deductions
[ ] [specific credit/deduction verification]
[8-12 items]

Part 4: Elections and Disclosures
[ ] [required election]
[ ] [required disclosure]
[5-8 items]

Part 5: Final Review
[5-7 self-review items]

REVIEWER CHECKLIST:

Part 1: Analytical Review
[8-12 ratio and comparison checks with specific thresholds that trigger a flag]

Part 2: High-Risk Items
[8-12 items known to attract IRS attention for this return type]

Part 3: Client Communication
[client-facing items to verify before delivery]

SIGN-OFF PROTOCOL:
- Preparer sign-off criteria
- Reviewer sign-off criteria
- Partner/principal review threshold (dollar amount or complexity trigger)

Rules:
- Every item must be a specific, verifiable check — not a general category
- Include the "why it matters" for high-risk items
- Flag items changed by recent legislation with [NEW/CHANGED]

Output: Complete checklist formatted as a working document.
```

**Revenue connection:** A well-built QC checklist reduces errors, reduces professional liability exposure, and reduces review time by 20-40% by catching issues at the preparer level.

---

## AT-12: CLIENT EDUCATION CONTENT

```
You are creating a client education asset for an accounting or tax firm.

ASSET TYPE: [newsletter article / email tip / FAQ document / webinar outline]
AUDIENCE: [small business owners / high-net-worth / real estate investors / professionals]
TOPIC: [specific tax or financial topic]
PURPOSE: [educate / build authority / generate leads / retain clients]
LENGTH: [short — 300 words / medium — 800 words / long — 1500+ words]

Create:
1. HEADLINE (specific promise to the target reader — not clever, not vague)
2. OPENING HOOK (first 2 sentences — surprising stat, specific mistake, or common misconception)
3. CORE CONTENT (3-5 key points with specific examples and numbers):
   For FAQs: 8-12 questions with concise, specific answers
   For webinar: sections with key messages and engagement moments
4. PRACTICAL TAKEAWAY (one specific action the reader can take this week)
5. CALL TO ACTION (natural, not a hard sell)
6. PROFESSIONAL DISCLAIMER (brief — for tax content)

Rules:
- Every piece must teach something usable regardless of whether they hire you
- Include at least one specific number or example — no vague claims
- Write at the target audience's knowledge level
- CTA must be natural

Output: Complete asset formatted for distribution.
```

---

## Productizable AI Tool Ideas for Accounting and Tax

These are complete tool concepts ready to build using T-15 (AI Agent Design) and T-17 (App Development Spec):

| Tool | Input | Output | Target Market | Pricing Model |
|---|---|---|---|---|
| Tax Profile Analyzer | Client tax documents, prior return | Prioritized planning opportunities with estimated impact | CPA firms, financial advisors | $199-$499/month per firm |
| Entity Comparison Calculator | Business profile (income, owners, state) | Side-by-side entity structure comparison | Attorneys, CPAs, business advisors | $99-$299/month or $49/report |
| IRS Notice Triage Bot | Notice type + client situation | Urgency, required docs, response options, draft response | CPA firms, EA firms | $299-$799/month |
| Tax Planning Memo Generator | Client intake form | Draft planning memo with strategies and review flags | Solo CPAs, small firms | $149-$399/month or $29/memo |
| Annual Review Generator | Financial statements, prior year return, goals | Draft advisory report | CPA firms with advisory practices | $499-$999/month |
| Client Education Platform | Topic + audience type | Plain-language articles, FAQs, explainers | CPA firms building content | $99-$299/month |
| Proposal Generator | Prospect info + services + fee range | Professional proposal with scope and investment | Solo practitioners and small firms | $79-$149/month |
| Discovery Call Prep Tool | Prospect information + service type | Research summary, questions, objections, agenda | Growth-focused CPA firms | $199-$399/month |

---

# CLOSING FRAMEWORK: THE AI MONETIZATION DECISION TREE

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
Every AI-powered revenue stream starts with a prompt:
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

---

> The competitive advantage is not the AI. The AI is available to everyone.
>
> The competitive advantage is the expertise that defines the prompts, the methodology that structures the workflow, and the professional judgment that reviews the output.
>
> That is not replicable. Build on that.

---

*Built by reverse-engineering production system prompts from Manus, Devin, Cursor, Kiro, Cluely, v0, Perplexity, Lovable, Warp, and Orchids — the most architecturally sophisticated AI tools in production as of 2025-2026. All templates are starting points requiring adaptation to specific professional situations. Nothing here constitutes legal, tax, or professional advice.*
