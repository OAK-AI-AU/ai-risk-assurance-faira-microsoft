#!/usr/bin/env node

/**
 * AI Risk Assurance Framework - Schema Validator (Node.js)
 *
 * Validates JSON files against the framework's JSON schemas.
 * Supports risk registers, FAIRA assessments, VAISS assessments, and more.
 *
 * Usage:
 *   node validate-schemas.js <json-file> [--schema <schema-type>]
 *   node validate-schemas.js --all
 *   node validate-schemas.js --help
 *
 * Examples:
 *   node validate-schemas.js ../examples/sample-risk-register.json
 *   node validate-schemas.js my-faira-assessment.json --schema faira
 *   node validate-schemas.js --all
 */

const fs = require('fs');
const path = require('path');

// Try to load Ajv, provide helpful error if not installed
let Ajv;
try {
  Ajv = require('ajv');
} catch (e) {
  console.error('❌ Error: ajv library not installed');
  console.error('Install with: npm install ajv ajv-formats');
  process.exit(1);
}

let addFormats;
try {
  addFormats = require('ajv-formats');
} catch (e) {
  console.error('❌ Error: ajv-formats library not installed');
  console.error('Install with: npm install ajv ajv-formats');
  process.exit(1);
}

// Schema type mappings
const SCHEMA_TYPES = {
  'risk-register': 'risk-register.schema.json',
  'faira': 'faira-assessment.schema.json',
  'control-catalog': 'control-catalog.schema.json',
  'nist-competencies': 'nist-ai-competencies.schema.json',
  'vaiss': 'vaiss-guardrails.schema.json',
  'compliance-mapping': 'compliance-mapping.schema.json',
};

// ANSI color codes
const colors = {
  green: '\x1b[92m',
  red: '\x1b[91m',
  yellow: '\x1b[93m',
  blue: '\x1b[94m',
  bold: '\x1b[1m',
  reset: '\x1b[0m'
};

/**
 * Get the path to the schemas directory
 */
function getSchemaPath() {
  // Assuming script is in /tools, schemas are in /schemas
  const scriptDir = __dirname;
  const repoRoot = path.dirname(scriptDir);
  return path.join(repoRoot, 'schemas');
}

/**
 * Load a JSON schema file
 */
function loadSchema(schemaFile) {
  const schemaPath = path.join(getSchemaPath(), schemaFile);

  if (!fs.existsSync(schemaPath)) {
    throw new Error(`Schema file not found: ${schemaPath}`);
  }

  const content = fs.readFileSync(schemaPath, 'utf8');
  return JSON.parse(content);
}

/**
 * Load a JSON file for validation
 */
function loadJsonFile(filePath) {
  if (!fs.existsSync(filePath)) {
    throw new Error(`JSON file not found: ${filePath}`);
  }

  const content = fs.readFileSync(filePath, 'utf8');
  return JSON.parse(content);
}

/**
 * Attempt to detect the schema type from the JSON data structure
 */
function detectSchemaType(data) {
  // Check for risk register
  if (data.risks && data.metadata && data.metadata.assessmentId) {
    return 'risk-register';
  }

  // Check for FAIRA assessment
  if (data.partA && data.partB && data.partC) {
    return 'faira';
  }

  // Check for VAISS assessment
  if (data.guardrailAssessments) {
    return 'vaiss';
  }

  // Check for NIST competencies
  if (data.competencyArea && data.competencies) {
    return 'nist-competencies';
  }

  // Check for control catalog
  if (data.controls && data.metadata && data.metadata.controlCatalogId) {
    return 'control-catalog';
  }

  // Check for compliance mapping
  if (data.mappings && data.sourceFramework) {
    return 'compliance-mapping';
  }

  return null;
}

/**
 * Validate JSON data against a schema
 *
 * @returns {Object} { valid: boolean, errors: Array }
 */
