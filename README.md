# CODEX PLUGINS

A Codex plugin workspace to rule them all, unlocking superpowers across
open-source ecosystems, enterprise platforms, and modern CLI-driven stacks.

```text
 ██████╗ ██████╗ ██████╗ ███████╗██╗  ██╗    ██████╗ ██╗     ██╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝╚██╗██╔╝    ██╔══██╗██║     ██║   ██║██╔════╝ ██║████╗  ██║██╔════╝
██║     ██║   ██║██║  ██║█████╗   ╚███╔╝     ██████╔╝██║     ██║   ██║██║  ███╗██║██╔██╗ ██║███████╗
██║     ██║   ██║██║  ██║██╔══╝   ██╔██╗     ██╔═══╝ ██║     ██║   ██║██║   ██║██║██║╚██╗██║╚════██║
╚██████╗╚██████╔╝██████╔╝███████╗██╔╝ ██╗    ██║     ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║███████║
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
```

## What Codex plugins can do today (planner style)

- [x] Create web apps quickly
  - [x] Build and refine Next.js-style product UIs with `build-web-apps` (`frontend-skill`, `react-best-practices`, `shadcn-best-practices`).
  - [x] Turn Figma designs into implementation tasks and component mappings with `figma` (`figma-implement-design`, `figma-code-connect-components`, `figma-create-design-system-rules`).
  - [x] Convert code changes into GitHub branches/PRs and verified auto-publish flows with `github` (`yeet`, `auto-publish-after-plan`, `github`, `gh-address-comments`).
  - [x] Add payments and database architecture safely with `stripe` (`stripe-best-practices`) and `supabase` (`setup`, `supabase-usage`, `cli`).

- [x] Design and visual iteration workflows
  - [x] Run design-to-code loops using `figma` plus UI refinement in `build-web-apps`.
  - [x] Test and verify web output in browser flows with `vercel` (`agent-browser`, `agent-browser-verify`, `verification`).
  - [x] Structure storefront/admin UX work for commerce projects with `medusa` and `saleor` skills.
  - [x] Iterate safely with branching and review workflows via `github` and `superpowers`.

- [x] Development tools you can run now
  - [x] Use structured implementation workflows from `superpowers` (planning, debugging, TDD, verification, code review).
  - [x] Run the full OMX workflow layer with `omx` (`deep-interview`, `ralplan`, `ralph`, `team`) and setup compatibility skills.
  - [x] Optimize prompt/token efficiency with `prompt-optimizer` (`prompt-optimizer`) for concise, reusable request patterns.
  - [x] Use Merchant API-focused integration/migration guidance with `google` (`mapi-developer-assistant`).
  - [x] Run plugin-specific CLI workflows with `supabase` (`cli`) and `resend` (`resend-cli`).
  - [x] Remove image backgrounds and prepare transparent assets with `rembg` (`rembg`).
  - [x] Run local filesystem and terminal automation workflows with `desktop-commander` (`desktop-commander-ops`).
  - [x] Standardize container build, compose, publish, and debug loops with `docker` (`docker-build-local-images`, `docker-compose-dev-loop`, `docker-publish-images`, `docker-debug-containers`).
  - [x] Use integration-focused workflows for cloud/platform ops with `aws`, `cloudflare`, `vercel`, and `netlify`.
  - [x] Triage production signals with `sentry` and feed fixes into repo workflows with `github`.

- [x] Deploy and ship faster
  - [x] Deploy and operate web apps with `vercel` (`deployments-cicd`, `vercel-cli`, `env-vars`, `observability`).
  - [x] Deploy to Netlify with `netlify` (`netlify-deploy`).
  - [x] Manage production-ready delivery flows from implementation to PR using `github` + `superpowers`.
  - [x] Support links/domains/env management through deployment and platform skills in `vercel` and `netlify`.

- [x] Collaboration and coordination
  - [x] Summarize channels, draft replies, and build digests with `slack` skills.
  - [x] Triage inboxes and draft email responses with `gmail`.
  - [x] Schedule and coordinate team calendars with `google-calendar`.
  - [x] Capture planning/research/meeting knowledge with `notion`.
  - [x] Add annotation-driven developer feedback loops in React apps with `agentation`.

