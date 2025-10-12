#!/usr/bin/env python3
"""
FAIRA Compliance Checker - Multi-Framework Compliance Analysis Tool

Check AI system compliance against:
- FAIRA Framework v1.0.0
- Microsoft AI Security Risk Assessment v4.1.4
- NIST AI Security Competency Area (NF-COM-002)
- VAISS (Voluntary AI Safety Standard) v1.0
- NFAAIG 2024-2025

Usage:
    faira-check.py <assessment-file> [--frameworks <framework-list>]
    faira-check.py <assessment-file> --report <output-file>
    faira-check.py --help

Examples:
    # Check against all frameworks
    faira-check.py my-risk-register.json

    # Check specific frameworks
    faira-check.py my-risk-register.json --frameworks FAIRA,VAISS,NIST

    # Generate detailed report
    faira-check.py my-risk-register.json --report compliance-report.html

    # Gap analysis mode
    faira-check.py my-assessment.json --gaps --framework VAISS
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime

try:
    import yaml
except ImportError:
    print("❌ Error: PyYAML library not installed")
    print("Install with: pip install PyYAML")
    sys.exit(1)

@dataclass
class ComplianceCheck:
    """Single compliance check result"""
    requirement: str
    status: str  # 'met', 'partial', 'not_met', 'not_applicable'
    framework: str
    category: str
    evidence: Optional[str] = None
    recommendation: Optional[str] = None
    severity: str = 'medium'  # 'low', 'medium', 'high', 'critical'

@dataclass
class ComplianceReport:
    """Overall compliance report"""
    assessment_id: str
    project_name: str
    frameworks_checked: List[str]
    timestamp: str
    checks: List[ComplianceCheck]
    overall_score: float
    summary: Dict[str, int]

class Colors:
    """ANSI color codes"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    BOLD = '\033[1m'
    END = '\033[0m'

class FrameworkChecker:
    """Base class for framework checkers"""

    def __init__(self, data: Dict):
        self.data = data

    def check_compliance(self) -> List[ComplianceCheck]:
        """Override in subclasses"""
        raise NotImplementedError

class FAIRAChecker(FrameworkChecker):
    """FAIRA Framework compliance checker"""

    def check_compliance(self) -> List[ComplianceCheck]:
        checks = []

        # Check Part A: Components Analysis
        checks.append(self._check_part_a())

        # Check Part B: Values Assessment
        checks.append(self._check_part_b())

        # Check Part C: Controls
        checks.append(self._check_part_c())

        return checks

    def _check_part_a(self) -> ComplianceCheck:
        """Check Part A components are documented"""
        if 'partA' in self.data:
            part_a = self.data['partA']
            required_tables = ['solutionOverview', 'componentArchitecture', 'interfaces',
                             'dataSources', 'dataTypes', 'outputs']
            present = sum(1 for table in required_tables if table in part_a)

            if present == len(required_tables):
                return ComplianceCheck(
                    requirement="Part A: Components Analysis complete",
                    status='met',
                    framework='FAIRA',
                    category='Documentation',
                    evidence=f"All {len(required_tables)} required tables present"
                )
            elif present > 0:
                return ComplianceCheck(
                    requirement="Part A: Components Analysis",
                    status='partial',
                    framework='FAIRA',
                    category='Documentation',
                    evidence=f"{present}/{len(required_tables)} tables present",
                    recommendation="Complete all Part A tables"
                )

        return ComplianceCheck(
            requirement="Part A: Components Analysis",
            status='not_met',
            framework='FAIRA',
            category='Documentation',
            recommendation="Complete FAIRA Part A assessment",
            severity='high'
        )

    def _check_part_b(self) -> ComplianceCheck:
        """Check Part B values assessment"""
        if 'partB' in self.data and 'ethicsPrinciples' in self.data['partB']:
            principles = self.data['partB']['ethicsPrinciples']
            if len(principles) == 8:
                return ComplianceCheck(
                    requirement="Part B: Values Assessment (8 AI Ethics Principles)",
                    status='met',
                    framework='FAIRA',
                    category='Ethics',
                    evidence="All 8 AI Ethics Principles assessed"
                )

        return ComplianceCheck(
            requirement="Part B: Values Assessment",
            status='not_met',
            framework='FAIRA',
            category='Ethics',
            recommendation="Assess all 8 AI Ethics Principles",
            severity='high'
        )

    def _check_part_c(self) -> ComplianceCheck:
        """Check Part C controls"""
        if 'partC' in self.data and 'controlPlan' in self.data['partC']:
            controls = self.data['partC']['controlPlan']
            if len(controls) > 0:
                return ComplianceCheck(
                    requirement="Part C: Controls for AI Risks",
                    status='met',
                    framework='FAIRA',
                    category='Controls',
                    evidence=f"{len(controls)} controls defined"
                )

        return ComplianceCheck(
            requirement="Part C: Controls for AI Risks",
            status='not_met',
            framework='FAIRA',
            category='Controls',
            recommendation="Define risk controls in Part C",
            severity='high'
        )

