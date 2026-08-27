---
layout: default
title: Fremanezumab
parent: 僅模型預測 (L5)
nav_order: 741
evidence_level: L5
indication_count: 2
---

# Fremanezumab
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

# Fremanezumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Fremanezumab is a fully humanized anti-CGRP monoclonal antibody used as a preventive treatment for episodic and chronic migraine. The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** (basilar-type migraine), with a prediction score of **99.94%**, though **no clinical trials** and only preclinical/observational literature currently support this specific subtype. This is presently a research-stage hypothesis rather than a clinically validated indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine prevention (episodic/chronic migraine) — per literature evidence; no Taiwan-approved label text available (drug not marketed) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 (preclinical / mechanism studies) |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fremanezumab is a monoclonal antibody that selectively binds and neutralizes calcitonin gene-related peptide (CGRP), a neuropeptide central to migraine pathophysiology. Preclinical work shows fremanezumab selectively inhibits trigeminovascular neurons and, when able to cross a compromised blood-brain barrier, slows the propagation and shortens the cortical recovery period of cortical spreading depression (CSD) — the electrophysiological event believed to underlie migraine aura.

Migraine with brainstem aura (basilar-type migraine) is a specific aura subtype for which triptans are traditionally avoided due to theoretical vasoconstrictive risk. Because anti-CGRP monoclonal antibodies act through a non-vasoconstrictive mechanism, they are mechanistically attractive for this subtype. However, patients with brainstem aura and related subtypes (e.g., hemiplegic migraine) are systematically excluded from the pivotal Phase 3 RCTs that established fremanezumab's efficacy, so this rationale remains mechanistic and extrapolated rather than directly confirmed. Notably, one preclinical study found fremanezumab did *not* block CSD-induced arterial dilatation or plasma protein extravasation, indicating the mechanism-to-outcome link for aura specifically is not fully established.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Case Report/Review | J Clin Med | Reviews case reports on anti-CGRP mAbs (incl. fremanezumab) for migraine aura prevention; suggests possible benefit but evidence remains limited |
| [41618146](https://pubmed.ncbi.nlm.nih.gov/41618146/) | 2026 | Cohort (individual patient analysis) | J Headache Pain | Individual patient data analysis of anti-CGRP mAbs in hemiplegic migraine (an aura subtype); reports effectiveness/safety despite systematic RCT exclusion of this population |
| [40264646](https://pubmed.ncbi.nlm.nih.gov/40264646/) | 2025 | Case Report/Review | Front Neurol | Case report plus literature review on anti-CGRP mAb efficacy in hemiplegic migraine, a rare aura subtype largely unstudied in RCTs |
| [38332541](https://pubmed.ncbi.nlm.nih.gov/38332541/) | 2024 | Observational case series | CNS Neurosci Ther | Observational case series on anti-CGRP-targeted therapy's effect specifically on migraine aura symptoms |
| [35302681](https://pubmed.ncbi.nlm.nih.gov/35302681/) | 2022 | Cohort (real-world, post hoc) | Eur J Neurol | Post hoc analysis of the fremanezumab FOCUS study; efficacy/QoL improvements maintained in patients with and without aura or neurological dysfunction |
| [31127003](https://pubmed.ncbi.nlm.nih.gov/31127003/) | 2019 | Preclinical (animal) | J Neurosci | Fremanezumab did not block CSD-induced arterial dilatation/plasma protein extravasation, raising questions about CGRP's specific role in migraine-with-aura pathophysiology |
| [31895266](https://pubmed.ncbi.nlm.nih.gov/31895266/) | 2020 | Preclinical (animal) | Pain | Fremanezumab (with compromised BBB) slowed CSD propagation and shortened cortical recovery but did not prevent CSD occurrence — the electrophysiological correlate of aura |
| [28642283](https://pubmed.ncbi.nlm.nih.gov/28642283/) | 2017 | Preclinical (mechanism) | J Neurosci | Foundational study showing fremanezumab selectively inhibits trigeminovascular neurons via peripheral CGRP blockade |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | Handb Exp Pharmacol | Review of CGRP's central role in migraine pathophysiology, including the aura subgroup |
| [37638190](https://pubmed.ncbi.nlm.nih.gov/37638190/) | 2023 | Cohort (real-world) | Front Neurol | 3-month prospective real-world study confirms fremanezumab efficacy/tolerability in chronic migraine (general population, not aura-specific) |

---

## Safety Considerations

Detailed warnings, contraindications, and drug-interaction data are not yet available in this evidence pack — fremanezumab is not currently marketed in Taiwan, and the TFDA label lookup returned no data (flagged as a Blocking data gap). Please refer to the manufacturer's package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (CGRP blockade acting on the CSD pathway underlying aura) is plausible, but current support comes only from preclinical/mechanism studies and post hoc subgroup analyses of general migraine populations — no trial or study specifically targets migraine with brainstem aura, a subtype systematically excluded from pivotal RCTs. The drug is also not marketed in Taiwan, and TFDA safety-label data required for an initial safety screen (S1) is currently a Blocking gap.

**To proceed, the following is needed:**
- TFDA (or manufacturer) approved package insert with warnings/contraindications, to clear the Blocking data gap and enable S1 safety review
- Structured DrugBank MOA data to formally document the mechanism-of-action linkage
- Prospective evidence (case series or trials) specifically enrolling migraine-with-brainstem-aura or hemiplegic migraine patients
- Confirmation of Taiwan regulatory/market entry status for fremanezumab
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

