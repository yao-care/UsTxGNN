---
layout: default
title: Floxuridine
parent: Model Prediction Only (L5)
nav_order: 712
evidence_level: L5
indication_count: 10
---

# Floxuridine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Floxuridine: From Fluoropyrimidine Chemotherapy to Hereditary Breast Ovarian Cancer Syndrome

## One-Sentence Summary

Floxuridine is a fluoropyrimidine antimetabolite chemotherapy marketed in the US as an injectable powder.
The TxGNN model predicts it may be effective for **hereditary breast ovarian cancer syndrome** (score 99.86%), but this is a **prediction only, with 0 clinical trials and 0 publications** supporting it.
Other predicted indications (melanoma, female breast carcinoma, myeloid leukemia) have somewhat more supporting material, and they are summarized below.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Hereditary breast ovarian cancer syndrome |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 (ANDA listings) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, floxuridine is a fluoropyrimidine. After conversion to FdUMP it inhibits thymidylate synthase, which reduces DNA synthesis in rapidly dividing cells.

Hereditary breast ovarian cancer syndrome is a **germline predisposition syndrome** (for example, BRCA-related), not a treatable tumor type. No data connect floxuridine to BRCA-related biology such as homologous recombination deficiency. The high score most likely reflects general breast and ovarian cancer neighborhood signals in the knowledge graph rather than a disease-specific link. The prediction is therefore mechanistically weak as stated.

The more plausible reading is that floxuridine might be studied in breast or ovarian cancers that arise in carriers of these syndromes. That would need separate evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Indications With Some Evidence

These are not the primary prediction, but they contain the only supporting material in the pack.

| Predicted Indication | Score | Evidence Level | Key Points |
|------|------|------|------|
| Female breast carcinoma | 99.38% | L3 | Retrospective HAI pump plus systemic chemotherapy series in breast cancer liver metastases ([PMID 34657511](https://pubmed.ncbi.nlm.nih.gov/34657511/), 2021). A 9-patient case series of HAI floxuridine plus dexamethasone and systemic therapy reported 7 objective responses, with grade 3 liver enzyme elevations in 4 patients ([PMID 23173748](https://pubmed.ncbi.nlm.nih.gov/23173748/), 2013). Small, uncontrolled data. |
| Melanoma | 99.52% | L4 | One Phase 2/3 trial of alternating systemic and HAI therapy after resection of colorectal liver metastases ([NCT02529774](https://clinicaltrials.gov/study/NCT02529774), n=432, status unknown). It is not melanoma-specific, so the link is doubtful. |
| Myeloid leukemia | 99.69% | L4 | Only in vitro and animal work on thymidylate synthase inhibition. One case report describes CML arising after fluoropyrimidine chemotherapy, which is a safety signal rather than efficacy ([PMID 18827427](https://pubmed.ncbi.nlm.nih.gov/18827427/)). |
| Ovarian clear cell adenocarcinoma | 99.47% | L4 | A 1991 Phase II study of doxifluridine, a different 5-FU prodrug, in cervical and ovarian cancer ([PMID 1660700](https://pubmed.ncbi.nlm.nih.gov/1660700/)). The evidence is indirect. |

The remaining predictions (neutrophil immunodeficiency syndrome, CMM7, pediatric leptomeningeal melanoma, epithelioid cell uveal melanoma, CNS melanocytic neoplasm) have no trials or literature. Neutrophil immunodeficiency syndrome is biologically counter-intuitive for a myelosuppressive drug and is probably a knowledge-graph artifact.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA075387 | Floxuridine | Injection, powder, lyophilized, for solution | Hikma Pharmaceuticals USA Inc. |
| ANDA075837 | Floxuridine | Injection, powder, lyophilized, for solution | Fresenius Kabi USA, LLC |
| ANDA075387 | Floxuridine | Injection, powder, lyophilized, for solution | JND Therapeutics, Inc. |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite) |
| Myelosuppression Risk | Medium to high (class-based estimate; neutropenia and infection risk are a concern). Please refer to the package insert warnings and precautions. |
| Emetogenicity Classification | Low to moderate (class-based estimate) |
| Monitoring Items | CBC with differential, liver function (liver enzyme elevations were seen with HAI use), renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The primary prediction is a model output only (L5), with no trials, no literature, and no documented link to BRCA-related biology. The indication is a germline syndrome rather than a treatment target. The best-supported directions are HAI-based use in breast cancer liver metastases (L3) and possibly uveal melanoma liver metastases, and both are better treated as separate research questions.

**To proceed, the following is needed:**
- FDA package insert warnings, contraindications and approved indications (currently missing, and blocking safety screening)
- Mechanism of action data from DrugBank
- A targeted literature search on floxuridine in BRCA-associated breast and ovarian cancers
- Confirmation of the intervention arms and eligibility criteria of NCT02529774
- A full-text review of the breast cancer liver metastasis HAI reports, including whether floxuridine was actually used
- A targeted search on floxuridine HAI in uveal melanoma liver metastases

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