class VAISSChecker(FrameworkChecker):
    """VAISS guardrail compliance checker"""

    def check_compliance(self) -> List[ComplianceCheck]:
        checks = []

        guardrail_names = [
            "Accountability and Governance",
            "Risk Management",
            "Data Governance and Protection",
            "Testing and Monitoring",
            "Human Oversight",
            "Transparency",
            "Contestability",
            "Supply Chain Transparency",
            "Compliance",
            "Stakeholder Engagement"
        ]

        if 'guardrailAssessments' in self.data:
            assessments = self.data['guardrailAssessments']

            for i, name in enumerate(guardrail_names, 1):
                # Find assessment for this guardrail
                assessment = next((a for a in assessments if a.get('guardrailNumber') == i), None)

                if assessment:
                    status_map = {
                        'Fully Implemented': 'met',
                        'Largely Implemented': 'partial',
                        'Partially Implemented': 'partial',
                        'Not Implemented': 'not_met'
                    }

                    impl_status = assessment.get('implementationStatus', 'Not Implemented')
                    check_status = status_map.get(impl_status, 'not_met')

                    checks.append(ComplianceCheck(
                        requirement=f"VAISS Guardrail {i}: {name}",
                        status=check_status,
                        framework='VAISS',
                        category='Guardrails',
                        evidence=f"Status: {impl_status}"
                    ))
                else:
                    checks.append(ComplianceCheck(
                        requirement=f"VAISS Guardrail {i}: {name}",
                        status='not_met',
                        framework='VAISS',
                        category='Guardrails',
                        recommendation=f"Assess guardrail {i}",
                        severity='medium'
                    ))

        else:
            # No VAISS assessment found
            checks.append(ComplianceCheck(
                requirement="VAISS 10 Guardrails Assessment",
                status='not_met',
                framework='VAISS',
                category='Guardrails',
                recommendation="Complete VAISS guardrail assessment",
                severity='high'
            ))

        return checks

class NISTChecker(FrameworkChecker):
    """NIST AI Security Competency checker"""

    def check_compliance(self) -> List[ComplianceCheck]:
        checks = []

        # Check if risks are mapped to NIST competencies
        if 'risks' in self.data:
            risks = self.data['risks']
            mapped_risks = sum(1 for r in risks if 'nistCompetency' in r and r['nistCompetency'])

            if mapped_risks > 0:
                percentage = (mapped_risks / len(risks)) * 100
                if percentage == 100:
                    status = 'met'
                elif percentage >= 50:
                    status = 'partial'
                else:
                    status = 'not_met'

                checks.append(ComplianceCheck(
                    requirement="NIST Competency Mapping",
                    status=status,
                    framework='NIST',
                    category='Competencies',
                    evidence=f"{mapped_risks}/{len(risks)} risks mapped to NIST competencies ({percentage:.0f}%)",
                    recommendation="Map all risks to relevant NIST AI-K-### or AI-S-### competencies" if percentage < 100 else None
                ))
            else:
                checks.append(ComplianceCheck(
                    requirement="NIST Competency Mapping",
                    status='not_met',
                    framework='NIST',
                    category='Competencies',
                    recommendation="Map risks to NIST AI Security competencies",
                    severity='medium'
                ))

        return checks

