---
layout: default
title: Cefazolin
parent: Model Prediction Only (L5)
nav_order: 504
evidence_level: L5
indication_count: 8
---

# Cefazolin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Cefazolin: From Bacterial Pneumonia and Other Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic, originally used for bacterial infections such as streptococcal and staphylococcal pneumonia, endocarditis, bacterial arthritis and cholangitis.
The TxGNN model predicts it may be effective for **infectious otitis media** (score 99.44%), but **no clinical trials** are registered and only **2 publications** are indirectly related, so the evidence is essentially model-driven.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia, cholangitis, endocarditis, bacterial arthritis (from the knowledge graph; no approved indication text is available in the US license records) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L4 (preclinical/indirect evidence only; no registered trials) |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 11 (all cancelled; 4 NDAs and 7 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, cefazolin is a first-generation cephalosporin that inhibits bacterial cell wall synthesis. It is active against gram-positive cocci such as streptococci and methicillin-susceptible staphylococci.

Its efficacy in streptococcal and staphylococcal pneumonia is already recognised, and these same organisms can cause otitis media and its complications. This makes an extension to bacterial ear infections mechanistically plausible.

There are important limits. Cefazolin has limited activity against *Haemophilus influenzae* and *Moraxella catarrhalis*, the main otitis media pathogens. The literature supporting this prediction is thin: a 2025 pediatric case report of Gradenigo syndrome (a complication of otitis media) used ceftazidime plus cefazolin together, so it does not test cefazolin alone. The other retrieved paper (Stevens-Johnson syndrome) is not relevant.

Other predicted indications in the same family (middle ear disease, chronic otitis media, suppurative otitis media, otosalpingitis, non-suppurative otitis media, allergic otitis media) all score above 99%. Their evidence ranges from one older comparative study to none at all. The non-suppurative and allergic forms are largely non-bacterial, so an antibacterial mechanism has little relevance there.

## Clinical Trial Evidence

Currently no related clinical trials are registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case report | Ann Otol Rhinol Laryngol | Ceftazidime-cefazolin empiric therapy in pediatric Gradenigo syndrome, a complication of acute otitis media; cefazolin was not tested alone |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Review | Clin Pharm | Management of Stevens-Johnson syndrome; otitis media appears only as the patient's background illness, so it is not relevant to this indication |

**Related evidence for other otitis media entries (for reference):** a 1982 comparative clinical study (PMID [6752467](https://pubmed.ncbi.nlm.nih.gov/6752467/), *Jpn J Antibiot*) compared cefmetazole with cefazolin in 172 evaluable patients with suppurative otitis media. Cefazolin was the comparator, and the study is old and does not meet current trial standards. The remaining items are veterinary surgical series or studies of other cephalosporins.

## US Market Information

All 11 US authorizations for cefazolin are cancelled; none is currently valid. Approved indication text is not available in the records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA216109 | Cefazolin (Hikma) | Injection, powder, for solution | Not available |
| NDA050779 | Cefazolin Sodium (B. Braun) | Solution | Not available |
| NDA207131 | Cefazolin (Baxter) | Injection, solution | Not available |
| ANDA062831 | Cefazolin (Sandoz) | Injection, powder, for solution | Not available |
| ANDA203661 | Cefazolin (Apotex) | Injection, powder, for solution | Not available |

The remaining 6 ANDAs (WG Critical Care ×2, Hikma ×2, Apotex, Samson Medical) are also cancelled and are not listed here.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text):** blood coagulation disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, congenital prothrombin deficiency.
- **Drug Interactions:** 100 interactions were identified. The Moderate-level ones are aminoglycosides (kanamycin, neomycin, streptomycin) and picosulfuric acid. Many others (e.g., amphotericin B, epinephrine, metformin, omeprazole, morphine) have an unclassified severity level.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high and the antibacterial mechanism is plausible for gram-positive otitis media. However, there are no registered trials, no direct evidence that cefazolin alone works in otitis media, and known gaps in coverage of the main otitis media pathogens. All US licenses are also cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Susceptibility data for the main otitis media pathogens (*H. influenzae*, *M. catarrhalis*, *S. pneumoniae*) against cefazolin
- Direct clinical evidence of cefazolin monotherapy in bacterial otitis media, or a rationale for selecting a better-targeted subtype (e.g., suppurative or complicated otitis media) given the weaker rationale for non-bacterial forms
- Clarification of the regulatory and route (injectable) feasibility for an ear infection indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

