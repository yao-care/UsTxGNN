---
layout: default
title: Desmopressin
parent: 僅模型預測 (L5)
nav_order: 586
evidence_level: L5
indication_count: 7
---

# Desmopressin
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

# Desmopressin: From Hemostatic Disorders to Congenital Prothrombin Deficiency

## One-Sentence Summary

Desmopressin (DDAVP) is a synthetic vasopressin analog with established hemostatic applications — including mild hemophilia A, von Willebrand disease Type 1, and uremic bleeding — that works by releasing stored von Willebrand Factor (vWF) and Factor VIII from vascular endothelium.

The TxGNN model's top-ranked prediction is **Congenital Prothrombin Deficiency** (score: 99.70%), yet this specific target has **no supporting clinical trials** and **no directly relevant literature**, with the high score most likely reflecting non-specific hemorrhagic disease node clustering in the knowledge graph rather than a true pharmacological relationship.

Critically, while Rank 4 (**Primary Release Disorder of Platelets**, L3 evidence) represents the most mechanistically plausible repurposing opportunity within this evidence pack, Ranks 2 and 5 (**Inherited Thrombophilia** and **Pseudo-von Willebrand Disease**) are potential **contraindications** where desmopressin administration could cause active harm.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Central diabetes insipidus; mild hemophilia A; von Willebrand disease Type 1 |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| US Market Status | Not found in registry (0 active authorizations) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Desmopressin acts on V2 receptors on vascular endothelial cells, triggering the release of pre-formed von Willebrand Factor multimers — including ultra-large multimers (ULvWF) — from Weibel-Palade bodies, while simultaneously raising circulating Factor VIII (FVIII) levels 2–5-fold. The net result is enhanced platelet adhesion (via GPIb–vWF interaction) and improved coagulation factor availability, shortening bleeding time. This mechanism is effective where the vWF–FVIII axis is rate-limiting for hemostasis, as in mild hemophilia A and VWD Type 1.

Congenital prothrombin deficiency (Factor II deficiency), however, is a rare autosomal recessive disorder affecting the common and extrinsic coagulation pathways. Factor II (prothrombin) is converted to thrombin by Factor Xa within the prothrombinase complex — a step that occurs entirely downstream of both vWF-mediated platelet plug formation and Factor VIII activity. Desmopressin's mechanism does not interact with the Factor II pathway, nor does it upregulate Factor II synthesis or activity. There is no established mechanistic bridge between these two.

The evidence pack's own repurposing rationale identifies this as a likely false positive: TxGNN's knowledge graph may cluster hemorrhagic disease nodes non-specifically, generating high scores for coagulopathies regardless of whether the drug's mechanism overlaps with the disease pathway. This is a recognized limitation of graph-based prediction models applied to rare disorders with sparse training data. The complete absence of trials and direct literature evidence for this specific combination corroborates that interpretation.

---

## Clinical Trial Evidence

Currently no related clinical trials for Desmopressin in congenital prothrombin deficiency are registered.

> One trial was retrieved during the evidence search (NCT04567511, Phase 4, Recruiting, n=20), but it was rated **Grade C — Irrelevant**: the study drug is Emicizumab, the target population is mild hemophilia A, and there is no connection to either Desmopressin or prothrombin deficiency. It is treated as background noise.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Review | *Drugs* | Rational treatment options for inherited bleeding disorders; confirms DDAVP efficacy in mild hemophilia A and VWD; no data on Factor II deficiency |
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | *Autoimmunity Reviews* | Acquired hemophilia A due to anti-FVIII autoantibodies; clinically and mechanistically distinct from congenital prothrombin deficiency |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case Report | *Rinsho Ketsueki* | DDAVP administered in a patient with combined Factor V + Factor VIII deficiency — a different coagulopathy from Factor II deficiency; partial contextual relevance only |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case Report | *Rinsho Ketsueki* | Cesarean section management in combined Factor V + VIII deficiency; Factor VIII concentrates used as mainstay; desmopressin not directly applicable to Factor II deficiency |