- [x] Advanced AI and platform capabilities
  - [x] Build AI-enabled app flows with `vercel` (`ai-sdk`, `ai-elements`, `ai-gateway`, `chat-sdk`).
  - [x] Configure and use MCP-backed workflows in supported plugins (`vercel`, `supabase`, `cloudflare`, `aws`, `medusa`, `resend`, `hugging-face`, `agentation`, `build-web-apps`, `desktop-commander`).
  - [x] Explore models, datasets, eval, and inference workflows with `hugging-face`.
  - [x] Build agent/runtime systems on edge/cloud with `cloudflare`, `aws`, and `vercel` skills.

- [x] Broad project support
  - [x] Web frameworks/platforms: strong support via `vercel`, `netlify`, `build-web-apps`, `cloudflare`.
  - [x] Mobile: `build-ios-apps` (SwiftUI) and `test-android-apps` (emulator QA).
  - [x] Commerce: `medusa`, `saleor`, and `google` (Merchant API skill support).
  - [x] Productivity/workspace automation: `google-drive`, `gmail`, `google-calendar`, `slack`, `notion`, `box`, `linear`, `prompt-optimizer`, `rembg`, `omx`.

- [x] Auto-generate top-skill blocks and skill counts from plugin metadata/scripts.

## README maintenance policy (enforced)

This repository follows strict governance in [AGENTS.md](./AGENTS.md):

- Every meaningful change requires a root `README.md` quality check and update pass if stale.
- Any plugin add/rename/remove/update must sync planner block, lineup/capabilities, roadmap/TODO, setup/update instructions, and generated catalog surfaces.
- Work is incomplete until plugin metadata and README surfaces are synchronized.

### When adding a new plugin

- Add plugin scaffold/metadata and ensure names match final lineup wording.
- Add or update plugin metadata and marketplace entry, then regenerate catalog surfaces.
- Update `What Codex plugins can do today (planner style)` when capability coverage changes.
- Update `What to add next (TODO roadmap)` by removing newly delivered items and/or adding follow-up gaps.
- Validate setup/update instructions if the plugin introduces new prerequisites or bootstrap steps.
- Re-run docs consistency checks before merge:
  - `python3 scripts/generate_readme_catalog.py`
  - `python3 scripts/validate_plugin_quality.py`

### What to add next (TODO roadmap)

#### P0 — Platform coverage next

- [ ] Google Cloud plugin — Build/deploy/troubleshoot Cloud Run, GKE, Cloud SQL, and Vertex AI workloads.
- [ ] Azure plugin — Ship and operate AKS/App Service/Cosmos workloads with Azure-native workflows.
- [ ] GitLab plugin — Manage merge requests, CI pipelines, and repo triage outside GitHub.
- [ ] Jira plugin — Link implementation work to issue triage, sprint flow, and delivery status.
- [ ] Kubernetes plugin — Diagnose cluster/app rollout issues with kubectl-first operational workflows.
- [x] Docker plugin — Standardize local container build, compose, publish, and debug flows.
- [ ] Firebase plugin — Support Auth, Firestore, Hosting, and Functions workflows.
- [ ] Render/Railway/Fly.io plugins — Expand non-Vercel/Netlify deployment coverage.

#### P1 — Productivity and collaboration expansion

- [ ] Microsoft Teams plugin — Summaries, update drafts, and channel coordination workflows.
- [ ] Discord plugin — Community/moderation summaries and outbound messaging workflows.
- [ ] Confluence plugin — Capture specs/runbooks and connect engineering docs to implementation tasks.
- [ ] Asana plugin — Convert project tasks into execution-ready engineering workflows.
- [ ] Trello plugin — Board triage and task lifecycle workflows for smaller teams.

#### P2 — AI workflow depth and automation

