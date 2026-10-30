# CurvDelta Project Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a private, static research project page containing the CurvDelta title, author block, abstract, overview, and two code repository links.

**Architecture:** A buildless `index.html` provides semantic content and `styles.css` provides responsive presentation. A single checked-in overview image is the only page asset, and a standard-library Python test validates publication-critical text, links, and privacy constraints.

**Tech Stack:** HTML5, CSS3, Python `unittest`, GitHub Pages-compatible static files.

## Global Constraints

- Keep the GitHub repository private and do not enable public Pages.
- Use no JavaScript, package manager, framework, or build step.
- Credit Zeguan Xiao and Zhuocheng Liang as equal contributors.
- Omit parenthesized institution domains from the supplied author block.
- Include only the title, author/affiliation block, abstract, overview, repository links, and minimal footer.
- Publish no credentials, private filesystem paths, or Chinese text.

---

### Task 1: Static research page

**Files:**
- Create: `index.html`
- Create: `styles.css`
- Create: `assets/overview.png`
- Create: `README.md`

**Interfaces:**
- Consumes: the approved abstract, overview image, author list, and repository URLs.
- Produces: a buildless static page whose entry point is `index.html`.

- [ ] **Step 1: Write the failing publication test**

Create `tests/test_site.py` with assertions that `index.html` contains the exact title, six author names, `Equal contribution`, the complete abstract opening and closing sentences, both repository URLs, and `assets/overview.png`; assert that neither HTML nor CSS contains a Windows drive path, credential token, or CJK character.

- [ ] **Step 2: Run the test to verify it fails**

Run: `python -m unittest tests.test_site -v`

Expected: FAIL because `index.html` and `styles.css` do not exist.

- [ ] **Step 3: Implement the minimal static page**

Create semantic `header`, `main`, `section`, and `footer` markup. Render authors as:

```text
Zeguan Xiao¹,* · Zhuocheng Liang¹,* · Yun Chen¹ · Yong Wang² · Guanhua Chen³ · Pinyan Lu⁴
```

Render affiliations without domains and add `* Equal contribution.` Add two repository cards linking capability learning and selective unlearning. Use responsive CSS with an off-white background, navy text, blue accents, visible focus states, and a one-column mobile breakpoint.

- [ ] **Step 4: Run the test to verify it passes**

Run: `python -m unittest tests.test_site -v`

Expected: all tests PASS.

- [ ] **Step 5: Commit**

```bash
git add index.html styles.css assets/overview.png README.md tests/test_site.py
git commit -m "feat: add CurvDelta project page"
```

### Task 2: Browser verification and private GitHub source

**Files:**
- Modify only if browser verification reveals a concrete layout or accessibility defect.

**Interfaces:**
- Consumes: Task 1 static page.
- Produces: private repository `xiaozi-max/CurvDelta`; no public deployment.

- [ ] **Step 1: Run static validation**

Run `python -m unittest discover -s tests -v`, scan HTML/CSS for private paths and credentials, and confirm `git diff --check` succeeds.

- [ ] **Step 2: Verify desktop and mobile layouts**

Serve the repository locally with `python -m http.server 8765`, inspect desktop and narrow mobile viewports, and confirm the title, author block, overview image, and repository cards are readable without horizontal overflow.

- [ ] **Step 3: Create and push the private repository**

Create `xiaozi-max/CurvDelta` with private visibility, set it as `origin`, and push `main`. Do not enable GitHub Pages.

- [ ] **Step 4: Verify remote state**

Confirm the repository visibility is `PRIVATE`, default branch is `main`, remote SHA equals local HEAD, and the remote tree contains `index.html`, `styles.css`, and `assets/overview.png`.
