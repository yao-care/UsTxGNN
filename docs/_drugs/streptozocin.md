---
layout: default
title: Streptozocin
parent: 僅模型預測 (L5)
nav_order: 1183
evidence_level: L5
indication_count: 10
---

# Streptozocin
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

# Streptozocin: From Undocumented Indication to Predicted Lymphosarcoma (Historical Antineoplastic Reuse)

## One-Sentence Summary

> Streptozocin's original approved indication is **not documented** in this evidence pack (data gap), and detailed mechanism-of-action data is also missing.
> The TxGNN model's **highest-scoring** prediction — relapsing-remitting multiple sclerosis — is explicitly flagged in the model's own rationale as a **network co-occurrence artifact, not a genuine drug-disease signal** (the only supporting paper tested an *unrelated* MS drug in a streptozocin-induced diabetes rat model).
> Among the 10 candidates evaluated, the only one with real historical human evidence is **lymphosarcoma**, supported by 1970s–80s Phase I/clinical studies of streptozocin itself (not an analog), currently rated **L3 / Proceed with Guardrails** — though a **blocking safety data gap** prevents any decision from proceeding today.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `original_indications` is empty in the evidence pack |
| Predicted New Indication | **Lymphosarcoma** (best-evidenced candidate; TxGNN's top-ranked prediction, relapsing-remitting MS, is flagged as a likely false positive — see below) |
| TxGNN Prediction Score (Lymphosarcoma) | 99.95% (rank 1791 of full candidate list) |
| Evidence Level | L3 (Lymphosarcoma) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** — blocked pending safety/label data (see DG001); candidate-level evidence alone would support "Proceed with Guardrails" |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack (DG002). Based on information embedded in the model's own rationale text, streptozocin is a **nitrosourea-class alkylating/DNA-methylating agent**. Its best-known toxicological property — selective destruction of pancreatic β-cells via the GLUT2 transporter — is used experimentally to induce diabetes in animal models; this is a toxicological tool use, not a treated indication, and should not be confused with the drug's clinical oncology history.

Separately from the GLUT2/diabetes-model mechanism, the DNA-alkylating action of nitrosoureas has historically supported use as **broad-spectrum cytotoxic chemotherapy**. This is the basis for the lymphosarcoma signal: streptozocin itself (not merely a structural analog) was directly tested in lymphoma patients in the 1970s, with reported antitumor activity (PMID 4371075) and tolerability data from a Phase I continuous-infusion study (PMID 160836). This is materially different from most of the other 9 candidates in this pack, where either no literature exists at all, or the cited literature tests **chlorozotocin** (a related but distinct nitrosourea analog) rather than streptozocin itself.

**Important caveat on the top-ranked prediction:** TxGNN's #1 candidate by score, relapsing-remitting multiple sclerosis, is explicitly annotated in the evidence pack as lacking any plausible mechanistic link. The single supporting citation (PMID 28162947) studies **fingolimod (FTY720)**, an approved MS drug, in a **streptozocin-induced diabetic rat model of erectile dysfunction** — streptozocin appears there only as a disease-induction tool, not as a treatment. This is a textbook example of a knowledge-graph co-occurrence artifact and should not be interpreted as a real repurposing signal.

---

## Predicted Indications Overview (All 10 Candidates)

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Note |
|------|---------|-------------|-----------------|-----------------|------------------|------|
| 1 | Relapsing-remitting multiple sclerosis | 99.97% | L5 | S0 | Hold | **Flagged as false positive** — unrelated drug tested in STZ-diabetes model |
| 2 | Small cell lung carcinoma | 99.97% | L2 | S1 | Hold | Direct STZ trials (PMID 229984, 148321) were **negative** |
| 3 | Pulmonary blastoma | 99.97% | L5 | S0 | Hold | No literature |
| 4 | Well-differentiated fetal adenocarcinoma of the lung | 99.96% | L5 | S0 | Hold | No literature |
| 5 | Hereditary breast/ovarian cancer syndrome | 99.96% | L5 | S0 | Hold | Not a single-tumor entity; no rationale for single-agent alkylator |
| 6 | Primary pulmonary lymphoma | 99.96% | L4 | S0 | Hold | Only pharmacokinetic review, no disease-specific data |
| **7** | **Lymphosarcoma** | **99.95%** | **L3** | **S2** | **Proceed with Guardrails** | **Direct human evidence with STZ itself (1970s–80s)** |
| 8 | Rhabdomyosarcoma | 99.95% | L5 | S0 | Hold | No literature |
| 9 | Parameningeal embryonal rhabdomyosarcoma | 99.95% | L5 | S0 | Hold | No literature |
| 10 | Embryonal extrahepatic bile duct rhabdomyosarcoma | 99.94% | L5 | S0 | Hold | No literature |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for lymphosarcoma or any of the 10 predicted indications (all `clinical_trials` and `ictrp_trials` arrays are empty in this evidence pack).

---

## Literature Evidence (Lymphosarcoma — the recommended candidate)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4371075](https://pubmed.ncbi.nlm.nih.gov/4371075/) | 1974 | Clinical Study | Cancer | Reports clinical antitumor activity and toxicity of streptozotocin (NSC-85998) |
| [160836](https://pubmed.ncbi.nlm.nih.gov/160836/) | 1979 | Phase I | Cancer Treatment Reports | Continuous IV infusion of STZ (~3.4 g/m² over 5-6 days/month) in advanced cancer; renal and GI toxicity were dose-limiting |
| [6211231](https://pubmed.ncbi.nlm.nih.gov/6211231/) | 1982 | Phase II (Analog: chlorozotocin) | Cancer Treatment Reports | 11% objective response in non-Hodgkin's lymphoma patients (chlorozotocin, not STZ itself — analog data) |
| [6234984](https://pubmed.ncbi.nlm.nih.gov/6234984/) | 1984 | Case Report | Cancer | STZ used in third trimester of pregnancy as part of combination regimen for diffuse histiocytic lymphoma; successful pregnancy outcome |

### For reference — Literature on the second-strongest candidate (Small Cell Lung Carcinoma, rank 2)

Two direct Phase II trials of streptozotocin itself were explicitly **negative**:
- [PMID 229984](https://pubmed.ncbi.nlm.nih.gov/229984/) — "Streptozotocin: an inactive agent in small cell carcinoma" (0/56 objective responses across pooled literature)
- [PMID 148321](https://pubmed.ncbi.nlm.nih.gov/148321/) — "Streptozotocin in advanced small cell bronchogenic carcinoma: an ineffective nonmyelosuppressive agent"

This candidate is **not recommended** despite its favorable TxGNN score, because the direct clinical evidence contradicts the prediction.

---

## US Market Information

This drug is currently **not marketed** under this profile (`market_status = 未上市`), and `total_licenses = 0`. No NDA/license records are available in the evidence pack.

---

## Cytotoxicity

Streptozocin's historical clinical use as a nitrosourea alkylating agent (confirmed by NCI compound number NSC-85998 in the literature) supports classification as an antineoplastic/cytotoxic agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Nitrosourea alkylating/DNA-methylating agent) |
| Myelosuppression Risk | Notably **low** relative to other alkylators — PMID 148321 explicitly describes STZ as an "ineffective **nonmyelosuppressive** agent" in the SCLC setting |
| Emetogenicity Classification | Not formally classified in the evidence pack; renal and gastrointestinal toxicity were reported as dose-limiting in Phase I data (PMID 160836) — please refer to the package insert |
| Monitoring Items | Renal function (creatinine/BUN — nephrotoxicity noted as dose-limiting), CBC/differential, liver function, electrolytes |
| Handling Protection | Cytotoxic drug handling precautions required given confirmed historical use as a chemotherapy agent |

---

## Safety Considerations

Please refer to the package insert for safety information. `key_warnings`, `contraindications`, and DDI data are all unavailable in this evidence pack (DG001, Blocking severity — TFDA label has not yet been sourced/parsed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap (DG001 — missing TFDA label/warnings) prevents this candidate from entering the S1 safety review stage regardless of indication. Separately, the model's top-scoring prediction (multiple sclerosis) is explicitly identified in the evidence as a knowledge-graph artifact rather than a genuine signal, and should not be pursued. Among the remaining candidates, only **lymphosarcoma** has direct historical human evidence with streptozocin itself, but this evidence is 40-50 years old with no modern RCT validation — insufficient on its own to override the outstanding safety data gap.

**To proceed, the following is needed:**
- TFDA (or equivalent) product label with warnings/contraindications (DG001 — Blocking)
- Formal mechanism-of-action confirmation from DrugBank or primary literature (DG002)
- If pursuing the lymphosarcoma signal: a search for modern (post-1990) clinical data on streptozocin in lymphoma, given current evidence predates modern lymphoma treatment standards
- Clarification of the drug's actual original approved indication(s), currently undocumented in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