- [ ] Cross-plugin workflow chains — Reusable templates that chain design, code, deploy, and comms steps.
- [x] Capability matrix generator — Auto-generate planner/lineup capability blocks from plugin metadata.
- [x] Plugin maturity labels — Track alpha/beta/stable status for each plugin in README.
- [x] Validation coverage indicators — CI-enforced sync and quality checks for plugin metadata/docs.
- [ ] Guided “best plugin for task” router — Add decision helpers for picking the right plugin path fast.

## 2-minute setup

Clone and open the repo (any location is fine):

```bash
git clone https://github.com/openwebu/codex-plugins.git
cd codex-plugins
```

### Linux

```bash
bash scripts/install_linux.sh
```

### Windows (Git Bash)

```bash
bash scripts/install_windows.sh
```

## Step-by-step tutorial

Use this quick flow to go from install to your first plugin scaffold.

**Format:** each step has what to run, what to verify, and a screenshot.
**Time:** ~2 to 3 minutes.

### Step 1: Install and link the plugin workspace

Run one command based on your OS:

```bash
# Linux
bash scripts/install_linux.sh

# Windows (Git Bash)
bash scripts/install_windows.sh
```

Verify that no errors are shown and the script completes.

![Step 1 - install and link workspace](./public/tutorial-step-1.png)

### Step 2: Verify symlink and marketplace wiring

Run the validation commands:

```bash
ls -l "$HOME/plugins"
ls -l "$HOME/.agents/plugins/marketplace.json"
scripts/sync_plugins_to_marketplace.py --dry-run
```

Expected result:
- `~/plugins` points to this repository's `plugins/` directory.
- `~/.agents/plugins/marketplace.json` points to this repository marketplace file.

![Step 2 - verify setup](./public/tutorial-step-2.png)

### Step 3: Generate your first plugin scaffold

Create your first plugin:

```bash
bash scripts/new-plugin.sh my-plugin
```

The script scaffolds the plugin, syncs marketplace metadata, and prints the next git commands to run.
It wraps the canonical Python scaffolder at `.agents/skills/plugin-creator/scripts/create_basic_plugin.py`.

![Step 3 - create first plugin](./public/tutorial-step-3.png)

## Check it worked

```bash
ls -l "$HOME/plugins"
ls -l "$HOME/.agents/plugins/marketplace.json"
scripts/sync_plugins_to_marketplace.py --dry-run
```

Expected:

- `~/plugins` points to this repo `plugins/`
- `~/.agents/plugins/marketplace.json` points to this repo marketplace

## Add your first plugin

```bash
bash scripts/new-plugin.sh my-plugin
```

This creates the plugin scaffold, syncs marketplace, and prints the exact `git add`, `git commit`, and `git push` commands.

## Plugin update expectations

When changing an existing plugin (skills, metadata, naming, capabilities):

- Update the plugin's local documentation as needed.
- Update root README capability/lineup/roadmap/setup sections affected by the change.
- Confirm cross-platform wording remains accurate (open-source + enterprise + CLI ecosystem coverage).
- Treat missing README synchronization as incomplete work.

## Need advanced options?

See [docs/setup-reference.md](docs/setup-reference.md) for:

- manual setup commands
- advanced scaffold options (still through `scripts/new-plugin.sh`)
- repo structure and optional plugin surfaces
- troubleshooting notes

## Current plugin lineup

This section is generated from plugin manifests and `.agents/plugins/marketplace.json`.

<!-- BEGIN AUTO:PLUGIN_LINEUP -->
### Productivity

#### [`linear`](./plugins/linear)

Find and reference issues and projects.

- Top skills: `linear`
- Skill count: `1`
- Maturity: `unspecified`

#### [`google-calendar`](./plugins/google-calendar)

Manage Google Calendar events and schedules

- Top skills: `google-calendar`, `google-calendar-daily-brief`, `google-calendar-free-up-time`, `google-calendar-group-scheduler`
- Additional skills: `google-calendar-meeting-prep`
- Skill count: `5`
- Maturity: `unspecified`

#### [`gmail`](./plugins/gmail)

Read and manage Gmail

- Top skills: `gmail`, `gmail-inbox-triage`
- Skill count: `2`
- Maturity: `unspecified`

