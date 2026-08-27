---
layout: default
title: Enfortumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 653
evidence_level: L5
indication_count: 9
---

# Enfortumab Vedotin
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

# Enfortumab Vedotin: From Urothelial Carcinoma to Leprosy

## One-Sentence Summary

Enfortumab vedotin is an antibody-drug conjugate (ADC) that targets Nectin-4-expressing tumour cells, used mainly in advanced urothelial carcinoma. The TxGNN model's top prediction for this drug is **Leprosy**, but this candidate is supported by **0 clinical trials** and **0 publications**, and the mechanistic rationale itself flags the prediction as likely embedding-similarity noise rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this evidence pack (no Taiwan licenses on file); background mechanistic notes describe use in Nectin-4-high urothelial carcinoma |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not marketed (Taiwan: 未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for enfortumab vedotin is currently a data gap (DG002, High severity) in this evidence pack. Based on the mechanistic notes attached to this candidate, enfortumab vedotin is an ADC combining an anti-Nectin-4 monoclonal antibody with MMAE, a microtubule inhibitor payload; it kills Nectin-4-high-expressing cells, a profile seen predominantly in urothelial cancer.

Leprosy (Hansen's disease) is a chronic mycobacterial infection driven by *Mycobacterium leprae* and host granulomatous/immune pathology — a disease biology entirely unrelated to Nectin-4 expression or microtubule-dependent cell killing. The evidence pack's own rationale is explicit on this point: there is **no known mechanistic relationship** between the drug's ADC/cytotoxic mode of action and leprosy pathophysiology, and the TxGNN score is assessed as most likely reflecting embedding similarity noise rather than a real pharmacological signal.

No clinical trials, literature, or regulatory precedent support this pairing. Given the absence of any corroborating evidence and a rationale that itself argues against biological plausibility, this candidate should not be interpreted as a credible repurposing signal at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No Taiwan (TFDA) authorizations are on file for this drug — 0 licenses recorded, market status "未上市" (not marketed).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Antibody-drug conjugate; MMAE microtubule-inhibitor payload) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Cytotoxic ADC — standard hazardous drug handling precautions expected, pending confirmation from official labeling |

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA label warnings/contraindications and DDI data are currently unavailable (DG001, Blocking severity — required before any S1 safety pre-assessment can proceed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (leprosy) has no clinical, literature, or regulatory support, and the attached mechanistic rationale itself concludes there is no plausible biological link between the drug's ADC/cytotoxic mechanism and the predicted indication — most consistent with model noise rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) to close the Blocking data gap (DG001)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- A documented original indication/regulatory history for this drug in the target market
- Independent mechanistic or preclinical evidence specifically linking Nectin-4/MMAE biology to leprosy before any further evaluation is warranted

*Note: All 9 predicted indications for this drug carry evidence level L5 (no clinical trials, minimal/no literature). Two lower-ranked candidates (malignant catarrh, infectious bovine rhinotracheitis) are veterinary-only conditions, indicating a likely disease-ontology species mismatch in this candidate set — a data-quality signal worth flagging for the broader prediction batch, not just this report.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

