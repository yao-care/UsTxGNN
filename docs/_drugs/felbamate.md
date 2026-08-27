---
layout: default
title: Felbamate
parent: 僅模型預測 (L5)
nav_order: 695
evidence_level: L5
indication_count: 2
---

# Felbamate
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

# Felbamate: From Epilepsy to Trigeminal Neuralgia

## One-Sentence Summary

Felbamate is an antiepileptic drug (NMDA receptor antagonist / GABA-A potentiator) originally developed for seizure disorders. The TxGNN model predicts it may be effective for **Trigeminal Neuralgia**, currently supported by **5 publications** (no registered clinical trials) at evidence level **L4**.

*Note: TxGNN's top-ranked prediction, "trigeminal nerve neoplasm" (score 99.62%), carries no supporting evidence and no plausible antineoplastic mechanism — it is treated as likely model noise (possibly driven by the shared "trigeminal" keyword) and excluded from further evaluation in this report.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / seizure disorders (antiepileptic drug; no TFDA/market license text available in this data) |
| Predicted New Indication | Trigeminal Neuralgia |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L4 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action text is not available in this data pack (data gap DG002). Based on the information available, Felbamate is an antiepileptic drug that acts as an NMDA receptor antagonist and GABA-A receptor potentiator, a dual mechanism that dampens neuronal hyperexcitability.

Trigeminal neuralgia is characterized by paroxysmal, seizure-like hyperexcitability of trigeminal ganglion/brainstem neurons — a pathophysiology that already justifies the established use of several antiepileptics in this condition (carbamazepine is first-line; phenytoin, valproate, and baclofen are also used).

Mechanistically, Felbamate's NMDA antagonism and GABA-A enhancement could plausibly suppress this abnormal firing, following a similar anticonvulsant-as-analgesic logic to carbamazepine's sodium-channel blockade. However, this rationale is weaker than carbamazepine's validated mechanism, and the current evidence base is limited to a single case report and contextual reviews rather than controlled trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23338129](https://pubmed.ncbi.nlm.nih.gov/23338129/) | 1997 | Review | CNS Drugs | General guide to TN drug choice; carbamazepine is first-line, with baclofen, phenytoin, and valproate also effective — establishes anticonvulsant class rationale for TN. |
| [8877250](https://pubmed.ncbi.nlm.nih.gov/8877250/) | 1996 | Review (PK-DDI, non-felbamate specific) | Clinical Pharmacokinetics | Reviews carbamazepine pharmacokinetic drug interactions in its use for trigeminal neuralgia; provides interaction-risk context for the anticonvulsant drug class rather than felbamate-specific data. |
| [7549170](https://pubmed.ncbi.nlm.nih.gov/7549170/) | 1995 | Case Report | The Clinical Journal of Pain | Reports analgesic efficacy of felbamate specifically in a trigeminal neuralgia patient — the only direct felbamate efficacy evidence in this pack. |
| [7633024](https://pubmed.ncbi.nlm.nih.gov/7633024/) | 1995 | Case Report (Adverse Event) | The Annals of Pharmacotherapy | Reports felbamate-induced delayed anaphylaxis — a safety signal, not an efficacy finding. |
| [22022008](https://pubmed.ncbi.nlm.nih.gov/22022008/) | 2011 | Animal Study (rat; felbamate not tested) | Indian Journal of Pharmacology | Compares carbamazepine, gabapentin, and lamotrigine for neuropathic pain in rats; felbamate is mentioned only as background context, not tested. |

---

## Safety Considerations

Please refer to the package insert for safety information (TFDA warning/contraindication data and DDI records are not available in this pack — data gap DG001, blocking).

**Additional literature safety signal:** one case report describes felbamate-induced delayed anaphylaxis (PMID [7633024](https://pubmed.ncbi.nlm.nih.gov/7633024/)).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for trigeminal neuralgia is currently limited to a single case report plus contextual reviews of the anticonvulsant drug class (L4, no clinical trials) — mechanistically plausible but not yet actionable. The alternative TxGNN prediction (trigeminal nerve neoplasm) has no supporting evidence and is not being pursued.

**To proceed, the following is needed:**
- TFDA/product label data (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism-of-action detail from DrugBank (DG002)
- Controlled trial or larger case-series data specifically evaluating felbamate in trigeminal neuralgia
- Formal DDI dataset, given felbamate's known interactions within the antiepileptic drug class
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

