---
layout: default
title: Mepivacaine
parent: Model Prediction Only (L5)
nav_order: 899
evidence_level: L5
indication_count: 2
---

# Mepivacaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Mepivacaine: From Local Anesthesia to Gastroduodenitis

## One-Sentence Summary

Mepivacaine is an amide-type local anesthetic, administered by injection.
The TxGNN model predicts it may be effective for **gastroduodenitis**, but **no clinical trials** and **no relevant publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available US license data (the approved indication text is empty) |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 6 (all ANDA, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacological knowledge, mepivacaine is an amide-type local anesthetic that blocks voltage-gated sodium channels. This information is not confirmed by the data compiled for this report.

The relationship between its anesthetic use and gastroduodenitis is not established. One plausible but unverified idea is an anti-nociceptive effect on visceral afferent nerves, or an effect on mucosal inflammation. Neither is supported by evidence here. The TxGNN score is a computational prediction only and should not be read as proof of efficacy.

A second predicted indication, peptic ulcer disease (score 99.41%), also has no supporting evidence. Sodium channel blockade has no established role in ulcer healing or acid suppression.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for gastroduodenitis.

For the second predicted indication, peptic ulcer disease, one publication was retrieved ([PMID 6890367](https://pubmed.ncbi.nlm.nih.gov/6890367/), 1982, *Arzneimittel-Forschung*). It is an animal safety pharmacology study of lofexidine, a different drug, and does not address mepivacaine. It is most likely a spurious match and is not counted as supporting evidence.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA089406 | Polocaine-MPF (Mepivacaine HCl), HF Acquisition Co (HealthFirst) | Injection, solution | Not listed (cancelled) |
| ANDA088387 | Mepivacaine, Benco Dental | Injection, solution | Not listed (cancelled) |
| ANDA089410 | Polocaine, Fresenius Kabi USA | Injection, solution | Not listed (cancelled) |
| ANDA089409 | Polocaine-MPF, Fresenius Kabi USA | Injection, solution | Not listed (cancelled) |
| ANDA089407 | Polocaine, Fresenius Kabi USA | Injection, solution | Not listed (cancelled) |

One further license (ANDA089408, Polocaine-MPF, Fresenius Kabi USA) is also cancelled. All six licenses are cancelled, so there is no currently valid US authorization in these records.

## Safety Considerations

- **Drug Interactions**: 11 interactions were identified. Ten are Moderate and one is Minor. Most involve other local anesthetics, which suggests additive effects.
  - Moderate: liposomal morphine, topical lidocaine, topical benzocaine, ophthalmic lidocaine, topical and nasal cocaine, ophthalmic tetracaine, ophthalmic oxybuprocaine, topical cinchocaine, topical tetracaine.
  - Minor: hyaluronidase.
- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text): kidney disease, pyoureter, liver disease, gallbladder disease, myasthenia gravis (including adult-onset), neuromuscular junction disease, butyrylcholinesterase deficiency, cardiovascular disease, and heart disease. These need to be checked against the official package insert.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score, with no clinical trials and no relevant literature (Evidence Level L5). The drug also has no currently valid US license, and its mechanism and label safety data are missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- A literature and trial search specific to mepivacaine in gastroduodenitis and peptic ulcer disease
- A clear mechanistic rationale and route compatibility assessment (injectable form versus the GI target)
- Review of the regulatory status, given that all licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

