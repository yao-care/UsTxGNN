---
layout: default
title: Alirocumab
parent: Model Prediction Only (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
monitor_inn: "ALIROCUMAB"
predicted_indications: ["ichthyosis, X-linked, without steroid sulfatase deficiency", "disorder of other vitamins and cofactors metabolism and transport", "xanthomatosis (disease)", "46,XY disorder of sexual development due to dihydrotestosterone backdoor pathway biosynthesis defect", "cholesterol catabolic process disease", "46,XY disorder of sex development due to a cholesterol synthesis defect", "dappled diaphyseal dysplasia", "neutral lipid storage disease", "3-hydroxyacyl-CoA dehydrogenase deficiency", "spastic paraplegia-optic atrophy-neuropathy and spastic paraplegia-optic atrophy-neuropathy-related disorder"]
---

# Alirocumab
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

# Alirocumab: From Dyslipidemia and Atherosclerosis to Xanthomatosis

## One-Sentence Summary

Alirocumab (Praluent) is a PCSK9-inhibiting monoclonal antibody, originally used to lower LDL cholesterol in dyslipidemia and atherosclerotic disease.
The TxGNN model's top-ranked prediction is X-linked ichthyosis, but it has no supporting evidence. The best-supported prediction in this list is **xanthomatosis**, which has **0 clinical trials** and **2 case reports** behind it. Of all 10 predictions, only the broader "cholesterol catabolic process disease" has substantial literature (**19 publications**), and these mostly overlap with the original indication.

## Quick Overview

The top-ranked prediction (rank 1) is shown below as required. The table also notes the better-supported alternatives.

| Item | Content |
|------|------|
| Original Indication | Syndromic dyslipidemia, arteriosclerosis disorder, atherosclerosis, arteriolosclerosis (from the knowledge graph; the US license record has no indication text) |
| Predicted New Indication | Ichthyosis, X-linked, without steroid sulfatase deficiency (rank 1) |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (the only license record, BLA125559, is listed as cancelled) |
| Number of NDAs | 1 (BLA125559) |
| Recommended Decision | Hold |

For reference, the better-supported predictions in this list:

| Predicted Indication | Score | Evidence Level | Recommendation |
|------|------|------|------|
| Xanthomatosis (rank 3) | 99.37% | L4 | Research Question |
| Cholesterol catabolic process disease (rank 5) | 99.36% | L3 | Research Question |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, alirocumab is a fully human monoclonal antibody that binds PCSK9 (the pharmacology record lists PCSK9 as its target). Blocking PCSK9 increases LDL receptor recycling and lowers LDL cholesterol. It was approved by the US FDA in 2015 for heterozygous familial hypercholesterolemia and clinical atherosclerotic cardiovascular disease.

**Rank 1, X-linked ichthyosis:** There is no clear mechanistic link. The prediction is likely driven by proximity in the cholesterol-metabolism network (the disease involves cholesterol sulfate accumulation), but no trials or literature support it. Lowering LDL-C would not be expected to correct this condition.

**Xanthomatosis (rank 3):** This is the most biologically plausible new-indication candidate. Xanthomas are lipid deposits driven by severe hypercholesterolemia, so lowering LDL-C could plausibly reduce them. However, the available evidence is indirect, and xanthoma outcomes with alirocumab have not been demonstrated.

**Cholesterol catabolic process disease (rank 5):** Mechanistic plausibility is strong, but the category is vague and the evidence mostly overlaps with the original lipid indications. It is not true repurposing.

**Other predictions (ranks 2, 4, 6–10):** These have no identifiable or plausible mechanistic link and no supporting evidence. The cholesterol synthesis defect (rank 6) is mechanistically counterproductive, since those patients already lack endogenous cholesterol.

## Clinical Trial Evidence

Currently no related clinical trials are registered for any of the 10 predicted indications.

## Literature Evidence

**Rank 1 (X-linked ichthyosis):** Currently no related literature available.

**Xanthomatosis (rank 3), the best-supported new indication:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32713907](https://pubmed.ncbi.nlm.nih.gov/32713907/) | 2020 | Case report | Internal Medicine | Sitosterolemia with severe hypercholesterolemia and tendon xanthomas (ABCG5 mutations), treated with ezetimibe and alirocumab |
| [31538826](https://pubmed.ncbi.nlm.nih.gov/31538826/) | 2019 | Case report | J Investig Med High Impact Case Rep | Severe combined dyslipidemia with a complex genetic basis (familial dysbetalipoproteinemia features, including xanthomas) |

**Cholesterol catabolic process disease (rank 5), selected publications:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38658193](https://pubmed.ncbi.nlm.nih.gov/38658193/) | 2024 | Pooled safety analysis | Eur Heart J Cardiovasc Pharmacother | Alirocumab safety from the ODYSSEY OUTCOMES trial (47,296 patient-years): fewer recurrent ischaemic events and lower all-cause death, with sustained LDL-C lowering |
| [40841123](https://pubmed.ncbi.nlm.nih.gov/40841123/) | 2025 | Meta-analysis | Open Heart | PCSK9-targeting therapies for familial hypercholesterolaemia across 23 RCTs: efficacy on lipid biomarkers and safety in adults and children |
| [38277255](https://pubmed.ncbi.nlm.nih.gov/38277255/) | 2024 | Review | Curr Opin Lipidol | PCSK9 antibodies markedly lower LDL-C and cardiovascular risk; new inhibition strategies are in development |
| [38185721](https://pubmed.ncbi.nlm.nih.gov/38185721/) | 2024 | Review | Signal Transduct Target Ther | PCSK9 as a therapeutic target, from bench to bedside, including roles beyond cardiovascular disease |
| [39679827](https://pubmed.ncbi.nlm.nih.gov/39679827/) | 2025 | Review | Pharmacotherapy | State-of-the-art review of PCSK9-directed therapies for lowering LDL-C and ASCVD risk |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Curr Atheroscler Rep | New treatments for homozygous familial hypercholesterolemia |
| [36739653](https://pubmed.ncbi.nlm.nih.gov/36739653/) | 2023 | Review | Kardiol Pol | PCSK9 inhibitors and reduced cardiovascular events |
| [38191052](https://pubmed.ncbi.nlm.nih.gov/38191052/) | 2024 | Preclinical | Metabolism | PCSK9 inhibition prevents and alleviates cholesterol gallstones through PPARα-mediated CYP7A1 activation |
| [26563849](https://pubmed.ncbi.nlm.nih.gov/26563849/) | 2015 | Review | Expert Rev Cardiovasc Ther | Alirocumab in primary hypercholesterolemia: Phase III trials showed LDL-C reductions of up to 62% |

Ranks 2 and 4 and ranks 6–10 have no related literature.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125559 (cancelled) | Praluent (Sanofi-Aventis U.S. LLC) | Injection, solution | Not listed in the license record |

## Safety Considerations

- **Drug Interactions:** The only record is a pharmacology entry for the drug's own target, PCSK9. It is not a drug-drug interaction, and no interacting drugs were identified.
- **Other safety data:** The pooled analysis of ODYSSEY OUTCOMES (47,296 patient-years) provides long-term safety observation in the original indication. No label warnings or contraindications were available.

Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (X-linked ichthyosis) is supported only by a graph score, with no trials, no literature, and no mechanistic link. Of the 10 predictions, xanthomatosis is the only one that is both plausible and a genuinely new indication, and its evidence is two case reports (L4). The "cholesterol catabolic process disease" evidence is mostly the original indication under another name. The US license is also listed as cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Clarification of the Praluent license status, since it is listed as cancelled in the compiled record
- For xanthomatosis: a systematic review of xanthoma outcomes in patients treated with PCSK9 inhibitors, and, if warranted, a pilot study in familial hypercholesterolemia or sitosterolemia
- For ranks 1–2, 4 and 6–10: no further work is recommended unless new mechanistic evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