class MicrosoftChecker(FrameworkChecker):
    """Microsoft AI Security compliance checker"""

    def check_compliance(self) -> List[ComplianceCheck]:
        checks = []

        # Check if risks are categorized by Microsoft threat types
        if 'risks' in self.data:
            risks = self.data['risks']
            threat_typed = sum(1 for r in risks if 'threatType' in r and r['threatType'])

            if threat_typed > 0:
                percentage = (threat_typed / len(risks)) * 100
                status = 'met' if percentage >= 80 else ('partial' if percentage >= 40 else 'not_met')

                checks.append(ComplianceCheck(
                    requirement="Microsoft Threat Type Classification",
                    status=status,
                    framework='Microsoft',
                    category='Threat Analysis',
                    evidence=f"{threat_typed}/{len(risks)} risks classified by threat type ({percentage:.0f}%)"
                ))

        # Check for Microsoft-specific controls
        checks.append(ComplianceCheck(
            requirement="Microsoft AI Security Controls",
            status='partial',
            framework='Microsoft',
            category='Controls',
            recommendation="Review Microsoft AI Security Risk Assessment guidance",
            severity='low'
        ))

        return checks

def load_assessment_file(file_path: str) -> Dict:
    """Load JSON or YAML assessment file"""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Assessment file not found: {file_path}")

    with open(path, 'r', encoding='utf-8') as f:
        if path.suffix in ['.yaml', '.yml']:
            return yaml.safe_load(f)
        else:
            return json.load(f)

def run_compliance_checks(data: Dict, frameworks: List[str]) -> List[ComplianceCheck]:
    """Run compliance checks for selected frameworks"""
    all_checks = []

    checker_map = {
        'FAIRA': FAIRAChecker,
        'VAISS': VAISSChecker,
        'NIST': NISTChecker,
        'Microsoft': MicrosoftChecker,
    }

    for framework in frameworks:
        if framework in checker_map:
            checker = checker_map[framework](data)
            checks = checker.check_compliance()
            all_checks.extend(checks)

    return all_checks

def calculate_scores(checks: List[ComplianceCheck]) -> Tuple[float, Dict[str, int]]:
    """Calculate overall compliance score and summary"""
    if not checks:
        return 0.0, {}

    status_counts = {
        'met': sum(1 for c in checks if c.status == 'met'),
        'partial': sum(1 for c in checks if c.status == 'partial'),
        'not_met': sum(1 for c in checks if c.status == 'not_met'),
        'not_applicable': sum(1 for c in checks if c.status == 'not_applicable'),
    }

    # Calculate weighted score (met=1.0, partial=0.5, not_met=0.0, n/a excluded)
    applicable = len(checks) - status_counts['not_applicable']
    if applicable == 0:
        return 0.0, status_counts

    score = (status_counts['met'] + (status_counts['partial'] * 0.5)) / applicable * 100

    return score, status_counts

def print_report(report: ComplianceReport, verbose: bool = False):
    """Print compliance report to console"""
    print(f"\n{Colors.BOLD}{'='*80}{Colors.END}")
    print(f"{Colors.BOLD}🛡️  AI Risk Assurance Compliance Report{Colors.END}")
    print(f"{Colors.BOLD}{'='*80}{Colors.END}\n")

    # Header
    print(f"{Colors.BOLD}Project:{Colors.END} {report.project_name}")
    print(f"{Colors.BOLD}Assessment ID:{Colors.END} {report.assessment_id}")
    print(f"{Colors.BOLD}Frameworks:{Colors.END} {', '.join(report.frameworks_checked)}")
    print(f"{Colors.BOLD}Generated:{Colors.END} {report.timestamp}\n")

    # Overall Score
    score_color = Colors.GREEN if report.overall_score >= 80 else (Colors.YELLOW if report.overall_score >= 50 else Colors.RED)
    print(f"{Colors.BOLD}Overall Compliance Score:{Colors.END} {score_color}{report.overall_score:.1f}%{Colors.END}\n")

    # Summary
    print(f"{Colors.BOLD}Summary:{Colors.END}")
    print(f"  {Colors.GREEN}✅ Met:{Colors.END} {report.summary['met']}")
    print(f"  {Colors.YELLOW}⚠️  Partial:{Colors.END} {report.summary['partial']}")
    print(f"  {Colors.RED}❌ Not Met:{Colors.END} {report.summary['not_met']}")
    if report.summary['not_applicable'] > 0:
        print(f"  ⊝ Not Applicable: {report.summary['not_applicable']}")
    print()

    # Detailed Checks
    if verbose:
        print(f"{Colors.BOLD}Detailed Checks:{Colors.END}\n")

        # Group by framework
        by_framework = {}
        for check in report.checks:
            if check.framework not in by_framework:
                by_framework[check.framework] = []
            by_framework[check.framework].append(check)

        for framework, checks in by_framework.items():
            print(f"{Colors.BOLD}{Colors.BLUE}Framework: {framework}{Colors.END}")
            print(f"{'-' * 80}")

            for check in checks:
                # Status icon and color
                if check.status == 'met':
                    icon, color = '✅', Colors.GREEN
                elif check.status == 'partial':
                    icon, color = '⚠️ ', Colors.YELLOW
                elif check.status == 'not_met':
                    icon, color = '❌', Colors.RED
                else:
                    icon, color = '⊝', ''

                print(f"{icon} {color}{check.requirement}{Colors.END}")

                if check.evidence:
                    print(f"   Evidence: {check.evidence}")

                if check.recommendation:
                    print(f"   {Colors.YELLOW}→ Recommendation: {check.recommendation}{Colors.END}")

                print()

    # Recommendations
    critical_issues = [c for c in report.checks if c.status == 'not_met' and c.severity == 'high']
    if critical_issues:
        print(f"{Colors.BOLD}{Colors.RED}Critical Issues ({len(critical_issues)}):{Colors.END}")
        for issue in critical_issues[:5]:  # Show top 5
            print(f"  • {issue.requirement}")
            if issue.recommendation:
                print(f"    → {issue.recommendation}")
        if len(critical_issues) > 5:
            print(f"  ... and {len(critical_issues) - 5} more")
        print()

    print(f"{Colors.BOLD}{'='*80}{Colors.END}\n")

