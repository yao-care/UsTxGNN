---
layout: default
title: Natalizumab
parent: Model Prediction Only (L5)
nav_order: 956
evidence_level: L5
indication_count: 5
---

# Natalizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Natalizumab: From Crohn's Disease and Multiple Sclerosis to Bronchitis

## One-Sentence Summary

Natalizumab is a monoclonal antibody originally used for Crohn's disease, inflammatory bowel disease and multiple sclerosis.
The TxGNN model predicts it may be effective for **Bronchitis**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** currently supporting this direction.
Among the other top predictions, the available literature (for example, in psoriasis) mostly reports adverse effects rather than benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Crohn's disease, inflammatory bowel disease, Crohn's colitis, multiple sclerosis |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 2 (both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, natalizumab blocks alpha4-integrin, which limits lymphocyte trafficking into inflamed tissue. Its efficacy in inflammatory bowel disease and multiple sclerosis is tied to this immune-cell trafficking effect.

In principle, the same effect could modulate airway inflammation, which may explain the high TxGNN score. However, this link is theoretical. Bronchitis is frequently infectious, and natalizumab carries infection risks, including progressive multifocal leukoencephalopathy (PML) and opportunistic infections. Using it for an infectious or inflammatory airway condition is therefore unsupported and a safety concern.

### Other Predictions Reviewed

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Summary |
|------|------|------|------|------|
| 2 | Parapsoriasis | 99.37% | L4 | Only a single 2020 case report of dermatologic adverse events (confounded by fingolimod); no treatment evidence |
| 3 | Psoriasis | 99.19% | L4 | Mostly case reports of natalizumab-induced or aggravated psoriasis; one small series reports improvement in comorbid psoriasis |
| 4 | Severe nonproliferative diabetic retinopathy | 99.18% | L5 | Prediction only; no trials or literature |
| 5 | Acute lichenoid pityriasis | 99.04% | L4 | Same single confounded case report as rank 2; no therapeutic support |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top predicted indication (bronchitis).

For reference, the literature found for the third-ranked prediction, **psoriasis**, is summarized below (10 of 18 articles listed):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33589543](https://pubmed.ncbi.nlm.nih.gov/33589543/) | 2021 | Observational (18 patients) | Neurol Neuroimmunol Neuroinflamm | Natalizumab given to 18 MS patients with comorbid psoriasis; reported improvement of psoriasis |
| [35646438](https://pubmed.ncbi.nlm.nih.gov/35646438/) | 2022 | Case report | Dermatol Pract Concept | Natalizumab-induced pustular psoriasis of palms and soles |
| [28905124](https://pubmed.ncbi.nlm.nih.gov/28905124/) | 2018 | Case report with review | Neurol Sci | Arthritic psoriasis during natalizumab treatment |
| [30323758](https://pubmed.ncbi.nlm.nih.gov/30323758/) | 2018 | Case study with review | Case Rep Neurol | Plaque psoriasis developed during natalizumab; evidence of induction or aggravation is limited to case reports |
| [35512502](https://pubmed.ncbi.nlm.nih.gov/35512502/) | 2022 | Pharmacovigilance analysis | Mult Scler Relat Disord | Disproportionate psoriasis reports with B-cell-depleting therapies in MS |
| [40526577](https://pubmed.ncbi.nlm.nih.gov/40526577/) | 2025 | Review | Dtsch Arztebl Int | Treatment options for MS comorbid with chronic inflammatory diseases such as psoriasis and IBD |
| [28765121](https://pubmed.ncbi.nlm.nih.gov/28765121/) | 2018 | Review | Ann Rheum Dis | Novel therapies for immune-mediated inflammatory diseases, including psoriasis and Crohn's disease |
| [20298966](https://pubmed.ncbi.nlm.nih.gov/20298966/) | 2010 | Review | Lancet Neurol | PML and other JC virus disorders; safety context for monoclonal antibodies |
| [24136456](https://pubmed.ncbi.nlm.nih.gov/24136456/) | 2013 | Review | Curr Neurol Neurosci Rep | PML in multiple sclerosis; safety context |
| [15955735](https://pubmed.ncbi.nlm.nih.gov/15955735/) | 2005 | Review | Curr Opin Pharmacol | Anti-adhesion therapies targeting integrins |

Overall, there is no trial evidence of benefit in psoriasis, and the case reports mainly suggest possible harm.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication | Status |
|---------|------|------|-----------|------|
| BLA761322 | TYRUKO (Sandoz Inc) | Injection | Not available | Cancelled |
| BLA125104 | TYSABRI (Biogen Inc.) | Injection | Not available | Cancelled |

## Safety Considerations

- **Disease associations (knowledge graph)**: Progressive multifocal leukoencephalopathy (PML) is listed as a contraindication-type association. The literature reviewed for this report also describes natalizumab-associated PML as a serious, often fatal risk.
- **Drug Interactions**: 100 interactions were identified. Main examples:
  - **Major**: corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, budesonide, triamcinolone), mercaptopurine, levamisole, trimetrexate, ibritumomab tiuxetan, tositumomab, iobenguane (I-131)
  - **Moderate**: naltrexone
  - **Minor**: zinc salts (sulfate, acetate, gluconate, chloride)

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (bronchitis) rests on a model score alone, with no trials or literature. For the other leading predictions, the available evidence is limited to case reports and pharmacovigilance signals suggesting natalizumab may induce or aggravate the conditions rather than treat them. Combined with the infection and PML risk, the benefit-risk balance is not supported.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data
- Preclinical or clinical data supporting benefit in the predicted indication
- Clarification of why both US licenses are listed as cancelled, and of the current regulatory status
- A benefit-risk assessment that addresses the PML and opportunistic infection risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

