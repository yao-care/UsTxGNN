---
layout: default
title: Capecitabine
parent: 僅模型預測 (L5)
nav_order: 492
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine: From Colorectal and Breast Cancer to Gastric Adenocarcinoma and Proximal Polyposis of the Stomach

## One-Sentence Summary

Capecitabine (Xeloda®) is an oral fluoropyrimidine prodrug, internationally established as a chemotherapy backbone for colorectal cancer, breast cancer, and gastric cancer, acting via tumor-selective enzymatic conversion to 5-fluorouracil.
The TxGNN model ranks **Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS)** as its top predicted new indication with a score of **99.94%**;
however, **no clinical trials** and **no publications** currently exist specifically supporting capecitabine use in this ultra-rare hereditary syndrome.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan (no domestic license on file) |
| Predicted New Indication | Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Capecitabine is an oral fluoropyrimidine carbamate that undergoes three-step enzymatic activation, with the final — and rate-limiting — step dependent on thymidine phosphorylase (TP). Because TP is characteristically overexpressed in solid tumors relative to surrounding normal tissue, this conversion mechanism provides a degree of tumor-selective cytotoxicity. The resulting active metabolite, 5-fluorouracil (5-FU), then inhibits thymidylate synthase (TS), blocking de novo DNA synthesis in actively proliferating cells. This mechanistic basis underpins capecitabine's established role across multiple gastrointestinal malignancies, where high TP/TS expression has been consistently documented.

GAPPS is an ultra-rare autosomal dominant hereditary syndrome caused by point mutations in the APC gene promoter 1B region, resulting in diffuse fundic gland polyposis of the proximal stomach and markedly elevated lifetime risk of gastric adenocarcinoma. Crucially, GAPPS-associated adenocarcinoma does not arise through the canonical intestinal metaplasia → dysplasia → carcinoma sequence, nor is it driven by the WNT/β-catenin hyperactivation pathway characteristic of sporadic gastric cancer. The specific TP/TS expression profile — and therefore the degree of fluoropyrimidine sensitivity — in GAPPS tumor tissue is entirely uncharacterized in the literature, making direct extrapolation from sporadic gastric adenocarcinoma trials mechanistically unjustified.

The TxGNN model's high score (99.94%) most likely reflects knowledge graph proximity between GAPPS and gastric adenocarcinoma nodes: because capecitabine is active in gastric adenocarcinoma broadly, the model infers extension to this genetically distinct subtype. This graph-based inference is a useful hypothesis-generating signal, but is not equivalent to clinical or biological evidence. With fewer than 200 families documented worldwide and no published chemotherapy efficacy data specific to GAPPS-associated adenocarcinoma, this prediction should be treated as a computational hypothesis requiring molecular validation before clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

Capecitabine is not registered in Taiwan (未上市); no Taiwan FDA license records are on file in this evidence pack. Internationally, Capecitabine (Xeloda®) holds regulatory approval in major markets — including the United States (NDA 020896), European Union, and Japan — for colorectal cancer, breast cancer, and gastric/gastroesophageal junction cancer.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Fluoropyrimidine class (oral prodrug of 5-FU) |
| Myelosuppression Risk | Moderate — neutropenia, thrombocytopenia, and anemia are well-documented class-associated adverse effects |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver function tests (AST, ALT, total bilirubin), serum creatinine and creatinine clearance (dose reduction required for CrCl 30–50 mL/min; contraindicated below 30 mL/min) |
| Handling Protection | Follow cytotoxic drug handling protocols; as an oral formulation, tablets must not be crushed or split — caregivers handling broken tablets require protective gloves |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
GAPPS is an ultra-rare hereditary gastric cancer syndrome for which zero published evidence exists regarding capecitabine efficacy, and the underlying tumor biology — arising from APC promoter 1B mutations rather than canonical intestinal-type progression — is sufficiently distinct from sporadic gastric adenocarcinoma to prevent direct extrapolation of standard chemotherapy data. The TxGNN score of 99.94% reflects disease-node proximity in the knowledge graph, not clinical validation.

**To proceed, the following is needed:**
- Molecular characterization of TP and TS expression levels in GAPPS-associated gastric adenocarcinoma tissue, to establish whether fluoropyrimidine sensitivity is mechanistically plausible
- Published case series, registry data, or expert consensus on systemic chemotherapy outcomes in GAPPS patients with invasive adenocarcinoma
- Taiwan FDA package insert retrieval to complete safety assessment (currently unavailable)
- Mechanism of action data from DrugBank to support formal mechanistic rationale
- Multidisciplinary consultation with hereditary gastric cancer specialists prior to any off-label consideration

> **Note on related indications with stronger evidence:** The TxGNN pipeline concurrently predicts capecitabine efficacy for **gastric tubular adenocarcinoma** (Rank 4, Evidence Level **L1** — including the CLASSIC trial [PMID 22226517] and RESOLVE trial [PMID 34252374], both completed Phase 3 RCTs establishing CAPOX as a standard adjuvant backbone) and **gastric cardia adenocarcinoma** (Rank 5, Evidence Level **L1** — including NCT00040859 directly studying CAPOX in gastric cardia). These two indications carry substantially stronger evidentiary support and are recommended for separate prioritized evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