def main():
    parser = argparse.ArgumentParser(
        description="FAIRA Compliance Checker - Multi-Framework Compliance Analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Check against all frameworks
  faira-check.py my-risk-register.json

  # Check specific frameworks
  faira-check.py my-risk-register.json --frameworks FAIRA,VAISS,NIST

  # Verbose output with detailed checks
  faira-check.py my-assessment.json --verbose

Supported Frameworks:
  - FAIRA      Queensland Government FAIRA Framework v1.0.0
  - VAISS      Voluntary AI Safety Standard v1.0
  - NIST       NIST AI Security Competency Area (NF-COM-002)
  - Microsoft  Microsoft AI Security Risk Assessment v4.1.4
  - NFAAIG     National Framework for AI Assurance in Government (coming soon)
        """
    )

    parser.add_argument(
        "assessment_file",
        help="Path to assessment file (JSON or YAML)"
    )

    parser.add_argument(
        "--frameworks",
        default="FAIRA,VAISS,NIST,Microsoft",
        help="Comma-separated list of frameworks to check (default: all)"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output with detailed checks"
    )

    parser.add_argument(
        "--report",
        help="Generate HTML report to specified file"
    )

    parser.add_argument(
        "--json",
        help="Export results as JSON to specified file"
    )

    args = parser.parse_args()

    try:
        # Load assessment
        print(f"{Colors.BLUE}Loading assessment: {args.assessment_file}{Colors.END}")
        data = load_assessment_file(args.assessment_file)

        # Parse frameworks
        frameworks = [f.strip() for f in args.frameworks.split(',')]

        # Run checks
        print(f"{Colors.BLUE}Running compliance checks...{Colors.END}\n")
        checks = run_compliance_checks(data, frameworks)

        # Calculate scores
        overall_score, summary = calculate_scores(checks)

        # Create report
        report = ComplianceReport(
            assessment_id=data.get('metadata', {}).get('assessmentId', 'N/A'),
            project_name=data.get('metadata', {}).get('projectName', 'Unnamed Project'),
            frameworks_checked=frameworks,
            timestamp=datetime.now().isoformat(),
            checks=checks,
            overall_score=overall_score,
            summary=summary
        )

        # Print report
        print_report(report, verbose=args.verbose)

        # Export if requested
        if args.json:
            with open(args.json, 'w', encoding='utf-8') as f:
                json.dump({
                    'assessmentId': report.assessment_id,
                    'projectName': report.project_name,
                    'overallScore': report.overall_score,
                    'summary': report.summary,
                    'checks': [
                        {
                            'requirement': c.requirement,
                            'status': c.status,
                            'framework': c.framework,
                            'category': c.category,
                            'evidence': c.evidence,
                            'recommendation': c.recommendation,
                            'severity': c.severity
                        }
                        for c in report.checks
                    ]
                }, f, indent=2)
            print(f"{Colors.GREEN}✅ JSON report saved to: {args.json}{Colors.END}\n")

        # Exit code based on score
        if overall_score >= 80:
            return 0
        elif overall_score >= 50:
            return 1
        else:
            return 2

    except FileNotFoundError as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.END}")
        return 1
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.END}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
