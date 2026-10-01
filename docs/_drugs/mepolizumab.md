---
layout: default
title: Mepolizumab
parent: Moderate Evidence (L3-L4)
nav_order: 900
evidence_level: L4
indication_count: 5
---

# Mepolizumab
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Mepolizumab: From Anti-IL-5 Biologic (Nucala) to Thrombocytopenia Due to Immune Destruction

## One-Sentence Summary

Mepolizumab is an anti-IL-5 antibody that depletes eosinophils and is marketed in the US as Nucala.
The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**,
but only **1 case report** supports this and there are **no registered clinical trials**. The high score comes from graph-based prediction and is not clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 license entries (2 unique BLAs: BLA125526, BLA761122) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Mepolizumab is an anti-IL-5 antibody that depletes eosinophils. Detailed mechanism of action data is not available in the current dataset. The reasoning below rests on the antibody's known target.

The only link to immune-mediated low platelet counts is indirect. A benefit would most likely come from controlling eosinophil-driven immune dysregulation, not from any direct effect on platelet destruction. The single supporting paper is a case report of a steroid-resistant hypereosinophilic immune diathesis with a concomitant mixed thrombotic microangiopathy. The available excerpt does not confirm a platelet outcome or separate the effect of mepolizumab from other concomitant therapy.

The very high TxGNN score (0.997) reflects proximity in the knowledge graph. It should be treated as a research question, not as evidence of efficacy.

The other four predictions are weaker still:
- **Autoimmune thrombocytopenic** has a theoretical Th2/eosinophil rationale but no evidence. It overlaps the top prediction and is not independent support.
- **Primary release disorder of platelets** cites only a hypereosinophilic syndrome review that does not address platelet function.
- **Pseudo-von Willebrand disease** and **Glanzmann thrombasthenia** have no plausible link to IL-5 blockade and no trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Case report | Blood Cells Mol Dis | Mepolizumab resolved a steroid-resistant hypereosinophilic immune diathesis, with concomitant improvement of a mixed thrombotic microangiopathy. Platelet outcome is not confirmed in the available excerpt. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA125526 | Nucala | Injection, powder, for solution | GlaxoSmithKline LLC |
| BLA761122 | Nucala | Injection, solution | GlaxoSmithKline LLC |

The pack lists BLA761122 twice with identical details, so it appears once here. Approved indication text is not available in the dataset.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is one case report and no trials. The mechanistic link between IL-5 blockade and platelet destruction is indirect, and the prediction score alone cannot support development.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for each license, to establish the original indication
- Full-text review of PMID 28648630 to confirm the platelet outcome and any confounding therapy
- Any controlled or observational data on mepolizumab in immune thrombocytopenia, especially in patients with concurrent eosinophilia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

