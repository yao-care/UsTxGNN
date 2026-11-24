---
layout: default
title: Cemiplimab
parent: Model Prediction Only (L5)
nav_order: 511
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
monitor_inn: "CEMIPLIMAB"
predicted_indications: ["gallbladder adenosquamous carcinoma", "rectal cloacogenic carcinoma", "adenosquamous prostate carcinoma", "urethral verrucous carcinoma", "pancreatic adenosquamous carcinoma"]
description: "Cemiplimab: predicted new indication Gallbladder adenosquamous carcinoma (evidence level L5). In the US: 1 FDA application (1 active)"
---

# Cemiplimab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Cemiplimab: Gallbladder adenosquamous carcinoma
{: .text-alpha }

## One-Sentence Summary

Cemiplimab is a PD-1 blocking antibody that is marketed in the United States.
The TxGNN model predicts it may be effective for **gallbladder adenosquamous carcinoma**,
but **no clinical trials and no publications** were found to support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Gallbladder adenosquamous carcinoma |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for cemiplimab: "Binding of the PD-1 ligands PD-L1 and PD-L2 to the PD-1 receptor found on T cells inhibits T-cell proliferation and cytokine production. Upregulation of PD-1 ligands occurs in some tumors and signaling through this pathway can contribute to inhibition of active T-cell immune surveillance of tumors. […] Cemiplimab-rwlc is a recombinant human immunoglobulin G4 (IgG4) monoclonal antibody that binds to PD-1 and blocks its interaction with PD-L1 and PD-L2, releasing PD-1 pathway-mediated inhibition of the immune response, including the anti-tumor immune response." ([DailyMed: Libtayo (cemiplimab-rwlc) prescribing information, Regeneron Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4347ae1f-d397-4f18-8b70-03897e1c054a), label version 2026-08-31; accessed 2026-11-19.) Based on what is known, cemiplimab is an antibody that blocks the interaction between PD-1 (encoded by PDCD1) and its ligand PD-L1, with an IC50 below 1 nM in a laboratory binding assay. Blocking this pathway releases the brake on T cells so they can attack tumour cells.

Adenosquamous carcinoma contains a squamous cell component. Because cemiplimab has clinical activity in a squamous-histology cancer (cutaneous squamous cell carcinoma), the squamous component of this tumour could plausibly respond to PD-1 blockade as well.

This link is only a hypothesis. No trial or publication was supplied for gallbladder adenosquamous carcinoma. The rationale rests on the model prediction and the shared squamous histology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| BLA761097 | LIBTAYO | REGENERON PHARMACEUTICALS | Injectable; intravenous | Valid |

<!-- licenses:end -->

Manufacturer: Regeneron Pharmaceuticals, Inc. The license is currently valid.

## Safety Considerations

- **Drug Interactions**: Ten interaction records were compiled. Nine are moderate-level interactions with corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone and deflazacort. The tenth is a pharmacological target record (PD-1, CD279) and carries no severity level.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials or publications for gallbladder adenosquamous carcinoma. The evidence level is therefore L5 and the rationale is theoretical.

**To proceed, the following is needed:**
- Published or registered studies of PD-1 blockade in gallbladder adenosquamous carcinoma
- Obtain and review the FDA package insert warnings and contraindications
- Detailed mechanism of action data from DrugBank
- Assessment of route compatibility and similarity to the original use (currently pending)

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Libtayo (cemiplimab-rwlc) prescribing information, Regeneron Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4347ae1f-d397-4f18-8b70-03897e1c054a) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

