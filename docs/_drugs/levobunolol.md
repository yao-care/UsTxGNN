---
layout: default
title: Levobunolol
parent: Model Prediction Only (L5)
nav_order: 852
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Levobunolol: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Open-angle glaucoma"
---

# Levobunolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Levobunolol: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Levobunolol is a topical beta-blocker, originally used to treat open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, but **no clinical trials and no publications** specific to this indication were found.
The evidence reviewed mainly confirms the existing glaucoma use, which is not a true repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active license) |
| Number of NDAs | 1 (an ANDA, cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, levobunolol is a non-selective beta-adrenergic blocker. It lowers intraocular pressure by reducing aqueous humor production. Its efficacy in open-angle glaucoma and ocular hypertension is well documented.

Primary hereditary glaucoma is also a disease of raised intraocular pressure, so the same pressure-lowering mechanism could plausibly apply. However, the high TxGNN score most likely reflects how closely the disease terms sit together in the knowledge graph, not independent evidence. It is also unclear whether "primary hereditary glaucoma" differs meaningfully from the already-approved open-angle glaucoma indication.

The other two predictions, "glaucoma 1, open angle" and "open angle glaucoma", essentially restate the original indication. They have extensive literature, but they are confirmations of existing use and not new repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for primary hereditary glaucoma. No registered trials were found for the related open-angle glaucoma predictions either.

---

## Literature Evidence

No literature is available for primary hereditary glaucoma. The table below lists selected publications for open-angle glaucoma, the original indication, as supporting context only. Study types are partly inferred from titles.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26526633](https://pubmed.ncbi.nlm.nih.gov/26526633/) | 2016 | Systematic review / network meta-analysis | Ophthalmology | Compares first-line medical treatments for primary open-angle glaucoma and ocular hypertension |
| [3881032](https://pubmed.ncbi.nlm.nih.gov/3881032/) | 1985 | RCT (inferred from title) | Am J Ophthalmol | 162 patients; 0.5% and 1% levobunolol lowered IOP by about 8 mmHg, similar to 0.5% timolol |
| [2664628](https://pubmed.ncbi.nlm.nih.gov/2664628/) | 1989 | Long-term clinical study | Ophthalmology | 4-year double-masked study of 391 patients; IOP fell about 7 mmHg with levobunolol, similar to timolol, with little loss of effect |
| [2865710](https://pubmed.ncbi.nlm.nih.gov/2865710/) | 1985 | Clinical study | Ophthalmology | Up to 2 years in 391 patients; levobunolol reduced mean IOP by 27% |
| [3912600](https://pubmed.ncbi.nlm.nih.gov/3912600/) | 1985 | Comparative clinical study | Klin Monbl Augenheilkd | 50 patients over one year; levobunolol was as effective as timolol, and heart rate fell similarly, suggesting systemic absorption |
| [8123096](https://pubmed.ncbi.nlm.nih.gov/8123096/) | 1993 | Comparative clinical study | J Ocul Pharmacol | Levobunolol vs dipivefrin in 38 African American patients with open-angle glaucoma |
| [2892662](https://pubmed.ncbi.nlm.nih.gov/2892662/) | 1987 | Review | Drugs | Levobunolol 0.5–1% reduced IOP by about 30%, superior to placebo and comparable to timolol |
| [8773166](https://pubmed.ncbi.nlm.nih.gov/8773166/) | 1996 | Review | Ann Pharmacother | Compares ocular beta-blockers on systemic adverse effects, tolerability and cost |
| [40261315](https://pubmed.ncbi.nlm.nih.gov/40261315/) | 2025 | Review | Med Lett Drugs Ther | Recent overview of drugs for open-angle glaucoma |

Most of this evidence dates from 1985–1996.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA074326 (cancelled) | Levobunolol Hydrochloride (Bausch & Lomb Incorporated) | Solution / drops | Indication text not available |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not label text): asthma (including intrinsic and allergic asthma), pulmonary emphysema, diabetes mellitus, diabetic ketoacidosis, myasthenia gravis and other neuromuscular junction disease, atrioventricular block, and anaphylaxis. These are consistent with the known risks of non-selective beta-blockade, but must be confirmed against the official label.
- **Drug interactions**: 24 potential interactions were identified, with the interaction level unclassified. Those listed include lansoprazole, pantoprazole, omeprazole, prednisone, warfarin, clopidogrel, ibuprofen, fluconazole, tacrolimus and metronidazole. Clinical significance cannot be judged from the available data.
- Systemic absorption after eye-drop use is suggested by observed heart rate reduction in one study, so systemic beta-blocker precautions are relevant.

Please refer to the package insert for full warnings and precautions, which were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for primary hereditary glaucoma has a very high model score but no trials or publications behind it, so the evidence level is L5. The strongly supported glaucoma findings concern the already-labeled open-angle glaucoma use. In addition, the only US license is cancelled, which limits practical availability.

**To proceed, the following is needed:**
- Clarification of whether primary hereditary glaucoma is distinct from the existing open-angle glaucoma indication
- Disease-specific literature or trials in hereditary glaucoma
- The FDA package insert (warnings and contraindications), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- A review of current market availability and formulation options, given the cancelled license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

