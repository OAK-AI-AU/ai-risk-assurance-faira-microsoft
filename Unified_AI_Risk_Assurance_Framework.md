# Unified AI Risk Assurance Framework

Applying FAIRA with Microsoft AI Security Controls in Practice

## Overview

This guide aims to help Queensland Government agencies and their project teams apply the [Foundational Artificial Intelligence Risk Assessment (FAIRA v1.0.0, OFFICIAL)](https://www.forgov.qld.gov.au/information-technology/queensland-government-enterprise-architecture-qgea/qgea-directions-and-guidance/qgea-policies-standards-and-guidelines/faira-framework) together with the [Microsoft AI Security Risk Assessment Framework](https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment) ([PDF download](https://github.com/MicrosoftDocs/security/blob/main/Downloads/AI_Risk_Assessment_v4.1.4.pdf)) to form a cohesive, lifecycle-wide AI governance and risk management practice.

**📋 For practical implementation, use the companion [AI Risk Assurance Checklists](./AI_Risk_Assurance_Checklists.md) which provide detailed, actionable tasks for each step outlined in this framework.**

It consolidates:

- Robust public sector governance and ethics expectations
- Technical security controls across the AI pipeline
- Alignment with national standards including:
  - **National Framework for the Assurance of AI in Government (NFAAIG)** - June 2024 framework with 2025 technical standards (updated July 30, 2025)
  - **NIST AI Security Competency Area (NF-COM-002)** - NICE Framework v2.0.0
  - **ACSC AI Security Guidance** - Australian Cyber Security Centre guidance
- Workplace Health and Safety (WHS) duties under the _Work Health and Safety Act 2011 (Qld)_
- AI-specific security competencies from NIST's 46 competency statements (39 knowledge + 7 skills)

---

## Step 1: Team Formation and Planning

**Control Type: Administrative**  
Form a multi-disciplinary team with expertise in:

- Technical (developers, data scientists, architects)
- Legal, privacy, records, and ethics
- Operational ownership (business leads)
- Risk, security, and evaluation roles
- AI security competencies including:
  - Knowledge of AI model vulnerabilities (NIST AI-K005)
  - Knowledge of data poisoning attacks (NIST AI-K013)
  - Skill in identifying AI hallucinations (NIST AI-S006)
  - Skill in secure prompt engineering (NIST AI-S002)

Plan iterative workshops with phases for:

- Systems scoping and documentation
- Stakeholder engagement
- Values, risks and WHS impacts
- Control and mitigation planning

---

## Step 2: Define the AI Solution (Components Analysis)

**Control Type: Technical + Administrative**  
Base your system description on FAIRA Part A. Complete Tables 1–9 to map:

- Solution components, interfaces, data, outputs, and governance
- Use Microsoft’s lifecycle control checklist to add:
  - RBAC, model versioning, input sanitisation, data integrity validation
  - Known attack surfaces (e.g. API endpoints, sensor inputs, deployment vectors)
  - NIST-identified AI-specific vulnerabilities:
    - Model inversion and extraction attacks
    - Membership inference vulnerabilities
    - Data poisoning vectors (NIST AI-K013)
    - Adversarial example generation points
    - Misinformation/disinformation risks (NIST AI-K023)

Add WHS considerations such as:

- Effects on worker autonomy, task load, or role redundancy
- Risk of harm from flawed outputs in operational or critical systems
- Training needs and fatigue or stress from AI-human interaction

Use FAIRA Tables 2.2 and 2.3 to document these effects.

---

## Step 3: Values Assessment (Ethics, Equity, WHS)

**Control Type: Administrative + Engagement**  
Use FAIRA Part B to evaluate alignment with the 8 AI Ethics Principles.

For each principle:

1. Document intended benefits (e.g. fairness, transparency, safety)
2. Identify risks (e.g. bias, privacy violation, harm to employment)
   - Use NIST AI bias taxonomy (NIST AI-K003) to identify specific bias types
   - Consider non-explainable risk factors (NIST AI-S007)
3. Plan mitigations (e.g. explainability, training, opt-outs, contestability)

Ensure:

- Legislative references include _WHS Act 2011_, _Human Rights Act 2019_, _Public Sector Ethics Act 1994_
- Workplace and societal wellbeing are addressed, including psychological or ergonomic impacts
- Human-machine interactions are safe, understood, and support mental wellbeing

---

## Step 4: Risk Assessment and Scoring

**Control Type: Administrative**  
Create a consolidated risk register. Score by:

- **Severity** (harm to life, infrastructure, sensitive data compromise)
- **Likelihood** (model exposure, endpoint availability, data provenance)
- **Impact** (on operations, reputation, community trust)

Use Microsoft’s matrix of threat types (e.g. model inversion, data poisoning, evasion) to document and prioritise risks.

Use this to:

- Justify control prioritisation
- Document residual and accepted risks
- Support internal audit and governance sign-off

---

## Step 5: Controls and Mitigation Planning

**Control Tags: Technical, Policy, Human-centred, Engagement**  
Use FAIRA Part C and Microsoft’s risk control guidance to define a control suite. Tag by function:

| Control Type      | Examples                                                             |
| ----------------- | -------------------------------------------------------------------- |
| **Technical**     | Encryption, adversarial training, input validation, security testing |
| **Policy**        | Privacy impact assessments, recordkeeping, WHS documentation         |
| **Human-centred** | Consent flows, clear interfaces, worker retraining support           |
| **Engagement**    | Stakeholder feedback, WHS committee input, transparency notices      |

Assign owners (e.g. executive sponsor, policy advisor, platform engineer). Ensure traceability of each control to a specific risk.

---

## Step 6: Documenting and Reporting

**Control Type: Administrative + Technical**  
Maintain a live register with:

- Completed FAIRA template and values matrix
- Security threat logs, scoring rationale, and mitigation tables
- WHS impact notes and staff consultation outcomes
- All updates, exceptions, and decision rationales

Link artefacts to:

- Risk registers, HRAs, PIAs
- Procurement documentation (QITC alignment)
- Internal dashboards or assurance processes

---

## Step 7: Lifecycle Maintenance

**Control Type: Ongoing Governance**  
Treat the FAIRA as a living document. Refresh when:

- AI models or training data change
- Deployment expands into new domains
- Incidents or WHS triggers emerge
- New threats (e.g. via red teaming or audit) are discovered

Include:

- Annual FAIRA review and sign-off
- Continuous monitoring for drift and emerging risks
- WHS consultation and training updates (per Part 21 of State Government Entities Agreement 2023)

---

## Summary

This unified framework helps project teams implement practical, secure, and ethical AI by combining:

✅ FAIRA’s values-anchored assessment  
✅ Microsoft’s structured lifecycle safeguards  
✅ WHS and human-centred risk awareness

Use this to ensure Queensland’s public-facing and internal AI systems are:

- Safe for users and staff
- Resilient and secure
- Transparent and equitable
- Well-governed across their lifecycle

**Build AI that is safer, smarter, and fairer for Queensland.**

---

## Appendix: NIST AI Security Competencies Integration

To strengthen AI security capabilities, teams should develop competencies aligned with NIST's AI Security Competency Area **(NF-COM-002)**, which describes capabilities to secure Artificial Intelligence (AI) against cyberattacks, ensure it is adequately contained where used, and mitigate threats AI presents where used with malicious intent.

### Framework Status & Updates

- **Source**: NICE Workforce Framework for Cybersecurity (NIST SP 800-181 Rev 1)
- **Competency Area**: NF-COM-002 (AI Security)
- **Current Version**: NICE Framework Components v2.0.0 (March 2025)
- **Proposed Updates**: June 2025 - Additional Knowledge and Skill statements proposed (public comment closed July 17, 2025)

The framework currently references **46 AI-specific competencies** (39 knowledge areas + 7 skills) based on the March 2024 release, with enhancements proposed in June 2025 pending finalization.

### Essential Knowledge Areas

- **AI Model Vulnerabilities (AI-K005)**: Understanding attack vectors specific to ML models
- **Data Poisoning (AI-K013)**: Recognizing and preventing training data manipulation
- **AI Bias Types (AI-K003)**: Comprehensive taxonomy of bias in AI systems
- **AI Common Security Risks (AI-K007)**: Understanding general security risks in AI systems
- **Misinformation Risks (AI-K023)**: AI-generated content risks and detection
- **NIST AI RMF (AI-K024)**: Framework for systematic AI risk management

### Critical Skills

- **Prompt Engineering Security (AI-S002)**: Secure interaction with generative AI systems
- **Hallucination Detection (AI-S006)**: Identifying AI-generated errors and false outputs
- **Non-explainable Risk Assessment (AI-S007)**: Measuring opacity risks in AI decision-making

### Security Paradigms

- **Security OF AI**: Protecting AI systems from adversarial attacks, data poisoning, model theft, and other targeted threats
- **Security THROUGH AI**: Leveraging AI for threat detection, anomaly identification, automated response, and enhanced cybersecurity operations

This competency framework ensures teams have the necessary knowledge and skills to implement secure AI systems throughout their lifecycle. For the latest updates and complete competency listings, consult the [NICE Framework Resource Center](https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center) and [NICCS NICE Framework Tools](https://niccs.cisa.gov/tools/nice-framework).

---

## Related Frameworks & Tools

This unified framework integrates well with complementary assessment and benchmarking tools:

### Australian Government Frameworks

- **[National Framework for the Assurance of AI in Government (NFAAIG)](https://www.finance.gov.au/government/public-data/data-and-digital-ministers-meeting/national-framework-assurance-artificial-intelligence-government)** - Agreed June 2024, updated 2025
  - **Five Cornerstones**: Governance, data governance, risk-based approach, standards, and procurement
  - **Technical Standard**: Updated July 30, 2025
  - **Pilot Programs**: Completed 2024-2025 with agency feedback
  - **Policy Requirements**: Accountable officials designated by Nov 30, 2024; AI transparency statements by Feb 28, 2025
  - Based on Australia's 8 AI Ethics Principles for nationally consistent AI assurance

- **[Australian Responsible AI Index 2025](./frameworks/naic-rai-index-2025.md)** (NAIC/Fifth Quadrant) - Use for organisational maturity benchmarking and peer comparison aligned with VAISS guardrails

- **[Voluntary AI Safety Standard (VAISS)](https://www.industry.gov.au/publications/voluntary-ai-safety-standard)** - Released September 2024, v2 planned for 2025
  - **10 Guardrails**: Accountability, risk management, data governance, testing, human oversight, transparency, contestability, supply chain transparency, compliance, stakeholder engagement
  - Aligned with ISO/IEC 42001:2023 and NIST AI RMF 1.0
  - Applies to both AI deployers and developers

### International Frameworks

- **NIST AI Risk Management Framework (AI RMF)** - Provides structured risk governance approach
- **ISO/IEC 42001:2023** - International standard for AI management systems
- **OECD AI Principles** - International best practice alignment
- **EU AI Act** - Regulatory compliance considerations

These frameworks can be used in combination to provide comprehensive AI governance coverage across technical security, organisational maturity, and regulatory alignment.
