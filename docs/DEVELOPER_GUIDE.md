# Developer Guide: Machine-Readable AI Risk Assurance

> Using Schemas, APIs, and Automation for AI Governance

## Overview

This guide explains how to use the machine-readable formats in this repository to integrate AI risk assurance into your development workflows, CI/CD pipelines, and automated compliance checking systems.

## What's Available

### 📋 JSON Schemas (`/schemas/`)

Eight comprehensive JSON Schema files define the structure for AI governance data:

1. **`risk-register.schema.json`** - AI risk assessment register (GenAI threats, AI6/EU AI Act)
2. **`faira-assessment.schema.json`** - Queensland FAIRA framework assessment
3. **`control-catalog.schema.json`** - Cross-framework control library (AI6, EU AI Act, NIST GenAI)
4. **`nist-ai-competencies.schema.json`** - NIST AI Security competency tracking
5. **`vaiss-guardrails.schema.json`** - VAISS 10 guardrails assessment (v2 enhancements)
6. **`compliance-mapping.schema.json`** - Cross-framework compliance mapping (12 frameworks)
7. **`ai6-framework.schema.json`** - AI6 Framework 6 Essential Practices assessment
8. **`eu-ai-act.schema.json`** - EU AI Act compliance assessment

### 🗺️ YAML Mappings (`/mappings/`)

Seven cross-framework mapping files:

1. **`naic-rai-index-2025.yaml`** - Australian RAI Index taxonomy (OECD 2024, GenAI additions)
2. **`faira-microsoft-crosswalk.yaml`** - FAIRA ↔ Microsoft AI Security mapping
3. **`risk-taxonomy.yaml`** - Risk categories, severity scales, GenAI-specific risks
4. **`ai6-naic-crosswalk.yaml`** - AI6 Framework to VAISS, FAIRA, NIST, ISO 42001, EU AI Act
5. **`eu-ai-act-crosswalk.yaml`** - EU AI Act to Australian frameworks
6. **`nist-genai-profile-crosswalk.yaml`** - NIST GenAI Profile GOVERN/MAP/MEASURE/MANAGE
7. **`mas-ai-guidelines-crosswalk.yaml`** - MAS FEAT principles to Australian frameworks

## Quick Start

### 1. Validating Risk Data

**Using Python with `jsonschema`:**

```python
import json
import jsonschema
from jsonschema import validate

# Load the risk register schema
with open('schemas/risk-register.schema.json', 'r') as f:
    schema = json.load(f)

# Load your risk data
with open('my-risk-register.json', 'r') as f:
    risk_data = json.load(f)

# Validate
try:
    validate(instance=risk_data, schema=schema)
    print("✅ Risk register is valid!")
except jsonschema.exceptions.ValidationError as err:
    print(f"❌ Validation error: {err.message}")
```

**Using Node.js with `ajv`:**

```javascript
const Ajv = require('ajv');
const fs = require('fs');

const ajv = new Ajv();

// Load schema and data
const schema = JSON.parse(fs.readFileSync('schemas/risk-register.schema.json', 'utf8'));
const riskData = JSON.parse(fs.readFileSync('my-risk-register.json', 'utf8'));

// Validate
const validate = ajv.compile(schema);
const valid = validate(riskData);

if (valid) {
    console.log('✅ Risk register is valid!');
} else {
    console.log('❌ Validation errors:', validate.errors);
}
```

### 2. Creating a Risk Register

**Minimal Example:**

```json
{
  "metadata": {
    "version": "1.0.0",
    "createdDate": "2025-10-12",
    "lastUpdated": "2025-10-12T10:00:00Z",
    "assessmentId": "ASSESS-001",
    "projectName": "AI Chatbot System",
    "frameworksApplied": ["FAIRA v1.0.0", "VAISS v1.0"]
  },
  "risks": [
    {
      "riskId": "RISK-0001",
      "title": "Prompt Injection Vulnerability",
      "category": "Security",
      "severity": 4,
      "likelihood": 3,
      "riskScore": 12,
      "threatType": "Prompt Injection",
      "nistCompetency": ["AI-S-002"],
      "description": "Users may craft prompts to bypass safety controls",
      "status": "Identified"
    }
  ],
  "summary": {
    "totalRisks": 1,
    "averageRiskScore": 12
  }
}
```

### 3. Using YAML Mappings

**Loading Cross-Framework Mappings:**

```python
import yaml

# Load FAIRA-Microsoft crosswalk
with open('mappings/faira-microsoft-crosswalk.yaml', 'r') as f:
    crosswalk = yaml.safe_load(f)

# Find Microsoft controls for FAIRA Part A
part_a_mappings = crosswalk['part_a_mappings']
for mapping in part_a_mappings:
    print(f"{mapping['faira_component']}:")
    print(f"  Microsoft Phase: {mapping['microsoft_phase']}")
    print(f"  Controls: {mapping['microsoft_controls']}\n")
```

**Finding Risks by Category:**

