# Changelog

All notable changes to the Unified AI Risk Assurance Framework will be documented in this file.

## [3.0.0] - 2026-02-08

### Added - International Framework Expansion

#### 🆕 New Frameworks

- **AI6 Framework 2025** (NAIC): Australia's 6 Essential AI Practices
  - New primary guidance for Australian AI adoption
  - 6 practices covering governance, risk, data, testing, transparency, and human oversight
  - NAIC screening tool and policy template integration
  - Cross-framework alignment with VAISS, FAIRA, ISO 42001, NIST AI RMF

- **EU AI Act 2024** (Regulation 2024/1689): The world's first comprehensive AI regulation
  - Risk classification system (Unacceptable/High-Risk/Limited/Minimal)
  - Annex III high-risk category definitions
  - Chapter 2 high-risk requirements (Articles 8-15)
  - GPAI model obligations
  - Implementation timeline tracking (2025-2027)

- **UK DSIT AI Framework**: UK's cross-sectoral AI governance approach
  - 5 principles (Safety, Transparency, Fairness, Accountability, Contestability)
  - AI Security Institute guidance
  - AI Assurance Roadmap integration

- **NIST AI RMF GenAI Profile** (NIST-AI-600-1): Generative AI guidance
  - GOVERN/MAP/MEASURE/MANAGE actions for GenAI
  - 12 GenAI-specific risks (Confabulation, Harmful Content, etc.)
  - Content provenance and watermarking guidance

- **MAS AI Guidelines 2025**: Singapore financial sector AI risk management
  - FEAT principles (Fairness, Ethics, Accountability, Transparency)
  - AI lifecycle controls
  - Sector-specific requirements

- **OECD AI Principles 2024**: Updated international principles
  - May 2024 revision
  - 47 jurisdictions adoption
  - GenAI-specific additions

#### 📋 New JSON Schemas (2 schemas)

- **`ai6-framework.schema.json`** - AI6 Framework assessment structure
  - 6 practice assessments with sub-practices
  - Implementation status and maturity levels
  - Gap identification and remediation tracking
  - Framework alignment references (VAISS, ISO, NIST, EU AI Act)
  - NAIC resource integration (screening tool, templates)

- **`eu-ai-act.schema.json`** - EU AI Act compliance assessment
  - Risk classification with Article 5 prohibited practices check
  - Annex III high-risk category assessment
  - Chapter 2 requirements (Articles 8-15) compliance tracking
  - Conformity assessment and CE marking
  - GPAI model requirements
  - Implementation timeline tracking
  - Transparency obligations (Article 50)
  - Australian relevance assessment

#### 📋 Schema Updates (4 schemas)

- **`vaiss-guardrails.schema.json`**
  - Added version 2.1 enum value
  - Added schemaVersion for migration support
  - Added v2Enhancements object:
    - Content provenance (C2PA compliance)
    - Watermarking (visible/invisible)
    - Developer guardrails
    - National AI Capability Plan alignment
    - Generative AI specific requirements

- **`risk-register.schema.json`**
  - Added new frameworksApplied values: VAISS v2.0, AI6 Framework 2025, EU AI Act 2024, NIST AI RMF GenAI Profile, MAS AI Guidelines 2025, OECD AI Principles 2024, UK DSIT AI Framework
  - Added GenAI-specific threatTypes: Confabulation, Harmful Content Generation, Copyright Infringement, Deepfake Generation, Training Data Leakage, Jailbreaking, Bias Amplification, Sycophancy
  - Added ai6Practices array (1-6) per risk
  - Added euAIActCategory per risk
  - Added nistGenAIActions for GenAI Profile mapping
  - Added schemaVersion for migration support

- **`compliance-mapping.schema.json`**
  - Added new primaryFramework values: AI6, EU AI Act, NIST GenAI Profile, MAS AI, OECD 2024, UK DSIT
  - Added frameworkReferences for: ai6, euAIAct, nistGenAI, masAI, oecd2024, ukDSIT

- **`control-catalog.schema.json`**
  - Added ai6 framework mapping (practices, subPractice)
  - Added euAIAct mapping (articles, highRiskRequirement, annexReference)
  - Added nistGenAI mapping (functions, actions, genAIRisksAddressed)
  - Added masAI mapping (principles)

#### 🗺️ New YAML Mappings (4 files)

- **`ai6-naic-crosswalk.yaml`**
  - AI6 6 practices detailed mapping
  - VAISS guardrail alignment per practice
  - FAIRA, NFAAIG, ISO 42001 alignment
  - NIST AI RMF function alignment
  - EU AI Act article alignment
  - OECD AI Principles 2024 alignment
  - NAIC resources and templates

