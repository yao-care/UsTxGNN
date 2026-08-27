---
layout: default
title: Montelukast
parent: 僅模型預測 (L5)
nav_order: 941
evidence_level: L5
indication_count: 5
---

# Montelukast
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Montelukast: From Asthma to Bronchitis

## One-Sentence Summary

Montelukast is a leukotriene receptor antagonist originally used to control asthma and allergic rhinitis. The TxGNN model predicts it may also be effective for **Bronchitis** (a category that in this evidence set spans infectious/eosinophilic bronchitis and post-transplant bronchiolitis obliterans), currently supported by **23 clinical trials** and **20 publications**, though a substantial share of the retrieved trials are ontology-matching noise rather than true montelukast evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma / Allergic Rhinitis (no local market license record found in this jurisdiction) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A structured mechanism-of-action record was not available for this drug in the current evidence pack. However, other parts of the same evidence set (the mechanistic rationale attached to the "asthma" candidate) confirm that montelukast is a selective cysteinyl leukotriene receptor 1 (CysLT1) antagonist: it blocks the bronchoconstrictive, mucus-hypersecretory, and eosinophil-recruiting effects of cysteinyl leukotrienes. This is the established mechanism behind its approved use in asthma and allergic rhinitis.

Bronchitis, as retrieved here, is not a single homogeneous disease — the underlying trials cluster into three sub-groups: (1) viral/RSV-induced bronchiolitis in infants, (2) non-asthmatic eosinophilic bronchitis, and (3) bronchiolitis obliterans (BO) following lung or hematopoietic stem-cell transplantation. Leukotriene-mediated inflammation has reasonable biological plausibility in the eosinophilic-bronchitis and post-transplant BO subtypes (both show measurable CysLT activity), which is where the highest-quality trial evidence (Phase 3/4 RCTs) actually concentrates. For general infectious bronchitis, the mechanistic link is comparatively weak.