#### [`slack`](./plugins/slack)

Read and manage Slack

- Top skills: `slack`, `slack-channel-summarization`, `slack-daily-digest`, `slack-notification-triage`
- Additional skills: `slack-outgoing-message`, `slack-reply-drafting`
- Skill count: `6`
- Maturity: `unspecified`

#### [`jam`](./plugins/jam)

Screen record with context

- Top skills: `jam-bug-triage`
- Skill count: `1`
- Maturity: `unspecified`

#### [`stripe`](./plugins/stripe)

Payments and business tools

- Top skills: `stripe-best-practices`, `upgrade-stripe`
- Skill count: `2`
- Maturity: `unspecified`

#### [`box`](./plugins/box)

Search and reference your documents

- Top skills: `box`
- Skill count: `1`
- Maturity: `unspecified`

#### [`google-drive`](./plugins/google-drive)

Work across Drive, Docs, Sheets, and Slides

- Top skills: `google-docs`, `google-drive`, `google-sheets`, `google-sheets-chart-builder`
- Additional skills: `google-sheets-formula-builder`, `google-slides`, `google-slides-import-presentation`, `google-slides-template-migration`, `google-slides-template-surgery`, `google-slides-visual-iteration`
- Skill count: `10`
- Maturity: `unspecified`

#### [`notion`](./plugins/notion)

Notion workflows for specs, research, meetings, and knowledge capture

- Top skills: `notion-knowledge-capture`, `notion-meeting-intelligence`, `notion-research-documentation`, `notion-spec-to-implementation`
- Skill count: `4`
- Maturity: `unspecified`

#### [`resend`](./plugins/resend)

Send and manage email with Resend

- Top skills: `resend-cli`
- Skill count: `1`
- Maturity: `unspecified`

#### [`prompt-optimizer`](./plugins/prompt-optimizer)

Lower token usage without losing intent

- Top skills: `prompt-optimizer`
- Skill count: `1`
- Maturity: `unspecified`

#### [`rembg`](./plugins/rembg)

Remove image backgrounds with rembg

- Top skills: `rembg`
- Skill count: `1`
- Maturity: `unspecified`

### Design

#### [`canva`](./plugins/canva)

Search, create, edit designs

- Top skills: `canva-branded-presentation`, `canva-resize-for-all-social-media`, `canva-translate-design`
- Skill count: `3`
- Maturity: `unspecified`

#### [`figma`](./plugins/figma)

Design-to-code workflows powered by the Figma integration

- Top skills: `figma-code-connect-components`, `figma-create-design-system-rules`, `figma-create-new-file`, `figma-generate-design`
- Additional skills: `figma-generate-library`, `figma-implement-design`, `figma-use`
- Skill count: `7`
- Maturity: `unspecified`

### Coding

#### [`hugging-face`](./plugins/hugging-face)

Inspect models, datasets, Spaces, and research

- Top skills: `cli`, `community-evals`, `datasets`, `gradio`
- Additional skills: `jobs`, `llm-trainer`, `paper-publisher`, `papers`, `trackio`, `transformers.js`, `vision-trainer`
- Skill count: `11`
- Maturity: `unspecified`

#### [`netlify`](./plugins/netlify)

Deploy projects and manage releases

- Top skills: `netlify-deploy`
- Skill count: `1`
- Maturity: `unspecified`

#### [`vercel`](./plugins/vercel)

Vercel ecosystem guidance for Codex

- Top skills: `agent-browser`, `agent-browser-verify`, `ai-elements`, `ai-gateway`
- Additional skills: `ai-generation-persistence`, `ai-sdk`, `auth`, `bootstrap`, `chat-sdk`, `cms`, `cron-jobs`, `deployments-cicd`, `email`, `env-vars`, `geist`, `geistdocs`, `investigation-mode`, `json-render`, `marketplace`, `micro`, `ncc`, `next-forge`, `nextjs`, `observability`, `payments`, `react-best-practices`, `routing-middleware`, `runtime-cache`, `satori`, `shadcn`, `sign-in-with-vercel`, `swr`, `turbopack`, `turborepo`, `v0-dev`, `vercel-agent`, `vercel-api`, `vercel-cli`, `vercel-firewall`, `vercel-flags`, `vercel-functions`, `vercel-queues`, `vercel-sandbox`, `vercel-services`, `vercel-storage`, `verification`, `workflow`
- Skill count: `47`
- Maturity: `unspecified`

