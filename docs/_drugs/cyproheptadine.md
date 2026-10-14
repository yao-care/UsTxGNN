---
layout: default
title: Cyproheptadine
parent: Model Prediction Only (L5)
nav_order: 559
evidence_level: L5
indication_count: 4
---

# Cyproheptadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Cyproheptadine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Cyproheptadine is a first-generation antihistamine, originally used for allergic conditions such as allergic rhinitis, urticaria and angioedema.
The TxGNN model predicts it may be effective for **allergic urticaria** (and, as a closely related second prediction, **cold urticaria**).
No clinical trials are registered for the top prediction, and **9 publications** were compiled for it, mostly old clinical studies from the 1960s to 1990s.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, urticaria, angioedema and related allergic conditions (from the knowledge graph; no approved indication text is available in the US license records) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 (for allergic urticaria); L3 for cold urticaria (rank 2) |
| US Market Status | Cancelled only (no currently valid listings) |
| Number of NDAs | 11 (all cancelled ANDA records) |
| Recommended Decision | Hold for allergic urticaria; Proceed with Guardrails for cold urticaria |

## Why is This Prediction Reasonable?

Cyproheptadine is a first-generation H1 antihistamine that also blocks serotonin receptors, and it has anticholinergic activity. Detailed mechanism-of-action data is not available in the data compiled for this report, so this description relies on general knowledge of the drug class.

Allergic urticaria is driven by histamine released from mast cells, so blocking H1 receptors is a direct mechanistic fit. Urticaria and angioedema are already among cyproheptadine's original indications, so this prediction is effectively an on-label or near-label use rather than true repurposing. The extra antiserotonergic activity may add benefit in some forms of urticaria.

The second prediction, cold urticaria, is a physical urticaria that also involves mast cell degranulation and histamine release. Several double-blind studies have tested cyproheptadine in it. However, current practice generally favors up-titrated second-generation antihistamines, with omalizumab as a further option. Cyproheptadine is therefore best seen as a legacy or second-line choice.

The remaining two predictions (nasal cavity disease and acute laryngopharyngitis) have no supporting studies. They most likely reflect overlap with the existing rhinitis, pharyngitis and common cold indications.

## Clinical Trial Evidence

Currently no related clinical trials registered (for allergic urticaria or cold urticaria).

## Literature Evidence

**Allergic urticaria (top prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7488341](https://pubmed.ncbi.nlm.nih.gov/7488341/) | 1995 | Double-blind crossover comparison | Asian Pac J Allergy Immunol | Cyproheptadine vs ketotifen in 6 Thai children with cold urticaria |
| [812662](https://pubmed.ncbi.nlm.nih.gov/812662/) | 1976 | Comparative efficacy study | Curr Ther Res | Cyproheptadine vs hydroxyzine for pruritus in allergic dermatoses |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review (acrivastine, indirect) | Drugs | Review of another antihistamine in urticaria and allergic rhinitis; indirect evidence only |
| [13685954](https://pubmed.ncbi.nlm.nih.gov/13685954/) | 1961 | Clinical study | Br Med J | Cyproheptadine in the treatment of urticaria |
| [14106555](https://pubmed.ncbi.nlm.nih.gov/14106555/) | 1964 | Clinical evaluation | J Assoc Physicians India | Early evaluation in allergic dermatosis |
| [4382319](https://pubmed.ncbi.nlm.nih.gov/4382319/) | 1967 | Clinical study/review | Med Lett Drugs Ther | Cyproheptadine for allergic and pruritic dermatoses |

**Cold urticaria (second prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [334082](https://pubmed.ncbi.nlm.nih.gov/334082/) | 1977 | Double-blind RCT | Arch Dermatol | Cyproheptadine, chlorpheniramine and placebo compared in 8 patients with primary acquired cold urticaria |
| [6102102](https://pubmed.ncbi.nlm.nih.gov/6102102/) | 1980 | Clinical study | J Allergy Clin Immunol | Patients were asymptomatic on cyproheptadine and ice cube tests reverted to normal; effect studied against histamine release |
| [6480953](https://pubmed.ncbi.nlm.nih.gov/6480953/) | 1984 | Double-blind comparative trial | J Am Acad Dermatol | Cinnarizine, cyproheptadine, doxepin and hydroxyzine compared; doxepin was preferred |
| [2901993](https://pubmed.ncbi.nlm.nih.gov/2901993/) | 1988 | Double-blind crossover trial | Dermatologica | Both acrivastine and cyproheptadine reduced wheals versus placebo; acrivastine was significantly more effective |

Overall, the evidence is small, old and mostly comparative. Modern controlled data are limited.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA212491 | Cyproheptadine Hydrochloride (Bryant Ranch Prepack) | Tablet | Not listed (cancelled) |
| ANDA206553 | Cyproheptadine Hydrochloride (TruPharma) | Tablet | Not listed (cancelled) |
| ANDA203191 | Cyproheptadine (Chartwell RX) | Syrup | Not listed (cancelled) |
| ANDA205087 | Cyproheptadine Hydrochloride (Ingenus) | Tablet | Not listed (cancelled) |
| ANDA212423 | Cyproheptadine Hydrochloride (Bryant Ranch Prepack) | Solution | Not listed (cancelled) |

Showing 5 of 11 authorizations; all 11 are cancelled and none is currently valid.

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text)**: hypertension, peptic ulcer disease, benign prostatic hyperplasia, ocular hypertension, angle-closure glaucoma, hyperthyroidism (including Graves disease and thyrotoxicosis), and bladder neck obstruction.
- **Drug Interactions**: 100 interactions are recorded. Major interactions are with potassium chloride and potassium citrate. Many moderate interactions involve anticholinergic agents (atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, trospium) and CNS-active or opioid agents (morphine, opium, loperamide, dronabinol, nabilone). Fenfluramine is also listed.
- **Practical cautions** (from the rationale for cold urticaria): sedation and anticholinergic effects; caution in children and the elderly; caution with CNS-depressant or serotonergic co-medication; and the risk of cold-induced systemic reactions in cold urticaria patients.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold (allergic urticaria); Proceed with Guardrails (cold urticaria)**

**Rationale:**
- Allergic urticaria is essentially an existing indication. The supporting studies are decades old, and there are no registered trials, so this offers little real repurposing value.
- Cold urticaria has several small double-blind studies, and the mechanism is plausible. It could proceed as a legacy or second-line option with safety guardrails.
- The nasal cavity disease and acute laryngopharyngitis predictions rest on model scores alone (L5) and should stay on hold.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data
- Comparison with current guideline therapy (up-titrated second-generation antihistamines, omalizumab)
- A safety plan for sedation and anticholinergic effects in children and the elderly, and for co-medication
- Review of the US market status, since all listed licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

