# ai-risk-assurance-faira-microsoft

## 🛡️ Unified AI Risk Assurance Framework

A practical synthesis of the **Queensland Government FAIRA Framework (v1.0.0)** and the **Microsoft AI Security Risk Assessment**, designed to help public sector teams deploy artificial intelligence solutions securely, ethically, and in compliance with national policy and WHS obligations.

Published by **[OAK AI](https://github.com/OAK-AI-Public)**  
GitHub Repository: [OAK-AI-Public/ai-risk-assurance-faira-microsoft](https://github.com/OAK-AI-Public/ai-risk-assurance-faira-microsoft)

**Latest Update**: Enhanced with NIST AI Security Competency Area (NF-COM-002) integration from NICE Framework Components v2.0.0 (March 2025), adding 46 AI-specific competencies (39 knowledge areas + 7 skills) with June 2025 proposed enhancements for comprehensive AI security capability assessment. Now includes the Australian Responsible AI Index 2025 (NAIC/Fifth Quadrant) for maturity benchmarking aligned with VAISS. Updated with National Framework for the Assurance of AI in Government (NFAAIG) 2025 technical standards.

---

## 📘 What’s Inside

This guide combines:

- ✅ [FAIRA Framework](https://www.forgov.qld.gov.au/information-technology/queensland-government-enterprise-architecture-qgea/qgea-directions-and-guidance/qgea-policies-standards-and-guidelines/faira-framework) – a values-based risk and governance framework for AI in Queensland Government
- 🔐 [Microsoft AI Security Risk Assessment](https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment) ([PDF](https://github.com/MicrosoftDocs/security/blob/main/Downloads/AI_Risk_Assessment_v4.1.4.pdf)) – practical lifecycle security controls for AI systems
- ⚖️ Alignment with the [NFAAIG (2024-2025)](./frameworks/nfaaig-framework-2025.md) ([Department of Finance](https://www.finance.gov.au/government/public-data/data-and-digital-ministers-meeting/national-framework-assurance-artificial-intelligence-government)) and QLD legislation
- ⚠️ Integration of **Workplace Health and Safety (WHS)** impacts under the _WHS Act 2011_
- 🎯 Integration of [NIST AI Security Competency Area (NF-COM-002)](https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center) – 46 AI-specific competencies for security teams (NICE Framework v2.0.0)
- 🇦🇺 **NEW**: Australian AI frameworks integrated:
  - [Australian Responsible AI Index 2025](./frameworks/naic-rai-index-2025.md) (NAIC/Fifth Quadrant) – maturity benchmarking
  - [Voluntary AI Safety Standard (VAISS)](./frameworks/vaiss-framework-2024-2025.md) – 10 guardrails with v2 tracking
  - [NFAAIG 2024-2025](./frameworks/nfaaig-framework-2025.md) – National government AI assurance framework

---

## 🧭 Use This Guide To

- Evaluate AI solutions with ethics, transparency and risk in mind
- Design and document controls across development, deployment and use
- Embed WHS, privacy, contestability and security into AI lifecycles
- Align with QLD GOV ICT, procurement and executive governance frameworks
- **NEW**: Automate risk assessments using JSON schemas and APIs
- **NEW**: Integrate compliance checking into CI/CD pipelines

---

## 🤖 Machine-Readable Formats

This repository now includes comprehensive machine-readable schemas and mappings for automated AI governance:

### JSON Schemas (`/schemas/`)

Six production-ready JSON Schema files enable programmatic validation and automation:

- **`risk-register.schema.json`** - Complete AI risk assessment structure
- **`faira-assessment.schema.json`** - Queensland FAIRA framework (Parts A, B, C)
- **`control-catalog.schema.json`** - Cross-framework control library
- **`nist-ai-competencies.schema.json`** - NIST AI Security (NF-COM-002)
- **`vaiss-guardrails.schema.json`** - VAISS 10 guardrails assessment
- **`compliance-mapping.schema.json`** - Cross-framework alignment

### YAML Mappings (`/mappings/`)

Cross-framework mappings for compliance and integration:

- **`naic-rai-index-2025.yaml`** - Australian RAI Index dimensions and maturity levels
- **`faira-microsoft-crosswalk.yaml`** - FAIRA ↔ Microsoft AI Security detailed mapping
- **`risk-taxonomy.yaml`** - Standardized risk categories, severity scales, and threat types

### Developer Resources

- **[Developer Guide](./docs/DEVELOPER_GUIDE.md)** - Complete guide with code examples, CI/CD integration, and best practices
- **[Examples](./examples/)** - Ready-to-use sample files including:
  - `sample-risk-register.json` - Complete risk register example with 3 detailed risks
  - Validation examples in Python and JavaScript

### Quick Start

```python
import json
import jsonschema

# Validate your risk register
with open('schemas/risk-register.schema.json') as f:
    schema = json.load(f)

with open('my-risks.json') as f:
    risks = json.load(f)

jsonschema.validate(instance=risks, schema=schema)
print("✅ Risk register is valid!")
```

**[Read the full Developer Guide →](./docs/DEVELOPER_GUIDE.md)**

---

## 🌐 REST API & Integration

The repository includes a complete **OpenAPI 3.0 specification** for building REST APIs that enable:

- **Automated CI/CD risk checks** - Validate risks before deployment
- **Multi-project dashboards** - Track compliance across all AI initiatives
- **Vendor assessment** - Validate third-party AI risk submissions
- **Continuous monitoring** - Detect regulatory drift automatically
- **Enterprise integration** - Connect with ServiceNow, Power BI, SharePoint

### Practical Use Cases

| Scenario | Solution |
|----------|----------|
| **DevOps Integration** | GitHub Actions workflow that automatically creates risk register and blocks deployment if critical gaps found |
| **Executive Reporting** | Power BI dashboard showing compliance scores across 15+ AI projects in real-time |
| **Procurement** | Automated validation of vendor risk assessments against FAIRA and NFAAIG requirements |
| **Compliance Monitoring** | Monthly scheduled job that re-checks all production AI systems against latest framework versions |
| **Risk Workflow** | Track risks from identification → assessment → mitigation → closure with full audit trail |
| **Cross-jurisdiction** | Map controls that satisfy both Queensland (FAIRA) and Federal (NFAAIG) requirements |

**📖 [See Complete Use Cases with Code Examples →](./api/USE_CASES.md)**

### API Documentation

- **[USE_CASES.md](./api/USE_CASES.md)** - Real-world integration patterns with working code
- **[api/README.md](./api/README.md)** - Complete API reference and endpoint documentation
- **[api/openapi.yaml](./api/openapi.yaml)** - OpenAPI 3.0 specification for generating SDKs

---

## 📂 Files

| File                                     | Description                                                      |
| ---------------------------------------- | ---------------------------------------------------------------- |
| `Unified_AI_Risk_Assurance_Framework.md` | The full synthesis guide (read this first)                       |
| `AI_Risk_Assurance_Checklists.md`        | Practical checklists for implementing the framework step-by-step |
| `FAIRA_Framework.md`                     | Queensland Government FAIRA Framework (extracted from DOCX)      |
| `AI_Security_Risk_Assessment.md`         | Microsoft AI Security Risk Assessment (extracted from PDF)       |
| `frameworks/naic-rai-index-2025.md`     | Australian Responsible AI Index 2025 (NAIC/Fifth Quadrant)       |
| `frameworks/nfaaig-framework-2025.md`   | National Framework for AI Assurance in Government (NFAAIG 2025)  |
| `frameworks/vaiss-framework-2024-2025.md` | Voluntary AI Safety Standard v1 & v2 tracking (VAISS)         |
| **Machine-Readable Formats** | |
| `schemas/risk-register.schema.json`     | JSON Schema for AI risk registers                                 |
| `schemas/faira-assessment.schema.json`  | JSON Schema for FAIRA assessments                                 |
| `schemas/control-catalog.schema.json`   | JSON Schema for control catalogs                                  |
| `schemas/nist-ai-competencies.schema.json` | JSON Schema for NIST AI competencies                           |
| `schemas/vaiss-guardrails.schema.json`  | JSON Schema for VAISS guardrail assessments                       |
| `schemas/compliance-mapping.schema.json` | JSON Schema for cross-framework mappings                         |
| `mappings/naic-rai-index-2025.yaml`     | NAIC RAI Index taxonomy mappings                                  |
| `mappings/faira-microsoft-crosswalk.yaml` | FAIRA-Microsoft detailed control mapping                        |
| `mappings/risk-taxonomy.yaml`           | Standardized risk taxonomy and scales                             |
| **API & Integration** | |
| `api/USE_CASES.md`                      | Real-world API integration patterns with working code examples    |
| `api/README.md`                         | Complete API reference documentation                              |
| `api/openapi.yaml`                      | OpenAPI 3.0 specification for REST API                            |
| **Developer Tools** | |
| `tools/validate_schemas.py`             | Python schema validator with auto-detection                       |
| `tools/validate-schemas.js`             | Node.js schema validator (identical features)                     |
| `tools/faira-check.py`                  | Multi-framework compliance checker CLI                            |
| `tools/README.md`                       | Tool documentation and usage examples                             |
| **Documentation & Examples** | |
| `docs/DEVELOPER_GUIDE.md`               | Complete guide for developers using machine-readable formats     |
| `examples/sample-risk-register.json`    | Complete example risk register with validation instructions       |
| `examples/README.md`                    | Guide to using and creating examples                              |
| **CI/CD & Automation** | |
| `.github/workflows/validate-schemas.yml` | Schema validation workflow (manual trigger)                      |
| `.github/workflows/lint-yaml.yml`       | YAML and OpenAPI validation workflow (manual trigger)             |
| `.github/workflows/check-docs.yml`      | Documentation quality checks (manual trigger)                     |
| `.pre-commit-config.yaml`               | Pre-commit hooks configuration                                    |
| **Other Resources** | |
| `Figure_1.webp`                          | FAIRA Framework diagram - How FAIRA Works                        |
| `Figure_2.webp`                          | FAIRA Framework diagram - Components of an AI solution           |
| `LICENSE`                                | MIT License with third-party licence attribution                 |
| `README.md`                              | Overview and repository index                                    |

---

## 🔍 References

- FAIRA Framework: © The State of Queensland 2024  
  [Licence: CC BY 4.0](http://creativecommons.org/licenses/by/4.0/)
- Microsoft AI Risk Assessment: © Microsoft Corporation  
  [GitHub Repo](https://github.com/MicrosoftDocs/security)
- NIST AI Security Competency Area: National Institute of Standards and Technology  
  Special thanks to [Ben Kereopa-Yorke](https://www.linkedin.com/in/benkereopayorke/) for highlighting the NIST AI Security Competency Area framework
- Australian Responsible AI Index 2025: © Fifth Quadrant / National AI Centre  
  [Framework Homepage](https://www.fifthquadrant.com.au/responsible-ai-index) | [NAIC News](https://www.industry.gov.au/news/benchmark-your-responsible-ai-maturity-level-new-self-assessment-tool)

---

## 📬 Contributions & Feedback

This guide is open and evolving. If you have suggestions or corrections:

- [Open an issue](https://github.com/OAK-AI-Public/ai-risk-assurance-faira-microsoft/issues)
- Or contact the maintainers via [OAK AI](https://github.com/OAK-AI-Public)

---

## 📄 Licence

MIT Licence with proper attribution to QLD Government FAIRA and Microsoft AI Risk Assessment. See [`LICENSE`](./LICENSE) for full details.
