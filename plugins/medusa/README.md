# Medusa Plugin

This plugin packages Medusa agent skills for Codex in `plugins/medusa`.

It includes these skills:

- `building-with-medusa`
- `building-admin-dashboard-customizations`
- `building-storefronts`
- `storefront-best-practices`
- `learning-medusa`
- `db-generate`
- `db-migrate`
- `new-user`

## What It Covers

- Medusa backend architecture and implementation patterns (modules, workflows, API routes)
- Medusa admin dashboard customization patterns (widgets, pages, forms, data loading)
- Storefront integration patterns with Medusa SDK and React Query
- Ecommerce storefront best practices for conversion, SEO, responsiveness, and UX
- Guided learning flow for onboarding into Medusa development
- Database migration and admin user helper command-skills

## Plugin Structure

- `.codex-plugin/plugin.json`
  - plugin manifest and interface metadata

- `.mcp.json`
  - plugin-local MCP configuration for MedusaDocs

- `skills/`
  - Medusa and storefront skill payload imported from `medusa-agent-skills`

- `assets/`
  - plugin icon assets used by interface metadata
