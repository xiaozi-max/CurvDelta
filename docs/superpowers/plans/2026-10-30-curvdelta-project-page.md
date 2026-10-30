# CurvDelta Project Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and privately publish the source repository for a minimal CurvDelta research project page.

**Architecture:** A buildless static page uses one semantic `index.html`, one `styles.css`, and one local overview image. Content is fixed paper metadata; external navigation is limited to the two GitHub repositories and the first two authors’ GitHub profiles.

**Tech Stack:** HTML5, CSS3, Python standard-library validation, GitHub Pages-compatible repository layout.

## Global Constraints

- Keep the GitHub repository private and do not enable public Pages.
- Use the six supplied author names and four affiliations exactly, without parenthesized institutional domains.
- Mark Zeguan Xiao and Zhuocheng Liang as equal contributors.
- Include only title, authors, abstract, overview, repository links, and a minimal footer.
- Do not add JavaScript, frameworks, package dependencies, animation, results, citation, or navigation.

---

### Task 1: Static research page

**Files:**
- Create: `index.html`
- Create: `styles.css`
- Create: `assets/overview.png`
- Create: `README.md`
- Create: `tests/test_page.py`

**Interfaces:**
- Consumes: the approved abstract and overview asset from `curvDelta_learning`.
- Produces: a GitHub Pages-compatible static document at repository root.

- [ ] **Step 1: Write the failing page-content test**

Create `tests/test_page.py` with standard-library assertions that `index.html` contains the exact title, all six authors, four affiliations, equal-contribution note, abstract heading, overview image, and both repository URLs; assert that `styles.css` and `assets/overview.png` exist.

- [ ] **Step 2: Run the test and verify it fails**

Run: `python -m unittest tests.test_page -v`

Expected: failure because `index.html` does not exist.

- [ ] **Step 3: Implement the minimal page**

Create semantic HTML sections in this order: `header`, author metadata, `Abstract`, `Overview`, `Code`, `footer`. Add only responsive typography, a centered content column, a two-column repository-link row that becomes one column on mobile, visible focus styles, and neutral research-page colors.

- [ ] **Step 4: Run tests and local validation**

Run:

```powershell
python -m unittest tests.test_page -v
python -m http.server 8000
```

Expected: all tests pass; browser inspection shows correct desktop and mobile layouts, working links, no console errors, and a visible overview image.

- [ ] **Step 5: Commit the page**

```powershell
git add index.html styles.css assets/overview.png README.md tests/test_page.py docs
git commit -m "feat: add CurvDelta project page"
```

### Task 2: Private GitHub source publication

**Files:**
- Verify: all tracked files

**Interfaces:**
- Consumes: the verified static page commit.
- Produces: private repository `xiaozi-max/CurvDelta`; no public Pages deployment.

- [ ] **Step 1: Run final release checks**

Run the unit test, HTML link scan, secret/path scan, `git diff --check`, and `git status --short`.

Expected: tests pass; no secrets, personal paths, Chinese text, or uncommitted files.

- [ ] **Step 2: Create and push the private repository**

```powershell
gh repo create xiaozi-max/CurvDelta --private --description "Project page for CurvDelta: low-curvature delta modeling for surgical learning and unlearning"
git remote add origin https://github.com/xiaozi-max/CurvDelta.git
git push -u origin main
```

- [ ] **Step 3: Verify remote state**

Run `gh repo view xiaozi-max/CurvDelta --json isPrivate,visibility,defaultBranchRef,url` and compare `git rev-parse HEAD` with `git ls-remote origin refs/heads/main`.

Expected: repository is private, default branch is `main`, and local/remote SHAs match.
