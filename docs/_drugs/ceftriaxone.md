---
layout: default
title: Ceftriaxone
parent: Model Prediction Only (L5)
nav_order: 508
evidence_level: L5
indication_count: 7
---

# Ceftriaxone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Ceftriaxone: From Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Ceftriaxone is a third-generation cephalosporin injectable antibiotic, originally used for streptococcal infection, bacterial pneumonia, bacterial meningitis, gonorrhea and related infections.
The TxGNN model's top-ranked prediction is polyclonal hyperviscosity syndrome, but that one has no supporting evidence. The best-supported prediction is **infectious otitis media**, with **1 registered clinical trial** (which does not test ceftriaxone) and **18 publications** currently supporting this direction.
This is closer to an on-label-adjacent use than true repurposing, because ceftriaxone already covers the pathogens that cause acute otitis media.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Streptococcal infection, bacterial pneumonia, bacterial meningitis, gonorrhea and related infections (from the knowledge graph; no approved-indication text was available in the US license records) |
| Predicted New Indication | Infectious otitis media (best-supported among the top 7 predictions; the rank-1 prediction is polyclonal hyperviscosity syndrome) |
| TxGNN Prediction Score | 99.26% (infectious otitis media); 99.39% for the rank-1 prediction |
| Evidence Level | L3 (infectious otitis media) |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 8 (7 ANDAs and 1 NDA) |
| Recommended Decision | Hold (pending safety data; the research question is worth pursuing for otitis media) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Ceftriaxone is a beta-lactam (cephalosporin) antibiotic that inhibits bacterial cell wall synthesis. Its efficacy in streptococcal and pneumococcal infections is established.

Acute otitis media is commonly caused by *S. pneumoniae*, *H. influenzae* and *M. catarrhalis*, which are typically susceptible to ceftriaxone. A single intramuscular dose is an established guideline alternative when oral therapy fails or is not feasible. Because the original indications already include streptococcal and pneumococcal infections, this prediction is better described as an extension of existing use.

**Other predictions in the top 7 are weaker:**

- **Suppurative otitis media (99.02%, L3):** Plausible for the acute form. Chronic forms involve *Pseudomonas aeruginosa* and biofilm-producing organisms, against which ceftriaxone has limited activity, and topical therapy is usually preferred.
- **Chronic otitis media (99.01%, L4):** Limited rationale, for the same reasons. Systemic ceftriaxone is generally not first-line.
- **Polyclonal hyperviscosity syndrome (99.39%), congenital analbuminemia (99.37%), blood group incompatibility (99.12%):** No plausible mechanistic link and no supporting trials or literature. These appear to be graph-proximity artifacts.
- **Hyperamylasemia (99.39%, L4):** No therapeutic mechanism. Ceftriaxone is associated with biliary sludge and pancreatitis, so any link is more likely adverse-effect related. One 1999 study of prophylaxis after endoscopic papillosphincterotomy gives only indirect evidence.

---

## Clinical Trial Evidence

For infectious otitis media:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | Not applicable | Completed | 250 | Tests tympanostomy tube placement versus nonsurgical management in children with recurrent acute otitis media. It does not test ceftriaxone, so it provides disease-context relevance only. |

No clinical trials were registered for the other predicted indications.

---

## Literature Evidence

