import unittest

from floorboards.core import Specimen, audit, render_specimen


class FloorboardsTests(unittest.TestCase):
    def make_specimen(self) -> Specimen:
        return Specimen.from_dict(
            {
                "id": "tiny-creak",
                "title": "Tiny creak",
                "observed": ["X happened."],
                "concluded": "Therefore Y.",
                "floorboard": "X was treated as sufficient evidence for Y.",
                "missing_evidence": ["A discriminating observation."],
                "ferret": {
                    "intervention": "Hold X fixed and vary the suspected mediator.",
                    "if_claim": "Y still follows in the predicted way.",
                    "if_floorboard": "Y varies independently."
                },
                "tags": ["test"]
            }
        )

    def test_render_contains_core_sections(self):
        rendered = render_specimen(self.make_specimen())
        self.assertIn("FOUND A FLOORBOARD", rendered)
        self.assertIn("observed:", rendered)
        self.assertIn("floorboard:", rendered)
        self.assertIn("suggested ferret:", rendered)

    def test_audit_accepts_well_formed_specimen(self):
        self.assertEqual(audit([self.make_specimen()]), [])

    def test_audit_rejects_duplicate_ids(self):
        specimen = self.make_specimen()
        problems = audit([specimen, specimen])
        self.assertIn("duplicate id: tiny-creak", problems)


if __name__ == "__main__":
    unittest.main()