function validateJson(data, schema) {
  const ajv = new Ajv({ allErrors: true, verbose: true });
  addFormats(ajv);

  const validate = ajv.compile(schema);
  const valid = validate(data);

  if (!valid) {
    const errors = validate.errors.map(error => {
      const path = error.instancePath || 'root';
      return `  • ${path}: ${error.message}`;
    });
    return { valid: false, errors };
  }

  return { valid: true, errors: [] };
}

/**
 * Validate a single JSON file
 *
 * @returns {boolean} True if validation succeeded
 */
function validateFile(filePath, schemaType = null, verbose = false) {
  try {
    // Load JSON file
    if (verbose) {
      console.log(`${colors.blue}📄 Loading: ${filePath}${colors.reset}`);
    }

    const data = loadJsonFile(filePath);

    // Detect or use provided schema type
    if (!schemaType) {
      schemaType = detectSchemaType(data);
      if (!schemaType) {
        console.log(`${colors.yellow}⚠️  Could not detect schema type for ${filePath}${colors.reset}`);
        console.log('   Please specify schema type with --schema option');
        return false;
      }
      if (verbose) {
        console.log(`${colors.blue}🔍 Detected schema type: ${schemaType}${colors.reset}`);
      }
    }

    // Validate schema type
    if (!SCHEMA_TYPES[schemaType]) {
      console.log(`${colors.red}❌ Invalid schema type: ${schemaType}${colors.reset}`);
      console.log(`   Valid types: ${Object.keys(SCHEMA_TYPES).join(', ')}`);
      return false;
    }

    // Load schema
    const schemaFile = SCHEMA_TYPES[schemaType];
    if (verbose) {
      console.log(`${colors.blue}📋 Loading schema: ${schemaFile}${colors.reset}`);
    }

    const schema = loadSchema(schemaFile);

    // Validate
    if (verbose) {
      console.log(`${colors.blue}✓ Validating...${colors.reset}`);
    }

    const result = validateJson(data, schema);

    // Report results
    if (result.valid) {
      console.log(`${colors.green}✅ VALID: ${filePath}${colors.reset}`);
      if (verbose) {
        console.log(`   Schema: ${schemaType}`);
      }
      return true;
    } else {
      console.log(`${colors.red}❌ INVALID: ${filePath}${colors.reset}`);
      console.log(`${colors.red}Schema: ${schemaType}${colors.reset}`);
      console.log(`${colors.red}Errors:${colors.reset}`);
      result.errors.forEach(error => {
        console.log(`${colors.red}${error}${colors.reset}`);
      });
      return false;
    }
  } catch (error) {
    if (error.message.includes('not found')) {
      console.log(`${colors.red}❌ File not found: ${error.message}${colors.reset}`);
    } else if (error instanceof SyntaxError) {
      console.log(`${colors.red}❌ Invalid JSON in ${filePath}: ${error.message}${colors.reset}`);
    } else {
      console.log(`${colors.red}❌ Error validating ${filePath}: ${error.message}${colors.reset}`);
    }
    return false;
  }
}

/**
 * Validate all example files in the examples directory
 *
 * @returns {number} Number of failed validations
 */
