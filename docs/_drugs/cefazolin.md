---
layout: default
title: Cefazolin
parent: Moderate Evidence (L3-L4)
nav_order: 504
evidence_level: L4
indication_count: 8
---

# Cefazolin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **8** 
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

# Cefazolin: From Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic. Its specific approved indications are not recorded in the available data, so the original use is inferred from its drug class.
The TxGNN model predicts it may be effective for **infectious otitis media**, but only **1 registered clinical trial (terminated, with no confirmed link to cefazolin)** and **3 loosely related publications** exist for this direction.
The evidence is weak, and the high score is a graph-based prediction, not clinical proof.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available record (antibacterial, first-generation cephalosporin) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (including ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cefazolin is a first-generation cephalosporin, a class that inhibits bacterial cell-wall synthesis by binding penicillin-binding proteins. Its efficacy against Gram-positive bacteria is well established, and mechanistically it may be applicable to bacterial otitis media.

The link between the original and new use is plausible but limited. Cefazolin covers *Staphylococcus aureus* and streptococci. However, it has limited activity against *Haemophilus influenzae* and *Moraxella catarrhalis*, the main pathogens in acute otitis media. It is also available only as an injection. That makes it a poor fit for routine outpatient treatment of a common childhood infection, where oral agents are the norm.

The TxGNN score of 0.994 reflects a pattern in the knowledge graph, not clinical evidence. The prediction should be read as a hypothesis, not as support for use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2 | Terminated | 520 | Randomized, double-blind, placebo-controlled trial comparing 5-day and 10-day antibiotic courses in children aged 6–23 months with acute otitis media. The available data does not show cefazolin as the study agent, so the trial cannot be linked to cefazolin. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [877649](https://pubmed.ncbi.nlm.nih.gov/877649/) | 1977 | Review | Southern Medical Journal | Overview of cephalosporins in pediatric infections. It supports their general usefulness and safety, especially in penicillin hypersensitivity, but is not specific to otitis media. |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Review | Clinical Pharmacy | Stevens-Johnson syndrome case and literature review. Otitis media appears only as the child's earlier infection and is not the subject. |
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case series | Annals of Otology, Rhinology, and Laryngology | Ceftazidime-cefazolin empiric therapy for pediatric Gradenigo syndrome, a rare complication of acute otitis media. It concerns a complication, not routine otitis media. |

Related evidence appears under other predicted otitis media entities. A 1982 Japanese comparative study (PMID 6752467) compared cefmetazole with cefazolin in suppurative otitis media (172 evaluable patients). Cefazolin served as the comparator there, and the results cannot be verified from the title alone.

---

## US Market Information

Approved indication text is not included in the available records.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA062831 | Cefazolin | Injection, powder, for solution | Sandoz Inc |
| ANDA203661 | Cefazolin | Injection, powder, for solution | Apotex Corp. |
| ANDA065303 | Cefazolin | Injection, powder, for solution | WG Critical Care, LLC |
| ANDA065143 | Cefazolin | Injection, powder, for solution | Hikma Pharmaceuticals USA Inc. |
| NDA216109 | Cefazolin | Injection, powder, for solution | Hikma Pharmaceuticals USA Inc. |

Other listed forms are injection solution, lyophilized powder for solution, and a solution. All are injectable or parenteral-type presentations.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests almost entirely on the model score. The only registered trial is terminated and not linked to cefazolin, and the literature is indirect. Cefazolin's spectrum and injection-only route are a poor match for the main otitis media pathogens and care setting. The strongest sub-signals lie in suppurative and chronic otitis media (L3), which are better framed as research questions than as repurposing candidates.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data from DrugBank
- Confirmation of whether cefazolin was studied in NCT01511107 (likely not)
- Review of the 1982 cefmetazole vs cefazolin study (PMID 6752467) for actual efficacy figures
- Data on middle ear fluid penetration and susceptibility of the main otitis media pathogens
- A route-of-administration assessment, since only injectable forms are marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

