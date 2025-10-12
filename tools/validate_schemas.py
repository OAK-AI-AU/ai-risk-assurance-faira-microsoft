#!/usr/bin/env python3
"""
AI Risk Assurance Framework - Schema Validator

Validates JSON files against the framework's JSON schemas.
Supports risk registers, FAIRA assessments, VAISS assessments, and more.

Usage:
    python validate_schemas.py <json-file> [--schema <schema-type>]
    python validate_schemas.py --all
    python validate_schemas.py --help

Examples:
    python validate_schemas.py ../examples/sample-risk-register.json
    python validate_schemas.py my-faira-assessment.json --schema faira
    python validate_schemas.py --all
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    import jsonschema
    from jsonschema import Draft202012Validator, ValidationError
except ImportError:
    print("❌ Error: jsonschema library not installed")
    print("Install with: pip install jsonschema")
    sys.exit(1)

# Schema type mappings
SCHEMA_TYPES = {
    "risk-register": "risk-register.schema.json",
    "faira": "faira-assessment.schema.json",
    "control-catalog": "control-catalog.schema.json",
    "nist-competencies": "nist-ai-competencies.schema.json",
    "vaiss": "vaiss-guardrails.schema.json",
    "compliance-mapping": "compliance-mapping.schema.json",
}

class Colors:
    """ANSI color codes for terminal output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def get_schema_path() -> Path:
    """Get the path to the schemas directory"""
    # Assuming script is in /tools, schemas are in /schemas
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    return repo_root / "schemas"

def load_schema(schema_file: str) -> Dict:
    """Load a JSON schema file"""
    schema_path = get_schema_path() / schema_file

    if not schema_path.exists():
        raise FileNotFoundError(f"Schema file not found: {schema_path}")

    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_json_file(file_path: str) -> Dict:
    """Load a JSON file for validation"""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"JSON file not found: {file_path}")

    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def detect_schema_type(data: Dict) -> Optional[str]:
    """
    Attempt to detect the schema type from the JSON data structure
    """
    # Check for risk register
    if "risks" in data and "metadata" in data:
        if "assessmentId" in data.get("metadata", {}):
            return "risk-register"

    # Check for FAIRA assessment
    if all(key in data for key in ["partA", "partB", "partC"]):
        return "faira"

    # Check for VAISS assessment
    if "guardrailAssessments" in data:
        return "vaiss"

    # Check for NIST competencies
    if "competencyArea" in data and "competencies" in data:
        return "nist-competencies"

    # Check for control catalog
    if "controls" in data and "metadata" in data:
        if "version" in data.get("metadata", {}) and "controlCatalogId" in data.get("metadata", {}):
            return "control-catalog"

    # Check for compliance mapping
    if "mappings" in data and "sourceFramework" in data:
        return "compliance-mapping"

    return None

