---
layout: default
title: Prochlorperazine
parent: 僅模型預測 (L5)
nav_order: 1088
evidence_level: L5
indication_count: 10
---

# Prochlorperazine
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

# Prochlorperazine: From Antiemetic/Antipsychotic Use (Data Gap) to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

> Prochlorperazine is a phenothiazine dopamine D2 antagonist; its formal original indication could not be confirmed in this evidence pack, but its known pharmacological class is used for nausea/vomiting and psychosis/sedation.
> The TxGNN model assigns a very high score (**99.998%**) to **Retinal Dystrophy with or without Extraocular Anomalies**, but the model's own rationale flags this association as likely **spurious co-occurrence noise** — no clinical trials, and none of the associated literature actually discusses prochlorperazine.
> Evidence level is **L5 (model prediction only)** and the recommended decision is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no market license data; drug's pharmacological class is historically used as antiemetic/antipsychotic (dopamine D2 antagonist) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.998% (rank 138 of all candidates) |
| Evidence Level | L5 |
| Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for prochlorperazine is not available as a structured field (flagged as a High-severity data gap). Based on information embedded in the model's own reasoning output, prochlorperazine is a **phenothiazine-class dopamine D2 receptor antagonist**, traditionally used for **antiemetic and sedative/antipsychotic** purposes.

The top-ranked predicted indication — retinal dystrophy with or without extraocular anomalies — is a largely **congenital, genetically-driven retinal/ocular structural disorder**. There is no known pharmacological pathway by which a D2-antagonist antiemetic would influence retinal developmental biology or congenital extraocular structural anomalies. The evidence pack's own repurposing rationale explicitly states this is likely a **spurious knowledge-graph co-occurrence** rather than a genuine drug–disease relationship: the 14 associated publications are general ophthalmology reviews/case reports (orbital infections, diplopia, congenital ptosis, CFEOM, etc.) and **none of them mention prochlorperazine**.

Of note, a lower-ranked candidate in this evidence pack — **manic bipolar affective disorder** (rank 10, score 99.98%, evidence level L4) — has meaningfully stronger mechanistic plausibility: phenothiazines as a class were historically used for acute mania before modern antipsychotics existed, and one directly relevant case report (PMID 13617778) describes a confusional dream-like reaction specifically attributed to prochlorperazine in a patient with mild manic-depressive illness. This suggests the model's *overall signal quality* is mixed — some predictions reflect real pharmacology, while the top-ranked candidate here does not.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The following literature is linked to *retinal dystrophy with or without extraocular anomalies* in the evidence pack. None of these publications discuss prochlorperazine directly; they are general ophthalmology/genetics reviews and case reports retrieved via disease-term co-occurrence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Case Series | Int J Mol Sci | Optic nerve/retinal abnormalities in congenital fibrosis of extraocular muscles (CFEOM); no drug relevance |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging review of pediatric congenital ocular pathologies |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital anomalies of lens shape |
| [36892533](https://pubmed.ncbi.nlm.nih.gov/36892533/) | 2023 | pending | Invest Ophthalmol Vis Sci | MAB21L1 mutations causing autosomal dominant ocular BAMD syndrome (genetic, not pharmacologic) |
| [36116851](https://pubmed.ncbi.nlm.nih.gov/36116851/) | 2022 | pending | Semin Ultrasound CT MR | Anatomy/pathology review of the oculomotor nerve |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocul Vis Ocul Motil | Congenital cranial dysinnervation disorders |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | Am J Ophthalmol | Maculopathy associated with cavitary optic disc anomalies |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | pending | J Neuroophthalmol | Congenital trochlear-oculomotor synkinesis |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Congenital ptosis review |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Diplopia diagnostic approach |

---

## Market Information

The drug is currently **not marketed** under this evidence pack's regulatory jurisdiction — `total_licenses = 0`, no license records available. No dosage form or approved-indication data could be extracted.

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug interaction database) could not be retrieved for this evidence pack — flagged as a **Blocking-severity data gap (DG001)**: TFDA/local label warnings and contraindications require manual PDF retrieval and have not yet been completed. DDI query returned no results (`query_status: not_found`).

> Please refer to the official package insert for safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (retinal dystrophy with extraocular anomalies) has no clinical trials, no directly relevant literature, and the model's own rationale identifies it as likely spurious knowledge-graph noise rather than a genuine pharmacological signal — evidence level L5, decision stage S0. This candidate should not advance without independent mechanistic or preclinical justification.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: retrieve official label warnings/contraindications before any safety-relevant decision (S1) can be made
- Resolve data gap DG002: confirm mechanism of action and original approved indication(s) from DrugBank/regulatory source
- If pursuing further, consider re-scoping toward the **manic bipolar affective disorder** candidate (rank 10, L4, S1 "Research Question"), which has class-level mechanistic plausibility and at least one drug-specific case report, rather than the top-ranked but mechanistically unsupported ophthalmologic candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

