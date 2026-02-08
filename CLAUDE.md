# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

The Unified AI Risk Assurance Framework synthesises the Queensland Government FAIRA Framework (v1.0.0) with the Microsoft AI Security Risk Assessment (v4.1.4). It provides practical guidance for public sector teams deploying AI solutions securely and ethically, with machine-readable schemas for automation.

**Integrated frameworks:** FAIRA, Microsoft AI Security, NIST AI Security Competency Area (NF-COM-002), VAISS v1.0/v2.0, NFAAIG 2024-2025, Australian Responsible AI Index 2025, AI6 Framework 2025, EU AI Act 2024, NIST AI RMF GenAI Profile, MAS AI Guidelines 2025, OECD AI Principles 2024, UK DSIT AI Framework.

## Commands

### Python Tools (from `tools/` directory)

```bash
# Install dependencies
pip install -r requirements.txt

# Validate a single file (auto-detects schema type)
python validate_schemas.py ../examples/sample-risk-register.json

# Validate with explicit schema type
python validate_schemas.py my-assessment.json --schema faira

# Validate all example files
python validate_schemas.py --all

# List available schema types
python validate_schemas.py --list-schemas

# Multi-framework compliance check
python faira-check.py my-risk-register.json
python faira-check.py my-risk-register.json --frameworks FAIRA,VAISS,NIST --verbose
python faira-check.py my-assessment.json --json report.json
```

### Node.js Tools (from `tools/` directory)

```bash
npm install
npm test                                    # Validate all examples
node validate-schemas.js my-file.json       # Validate single file
```

### Pre-commit Hooks

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

### GitHub Actions Workflows (manual trigger only)

- `validate-schemas.yml` - Schema validation (Python + Node.js + cross-platform matrix)
- `lint-yaml.yml` - YAML and OpenAPI validation
- `check-docs.yml` - Documentation quality checks

## Architecture

### JSON Schemas (`schemas/`)

Eight production-ready JSON Schema files (Draft 2020-12):

| Schema | Purpose |
|--------|---------|
| `risk-register.schema.json` | AI risk assessment register (GenAI threats, AI6/EU AI Act) |
| `faira-assessment.schema.json` | Queensland FAIRA Parts A, B, C |
| `control-catalog.schema.json` | Cross-framework control library (AI6, EU AI Act, NIST GenAI) |
| `nist-ai-competencies.schema.json` | NIST AI Security (NF-COM-002) |
| `vaiss-guardrails.schema.json` | VAISS 10 guardrails (v2 enhancements) |
| `compliance-mapping.schema.json` | Cross-framework alignment (12 frameworks) |
| `ai6-framework.schema.json` | AI6 Framework 6 Essential Practices |
| `eu-ai-act.schema.json` | EU AI Act compliance assessment |

### YAML Mappings (`mappings/`)

| File | Purpose |
|------|---------|
| `faira-microsoft-crosswalk.yaml` | FAIRA ↔ Microsoft AI Security detailed mapping |
| `naic-rai-index-2025.yaml` | Australian RAI Index (OECD 2024, GenAI additions) |
| `risk-taxonomy.yaml` | Risk categories, severity scales, GenAI-specific risks |
| `ai6-naic-crosswalk.yaml` | AI6 Framework to VAISS, FAIRA, NIST, ISO 42001, EU AI Act |
| `eu-ai-act-crosswalk.yaml` | EU AI Act to Australian frameworks |
| `nist-genai-profile-crosswalk.yaml` | NIST GenAI Profile GOVERN/MAP/MEASURE/MANAGE |
| `mas-ai-guidelines-crosswalk.yaml` | MAS FEAT principles to Australian frameworks |

### Validation Tools

Schema validators auto-detect type based on JSON structure:

| Schema Type | Detection Criteria |
|-------------|-------------------|
| `risk-register` | Has `risks` and `metadata.assessmentId` |
| `faira` | Has `partA`, `partB`, and `partC` |
| `vaiss` | Has `guardrailAssessments` |
| `nist-competencies` | Has `competencyArea` and `competencies` |
| `control-catalog` | Has `controls` and `metadata.controlCatalogId` |
| `compliance-mapping` | Has `mappings` and `sourceFramework` |
| `ai6-framework` | Has `practiceAssessments` |
| `eu-ai-act` | Has `riskClassification` with `category` |

### OpenAPI Specification (`api/openapi.yaml`)

REST API spec (OpenAPI 3.0) for building automated CI/CD risk checks, multi-project dashboards, vendor assessment, and continuous monitoring.

## Standards

- **Language**: Use Australian English (organisation, behaviour, colour)
- **ID Patterns**: `RISK-0001`, `CTRL-0001` (4 digits, zero-padded)
- **Risk Scoring**: Severity (1-5) × Likelihood (1-5) = Risk Score
- **NIST Competencies**: Format as `AI-K-###` (knowledge) or `AI-S-###` (skills)
- **Checklists**: Use `- [ ]` format for GitHub checkbox rendering

## Seven-Step Implementation Process

1. **Team Formation and Planning** - Multi-disciplinary team with NIST AI security competencies
2. **Define the AI Solution** - FAIRA Part A system definition
3. **Values Assessment** - 8 AI Ethics Principles evaluation
4. **Risk Assessment and Scoring** - Identify and quantify risks
5. **Controls and Mitigation Planning** - Technical and administrative controls
6. **Documenting and Reporting** - Governance documentation
7. **Lifecycle Maintenance** - Continuous monitoring and updates

## Key Framework Documents

| File | Description |
|------|-------------|
| `Unified_AI_Risk_Assurance_Framework.md` | Main synthesis guide (read first) |
| `AI_Risk_Assurance_Checklists.md` | 407 practical checklist items across 7 steps |
| `FAIRA_Framework.md` | Queensland Government FAIRA reference |
| `AI_Security_Risk_Assessment.md` | Microsoft AI Security reference |