```python
# Load risk taxonomy
with open('mappings/risk-taxonomy.yaml', 'r') as f:
    taxonomy = yaml.safe_load(f)

# Get all security subcategories
security_cat = taxonomy['risk_categories']['security']
print(f"Security Risk Subcategories: {security_cat['subcategories']}")

# Get Microsoft threat types for security risks
print(f"Microsoft Threats: {security_cat['microsoft_threat_types']}")
```

## Common Use Cases

### Use Case 1: Automated Risk Scoring

```python
def calculate_risk_priority(severity, likelihood):
    """Calculate risk score and priority level"""
    score = severity * likelihood

    if score >= 20:
        return score, "Extreme"
    elif score >= 15:
        return score, "Very High"
    elif score >= 10:
        return score, "High"
    elif score >= 5:
        return score, "Medium"
    else:
        return score, "Low"

# Example
risk_score, priority = calculate_risk_priority(severity=4, likelihood=4)
print(f"Risk Score: {risk_score}, Priority: {priority}")
# Output: Risk Score: 16, Priority: Very High
```

### Use Case 2: Compliance Checking

```python
import json

def check_vaiss_compliance(guardrail_assessment):
    """Check VAISS compliance level"""
    implemented = 0
    total = len(guardrail_assessment['guardrailAssessments'])

    for guardrail in guardrail_assessment['guardrailAssessments']:
        if guardrail['implementationStatus'] in ['Fully Implemented', 'Largely Implemented']:
            implemented += 1

    compliance_percentage = (implemented / total) * 100

    if compliance_percentage >= 80:
        return "Leading"
    elif compliance_percentage >= 60:
        return "Implementing"
    elif compliance_percentage >= 40:
        return "Developing"
    else:
        return "Emerging"

# Load and check
with open('my-vaiss-assessment.json', 'r') as f:
    assessment = json.load(f)

maturity_level = check_vaiss_compliance(assessment)
print(f"VAISS Maturity Level: {maturity_level}")
```

### Use Case 3: Generating Compliance Reports

```python
from datetime import datetime

def generate_compliance_report(risk_register, faira_assessment, vaiss_assessment):
    """Generate executive compliance report"""

    report = {
        "generated": datetime.now().isoformat(),
        "project": risk_register['metadata']['projectName'],
        "frameworks_assessed": risk_register['metadata']['frameworksApplied'],
        "risk_summary": {
            "total_risks": risk_register['summary']['totalRisks'],
            "high_priority": len([r for r in risk_register['risks']
                                  if r['riskScore'] >= 15]),
            "average_score": risk_register['summary']['averageRiskScore']
        },
        "faira_status": {
            "part_a_completed": bool(faira_assessment.get('partA')),
            "part_b_completed": bool(faira_assessment.get('partB')),
            "part_c_completed": bool(faira_assessment.get('partC'))
        },
        "vaiss_maturity": check_vaiss_compliance(vaiss_assessment)
    }

    return report

# Generate report
report = generate_compliance_report(risk_data, faira_data, vaiss_data)
print(json.dumps(report, indent=2))
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Validate AI Risk Assessments

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install jsonschema pyyaml

      - name: Validate Risk Register
        run: |
          python validate_schemas.py \
            --schema schemas/risk-register.schema.json \
            --data assessments/risk-register.json

      - name: Check Risk Scores
        run: |
          python check_risk_thresholds.py \
            --data assessments/risk-register.json \
            --max-score 20
```

### Pre-Commit Hook Example

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: validate-risk-register
        name: Validate Risk Register
        entry: python scripts/validate_risk_register.py
        language: python
        files: 'assessments/.*\.json$'
        additional_dependencies: ['jsonschema']
```

## Advanced Patterns

### Pattern 1: Cross-Framework Control Mapping

```python
def find_controls_for_risk(risk_id, control_catalog, mappings):
    """Find all controls across frameworks that address a risk"""

    controls = []

    for control in control_catalog['controls']:
        if risk_id in control.get('applicableRiskTypes', []):
            controls.append({
                'control_id': control['controlId'],
                'title': control['title'],
                'frameworks': {
                    'faira': control['frameworks'].get('faira'),
                    'microsoft': control['frameworks'].get('microsoftAI'),
                    'vaiss': control['frameworks'].get('vaissGuardrails'),
                    'nist': control['frameworks'].get('nistCompetencies')
                }
            })

    return controls

# Usage
controls = find_controls_for_risk('RISK-0001', catalog_data, mapping_data)
for control in controls:
    print(f"Control: {control['title']}")
    print(f"  VAISS Guardrails: {control['frameworks']['vaiss']}")
```

### Pattern 2: NIST Competency Gap Analysis

```python
def assess_team_competencies(team_assessment, required_competencies):
    """Identify competency gaps in team"""

    gaps = []

    for required in required_competencies:
        found = False
        for member in team_assessment['teamMembers']:
            for comp in member.get('knowledgeAreas', []) + member.get('skills', []):
                if comp['competencyId'] == required:
                    if comp['proficiencyLevel'] in ['Advanced', 'Expert']:
                        found = True
                        break

        if not found:
            gaps.append({
                'competency': required,
                'severity': 'High',
                'recommendation': 'Training or recruitment needed'
            })

    return gaps

