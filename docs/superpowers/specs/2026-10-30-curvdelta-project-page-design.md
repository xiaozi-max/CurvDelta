# CurvDelta Project Page Design

## Goal

Create a compact research project page for CurvDelta that introduces the unified learning and unlearning framework and directs readers to the two implementation repositories.

## Hosting and release

- Source repository: `xiaozi-max/CurvDelta`.
- The repository starts private.
- GitHub Pages remains disabled until the user explicitly approves public release.
- The intended public URL is `https://xiaozi-max.github.io/CurvDelta/`.
- The site is plain static HTML and CSS with no build step or JavaScript dependency.

## Content

The page contains one concise, responsive document:

1. Hero section with the paper title: “CurvDelta: Low-Curvature Delta Modeling For Surgical Learning and Unlearning.”
2. The author list and affiliations, without institutional domains in parentheses:
   - Zeguan Xiao¹,*
   - Zhuocheng Liang¹,*
   - Yun Chen¹
   - Yong Wang²
   - Guanhua Chen³
   - Pinyan Lu⁴
   - ¹ Shanghai University of Finance and Economics
   - ² Alibaba Group
   - ³ Southern University of Science and Technology
   - ⁴ Huawei Technologies Ltd.
   - `* Equal contribution.`
   The first two author names link to the `ZeguanXiao` and `xiaozi-max` GitHub profiles.
3. The paper abstract, copied exactly from the repository README.
4. The overview figure and its existing caption.
5. Two equal code cards:
   - Capability Learning → `https://github.com/xiaozi-max/curvDelta_learning`
   - Selective Unlearning → `https://github.com/xiaozi-max/curvDelta_unlearning`
6. A minimal footer with the project name and year. No citation or paper button is included until an arXiv URL exists.

## Visual direction

Use the reference page’s research-first hierarchy without copying its dense interactions. The page uses a warm off-white background, dark navy text, blue accents, a strong editorial title, generous whitespace, and thin technical dividers. The overview figure is the visual center. No animations, result dashboards, navigation rail, or decorative terminal effects are needed.

## Responsive and accessible behavior

- Desktop: centered content with a wide overview figure and two-column repository cards.
- Mobile: single-column flow with full-width repository cards.
- Semantic landmarks and heading order.
- Descriptive image alternative text and visible keyboard focus.
- Sufficient color contrast and no motion dependency.

## Source layout

```text
CurvDelta/
├── index.html
├── styles.css
├── assets/
│   └── overview.png
├── README.md
└── docs/superpowers/specs/2026-10-30-curvdelta-project-page-design.md
```

## Validation

- Confirm all required text and both repository URLs are present.
- Confirm there are no secrets, private filesystem paths, or Chinese text in published files.
- Validate HTML structure and links.
- Check desktop and mobile layouts in a browser before committing and pushing.
- Confirm the GitHub repository remains private and Pages is not publicly deployed.

## Contributor display note

The unlearning repository already recognizes `ZeguanXiao` as a contributor. GitHub’s homepage renders a limited avatar list and does not expose a manual refresh or pinning control. The learning repository will recognize his historical commits only after the old commit email (`www.hainanxzg@gmail.com`) is added to and verified on his GitHub account, unless the history is rewritten. The project page therefore gives both contributors explicit, stable credit regardless of sidebar presentation.