#### [`game-studio`](./plugins/game-studio)

Design, prototype, and ship browser games

- Top skills: `game-playtest`, `game-studio`, `game-ui-frontend`, `phaser-2d-game`
- Additional skills: `react-three-fiber-game`, `sprite-pipeline`, `three-webgl-game`, `web-3d-asset-pipeline`, `web-game-foundations`
- Skill count: `9`
- Maturity: `unspecified`

#### [`github`](./plugins/github)

Triage PRs, issues, CI, and publish flows

- Top skills: `auto-publish-after-plan`, `gh-address-comments`, `gh-fix-ci`, `github`
- Additional skills: `yeet`
- Skill count: `5`
- Maturity: `unspecified`

#### [`cloudflare`](./plugins/cloudflare)

Cloudflare platform guidance with official MCP

- Top skills: `agents-sdk`, `building-ai-agent-on-cloudflare`, `building-mcp-server-on-cloudflare`, `cloudflare`
- Additional skills: `durable-objects`, `sandbox-sdk`, `web-perf`, `workers-best-practices`, `wrangler`
- Skill count: `9`
- Maturity: `unspecified`

#### [`sentry`](./plugins/sentry)

Inspect recent Sentry issues and events

- Top skills: `sentry`
- Skill count: `1`
- Maturity: `unspecified`

#### [`build-ios-apps`](./plugins/build-ios-apps)

Build, refine, and debug iOS apps with SwiftUI and Xcode workflows

- Top skills: `ios-debugger-agent`, `swiftui-liquid-glass`, `swiftui-performance-audit`, `swiftui-ui-patterns`
- Additional skills: `swiftui-view-refactor`
- Skill count: `5`
- Maturity: `unspecified`

#### [`build-web-apps`](./plugins/build-web-apps)

Build, review, ship, and scale web apps across UI, React, deployment, payments, and databases

- Top skills: `deploy-to-vercel`, `frontend-skill`, `react-best-practices`, `shadcn-best-practices`
- Additional skills: `stripe-best-practices`, `supabase-best-practices`, `web-design-guidelines`
- Skill count: `7`
- Maturity: `unspecified`

#### [`test-android-apps`](./plugins/test-android-apps)

Reproduce issues, inspect UI, and capture evidence from Android emulators

- Top skills: `android-emulator-qa`
- Skill count: `1`
- Maturity: `unspecified`

#### [`aws`](./plugins/aws)

AWS implementation workflows and MCP tooling

- Top skills: `aws-openai-workflow`, `aws-workflow`
- Skill count: `2`
- Maturity: `unspecified`

#### [`medusa`](./plugins/medusa)

Build Medusa backend, admin, and storefront features with guided skills

- Top skills: `building-admin-dashboard-customizations`, `building-storefronts`, `building-with-medusa`, `db-generate`
- Additional skills: `db-migrate`, `learning-medusa`, `new-user`, `plugin-catalog`, `storefront-best-practices`
- Skill count: `9`
- Maturity: `unspecified`

#### [`agentation`](./plugins/agentation)

Add in-app annotations and sync them to MCP-enabled coding agents

- Top skills: `agentation`
- Skill count: `1`
- Maturity: `unspecified`

#### [`saleor`](./plugins/saleor)

Saleor storefront build guidance

- Top skills: `saleor-paper-storefront`
- Skill count: `1`
- Maturity: `unspecified`

#### [`supabase`](./plugins/supabase)

Supabase MCP + setup/usage/CLI workflows

- Top skills: `cli`, `setup`, `supabase-usage`
- Skill count: `3`
- Maturity: `unspecified`

#### [`ssh-skill`](./plugins/ssh-skill)

