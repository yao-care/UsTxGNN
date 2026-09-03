---
layout: default
title: Rosuvastatin
parent: 僅模型預測 (L5)
nav_order: 1136
evidence_level: L5
indication_count: 10
---

# Rosuvastatin
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

# Rosuvastatin: From Undetermined Original Indication to Cholesterol-Ester Transfer Protein Deficiency

## One-Sentence Summary

The original indication and mechanism of action for Rosuvastatin are not documented in this evidence pack (market status: **Not Marketed**, 0 licenses on file). TxGNN's top-ranked prediction is **Cholesterol-Ester Transfer Protein (CETP) Deficiency**, but this candidate is supported by **0 clinical trials** and only **2 tangentially related case reports** — and the accompanying analyst rationale flags this specific prediction as a likely disease-ontology mapping artifact rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no licenses on file; MOA also undocumented) |
| Predicted New Indication | Cholesterol-Ester Transfer Protein Deficiency |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. What can be established from the literature attached to this candidate and from the broader evidence pack is that rosuvastatin is a **HMG-CoA reductase inhibitor** (statin class) that lowers LDL-cholesterol by upregulating hepatic LDL receptor expression.

This mechanism does **not** align well with CETP deficiency. CETP deficiency classically presents with **markedly elevated HDL-cholesterol**, not elevated LDL — the opposite lipid abnormality that statins are designed to treat. The directionality of rosuvastatin's known pharmacology therefore runs counter to the pathophysiology of this disease.

Furthermore, the two literature citations attached to this prediction do not actually discuss CETP deficiency: one describes a case of complete **Apo A-I deficiency**, and the other a case of **hepatic lipase deficiency** — both distinct genetic lipid disorders. Given the absence of on-target literature, the absence of any clinical trials, and the mechanistic direction mismatch, this prediction is most plausibly explained by a **disease ontology/terminology mapping error** in the underlying knowledge graph rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21122686](https://pubmed.ncbi.nlm.nih.gov/21122686/) | 2010 | Case report | Journal of Clinical Lipidology | Describes an Iraqi Mandaean family with complete **Apo A-I deficiency** (not CETP deficiency); discusses premature atherosclerosis phenotype. Not directly relevant to the predicted indication. |
| [22798447](https://pubmed.ncbi.nlm.nih.gov/22798447/) | 2010 | Case report | BMJ Case Reports | Describes **hepatic lipase deficiency** in a Middle-Eastern-Arabic male; reports CETP activity/mass as a secondary comparator, but the underlying disease is hepatic lipase deficiency, not CETP deficiency itself. |

---

## US Market Information

No marketing authorization (NDA) records are present in the evidence pack for this drug. Market status is recorded as **Not Marketed**, with 0 total licenses.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all marked as data gaps in this evidence pack — see DG001, "TFDA-equivalent label warnings/contraindications," flagged as **Blocking** for safety review.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This specific candidate (CETP deficiency) has no supporting clinical trials, only two off-target case reports, and a mechanistic direction that contradicts the known pathophysiology of the disease (HDL excess vs. LDL-lowering therapy). The evidence pack's own rationale identifies this as a likely ontology-mapping artifact rather than a credible repurposing signal.

**To proceed, the following is needed:**
- Confirm/correct the disease-entity mapping between TxGNN's "cholesterol-ester transfer protein deficiency" node and the clinical entity intended, before any further review of this specific candidate
- Resolve DG001 (TFDA/label warnings and contraindications — Blocking) via label PDF retrieval and parsing
- Resolve DG002 (mechanism of action) via DrugBank API query
- Obtain original indication and NDA/licensing data, since none is currently on file despite this being a globally marketed drug — this looks like a data collection gap rather than a true absence of market presence

---

### Note: Other Candidate Indications in This Evidence Pack

This evidence pack (`TW-DB01098-multi`) profiles 10 predicted indications for rosuvastatin. Several other candidates carry substantially stronger evidence than the top-ranked one above and may warrant separate evaluation:

| Rank | Disease | Score | Evidence Level | Recommendation |
|------|---------|-------|------|------|
| 2 | Familial hypercholesterolemia | 99.54% | L1 | Proceed with Guardrails |
| 10 | Hyperlipidemia | 99.09% | L1 | Proceed with Guardrails |
| 5 | HIV infectious disease (CV risk/inflammation management) | 99.37% | L2 | Proceed with Guardrails |
| 6 | Hypoalphalipoproteinemia | 99.25% | L3 | Research Question |
| 3 | Hypercholesterolemia due to CYP7A1 deficiency | 99.51% | L4 | Research Question |
| 4 | Brain stem infarction | 99.44% | L4 | Research Question |
| 1 | CETP deficiency (this report) | 99.54% | L5 | Hold |
| 7–9 | Rare neurodevelopmental/amyloidosis/lipase disorders | 99.18–99.22% | L5 | Hold |

Notably, ranks 2 and 10 (familial hypercholesterolemia, hyperlipidemia) are not truly novel repurposing candidates — they represent statin-class core/on-label use with extensive Phase 3 RCT support — but they confirm the model correctly recovers known indications. If a genuine repurposing report is desired, rank 5 (HIV-associated cardiovascular risk management) is the most credible "new use" signal, with a Phase 4 placebo-controlled RCT (NCT01813357) as direct supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

