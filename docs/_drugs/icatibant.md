---
layout: default
title: Icatibant
parent: 僅模型預測 (L5)
nav_order: 785
evidence_level: L5
indication_count: 7
---

# Icatibant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Icatibant: From Hereditary Angioedema to C1 Inhibitor Deficiency

## One-Sentence Summary

Icatibant is a bradykinin B2 receptor antagonist established for acute attacks of hereditary angioedema (HAE) internationally, though it currently holds no TFDA license and is not marketed in Taiwan. The TxGNN model predicts it may be effective for the broader disease category **C1 Inhibitor Deficiency** — including acquired forms beyond the classic hereditary type — with **23 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary Angioedema (HAE), acute attacks — derived from clinical trial evidence; no TFDA-approved label on file |
| Predicted New Indication | C1 inhibitor deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of TFDA Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation (e.g., from DrugBank) is not yet available in this evidence pack (data gap DG002). Based on information captured within the trial evidence itself, icatibant is described as a synthetic bradykinin B2 receptor antagonist ("a bradykinin antagonist," NCT00097695) used to block bradykinin-mediated vascular permeability. Its efficacy in acute HAE attacks caused by hereditary C1 inhibitor (C1-INH) deficiency has been repeatedly demonstrated across multiple completed Phase 3 trials.

Hereditary angioedema is itself the clinical manifestation of C1-INH deficiency or dysfunction — the TxGNN model's top prediction, "C1 inhibitor deficiency," is therefore mechanistically continuous with icatibant's established use rather than a distant repurposing target. Several publications in this pack (e.g., PMID 22686628, PMID 35871284, PMID 28687105) go further and describe real-world, largely off-label use of icatibant in **acquired** C1-INH deficiency (AAE-C1-INH) — a rarer, non-hereditary condition with no approved therapy. This suggests the prediction may reflect a genuine, if narrower, opportunity: extending icatibant's evidence base from the hereditary form to the wider C1-INH deficiency spectrum, including acquired angioedema.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00097695](https://clinicaltrials.gov/study/NCT00097695) | Phase 3 | Completed | 84 | Pivotal RCT: SC icatibant vs. placebo for acute cutaneous/abdominal HAE attacks |
| [NCT00912093](https://clinicaltrials.gov/study/NCT00912093) | Phase 3 | Completed | 98 | RCT: SC icatibant vs. placebo confirms efficacy/safety in acute HAE attacks |
| [NCT00500656](https://clinicaltrials.gov/study/NCT00500656) | Phase 3 | Completed | 85 | RCT: SC icatibant vs. oral tranexamic acid, time to symptom relief |
| [NCT00997204](https://clinicaltrials.gov/study/NCT00997204) | Phase 3 | Completed | 151 | Open-label: self-administered SC icatibant, safety/tolerability/convenience |
| [NCT03888755](https://clinicaltrials.gov/study/NCT03888755) | Phase 3 | Completed | 8 | Japanese HAE type I/II patients, efficacy/PK/safety of acute-attack treatment |
| [NCT01386658](https://clinicaltrials.gov/study/NCT01386658) | Phase 3 | Completed | 32 | Pediatric/adolescent PK, tolerability, and safety of single SC dose |
| [NCT04654351](https://clinicaltrials.gov/study/NCT04654351) | Phase 3 | Completed | 2 | Japanese children/adolescents, safety, efficacy, and PK |
| [NCT01457430](https://clinicaltrials.gov/study/NCT01457430) | Phase 4 | Completed | 19 | Real-world self-administered icatibant for acute HAE attacks |
| [NCT07290855](https://clinicaltrials.gov/study/NCT07290855) | Phase 4 | Completed | 5 | Taiwan (NHI-reimbursed): icatibant for bradykinin-induced angioedema |
| [NCT01034969](https://clinicaltrials.gov/study/NCT01034969) | N/A | Completed | 1761 | Icatibant Outcome Survey (IOS), international long-term real-world registry |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22686628](https://pubmed.ncbi.nlm.nih.gov/22686628/) | 2012 | Observational | Allergy | Icatibant used off-label in 8 patients with acquired C1-INH deficiency; attack resolution comparable to hereditary-form experience |
| [35871284](https://pubmed.ncbi.nlm.nih.gov/35871284/) | 2023 | Retrospective study | Journal of Clinical Pharmacology | Majority of icatibant/C1INH prescriptions in real-world inpatient setting were off-label (ACEi-related, undetermined angioedema) |
| [28687105](https://pubmed.ncbi.nlm.nih.gov/28687105/) | 2017 | Review | Immunology and Allergy Clinics of North America | Reviews acquired C1-INH deficiency, its autoimmune/lymphoproliferative associations, and treatment options |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Review | J Allergy Clin Immunol | Asia-Pacific burden of C1-INH-deficiency HAE; diagnostic and access gaps relevant to regional expansion |
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Review | J Investig Allergol Clin Immunol | Current/emerging therapies for C1-INH-HAE via kallikrein-kinin pathway inhibition |
| [23420425](https://pubmed.ncbi.nlm.nih.gov/23420425/) | 2013 | Systematic Review | Pneumonologia i Alergologia Polska | Comparative review of conestat alfa, C1 esterase inhibitor, and icatibant for acute HAE attacks |
| [26106828](https://pubmed.ncbi.nlm.nih.gov/26106828/) | 2015 | Review | Curr Opin Allergy Clin Immunol | Italian diagnostic and therapeutic experience managing C1-INH-HAE |
| [34965883](https://pubmed.ncbi.nlm.nih.gov/34965883/) | 2021 | Observational (Registry) | Allergy Asthma Clin Immunol | Icatibant Outcome Survey (IOS) Spain: real-world treatment outcomes in HAE type 1/2 |
| [29757016](https://pubmed.ncbi.nlm.nih.gov/29757016/) | 2018 | Review | Expert Rev Clin Immunol | Icatibant use in adolescents and children over 2 years with C1-INH-HAE |
| [30280305](https://pubmed.ncbi.nlm.nih.gov/30280305/) | 2018 | Case series | J Clin Immunol | Icatibant and recombinant C1 inhibitor used for HAE attacks during pregnancy |

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA label data (warnings, contraindications) is not currently available for icatibant in this evidence pack — this is flagged as a **Blocking** data gap (DG001) that prevents completion of an initial safety review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence is strong — three or more completed Phase 3 RCTs plus a large international outcomes registry support icatibant's use across the C1 inhibitor deficiency spectrum. However, icatibant currently holds **zero TFDA licenses** and is not marketed in Taiwan, and the **Blocking** absence of TFDA label/safety data (DG001) means an initial safety assessment (S1) cannot be completed regardless of efficacy strength.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (Blocking gap DG001) — required before any S1 safety review
- Confirmed mechanism-of-action documentation from DrugBank (gap DG002)
- Regulatory pathway assessment for Taiwan market entry/licensing, since no NDA currently exists
- Evidence specifically distinguishing on-label (hereditary) vs. off-label (acquired C1-INH deficiency) use, given most supporting literature for the "new" indication describes off-label practice

*Note: TxGNN also surfaced six lower-ranked candidates (serpinopathy, pseudo-von Willebrand disease, primary platelet release disorder, immune-mediated necrotizing myopathy, antisynthetase syndrome, Glanzmann thrombasthenia) with no supporting trials or literature (Evidence Level L5); these are not clinically actionable and are excluded from this report.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

