---
layout: default
title: Panitumumab
parent: Model Prediction Only (L5)
nav_order: 1012
evidence_level: L5
indication_count: 2
---

# Panitumumab
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

# Panitumumab: From Metastatic Colorectal Cancer to Drug-Induced Osteoporosis

## One-Sentence Summary

Panitumumab is a fully human anti-EGFR monoclonal antibody, originally used to treat metastatic colon cancer.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic malignant neoplasm in the colon |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.13% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single BLA is cancelled) |
| Number of NDAs | 1 (BLA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, panitumumab is a fully human monoclonal antibody that targets EGFR, and its efficacy in metastatic colon cancer is the basis of its original indication. Whether this mechanism applies to drug-induced osteoporosis is not established by the data compiled for this report.

EGFR signaling takes part in bone remodeling, including osteoblast differentiation and osteoclast regulation, so a biological connection is plausible in principle. However, EGFR inhibition has been associated with low magnesium and low calcium levels, which could harm bone rather than help it. This points toward a risk, not a benefit. The idea is a hypothesis only, and no data support it. The high TxGNN score (0.991) cannot be checked against a known mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125147 | Vectibix (Amgen Inc) | Solution | Not listed; license status: cancelled |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-EGFR monoclonal antibody) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions. Because EGFR inhibition is associated with low magnesium and calcium, electrolytes are a reasonable item to monitor. |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

**Drug Interactions:** The interaction screen returned 27 records in total. The 20 shown in the compiled data include these main ones:
- **Major:** amiodarone, arsenic trioxide, bevacizumab, dofetilide, dronedarone, droperidol, aminolevulinic acid, irinotecan (including liposomal), levacetylmethadol
- **Moderate:** proton pump inhibitors (rabeprazole, omeprazole, dexlansoprazole, esomeprazole, lansoprazole, pantoprazole), methoxsalen, topical aminolevulinic acid, disopyramide, idelalisib

Several of the major interactions involve drugs that affect heart rhythm (QT prolongation).

Other safety considerations from the mechanism: EGFR inhibitors are known to cause low magnesium and calcium levels, which could be unfavourable for bone health.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials or publications, and the mechanism data are missing. The known EGFR-inhibitor effects on calcium and magnesium point toward possible harm to bone, not benefit. In addition, the only US license is cancelled, and a chronic bone indication for a cancer antibody would need a strong case.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a mechanistic analysis of EGFR in bone biology
- Package insert warnings and contraindications from the FDA, since safety screening cannot proceed without them
- Preclinical or observational evidence on bone outcomes in patients treated with EGFR inhibitors
- Clarification of the cancelled BLA status and of the route and dosing that would suit a chronic bone indication

---

**Additional note: second prediction.** The second-ranked prediction, **severe nonproliferative diabetic retinopathy** (score 99.05%, evidence level L5, Hold), also has no trials or literature. The disease is driven mainly by VEGF, inflammation and microvascular damage, while panitumumab targets EGFR, so a direct link is not apparent. EGFR inhibitors are known to cause eye toxicities such as keratitis and ocular surface disease, and delivery of a large antibody to the eye raises further safety questions. It is not recommended for further work without new evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

