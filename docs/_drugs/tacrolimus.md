---
layout: default
title: Tacrolimus
parent: High Evidence (L1-L2)
nav_order: 1191
evidence_level: L1
indication_count: 3
---

# Tacrolimus
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **3** 
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

# Tacrolimus: From Atopic Eczema to Seborrheic Dermatitis

## One-Sentence Summary

Tacrolimus is a calcineurin inhibitor originally used (as a topical ointment) for atopic eczema / atopic dermatitis.
The TxGNN model predicts it may be effective for **Seborrheic Dermatitis**,
with **2 clinical trials** (one completed Phase 3, one completed Phase 4) and **20 publications** currently supporting this direction, including a randomized, double-blind trial against ciclopiroxolamine.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic eczema / atopic dermatitis (from the knowledge graph; no approved-indication text is available in the US licence records) |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 |
| US Market Status | Cancelled only (all licences currently listed as cancelled) |
| Number of NDAs | 13 licences (2 NDAs, 11 ANDAs) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on the known pharmacology of tacrolimus, it is a calcineurin inhibitor. It blocks NFAT-dependent T-cell activation and the release of pro-inflammatory cytokines (IL-2, IL-4, IFN-gamma, TNF-alpha).

Atopic dermatitis and seborrheic dermatitis are both chronic, relapsing inflammatory skin diseases. Seborrheic dermatitis involves an inflammatory response to *Malassezia* yeast and skin barrier dysfunction. Topical calcineurin inhibition therefore plausibly reduces this inflammation, and the mechanism overlaps with the approved atopic dermatitis use. Clinical studies of tacrolimus ointment as maintenance therapy in facial seborrheic dermatitis support this reasoning.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Tacrolimus ointment (Protopic) as maintenance treatment of severe seborrheic dermatitis on the adult face, aiming to reduce relapses and steroid use. Randomization and blinding details should be verified. |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Proactive once- or twice-weekly 0.1% tacrolimus ointment to keep adult facial seborrheic dermatitis in remission and reduce exacerbations |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | RCT (multicenter, double-blind) | J Am Acad Dermatol | Tacrolimus 0.1% vs ciclopiroxolamine 1% for maintenance therapy in severe facial seborrheic dermatitis |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Clinical study | Ann Dermatol | Maintenance therapy of facial seborrheic dermatitis with 0.1% tacrolimus ointment |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic review | Am J Clin Dermatol | Topical treatment of facial seborrheic dermatitis (antifungals, keratolytics, corticosteroids) |
| [31476936](https://pubmed.ncbi.nlm.nih.gov/31476936/) | 2019 | Review | J Cutan Med Surg | Off-label use of topical calcineurin inhibitors across dermatologic disorders |
| [11770914](https://pubmed.ncbi.nlm.nih.gov/11770914/) | 2001 | Review | Semin Cutan Med Surg | Topical tacrolimus and pimecrolimus used in psoriasis, seborrheic dermatitis, lichen planus and other conditions |
| [17685874](https://pubmed.ncbi.nlm.nih.gov/17685874/) | 2007 | Review | Expert Opin Investig Drugs | New roles for topical tacrolimus beyond atopic dermatitis |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Current status and therapeutic horizons for facial seborrheic dermatitis |
| [15461548](https://pubmed.ncbi.nlm.nih.gov/15461548/) | 2004 | Review | Expert Opin Pharmacother | Tacrolimus ointment in atopic dermatitis and other inflammatory skin diseases |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Systematic review / network meta-analysis | Clin Exp Allergy | Topical anti-inflammatory treatments for eczema (indirect evidence) |
| [20347654](https://pubmed.ncbi.nlm.nih.gov/20347654/) | 2010 | Review | Clin Dermatol | Tinea incognito can be caused by topical tacrolimus and may mimic seborrheic dermatitis (misdiagnosis caution) |

## US Market Information

All 13 licences are currently listed as cancelled. The main ones are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA050777 | Tacrolimus (Padagis) | Ointment | Not available |
| NDA204096 | ASTAGRAF XL | Extended-release capsule | Not available |
| ANDA200744 | Tacrolimus (Fougera) | Ointment | Not available |
| ANDA210393 | Tacrolimus (Glenmark) | Ointment | Not available |
| ANDA212387 | Tacrolimus (Encube) | Ointment | Not available |

## Safety Considerations

- **Contraindications from the knowledge graph (not label text):** The knowledge graph links tacrolimus to conditions including hypertension, long QT syndrome / torsades de pointes, liver failure, kidney disease, epilepsy, hyperglycemia and diabetes, active infections (including herpes simplex and herpes zoster), lymphoma and other cancers, and progressive multifocal leukoencephalopathy. Many of these relate to systemic (oral) tacrolimus and may not apply equally to topical use.
- **Drug interactions:** 100 interactions were found. Major-level interactions include amphotericin B (including lipid complex), loperamide, mesalazine, balsalazide and omeprazole. Moderate-level examples include famotidine, rabeprazole, metformin, pioglitazone, aprepitant, and several corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide).
- **Cancer risk:** A 2023 systematic review and meta-analysis evaluated cancer risk with topical calcineurin inhibitors, so long-term safety monitoring is warranted.
- **Misdiagnosis risk:** Topical immunomodulators can mask fungal infections (tinea incognito), so diagnosis should be confirmed before use.

Please also refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 trial and a completed Phase 4 study in facial seborrheic dermatitis, plus a published double-blind randomized trial, directly support the prediction. The mechanism is plausible and shared with the approved atopic dermatitis use. Evidence is rated L1 per the project criteria, but only one Phase 3 trial is listed, so confirmation is advisable. The US licences are all cancelled, and label-level safety data is missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently missing)
- Detailed mechanism-of-action data from DrugBank
- Verification of randomization, blinding and results for NCT02004860 and the published trial
- A US regulatory pathway review, since all current licences are cancelled
- A long-term safety monitoring plan (cancer risk, infection) and age/duration limits consistent with labeling

**Other predictions (for reference):**
- **Dermatitis (99.17%, L1):** This is largely atopic dermatitis, the already-established indication, so it is a confirmation rather than a new repurposing finding.
- **Parapsoriasis (99.24%, L4, Hold):** Evidence is limited to two case reports of pityriasis lichenoides, with no clinical trials. The high TxGNN score is a prediction, not clinical validation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