- **`eu-ai-act-crosswalk.yaml`**
  - Implementation timeline (2024-2027)
  - Risk classification mapping
  - High-risk requirements to Australian frameworks
  - GPAI requirements and VAISS v2 alignment
  - Gap analysis between EU and Australian frameworks
  - Australian relevance guidance

- **`nist-genai-profile-crosswalk.yaml`**
  - 12 GenAI-specific risks mapped
  - GOVERN/MAP/MEASURE/MANAGE actions
  - VAISS, AI6, FAIRA, EU AI Act alignment per action
  - Microsoft AI Security threat mapping
  - NIST competency alignment
  - VAISS v2 enhancement mapping

- **`mas-ai-guidelines-crosswalk.yaml`**
  - FEAT principles detailed mapping
  - AI lifecycle controls
  - Sector-specific requirements
  - Australian framework alignment
  - Implementation guidance

#### 🗺️ YAML Mapping Updates (2 files)

- **`naic-rai-index-2025.yaml`**
  - Added OECD AI Principles 2024 alignment section
  - Added GenAI-specific additions per dimension

- **`risk-taxonomy.yaml`**
  - Added GenAI subcategories to Security, Ethical, Legal/Compliance categories
  - Added 10 GenAI-specific standard risks (RISK-G001 to RISK-G010)

#### 📚 New Framework Documentation (3 files)

- **`frameworks/ai6-framework-2025.md`**
  - 6 essential practices explained
  - VAISS alignment per practice
  - FAIRA alignment per practice
  - International framework alignment (ISO 42001, NIST AI RMF, EU AI Act)
  - NAIC resources and templates
  - Implementation roadmap

- **`frameworks/eu-ai-act-2024.md`**
  - Risk classification system
  - High-risk AI requirements (Articles 8-15)
  - Implementation timeline (2024-2027)
  - Relevance to Australian organisations
  - Australian framework alignment
  - Gap analysis

- **`frameworks/uk-dsit-ai-framework.md`**
  - 5 cross-sectoral principles
  - AI Security Institute overview
  - AI Assurance Roadmap
  - Australian framework alignment

#### 📚 Documentation Updates

- **`frameworks/vaiss-framework-2024-2025.md`**
  - Added comprehensive v2 enhancements section
  - Content provenance (C2PA)
  - Watermarking capabilities
  - Developer guardrails
  - National AI Capability Plan alignment
  - Generative AI specific requirements
  - AI6 Framework relationship section

#### 🔧 Tool Updates

- **`tools/faira-check.py`**
  - Added AI6Checker class (6 practices assessment)
  - Added EUAIActChecker class (risk classification, high-risk requirements, transparency)
  - Added NISTGenAIChecker class (GOVERN/MAP/MEASURE/MANAGE, GenAI threats)
  - Updated checker_map with new frameworks
  - AI6 now included in default frameworks
  - Updated help text and docstring

- **`tools/validate_schemas.py`**
  - Added ai6-framework and eu-ai-act to SCHEMA_TYPES
  - Added detection logic for AI6 (practiceAssessments)
  - Added detection logic for EU AI Act (riskClassification)
  - Updated help text with new schema types

#### 🌐 API Updates

- **`api/openapi.yaml`** (now v3.0.0)
  - Added AI6 Assessments tag and endpoints (/ai6-assessments)
  - Added EU AI Act Assessments tag and endpoints (/eu-ai-act-assessments)
  - Added validation endpoints for new schemas
  - Updated frameworks enums to include: AI6, EUAIAct, NISTGenAI, MAS, OECD, UKDSIT
  - Added AI6Assessment and AI6AssessmentSummary schemas
  - Added EUAIActAssessment and EUAIActAssessmentSummary schemas

### Changed

- Framework version updated to 3.0.0
- API version updated to 3.0.0
- Updated README with new frameworks and files
- Updated CLAUDE.md with new architecture information

### Technical

- All new schemas follow JSON Schema Draft 2020-12 specification
- Backwards compatibility maintained through:
  - Enum expansion (not replacement)
  - New properties are optional
  - schemaVersion tracking for migration support
  - Framework aliases maintained in tools

---

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
| VAISS | v1.0/v2.0 (September 2024, 2025-2026) | v1 Current, v2 enhancements added |
| NFAAIG | June 2024, Technical Standard July 30, 2025 | Current |
| NAIC RAI Index | 2025 Edition | Current |
| AI6 Framework | 1.0 (October 2025) | Current |
| EU AI Act | 2024/1689 (August 2024) | In force (phased implementation) |
| NIST AI RMF GenAI Profile | NIST-AI-600-1 (July 2024) | Current |
| MAS AI Guidelines | 2025 | Current |
| OECD AI Principles | 2024 (May 2024) | Current |
| UK DSIT AI Framework | 2023-2024 | Current |
