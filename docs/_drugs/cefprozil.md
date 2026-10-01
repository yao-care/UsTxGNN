---
layout: default
title: Cefprozil
parent: Model Prediction Only (L5)
nav_order: 506
evidence_level: L5
indication_count: 10
---

# Cefprozil
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

# Cefprozil: From Oral Cephalosporin Antibiotic to Urinary Tract Infection

## One-Sentence Summary

Cefprozil is a second-generation oral cephalosporin antibiotic, marketed in the US as generic products for common bacterial infections.
The TxGNN model predicts it may be effective for **urinary tract infection (UTI)**.
This is supported by **3 randomized comparative trials** and **9 publications** in total, but **no registered clinical trials**, and all the studies date from 1991-1995.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (oral cephalosporin antibiotic); label indication text is not included in the source data |
| Predicted New Indication | Urinary tract infection |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (as assigned in the Evidence Pack, based on 3 randomized trials in acute uncomplicated UTI; none are registry-listed and their quality is unverified) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all generic ANDAs) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is not available in the Evidence Pack. Cefprozil is a beta-lactam cephalosporin. It inhibits penicillin-binding proteins (PBPs) and blocks bacterial cell wall synthesis. It is active against common urinary pathogens such as *E. coli* and *Klebsiella pneumoniae*, and an in vitro study of 637 clinical isolates from a Taiwan hospital found it inhibited over 80% of *E. coli* and *K. pneumoniae* isolates at 8 mg/L.

This is closer to an established antibacterial use than to true repurposing. Cefprozil already treats respiratory and skin infections, and the same antibacterial activity covers the organisms behind uncomplicated UTI. The Evidence Pack lists no original indications, so the "original to new" link rests on general antibacterial spectrum, not on a label-to-label comparison.

The main caveat is that the supporting trials are from 1991-1992, have no registry entries, and their methodological quality could not be verified from the titles and abstracts. Any use should follow current local susceptibility data and regulatory labeling.

## Clinical Trial Evidence

Currently no related clinical trials registered for urinary tract infection.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1952874](https://pubmed.ncbi.nlm.nih.gov/1952874/) | 1991 | RCT | Antimicrob Agents Chemother | 108 college women with acute UTI, cefprozil 500 mg once daily vs cefaclor 250 mg three times daily for 10 days. Clinical/bacterial cure at 1 week was 94%/93% (cefprozil) vs 94%/94% (cefaclor), not significantly different. |
| [1761453](https://pubmed.ncbi.nlm.nih.gov/1761453/) | 1991 | RCT | J Antimicrob Chemother | Open, randomized trial in about 100 adults with acute uncomplicated UTI, cefprozil 500 mg once daily vs cefaclor 250 mg three times daily. |
| [1611652](https://pubmed.ncbi.nlm.nih.gov/1611652/) | 1992 | RCT | Clin Ther | Multicenter randomized study, once-daily cefprozil vs three-times-daily cefaclor for 10 days in patients aged 2 years or older with acute uncomplicated UTI. |
| [7681376](https://pubmed.ncbi.nlm.nih.gov/7681376/) | 1993 | Review | Drugs | Review of antibacterial activity, pharmacokinetics and therapeutic potential. Active against Gram-positive cocci and moderately active against several Gram-negative organisms; not active against MRSA. |
| [8042575](https://pubmed.ncbi.nlm.nih.gov/8042575/) | 1994 | Review | Am Fam Physician | Oral cephalosporins (including cefprozil) are effective but expensive alternatives for skin, respiratory and urinary tract infections. |
| [8464648](https://pubmed.ncbi.nlm.nih.gov/8464648/) | 1993 | Review | Pediatr Ann | Overview of cefprozil activity in respiratory and skin infections, with once- or twice-daily dosing and a low rate of GI and skin side effects. The available abstract does not mention UTI. |
| [1289583](https://pubmed.ncbi.nlm.nih.gov/1289583/) | 1992 | Cohort | Jpn J Antibiot | 21 children with acute bacterial infections (including 3 UTIs); good to excellent response in 19 of 21 and all 11 strains eradicated. |
| [1494237](https://pubmed.ncbi.nlm.nih.gov/1494237/) | 1992 | Cohort | Jpn J Antibiot | Pediatric laboratory and clinical study, including serum and urinary concentrations and urinary recovery of cefprozil. |
| [8529432](https://pubmed.ncbi.nlm.nih.gov/8529432/) | 1995 | In vitro study | Chemotherapy | Tested against 637 clinical isolates from Kaohsiung Veterans General Hospital, Taiwan. Inhibited over 80% of *E. coli* and *K. pneumoniae* at 8 mg/L. |

## US Market Information

The source data does not include approved indication text for these products.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA065381 | Cefprozil | Powder, for suspension | Rising Pharma Holdings, Inc. |
| ANDA065340 | Cefprozil | Tablet, film coated | Aurobindo Pharma Limited |
| ANDA090857 | Cefprozil | Tablet, film coated | Ascend Laboratories, LLC |
| ANDA065261 | Cefprozil | Powder, for suspension | Lupin Pharmaceuticals, Inc. |
| ANDA065340 | Cefprozil | Tablet, film coated | NorthStar Rx LLC |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three randomized trials in acute uncomplicated UTI show cefprozil performing comparably to cefaclor, and its spectrum covers the usual urinary pathogens. However, the trials are more than 30 years old, are not registry-listed, and were not appraised for quality. Safety data are also missing from the pack.

Other predicted indications are weaker:
- **Research questions:** Pneumonia (only an indirect duration-comparison trial, NCT06494072, still recruiting) and laryngitis (uncontrolled pediatric series, 0% efficacy in one small laryngitis subgroup, and most cases are viral).
- **On hold:** Epiglottitis, gonococcal urethritis, xanthogranulomatous pyelonephritis and uterine inflammatory disease, all with no supporting evidence and better-established therapies.
- **Mechanistically implausible:** Ureaplasma urethritis (no cell wall) and urogenital and abdominal tuberculosis (intrinsic beta-lactamase resistance). These are likely knowledge-graph artifacts.

**To proceed, the following is needed:**
- FDA package insert warnings, contraindications and approved indications (the pack has none)
- DrugBank mechanism-of-action data
- Quality appraisal of the 1991-1992 UTI trials and a check against current guidelines and local resistance data
- Any recent (post-2000) UTI comparative data, or confirmation that current guidelines still support this use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

