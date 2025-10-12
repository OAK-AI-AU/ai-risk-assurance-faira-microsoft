# Changelog

All notable changes to the Unified AI Risk Assurance Framework will be documented in this file.

## [2.0.0] - 2025-10-12

### Added - Machine-Readable Formats & Enhanced Documentation

#### 🆕 Framework Content Updates
- **NIST AI Security Competency Area (NF-COM-002)**: Updated with June 2025 proposed enhancements
  - Added competency area designation and framework version tracking
  - Enhanced documentation of 46 AI-specific competencies (39 knowledge + 7 skills)
  - Added links to NICE Framework Resource Center and NICCS tools

- **NFAAIG 2024-2025 Framework**: Comprehensive documentation added
  - Five cornerstones of AI assurance
  - July 30, 2025 Technical Standard updates
  - Policy requirements and implementation timeline
  - Integration with other Australian frameworks

- **VAISS Framework v1 & v2**: Detailed tracking document
  - Complete v1.0 (September 2024) specification
  - Version 2.0 consultation and roadmap tracking
  - Implementation guidance and maturity levels
  - Integration with ISO 42001 and NIST AI RMF

#### 📋 JSON Schemas (6 schemas)
- **`risk-register.schema.json`** - Comprehensive AI risk register structure
  - Risk metadata, categories, and severity/likelihood scales
  - Microsoft AI Security threat type integration
  - NIST competency mapping
  - VAISS guardrail alignment
  - Control tracking and residual risk assessment

- **`faira-assessment.schema.json`** - Complete FAIRA framework structure
  - Part A: Components Analysis (9 tables)
  - Part B: Values Assessment (8 AI Ethics Principles)
  - Part C: Controls for AI Risks
  - WHS considerations integration
  - Approval and sign-off tracking

- **`control-catalog.schema.json`** - Cross-framework control library
  - Multi-framework mapping (FAIRA, Microsoft, NIST, VAISS, NFAAIG, ISO 42001)
  - Implementation and testing guidance
  - Control relationships and dependencies
  - Maturity levels and effectiveness ratings

