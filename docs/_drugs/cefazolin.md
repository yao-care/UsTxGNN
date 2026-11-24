---
layout: default
title: Cefazolin
parent: Model Prediction Only (L5)
nav_order: 504
evidence_level: L5
indication_count: 8
monitor_inn: "CEFAZOLIN"
predicted_indications: ["infectious otitis media", "bronchitis", "middle ear disease", "chronic otitis media", "suppurative otitis media", "otosalpingitis", "non-suppurative otitis media", "allergic otitis media"]
last_modified_at: 2026-11-24
description: "Cefazolin: predicted new indication infectious otitis media (evidence level L5). In the US: 41 FDA applications (12 active)"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Cefazolin: first-generation cephalosporin antibiotic → infectious otitis media
{: .text-alpha }

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic that inhibits bacterial cell wall synthesis.
The TxGNN model predicts it may be effective for **infectious otitis media**, with a score of **0.9944**.
No clinical trials are registered, and the 2 publications in the data compiled for this report only indirectly address this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | infectious otitis media |
| TxGNN Prediction Score | 0.9944 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 12 of 41) |
| Number of FDA Applications | 41 (active: 12) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the FDA-approved prescribing information for cefazolin: "Cefazolin is an antibacterial drug. […] Cefazolin is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis." ([DailyMed: Cefazolin (cefazolin sodium) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d91a8d13-99a0-4d87-88dc-71cbd37922b4), label version 2026-08-31; accessed 2026-11-19.) Cefazolin is a first-generation cephalosporin that blocks bacterial cell wall synthesis. It is active against gram-positive cocci such as streptococci and methicillin-susceptible staphylococci, which can cause otitis media and its complications.

The mechanism is only partly suited to this disease. Cefazolin has limited activity against *Haemophilus influenzae* and *Moraxella catarrhalis*, the main pathogens of otitis media. This weakens the rationale and is a reason for caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case report/series | Ann Otol Rhinol Laryngol | Pediatric Gradenigo syndrome, a complication of acute otitis media, managed with empiric ceftazidime plus cefazolin. This is a combination regimen, not cefazolin alone, and not otitis media itself. |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Review | Clinical Pharmacy | Management of Stevens-Johnson syndrome. Otitis media appears only as part of one patient's history, so it is not relevant to this indication. |

No study directly evaluates cefazolin for infectious otitis media, so the evidence level is L5 (model prediction only).

## US Market Information

Eleven US authorizations are recorded for single-ingredient cefazolin products, all injectable or solution forms.

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA062831 | CEFAZOLIN SODIUM | SANDOZ | Injectable; injection | Valid |
| ANDA065047 | CEFAZOLIN SODIUM | HIKMA FARMACEUTICA | Injectable; injection | Valid |
| ANDA065141 | CEFAZOLIN SODIUM | SAMSON MEDCL | Injectable; injection | Valid |
| ANDA065143 | CEFAZOLIN SODIUM | HIKMA FARMACEUTICA | Injectable; injection | Valid |
| ANDA065303 | CEFAZOLIN SODIUM | ACS DOBFAR | Injectable; injection | Valid |

Showing 5 of 41 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the DDI query. The moderate-level ones are the aminoglycosides kanamycin, neomycin and streptomycin, and picosulfuric acid. Others, such as amphotericin B, calcitriol, epinephrine, mannitol, metformin and omeprazole, have an unknown severity level.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but no clinical trial exists and no published study directly tests cefazolin in infectious otitis media. Cefazolin also has weak coverage of the main otitis media pathogens, so the evidence is insufficient to advance.

**To proceed, the following is needed:**
- Package insert warnings and contraindications
- Mechanism of action data
- Clinical data on cefazolin in otitis media, including pathogen coverage against *H. influenzae* and *M. catarrhalis*
- Comparison with current standard-of-care antibiotics for otitis media

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cefazolin (cefazolin sodium) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d91a8d13-99a0-4d87-88dc-71cbd37922b4) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

