# EU AI Act - Regulation (EU) 2024/1689

**The World's First Comprehensive AI Regulation**

## Overview

The EU AI Act (Regulation (EU) 2024/1689) is the European Union's comprehensive legal framework for artificial intelligence. It establishes harmonised rules for AI systems across the EU market, with a risk-based approach that imposes different obligations depending on the risk level of AI applications.

## Regulation Information

| Attribute | Value |
|-----------|-------|
| **Name** | EU AI Act |
| **Full Title** | Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence |
| **Publisher** | European Parliament and Council |
| **Entry into Force** | 1 August 2024 |
| **Status** | In force (phased implementation) |
| **Type** | Binding EU regulation |
| **Scope** | AI systems on EU market or affecting EU residents |

## Relevance for Australian Organisations

### When the EU AI Act Applies

Australian organisations are subject to EU AI Act requirements when:

1. **AI placed on EU market** - AI systems or GPAI models made available in the EU
2. **AI outputs used in EU** - System outputs affect people within the EU
3. **Provider established in EU** - Even if development occurs elsewhere
4. **EU data subjects** - AI processes data of EU residents

### Recommended Actions

- Conduct risk classification for all AI systems with EU exposure
- Map existing VAISS/AI6 compliance to EU AI Act requirements
- Identify gaps in technical documentation
- Establish conformity assessment procedures for high-risk systems
- Implement transparency measures for GenAI systems

---

## Implementation Timeline

| Milestone | Date | Status |
|-----------|------|--------|
| Entry into force | 1 August 2024 | ✅ Complete |
| **Prohibited AI practices (Article 5)** | **2 February 2025** | ✅ In effect |
| **GPAI model obligations** | **2 August 2025** | ✅ In effect |
| High-risk AI obligations | 2 August 2026 | ⏳ Upcoming |
| Annex I extensions | 2 August 2027 | 🔮 Future |

---

## Risk Classification System

### Unacceptable Risk (Prohibited - Article 5)

AI practices that are **banned** in the EU:

| Prohibited Practice | Description |
|--------------------|-------------|
| Subliminal manipulation | AI using subliminal techniques beyond consciousness |
| Exploitation of vulnerabilities | Targeting age, disability, or social circumstances |
| Social scoring | Public authority social scoring systems |
| Real-time biometric ID | Remote biometric identification in public spaces (with exceptions) |
| Emotion recognition (workplace) | In workplace or educational contexts |
| Biometric categorisation | Inferring sensitive attributes (race, religion, sexuality) |
| Facial recognition scraping | Untargeted scraping for facial recognition databases |
| Predictive policing | Based solely on profiling without objective facts |

**Australian Relevance**: If your AI could be interpreted as any of these, it cannot be used with EU residents.

### High-Risk (Annex III Categories)

AI systems in these areas face **stringent requirements**:

| Category | Examples |
|----------|----------|
| **Biometric identification** | Remote biometric ID (not real-time), emotion recognition, biometric categorisation |
| **Critical infrastructure** | Safety components in water, gas, electricity, transport |
| **Education** | Access decisions, learning assessment, exam proctoring |
| **Employment** | Recruitment, hiring, worker management, evaluation |
| **Essential services** | Credit scoring, insurance risk, emergency dispatch |
| **Law enforcement** | Risk assessment, evidence reliability, profiling |
| **Migration** | Visa applications, asylum, border control |
| **Justice** | Legal research, applying law, sentencing |

### Limited Risk

AI systems with **specific transparency obligations**:

- **Chatbots/AI assistants**: Must disclose AI interaction
- **Emotion recognition**: Inform affected persons
- **Deepfakes**: Label AI-generated/manipulated content
- **GenAI outputs**: Mark synthetic audio, image, video, text

### Minimal Risk

Most AI systems with **no specific obligations**:

- AI-enabled video games
- Spam filters
- Inventory management systems

---

## High-Risk Requirements (Chapter 2)

For high-risk AI systems, providers must comply with:

### Article 8: Compliance with Requirements

High-risk AI systems shall comply with all Chapter 2 requirements throughout their lifecycle.

### Article 9: Risk Management System

| Requirement | Description |
|-------------|-------------|
| Establish system | Continuous iterative risk management |
| Risk identification | Identify and analyse known/foreseeable risks |
| Risk estimation | Estimate risks from intended use and misuse |
| Risk mitigation | Adopt risk management measures |
| Residual risk | Ensure residual risks are acceptable |
| Testing | Appropriate testing procedures |

**VAISS Alignment**: Guardrail 2 (Risk Management) - Full alignment

### Article 10: Data and Data Governance

| Requirement | Description |
|-------------|-------------|
| Training data | Subject to appropriate governance |
| Quality criteria | Relevance, representativeness, correctness |
| Bias examination | Detect, prevent, mitigate biases |
| Gap identification | Identify data gaps and shortcomings |

**VAISS Alignment**: Guardrail 3 (Data Governance) - Full alignment

### Article 11: Technical Documentation

Technical documentation drawn up before market placement, containing:

- General system description
- Development process elements
- Monitoring, functioning, control
- Risk management information
- Applicable standards
- EU declaration of conformity

**FAIRA Alignment**: Part A (all tables) provides documentation foundation

### Article 12: Record-keeping (Logging)

| Requirement | Description |
|-------------|-------------|
| Automatic logging | Enable traceability |
| Retention | Appropriate to intended purpose |
| Access | Available to market surveillance authorities |

### Article 13: Transparency and Information

Instructions for use must include:

- Provider identity and contact
- AI system characteristics, capabilities, limitations
- Human oversight measures
- Expected lifetime and maintenance

**VAISS Alignment**: Guardrail 6 (Transparency) - Full alignment

### Article 14: Human Oversight

Measures enabling humans to:

