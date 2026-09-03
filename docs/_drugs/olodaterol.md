---
layout: default
title: Olodaterol
parent: 僅模型預測 (L5)
nav_order: 988
evidence_level: L5
indication_count: 2
---

# Olodaterol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Olodaterol: From Chronic Obstructive Pulmonary Disease (COPD) to Bronchitis

## One-Sentence Summary

> Olodaterol is a long-acting β2-adrenergic agonist (LABA) bronchodilator, established in the literature as a once-daily maintenance therapy for chronic obstructive pulmonary disease (COPD).
> The TxGNN model predicts it may also be effective for **Bronchitis**,
> with **3 clinical trials** and **2 publications** currently supporting this specific direction — though these largely reflect the drug's existing COPD-spectrum use rather than a distinctly novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Obstructive Pulmonary Disease (COPD) — inferred from supporting literature (e.g. PMID 25773742: olodaterol is "indicated as a once-daily maintenance bronchodilator therapy in adults with COPD"); no formal license record is available in this evidence pack |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information from the supporting literature, olodaterol belongs to the **long-acting β2-adrenergic agonist (LABA)** class, delivered via the Respimat inhaler, typically as monotherapy (Striverdi Respimat) or in fixed-dose combination with the LAMA tiotropium (Spiolto/Stiolto Respimat). Its established efficacy is in COPD, where it produces sustained bronchodilation over 24 hours.

Bronchitis — particularly chronic bronchitis — is one of the two classic clinical phenotypes of COPD (alongside emphysema), so the TxGNN prediction largely overlaps with olodaterol's already-recognized therapeutic domain rather than pointing to a mechanistically distant, truly novel indication. This is reinforced by the evidence pack's second-ranked prediction, "obstructive lung disease" (score 99.57%), which is supported by a substantial body of completed Phase 3 RCTs (e.g. TONADO, DYNAGITO, VIVACITO) — confirming that β2-agonist bronchodilation is robustly effective across the airway-obstruction spectrum that includes bronchitis.

Mechanistically, β2-adrenergic stimulation relaxes airway smooth muscle regardless of whether the underlying obstructive process is labeled "bronchitis," "COPD," or "obstructive lung disease" — supporting biological plausibility. However, because the evidence specifically tagged to "bronchitis" consists of observational/real-world studies rather than disease-specific RCTs, this should be read as confirmatory of known LABA class effect rather than as a distinct new therapeutic signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05127304](https://clinicaltrials.gov/study/NCT05127304) | N/A | Completed | 11,316 | Retrospective claims analysis comparing healthcare resource utilization, cost, and clinical outcomes in COPD patients initiating Tiotropium Bromide/Olodaterol vs. Fluticasone Furoate/Umeclidinium/Vilanterol. |
| [NCT03333018](https://clinicaltrials.gov/study/NCT03333018) | N/A | Completed | 22,155 | European post-authorization drug utilization study (DUS1/DUS2) characterizing new users of aclidinium bromide (mono/combination) and comparator COPD maintenance medications, including off-label use patterns. |
| [NCT02850978](https://clinicaltrials.gov/study/NCT02850978) | N/A | Completed | 1,335 | Japanese post-marketing surveillance of long-term safety and effectiveness of tiotropium+olodaterol FDC (Spiolto) in real-world COPD patients, explicitly including chronic bronchitis and emphysema phenotypes. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27354040](https://pubmed.ncbi.nlm.nih.gov/27354040/) | 2016 | Review | Am J Health-Syst Pharm | Narrative review of olodaterol's pharmacology, pharmacokinetics, efficacy, and safety as a once-daily LABA for COPD. |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline/Review | Basic Clin Pharmacol Toxicol | Finnish national guideline update on diagnosis and pharmacotherapy of stable COPD, covering bronchodilator therapy including LABAs such as olodaterol. |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack; TFDA label data has been flagged as a **Blocking** data gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking data gap (missing TFDA label warnings/contraindications) prevents entry into the initial safety review stage, and the current bronchitis-specific evidence is observational only (L3), largely reflecting olodaterol's already-established COPD-spectrum use rather than a distinct new indication signal.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — required to clear the S1 safety gate
- Confirmed mechanism of action (MOA) documentation from DrugBank
- Clarification of whether "bronchitis" represents label-scope overlap with COPD or a genuinely distinct indication
- Drug-drug interaction (DDI) data, currently not found in available sources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