**Data-quality caveat**: this evidence pack separately lists "asthma" (rank 3) as a *predicted* new indication for montelukast, with an evidence level of L1 and 50 clinical trials. Asthma is in fact montelukast's well-established, decades-old core indication — not a genuine repurposing signal. This indicates the underlying ranking pipeline is not filtering out already-approved indications, and the disease-matching for "bronchitis" and "obstructive lung disease" pulls a similarly large volume of unrelated or duplicated trials (sepsis, ruxolitinib/belumosudil GVHD studies, STEMI, probiotics). All quantitative counts in this report should be read with that caveat in mind.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863317](https://clinicaltrials.gov/study/NCT00863317) | N/A | Completed | 141 | Double-blind placebo-controlled RCT of daily montelukast for viral bronchiolitis in infants; primary endpoint was duration of acute illness. |
| [NCT01211509](https://clinicaltrials.gov/study/NCT01211509) | Phase 4 | Completed | 30 | Double-blind placebo-controlled RCT testing whether montelukast slows chronic rejection (bronchiolitis obliterans syndrome) after lung transplantation. |
| [NCT01307462](https://clinicaltrials.gov/study/NCT01307462) | Phase 2 | Completed | 36 | Fluticasone + azithromycin + montelukast (FAM) combination in bronchiolitis obliterans after stem cell transplant. |
| [NCT00394069](https://clinicaltrials.gov/study/NCT00394069) | Phase 2 | Completed | 14 | Safety, tolerability and plasma concentration of montelukast oral granules in infants 3–6 months with bronchiolitis. |
| [NCT00076973](https://clinicaltrials.gov/study/NCT00076973) | Phase 3 | Completed | 1125 | Large 2-period RCT of two montelukast (MK0476) doses vs. placebo for respiratory symptoms of RSV-induced bronchiolitis in children 3–24 months. |
| [NCT00656058](https://clinicaltrials.gov/study/NCT00656058) | Phase 2 | Completed | 25 | Multi-institutional prospective study of montelukast for bronchiolitis obliterans after allogeneic/autologous stem cell transplant. |
| [NCT01121016](https://clinicaltrials.gov/study/NCT01121016) | Phase 4 | Unknown | 63 | Randomized double-blind add-on montelukast vs. inhaled budesonide alone in non-asthmatic eosinophilic bronchitis. |
| [NCT04613180](https://clinicaltrials.gov/study/NCT04613180) | Phase 4 | Unknown | 100 | Evaluated effectiveness of montelukast for treatment/prevention of recurrent obstructive bronchitis in children 1–7 years. |
| [NCT00524693](https://clinicaltrials.gov/study/NCT00524693) | N/A | Completed | 51 | Double-blind placebo-controlled RCT of montelukast in acute RSV bronchiolitis, assessing clinical progress and cytokine profiles. |
| [NCT01370187](https://clinicaltrials.gov/study/NCT01370187) | N/A | Completed | 146 | Montelukast for acute bronchiolitis and post-bronchiolitis viral-induced wheezing in infants 3–12 months. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25563311](https://pubmed.ncbi.nlm.nih.gov/25563311/) | 2015 | RCT | Chinese Medical Journal | Montelukast + budesonide improved life quality and suppressed airway eosinophilia vs. budesonide alone in non-asthmatic eosinophilic bronchitis. |
| [20976161](https://pubmed.ncbi.nlm.nih.gov/20976161/) | 2010 | RCT | PLoS ONE | Compared fish oil and montelukast, alone and combined, on airway inflammation and hyperpnea-induced bronchoconstriction. |
| [38504551](https://pubmed.ncbi.nlm.nih.gov/38504551/) | 2024 | Review | Ther Adv Respir Dis | Reviews therapeutic potential and mechanisms of montelukast in bronchiolitis obliterans syndrome after lung/HSC transplantation. |
| [30038355](https://pubmed.ncbi.nlm.nih.gov/30038355/) | 2019 | Review | Bone Marrow Transplant | Reviews diagnosis and treatment challenges of bronchiolitis obliterans syndrome, a manifestation of chronic GVHD. |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | BMJ Clinical Evidence | General clinical-evidence review of bronchiolitis in infants. |
| [38485149](https://pubmed.ncbi.nlm.nih.gov/38485149/) | 2024 | Guideline | Eur Respir J | ERS/EBMT joint clinical practice guideline on treatment of pulmonary chronic GVHD (includes BO management context). |
| [35114411](https://pubmed.ncbi.nlm.nih.gov/35114411/) | 2022 | Phase II Trial | Transplant Cell Ther | Prospective Phase II trial of montelukast for BOS after hematopoietic cell transplantation; investigates BOS pathogenesis. |
| [26475726](https://pubmed.ncbi.nlm.nih.gov/26475726/) | 2016 | Phase II Trial | Biol Blood Marrow Transplant | FAM (fluticasone/azithromycin/montelukast) regimen for new-onset BOS after HCT (publication of NCT01307462). |
| [27229850](https://pubmed.ncbi.nlm.nih.gov/27229850/) | 2016 | Clinical Study | Respiratory Research | Budesonide/formoterol + montelukast + N-acetylcysteine for BOS after HSCT. |
| [28545478](https://pubmed.ncbi.nlm.nih.gov/28545478/) | 2017 | Preclinical (rat model) | J Cardiothoracic Surgery | Investigated LTB4 and montelukast in transplantation-related bronchiolitis obliterans in a rat model. |

---

## US Market Information

Montelukast currently has **no marketing license or NDA on record** in this jurisdiction (market status: Not Marketed; 0 licenses returned by the regulatory query). No product-level formulation or approved-indication text is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Additional signal noted in the literature evidence (not part of the formal DDI/label data queried for this candidate):** multiple publications retrieved for related montelukast indications (e.g., PMID 37758273, 35608857, 36948487, 39836401, 39578088) discuss the FDA's 2020 boxed warning on neuropsychiatric adverse events associated with montelukast. This is not sourced from the structured `safety` block and should be independently verified against the current label before use in any clinical evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The drug has no local marketing authorization, and the blocking data gap (TFDA label/warnings, DG001) means no formal safety review is currently possible. The "bronchitis" evidence itself is a mixed bag — real signal exists only in specific subtypes (post-transplant bronchiolitis obliterans, eosinophilic bronchitis), while much of the raw trial count reflects ontology-matching noise unrelated to montelukast or to bronchitis at all.

**To proceed, the following is needed:**
- TFDA-equivalent label, warnings, and contraindications (DG001, blocking)
- Structured mechanism-of-action data from DrugBank (DG002)
- Manual disease-subtype triage: separate infectious bronchitis, eosinophilic bronchitis, and bronchiolitis obliterans into distinct candidates, since they have very different evidence strength and mechanistic rationale
- Re-run/audit the ranking pipeline — the "asthma" candidate in this same batch is montelukast's existing approved indication, not a new use, indicating disease-matching needs review before any candidate in this batch is trusted at face value
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

