# API Use Cases: Real-World Applications

This document explains how organisations can use the AI Risk Assurance API in practical, day-to-day scenarios.

## Who Would Use This API?

### Government Agencies

- **Queensland Government departments** implementing AI systems
- **Federal agencies** required to comply with NFAAIG
- **IT teams** managing multiple AI projects across departments

### Private Sector

- **AI vendors** building solutions for government
- **Consulting firms** conducting risk assessments for clients
- **Enterprise organisations** with AI governance requirements

### Development Teams

- **DevOps engineers** integrating risk checks into CI/CD pipelines
- **Compliance officers** tracking AI system compliance
- **Risk managers** generating reports for audits

---

## Use Case 1: Automated Risk Assessment in CI/CD Pipeline

### Scenario

Your development team is building an AI-powered customer service chatbot. Every time you deploy a new version, you need to assess risks.

### Without API (Manual Process)
1. Developer completes code changes
2. Downloads risk register Excel template
3. Manually fills out 50+ fields
4. Emails to compliance team
5. Compliance team reviews and files it
6. Takes 2-3 days

### With API (Automated)

```yaml
# .github/workflows/deploy.yml
name: Deploy AI System

on:
  push:
    branches: [main]

jobs:
  risk-assessment:
    runs-on: ubuntu-latest
    steps:
      - name: Create Risk Register
        run: |
          curl -X POST https://api.example.qld.gov.au/v2/risk-registers \
            -H "X-API-Key: ${{ secrets.RISK_API_KEY }}" \
            -H "Content-Type: application/json" \
            -d @deployment-risks.json

      - name: Check Compliance
        run: |
          curl -X POST https://api.example.qld.gov.au/v2/compliance/check \
            -H "X-API-Key: ${{ secrets.RISK_API_KEY }}" \
            -d '{
              "assessmentId": "CHATBOT-v2.1",
              "frameworks": ["FAIRA", "VAISS", "NIST"]
            }'

      - name: Fail if high-risk gaps found
        run: |
          # Parse response, fail deployment if critical gaps exist
```

**Result**: Risk assessment happens automatically in seconds, blocks deployment if critical issues found.

---

## Use Case 2: Multi-Project Risk Dashboard

### Scenario

A government department has 15 different AI projects running simultaneously. The CIO needs to see risk status across all projects.

### Implementation

```python
# dashboard.py - Backend for executive dashboard
import requests
from datetime import datetime

def get_department_risk_overview():
    """Fetch all risk registers for dashboard"""

    # Get all active projects
    response = requests.get(
        'https://api.example.qld.gov.au/v2/risk-registers',
        headers={'X-API-Key': API_KEY},
        params={
            'status': 'Assessed',
            'limit': 100
        }
    )

    projects = response.json()['data']

    # Generate executive summary
    summary = {
        'total_projects': len(projects),
        'high_risk_count': sum(1 for p in projects if p['highPriorityRisks'] > 0),
        'projects': []
    }

    for project in projects:
        # Get detailed compliance for each project
        compliance = requests.post(
            'https://api.example.qld.gov.au/v2/compliance/check',
            headers={'X-API-Key': API_KEY},
            json={
                'assessmentId': project['assessmentId'],
                'frameworks': ['FAIRA', 'VAISS', 'NFAAIG']
            }
        ).json()

        summary['projects'].append({
            'name': project['projectName'],
            'risk_count': project['totalRisks'],
            'compliance_score': compliance['frameworks'][0]['compliancePercentage'],
            'status': 'At Risk' if compliance['frameworks'][0]['compliancePercentage'] < 80 else 'Compliant'
        })

    return summary

# Use in web dashboard
@app.route('/executive-dashboard')
def dashboard():
    data = get_department_risk_overview()
    return render_template('dashboard.html', data=data)
```

**Result**: Real-time visibility across all AI projects, automated compliance tracking, executive reporting.

---

## Use Case 3: Third-Party Vendor Assessment

### Scenario

A government agency is procuring an AI system from a vendor. They need to verify the vendor's risk assessment meets FAIRA requirements.

### Workflow