# Usage
required = ['AI-K-005', 'AI-K-013', 'AI-S-002', 'AI-S-006']
gaps = assess_team_competencies(team_data, required)
print(f"Found {len(gaps)} competency gaps")
```

### Pattern 3: Automated FAIRA Completion Checker

```python
def check_faira_completeness(faira_assessment):
    """Check if FAIRA assessment is complete"""

    completeness = {
        'part_a': {
            'required_tables': ['solutionOverview', 'componentArchitecture',
                              'interfaces', 'dataSources', 'dataTypes',
                              'outputs', 'usersAndStakeholders',
                              'governance', 'relatedSystems'],
            'completed': []
        },
        'part_b': {
            'required_principles': 8,
            'completed_count': len(faira_assessment['partB']['ethicsPrinciples'])
        },
        'part_c': {
            'minimum_controls': 10,
            'control_count': len(faira_assessment['partC']['controlPlan'])
        }
    }

    # Check Part A completeness
    part_a = faira_assessment['partA']
    for table in completeness['part_a']['required_tables']:
        if table in part_a and part_a[table]:
            completeness['part_a']['completed'].append(table)

    completeness['part_a']['percentage'] = (
        len(completeness['part_a']['completed']) /
        len(completeness['part_a']['required_tables']) * 100
    )

    return completeness

# Usage
completeness = check_faira_completeness(faira_data)
print(f"Part A: {completeness['part_a']['percentage']:.0f}% complete")
print(f"Part B: {completeness['part_b']['completed_count']}/8 principles assessed")
print(f"Part C: {completeness['part_c']['control_count']} controls defined")
```

## Best Practices

### 1. Version Control Your Assessments

```bash
# Store assessments in git
git add assessments/risk-register.json
git commit -m "Update risk assessment - added RISK-0015"
git push
```

### 2. Separate Sensitive and Public Data

```text
assessments/
├── public/
│   ├── risk-categories.json      # Safe to share
│   └── control-catalog.json       # Safe to share
└── confidential/
    ├── risk-register.json         # Contains sensitive details
    └── faira-assessment.json      # Contains org-specific data
```

### 3. Use Schema Validation in Production

```python
def save_risk_register(data, filepath):
    """Save risk register with validation"""

    # Validate before saving
    with open('schemas/risk-register.schema.json', 'r') as f:
        schema = json.load(f)

    try:
        jsonschema.validate(instance=data, schema=schema)
    except jsonschema.ValidationError as err:
        raise ValueError(f"Invalid risk register: {err.message}")

    # Save if valid
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

    return True
```

### 4. Automate Regular Reviews

```python
from datetime import datetime, timedelta

def check_review_due(risk_register):
    """Check which risks need review"""

    due_for_review = []
    today = datetime.now().date()

    for risk in risk_register['risks']:
        last_reviewed = datetime.fromisoformat(
            risk.get('lastReviewed', risk['identifiedDate'])
        ).date()

        # High risks: review every 3 months
        # Medium risks: review every 6 months
        # Low risks: review annually
        if risk['riskScore'] >= 10:
            review_interval = 90
        elif risk['riskScore'] >= 5:
            review_interval = 180
        else:
            review_interval = 365

        next_review = last_reviewed + timedelta(days=review_interval)

        if today >= next_review:
            due_for_review.append({
                'risk_id': risk['riskId'],
                'title': risk['title'],
                'days_overdue': (today - next_review).days
            })

    return due_for_review
```

## Troubleshooting

### Common Validation Errors

#### Error: Missing required property

```text
Solution: Check the schema's "required" array and ensure all fields are present.
```

#### Error: Additional property not allowed

```text
Solution: The schema uses "additionalProperties": false. Only use defined properties.
```

#### Error: Pattern mismatch

```text
Solution: IDs must match patterns like "RISK-0001" or "CTRL-0001" (4 digits).
```

### Performance Tips

1. **Cache compiled schemas** - Don't recompile schemas on every validation
2. **Use streaming for large files** - Don't load entire register into memory
3. **Index risk data** - Create indexes on frequently queried fields

## Resources

- **JSON Schema Documentation**: <https://json-schema.org/>
- **YAML Specification**: <https://yaml.org/spec/>
- **Python jsonschema**: <https://python-jsonschema.readthedocs.io/>
- **AJV (Node.js)**: <https://ajv.js.org/>

## Next Steps

1. **Try the examples** in this guide with your own data
2. **Explore the schemas** in `/schemas/` directory
3. **Review the mappings** in `/mappings/` directory
4. **Set up validation** in your CI/CD pipeline
5. **Contribute** improvements back to the repository

## Support

- Open an issue: <https://github.com/OAK-AI-Public/ai-risk-assurance-faira-microsoft/issues>
- Read the full framework: [`Unified_AI_Risk_Assurance_Framework.md`](../Unified_AI_Risk_Assurance_Framework.md)
- Review checklists: [`AI_Risk_Assurance_Checklists.md`](../AI_Risk_Assurance_Checklists.md)

---

**Happy building secure, responsible AI systems!** 🛡️🤖
