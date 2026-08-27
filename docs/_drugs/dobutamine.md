---
layout: default
title: Dobutamine
parent: 僅模型預測 (L5)
nav_order: 616
evidence_level: L5
indication_count: 10
---

# Dobutamine
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

# Dobutamine: From Cardiac Inotropic Support to Alopecia

## One-Sentence Summary

Dobutamine is a short-acting intravenous β1-adrenergic agonist historically used for cardiac inotropic/hemodynamic support; this project's structured records on its original approved indication and mechanism of action are currently gapped. The TxGNN model predicts a possible new application in **Alopecia**, but the supporting evidence is minimal — **0 clinical trials** and only **2 tangentially related case reports**, with the evidence pack itself flagging the prediction as a likely knowledge-graph artifact rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — no Taiwan/US license on file (0 licenses). Narrative evidence in this pack describes dobutamine generically as a β1-agonist used for myocardial contractile/hemodynamic support, but a formally confirmed indication text is unavailable (data gap, see DG002). |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for dobutamine in this evidence pack (DG002, severity: High). Based on the information that is present — drawn from the model's own repurposing rationale and the associated literature — dobutamine acts as a β1-adrenergic agonist that increases myocardial contractility, and it appears clinically in this pack's supporting literature in the context of acute heart failure management and dobutamine-stress echocardiography, not dermatology.

There is no established pharmacological pathway connecting β1-adrenergic myocardial stimulation to hair follicle biology, the androgen/prostaglandin signaling implicated in alopecia, or any known hair-growth mechanism. The evidence pack's own analysis is explicit on this point: it assesses the high TxGNN score as most likely arising from **knowledge-graph node proximity** — dobutamine sitting near other cardiovascular-adjacent drugs such as minoxidil (a drug with a *bona fide* alopecia indication) in the embedding space — rather than from any genuine shared biological mechanism. This is a textbook example of a plausible-looking but mechanistically unsupported TxGNN prediction, and it should be treated as such.

Given both the absence of a confirmed original indication in the structured record and the absence of any mechanistic rationale for the new indication, this candidate does not currently meet the bar for further pharmacological justification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Case Report (Veterinary) | Journal of Veterinary Cardiology | Describes a cat with congestive heart failure where dobutamine was used for hypotension management; no hair-loss/alopecia outcome is reported — the link to alopecia is not substantive. |
| [17505274](https://pubmed.ncbi.nlm.nih.gov/17505274/) | 2007 | Case Report | Pediatric Emergency Care | Reports acute **colchicine** (not dobutamine) intoxication in a child, noting hair loss during the recovery phase of colchicine poisoning; dobutamine is not the study drug and this record appears to be a mismatched/indirect literature association. |

**Note:** Neither publication provides direct evidence of dobutamine being used for, or effective against, alopecia. Both entries are marked "relevance: pending" in the source data and should be treated as low-quality, indirect matches rather than supportive evidence.

---

## US Market Information

Dobutamine currently holds no market authorization on record for this jurisdiction — market status is "Not Marketed" with 0 total licenses. No product/dosage-form table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug-drug interaction data are all currently gapped in this evidence pack — DG001, severity: Blocking, prevents this candidate from entering the S1 safety pre-screening stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted alopecia indication has no supporting clinical trials, only two low-relevance case reports (neither demonstrating a therapeutic effect on hair loss), and the evidence pack's own rationale identifies the high TxGNN score as a probable knowledge-graph confounding artifact (proximity to minoxidil) rather than a real mechanistic signal. Evidence level is L5 — essentially model prediction only.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/product label warnings and contraindications to enable S1 safety pre-screening.
- Resolve DG002 (High): confirm dobutamine's formal mechanism of action via DrugBank API to properly evaluate mechanistic plausibility.
- Establish a confirmed original/approved indication record, since none currently exists in the regulatory dataset (0 licenses, not marketed).
- If this candidate is to be pursued further despite the weak signal, independent preclinical or mechanistic evidence linking β1-adrenergic agonism to hair follicle biology would be required before any clinical hypothesis is credible.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