```python
# vendor_assessment.py
import requests

def validate_vendor_submission(vendor_risk_file):
    """Validate vendor's risk assessment submission"""

    with open(vendor_risk_file, 'r') as f:
        vendor_data = json.load(f)

    # Step 1: Validate against schema
    validation = requests.post(
        'https://api.example.qld.gov.au/v2/validate/risk-register',
        headers={'X-API-Key': API_KEY},
        json=vendor_data
    ).json()

    if not validation['valid']:
        return {
            'approved': False,
            'reason': 'Schema validation failed',
            'errors': validation['errors']
        }

    # Step 2: Check FAIRA compliance
    compliance = requests.post(
        'https://api.example.qld.gov.au/v2/compliance/check',
        headers={'X-API-Key': API_KEY},
        json={
            'assessmentId': vendor_data['metadata']['assessmentId'],
            'frameworks': ['FAIRA', 'NFAAIG']
        }
    ).json()

    faira_score = compliance['frameworks'][0]['compliancePercentage']

    if faira_score < 90:
        # Identify specific gaps
        gaps = requests.post(
            'https://api.example.qld.gov.au/v2/compliance/gaps',
            headers={'X-API-Key': API_KEY},
            json={
                'assessmentId': vendor_data['metadata']['assessmentId'],
                'targetFramework': 'FAIRA'
            }
        ).json()

        return {
            'approved': False,
            'reason': f'FAIRA compliance only {faira_score}% (minimum 90% required)',
            'gaps': gaps['gaps']
        }

    return {
        'approved': True,
        'compliance_score': faira_score
    }

# Usage in procurement process
result = validate_vendor_submission('vendor_abc_risk_assessment.json')
if result['approved']:
    print("✅ Vendor assessment approved for procurement")
else:
    print(f"❌ Rejected: {result['reason']}")
    print("Required improvements:", result.get('gaps'))
```

**Result**: Automated vendor assessment validation, consistent procurement standards, clear rejection reasons with remediation guidance.

---

## Use Case 4: Continuous Compliance Monitoring

### Scenario

An AI system is deployed and running in production. Regulations change (e.g., NFAAIG July 2025 updates). You need to re-assess existing systems against new requirements.

### Implementation

```python
# compliance_monitor.py - Scheduled job (runs monthly)
import requests
from datetime import datetime

def monthly_compliance_check():
    """Re-check all production AI systems against current frameworks"""

    # Get all production systems
    systems = requests.get(
        'https://api.example.qld.gov.au/v2/risk-registers',
        headers={'X-API-Key': API_KEY},
        params={'status': 'Mitigated'}  # Production systems
    ).json()['data']

    non_compliant_systems = []

    for system in systems:
        # Check against latest framework versions
        compliance = requests.post(
            'https://api.example.qld.gov.au/v2/compliance/check',
            headers={'X-API-Key': API_KEY},
            json={
                'assessmentId': system['assessmentId'],
                'frameworks': ['FAIRA', 'NFAAIG', 'VAISS']
            }
        ).json()

        for framework in compliance['frameworks']:
            if not framework['compliant']:
                non_compliant_systems.append({
                    'project': system['projectName'],
                    'framework': framework['framework'],
                    'compliance': framework['compliancePercentage'],
                    'gaps': framework['gaps']
                })

    if non_compliant_systems:
        # Send alert to compliance team
        send_alert_email(
            to='compliance-team@example.qld.gov.au',
            subject=f'Monthly Compliance Alert - {len(non_compliant_systems)} systems need attention',
            body=format_compliance_report(non_compliant_systems)
        )

    return non_compliant_systems

# Schedule with cron or cloud scheduler
# 0 9 1 * * /usr/bin/python3 /opt/compliance_monitor.py
```

**Result**: Proactive compliance monitoring, early detection of regulatory drift, automated alerts for remediation.

---

## Use Case 5: Risk Treatment Workflow

### Scenario

A risk has been identified. You need to track it through identification → assessment → mitigation → closure.

### Implementation

