---
layout: default
title: Isoflurane
parent: 僅模型預測 (L5)
nav_order: 813
evidence_level: L5
indication_count: 7
---

# Isoflurane
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

# Isoflurane: From General Anesthesia to Prinzmetal Angina, Migraine, and Other Predicted Indications

## One-Sentence Summary

Isoflurane (DrugBank DB00753) is a volatile halogenated-ether agent whose established use is inhalational general anesthesia; detailed original-indication and mechanism-of-action records are not available in this evidence pack, and it currently holds **no marketing license in Taiwan**. The TxGNN model surfaced **7 candidate new indications**, ranked highest for **Prinzmetal angina** (99.67%), but literature support is uneven: only **migraine disorder** (13 publications) and **manic bipolar affective disorder** (3 publications) have any supporting evidence, while the remaining 5 candidates — including the top-ranked Prinzmetal angina — rest on the model score alone, with zero clinical trials identified for any candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in regulatory data (isoflurane is generally used for induction/maintenance of general anesthesia) |
| Predicted New Indication (top rank) | Prinzmetal angina |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Taiwan Market Status | Not marketed |
| Number of Taiwan Licenses | 0 |
| Recommended Decision | Hold |

### All Predicted Indications at a Glance

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|-----------------|-----------------|
| 1 | Prinzmetal angina | 99.67% | L5 | S0 | Hold |
| 2 | Tourette syndrome | 99.61% | L5 | S0 | Hold |
| 3 | Manic bipolar affective disorder | 99.57% | L3 | S1 | Research Question |
| 4 | Trichotillomania | 99.54% | L5 | S0 | Hold |
| 5 | Dysthymic disorder | 99.27% | L5 | S0 | Hold |
| 6 | Nephrogenic syndrome of inappropriate antidiuresis | 99.09% | L5 | S0 | Hold |
| 7 | Migraine disorder | 99.06% | L4 | S1 | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for isoflurane is flagged as a data gap in this evidence pack. Based on general pharmacological knowledge, isoflurane is a volatile general anesthetic that potentiates GABA-A receptor activity and antagonizes NMDA receptors, producing dose-dependent central nervous system depression, including a distinctive "burst-suppression" EEG pattern at high concentrations. No original indication text or Taiwan regulatory record was found for this drug, so the mechanistic link below is drawn entirely from the two indications with any evidentiary support.

For **migraine disorder** (L4), the strongest mechanistic thread is isoflurane's demonstrated suppression of cortical spreading depression (CSD) in preclinical models — CSD is the electrophysiological correlate of migraine aura. This is reinforced by case-report evidence of general anesthesia (including isoflurane) being used to terminate refractory status migrainosus, though no controlled trials confirm this translational path.

For **manic bipolar affective disorder** (L3), the rationale rests on isoflurane's ability to induce burst-suppression cortical activity, a state mechanistically analogous to the cortical inhibition produced by electroconvulsive therapy (ECT). One small cohort study found isoflurane-induced burst-suppression comparable to ECT in treatment-refractory depression, but direct evidence for the manic (rather than depressive) pole of bipolar disorder is weak. The remaining five candidates (Prinzmetal angina, Tourette syndrome, trichotillomania, dysthymic disorder, nephrogenic SIAD) have no clinical trials or literature identified — their mechanistic rationale, where offered, is speculative and score-driven only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the 7 predicted indications (ClinicalTrials.gov and ICTRP searches both returned zero results across all indications).

---

## Literature Evidence

### Migraine Disorder (L4)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8665587](https://pubmed.ncbi.nlm.nih.gov/8665587/) | 1996 | Review | Cephalalgia | Inhalational anesthetics, including isoflurane, inhibit cortical spreading depression — proposed relevance to migraine pathophysiology |
| [26323741](https://pubmed.ncbi.nlm.nih.gov/26323741/) | 2015 | Cohort | Brazilian Journal of Anesthesiology | Case report: status migrainosus treated with general anesthesia; propofol and isoflurane act on sub-GABA-A receptors, theoretically useful for severe migraine |
| [26363696](https://pubmed.ncbi.nlm.nih.gov/26363696/) | 2015 | Cohort | Revista Brasileira de Anestesiologia | Portuguese-language version of the same status migrainosus case report above |
| [17267580](https://pubmed.ncbi.nlm.nih.gov/17267580/) | 2007 | Review | J Pharmacol Exp Ther | NMDA receptor antagonists suppress cortical spreading depression in rats — therapeutic potential for migraine |
| [27122032](https://pubmed.ncbi.nlm.nih.gov/27122032/) | 2016 | Review | J Neuroscience | Sensory cortex susceptibility to spreading depolarizations, the biological substrate of migraine aura |
| [22523186](https://pubmed.ncbi.nlm.nih.gov/22523186/) | 2012 | Review | Cephalalgia | Chronic topiramate suppresses potassium-induced cortical spreading depression in rats |
| [39354357](https://pubmed.ncbi.nlm.nih.gov/39354357/) | 2024 | Review | J Headache Pain | Passive smoking effects on cortical spreading depolarization susceptibility in a mouse model |
| [40764901](https://pubmed.ncbi.nlm.nih.gov/40764901/) | 2025 | RCT | J Headache Pain | CGRP antagonist atogepant does not affect cortical spreading depression susceptibility in rats |

*Note: 5 additional lower-relevance publications on trigeminal/CGRP mechanisms were identified but omitted here as they do not reference isoflurane or spreading-depression suppression directly.*

### Manic Bipolar Affective Disorder (L3)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8462536](https://pubmed.ncbi.nlm.nih.gov/8462536/) | 1993 | Cohort | European Journal of Anaesthesiology | Burst-suppression isoflurane anesthesia compared to ECT in 12 patients with severe treatment-refractory depression; marked improvement in both arms |
| [7502646](https://pubmed.ncbi.nlm.nih.gov/7502646/) | 1995 | Review | AANA Journal | Case report of isoflurane anesthesia in a patient with manic-depressive psychosis; malignant hyperthermia differential diagnosis discussion |
| [18930636](https://pubmed.ncbi.nlm.nih.gov/18930636/) | 2008 | Review | Psychiatry Research | Animal model of mania using isoflurane-anesthetized rats with PET imaging of frontal glucose metabolism |

### Other Candidates (Prinzmetal angina, Tourette syndrome, trichotillomania, dysthymic disorder, nephrogenic SIAD)

Currently no related literature available for these indications.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-scoring TxGNN candidate (Prinzmetal angina) has no supporting clinical or literature evidence (L5), and isoflurane is not currently marketed in Taiwan, so no regulatory or safety baseline exists to build on. Two lower-ranked candidates — migraine disorder (L4) and manic bipolar affective disorder (L3) — have preclinical/mechanistic and case-report support and are appropriately flagged as **Research Questions (S1)** rather than ready for clinical evaluation.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (currently blocking — flagged as DG001)
- Confirmed mechanism-of-action data from DrugBank (flagged as DG002)
- Original indication and regulatory history, since isoflurane has no Taiwan license on record
- For migraine and bipolar mania candidates specifically: controlled studies (not just case reports/animal models) testing isoflurane or burst-suppression anesthesia against these indications before any Go/Guardrails decision
- Route-of-administration feasibility assessment — isoflurane is an inhalational anesthetic, which constrains its practical use for non-procedural chronic indications like dysthymic disorder or trichotillomania
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