| Capability | Description |
|------------|-------------|
| Understand | Fully understand system capabilities |
| Interpret | Correctly interpret outputs |
| Decide | Decide not to use or override |
| Intervene | Interrupt or stop operation |

**VAISS Alignment**: Guardrail 5 (Human Oversight) - Full alignment
**AI6 Alignment**: Practice 6 (Human Oversight and Control)

### Article 15: Accuracy, Robustness, Cybersecurity

| Requirement | Description |
|-------------|-------------|
| Accuracy levels | Appropriate for intended purpose |
| Robustness | Against errors and inconsistencies |
| Cybersecurity | Protection against attacks |
| Adversarial resilience | Resilience against adversarial manipulation |

---

## GPAI Model Requirements (Chapter V)

### All GPAI Models (Article 53)

| Requirement | Description |
|-------------|-------------|
| Technical documentation | Maintained and up-to-date |
| Information for downstream | For AI system providers using the model |
| Copyright policy | Respecting Union copyright law |
| Training summary | Sufficiently detailed content summary |

### Systemic Risk Models (Article 55)

GPAI models with >10^25 FLOPs or designated systemic risk:

| Requirement | Description |
|-------------|-------------|
| Model evaluation | Standardised evaluation protocols |
| Adversarial testing | Assess and mitigate systemic risks |
| Incident reporting | Report serious incidents to AI Office |
| Cybersecurity | Adequate protection level |
| Energy consumption | Document and report |

**VAISS v2 Alignment**: Content provenance, watermarking, developer guardrails

---

## Transparency Obligations (Article 50)

### AI System Interaction

When AI systems interact with natural persons:
- Must inform they are interacting with AI
- Unless obvious from circumstances

### Emotion Recognition / Biometric Categorisation

When systems recognise emotions or perform biometric categorisation:
- Must inform affected persons
- Apply personal data protection rules

### AI-Generated Content (Including Deepfakes)

Providers of AI generating synthetic content must:
- Mark outputs as AI-generated
- Use machine-readable format
- Enable detection

**Note**: Artistic, satirical, and obviously fictional content has lighter requirements.

---

## Conformity Assessment

### Internal Control (Most High-Risk)

Provider self-assessment for most Annex III high-risk systems:

1. Quality management system
2. Technical documentation review
3. Performance assessment
4. EU Declaration of Conformity
5. CE marking

### Third-Party Assessment (Specific Cases)

Required for:
- Biometric identification systems
- Critical infrastructure safety components
- When relying on harmonised standards with limitations

---

## Australian Framework Alignment

### VAISS Alignment

| EU AI Act Requirement | VAISS Guardrail | Strength |
|----------------------|-----------------|----------|
| Risk management | G2: Risk Management | Full |
| Data governance | G3: Data Governance | Full |
| Transparency | G6: Transparency | Full |
| Human oversight | G5: Human Oversight | Full |
| Testing/monitoring | G4: Testing and Monitoring | Full |
| Accountability | G1: Accountability | Full |
| Compliance | G9: Compliance | Full |
| Supply chain | G8: Supply Chain | Partial |

### AI6 Alignment

| EU AI Act Requirement | AI6 Practice | Alignment |
|----------------------|--------------|-----------|
| Governance | P1: Governance and Accountability | High |
| Risk management | P2: Risk Management | High |
| Data governance | P3: Data Quality and Privacy | High |
| Testing | P4: Testing and Validation | High |
| Transparency | P5: Transparency and Explainability | High |
| Human oversight | P6: Human Oversight and Control | High |

### FAIRA Alignment

| EU AI Act Requirement | FAIRA Component | Notes |
|----------------------|-----------------|-------|
| Documentation | Part A (all tables) | Good foundation |
| Values/ethics | Part B (8 principles) | Broader than EU Act |
| Controls | Part C | Risk-focused approach |

---

## Penalties

| Violation | Maximum Fine |
|-----------|--------------|
| Prohibited AI practices | €35M or 7% global turnover |
| High-risk requirements | €15M or 3% global turnover |
| Incorrect information | €7.5M or 1.5% global turnover |
| SME reduced penalties | Proportionate reductions |

---

## Gap Analysis: EU AI Act vs Australian Frameworks

### Unique to EU AI Act

- Risk classification system (Unacceptable/High/Limited/Minimal)
- Conformity assessment and CE marking
- EU database registration
- Notified body involvement
- Market surveillance authorities
- Significant financial penalties

### Unique to Australian Frameworks

- WHS integration (FAIRA)
- 8 AI Ethics Principles focus
- Voluntary/self-assessment approach (currently)
- National AI Capability Plan alignment (VAISS v2)

### Shared Requirements

- Risk management
- Data governance
- Transparency
- Human oversight
- Testing and monitoring
- Accountability and governance

---

## Resources

### Official Sources

- **EU AI Act Text**: [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- **Implementation Timeline**: [AI Act EU](https://artificialintelligenceact.eu/implementation-timeline/)
- **European AI Office**: [European Commission](https://digital-strategy.ec.europa.eu/en/policies/ai-office)

### Guidance

- [European Commission AI Act FAQ](https://digital-strategy.ec.europa.eu/en/faqs/ai-act-questions-and-answers)
- [AI Act Explorer](https://artificialintelligenceact.eu/ai-act-explorer/)

---

## Document Information

| Attribute | Value |
|-----------|-------|
| **Regulation** | EU AI Act (2024/1689) |
| **Entry into Force** | 1 August 2024 |
| **Publisher** | European Parliament and Council |
| **Status** | In force (phased implementation) |
| **Document Updated** | February 2026 |

---

*This framework description is part of the [Unified AI Risk Assurance Framework](../README.md) maintained by [OAK AI](https://github.com/OAK-AI-Public).*
