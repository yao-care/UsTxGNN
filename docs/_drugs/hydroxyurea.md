---
layout: default
title: Hydroxyurea
parent: Model Prediction Only (L5)
nav_order: 781
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
monitor_inn: "HYDROXYUREA"
predicted_indications: ["female breast carcinoma", "sickle cell-hemoglobin E disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "sickle cell-hemoglobin d disease syndrome", "sickle cell-hemoglobin c disease syndrome", "cervical adenosarcoma", "colon mucinous adenocarcinoma", "rectum mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma"]
description: "Hydroxyurea: predicted new indication Female breast carcinoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Hydroxyurea
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Hydroxyurea: Female breast carcinoma
{: .text-alpha }

## One-Sentence Summary

Hydroxyurea is an oral antimetabolite chemotherapy originally used for melanoma, ovarian cancer, and sickle cell anemia.
The TxGNN model predicts it may be effective for **female breast carcinoma**, but there are currently **0 registered clinical trials** and **20 publications** for this indication. Most of those publications are preclinical or only tangentially related, and the clinical ones are old Phase 1 combination studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 (preclinical and mechanistic studies only) |
| US Market Status | Marketed (valid licenses on record: at least 7) |
| Number of NDAs | 7 authorizations in total (3 NDAs, 4 ANDAs), all cancelled |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Hydroxyurea is a ribonucleotide reductase inhibitor. It depletes the cell's pool of DNA building blocks (dNTPs) and causes replication stress. This is the basis of its use in cancers and, through a different effect (raising fetal hemoglobin), in sickle cell anemia.

Rapidly dividing tumours such as breast cancer are plausible targets for this mechanism. Preclinical studies link hydroxyurea to replication-stress and DNA-repair pathways in breast cancer cells. Examples include work on RPA2 hyperphosphorylation, in which valproic acid sensitized breast cancer cells to hydroxyurea, and work on replication-stress avoidance. The original oncology indications (melanoma, ovarian cancer) are also solid or gynaecological tumours treated with DNA-synthesis-targeting agents.

No dedicated breast cancer trial of hydroxyurea is listed. The link is therefore biologically reasonable but clinically unproven.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1733549](https://pubmed.ncbi.nlm.nih.gov/1733549/) | 1992 | Phase 1 combination study | Cancer Chemother Pharmacol | Escalating-dose cisplatin added to 5-FU, leucovorin, hydroxyurea and radiotherapy in advanced solid tumours, to find the maximum tolerated cisplatin dose |
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase 1 combination study | Am J Clin Oncol | Sequential 5-FU/leucovorin followed by hydroxyurea with allopurinol in 20 patients with advanced colorectal, pancreatic, gastric and breast cancer |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | In-silico/Preclinical | Drug Research | Designed hydroxyurea-lipid conjugates to improve cellular uptake in breast cancer, targeting the PI3K/AKT/mTOR pathway |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | Preclinical | DNA Repair | Valproic acid sensitized breast cancer cells to hydroxyurea by inhibiting RPA2 hyperphosphorylation-mediated DNA repair |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclinical | DNA Repair | A valproic acid analogue acts on the same RPA2-mediated DNA repair pathway, building on the hydroxyurea sensitization findings in breast carcinoma |
| [25814515](https://pubmed.ncbi.nlm.nih.gov/25814515/) | 2015 | Preclinical | Mol Pharmacol | A newer ribonucleotide reductase inhibitor (COH29, same target class as hydroxyurea) inhibited DNA repair in BRCA1-defective breast cancer cells |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | Case report | Case Rep Hematol | Management of coexisting hormone-positive breast cancer and essential thrombocythemia; a therapeutic-challenge report, not a test of hydroxyurea efficacy in breast cancer |
| [27504932](https://pubmed.ncbi.nlm.nih.gov/27504932/) | 2017 | Preclinical | J Cell Physiol | Chemoresistance of lung and breast cancer cells under prolonged serum starvation |
| [27634334](https://pubmed.ncbi.nlm.nih.gov/27634334/) | 2016 | Preclinical | Genome Biol | DNA replication stress mediates APOBEC3 mutagenesis in breast cancer (mechanistic context only) |

Several other retrieved papers are only loosely related, such as cervical cancer chemoradiation, a meningioma case report, and a lncRNA review. They are not listed here.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|------|------|
| NDA016295 | HYDREA | Capsule | H2-Pharma LLC | Valid |
| NDA208843 | Siklos | Film-coated tablet | Medunik | Valid |
| NDA216593 | XROMI | Solution | Nova Laboratories, Ltd. | Valid |
| ANDA075340 | Hydroxyurea | Capsule | Endo USA, Inc. | Valid |
| ANDA075143 | Hydroxyurea | Capsule | AvKARE | Valid |

Two further generic capsule authorizations (ANDA218021, ANDA213438) are also cancelled. Approved-indication text is not available for these entries.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite, ribonucleotide reductase inhibitor) |
| Myelosuppression Risk | High. The knowledge graph lists leukopenia, thrombocytopenia and anemia as contraindication-related conditions, consistent with marrow suppression being the main concern |
| Emetogenicity Classification | Low (general class expectation; please verify against the package insert) |
| Monitoring Items | CBC with differential, platelet count, renal function, liver function |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text):** kidney disease, pyoureter, thrombocytopenia, anemia, macrocytic anemia, leukopenia, cutaneous vasculitis.
- **Drug Interactions:** 100 interacting drugs were identified. The one with a specified severity is levofloxacin (Minor). Others, such as doxycycline, amphotericin B, hydrocortisone, acetylsalicylic acid, metformin, omeprazole, and vancomycin, have no severity grading.

Package insert warnings and contraindications were not available. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (0.9997), but breast cancer support is limited to preclinical work and two Phase 1 combination studies from 1991-1992. No breast cancer trial is registered, so the evidence level is L4.

Among the other candidates evaluated for hydroxyurea, **sickle cell-hemoglobin C disease** is much better supported. It has a Phase 2 trial (NCT00532883, terminated), a 2025 NEJM Evidence publication, Cochrane reviews, and an L2 rating. It carries a "Proceed with Guardrails" recommendation and may be a stronger repurposing direction.

**To proceed with breast cancer, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism-of-action data
- Modern preclinical data on hydroxyurea alone or in combination in breast cancer models, such as subtype-specific or BRCA-deficient models
- A clinical rationale and trial design, since no registered breast cancer trial exists
- Clarification of the US regulatory position, since 7 authorizations are currently valid
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

