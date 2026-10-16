---
layout: default
title: Valrubicin
parent: Model Prediction Only (L5)
nav_order: 1281
evidence_level: L5
indication_count: 10
monitor_inn: "VALRUBICIN"
predicted_indications: ["colonic neoplasm", "rectosigmoid junction neoplasm", "colonic lymphangioma", "lipoma of colon", "cecum villous adenoma", "cecum neuroendocrine tumor G1", "cecal disease", "benign neoplasm of cecum", "colon leiomyoma", "cavernous hemangioma of colon"]
last_modified_at: 2026-10-14
description: "Valrubicin: predicted new indication Colonic neoplasm (evidence level L5). Approved use: Urinary bladder cancer (including bladder carcinoma, bladder neoplasm…"
---

# Valrubicin
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

# Valrubicin: From Bladder Cancer to Colonic Neoplasm

## One-Sentence Summary

Valrubicin is an anthracycline chemotherapy given directly into the bladder, originally used to treat bladder cancer.
The TxGNN model predicts it may be effective for **Colonic Neoplasm**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary bladder cancer (including bladder carcinoma, bladder neoplasm, bladder small cell neuroendocrine carcinoma, and non-papillary transitional cell carcinoma of the bladder) |
| Predicted New Indication | Colonic neoplasm |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 2 (both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, valrubicin is a semisynthetic anthracycline (N-trifluoroacetyladriamycin-14-valerate). It acts as a topoisomerase II inhibitor and DNA intercalator, and it is used in the bladder for BCG-refractory carcinoma in situ. A cytotoxic mechanism like this could plausibly act on other epithelial tumors, which may explain the high TxGNN score.

There are significant limits to this reasoning. Valrubicin is lipophilic and designed for local delivery into the bladder, with minimal systemic absorption. There is therefore no established route for the drug to reach colonic tumors. A hypothetical intrarectal or other local route would be entirely untested. No trial or literature evidence supports the colonic indication.

The other top-ranked predictions are weaker still. Most are benign lesions (colonic lymphangioma, lipoma, leiomyoma, cavernous hemangioma, benign cecal neoplasm, cecal villous adenoma) where cytotoxic chemotherapy is not clinically justified. They likely reflect proximity to colon neoplasm nodes in the knowledge graph rather than real biology. The low-grade cecal neuroendocrine tumor (G1) is poorly responsive to cytotoxic agents, and "cecal disease" is too non-specific to form a testable hypothesis. The rectosigmoid junction neoplasm (score 99.96%) shares the same unsupported rationale as colonic neoplasm.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020892 (Cancelled) | Valstar (Endo USA, Inc.) | Solution, concentrate | Not listed in the compiled data |
| ANDA206430 (Cancelled) | Valrubicin Intravesical Solution (Hikma Pharmaceuticals USA Inc.) | Solution, concentrate | Not listed in the compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. Systemic absorption after intravesical use is minimal. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Handle as a cytotoxic drug, following cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: urinary tract infection and overactive bladder.
- **Drug Interactions** (5 identified):
  - **Major**: Hexaminolevulinate, Cladribine
  - **Moderate**: Gadobenic acid, Omacetaxine mepesuccinate, Vitamin E

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support (Evidence Level L5). Valrubicin's local-delivery design with minimal systemic exposure offers no clear route to colonic disease, and its US authorizations are cancelled. Safety label data is also missing.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- Package insert warnings and contraindications, so safety screening can be done
- A route-compatibility assessment, since the current formulation is intravesical only
- Preclinical evidence (for example, in vitro cytotoxicity in colon cancer cell lines) to give the prediction a biological basis
- A literature and trial search focused on anthracyclines in colorectal tumors
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

