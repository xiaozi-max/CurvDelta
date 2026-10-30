from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ProjectPageTest(unittest.TestCase):
    def test_required_content_and_links(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        required = (
            "CurvDelta: Low-Curvature Delta Modeling For Surgical Learning and Unlearning",
            "Zeguan Xiao",
            "Zhuocheng Liang",
            "Yun Chen",
            "Yong Wang",
            "Guanhua Chen",
            "Pinyan Lu",
            "Equal contribution",
            "A central challenge in adapting large language models",
            "with retention performance close to the from-scratch retraining reference.",
            "assets/overview.png",
            "https://github.com/xiaozi-max/curvDelta_learning",
            "https://github.com/xiaozi-max/curvDelta_unlearning",
        )
        for value in required:
            with self.subTest(value=value):
                self.assertIn(value, html)

    def test_public_files_are_english_and_private_data_free(self):
        for relative_path in ("index.html", "styles.css", "README.md"):
            text = (ROOT / relative_path).read_text(encoding="utf-8")
            with self.subTest(path=relative_path):
                self.assertNotRegex(text, r"[\u3400-\u9fff]")
                self.assertNotRegex(text, r"[A-Za-z]:[\\/](?:Users|project)")
                self.assertNotRegex(text, r"hf_[A-Za-z0-9]{20,}")
                self.assertNotRegex(text, r"wandb_v1_[A-Za-z0-9_-]{20,}")

    def test_overview_asset_exists(self):
        self.assertTrue((ROOT / "assets/overview.png").is_file())

    def test_layout_remains_minimal(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('<h2>Abstract</h2>', html)
        self.assertIn('<h2>Overview</h2>', html)
        self.assertIn('<h2>Code</h2>', html)
        self.assertNotIn("eyebrow", html)
        self.assertNotIn("section-index", html)
        self.assertNotIn("repo-card", html)
        self.assertNotIn("<script", html)


if __name__ == "__main__":
    unittest.main()
