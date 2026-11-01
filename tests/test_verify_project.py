import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify_project", ROOT / "tools" / "verify_project.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class ConfigurationTests(unittest.TestCase):
    def test_rejects_missing_tier(self):
        with self.assertRaisesRegex(ValueError, "Missing verification tier"):
            module.validate_config({"checks": {"unit": {"status": "required", "command": ["true"]}}})

    def test_rejects_unconfigured_tier(self):
        checks = {t: {"status": "not-applicable", "reason": "not in project"} for t in module.TIERS}
        checks["e2e"] = {"status": "unconfigured"}
        with self.assertRaisesRegex(ValueError, "e2e"):
            module.validate_config({"checks": checks})

    def test_rejects_empty_command(self):
        checks = {t: {"status": "not-applicable", "reason": "not in project"} for t in module.TIERS}
        checks["unit"] = {"status": "required", "command": []}
        with self.assertRaisesRegex(ValueError, "command"):
            module.validate_config({"checks": checks})

    def test_accepts_explicit_non_applicable(self):
        checks = {t: {"status": "not-applicable", "reason": "no application yet"} for t in module.TIERS}
        module.validate_config({"checks": checks})

if __name__ == "__main__":
    unittest.main()
