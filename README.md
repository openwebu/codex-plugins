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

Live in this repo today, each with focused skills you can invoke immediately:

- **`linear`** — Turn product requests into shipped work with issue triage and delivery workflows.
  - **Skills:** `linear`

- **`google-calendar`** — Plan smarter schedules, automate prep, and keep team calendars conflict-free.
  - **Skills:** `google-calendar`, `google-calendar-daily-brief`, `google-calendar-free-up-time`, `google-calendar-group-scheduler` (+1 more)

- **`gmail`** — Triage inboxes fast and draft high-quality replies with context-aware workflows.
  - **Skills:** `gmail`, `gmail-inbox-triage`

- **`slack`** — Summarize channels, triage notifications, and ship clear outbound updates in seconds.
  - **Skills:** `slack`, `slack-channel-summarization`, `slack-daily-digest`, `slack-notification-triage` (+2 more)

- **`canva`** — Generate polished visual assets and social-ready variants without leaving the terminal.
  - **Skills:** `canva-branded-presentation`, `canva-resize-for-all-social-media`, `canva-translate-design`

- **`figma`** — Bridge design and code with component generation, system rules, and rapid design ops.
  - **Skills:** `figma-code-connect-components`, `figma-create-design-system-rules`, `figma-create-new-file`, `figma-generate-design` (+3 more)

- **`hugging-face`** — Production toolkit for model discovery, datasets, evals, Spaces, and inference flows.
  - **Skills:** `cli`, `community-evals`, `datasets`, `gradio` (+7 more)

- **`jam`** — Capture and structure bug feedback loops to accelerate debugging and product quality.
  - **Skills:** `coming soon` (plugin scaffold present, skill pack in progress)

- **`netlify`** — Deploy and operate modern web projects with streamlined Netlify-focused automation.
  - **Skills:** `netlify-deploy`

- **`stripe`** — Build safer payment flows, upgrades, and integration decisions with battle-tested patterns.
  - **Skills:** `stripe-best-practices`, `upgrade-stripe`

- **`vercel`** — Ship full-stack apps faster with deep support for deploys, AI, observability, and infra.
  - **Skills:** `agent-browser`, `agent-browser-verify`, `ai-elements`, `ai-gateway` (+43 more)

- **`game-studio`** — Prototype, playtest, and ship engaging game experiences across 2D/3D web stacks.
  - **Skills:** `game-playtest`, `game-studio`, `game-ui-frontend`, `phaser-2d-game` (+5 more)

- **`box`** — Automate secure file workflows and enterprise document operations at scale.
  - **Skills:** `box`

- **`github`** — Run end-to-end repo operations: triage, CI fixes, review workflows, and PR publishing.
  - **Skills:** `gh-address-comments`, `gh-fix-ci`, `github`, `yeet`

- **`google-drive`** — Work across Docs, Sheets, and Drive assets with high-speed workspace automation.
  - **Skills:** `google-docs`, `google-drive`, `google-sheets`, `google-sheets-chart-builder` (+6 more)

- **`notion`** — Capture knowledge, transform notes into specs, and operationalize docs workflows.
  - **Skills:** `notion-knowledge-capture`, `notion-meeting-intelligence`, `notion-research-documentation`, `notion-spec-to-implementation`

- **`cloudflare`** — Build edge-native apps, agents, workers, and durable systems on Cloudflare.
  - **Skills:** `agents-sdk`, `building-ai-agent-on-cloudflare`, `building-mcp-server-on-cloudflare`, `cloudflare` (+5 more)

- **`sentry`** — Inspect real production issues and prioritize fixes with error-first operational visibility.
  - **Skills:** `sentry`

- **`build-ios-apps`** — Design, refactor, and debug SwiftUI apps with simulator-aware engineering workflows.
  - **Skills:** `ios-debugger-agent`, `swiftui-liquid-glass`, `swiftui-performance-audit`, `swiftui-ui-patterns` (+1 more)

- **`build-web-apps`** — Create high-impact web products with deployment, UI, data, and payments best practices.
  - **Skills:** `deploy-to-vercel`, `frontend-skill`, `react-best-practices`, `shadcn-best-practices` (+3 more)

- **`test-android-apps`** — Automate Android app QA and emulator-driven validation for release confidence.
  - **Skills:** `android-emulator-qa`

- **`aws`** — Design and operate secure AWS architectures, including OpenAI-powered workloads.
  - **Skills:** `aws-openai-workflow`, `aws-workflow`

- **`medusa`** — Build and extend commerce backends, storefronts, and admin customizations with speed.
  - **Skills:** `building-admin-dashboard-customizations`, `building-storefronts`, `building-with-medusa`, `db-generate` (+4 more)

- **`agentation`** — Add annotation-driven agent feedback loops directly into React product workflows.
  - **Skills:** `agentation`

- **`resend`** — Operationalize email delivery from local dev to CI pipelines with Resend-native tooling.
  - **Skills:** `resend-cli`

- **`saleor`** — Accelerate Saleor storefront architecture with practical, implementation-ready guidance.
  - **Skills:** `saleor-paper-storefront`

- **`supabase`** — Stand up and run Supabase projects with CLI-first setup and usage workflows.
  - **Skills:** `cli`, `setup`, `supabase-usage`

- **`superpowers`** — Advanced engineering execution skills for planning, debugging, reviews, and delivery.
  - **Skills:** `brainstorming`, `dispatching-parallel-agents`, `executing-plans`, `finishing-a-development-branch` (+10 more)

## License

MIT
