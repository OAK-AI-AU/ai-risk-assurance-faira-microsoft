# Examples

This directory contains practical examples demonstrating how to use the machine-readable formats in this repository.

## Available Examples

### 1. sample-risk-register.json

A complete example of an AI risk register for a customer service chatbot project, demonstrating:

- **3 comprehensive risk entries** covering Security, Technical, and Bias categories
- Integration of multiple frameworks (FAIRA, Microsoft, NIST, VAISS)
- Proper use of risk scoring and severity levels
- Control mapping and mitigation planning
- Risk owner assignment and review tracking

**Use this example to:**
- Understand the risk register structure
- Validate your own risk data against the schema
- Learn how to map risks to NIST competencies and VAISS guardrails
- See how to document controls and residual risk

### Validating the Example

**Python:**
```bash
pip install jsonschema
python -c "
import json
import jsonschema

schema = json.load(open('../schemas/risk-register.schema.json'))
data = json.load(open('sample-risk-register.json'))
jsonschema.validate(instance=data, schema=schema)
print('✅ Example is valid!')
"
```

**Node.js:**
```bash
npm install ajv
node -e "
const Ajv = require('ajv');
const fs = require('fs');
const ajv = new Ajv();

const schema = JSON.parse(fs.readFileSync('../schemas/risk-register.schema.json'));
const data = JSON.parse(fs.readFileSync('sample-risk-register.json'));

const validate = ajv.compile(schema);
if (validate(data)) {
  console.log('✅ Example is valid!');
} else {
  console.log('❌ Validation errors:', validate.errors);
}
"
```

## Creating Your Own Risk Register

1. **Copy the sample** as a starting point:
   ```bash
   cp examples/sample-risk-register.json my-project-risks.json
   ```

2. **Update metadata** with your project details:
   - `assessmentId`: Your unique identifier
   - `projectName`: Your AI system name
   - `assessor`: Your details
   - `frameworksApplied`: Frameworks you're using

3. **Modify or add risks** following the structure:
   ```json
   {
     "riskId": "RISK-####",
     "title": "Brief risk title",
     "category": "Choose from: Technical, Security, Ethical, etc.",
     "severity": 1-5,
     "likelihood": 1-5,
     ...
   }
   ```

4. **Validate** your risk register:
   ```bash
   python validate_schema.py ../schemas/risk-register.schema.json my-project-risks.json
   ```

## Next Steps

- Read the [Developer Guide](../docs/DEVELOPER_GUIDE.md) for comprehensive usage instructions
- Explore other schemas in `/schemas/` directory
- Check YAML mappings in `/mappings/` for cross-framework alignment

## Need Help?

- Review the [JSON Schema documentation](https://json-schema.org/)
- Check the main [README](../README.md) for framework details
- Open an [issue](https://github.com/OAK-AI-Public/ai-risk-assurance-faira-microsoft/issues) for questions
