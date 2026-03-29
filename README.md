# CODEX PLUGINS

The plugin workspace for Codex.

Built for humans, AI agents, and CI/CD pipelines.

```text
 ██████╗ ██████╗ ██████╗ ███████╗██╗  ██╗    ██████╗ ██╗     ██╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝╚██╗██╔╝    ██╔══██╗██║     ██║   ██║██╔════╝ ██║████╗  ██║██╔════╝
██║     ██║   ██║██║  ██║█████╗   ╚███╔╝     ██████╔╝██║     ██║   ██║██║  ███╗██║██╔██╗ ██║███████╗
██║     ██║   ██║██║  ██║██╔══╝   ██╔██╗     ██╔═══╝ ██║     ██║   ██║██║   ██║██║██║╚██╗██║╚════██║
╚██████╗╚██████╔╝██████╔╝███████╗██╔╝ ██╗    ██║     ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║███████║
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
```

## What you can do with Onlook:

- [x] Create Next.js app in seconds
  - [x] Start from text or image
  - [x] Use prebuilt templates
  - [ ] Import from Figma
  - [ ] Import from GitHub repo
  - [ ] Make a PR to a GitHub repo
- [x] Visually edit your app
  - [x] Use Figma-like UI
  - [x] Preview your app in real-time
  - [x] Manage brand assets and tokens
  - [x] Create and navigate to Pages
  - [x] Browse layers
  - [x] Manage project Images
  - [x] Detect and use Components - _Previously in [Onlook Desktop](https://github.com/onlook-dev/desktop)_
  - [ ] Drag-and-drop Components Panel
  - [x] Use Branching to experiment with designs
- [x] Development Tools
  - [x] Real-time code editor
  - [x] Save and restore from checkpoints
  - [x] Run commands via CLI
  - [x] Connect with app marketplace
- [x] Deploy your app in seconds
  - [x] Generate sharable links
  - [x] Link your custom domain
- [ ] Collaborate with your team
  - [x] Real-time editing
  - [ ] Leave comments
- [ ] Advanced AI capabilities
  - [x] Queue multiple messages at once
  - [ ] Use Images as references and as assets in a project
  - [ ] Setup and use MCPs in projects
  - [ ] Allow Onlook to use itself as a toolcall for branch creation and iteration
- [ ] Advanced project support
  - [ ] Support non-NextJS projects
  - [ ] Support non-Tailwind projects

TODO: auto-generate top-skill and expandable hidden-skill blocks from plugin metadata/scripts.


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

## Need advanced options?

See [docs/setup-reference.md](docs/setup-reference.md) for:

- manual setup commands
- manual plugin creation flow
- repo structure and optional plugin surfaces
- troubleshooting notes

## Current plugin lineup

Live in this repo today, grouped by use case so you can find the right plugin and skills quickly.

TODO: auto-generate top-skill and expandable hidden-skill blocks from plugin metadata/scripts.

### Productivity

#### `linear`
Turn product requests into shipped work with issue triage and delivery workflows.
- Top skills: `linear`
- Skill count: `1`

#### `google-calendar`
Plan smarter schedules, automate prep, and keep team calendars conflict-free.
- Top skills: `google-calendar`, `google-calendar-daily-brief`, `google-calendar-free-up-time`, `google-calendar-group-scheduler`
  <details>
  <summary>Show 1 more skills</summary>
  - More skills: `google-calendar-meeting-prep`
  </details>
- Skill count: `5`

#### `gmail`
Triage inboxes fast and draft high-quality replies with context-aware workflows.
- Top skills: `gmail`, `gmail-inbox-triage`
- Skill count: `2`

#### `slack`
Summarize channels, triage notifications, and ship clear outbound updates in seconds.
- Top skills: `slack`, `slack-channel-summarization`, `slack-daily-digest`, `slack-notification-triage`
  <details>
  <summary>Show 2 more skills</summary>
  - More skills: `slack-outgoing-message`, `slack-reply-drafting`
  </details>
- Skill count: `6`

#### `canva`
Generate polished visual assets and social-ready variants without leaving the terminal.
- Top skills: `canva-branded-presentation`, `canva-resize-for-all-social-media`, `canva-translate-design`
- Skill count: `3`

#### `figma`
Bridge design and code with component generation, system rules, and rapid design ops.
- Top skills: `figma-code-connect-components`, `figma-create-design-system-rules`, `figma-create-new-file`, `figma-generate-design`
  <details>
  <summary>Show 3 more skills</summary>
  - More skills: `figma-generate-library`, `figma-implement-design`, `figma-use`
  </details>
- Skill count: `7`

#### `jam`
Capture and structure bug feedback loops to accelerate debugging and product quality.
- Top skills: `coming soon`
- Skill count: `0` (plugin scaffold present, skill pack in progress)

#### `box`
Automate secure file workflows and enterprise document operations at scale.
- Top skills: `box`
- Skill count: `1`

#### `google-drive`
Work across Docs, Sheets, and Drive assets with high-speed workspace automation.
- Top skills: `google-docs`, `google-drive`, `google-sheets`, `google-sheets-chart-builder`
  <details>
  <summary>Show 6 more skills</summary>
  - More skills: `google-sheets-formula-builder`, `google-slides`, `google-slides-import-presentation`, `google-slides-template-migration`, `google-slides-template-surgery`, `google-slides-visual-iteration`
  </details>
- Skill count: `10`

#### `notion`
Capture knowledge, transform notes into specs, and operationalize docs workflows.
- Top skills: `notion-knowledge-capture`, `notion-meeting-intelligence`, `notion-research-documentation`, `notion-spec-to-implementation`
- Skill count: `4`

### Developer Workflows

#### `github`
Run end-to-end repo operations: triage, CI fixes, review workflows, and PR publishing.
- Top skills: `gh-address-comments`, `gh-fix-ci`, `github`, `yeet`
- Skill count: `4`

#### `build-ios-apps`
Design, refactor, and debug SwiftUI apps with simulator-aware engineering workflows.
- Top skills: `ios-debugger-agent`, `swiftui-liquid-glass`, `swiftui-performance-audit`, `swiftui-ui-patterns`
  <details>
  <summary>Show 1 more skills</summary>
  - More skills: `swiftui-view-refactor`
  </details>
- Skill count: `5`

#### `build-web-apps`
Create high-impact web products with deployment, UI, data, and payments best practices.
- Top skills: `deploy-to-vercel`, `frontend-skill`, `react-best-practices`, `shadcn-best-practices`
  <details>
  <summary>Show 3 more skills</summary>
  - More skills: `stripe-best-practices`, `supabase-best-practices`, `web-design-guidelines`
  </details>
- Skill count: `7`

#### `test-android-apps`
Automate Android app QA and emulator-driven validation for release confidence.
- Top skills: `android-emulator-qa`
- Skill count: `1`

#### `superpowers`
Advanced engineering execution skills for planning, debugging, reviews, and delivery.
- Top skills: `brainstorming`, `dispatching-parallel-agents`, `executing-plans`, `finishing-a-development-branch`
  <details>
  <summary>Show 10 more skills</summary>
  - More skills: `receiving-code-review`, `requesting-code-review`, `subagent-driven-development`, `systematic-debugging`, `test-driven-development`, `using-git-worktrees`, `using-superpowers`, `verification-before-completion`, `writing-plans`, `writing-skills`
  </details>
- Skill count: `14`

#### `game-studio`
Prototype, playtest, and ship engaging game experiences across 2D/3D web stacks.
- Top skills: `game-playtest`, `game-studio`, `game-ui-frontend`, `phaser-2d-game`
  <details>
  <summary>Show 5 more skills</summary>
  - More skills: `react-three-fiber-game`, `sprite-pipeline`, `three-webgl-game`, `web-3d-asset-pipeline`, `web-game-foundations`
  </details>
- Skill count: `9`

#### `saleor`
Accelerate Saleor storefront architecture with practical, implementation-ready guidance.
- Top skills: `saleor-paper-storefront`
- Skill count: `1`

#### `medusa`
Build and extend commerce backends, storefronts, and admin customizations with speed.
- Top skills: `building-admin-dashboard-customizations`, `building-storefronts`, `building-with-medusa`, `db-generate`
  <details>
  <summary>Show 4 more skills</summary>
  - More skills: `db-migrate`, `learning-medusa`, `new-user`, `storefront-best-practices`
  </details>
- Skill count: `8`

#### `agentation`
Add annotation-driven agent feedback loops directly into React product workflows.
- Top skills: `agentation`
- Skill count: `1`

### Platform & Infrastructure

#### `vercel`
Ship full-stack apps faster with deep support for deploys, AI, observability, and infra.
- Top skills: `agent-browser`, `agent-browser-verify`, `ai-elements`, `ai-gateway`
  <details>
  <summary>Show 43 more skills</summary>
  - More skills: `ai-generation-persistence`, `ai-sdk`, `auth`, `bootstrap`, `chat-sdk`, `cms`, `cron-jobs`, `deployments-cicd`, `email`, `env-vars`, `geist`, `geistdocs`, `investigation-mode`, `json-render`, `marketplace`, `micro`, `ncc`, `next-forge`, `nextjs`, `observability`, `payments`, `react-best-practices`, `routing-middleware`, `runtime-cache`, `satori`, `shadcn`, `sign-in-with-vercel`, `swr`, `turbopack`, `turborepo`, `v0-dev`, `vercel-agent`, `vercel-api`, `vercel-cli`, `vercel-firewall`, `vercel-flags`, `vercel-functions`, `vercel-queues`, `vercel-sandbox`, `vercel-services`, `vercel-storage`, `verification`, `workflow`
  </details>
- Skill count: `47`

#### `netlify`
Deploy and operate modern web projects with streamlined Netlify-focused automation.
- Top skills: `netlify-deploy`
- Skill count: `1`

#### `stripe`
Build safer payment flows, upgrades, and integration decisions with battle-tested patterns.
- Top skills: `stripe-best-practices`, `upgrade-stripe`
- Skill count: `2`

#### `cloudflare`
Build edge-native apps, agents, workers, and durable systems on Cloudflare.
- Top skills: `agents-sdk`, `building-ai-agent-on-cloudflare`, `building-mcp-server-on-cloudflare`, `cloudflare`
  <details>
  <summary>Show 5 more skills</summary>
  - More skills: `durable-objects`, `sandbox-sdk`, `web-perf`, `workers-best-practices`, `wrangler`
  </details>
- Skill count: `9`

#### `sentry`
Inspect real production issues and prioritize fixes with error-first operational visibility.
- Top skills: `sentry`
- Skill count: `1`

#### `aws`
Design and operate secure AWS architectures, including OpenAI-powered workloads.
- Top skills: `aws-openai-workflow`, `aws-workflow`
- Skill count: `2`

#### `supabase`
Stand up and run Supabase projects with CLI-first setup and usage workflows.
- Top skills: `cli`, `setup`, `supabase-usage`
- Skill count: `3`

#### `resend`
Operationalize email delivery from local dev to CI pipelines with Resend-native tooling.
- Top skills: `resend-cli`
- Skill count: `1`

#### `hugging-face`
Production toolkit for model discovery, datasets, evals, Spaces, and inference flows.
- Top skills: `cli`, `community-evals`, `datasets`, `gradio`
  <details>
  <summary>Show 7 more skills</summary>
  - More skills: `jobs`, `llm-trainer`, `paper-publisher`, `papers`, `trackio`, `transformers.js`, `vision-trainer`
  </details>
- Skill count: `11`

## License

MIT
