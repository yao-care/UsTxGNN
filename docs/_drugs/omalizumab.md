---
layout: default
title: Omalizumab
parent: Moderate Evidence (L3-L4)
nav_order: 992
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-28
description: "Omalizumab: predicted new indication Bronchitis (evidence level L3). Approved use: Asthma (allergic and intrinsic) and chronic idiopathic urticaria"
monitor_inn: "OMALIZUMAB"
predicted_indications: ["bronchitis", "atopic eczema", "obstructive lung disease", "dermatitis", "bronchial neoplasm (disease)", "acne keloid", "acrodermatitis chronica atrophicans", "hydroa vacciniforme, familial", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease"]
---

# Omalizumab
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Omalizumab: From Asthma to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Omalizumab is an anti-IgE monoclonal antibody, originally used to treat allergic asthma and chronic idiopathic urticaria.
The TxGNN model predicts it may be effective for **bronchitis**, but the supporting evidence is thin: **2 loosely related clinical trials** and **7 publications**, none of which directly tests bronchitis as the indication.
Among the top predictions, the stronger signals are in atopic eczema and dermatitis (Phase 4 and smaller studies with mixed results) and in obstructive lung disease (largely asthma, the original indication).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (allergic and intrinsic) and chronic idiopathic urticaria (the data compiled for this report lists no approved-indication text for the US licenses) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L3 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of NDAs | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the pharmacology data, omalizumab is an antibody that targets human immunoglobulin E (IgE, gene IGHE). By binding free IgE, it reduces allergic airway inflammation and lowers IgE signaling through mast cells and basophils. It is used for moderate-to-severe IgE-mediated asthma, chronic spontaneous urticaria, and, since February 2024, for reducing the risk of IgE-mediated reactions to food allergens.

Bronchitis is related to the original asthma indication through airway inflammation. However, any benefit is probably indirect. It would most likely appear in patients with asthma, or asthma-COPD overlap with a chronic bronchitis phenotype, rather than in bronchitis as a stand-alone disease. No trial directly tests bronchitis as the indication. The high prediction score should therefore be read as a hypothesis for further study, not as a confirmed finding.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Completed | 11 | Placebo-controlled test of whether omalizumab lets patients with asthma and eosinophilic bronchitis reduce their prednisone dose; very small and underpowered |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | Completed | 382 | Dose-finding study of QGE031 (a next-generation anti-IgE) as add-on therapy in chronic spontaneous urticaria; not a bronchitis trial |

Neither trial tests bronchitis as the target condition, and no efficacy results are available in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohort | Postepy Dermatol Alergol | Biologics such as omalizumab may help middle-aged or older patients with severe allergic asthma-COPD overlap |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Safety study | Curr Med Res Opin | Pooled analysis of omalizumab safety in children with allergic asthma |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clin Rev Allergy Immunol | Omalizumab reduces free IgE and FcεRI expression and is effective in moderate-to-severe persistent asthma |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | Treatment challenges in asthma with smoking-induced airway disease, including chronic bronchitis |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui | Preoperative management of asthma or chronic bronchitis; mentions omalizumab for severe allergic asthma |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergol Immunopathol | Overview of monoclonal antibodies in pediatrics |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case report | J Investig Allergol Clin Immunol | Rare case of plastic bronchitis after bronchial thermoplasty |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA103976 | Xolair PFS (Genentech, Inc.) | Injection, solution | Not listed; status valid |
| BLA761399 | Omalizumab-igec (CELLTRION, Inc.) | Injection | Not listed; status valid |

---

## Safety Considerations

- **Drug Interactions**: 8 interactions were recorded. Most are minor (zinc sulfate, zinc acetate, zinc gluconate, zinc chloride, echinacea, vitamin E). One is moderate: omacetaxine mepesuccinate. The pharmacology database also lists the IgE target (IGHE) as an interaction entry; this is the drug's intended target, not a drug-drug interaction.

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Bronchitis has no trial that directly tests it. The only related trial is a very small study (n=11) in asthma with eosinophilic bronchitis, and the literature consists of reviews, one cohort, and one case report. The high TxGNN score likely reflects the drug's strong link to asthma, which is its original indication, rather than a distinct bronchitis signal.

**Other predictions worth noting:**
- **Atopic eczema / dermatitis (evidence level L2)**: A Phase 4 trial in severe pediatric atopic eczema (NCT02300701, n=62) and several smaller studies exist, but reviews describe the efficacy evidence as mixed ("for and against"), and omalizumab is generally considered less effective than agents targeting IL-4/IL-13. This is the most credible new-indication research question.
- **Obstructive lung disease (L1)**: The Phase 3 evidence applies to allergic asthma, which is the original indication, so it is not true repurposing. For COPD specifically, a Phase 2 trial in allergen-sensitized patients is recruiting (NCT07059091, n=334), and an earlier one was withdrawn before enrollment.
- **Bronchial neoplasm, acne keloid, and the other low-evidence predictions (L5)**: There is no supporting evidence or plausible mechanism, so they should be held.

**To proceed, the following is needed:**
- Mechanism of action data and the FDA package insert warnings and contraindications, which are currently missing
- A trial with bronchitis (or a chronic bronchitis phenotype) as the defined condition, or an analysis of asthma-COPD overlap subgroups
- Clarification of the cancelled US license status and the current marketed products
- Review of the atopic dermatitis and COPD-OMA results as higher-priority research questions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