function validateAllExamples(verbose = false) {
  const scriptDir = __dirname;
  const repoRoot = path.dirname(scriptDir);
  const examplesDir = path.join(repoRoot, 'examples');

  if (!fs.existsSync(examplesDir)) {
    console.log(`${colors.yellow}⚠️  Examples directory not found: ${examplesDir}${colors.reset}`);
    return 0;
  }

  // Find all JSON files recursively
  function findJsonFiles(dir) {
    const files = [];
    const items = fs.readdirSync(dir);

    items.forEach(item => {
      const fullPath = path.join(dir, item);
      const stat = fs.statSync(fullPath);

      if (stat.isDirectory()) {
        files.push(...findJsonFiles(fullPath));
      } else if (item.endsWith('.json')) {
        files.push(fullPath);
      }
    });

    return files;
  }

  const jsonFiles = findJsonFiles(examplesDir);

  if (jsonFiles.length === 0) {
    console.log(`${colors.yellow}⚠️  No JSON files found in ${examplesDir}${colors.reset}`);
    return 0;
  }

  console.log(`${colors.bold}Validating ${jsonFiles.length} example file(s)...${colors.reset}\n`);

  let failures = 0;
  jsonFiles.forEach(jsonFile => {
    if (!validateFile(jsonFile, null, verbose)) {
      failures++;
    }
    console.log(); // Blank line between files
  });

  // Summary
  const successes = jsonFiles.length - failures;
  console.log(`${colors.bold}${'='.repeat(60)}${colors.reset}`);
  console.log(`${colors.bold}Validation Summary:${colors.reset}`);
  console.log(`  ${colors.green}✅ Passed: ${successes}${colors.reset}`);
  console.log(`  ${colors.red}❌ Failed: ${failures}${colors.reset}`);
  console.log(`${colors.bold}${'='.repeat(60)}${colors.reset}`);

  return failures;
}

/**
 * Display help message
 */
function showHelp() {
  console.log(`
AI Risk Assurance Framework - Schema Validator (Node.js)

Usage:
  node validate-schemas.js <json-file> [--schema <schema-type>]
  node validate-schemas.js --all
  node validate-schemas.js --help

Options:
  --schema <type>    Specify schema type (auto-detected if not specified)
  --all              Validate all example files
  --verbose, -v      Verbose output
  --list-schemas     List available schema types
  --help, -h         Show this help message

Examples:
  # Validate a risk register (auto-detect schema)
  node validate-schemas.js ../examples/sample-risk-register.json

  # Validate with explicit schema type
  node validate-schemas.js my-assessment.json --schema faira

  # Validate all example files
  node validate-schemas.js --all

  # Verbose output
  node validate-schemas.js my-file.json --verbose

Available schema types:
  - risk-register      Risk assessment register
  - faira              FAIRA framework assessment
  - vaiss              VAISS guardrail assessment
  - nist-competencies  NIST AI Security competencies
  - control-catalog    Control catalog
  - compliance-mapping Cross-framework compliance mapping
`);
}

/**
 * List available schemas
 */
function listSchemas() {
  console.log(`${colors.bold}Available Schema Types:${colors.reset}`);
  Object.entries(SCHEMA_TYPES).forEach(([type, file]) => {
    console.log(`  • ${type.padEnd(20)} → ${file}`);
  });
}

/**
 * Main function
 */
function main() {
  const args = process.argv.slice(2);

  // Parse arguments
  const options = {
    file: null,
    schema: null,
    all: false,
    verbose: false,
    listSchemas: false,
    help: false
  };

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];

    if (arg === '--help' || arg === '-h') {
      options.help = true;
    } else if (arg === '--all') {
      options.all = true;
    } else if (arg === '--verbose' || arg === '-v') {
      options.verbose = true;
    } else if (arg === '--list-schemas') {
      options.listSchemas = true;
    } else if (arg === '--schema') {
      options.schema = args[++i];
    } else if (!arg.startsWith('--')) {
      options.file = arg;
    }
  }

  // Handle options
  if (options.help) {
    showHelp();
    process.exit(0);
  }

  if (options.listSchemas) {
    listSchemas();
    process.exit(0);
  }

  if (options.all) {
    const failures = validateAllExamples(options.verbose);
    process.exit(failures > 0 ? 1 : 0);
  }

  if (options.file) {
    const success = validateFile(options.file, options.schema, options.verbose);
    process.exit(success ? 0 : 1);
  }

  // No file specified
  showHelp();
  process.exit(1);
}

// Run if called directly
if (require.main === module) {
  main();
}

module.exports = {
  validateFile,
  validateAllExamples,
  detectSchemaType,
  loadSchema,
  loadJsonFile
};
