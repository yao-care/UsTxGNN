---
layout: default
title: Daptomycin
parent: Model Prediction Only (L5)
nav_order: 570
evidence_level: L5
indication_count: 9
monitor_inn: "DAPTOMYCIN"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "gout", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome"]
last_modified_at: 2026-10-14
description: "Daptomycin: predicted new indication Osteoarthritis (evidence level L4). Approved use: Not available in the compiled data (the retrieved literature describe…"
---

# Daptomycin
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

## Daptomycin: From Gram-Positive Bacterial Infections to Osteoarthritis
{: .text-alpha }

## One-Sentence Summary

Daptomycin is a cyclic lipopeptide antibiotic against Gram-positive bacteria, and the data compiled for this report do not list its approved indication text.
The TxGNN model predicts it may be effective for **Osteoarthritis**, but there are **0 clinical trials** and only **10 publications**, none of which show a therapeutic effect on osteoarthritis itself (they describe treating bone and joint *infections*).
This prediction is best viewed as a model artifact rather than a real repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the retrieved literature describes use against Gram-positive infections such as skin infections, bacteraemia and right-sided endocarditis) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 17) |
| Number of NDAs | 17 authorizations in total (all cancelled; includes NDAs and ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, daptomycin is a cyclic lipopeptide antibiotic that acts on Gram-positive bacteria, and its efficacy in bacterial infections is established. Mechanistically, there is no clear basis for it being applicable to degenerative osteoarthritis.

The retrieved literature concerns daptomycin used to treat osteoarticular and prosthetic joint infections caused by organisms such as *Staphylococcus*. That is an anti-infective use, not disease modification of osteoarthritis. The high TxGNN score most likely reflects network proximity to bone and joint terms rather than a true repurposing signal.

A more plausible, though still early, lead is in a neighbouring joint disease. A 2025 animal study reported that daptomycin reduced collagen-induced arthritis by suppressing inflammatory cytokines and the NF-κB pathway. This is relevant to rheumatoid arthritis (the second-ranked prediction), not osteoarthritis, and it is preclinical only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the publications below tests daptomycin as a treatment for osteoarthritis. Most concern bone and joint infections.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Cohort | International Orthopaedics | Safety and efficacy of high-dose daptomycin plus rifampicin in Gram-positive osteoarticular infections |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Cohort | J Antimicrob Chemother | Outcomes of daptomycin vs standard therapy in osteoarticular infections with *S. aureus* bacteraemia |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Cohort | J Antimicrob Chemother | Clinical efficacy and safety of daptomycin in hip and knee periprosthetic joint infections |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Cohort | Int J Antimicrob Agents | High-dose daptomycin (>6 mg/kg) in complicated bone, joint and implant-associated infections |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Registry | Medicina Clinica | EU-CORE registry: daptomycin use in Spanish hospitals across Gram-positive infections |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Survey | Int J Antimicrob Agents | Survey of current practice in managing prosthetic joint infections |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In vitro | J Antibiotics | Antibiotic susceptibility of staphylococci from prosthetic joint infections |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Cohort | Surgical Infections | Ten-year evolution of staphylococcal profiles in osteoarticular infections |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Case report | Case Reports in Orthopedics | Chronic *Corynebacterium striatum* septic arthritis in a patient with osteoarthritis referred for knee arthroplasty |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | Case report | ASM Case Reports | Septic arthritis from *Corynebacterium propinquum* in a native joint |

---

## US Market Information

All 17 US authorizations for daptomycin are currently valid. The approved indication text is not available for any of them. Five representative entries:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA213645 | DAPZURA RT (Baxter Healthcare) | Lyophilized powder for injection (solution) | Not available |
| NDA217415 | Daptomycin (Xellia) | Lyophilized powder for injection (solution) | Not available |
| NDA208385 | Daptomycin (Sagent) | Lyophilized powder for injection (solution) | Not available |
| NDA210282 | Daptomycin (Hospira) | Lyophilized powder for injection (solution) | Not available |
| NDA217630 | Daptomycin (MAIA) | Lyophilized powder for injection (solution) | Not available |

---

## Safety Considerations

- **Disease associations flagged by the knowledge graph** (not label text): myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, diarrheal disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, eosinophilic pneumonia, pulmonary eosinophilia, peripheral neuropathy and peripheral nervous system disease.
- **Muscle toxicity:** A published case report describes daptomycin-induced rhabdomyolysis complicated by acute gouty arthritis, in line with the muscle-related flags above.
- **Drug Interactions:** 12 interactions were found.
  - Moderate: picosulfuric acid, rosuvastatin, simvastatin, iobenguane (I-131), ibuprofen, diclofenac, ethinylestradiol, celecoxib, cyclosporine, mycophenolic acid.
  - Minor: dicoumarol, warfarin.
  - The statin interactions and NSAID co-use are particularly relevant given the muscle-toxicity signal, and NSAIDs are commonly used in arthritis.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials exist, and the literature concerns treating joint infections rather than osteoarthritis. No mechanistic link to degenerative osteoarthritis is supported. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The muscle-toxicity profile (myopathy, rhabdomyolysis) adds a safety concern for a chronic, non-infectious condition. Daptomycin is also an injectable-only antibiotic, with 17 US licenses currently valid.

**Other predictions for context:**
- **Rheumatoid arthritis** is the only prediction with a preclinical signal (collagen-induced arthritis in mice, 2025). It is worth treating as a research question, not a clinical candidate.
- **Osteoarthritis susceptibility, gout** and the rare skeletal or developmental disorders (pseudoachondroplasia, Hunter-Thompson acromesomelic dysplasia, brachyolmia and others) have no supporting evidence. For gout, the only report describes an adverse event, not a benefit.

**To proceed, the following is needed:**
- Mechanism of action data and the original indication text, which are missing from the compiled data
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Further preclinical work on anti-inflammatory activity, ideally redirected toward rheumatoid arthritis models
- A risk-benefit assessment of systemic exposure and muscle toxicity for a chronic non-infectious indication, plus a route-compatibility check
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