```python
# risk_workflow.py
import requests
from enum import Enum

class RiskStatus(Enum):
    IDENTIFIED = "Identified"
    ASSESSED = "Assessed"
    MITIGATION_PLANNED = "Mitigation Planned"
    MITIGATION_IN_PROGRESS = "Mitigation In Progress"
    MITIGATED = "Mitigated"
    CLOSED = "Closed"

class RiskWorkflow:
    def __init__(self, api_key, register_id):
        self.api_key = api_key
        self.register_id = register_id
        self.base_url = 'https://api.example.qld.gov.au/v2'

    def add_new_risk(self, risk_details):
        """Step 1: Risk identified"""
        risk_details['status'] = RiskStatus.IDENTIFIED.value

        response = requests.post(
            f'{self.base_url}/risk-registers/{self.register_id}/risks',
            headers={'X-API-Key': self.api_key},
            json=risk_details
        )

        return response.json()['riskId']

    def assess_risk(self, risk_id, severity, likelihood, controls):
        """Step 2: Risk assessed with controls"""
        update = {
            'severity': severity,
            'likelihood': likelihood,
            'riskScore': severity * likelihood,
            'existingControls': controls,
            'status': RiskStatus.ASSESSED.value
        }

        requests.put(
            f'{self.base_url}/risk-registers/{self.register_id}/risks/{risk_id}',
            headers={'X-API-Key': self.api_key},
            json=update
        )

    def plan_mitigation(self, risk_id, mitigation_plan):
        """Step 3: Mitigation planned"""
        update = {
            'mitigationPlan': mitigation_plan,
            'status': RiskStatus.MITIGATION_PLANNED.value
        }

        requests.put(
            f'{self.base_url}/risk-registers/{self.register_id}/risks/{risk_id}',
            headers={'X-API-Key': self.api_key},
            json=update
        )

    def start_mitigation(self, risk_id, owner, due_date):
        """Step 4: Mitigation in progress"""
        update = {
            'riskOwner': owner,
            'targetDate': due_date,
            'status': RiskStatus.MITIGATION_IN_PROGRESS.value
        }

        requests.put(
            f'{self.base_url}/risk-registers/{self.register_id}/risks/{risk_id}',
            headers={'X-API-Key': self.api_key},
            json=update
        )

    def complete_mitigation(self, risk_id, residual_severity, residual_likelihood):
        """Step 5: Mitigation completed"""
        update = {
            'residualSeverity': residual_severity,
            'residualLikelihood': residual_likelihood,
            'residualRiskScore': residual_severity * residual_likelihood,
            'status': RiskStatus.MITIGATED.value
        }

        requests.put(
            f'{self.base_url}/risk-registers/{self.register_id}/risks/{risk_id}',
            headers={'X-API-Key': self.api_key},
            json=update
        )

# Example usage
workflow = RiskWorkflow(API_KEY, 'ASSESS-2025-001')

# Day 1: Risk discovered
risk_id = workflow.add_new_risk({
    'riskId': 'RISK-0042',
    'title': 'Bias in loan approval model',
    'category': 'Bias',
    'description': 'Model may discriminate against certain demographics'
})

# Day 2: Risk assessed
workflow.assess_risk(
    risk_id,
    severity=4,
    likelihood=3,
    controls=['Fairness testing', 'Human review for edge cases']
)

# Day 3: Mitigation planned
workflow.plan_mitigation(
    risk_id,
    mitigation_plan='Implement fairness constraints, add demographic parity testing'
)

# Week 2: Work begins
workflow.start_mitigation(risk_id, owner='data-science-team@example.qld.gov.au', due_date='2025-11-30')

# Week 6: Mitigation complete
workflow.complete_mitigation(risk_id, residual_severity=2, residual_likelihood=2)
```

**Result**: Structured workflow, audit trail, accountability tracking, residual risk calculation.

---

## Use Case 6: Framework Mapping for Cross-Jurisdiction Projects

### Scenario

Your AI project needs to comply with both Queensland (FAIRA) and Federal (NFAAIG) requirements. You want to know which controls satisfy both.

### Implementation

```python
# framework_mapper.py
import requests

def get_dual_compliance_requirements():
    """Find controls that satisfy both FAIRA and NFAAIG"""

    # Get FAIRA → NFAAIG mappings
    faira_mappings = requests.get(
        'https://api.example.qld.gov.au/v2/frameworks/faira/mappings',
        headers={'X-API-Key': API_KEY},
        params={'targetFramework': 'nfaaig'}
    ).json()

    efficient_controls = []

    for mapping in faira_mappings['mappings']:
        if mapping['alignmentStrength'] == 'Full':
            # This control satisfies both frameworks
            efficient_controls.append({
                'faira_requirement': mapping['sourceRequirement'],
                'nfaaig_requirements': mapping['targetRequirements'],
                'control_suggestion': get_control_recommendation(mapping['sourceRequirement'])
            })

    return efficient_controls

def get_control_recommendation(requirement_id):
    """Get specific control recommendations from control catalog"""
    # Query control catalog schema
    return "Implement input validation with audit logging"

# Generate implementation guide
controls = get_dual_compliance_requirements()
print(f"Implement these {len(controls)} controls to satisfy both FAIRA and NFAAIG:")
for ctrl in controls:
    print(f"  - {ctrl['control_suggestion']}")
    print(f"    ✓ FAIRA: {ctrl['faira_requirement']}")
    print(f"    ✓ NFAAIG: {', '.join(ctrl['nfaaig_requirements'])}")
```

