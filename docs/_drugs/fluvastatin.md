---
layout: default
title: Fluvastatin
parent: 僅模型預測 (L5)
nav_order: 731
evidence_level: L5
indication_count: 10
---

# Fluvastatin
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

# Fluvastatin: From Hypercholesterolemia to Hyperlipoproteinemia

## One-Sentence Summary

Fluvastatin is an HMG-CoA reductase inhibitor (statin) established for treating hypercholesterolemia and hyperlipidemia. The TxGNN model's top prediction, **Hyperlipoproteinemia**, is supported by **5 clinical trials** and **20 publications** — but the pack's own mechanistic analysis flags this as an extension of fluvastatin's *existing* core indication rather than a true novel repurposing case. Critically, official Taiwan/US label data (warnings, contraindications) is a **blocking data gap**, so no safety pre-assessment can yet be completed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no TFDA/US license records; `original_indications` empty). Fluvastatin is broadly established in the literature as a statin for hypercholesterolemia/hyperlipidemia. |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (`original_moa`) is not available in this pack. Based on the repurposing rationale attached to the top prediction, fluvastatin is an HMG-CoA reductase inhibitor — it inhibits cholesterol synthesis and upregulates LDL receptor expression. This is stated explicitly to be the statin class's own core mechanism.

Importantly, the pack itself notes this prediction is **not a typical "old drug, new use" case** — hyperlipoproteinemia is essentially an extension/synonym of fluvastatin's already-established, direct indication rather than a novel therapeutic area. The mechanistic link is direct and well-characterized precisely because it reflects known statin pharmacology, not a speculative cross-disease connection.

By contrast, lower-ranked candidates in this pack (e.g., homozygous familial hypercholesterolemia, HIV infectious disease) represent more genuine repurposing hypotheses with weaker or more indirect mechanistic support — see the full candidate list below for comparison.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00726362](https://clinicaltrials.gov/study/NCT00726362) | N/A | Completed | 3270 | Large surveillance study comparing commercially available statins (incl. fluvastatin) in routine clinical practice for hyperlipidemia; statin-class effect validation |
| [NCT01634906](https://clinicaltrials.gov/study/NCT01634906) | N/A | Completed | 55 | Non-randomized study of erythrocyte-bound ApoB changes after statin withdrawal; statin-class relevant, not fluvastatin-specific RCT |
| [NCT00532311](https://clinicaltrials.gov/study/NCT00532311) | Phase 3 | Terminated | 411 | Lapaquistat acetate (not fluvastatin) added to statin background therapy in hypercholesterolemia; same lipid-lowering mechanism class only |
| [NCT04608474](https://clinicaltrials.gov/study/NCT04608474) | Phase 4 | Completed | 81 | PCSK9 inhibitor (evolocumab) pilot in renal transplant recipients with hyperlipidemia; not fluvastatin |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab in pediatric/adolescent homozygous FH; not fluvastatin |

**Note:** None of the trials above tested fluvastatin directly against hyperlipoproteinemia as a primary endpoint — evidence is class-level (statin/PCSK9i), not drug-specific for this exact indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10067240](https://pubmed.ncbi.nlm.nih.gov/10067240/) | 1998 | RCT | Terapevticheskii arkhiv | Compared hypolipidemic effect variability of simvastatin vs. fluvastatin in primary hyperlipoproteinemia |
| [10856536](https://pubmed.ncbi.nlm.nih.gov/10856536/) | 2000 | RCT | Atherosclerosis | FACT study: fluvastatin + bezafibrate combination efficacy/safety in mixed hyperlipidaemia (n=333) |
| [11219479](https://pubmed.ncbi.nlm.nih.gov/11219479/) | 2001 | RCT | Clinical Therapeutics | Compared fluvastatin extended-release vs. immediate-release formulations in primary hypercholesterolemia |
| [15598476](https://pubmed.ncbi.nlm.nih.gov/15598476/) | 2004 | RCT | Clinical Therapeutics | 12-month RCT: fluvastatin+fenofibrate vs. fluvastatin monotherapy in combined hyperlipidemia with T2DM and CHD |
| [17062478](https://pubmed.ncbi.nlm.nih.gov/17062478/) | 2006 | RCT | Acta Paediatrica | Efficacy/safety of fluvastatin in children/adolescents with heterozygous familial hypercholesterolaemia |
| [8157036](https://pubmed.ncbi.nlm.nih.gov/8157036/) | 1993 | RCT | European Journal of Clinical Pharmacology | Double-blind study of high-dose fluvastatin in familial hypercholesterolaemia (n=52) |
| [7604789](https://pubmed.ncbi.nlm.nih.gov/7604789/) | 1995 | Cohort | American Journal of Cardiology | Fluvastatin effects on lipid profile and apolipoproteins in Chinese hypercholesterolemia patients (n=31) |
| [9271817](https://pubmed.ncbi.nlm.nih.gov/9271817/) | 1997 | Cohort | Thrombosis Research | Fluvastatin and tissue factor pathway inhibitor in type IIA/IIB hyperlipidemia and acute MI |
| [11347136](https://pubmed.ncbi.nlm.nih.gov/11347136/) | 2001 | Review | Nihon Rinsho | General review of fluvastatin pharmacology and clinical use |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clinical Therapeutics | Review of rosuvastatin (comparator statin) in hyperlipidemia management |

---

## US Market Information

No license/authorization records are available — `taiwan_regulatory.total_licenses = 0` and `licenses` is empty, consistent with the recorded market status of **Not Marketed**.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and DDI data are all recorded as data gaps in this pack — notably DG001, a **Blocking**-severity gap on TFDA label warnings/contraindications, which prevents any safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence volume is strong (L1, 5 trials + 20 publications), but this strength comes from fluvastatin's already-established statin pharmacology rather than a genuinely novel indication — the mechanistic rationale itself states this is a direct extension, not typical repurposing. Separately, the drug is not currently marketed in the reference jurisdiction and has no license records, and safety data (warnings/contraindications) is a **Blocking** gap (DG001) that must be resolved before any S1 safety review can proceed.

**To proceed, the following is needed:**
- TFDA/US package insert warnings and contraindications (DG001 — Blocking)
- Confirmed mechanism of action documentation (DG002 — High)
- Official original-indication license text (currently absent from the pack)
- Fluvastatin-specific (not statin-class-general or comparator-drug) trial data directly targeting hyperlipoproteinemia, to confirm this is worth tracking as a distinct repurposing candidate rather than routine label extension
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

