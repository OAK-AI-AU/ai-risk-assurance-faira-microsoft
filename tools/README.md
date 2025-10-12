# AI Risk Assurance Framework - Tools

Validation and compliance checking tools for the Unified AI Risk Assurance Framework.

## 📦 Available Tools

### 1. Schema Validators

Validate JSON files against framework schemas:

- **`validate_schemas.py`** - Python validation tool
- **`validate-schemas.js`** - Node.js validation tool

Both tools provide identical functionality with platform-specific implementations.

### 2. Compliance Checker (Coming Soon)

CLI tool for cross-framework compliance checking and gap analysis.

---

## 🚀 Quick Start

### Python Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Make script executable (Linux/macOS)
chmod +x validate_schemas.py

# Validate a file
python validate_schemas.py ../examples/sample-risk-register.json

# Or if executable:
./validate_schemas.py ../examples/sample-risk-register.json
```

### Node.js Setup

```bash
# Install dependencies
npm install

# Validate a file
node validate-schemas.js ../examples/sample-risk-register.json
```

---

## 📖 Usage Guide

### Schema Validation

Both validators support automatic schema detection or explicit schema specification.

#### Auto-detect Schema Type

```bash
# Python
python validate_schemas.py my-risk-register.json

# Node.js
node validate-schemas.js my-risk-register.json
```

#### Specify Schema Type

```bash
# Python
python validate_schemas.py my-assessment.json --schema faira

# Node.js
node validate-schemas.js my-assessment.json --schema faira
```

#### Available Schema Types

- `risk-register` - AI risk assessment register
- `faira` - FAIRA framework assessment
- `vaiss` - VAISS guardrail assessment
- `nist-competencies` - NIST AI Security competencies
- `control-catalog` - Control catalog
- `compliance-mapping` - Cross-framework mappings

#### Validate All Examples

```bash
# Python
python validate_schemas.py --all

# Node.js
node validate-schemas.js --all
# Or using npm script:
npm test
```

#### List Available Schemas

```bash
# Python
python validate_schemas.py --list-schemas

# Node.js
node validate-schemas.js --list-schemas
```

#### Verbose Output

```bash
# Python
python validate_schemas.py my-file.json --verbose

# Node.js
node validate-schemas.js my-file.json --verbose
```

---

## 🔧 Integration Examples

### Git Pre-commit Hook

Add to `.git/hooks/pre-commit`:

```bash
#!/bin/bash
# Validate all JSON files before commit

echo "Validating JSON files..."
python tools/validate_schemas.py --all

if [ $? -ne 0 ]; then
    echo "❌ Validation failed. Please fix errors before committing."
    exit 1
fi

echo "✅ All validations passed"
```

### CI/CD Pipeline (GitHub Actions)

```yaml
# .github/workflows/validate.yml
name: Validate Schemas

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install Python dependencies
        run: |
          cd tools
          pip install -r requirements.txt

      - name: Validate all examples
        run: python tools/validate_schemas.py --all
```

### Node.js CI/CD

```yaml
# .github/workflows/validate-node.yml
name: Validate Schemas (Node.js)

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: |
          cd tools
          npm install

      - name: Validate all examples
        run: npm test
```

### Python Script Integration

```python
import sys
sys.path.append('tools')

from validate_schemas import validate_file

# Validate a risk register
is_valid = validate_file('my-risks.json', schema_type='risk-register')

if not is_valid:
    print("Validation failed!")
    sys.exit(1)
```

### Node.js Module Integration

```javascript
const { validateFile } = require('./tools/validate-schemas');

// Validate a risk register
const isValid = validateFile('my-risks.json', 'risk-register');

if (!isValid) {
  console.error('Validation failed!');
  process.exit(1);
}
```

---

## 📋 Validation Output

### Successful Validation

```
✅ VALID: ../examples/sample-risk-register.json
```

### Failed Validation

```
❌ INVALID: my-risk-register.json
Schema: risk-register
Errors:
  • metadata.assessmentId: is required
  • risks[0].severity: must be <= 5
  • risks[1].category: must be equal to one of the allowed values
```

### Summary Report (--all flag)

```
Validating 3 example file(s)...

✅ VALID: examples/sample-risk-register.json

❌ INVALID: examples/test-faira.json
Schema: faira
Errors:
  • partA.solutionOverview.name: is required

✅ VALID: examples/sample-vaiss-assessment.json

============================================================
Validation Summary:
  ✅ Passed: 2
  ❌ Failed: 1
============================================================
```

---

## 🐛 Troubleshooting

### Python Issues

**Problem**: `ModuleNotFoundError: No module named 'jsonschema'`

**Solution**:
```bash
pip install -r requirements.txt
```

**Problem**: Script not executable on Linux/macOS

**Solution**:
```bash
chmod +x validate_schemas.py
```

### Node.js Issues

**Problem**: `Cannot find module 'ajv'`

**Solution**:
```bash
cd tools
npm install
```

**Problem**: `SyntaxError: Unexpected token`

**Solution**: Ensure Node.js version >= 14:
```bash
node --version
# If < 14, update Node.js
```

### General Issues

**Problem**: Schema file not found

**Solution**: Ensure you're running the tool from the correct directory. The validator expects:
```
repository-root/
  ├── tools/           (you are here)
  ├── schemas/         (schemas must exist)
  └── examples/        (for --all validation)
```

**Problem**: JSON syntax errors

**Solution**: Use a JSON validator (like [jsonlint.com](https://jsonlint.com)) to check your JSON file syntax before schema validation.

---

## 🔍 Schema Detection Logic

The validators attempt to auto-detect schema types based on file structure:

| Schema Type | Detection Criteria |
|-------------|-------------------|
| `risk-register` | Has `risks` and `metadata.assessmentId` |
| `faira` | Has `partA`, `partB`, and `partC` |
| `vaiss` | Has `guardrailAssessments` |
| `nist-competencies` | Has `competencyArea` and `competencies` |
| `control-catalog` | Has `controls` and `metadata.controlCatalogId` |
| `compliance-mapping` | Has `mappings` and `sourceFramework` |

If detection fails, specify the schema type explicitly with `--schema`.

---

## 📚 Related Documentation

- [Developer Guide](../docs/DEVELOPER_GUIDE.md) - Comprehensive developer documentation
- [JSON Schemas](../schemas/) - All available schemas
- [Examples](../examples/) - Sample files for each schema type
- [API Documentation](../api/) - OpenAPI specification

---

## 🤝 Contributing

To add new validation tools:

1. Follow the existing code structure
2. Add error handling for common issues
3. Include helpful error messages
4. Update this README
5. Add tests/examples

---

## 📄 License

MIT License - see [LICENSE](../LICENSE) for details

---

**Maintained by**: [OAK AI](https://github.com/OAK-AI-Public)
**Repository**: [ai-risk-assurance-faira-microsoft](https://github.com/OAK-AI-Public/ai-risk-assurance-faira-microsoft)
