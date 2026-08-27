---
layout: default
title: Methylene Blue
parent: 僅模型預測 (L5)
nav_order: 914
evidence_level: L5
indication_count: 3
---

# Methylene Blue
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Methylene Blue: Three TxGNN-Predicted Indications Evaluated

## One-Sentence Summary

> Methylene blue is not currently marketed in Taiwan (0 licenses on file), and its original indication and mechanism-of-action data are both gaps in this evidence pack.
> TxGNN predicts three possible new indications for this drug — **Bronchitis**, **Methemoglobinemia (Alpha Type)**, and **Methemoglobinemia due to Methemoglobin Reductase Deficiency** —
> but the supporting evidence ranges from a likely false-positive prediction to an already well-established antidote mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no original indications or Taiwan licenses on file) |
| US/Taiwan Market Status | Not Marketed |
| Number of NDAs | 0 |

| Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommended Decision |
|---|---|---|---|---|
| Bronchitis | 99.97% | L5 | S0 | **Hold** |
| Methemoglobinemia, Alpha Type | 99.36% | L3 | S2 | **Proceed with Guardrails** |
| Methemoglobinemia due to Methemoglobin Reductase Deficiency | 99.36% | L4 | S1 | **Research Question** |

---

## Why Are These Predictions Reasonable (or Not)?

Detailed mechanism-of-action data for methylene blue is not available in this evidence pack (flagged as a High-severity data gap). Based on the literature retrieved for each candidate indication, the reasoning differs sharply by indication:

**Bronchitis** — The 10 literature hits retrieved are almost entirely unrelated to a therapeutic use of methylene blue in bronchitis. Most describe methylene blue as a **diagnostic staining/dye reagent** (fiberoptic bronchoscopy tumor staining, chromoendoscopy, bronchoalveolar lavage dilution marker, erythrocyte spectrophotometry) or are entirely unrelated compounds/drugs that merely mention "bronchitis" in passing. No study supports a treatment effect. This pattern is consistent with a **knowledge-graph co-occurrence artifact** — methylene blue's frequent appearance alongside "bronchitis" in diagnostic-staining literature likely drove a spurious high TxGNN score rather than a genuine pharmacological signal.

**Methemoglobinemia (Alpha Type)** — This is mechanistically well-founded and not really a "new" indication: methylene blue is reduced by NADPH-dependent methemoglobin reductase to leucomethylene blue, which in turn reduces Fe³⁺ (methemoglobin) back to Fe²⁺ (functional hemoglobin). This is the classic antidote mechanism for acquired (drug/toxin-induced) methemoglobinemia and is already standard-of-care in many clinical guidelines — the TxGNN prediction here largely reconfirms known pharmacology.

**Methemoglobinemia due to Methemoglobin Reductase Deficiency (hereditary/congenital form)** — In patients with congenital cytochrome b5 reductase (diaphorase) deficiency, methylene blue can theoretically bypass the deficient enzyme via the same NADPH-dependent reduction pathway used in acquired methemoglobinemia. This extrapolation is mechanistically plausible but is currently supported only by case reports and veterinary (canine) data, not prospective human trials.

---

## Clinical Trial Evidence

No registered clinical trials (ClinicalTrials.gov or ICTRP) were found for any of the three predicted indications.

---

## Literature Evidence