For infectious otitis media (most relevant publications):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | RCT (single-blind) | Pediatrics | A single intramuscular dose of ceftriaxone compared with 10 days of oral trimethoprim-sulfamethoxazole for acute otitis media |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | Clinical study | Pediatr Infect Dis J | One-day versus three-day intramuscular ceftriaxone in children with nonresponsive acute otitis media |
| [9877360](https://pubmed.ncbi.nlm.nih.gov/9877360/) | 1998 | Clinical study | Pediatr Infect Dis J | Bacteriologic efficacy of a three-day intramuscular ceftriaxone regimen in nonresponsive acute otitis media |
| [12166789](https://pubmed.ncbi.nlm.nih.gov/12166789/) | 2002 | Consensus recommendations | Clin Pediatr | Consensus recommendations for acute otitis media management (sponsored by an industry educational grant) |
| [10688388](https://pubmed.ncbi.nlm.nih.gov/10688388/) | 2000 | Review | Clin Ther | Review and revision of antimicrobial treatment recommendations for acute otitis media |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | Cohort | Int J Pediatr Otorhinolaryngol | Real-world ceftriaxone use for acute otitis media in a large US primary care population; increasing use may be a marker of antimicrobial resistance |
| [39361280](https://pubmed.ncbi.nlm.nih.gov/39361280/) | 2024 | Review | JAMA Netw Open | Appropriateness of pediatric outpatient antibiotic prescribing |
| [20802367](https://pubmed.ncbi.nlm.nih.gov/20802367/) | 2010 | Review | Otol Neurotol | Prevention and treatment of meningitis and acute otitis media in children with cochlear implants |
| [6301365](https://pubmed.ncbi.nlm.nih.gov/6301365/) | 1983 | Clinical study | Antimicrob Agents Chemother | Ceftriaxone for serious bacterial infections in adults; favorable responses in 34 of 37 infections |

For suppurative otitis media, the most direct evidence is [PMID 2523493](https://pubmed.ncbi.nlm.nih.gov/2523493/) (1989, Japanese J Antibiot), a comparison with cefotiam in acute suppurative otitis media and acute exacerbation of chronic disease. Clinical efficacy was 71% for ceftriaxone and 86% for cefotiam. The remaining literature is mostly microbiology and susceptibility surveys.

---

## US Market Information

All 8 US licenses are cancelled and none is currently valid. Approved-indication text was not available in the license records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA065169 | Ceftriaxone Sodium (Hospira) | Injection, powder, for solution | Not available (cancelled) |
| ANDA065342 | Ceftriaxone (Civica) | Injection, powder, for solution | Not available (cancelled) |
| ANDA203702 | Ceftriaxone Sodium (Apotex) | Injection, powder, for solution | Not available (cancelled) |
| ANDA065204 | Ceftriaxone Sodium (Hospira) | Injection, powder, for solution | Not available (cancelled) |
| ANDA065329 | Ceftriaxone (WG Critical Care) | Injection, powder, for solution | Not available (cancelled) |

Three further licenses are also cancelled: ANDA065224 (Baxter, injection solution), NDA050796 (B. Braun, ceftriaxone and dextrose injection solution) and ANDA065328 (WG Critical Care, injection powder).

---

## Safety Considerations

- **Disease associations from the knowledge graph (not label text):** liver disease, gallbladder disease, neonatal jaundice, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis and hemolytic anemia are listed as contraindication-related conditions.
- **Drug Interactions:** 100 interactions were identified. Major interactions were flagged with **calcium chloride, calcium glucoheptonate and calcium gluconate**. Moderate interactions include **kanamycin, neomycin, streptomycin and picosulfuric acid**. Others (for example calcitriol, epinephrine, amphotericin B, amoxicillin, doxycycline) have an unknown severity level.
- **Pharmacokinetics:** Ceftriaxone is highly protein-bound, so low albumin raises the free fraction, which is a dosing consideration.
- **Biliary effects:** Ceftriaxone is associated with biliary sludge and pancreatitis.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predictions (polyclonal hyperviscosity syndrome, hyperamylasemia, congenital analbuminemia, blood group incompatibility) lack a plausible mechanism and should not be pursued. Infectious otitis media is mechanistically credible and supported by older comparative studies and guidelines, but the only registered trial does not test ceftriaxone. It also overlaps with existing antibacterial use. Package insert safety data were missing, which blocks safety screening, and all US licenses are currently cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking data gap)
- Mechanism-of-action data from DrugBank
- Current US marketing and labeling status, since all licenses are cancelled
- A review of current guideline positions and resistance trends for ceftriaxone in acute otitis media, including any recent comparative trials
- Route compatibility assessment, which is still pending (ceftriaxone is injectable only)
- If the chronic or suppurative forms are pursued, evidence of activity against *Pseudomonas* and biofilm-producing organisms, which is currently lacking
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

