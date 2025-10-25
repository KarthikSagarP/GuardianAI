import os
import json
import argparse
import importlib.util
from typing import Dict, Any, Callable, Optional

# Helper to load a module from a file path (works even if folder names have dashes)
def load_module_from_path(name: str, path: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module {name} from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Try to load person-provided implementations (Person-B and Person-C).
# If they aren't present or fail, fall back to the local `contracts.py` mocks.
ROOT = os.path.dirname(__file__)

def _load_tool_funcs() -> Dict[str, Callable]:
    funcs = {}

    # Default: load from contracts.py
    try:
        import contracts as contracts_mod
        funcs['legal_analyst_tool'] = getattr(contracts_mod, 'legal_analyst_tool')
        funcs['code_auditor_agent'] = getattr(contracts_mod, 'code_auditor_agent')
    except Exception:
        funcs['legal_analyst_tool'] = None
        funcs['code_auditor_agent'] = None

    # Try Person-B implementation
    person_b_path = os.path.join(ROOT, 'Person-B', 'legal_tool.py')
    if os.path.exists(person_b_path):
        try:
            mod_b = load_module_from_path('person_b_legal_tool', person_b_path)
            if hasattr(mod_b, 'legal_analyst_tool'):
                funcs['legal_analyst_tool'] = mod_b.legal_analyst_tool
                print("Loaded legal_analyst_tool from Person-B/legal_tool.py")
        except Exception as e:
            print(f"Warning: failed to load Person-B legal tool: {e}")

    # Try Person-C implementation
    person_c_path = os.path.join(ROOT, 'Person-C', 'code_tool.py')
    if os.path.exists(person_c_path):
        try:
            mod_c = load_module_from_path('person_c_code_tool', person_c_path)
            if hasattr(mod_c, 'code_auditor_agent'):
                funcs['code_auditor_agent'] = mod_c.code_auditor_agent
                print("Loaded code_auditor_agent from Person-C/code_tool.py")
        except Exception as e:
            print(f"Warning: failed to load Person-C code tool: {e}")

    return funcs


TOOLS = _load_tool_funcs()


def orchestrate_compliance_check(regulation_pdf: str, repository_url: str, use_existing_db: Optional[bool] = None, filter_by_current_pdf: bool = True) -> str:
    """Orchestrates the two-step compliance checking process.

    Step 1: Get technical brief from legal analyst
    Step 2: Use brief to audit code
    """
    legal_fn = TOOLS.get('legal_analyst_tool')
    code_fn = TOOLS.get('code_auditor_agent')

    if legal_fn is None or code_fn is None:
        raise RuntimeError("Required tool implementations not available. Check Person-B/Person-C folders or contracts.py")

    print("\n=== STEP 1: Analyzing Regulatory Document ===")
    question = "Create a concise, bullet-pointed technical brief for a developer. This brief should list the key compliance requirements from this document that can be checked in a codebase."

    # Person-B's function supports `use_existing_db` and `filter_by_current_pdf` extras; pass them if supported
    try:
        # Some implementations accept additional kwargs
        technical_brief = legal_fn(regulation_pdf, question, use_existing_db, filter_by_current_pdf)
    except TypeError:
        technical_brief = legal_fn(regulation_pdf, question)

    print(f"Technical Brief:\n{technical_brief}\n")

    print("\n=== STEP 2: Auditing Code Repository ===")

    try:
        violations = code_fn(repository_url, technical_brief)
    except TypeError:
        violations = code_fn(repository_url, technical_brief)

    print(f"Violations Found:\n{violations}\n")

    return violations


def run_compliance_audit(regulation_pdf: str, repository_url: str, use_existing_db: Optional[bool] = None, filter_by_current_pdf: bool = True) -> Dict[str, Any]:
    """Main function to run a compliance audit.

    Returns parsed JSON dict when possible, otherwise returns {'raw_output': str}
    """
    try:
        violations_json = orchestrate_compliance_check(regulation_pdf, repository_url, use_existing_db, filter_by_current_pdf)

        try:
            return json.loads(violations_json)
        except json.JSONDecodeError:
            return {"raw_output": violations_json}

    except ValueError as ve:
        raise ValueError(f"Configuration error: {str(ve)}") from ve
    except Exception as e:
        raise RuntimeError(f"Error during compliance audit: {str(e)}") from e


def _parse_cli_args():
    parser = argparse.ArgumentParser(description='GuardianAI Orchestrator - Run a two-step compliance audit')
    parser.add_argument('--pdf', required=False, help='Path to the regulatory PDF')
    parser.add_argument('--repo', required=False, help='GitHub repository URL to audit')
    parser.add_argument('--use-existing-db', dest='use_existing_db', action='store_true', help='If set, add PDF to existing ChromaDB instead of recreating it')
    parser.add_argument('--no-filter-current-pdf', dest='filter_by_current_pdf', action='store_false', help='Do not limit retrieval to the current PDF only')
    parser.add_argument('--sample', action='store_true', help='Run with sample placeholders (for quick demo)')
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_cli_args()

    # Defaults for a quick demo if not provided
    if args.sample and (not args.pdf or not args.repo):
        script_dir = os.path.dirname(__file__)
        default_pdf = os.path.join(script_dir, 'sample_regulation.pdf')
        default_repo = 'https://github.com/your-repo/to-audit'
        regulation_pdf = args.pdf or default_pdf
        repository_url = args.repo or default_repo
    else:
        if not args.pdf or not args.repo:
            print("Error: please provide --pdf and --repo or use --sample")
            exit(1)
        regulation_pdf = args.pdf
        repository_url = args.repo

    try:
        report = run_compliance_audit(regulation_pdf, repository_url, use_existing_db=(args.use_existing_db or None), filter_by_current_pdf=args.filter_by_current_pdf)
        print("\nFinal Compliance Report:")
        print(json.dumps(report, indent=2))
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
        exit(1)