Secure SSH profile setup and remote Supabase workflows

- Top skills: `remote-supabase-ops`, `setup-profile`
- Skill count: `2`
- Maturity: `unspecified`

#### [`superpowers`](./plugins/superpowers)

Structured engineering workflows for Codex sessions

- Top skills: `brainstorming`, `dispatching-parallel-agents`, `executing-plans`, `finishing-a-development-branch`
- Additional skills: `receiving-code-review`, `requesting-code-review`, `subagent-driven-development`, `systematic-debugging`, `test-driven-development`, `using-git-worktrees`, `using-superpowers`, `verification-before-completion`, `writing-plans`, `writing-skills`
- Skill count: `14`
- Maturity: `unspecified`

#### [`docker`](./plugins/docker)

Container build, compose, publish, and debug workflows in Codex

- Top skills: `audit-go-dependencies`, `bump-go-dependencies`, `docker-build-local-images`, `docker-compose-dev-loop`
- Additional skills: `docker-debug-containers`, `docker-publish-images`, `plan-go-major-upgrades`, `triage-go-vulnerabilities`
- Skill count: `8`
- Maturity: `unspecified`

#### [`desktop-commander`](./plugins/desktop-commander)

Local filesystem and terminal superpowers via MCP

- Top skills: `desktop-commander-ops`
- Skill count: `1`
- Maturity: `unspecified`

#### [`omx`](./plugins/omx)

Complete oh-my-codex workflow skill pack

- Top skills: `deep-interview`, `ralplan`, `ralph`, `team`
- Additional skills: `ai-slop-cleaner`, `analyze`, `ask-claude`, `ask-gemini`, `autopilot`, `build-fix`, `cancel`, `code-review`, `configure-notifications`, `deepsearch`, `doctor`, `ecomode`, `frontend-ui-ux`, `git-master`, `help`, `hud`, `note`, `omx-setup`, `pipeline`, `plan`, `ralph-init`, `review`, `security-review`, `setup`, `skill`, `swarm`, `tdd`, `trace`, `ultraqa`, `ultrawork`, `visual-verdict`, `web-clone`, `worker`
- Skill count: `37`
- Maturity: `unspecified`

#### [`google`](./plugins/google)

Merchant API developer assistant

- Top skills: `mapi-developer-assistant`
- Skill count: `1`
- Maturity: `unspecified`
<!-- END AUTO:PLUGIN_LINEUP -->

## Capability matrix

This matrix is generated from plugin metadata and skill discovery.