- **`nist-ai-competencies.schema.json`** - NIST AI Security competencies
  - NF-COM-002 structure
  - Knowledge areas (AI-K-###) and skills (AI-S-###)
  - Team assessment templates
  - Competency gap analysis support

- **`vaiss-guardrails.schema.json`** - VAISS 10 guardrails assessment
  - Implementation status tracking
  - Gap identification and remediation planning
  - Evidence documentation
  - Maturity scoring

- **`compliance-mapping.schema.json`** - Cross-framework alignment
  - Multi-framework requirement mapping
  - Framework alignment matrix
  - Gap analysis support

#### 🗺️ YAML Mappings (3 mapping files)
- **`faira-microsoft-crosswalk.yaml`** - Detailed FAIRA ↔ Microsoft mapping
  - Part A, B, and C component mappings
  - AI Ethics Principles to Microsoft controls
  - Threat type to risk category mapping
  - Lifecycle phase alignment
  - Integration recommendations

- **`risk-taxonomy.yaml`** - Standardized risk framework
  - 12 risk categories with subcategories
  - 5-level severity and likelihood scales
  - Risk matrix (priority levels)
  - 10 standard risk templates
  - Framework alignment for each category

- **`naic-rai-index-2025.yaml`** - Australian RAI Index taxonomy (existing, retained)

#### 📚 Documentation
- **`docs/DEVELOPER_GUIDE.md`** - Comprehensive 400+ line developer guide
  - JSON Schema validation examples (Python & JavaScript)
  - Creating and using risk registers
  - YAML mapping usage patterns
  - CI/CD integration examples
  - GitHub Actions and pre-commit hook templates
  - Advanced patterns (cross-framework mapping, gap analysis, automation)
  - Common use cases with code samples
  - Best practices and troubleshooting

- **`examples/sample-risk-register.json`** - Production-ready example
  - 3 complete risk entries (Security, Technical, Bias categories)
  - Multi-framework integration demonstration
  - Control mapping and mitigation planning
  - Residual risk assessment examples

- **`examples/README.md`** - Guide to using examples

#### 📖 Enhanced Framework Documentation
- **Australian Government Frameworks Section**: Added to Unified Framework
  - NFAAIG with five cornerstones and 2025 updates
  - VAISS with 10 guardrails and v2 tracking
  - NAIC RAI Index integration
  - International frameworks comparison

- **README.md Updates**:
  - New "Machine-Readable Formats" section
  - Quick start code examples
  - Comprehensive file listing with all new resources
  - Updated "What's Inside" section

#### 🔧 Developer Tools & Automation
- **`tools/validate_schemas.py`** - Python schema validator
  - Auto-detects schema types from JSON structure
  - Validates against all 6 JSON schemas
  - Batch validation for all examples
  - Colored terminal output with detailed error reporting
  - Support for custom schema paths

- **`tools/validate-schemas.js`** - Node.js schema validator
  - Identical functionality to Python version
  - Uses Ajv for JSON Schema Draft 2020-12 validation
  - Can be used as importable module or CLI tool
  - npm script integration (`npm test`)

- **`tools/faira-check.py`** - Multi-framework compliance checker
  - Checks compliance against FAIRA, VAISS, NIST, and Microsoft frameworks
  - Generates compliance scores and gap analysis
  - Detailed recommendations for each framework
  - JSON export capability for reports
  - Severity-based issue prioritization

- **`tools/requirements.txt`** & **`tools/package.json`** - Dependency management
- **`tools/README.md`** - Comprehensive tool documentation with examples

#### 🔄 CI/CD & Automation
- **`.github/workflows/validate-schemas.yml`** - Schema validation workflow
  - Python and Node.js validation in parallel
  - Cross-platform testing (Ubuntu, macOS, Windows)
  - Multiple Python versions (3.9, 3.10, 3.11, 3.12)
  - Schema quality checks and metadata validation
  - Manual trigger only (workflow_dispatch)

- **`.github/workflows/lint-yaml.yml`** - YAML linting workflow
  - yamllint with custom rules
  - OpenAPI specification validation
  - YAML syntax checking
  - Framework mapping validation
  - Manual trigger only

- **`.github/workflows/check-docs.yml`** - Documentation checks
  - Markdown linting
  - Internal link checking
  - Australian English spelling verification
  - Documentation structure validation
  - Code block counting and verification
  - Manual trigger only

- **`.pre-commit-config.yaml`** - Pre-commit hooks configuration
  - JSON/YAML syntax validation
  - Auto-formatting with prettier
  - Python code quality (Black, flake8)
  - Australian English spelling checks
  - Schema validation on examples
  - OpenAPI spec validation
  - TODO/FIXME detection

#### 🌐 API & Integration
- **`api/openapi.yaml`** - Complete OpenAPI 3.0 specification
  - REST API for risk register management
  - FAIRA and VAISS assessment endpoints
  - Compliance checking and gap analysis endpoints
  - Schema validation services
  - Framework metadata and mapping queries
  - Authentication (API Key and OAuth 2.0)
  - Rate limiting (1000 req/hour)
  - Comprehensive request/response schemas

- **`api/README.md`** - API reference documentation
  - Quick start guides
  - Complete endpoint documentation
  - Authentication examples (Python, JavaScript, curl)
  - Error handling guide
  - Response code reference
  - Complete workflow examples
  - SDK usage patterns

### Changed
- **Australian English Spelling**: Standardised all newly created documentation to Australian English (en-AU)
  - Changed "organization" to "organisation" in framework documentation and JSON schema property names
  - Changed "organizational" to "organisational" in descriptive text
  - Maintained "color" for technical/programming contexts (hex color codes) per international standards
- Updated NIST AI Security references throughout framework documents
- Enhanced cross-framework integration documentation
- Improved framework version tracking and update information

### Technical
- All schemas follow JSON Schema Draft 2020-12 specification
- Schema IDs use GitHub repository URLs for resolution
- YAML files follow YAML 1.2 specification
- Examples validate against production schemas

## [1.0.0] - 2024-10-04

### Initial Release
- FAIRA Framework v1.0.0 documentation
- Microsoft AI Security Risk Assessment v4.1.4 integration
- AI Risk Assurance Checklists
- NIST AI Security Competency Area integration (46 competencies)
- Australian Responsible AI Index 2025
- Unified AI Risk Assurance Framework guide
- Queensland Government WHS integration
- 8 AI Ethics Principles alignment

---

## Version Numbering

This project uses [Semantic Versioning](https://semver.org/):
- **MAJOR**: Significant framework changes or breaking schema changes
- **MINOR**: New features, schemas, or substantial documentation additions
- **PATCH**: Bug fixes, minor documentation updates, clarifications

## Framework Versions Referenced

| Framework | Version | Status |
|-----------|---------|--------|
| FAIRA | v1.0.0 | Current |
| Microsoft AI Security | v4.1.4 | Current |
| NIST AI Security Competency | NF-COM-002 (NICE Framework v2.0.0, March 2025) | Current, June 2025 updates proposed |
| VAISS | v1.0 (September 2024) | Current, v2 planned 2025 |
| NFAAIG | June 2024, Technical Standard July 30, 2025 | Current |
| NAIC RAI Index | 2025 Edition | Current |