> **Assessment**: All four publications address FVIII-related or combined coagulopathies. None directly study or support Desmopressin use in Factor II (prothrombin) deficiency. This literature set constitutes background context, not evidence.

---

## Safety Considerations

Formal package insert warnings and contraindications were not retrieved by the data pipeline. Based on the evidence pack's mechanistic analysis, the following safety signals are identified:

- **⚠️ Potential Contraindication — Inherited Thrombophilia (Rank 2)**: Desmopressin-induced ULvWF release enhances platelet aggregation and may significantly increase thrombotic risk in patients with inherited thrombophilias (e.g., Factor V Leiden, Prothrombin G20210A mutation). PMID 16460464 documents an unexpected and dangerous link between desmopressin and inherited thrombotic thrombocytopenic purpura (Upshaw-Schulman syndrome). This predicted indication points toward risk, not benefit.

- **⚠️ Potential Contraindication — Pseudo-von Willebrand Disease (Rank 5)**: Platelet-type VWD (pseudo-VWD) involves gain-of-function GPIbα mutations causing abnormally high platelet–vWF affinity. Desmopressin administration would flood circulation with ULvWF multimers, accelerating pathological platelet capture and clearance — potentially worsening thrombocytopenia and precipitating thrombotic microangiopathy. PMID 27819553 explicitly highlights the diagnostic and therapeutic challenges in PT-VWD where standard VWD therapies including desmopressin must be used with extreme caution or avoided.

- **General known safety concerns** include: hyponatremia (especially in children and elderly patients receiving concurrent hypotonic fluids), fluid retention, tachyphylaxis with repeated dosing, and rare arterial thrombotic events — per the 2023 systematic review (PMID 36656570, cited under Rank 4 evidence).

---

## Conclusion and Next Steps

**Decision: Hold** (for Rank 1 — Congenital Prothrombin Deficiency)

**Rationale:**
There is no mechanistic plausibility, no clinical trial, and no directly relevant literature linking Desmopressin to congenital prothrombin deficiency. The TxGNN high score (99.70%) is attributed to non-specific hemorrhagic disease clustering in the knowledge graph rather than true pharmacological prediction. The evidence pack scores this at L5 and Stage S0 — the lowest evidence tier, requiring a hold before any further investment. Furthermore, two other top-ranked predictions (Ranks 2 and 5) carry active contraindication signals, which constrains the overall repurposing profile and warrants caution in any expansion strategy.

**Higher-Priority Signal Within This Evidence Pack:**
Rank 4 — **Primary Release Disorder of Platelets** — carries the strongest evidence (L3, Stage S2, Proceed with Guardrails), supported by a 2023 systematic review (PMID 36656570) and a prospective pediatric clinical study (PMID 21509710). This indication has a coherent mechanistic link (desmopressin's ULvWF release compensates for δ-granule ADP deficiency via GPIb-dependent adhesion reinforcement) and should be evaluated as the primary repurposing target.

**To advance this evidence pack, the following is needed:**

- **Blocking — Safety data**: Retrieve and parse FDA/TFDA package insert (DG001, Severity: Blocking) to complete S1 safety evaluation; all Stage S1+ indications are blocked until resolved
- **Mechanistic gap**: Confirm whether any pharmacological interaction between desmopressin and the Factor II (prothrombin) pathway exists; if none, formally close Rank 1 and reallocate resources
- **Contraindication documentation**: Formally document Ranks 2 and 5 as contraindications in the drug's repurposing safety profile to prevent inadvertent inclusion in future indication screening
- **Rank 4 next step**: Design a hemostatic biomarker study (DDAVP response testing via PFA-100 or ROTEM) in pediatric patients with aspirin-like platelet defects and δ-storage pool disease to generate prospective L2 evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