<!-- BEGIN AUTO:CAPABILITY_MATRIX -->
| Plugin | Category | Skills | Top Skills | Maturity |
|---|---|---:|---|---|
| `linear` | `Productivity` | 1 | linear | `unspecified` |
| `google-calendar` | `Productivity` | 5 | google-calendar, google-calendar-daily-brief, google-calendar-free-up-time, google-calendar-group-scheduler | `unspecified` |
| `gmail` | `Productivity` | 2 | gmail, gmail-inbox-triage | `unspecified` |
| `slack` | `Productivity` | 6 | slack, slack-channel-summarization, slack-daily-digest, slack-notification-triage | `unspecified` |
| `canva` | `Design` | 3 | canva-branded-presentation, canva-resize-for-all-social-media, canva-translate-design | `unspecified` |
| `figma` | `Design` | 7 | figma-code-connect-components, figma-create-design-system-rules, figma-create-new-file, figma-generate-design | `unspecified` |
| `hugging-face` | `Coding` | 11 | cli, community-evals, datasets, gradio | `unspecified` |
| `jam` | `Productivity` | 1 | jam-bug-triage | `unspecified` |
| `netlify` | `Coding` | 1 | netlify-deploy | `unspecified` |
| `stripe` | `Productivity` | 2 | stripe-best-practices, upgrade-stripe | `unspecified` |
| `vercel` | `Coding` | 47 | agent-browser, agent-browser-verify, ai-elements, ai-gateway | `unspecified` |
| `game-studio` | `Coding` | 9 | game-playtest, game-studio, game-ui-frontend, phaser-2d-game | `unspecified` |
| `box` | `Productivity` | 1 | box | `unspecified` |
| `github` | `Coding` | 5 | auto-publish-after-plan, gh-address-comments, gh-fix-ci, github | `unspecified` |
| `google-drive` | `Productivity` | 10 | google-docs, google-drive, google-sheets, google-sheets-chart-builder | `unspecified` |
| `notion` | `Productivity` | 4 | notion-knowledge-capture, notion-meeting-intelligence, notion-research-documentation, notion-spec-to-implementation | `unspecified` |
| `cloudflare` | `Coding` | 9 | agents-sdk, building-ai-agent-on-cloudflare, building-mcp-server-on-cloudflare, cloudflare | `unspecified` |
| `sentry` | `Coding` | 1 | sentry | `unspecified` |
| `build-ios-apps` | `Coding` | 5 | ios-debugger-agent, swiftui-liquid-glass, swiftui-performance-audit, swiftui-ui-patterns | `unspecified` |
| `build-web-apps` | `Coding` | 7 | deploy-to-vercel, frontend-skill, react-best-practices, shadcn-best-practices | `unspecified` |
| `test-android-apps` | `Coding` | 1 | android-emulator-qa | `unspecified` |
| `aws` | `Coding` | 2 | aws-openai-workflow, aws-workflow | `unspecified` |
| `medusa` | `Coding` | 9 | building-admin-dashboard-customizations, building-storefronts, building-with-medusa, db-generate | `unspecified` |
| `agentation` | `Coding` | 1 | agentation | `unspecified` |
| `resend` | `Productivity` | 1 | resend-cli | `unspecified` |
| `saleor` | `Coding` | 1 | saleor-paper-storefront | `unspecified` |
| `supabase` | `Coding` | 3 | cli, setup, supabase-usage | `unspecified` |
| `ssh-skill` | `Coding` | 2 | remote-supabase-ops, setup-profile | `unspecified` |
| `superpowers` | `Coding` | 14 | brainstorming, dispatching-parallel-agents, executing-plans, finishing-a-development-branch | `unspecified` |
| `docker` | `Coding` | 8 | audit-go-dependencies, bump-go-dependencies, docker-build-local-images, docker-compose-dev-loop | `unspecified` |
| `desktop-commander` | `Coding` | 1 | desktop-commander-ops | `unspecified` |
| `prompt-optimizer` | `Productivity` | 1 | prompt-optimizer | `unspecified` |
| `rembg` | `Productivity` | 1 | rembg | `unspecified` |
| `omx` | `Coding` | 37 | deep-interview, ralplan, ralph, team | `unspecified` |
| `google` | `Coding` | 1 | mapi-developer-assistant | `unspecified` |
<!-- END AUTO:CAPABILITY_MATRIX -->

## Plugin maturity

Maturity labels (`alpha`, `beta`, `stable`) are sourced from marketplace entries.

<!-- BEGIN AUTO:MATURITY_BADGES -->
- `stable`: 0
- `beta`: 0
- `alpha`: 0
- `unspecified`: 35
<!-- END AUTO:MATURITY_BADGES -->

## License

MIT

## Skill Source Repositories

These are the source repositories used to create and evolve skills across this plugin collection:

- [agent-plugins](https://github.com/awslabs/agent-plugins)
- [aws-cli](https://github.com/aws/aws-cli)
- [claude-codex-settings](https://github.com/fcakyon/claude-codex-settings)
- [cli](https://github.com/supabase/cli)
- [DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP)
- [medusa-agent-skills](https://github.com/medusajs/medusa-agent-skills)
- [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex)
- [openai/plugins](https://github.com/openai/plugins) _(official upstream plugin repository)_
- [plugins](https://github.com/openwebu/codex-plugins)
- [resend-cli](https://github.com/resend/resend-cli)
- [resend-mcp](https://github.com/resend/resend-mcp)
- [saleor-paper-storefront](https://github.com/saleor/agent-skills) _(base reference for the Saleor storefront skill pack)_
- [superpowers](https://github.com/obra/superpowers)