### 1. Bronchitis

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9387672](https://pubmed.ncbi.nlm.nih.gov/9387672/) | 1996 | Case Series (diagnostic staining) | Zhonghua wai ke za zhi | Methylene blue used as a bronchoscopic staining agent to distinguish malignant bronchial tumors from bronchitis; not a treatment study |
| [7313968](https://pubmed.ncbi.nlm.nih.gov/7313968/) | 1981 | Case Series (diagnostic staining) | Terapevticheskii arkhiv | Chromoendoscopy with methylene blue for differential diagnosis of benign vs. malignant GI/bronchial lesions |
| [31419501](https://pubmed.ncbi.nlm.nih.gov/31419501/) | 2020 | Preclinical (unrelated compound) | Journal of Ethnopharmacology | Essential oil of an unrelated plant (Lippia alnifolia) studied for tracheal relaxation; methylene blue not the study drug |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical chemistry (unrelated) | Analytica Chimica Acta | Biosensor for theophylline detection; methylene blue not the study drug |
| [21767626](https://pubmed.ncbi.nlm.nih.gov/21767626/) | 2011 | Preclinical (unrelated compound) | Journal of Ethnopharmacology | Antidepressant-like effects of an unrelated plant extract traditionally used for bronchitis; methylene blue not involved |
| [8420409](https://pubmed.ncbi.nlm.nih.gov/8420409/) | 1993 | Methodological/Cohort | American Review of Respiratory Disease | Methylene blue used only as a dilution marker in bronchoalveolar lavage fluid quantitation |
| [6121761](https://pubmed.ncbi.nlm.nih.gov/6121761/) | 1982 | Preclinical (unrelated drug) | Int J Clin Pharmacol Ther Toxicol | Methylene blue used only to measure circulation time in a beta-blocker cardiovascular study |
| [20084922](https://pubmed.ncbi.nlm.nih.gov/20084922/) | 2009 | Case Report (unrelated) | Mikrobiyoloji Bulteni | Moraxella catarrhalis endocarditis case; bronchitis mentioned only as background pathogen context |
| [17120034](https://pubmed.ncbi.nlm.nih.gov/17120034/) | 2007 | Case Report (unrelated) | European Journal of Pediatrics | Isolated tracheoesophageal fistula case; unrelated to methylene blue |
| [2749902](https://pubmed.ncbi.nlm.nih.gov/2749902/) | 1989 | Basic science (unrelated) | Tsitologiia | Spectrophotometric study of erythrocyte methemoglobin using methylene blue-based reagent; unrelated to bronchitis |

### 2. Methemoglobinemia, Alpha Type

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3537620](https://pubmed.ncbi.nlm.nih.gov/3537620/) | 1986 | Review | Medical Toxicology | Clinical features and management review of drug/chemical-induced methemoglobinemia, including methylene blue's role |
| [26950891](https://pubmed.ncbi.nlm.nih.gov/26950891/) | 2016 | In vitro/Mechanistic | J Photochem Photobiol B | Photochemical/computational study of methylene blue-protein binding; notes known toxicities including methemoglobinemia |

### 3. Methemoglobinemia due to Methemoglobin Reductase Deficiency

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36638001](https://pubmed.ncbi.nlm.nih.gov/36638001/) | 2023 | Cohort (veterinary) | Am J Vet Res | Long-term oral methylene blue therapy in dogs with hereditary CYB5R-deficiency methemoglobinemia; effects on MetHb levels and inflammatory markers |
| [35202847](https://pubmed.ncbi.nlm.nih.gov/35202847/) | 2022 | Case Report (veterinary) | Top Companion Anim Med | Oral methylene blue treatment in a dog with cytochrome b5 reductase deficiency |
| [29845943](https://pubmed.ncbi.nlm.nih.gov/29845943/) | 2018 | Case Report | Netherlands J Medicine | 61-year-old with congenital methemoglobinemia (CYB5R3 variant); methylene blue used diagnostically/therapeutically |
| [14109019](https://pubmed.ncbi.nlm.nih.gov/14109019/) | 1964 | Case Report | Archives of Internal Medicine | Hereditary diaphorase deficiency and methemoglobinemia |
| [14248326](https://pubmed.ncbi.nlm.nih.gov/14248326/) | 1964 | Case Report | Archives Françaises de Pédiatrie | Recessive congenital methemoglobinemia linked with diaphorase I deficiency |

---

## Market Information

Methylene blue is currently **not marketed** in Taiwan — 0 licenses on file, no dosage forms recorded.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are all currently unavailable — TFDA label data is flagged as a **Blocking** data gap (DG001), which prevents any S1 safety pre-assessment.)

---

## Conclusion and Next Steps

**1. Bronchitis — Decision: Hold**
- **Rationale:** The retrieved literature is almost entirely diagnostic-staining or unrelated-compound studies; no evidence supports a treatment effect. This is likely a knowledge-graph co-occurrence false positive.
- **To proceed:** Would need genuine mechanistic or preclinical efficacy data in respiratory inflammation before any further evaluation — not recommended to pursue with current evidence.

**2. Methemoglobinemia, Alpha Type — Decision: Proceed with Guardrails**
- **Rationale:** Mechanism (NADPH-dependent methemoglobin reductase pathway) is well established and already reflected in clinical management guidelines; evidence level L3 (review + mechanistic literature).
- **To proceed, the following is needed:**
  - TFDA package insert / label data (Blocking gap DG001) for dosing and contraindication confirmation
  - Formal mechanism-of-action documentation (High gap DG002)
  - Since the drug is not currently marketed in Taiwan, a market-entry or named-patient access pathway would need to be established

**3. Methemoglobinemia due to Methemoglobin Reductase Deficiency — Decision: Research Question**
- **Rationale:** Mechanistically plausible extrapolation from the acquired-methemoglobinemia indication, but human evidence is limited to old case reports; the strongest recent data are veterinary (canine).
- **To proceed:** Prospective case series or registry data in genetically confirmed CYB5R-deficient patients would be needed before moving beyond a research question.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

