---
layout: default
title: Ampicillin
parent: Moderate Evidence (L3-L4)
nav_order: 335
evidence_level: L4
indication_count: 10
---

# Ampicillin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Ampicillin: From Bacterial Infections to Laryngitis

## One-Sentence Summary

Ampicillin is a beta-lactam antibiotic given by injection, and the US label data supplied do not list a specific approved indication.
The TxGNN model predicts it may be effective for **laryngitis**, but only **1 loosely related clinical trial** (about a different drug) and **no ampicillin-specific studies** support this.
Most of the 20 publications are case reports and reviews of bacterial complications such as epiglottitis and laryngeal abscess, not laryngitis treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license data provided (ampicillin is an antibacterial for susceptible bacterial infections) |
| Predicted New Indication | Laryngitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the input. Ampicillin is a beta-lactam that inhibits penicillin-binding proteins and bacterial cell wall synthesis. This kills susceptible bacteria and could help in rare bacterial forms of laryngitis, such as epiglottitis or laryngeal abscess.

Most laryngitis is viral, and antibiotics do not treat viral infections. The very high graph score (99.97%) most likely reflects the general antibacterial class rather than a specific effect of ampicillin on the larynx. The prediction is therefore mechanistically plausible only for a small bacterial subset of laryngitis, not for the condition as a whole.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01406275](https://clinicaltrials.gov/study/NCT01406275) | N/A | Completed | 363 | Post-marketing surveillance of amoxicillin/clavulanate (a different drug) in Japanese children. Laryngitis was one of many listed indications. It is non-randomized and yields no ampicillin-specific outcome. |

## Literature Evidence

No randomized trials were found. The papers below are the most relevant of the 20 retrieved, and none tests ampicillin for laryngitis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39879424](https://pubmed.ncbi.nlm.nih.gov/39879424/) | 2025 | Guideline quality appraisal | CoDAS | Assesses the methodological quality of clinical guidelines for laryngitis and pharyngitis (AGREE II) |
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | Case report/Review | Ann Otol Rhinol Laryngol | Spontaneous laryngeal abscess is rare in the antibiotic era. Presents a case with uncontrolled diabetes and a review of modern cases |
| [34986973](https://pubmed.ncbi.nlm.nih.gov/34986973/) | 2023 | Case report/Review | Auris Nasus Larynx | COVID-19 presenting as acute epiglottitis, illustrating a viral cause of acute laryngeal inflammation |
| [30579693](https://pubmed.ncbi.nlm.nih.gov/30579693/) | 2019 | Case report | Auris Nasus Larynx | Laryngeal actinomycosis in a 14-year-old after bone marrow transplantation |
| [25944348](https://pubmed.ncbi.nlm.nih.gov/25944348/) | 2015 | Observational | Otolaryngol Head Neck Surg | Perioperative antibiotic choice in laryngectomy was associated with surgical-site infection and other complications. This is a surgical prophylaxis setting |
| [38145982](https://pubmed.ncbi.nlm.nih.gov/38145982/) | 2024 | Observational | Eur Arch Otorhinolaryngol | Microbiology and antibiotic selection strategy in neck abscesses in patients with diabetes |
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | Review | Anaesth Intensive Care | Review of 161 children with acute epiglottitis: 45 complications and 5 deaths, with emphasis on airway management |
| [2603419](https://pubmed.ncbi.nlm.nih.gov/2603419/) | 1989 | Case series | West J Med | Nine adults with acute epiglottitis: 4 needed intubation and 6 were misdiagnosed at first presentation |
| [3347186](https://pubmed.ncbi.nlm.nih.gov/3347186/) | 1988 | Case reports | Med J Aust | Three adult epiglottitis cases, with discussion of diagnostic difficulty |
| [6465636](https://pubmed.ncbi.nlm.nih.gov/6465636/) | 1984 | Case reports | Ann Emerg Med | Three adult epiglottitis cases, with a risk of acute airway obstruction |

## US Market Information

The source data list 20 US licenses, all generic ANDAs, and give no approved-indication text. The first 5 are shown.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA062719 | Ampicillin | Injection, powder, for solution | Fresenius Kabi USA, LLC |
| ANDA062738 | Ampicillin | Injection, powder, for solution | Sandoz Inc |
| ANDA062772 | Ampicillin | Injection, powder, for solution | Medical Purchasing Solutions, LLC |
| ANDA090354 | Ampicillin | Powder, for solution | Heritage Pharmaceuticals Inc. d/b/a Avet Pharmaceuticals Inc. |
| ANDA061395 | Ampicillin | Injection, powder, for solution | Sandoz Inc |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is model prediction plus indirect literature (L4). The only registered trial concerns a different drug in a mixed-indication surveillance study, and no source tests ampicillin in laryngitis. Most laryngitis is viral, so any benefit would be limited to rare bacterial subtypes. Among the other predicted indications, gonococcal urethritis has the most direct ampicillin evidence (historical comparative studies). Widespread resistance has made that use obsolete, so it is historical use rather than a repurposing opportunity.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the FDA label
- Ampicillin-specific clinical data in bacterial laryngitis, epiglottitis, or laryngeal abscess, defined by pathogen
- Local susceptibility and beta-lactamase data for the relevant pathogens
- Detailed mechanism-of-action data from DrugBank
- Drug-interaction data (the query returned no results)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