**Result**: Efficient compliance strategy, avoid duplicate work, clear implementation roadmap.

---

## Integration Patterns

### Pattern 1: Web Application Integration

```javascript
// React frontend for risk assessment form
async function submitRiskAssessment(formData) {
  // Validate before submission
  const validation = await fetch('/api/v2/validate/risk-register', {
    method: 'POST',
    headers: {
      'X-API-Key': process.env.RISK_API_KEY,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(formData)
  });

  const validationResult = await validation.json();

  if (!validationResult.valid) {
    // Show errors to user in real-time
    setErrors(validationResult.errors);
    return;
  }

  // Submit to risk register
  const response = await fetch('/api/v2/risk-registers', {
    method: 'POST',
    headers: {
      'X-API-Key': process.env.RISK_API_KEY,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(formData)
  });

  if (response.ok) {
    showSuccess('Risk assessment created successfully');
  }
}
```

### Pattern 2: ServiceNow Integration

```python
# servicenow_integration.py
def sync_risk_to_servicenow(risk_id):
    """Sync risk register to ServiceNow ticket"""

    # Get risk from API
    risk = requests.get(
        f'https://api.example.qld.gov.au/v2/risk-registers/ASSESS-001/risks/{risk_id}',
        headers={'X-API-Key': API_KEY}
    ).json()

    # Create ServiceNow incident
    servicenow_ticket = {
        'short_description': f"AI Risk: {risk['title']}",
        'description': risk['description'],
        'priority': map_severity_to_priority(risk['severity']),
        'assignment_group': 'AI Governance Team',
        'custom_fields': {
            'risk_id': risk['riskId'],
            'risk_score': risk['riskScore'],
            'faira_compliance': get_compliance_status(risk_id)
        }
    }

    # Submit to ServiceNow
    requests.post(
        'https://yourorg.service-now.com/api/now/table/incident',
        auth=(SERVICENOW_USER, SERVICENOW_PASS),
        json=servicenow_ticket
    )
```

### Pattern 3: Power BI Reporting

```python
# Export data for Power BI dashboard
def export_for_powerbi():
    """Export all risk data for Power BI consumption"""

    all_risks = []
    page = 1

    while True:
        response = requests.get(
            'https://api.example.qld.gov.au/v2/risk-registers',
            headers={'X-API-Key': API_KEY},
            params={'page': page, 'limit': 100}
        ).json()

        all_risks.extend(response['data'])

        if page >= response['pagination']['totalPages']:
            break
        page += 1

    # Convert to DataFrame for Power BI
    import pandas as pd
    df = pd.DataFrame(all_risks)
    df.to_csv('/powerbi/risk_data.csv', index=False)

    return df
```

---

## Benefits Summary

| Without API | With API |
|-------------|----------|
| Manual data entry (hours) | Automated data submission (seconds) |
| Spreadsheet chaos | Centralized risk database |
| No real-time compliance view | Live compliance dashboards |
| Manual audit preparation | Automated audit reports |
| Siloed risk information | Cross-project risk visibility |
| Point-in-time assessments | Continuous monitoring |
| Inconsistent risk tracking | Standardized workflow |

---

## Next Steps

1. **For Developers**: See `api/README.md` for authentication and endpoint documentation
2. **For Risk Managers**: Contact your IT team to discuss API integration requirements
3. **For Government Agencies**: Evaluate API for alignment with existing systems (ServiceNow, SharePoint, etc.)

The API specification (`api/openapi.yaml`) can be used to generate:
- Client SDKs (Python, JavaScript, Java, C#)
- API documentation portals
- Mock servers for testing
- Contract testing suites
