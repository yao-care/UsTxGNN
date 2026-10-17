---
layout: default
title: Capecitabine
parent: Model Prediction Only (L5)
nav_order: 492
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Capecitabine: predicted new indication Top-ranked: gastric adenocarcinoma and proximal polyposis of the stom… (evidence level L5). Approved use: Metastasis from malignant tumor of colon"
monitor_inn: "CAPECITABINE"
predicted_indications: ["gastric adenocarcinoma and proximal polyposis of the stomach", "signet ring cell gastric adenocarcinoma", "gastric tubular adenocarcinoma", "gastric cardia adenocarcinoma"]
---

# Capecitabine
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

# Capecitabine: From Gastric Cancer to Signet Ring Cell Gastric Adenocarcinoma

## One-Sentence Summary

Capecitabine is an oral fluoropyrimidine (a 5-FU prodrug) originally used for gastric cancer and metastatic colon cancer.
The TxGNN model ranks several gastric cancer subtypes as predicted new indications. The top-ranked entry is a hereditary syndrome with no supporting evidence, so this report focuses on **signet ring cell gastric adenocarcinoma**, the first prediction with clinical trial and literature evidence, with **1 clinical trial** (not yet recruiting, testing an add-on agent rather than capecitabine) and **20 publications** retrieved.
Most of these predictions are subtypes of gastric cancer, which is already an established capecitabine indication, so this is largely an extension of an existing use and not true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastasis from malignant tumor of colon; gastric cancer (the label text for the US licenses was not available, so this comes from the knowledge graph) |
| Predicted New Indication | Top-ranked: gastric adenocarcinoma and proximal polyposis of the stomach (no evidence, L5, Hold). Focus of this report: signet ring cell gastric adenocarcinoma (rank 2) |
| TxGNN Prediction Score | 99.94% (rank 1 entry: 99.94%; rank 2 entry: 99.94%) |
| Evidence Level | L3 (signet ring cell gastric adenocarcinoma; observational studies and reviews, no completed capecitabine-specific RCT) |
| US Market Status | Cancelled only (all licenses show as cancelled) |
| Number of NDAs | 11 (1 NDA and 10 ANDAs) |
| Recommended Decision | Hold (the strongest subtype-level result is a Research Question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, capecitabine is an oral prodrug converted to 5-FU, which inhibits thymidylate synthase and disrupts DNA synthesis. Its efficacy in gastric cancer is established, and mechanistically it applies to any gastric adenocarcinoma subtype.

Signet ring cell carcinoma is a histologic subtype of gastric adenocarcinoma, so a link to the original indication is plausible. However, this subtype is often less chemosensitive, so the benefit is uncertain. Most of the retrieved evidence is retrospective, case-based or general gastric cancer literature.

The other predicted subtypes vary widely in support:
- **Gastric tubular adenocarcinoma** (L1) and **gastric body carcinoma** (L1, conditional) have the strongest apparent evidence, but it comes from general gastric cancer trials, not subtype-specific ones. For gastric body carcinoma, the Phase 3 trial's regimen could not be confirmed.
- **Gastric cardia adenocarcinoma** (L2) is supported by completed Phase 2 trials of capecitabine regimens in mixed gastric, gastroesophageal junction and esophageal adenocarcinoma.
- **Microinvasive gastric cancer, gastric proximal polyposis syndrome, and malignant gastric granular cell tumor** have little or no evidence, and the rationale is weak or likely a knowledge-graph artifact.

---

## Clinical Trial Evidence

For signet ring cell gastric adenocarcinoma:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07091227](https://clinicaltrials.gov/study/NCT07091227) | Phase 2 | Not yet recruiting | 66 | Neoadjuvant AK112 plus chemotherapy in signet ring cell-containing gastric or GEJ adenocarcinoma. It tests the added agent, and capecitabine may be part of the chemotherapy backbone (unconfirmed), so it gives no direct efficacy data for capecitabine. |

Supporting trials for other predicted subtypes:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00040859](https://clinicaltrials.gov/study/NCT00040859) | Phase 2 | Completed | 48 | Oxaliplatin plus capecitabine in metastatic esophageal, GEJ and gastric cardia adenocarcinoma (cardia) |
| [NCT00938470](https://clinicaltrials.gov/study/NCT00938470) | Phase 2 | Completed | 73 | Extended neoadjuvant therapy in locally advanced esophageal, GEJ and gastric cardia adenocarcinoma; capecitabine involvement is unclear (cardia) |
| [NCT01295086](https://clinicaltrials.gov/study/NCT01295086) | NA | Completed | 27 | Dose-finding of docetaxel, oxaliplatin and capecitabine plus trastuzumab in HER2-positive advanced gastro-esophageal cancer (cardia) |
| [NCT00021047](https://clinicaltrials.gov/study/NCT00021047) | Phase 1/2 | Completed | Not reported | Epirubicin, carboplatin and capecitabine in mixed solid tumors (salivary gland type stomach carcinoma) |
| [NCT00010023](https://clinicaltrials.gov/study/NCT00010023) | Phase 1 | Completed | Not reported | Capecitabine plus cisplatin in advanced digestive system cancers; early safety and dosing only (salivary gland type stomach carcinoma) |
| [NCT02494583](https://clinicaltrials.gov/study/NCT02494583) | Phase 3 | Completed | 763 | Pembrolizumab with or without cisplatin plus 5-FU or capecitabine in advanced gastric/GEJ adenocarcinoma; the capecitabine role is provisional (gastric body) |

---

## Literature Evidence

For signet ring cell gastric adenocarcinoma (top studies by design; most other entries are case reports):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35085931](https://pubmed.ncbi.nlm.nih.gov/35085931/) | 2022 | Cohort | Eur J Cancer | Comparison of FLOT and MAGIC (epirubicin, cisplatin plus capecitabine or 5-FU) perioperative regimens in oesophago-gastric adenocarcinoma |
| [29372626](https://pubmed.ncbi.nlm.nih.gov/29372626/) | 2018 | Re-analysis of Phase 3 | Asia Pac J Clin Oncol | Capecitabine/cisplatin vs 5-FU/cisplatin in Chinese patients with advanced gastric cancer (ML17032) |
| [34000769](https://pubmed.ncbi.nlm.nih.gov/34000769/) | 2021 | Cohort | Zhonghua Wei Chang Wai Ke Za Zhi | Real-world multicenter study of perioperative chemotherapy for gastric cancer |
| [19615292](https://pubmed.ncbi.nlm.nih.gov/19615292/) | 2009 | Retrospective | Zhonghua Zhong Liu Za Zhi | Toxicity and efficacy of capecitabine-based regimens in advanced gastric cancer |
| [24175788](https://pubmed.ncbi.nlm.nih.gov/24175788/) | 2013 | Comparative study | Asian Pac J Cancer Prev | Capecitabine vs bolus 5-FU in postoperative chemoradiotherapy for gastric adenocarcinoma |
| [19622303](https://pubmed.ncbi.nlm.nih.gov/19622303/) | 2009 | Clinical study | Ai Zheng | Oxaliplatin plus capecitabine as first-line therapy in advanced gastric cancer |
| [17848909](https://pubmed.ncbi.nlm.nih.gov/17848909/) | 2007 | Phase 1/2 | Br J Cancer | Dose-finding of postoperative radiotherapy with cisplatin and capecitabine in gastric cancer |
| [26324361](https://pubmed.ncbi.nlm.nih.gov/26324361/) | 2015 | Review | J Clin Oncol | Adjuvant options after surgery for localized gastric adenocarcinoma |
| [20721843](https://pubmed.ncbi.nlm.nih.gov/20721843/) | 2010 | Review | Dtsch Med Wochenschr | Diagnosis and treatment of gastric cancer |
| [26848413](https://pubmed.ncbi.nlm.nih.gov/26848413/) | 2015 | Case report | Cureus | Recurrent signet ring cell gastric adenocarcinoma treated with ECX chemotherapy and multivisceral resection |

Stronger literature exists for gastric tubular adenocarcinoma, including phase 3 trials of capecitabine-containing regimens such as [CLASSIC (PMID 22226517)](https://pubmed.ncbi.nlm.nih.gov/22226517/) (adjuvant CAPOX after D2 gastrectomy, 2012, Lancet) and [RESOLVE (PMID 34252374)](https://pubmed.ncbi.nlm.nih.gov/34252374/) (SOX vs CapOx, 2021, Lancet Oncol). The gastric cardia entry is supported by a Phase 2 study of oxaliplatin plus capecitabine ([PMID 16303863](https://pubmed.ncbi.nlm.nih.gov/16303863/), 2006, Ann Oncol). These are general gastric cancer studies and are not specific to the subtype.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020896 | XELODA (H2-Pharma, LLC) | Film-coated tablet | Not available; status cancelled |
| ANDA211724 | Capecitabine (Lifestar Pharma LLC) | Film-coated tablet | Not available; status cancelled |
| ANDA207652 | Capecitabine (Ascend Laboratories, LLC) | Film-coated tablet | Not available; status cancelled |
| ANDA204668 | Capecitabine (Sun Pharmaceutical Industries, Inc.) | Film-coated tablet | Not available; status cancelled |
| ANDA091649 | Capecitabine (Teva Pharmaceuticals USA, Inc.) | Film-coated tablet | Not available; status cancelled |

There are 11 licenses in total (1 NDA, 10 ANDAs), all with cancelled status in the compiled data. The dosage forms are oral tablets only.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite, 5-FU prodrug) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. The knowledge graph lists neutropenia, thrombocytopenia, agranulocytosis and anemia among contraindicated conditions. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver function (bilirubin), renal function; screening for dihydropyrimidine dehydrogenase deficiency should be considered |
| Handling Protection | Follow standard cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindicated or high-risk conditions (from the knowledge graph, not label text)**: liver disease, gallbladder disease, thrombocytopenia, infectious disease, neutropenia, agranulocytosis, coronary artery disease, anemia (including macrocytic anemia), hyperbilirubinemia (including hereditary forms and Gilbert syndrome), impaired renal function, sudden cardiac arrest, heart conduction disease, necrotizing enterocolitis, stomatitis, and dihydropyrimidine dehydrogenase deficiency.
- **Drug Interactions**: 100 interactions were found in total. The main ones listed are:
  - Moderate: metronidazole, tinidazole
  - Minor: aluminum hydroxide, levofloxacin, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide
  - Severity unknown: pantoprazole, omeprazole, lansoprazole, glimepiride, metformin, doxycycline, morphine, atropine, prednisone, hydrocortisone, simvastatin, dolasetron

Official FDA label warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For signet ring cell gastric adenocarcinoma, the evidence is L3: no completed capecitabine-specific trial, mostly retrospective and case-based literature, and a benefit that is uncertain because of this subtype's lower chemosensitivity. Most predicted entries are subtypes of gastric cancer, an indication capecitabine already has, so they are extensions of an existing use and not new repurposing. The strongest entries are gastric tubular adenocarcinoma (L1) and gastric cardia adenocarcinoma (L2), both of which merit Proceed with Guardrails. Gastric body carcinoma (L1) is conditional on verifying its Phase 3 trial. The top-ranked syndrome entry, microinvasive gastric cancer and malignant gastric granular cell tumor have no supporting data and should remain on Hold.

**To proceed, the following is needed:**
- Official FDA package insert warnings and contraindications (a blocking data gap for safety screening)
- Mechanism of action data from DrugBank
- Subtype-specific data for signet ring cell carcinoma, such as a subgroup analysis of CAPOX/XELOX trials
- Verification of the regimen in NCT02494583 and of capecitabine's role in NCT07091227 and NCT00938470
- Confirmation of the current US market status, since all 11 licenses appear as cancelled
- Biomarker requirements of combination partners (HER2, PD-L1, CLDN18.2) and a DPD deficiency screening plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

