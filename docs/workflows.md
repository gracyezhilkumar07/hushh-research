
This repository uses multiple GitHub Actions workflows for CI/CD and automation.

## CI Pipeline
- ci.yml → Runs lint, tests, and build checks on pull requests.

## Deployment Workflows

- deploy-uat.yml → Deploys to UAT environment
- deploy-production.yml → Deploys to production

## Validation Workflows

- queue-validation.yml → Validates queue processing logic
- main-post-merge-smoke.yml → Runs post-merge smoke tests

## Backup & Maintenance

- prod-supabase-backup-posture.yml → Ensures database backup safety

## Notes
- Workflows are triggered automatically based on branch rules.
- Do not modify production workflows without review.