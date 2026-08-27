---
layout: default
title: Floxuridine
parent: 僅模型預測 (L5)
nav_order: 712
evidence_level: L5
indication_count: 10
---

# Floxuridine
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

Using the report template as specified. This is a self-contained content-generation task (no code changes, no repo exploration needed) — I'll produce the Markdown report directly from the evidence pack.

A few notes on how I handled data gaps in this pack, before the report:

- `drug.original_indications` is empty and `original_moa` is `[Data Gap]`. I inferred the original indication from context embedded in the literature evidence itself (multiple citations describe floxuridine/FUDR as a hepatic arterial infusion agent for colorectal/GI liver metastases — e.g. PMID 20048179), since no formal field was populated. This is flagged in the report rather than stated as fact.
- `predicted_indications[0]` (rank 1, per spec) is "hereditary breast ovarian cancer syndrome" — but its own `repurposing_rationale` explicitly says this is likely a knowledge-graph artifact (a germline predisposition syndrome isn't a chemotherapy target). I reported this honestly rather than dressing it up as a strong signal, since the evidence level (L5) and recommendation (Hold) in the data already reflect that.

---

# Floxuridine: From Metastatic Colorectal Cancer to Hereditary Breast Ovarian Cancer Syndrome

## One-Sentence Summary

Floxuridine (FUDR) is a fluoropyrimidine antimetabolite historically administered via hepatic arterial infusion (HAI) for gastrointestinal cancers metastatic to the liver, most notably colorectal cancer. The TxGNN model's top-ranked prediction is **Hereditary Breast Ovarian Cancer Syndrome**, with a **99.86%** confidence score, but currently **0 clinical trials** and **0 publications** support this specific direction — the underlying rationale flags this as a likely knowledge-graph artifact rather than a genuine repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer / GI malignancies with liver metastases, treated via hepatic arterial infusion (inferred from literature context — no formal `original_indications` record in this evidence pack) |
| Predicted New Indication | Hereditary Breast Ovarian Cancer Syndrome |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on known information, Floxuridine is a pyrimidine antimetabolite closely related to 5-fluorouracil (5-FU) and belongs to the fluoropyrimidine class of thymidylate synthase (TS) inhibitors; its efficacy in gastrointestinal malignancies, particularly colorectal cancer with liver metastases treated via hepatic arterial infusion, is well established in the literature accompanying this evidence pack (e.g., PMID 20048179, an NCCTG/NSABP intergroup trial of HAI floxuridine for resected colorectal liver metastases).

The predicted new indication, however, is not a tumor type — it is a **hereditary cancer predisposition syndrome** driven by germline BRCA1/2 mutations. There is no tumor tissue, proliferating cell population, or DNA-synthesis-dependent process that a cytotoxic TS inhibitor could act on in this context; a predisposition syndrome by itself is not a pharmacological treatment target in the way a diagnosed malignancy is.

For this reason, the mechanism does **not** clearly apply. The rationale attached to this candidate states directly that the high TxGNN score likely reflects a knowledge-graph association carried over from adjacent breast/ovarian cancer nodes, rather than any direct clinical or mechanistic evidence linking Floxuridine to this syndrome. This is a case where the raw prediction score is high but the underlying signal should be treated with substantial skepticism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

No U.S. market authorizations are on record for Floxuridine in this dataset — market status is "Not Marketed" with 0 total licenses, so no NDA/license entries are available to tabulate.

## Cytotoxicity

Floxuridine is a conventional cytotoxic chemotherapeutic agent (fluoropyrimidine class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine / pyrimidine antimetabolite, thymidylate synthase inhibitor — mechanistically related to 5-FU) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (no formal toxicity/DDI data available in this pack — DDI query returned `not_found`) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | As a cytotoxic antineoplastic agent, handling should follow institutional cytotoxic drug handling protocols; please confirm against the official package insert |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for this candidate is high (99.86%), but it is unsupported by any clinical trial or literature evidence, and the predicted target — a hereditary germline predisposition syndrome — is not a mechanistically plausible target for a cytotoxic antimetabolite. This pattern is consistent with a knowledge-graph artifact rather than a genuine repurposing signal, and the evidence pack itself explicitly flags it as such (Evidence Level L5, Decision Stage S0).

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: TFDA/regulatory label (warnings, contraindications) — required before this or any Floxuridine candidate can enter S1 safety pre-assessment
- Resolve data gap DG002: formal DrugBank/mechanism-of-action data to properly evaluate mechanistic plausibility
- Given the weak evidentiary basis for the top-ranked candidate, prioritize evaluation of the pipeline's lower-ranked but evidence-supported candidates instead: **myeloid leukemia** (rank 3, L4/S1, 20 literature hits — though one case report suggests a possible adverse secondary-malignancy signal that needs scrutiny), **melanoma** (rank 6, L3/S1, 1 Phase 2/3 trial pending manual verification of tumor histology), **ovarian clear cell adenocarcinoma** (rank 8, L4/S1), and **female breast carcinoma** (rank 10, L4/S1, includes direct HAI-floxuridine cohort evidence in liver metastases)
- If hereditary breast ovarian cancer syndrome is to be pursued further, request expert clinical/genetics review to determine whether any biologically plausible sub-population (e.g., BRCA-mutated tumors with defined chemosensitivity) could justify continued investigation, rather than the syndrome as a whole
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

