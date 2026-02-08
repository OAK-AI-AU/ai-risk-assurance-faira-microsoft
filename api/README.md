# AI Risk Assurance API - Reference Documentation

Comprehensive REST API for managing AI risk assessments using the Unified AI Risk Assurance Framework.

**Version**: 3.0.0
**OpenAPI Specification**: [openapi.yaml](./openapi.yaml)

---

## 📋 Table of Contents

- [Overview](#overview)
- **[Real-World Use Cases](./USE_CASES.md)** ⭐ **Start here for practical examples**
- [Authentication](#authentication)
- [Rate Limiting](#rate-limiting)
- [Base URLs](#base-urls)
- [Quick Start](#quick-start)
- [Endpoints](#endpoints)
  - [Risk Registers](#risk-registers)
  - [FAIRA Assessments](#faira-assessments)
  - [VAISS Assessments](#vaiss-assessments)
  - [AI6 Assessments](#ai6-assessments)
  - [EU AI Act Assessments](#eu-ai-act-assessments)
  - [Compliance Checking](#compliance-checking)
  - [Validation Services](#validation-services)
  - [Framework Metadata](#framework-metadata)
- [Response Codes](#response-codes)
- [Error Handling](#error-handling)
- [Examples](#examples)
- [SDKs and Tools](#sdks-and-tools)

---

## Overview

The AI Risk Assurance API provides programmatic access to:

- ✅ **Risk Register Management** - CRUD operations for AI risk assessments
- 📊 **Framework Assessments** - FAIRA, VAISS, and NIST assessments
- 🔍 **Compliance Checking** - Multi-framework compliance verification
- ✓ **Schema Validation** - JSON Schema validation services
- 🗺️ **Framework Mappings** - Cross-framework requirement mappings

> **📖 New to this API?** Check out **[USE_CASES.md](./USE_CASES.md)** for practical scenarios including:
>
> - Automated risk assessment in CI/CD pipelines
> - Multi-project risk dashboards
> - Vendor assessment validation
> - Continuous compliance monitoring
> - ServiceNow, Power BI, and web app integration patterns

### Integrated Frameworks

- **FAIRA v1.0.0** - Queensland Government AI risk assessment
- **Microsoft AI Security v4.1.4** - AI security controls and threat assessment
- **NIST NF-COM-002** - AI Security Competency Area (46 competencies)
- **VAISS v1.0/v2.0** - Voluntary AI Safety Standard (10 guardrails, v2 enhancements)
- **NFAAIG 2024-2025** - National government AI assurance framework
- **AI6 Framework 2025** - Australia's 6 Essential AI Practices
- **EU AI Act 2024** - Regulation 2024/1689, risk classification
- **NIST AI RMF GenAI Profile** - NIST-AI-600-1, generative AI guidance
- **MAS AI Guidelines 2025** - Singapore financial sector AI risk management
- **OECD AI Principles 2024** - International AI principles (47 jurisdictions)
- **UK DSIT AI Framework** - UK cross-sectoral AI principles

---

## Authentication

All API endpoints require authentication using one of the following methods:

### API Key Authentication

Include the API key in the request header:

```http
GET /v2/risk-registers HTTP/1.1
Host: api.example.qld.gov.au
X-API-Key: your-api-key-here
```

**Python Example:**

```python
import requests

headers = {
    'X-API-Key': 'your-api-key-here',
    'Content-Type': 'application/json'
}

response = requests.get(
    'https://api.example.qld.gov.au/v2/risk-registers',
    headers=headers
)
```

### Bearer Token Authentication (OAuth 2.0)

Include the bearer token in the Authorization header:

```http
GET /v2/risk-registers HTTP/1.1
Host: api.example.qld.gov.au
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**JavaScript Example:**

```javascript
const response = await fetch('https://api.example.qld.gov.au/v2/risk-registers', {
  headers: {
    'Authorization': 'Bearer your-token-here',
    'Content-Type': 'application/json'
  }
});
```

---

## Rate Limiting

- **Limit**: 1000 requests per hour per API key
- **Headers Returned**:


  - `X-RateLimit-Limit`: Maximum requests per hour
  - `X-RateLimit-Remaining`: Remaining requests in current window
  - `X-RateLimit-Reset`: Unix timestamp when limit resets

**Response when limit exceeded:**

```json
{
  "code": "RATE_LIMIT_EXCEEDED",
  "message": "Rate limit of 1000 requests per hour exceeded",
  "details": {
    "retryAfter": 3600
  }
}
```

---

## Base URLs

| Environment | URL |
|-------------|-----|
| Production | `https://api.example.qld.gov.au/v2` |
| Staging | `https://api-staging.example.qld.gov.au/v2` |
| Development | `http://localhost:3000/v2` |

---

## Quick Start

### 1. Create a Risk Register

```bash
curl -X POST https://api.example.qld.gov.au/v2/risk-registers \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "metadata": {
      "version": "1.0.0",
      "assessmentId": "ASSESS-2025-001",
      "projectName": "AI Chatbot Assessment",
      "assessor": {
        "name": "Jane Smith",
        "role": "AI Risk Manager",
        "organisation": "QLD Government",
        "email": "jane.smith@qld.gov.au"
      }
    },
    "risks": []
  }'
```

### 2. Add a Risk

```bash
curl -X POST https://api.example.qld.gov.au/v2/risk-registers/ASSESS-2025-001/risks \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "riskId": "RISK-0001",
    "title": "Prompt Injection Vulnerability",
    "category": "Security",
    "severity": 4,
    "likelihood": 3,
    "status": "Identified"
  }'
```

### 3. Run Compliance Check

```bash
curl -X POST https://api.example.qld.gov.au/v2/compliance/check \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "assessmentId": "ASSESS-2025-001",
    "frameworks": ["FAIRA", "VAISS", "NIST"]
  }'
```

---

## Endpoints

### Risk Registers

#### List Risk Registers

```http
GET /v2/risk-registers
```

**Query Parameters:**


- `page` (integer, default: 1) - Page number
- `limit` (integer, default: 20, max: 100) - Results per page
- `projectName` (string) - Filter by project name
- `status` (string) - Filter by status (Identified, Assessed, etc.)

**Example Response:**

```json
{
  "data": [
    {
      "assessmentId": "ASSESS-2025-001",
      "projectName": "AI Chatbot Assessment",
      "createdDate": "2025-10-12",
      "lastUpdated": "2025-10-12T14:30:00Z",
      "totalRisks": 5,
      "highPriorityRisks": 2
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 1,
    "totalPages": 1
  }
}
```

#### Create Risk Register

```http
POST /v2/risk-registers
```

**Request Body:** Complete risk register object (see JSON schema)

**Response:** `201 Created` with created risk register

#### Get Risk Register

```http
GET /v2/risk-registers/{registerId}
```

**Path Parameters:**


- `registerId` (string, required) - Assessment ID

**Response:** `200 OK` with full risk register

#### Update Risk Register

```http
PUT /v2/risk-registers/{registerId}
```

**Request Body:** Updated risk register object

**Response:** `200 OK` with updated register

#### Delete Risk Register

```http
DELETE /v2/risk-registers/{registerId}
```

**Response:** `204 No Content`

#### Add Risk to Register

```http
POST /v2/risk-registers/{registerId}/risks
```

**Request Body:**

```json
{
  "riskId": "RISK-0001",
  "title": "AI Hallucination Risk",
  "description": "Model may generate false information",
  "category": "Technical",
  "severity": 4,
  "likelihood": 3,
  "riskScore": 12,
  "status": "Identified"
}
```

**Response:** `201 Created` with risk object

#### Update Risk

```http
PUT /v2/risk-registers/{registerId}/risks/{riskId}
```

**Path Parameters:**


- `registerId` (string, required)
- `riskId` (string, required, pattern: `RISK-\d{4}`)

**Request Body:** Updated risk object

**Response:** `200 OK` with updated risk

---

### FAIRA Assessments

#### List FAIRA Assessments

```http
GET /v2/faira-assessments
```

**Query Parameters:**


- `page` (integer)
- `limit` (integer)

**Example Response:**

```json
{
  "data": [
    {
      "assessmentId": "FAIRA-2025-001",
      "projectName": "AI Decision Support System",
      "organisation": "Department of Health",
      "createdDate": "2025-10-10"
    }
  ],
  "pagination": {...}
}
```

#### Create FAIRA Assessment

```http
POST /v2/faira-assessments
```

**Request Body:** Complete FAIRA assessment (Parts A, B, C)

**Response:** `201 Created`

#### Get FAIRA Assessment

```http
GET /v2/faira-assessments/{assessmentId}
```

**Response:** `200 OK` with full FAIRA assessment including all parts

---

### VAISS Assessments

#### List VAISS Assessments

```http
GET /v2/vaiss-assessments
```

**Response:** Paginated list of VAISS guardrail assessments

#### Create VAISS Assessment

```http
POST /v2/vaiss-assessments
```

**Request Body:**

```json
{
  "metadata": {
    "version": "1.0",
    "assessmentDate": "2025-10-12",
    "organisation": "QLD Department",
    "aiSystemName": "Risk Assessment AI"
  },
  "guardrailAssessments": [
    {
      "guardrailNumber": 1,
      "guardrailName": "Accountability and Governance",
      "implementationStatus": "Largely Implemented"
    }
  ]
}
```

**Response:** `201 Created` with VAISS assessment

---

### Compliance Checking

#### Run Compliance Check

```http
POST /v2/compliance/check
```

**Request Body:**

```json
{
  "assessmentId": "ASSESS-2025-001",
  "frameworks": ["FAIRA", "Microsoft", "NIST", "VAISS"]
}
```

**Response:**

```json
{
  "assessmentId": "ASSESS-2025-001",
  "frameworks": [
    {
      "framework": "FAIRA",
      "compliant": true,
      "compliancePercentage": 95.5,
      "gaps": ["Part C controls need additional documentation"]
    },
    {
      "framework": "VAISS",
      "compliant": false,
      "compliancePercentage": 72.0,
      "gaps": [
        "Guardrail 5: Human Oversight - Partially Implemented",
        "Guardrail 8: Supply Chain - Not Implemented"
      ]
    }
  ],
  "generatedAt": "2025-10-12T15:00:00Z"
}
```

#### Identify Compliance Gaps

```http
POST /v2/compliance/gaps
```

**Request Body:**

```json
{
  "assessmentId": "ASSESS-2025-001",
  "targetFramework": "VAISS"
}
```

**Response:**

```json
{
  "assessmentId": "ASSESS-2025-001",
  "targetFramework": "VAISS",
  "gaps": [
    {
      "requirement": "Guardrail 5: Human Oversight",
      "severity": "High",
      "recommendation": "Implement human-in-the-loop decision review process"
    }
  ],
  "coveragePercentage": 72.0
}
```

---

### Validation Services

#### Validate Risk Register

```http
POST /v2/validate/risk-register
```

**Request Body:** Risk register JSON to validate

**Response:**

```json
{
  "valid": true,
  "errors": []
}
```

Or if invalid:

```json
{
  "valid": false,
  "errors": [
    {
      "field": "metadata.assessmentId",
      "message": "is required",
      "code": "REQUIRED_FIELD"
    },
    {
      "field": "risks[0].severity",
      "message": "must be <= 5",
      "code": "RANGE_ERROR"
    }
  ]
}
```

#### Validate FAIRA Assessment

```http
POST /v2/validate/faira-assessment
```

**Request Body:** FAIRA assessment JSON

**Response:** Validation result (same format as above)

---

### Framework Metadata

#### List Frameworks

```http
GET /v2/frameworks
```

**Response:**

```json
[
  {
    "id": "faira",
    "name": "FAIRA Framework",
    "version": "1.0.0",
    "description": "Queensland Government AI risk assessment",
    "publisher": "Queensland Government",
    "releaseDate": "2024-01-01"
  },
  {
    "id": "vaiss",
    "name": "Voluntary AI Safety Standard",
    "version": "1.0",
    "description": "Australian AI safety guardrails",
    "publisher": "National AI Centre",
    "releaseDate": "2024-09-05"
  }
]
```

#### Get Framework Mappings

```http
GET /v2/frameworks/{frameworkId}/mappings?targetFramework=vaiss
```

**Path Parameters:**


- `frameworkId` (string) - Source framework (faira, microsoft, nist, vaiss, nfaaig, iso42001)

**Query Parameters:**

- `targetFramework` (string) - Target framework for mapping

**Example Response:**

```json
{
  "sourceFramework": "faira",
  "targetFramework": "vaiss",
  "mappings": [
    {
      "sourceRequirement": "Part A: Components Analysis",
      "targetRequirements": [
        "Guardrail 1: Accountability and Governance",
        "Guardrail 3: Data Governance"
      ],
      "alignmentStrength": "Partial"
    }
  ]
}
```

---

## Response Codes

| Code | Description |
|------|-------------|
| `200` | Success |
| `201` | Created successfully |
| `204` | No content (successful deletion) |
| `400` | Bad request (invalid parameters) |
| `401` | Unauthorized (invalid/missing API key) |
| `404` | Resource not found |
| `422` | Validation error (invalid schema) |
| `429` | Rate limit exceeded |
| `500` | Internal server error |

---

## Error Handling

All error responses follow this format:

```json
{
  "code": "ERROR_CODE",
  "message": "Human-readable error message",
  "details": {
    "field": "specific field with error",
    "constraint": "violated constraint"
  }
}
```

### Common Error Codes

- `INVALID_REQUEST` - Malformed request body
- `VALIDATION_ERROR` - Schema validation failed
- `NOT_FOUND` - Resource doesn't exist
- `UNAUTHORIZED` - Authentication failed
- `RATE_LIMIT_EXCEEDED` - Too many requests
- `CONFLICT` - Resource already exists

---

## Examples

### Complete Risk Assessment Workflow

#### 1. Create Risk Register

```python
import requests

api_key = "your-api-key"
base_url = "https://api.example.qld.gov.au/v2"
headers = {"X-API-Key": api_key, "Content-Type": "application/json"}

# Create register
register = {
    "metadata": {
        "version": "1.0.0",
        "assessmentId": "ASSESS-2025-005",
        "projectName": "AI Recruitment System",
        "assessor": {
            "name": "John Doe",
            "role": "Risk Analyst",
            "organisation": "HR Department",
            "email": "john.doe@qld.gov.au"
        },
        "frameworksApplied": ["FAIRA v1.0.0", "VAISS v1.0"]
    },
    "risks": []
}

response = requests.post(f"{base_url}/risk-registers", json=register, headers=headers)
print(f"Created: {response.status_code}")
```

#### 2. Add Multiple Risks

```python
risks = [
    {
        "riskId": "RISK-0001",
        "title": "Algorithmic Bias in Candidate Screening",
        "category": "Bias",
        "severity": 5,
        "likelihood": 4,
        "aiEthicsPrinciples": ["Fairness"]
    },
    {
        "riskId": "RISK-0002",
        "title": "Privacy Breach - Candidate Data",
        "category": "Privacy",
        "severity": 4,
        "likelihood": 2,
        "aiEthicsPrinciples": ["Privacy Protection and Security"]
    }
]

for risk in risks:
    response = requests.post(
        f"{base_url}/risk-registers/ASSESS-2025-005/risks",
        json=risk,
        headers=headers
    )
    print(f"Added {risk['riskId']}: {response.status_code}")
```

#### 3. Run Compliance Check

```python
compliance_request = {
    "assessmentId": "ASSESS-2025-005",
    "frameworks": ["FAIRA", "VAISS"]
}

response = requests.post(
    f"{base_url}/compliance/check",
    json=compliance_request,
    headers=headers
)

report = response.json()
print(f"Compliance Score: {report['frameworks'][0]['compliancePercentage']}%")
```

### TypeScript/Node.js Example

```typescript
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'https://api.example.qld.gov.au/v2',
  headers: {
    'X-API-Key': process.env.API_KEY,
    'Content-Type': 'application/json'
  }
});

async function validateRiskRegister(data: any) {
  try {
    const response = await apiClient.post('/validate/risk-register', data);

    if (response.data.valid) {
      console.log('✅ Risk register is valid');
      return true;
    } else {
      console.error('❌ Validation errors:', response.data.errors);
      return false;
    }
  } catch (error) {
    console.error('API error:', error);
    return false;
  }
}

// Usage
const myRiskRegister = {...};
await validateRiskRegister(myRiskRegister);
```

---

## SDKs and Tools

### Official Tools

- **Python Validation Tool** - `validate_schemas.py` in `/tools`
- **JavaScript Validator** - `validate-schemas.js` in `/tools`
- **Compliance Checker** - `faira-check.py` in `/tools`

### Usage with Local Tools

The local validation tools can validate data before sending to the API:

```bash
# Validate before submitting
python tools/validate_schemas.py my-risk-register.json --schema risk-register

# If valid, submit to API
curl -X POST https://api.example.qld.gov.au/v2/risk-registers \
  -H "X-API-Key: $API_KEY" \
  -d @my-risk-register.json
```

---

## Additional Resources

- **Real-World Use Cases**: [USE_CASES.md](./USE_CASES.md) - Practical integration examples
- **OpenAPI Spec**: [openapi.yaml](./openapi.yaml)
- **JSON Schemas**: [/schemas](../schemas/)
- **YAML Mappings**: [/mappings](../mappings/)
- **Developer Guide**: [/docs/DEVELOPER_GUIDE.md](../docs/DEVELOPER_GUIDE.md)
- **Examples**: [/examples](../examples/)

---

## Support

For API issues or questions:
- **Repository**: [GitHub Issues](https://github.com/OAK-AI-Public/ai-risk-assurance-faira-microsoft/issues)
- **Documentation**: [Main README](../README.md)

---

**API Version**: 2.0.0
**Last Updated**: October 2025
**Maintained by**: [OAK AI](https://github.com/OAK-AI-Public)
