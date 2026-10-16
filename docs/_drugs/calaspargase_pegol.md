---
layout: default
title: Calaspargase Pegol
parent: Model Prediction Only (L5)
nav_order: 485
evidence_level: L5
indication_count: 4
monitor_inn: "CALASPARGASE PEGOL"
predicted_indications: ["insomnia (disease)", "factor 5 excess with spontaneous thrombosis", "heparin cofactor 2 deficiency", "antithrombin deficiency type 2"]
---

# Calaspargase Pegol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Calaspargase Pegol: From an Unspecified Original Indication to Insomnia

## One-Sentence Summary

Calaspargase pegol is a pegylated asparaginase product (marketed in the US as Asparlas), and the data compiled for this report do not list an approved indication for it.
The TxGNN model predicts it may be effective for **insomnia**, but **no clinical trials** and **no publications** support this prediction, and the biological rationale is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the available regulatory data |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (BLA761102, cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, calaspargase pegol is a pegylated asparaginase that depletes circulating asparagine and is used in acute lymphoblastic leukemia. The original indication text is missing from the regulatory record, so this description comes from drug-class knowledge rather than the label data.

The prediction for insomnia does not have a credible mechanistic link. The drug has no known action on sleep-wake regulation or on central nervous system targets. Insomnia appears in the literature mainly as an adverse effect of asparaginase-containing regimens, largely because of corticosteroid co-medication. The very high TxGNN score (0.998) is a knowledge-graph output without supporting biological rationale and is likely an artifact.

Three other predictions were also reviewed, and all share the same problem. Each has an L5 evidence level, no trials, and no literature:

| Predicted Disease | TxGNN Score | Assessment |
|------|------|------|
| Factor 5 excess with spontaneous thrombosis | 99.25% | Wrong direction: asparaginase lowers coagulation and anticoagulant protein synthesis and is associated with thrombosis, so it would be expected to worsen thrombotic risk |
| Heparin cofactor 2 deficiency | 99.24% | Asparaginase reduces serpin-family anticoagulants, so the effect would mimic or worsen the deficiency |
| Antithrombin deficiency type 2 | 99.21% | Asparaginase causes acquired antithrombin deficiency, so it would aggravate the condition rather than treat it |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761102 | Asparlas (Servier Pharmaceuticals LLC) | Injection, solution | Not listed (status: cancelled) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Enzyme-based antineoplastic (asparagine-depleting agent), not a conventional DNA-damaging cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions. Based on the known class effects described above, coagulation parameters (antithrombin, fibrinogen) and liver function are relevant |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Package insert warnings and contraindications are not available in the data compiled for this report, so please refer to the package insert for safety information.

- **Class-related coagulation effects**: Asparaginase therapy is associated with reduced synthesis of antithrombin, fibrinogen, and protein C/S, which raises thrombosis risk. This is especially relevant for the predicted coagulation-related indications, where it argues against repurposing.
- **Drug Interactions**: A query found 100 interacting drugs. The 20 reviewed are all rated Moderate. They include antidiabetic agents (acarbose, alogliptin, albiglutide, metformin, pioglitazone, canagliflozin, dapagliflozin, acetohexamide, chlorpropamide), corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), and others such as doxycycline, clarithromycin, clotrimazole, bupropion, acetylsalicylic acid, and chenodeoxycholic acid.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predictions rest on model scores alone (L5), with no trials or literature. The insomnia prediction has no plausible mechanism, and the three coagulation-related predictions point in the opposite direction from a therapeutic effect, because the drug is known to worsen these conditions. The only US license is cancelled, and the label safety data are missing.

**To proceed, the following is needed:**
- Obtain the FDA package insert (warnings, contraindications, and the approved indication)
- Obtain mechanism of action data from DrugBank
- Provide a biological rationale for any proposed new indication before further evaluation
- Confirm the current regulatory and supply status, since the only license is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

