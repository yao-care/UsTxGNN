---
layout: default
title: Procaine
parent: Model Prediction Only (L5)
nav_order: 1086
evidence_level: L5
indication_count: 10
---

# Procaine
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

# Procaine: From Local Anesthesia to Methemoglobinemia

## One-Sentence Summary

Procaine is an ester-type local anesthetic, and it is also a component of some combination penicillin products.
The TxGNN model predicts it for **methemoglobinemia**, but the literature points the opposite way: the **8 publications** found mostly describe procaine as a *cause* of methemoglobinemia, and there are **no clinical trials**.
The high score most likely reflects a drug-induces-disease link in the knowledge graph, not a therapeutic one.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available license records (procaine is a local anesthetic) |
| Predicted New Indication | Methemoglobinemia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L4 (case reports and small clinical observations only; no trials) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Procaine is a local anesthetic that blocks nerve conduction, and its metabolism involves an aromatic amine (para-aminobenzoic acid, PABA) fragment.

This prediction is **not mechanistically supported**. Case reports describe methemoglobinemia after intravenous procaine (1970) and after subcutaneous novocaine infiltration in a newborn (1978). A related agent, lignocaine, has a similar report (1965). Aromatic-amine local anesthetics are known to promote methemoglobin formation, so a therapeutic role would run against the known pharmacology.

A likely explanation for the high score is that the knowledge graph links drug and disease through an adverse-effect association. The model cannot distinguish "treats" from "causes" in that case. The 1987 Chinese clinical study on methemoglobin levels under intravenous procaine anesthesia has no abstract available, so its direction of effect could not be verified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5529388](https://pubmed.ncbi.nlm.nih.gov/5529388/) | 1970 | Case report | Acta Physiol Latino Am | Methemoglobinemia caused by intravenous procaine |
| [705003](https://pubmed.ncbi.nlm.nih.gov/705003/) | 1978 | Case report (neonate) | Rev Esp Anestesiol Reanim | Methemoglobinemia in a newborn after subcutaneous novocaine infiltration during general anesthesia |
| [14246695](https://pubmed.ncbi.nlm.nih.gov/14246695/) | 1965 | Case report (related agent) | Lancet | Methemoglobinemia following lignocaine |
| [3691245](https://pubmed.ncbi.nlm.nih.gov/3691245/) | 1987 | Clinical study | Zhonghua Wai Ke Za Zhi | Effect of intravenous procaine anesthesia on methemoglobin levels (no abstract; direction of effect not verifiable) |
| [6705717](https://pubmed.ncbi.nlm.nih.gov/6705717/) | 1984 | Review | Drugs | General review of rational use of local anesthetics |
| [5644303](https://pubmed.ncbi.nlm.nih.gov/5644303/) | 1968 | Pharmacokinetic study | Am J Obstet Gynecol | Passage of procaine and PABA across the human placenta |
| [6745527](https://pubmed.ncbi.nlm.nih.gov/6745527/) | 1984 | Toxicology review | Fundam Appl Toxicol | Organophosphate interactions with ester-containing drugs (indirect relevance) |
| [5118947](https://pubmed.ncbi.nlm.nih.gov/5118947/) | 1971 | Overview | Laval Med | Local anesthetics overview (no abstract) |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA050138 | BICILLIN C-R 900/300 | Injection, suspension | Not stated in the record |
| NDA050138 | BICILLIN CR | Injection, suspension | Not stated in the record |
| M017 | TXTK NUMB | Ointment | Not stated in the record |
| M017 | TKTX NUMB | Ointment | Not stated in the record |

## Safety Considerations

The package insert warnings, contraindications and DDI data were not retrievable, so please refer to the package insert for safety information.

Literature on this prediction does report these signals:
- **Methemoglobinemia**: case reports after intravenous and infiltration use, including in a newborn.
- **Hypersensitivity**: contact dermatitis is mainly reported with ester-type anesthetics such as procaine. Hoigné's syndrome (a non-allergic reaction) is reported after procaine penicillin.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence points to procaine causing, not treating, methemoglobinemia, and there are no trials. This prediction should not be pursued as a therapeutic candidate.

Other predicted indications in the same pack look more plausible and could be reviewed as research questions. Fibromyalgia and tendinitis are consistent with procaine's local anesthetic action, and both are marked "Research Question". For tendinitis, a 2022 study of 1% procaine neural therapy in supraspinatus tendinopathy (PMID 35480510) is the most recent report. The other supporting reports are historical and uncontrolled.

**To proceed, the following is needed:**
- Retrieve the FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Retrieve mechanism of action data from DrugBank
- Confirm the direction of effect in the 1987 procaine and methemoglobin study (PMID 3691245)
- For the fibromyalgia and tendinitis leads, review the full text of the 2022 study and design a modern controlled trial

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

