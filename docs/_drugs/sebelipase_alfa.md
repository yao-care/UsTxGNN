---
layout: default
title: Sebelipase Alfa
parent: 僅模型預測 (L5)
nav_order: 1146
evidence_level: L5
indication_count: 10
---

# Sebelipase Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Sebelipase Alfa: From Lysosomal Acid Lipase Deficiency to Scheie Syndrome

## One-Sentence Summary

> Sebelipase alfa is a recombinant human lysosomal acid lipase (rhLAL) enzyme replacement therapy, established in the literature for treating Lysosomal Acid Lipase Deficiency (LAL-D, covering both the infantile Wolman disease and later-onset cholesteryl ester storage disease phenotypes).
> The TxGNN model's top-ranked prediction is **Scheie syndrome**, a subtype of mucopolysaccharidosis I (MPS I).
> Currently there are **no clinical trials and no published literature** directly supporting this specific prediction — it rests entirely on knowledge-graph embedding similarity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lysosomal Acid Lipase Deficiency (LAL-D) — established per accompanying literature evidence (e.g., PMID 26452566, 35442238); not recorded in the local regulatory license dataset, as the drug is currently unmarketed in this dataset |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the regulatory dataset. Based on the literature evidence attached to this candidate pool (e.g., PMID 26452566 "Sebelipase alfa: first global approval"), sebelipase alfa is a recombinant human lysosomal acid lipase (rhLAL) administered by intravenous infusion, which acts to replace the deficient LAL enzyme and reduce lysosomal lipid (cholesteryl ester and triglyceride) accumulation. Its efficacy has been proven in Lysosomal Acid Lipase Deficiency (LAL-D), spanning both the rapidly progressive infantile-onset form (Wolman disease) and the attenuated later-onset form (cholesteryl ester storage disease), through multiple completed Phase 2/3 trials documented elsewhere in this evidence pack.

Scheie syndrome, however, is the attenuated form of mucopolysaccharidosis type I (MPS I), caused by deficiency of α-L-iduronidase (IDUA) — a different lysosomal enzyme acting on glycosaminoglycan degradation, not lipid metabolism. The connection between the two conditions is therefore at the *category* level only: both are lysosomal storage diseases treatable in principle by the enzyme replacement therapy (ERT) paradigm, and both share adjacency in the TxGNN knowledge graph through "lysosomal storage disease" and "enzyme replacement therapy" node relationships. This is a mechanistically plausible *class-level* analogy, but there is no evidence that sebelipase alfa's substrate specificity (cholesteryl esters/triglycerides) extends to glycosaminoglycan clearance relevant to MPS I. No clinical trial or publication in this evidence pack directly investigates sebelipase alfa in Scheie syndrome or MPS I patients.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No marketing authorization records are available for sebelipase alfa in this dataset — the drug is recorded as **Not Marketed** with **0 licenses** on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a rank-1 TxGNN output (99.80% embedding similarity), but it is supported by zero clinical trials and zero publications, and the underlying enzyme mechanism (LAL vs. IDUA) does not directly overlap with Scheie syndrome's pathophysiology. This meets the L5 criterion (model prediction only, no actual studies) and does not currently warrant progression.

**To proceed, the following is needed:**
- Preclinical/mechanistic data establishing any functional relevance of LAL activity to glycosaminoglycan accumulation or MPS I pathways
- Confirmed mechanism of action (MOA) and full prescribing information (currently flagged as blocking data gaps — DG001, DG002)
- Verified US regulatory/marketing status, since the current dataset shows the product as unmarketed despite known global approval as Kanuma
- Any hypothesis-generating case reports, registry data, or in vitro/animal studies specifically linking sebelipase alfa exposure to MPS I disease markers before considering trial design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

