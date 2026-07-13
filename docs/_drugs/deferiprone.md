---
layout: default
title: Deferiprone
parent: 僅模型預測 (L5)
nav_order: 578
evidence_level: L5
indication_count: 9
---

# Deferiprone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Deferiprone: From Thalassemia Iron Overload to Hepatic Porphyria

## One-Sentence Summary

Deferiprone (Ferriprox) is an oral iron chelator with documented FDA and EMA approval for managing iron overload in transfusion-dependent thalassemia major — though it does not appear in the current US regulatory dataset, likely due to a data collection gap.
The TxGNN model predicts it may also be effective for **Hepatic Porphyria**,
with **0 clinical trials** and **2 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron overload in transfusion-dependent thalassemia major (FDA/EMA approved; absent from current dataset — data gap) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L4 |
| US Market Status | Not found in dataset (known FDA approval: Ferriprox, 2011 — data gap) |
| Number of NDAs | 0 (data gap) |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack (flagged as a high-severity data gap). Based on established pharmacology, deferiprone is a bidentate oral iron chelator that binds ferric iron (Fe³⁺) with high affinity and excretes the resulting complex predominantly via urine. Its unusually small molecular weight allows it to cross cell membranes and mobilize intracellular iron deposits — a property that distinguishes it from other chelators such as deferoxamine and makes it particularly effective at removing cardiac iron in thalassemia patients.

In hepatic porphyria — specifically Porphyria Cutanea Tarda (PCT) and Congenital Erythropoietic Porphyria (CEP) — hepatic iron overload functions as a key pathological trigger. Excess iron catalyzes oxidative reactions that drive the accumulation of uroporphyrin and other phototoxic porphyrin isomers. This iron-porphyrin link is so well established that phlebotomy (iron depletion via bloodletting) is the standard first-line treatment for PCT, directly validating iron removal as a therapeutic strategy. An oral iron chelator such as deferiprone provides a pharmacological route to the same endpoint, and two preclinical studies — detailed below — have already demonstrated this in animal models.

It is critical to note that this mechanistic logic applies only to iron-overload-driven porphyria subtypes (PCT, CEP). For acute hepatic porphyrias such as Acute Intermittent Porphyria (AIP), where the pathology is driven by enzyme dysfunction and ALA/PBG accumulation rather than iron excess, deferiprone would lack direct mechanistic rationale. The TxGNN prediction likely reflects clustering around the shared liver-iron-porphyrin metabolic node in the knowledge graph, making PCT and CEP the clinically meaningful targets for follow-up investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32678895](https://pubmed.ncbi.nlm.nih.gov/32678895/) | 2020 | Preclinical/Case | *Blood* | Iron chelation rescued both hemolytic anemia and skin photosensitivity in a mouse model of congenital erythropoietic porphyria (CEP), directly supporting iron removal as a viable therapeutic strategy for porphyrin-accumulation disorders. |
| [17854053](https://pubmed.ncbi.nlm.nih.gov/17854053/) | 2007 | Animal Model | *Hepatology* | Deferiprone (L1) reduced hepatic uroporphyrin accumulation in Hfe⁻/⁻ mice treated with ALA (a PCT model), performing comparably to iron-deficient diet. Demonstrated that oral iron chelation can substitute for dietary iron restriction in reducing hepatic porphyrin load. |

---

## US Market Information

No US FDA authorization records were retrieved for deferiprone in the current dataset.

> **Data Gap Notice**: The repurposing rationale documented in this Evidence Pack explicitly references FDA approval (2011) and EMA approval of Deferiprone (Ferriprox) for transfusion-dependent thalassemia major. The absence of NDA records reflects a data collection failure, not actual non-approval. Verified authorization details should be retrieved directly from [FDA Drugs@FDA](https://www.accessdata.fda.gov/scripts/cder/daf/) before clinical development decisions are made.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Evidence is currently limited to two preclinical and animal model studies (Evidence Level L4) with no registered clinical trials. The mechanistic link between deferiprone's iron-chelating activity and hepatic porphyria pathology is biologically coherent and supported by animal data, but remains entirely unvalidated in human patients. This warrants a targeted research effort before committing to formal drug development.

**To proceed, the following is needed:**
- Retrieve deferiprone's full MOA and toxicity profile from DrugBank (DG002 remediation) and FDA package insert for Ferriprox (DG001 remediation — currently blocking S1 safety review)
- Narrow the clinical target: distinguish PCT and CEP (mechanistically supported) from AIP and other acute porphyrias (mechanistically unsupported) — the current ICD term "hepatic porphyria" is too broad to guide development
- Conduct a broader literature search for PCT + iron chelation ± oral chelator in human cohort or pilot study designs, particularly in patients unable to tolerate phlebotomy
- Verify US FDA NDA records for Ferriprox to understand the existing regulatory framework, safety precedents, and labeled contraindications
- Identify a natural target population: PCT patients with contraindications to phlebotomy (e.g., severe anemia, poor venous access) could serve as a proof-of-concept cohort with minimal additional safety burden given deferiprone's established human use in thalassemia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