def validate_json(data: Dict, schema: Dict, file_path: str) -> Tuple[bool, List[str]]:
    """
    Validate JSON data against a schema

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    try:
        # Use Draft 2020-12 validator
        validator = Draft202012Validator(schema)

        # Validate
        validation_errors = sorted(validator.iter_errors(data), key=lambda e: e.path)

        if validation_errors:
            for error in validation_errors:
                path = ".".join(str(p) for p in error.absolute_path) if error.absolute_path else "root"
                errors.append(f"  • {path}: {error.message}")
            return False, errors

        return True, []

    except Exception as e:
        errors.append(f"  • Validation error: {str(e)}")
        return False, errors

def validate_file(file_path: str, schema_type: Optional[str] = None, verbose: bool = False) -> bool:
    """
    Validate a single JSON file

    Returns:
        True if validation succeeded, False otherwise
    """
    try:
        # Load JSON file
        if verbose:
            print(f"{Colors.BLUE}📄 Loading: {file_path}{Colors.END}")

        data = load_json_file(file_path)

        # Detect or use provided schema type
        if schema_type is None:
            schema_type = detect_schema_type(data)
            if schema_type is None:
                print(f"{Colors.YELLOW}⚠️  Could not detect schema type for {file_path}{Colors.END}")
                print("   Please specify schema type with --schema option")
                return False
            if verbose:
                print(f"{Colors.BLUE}🔍 Detected schema type: {schema_type}{Colors.END}")

        # Validate schema type
        if schema_type not in SCHEMA_TYPES:
            print(f"{Colors.RED}❌ Invalid schema type: {schema_type}{Colors.END}")
            print(f"   Valid types: {', '.join(SCHEMA_TYPES.keys())}")
            return False

        # Load schema
        schema_file = SCHEMA_TYPES[schema_type]
        if verbose:
            print(f"{Colors.BLUE}📋 Loading schema: {schema_file}{Colors.END}")

        schema = load_schema(schema_file)

        # Validate
        if verbose:
            print(f"{Colors.BLUE}✓ Validating...{Colors.END}")

        is_valid, errors = validate_json(data, schema, file_path)

        # Report results
        if is_valid:
            print(f"{Colors.GREEN}✅ VALID: {file_path}{Colors.END}")
            if verbose:
                print(f"   Schema: {schema_type}")
            return True
        else:
            print(f"{Colors.RED}❌ INVALID: {file_path}{Colors.END}")
            print(f"{Colors.RED}Schema: {schema_type}{Colors.END}")
            print(f"{Colors.RED}Errors:{Colors.END}")
            for error in errors:
                print(f"{Colors.RED}{error}{Colors.END}")
            return False

    except FileNotFoundError as e:
        print(f"{Colors.RED}❌ File not found: {e}{Colors.END}")
        return False
    except json.JSONDecodeError as e:
        print(f"{Colors.RED}❌ Invalid JSON in {file_path}: {e}{Colors.END}")
        return False
    except Exception as e:
        print(f"{Colors.RED}❌ Error validating {file_path}: {e}{Colors.END}")
        return False

def validate_all_examples(verbose: bool = False) -> int:
    """
    Validate all example files in the examples directory

    Returns:
        Number of failed validations
    """
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    examples_dir = repo_root / "examples"

    if not examples_dir.exists():
        print(f"{Colors.YELLOW}⚠️  Examples directory not found: {examples_dir}{Colors.END}")
        return 0

    # Find all JSON files
    json_files = list(examples_dir.glob("**/*.json"))

    if not json_files:
        print(f"{Colors.YELLOW}⚠️  No JSON files found in {examples_dir}{Colors.END}")
        return 0

    print(f"{Colors.BOLD}Validating {len(json_files)} example file(s)...{Colors.END}\n")

    failures = 0
    for json_file in json_files:
        if not validate_file(str(json_file), verbose=verbose):
            failures += 1
        print()  # Blank line between files

    # Summary
    successes = len(json_files) - failures
    print(f"{Colors.BOLD}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}Validation Summary:{Colors.END}")
    print(f"  {Colors.GREEN}✅ Passed: {successes}{Colors.END}")
    print(f"  {Colors.RED}❌ Failed: {failures}{Colors.END}")
    print(f"{Colors.BOLD}{'='*60}{Colors.END}")

    return failures

def main():
    parser = argparse.ArgumentParser(
        description="Validate JSON files against AI Risk Assurance Framework schemas",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate a risk register (auto-detect schema)
  python validate_schemas.py ../examples/sample-risk-register.json

  # Validate with explicit schema type
  python validate_schemas.py my-assessment.json --schema faira

  # Validate all example files
  python validate_schemas.py --all

  # Verbose output
  python validate_schemas.py my-file.json --verbose

Available schema types:
  - risk-register      Risk assessment register
  - faira              FAIRA framework assessment
  - vaiss              VAISS guardrail assessment
  - nist-competencies  NIST AI Security competencies
  - control-catalog    Control catalog
  - compliance-mapping Cross-framework compliance mapping
        """
    )

    parser.add_argument(
        "file",
        nargs="?",
        help="JSON file to validate"
    )

    parser.add_argument(
        "--schema",
        choices=list(SCHEMA_TYPES.keys()),
        help="Schema type (auto-detected if not specified)"
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Validate all example files in the examples directory"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )

    parser.add_argument(
        "--list-schemas",
        action="store_true",
        help="List available schema types"
    )

    args = parser.parse_args()

    # List schemas
    if args.list_schemas:
        print(f"{Colors.BOLD}Available Schema Types:{Colors.END}")
        for schema_type, schema_file in SCHEMA_TYPES.items():
            print(f"  • {schema_type:20s} → {schema_file}")
        return 0

    # Validate all examples
    if args.all:
        failures = validate_all_examples(verbose=args.verbose)
        return 1 if failures > 0 else 0

    # Validate single file
    if args.file:
        success = validate_file(args.file, schema_type=args.schema, verbose=args.verbose)
        return 0 if success else 1

    # No file specified
    parser.print_help()
    return 1

if __name__ == "__main__":
    sys.exit(main())
