---
layout: default
title: Ampicillin
parent: Model Prediction Only (L5)
nav_order: 335
evidence_level: L5
indication_count: 9
monitor_inn: "AMPICILLIN"
predicted_indications: ["laryngitis", "Ureaplasma urethritis", "chronic rhinosinusitis", "chronic ethmoidal sinusitis", "gingivitis", "paranasal sinus neoplasm (disease)", "bacterial arthritis", "conjunctivitis", "pericoronitis"]
last_modified_at: 2026-10-30
description: "Ampicillin: predicted new indication laryngitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Ampicillin
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

## Ampicillin: Beta-lactam penicillin antibiotic → laryngitis
{: .text-alpha }

## One-Sentence Summary

Ampicillin is a beta-lactam (aminopenicillin) antibiotic. The TxGNN model predicts it may be useful for **laryngitis**, but this rests on **0 registered clinical trials** and **19 publications**, which are mostly case reports, case series and reviews of related bacterial laryngeal infections (epiglottitis, laryngeal abscess). None is a controlled study of ampicillin for laryngitis itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | laryngitis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 9) |
| Number of FDA Applications | at least 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. As a general property of the class, ampicillin is a beta-lactam that interferes with bacterial cell wall synthesis. It is active against many common respiratory pathogens, such as streptococci and susceptible *Haemophilus influenzae*.

That activity makes use in bacterial infections of the larynx plausible, for example epiglottitis or laryngeal abscess. However, most laryngitis is viral and non-bacterial, so any benefit would be limited to a bacterial subset. Ampicillin has also been largely replaced by other agents for epiglottitis, and ampicillin-resistant *H. influenzae* type b has been reported. Several retrieved papers are off-topic (Whipple's disease, canine neck infections, experimental otitis media).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No retrieved study directly tests ampicillin for laryngitis. The table lists the most relevant items, which address related bacterial laryngeal conditions.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | Review | Anaesth Intensive Care | 161 children with acute epiglottitis; 45 complications and 5 deaths; airway management is the priority |
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | Review/Case report | Ann Otol Rhinol Laryngol | Spontaneous laryngeal abscess case with review of reported cases |
| [3026014](https://pubmed.ncbi.nlm.nih.gov/3026014/) | 1986 | Review | Rev Infect Dis | Sulbactam/ampicillin for pediatric epiglottitis; up to 25% of Hib strains produce beta-lactamase |
| [3290661](https://pubmed.ncbi.nlm.nih.gov/3290661/) | 1988 | Case series | Monatsschr Kinderheilkd | 27 children with epiglottitis; therapy changed after ampicillin-resistant Hib appeared |
| [6881564](https://pubmed.ncbi.nlm.nih.gov/6881564/) | 1983 | Case series | Anesth Analg | 23 children with epiglottitis treated with ampicillin or chloramphenicol; intubation duration reviewed |
| [3322611](https://pubmed.ncbi.nlm.nih.gov/3322611/) | 1987 | Case series | Clin Otolaryngol | 19 adults with epiglottitis; bacteriology and therapeutic principles |
| [2603419](https://pubmed.ncbi.nlm.nih.gov/2603419/) | 1989 | Review | West J Med | 9 adults with epiglottitis; intubation required in 4 |
| [25944348](https://pubmed.ncbi.nlm.nih.gov/25944348/) | 2015 | Cohort | Otolaryngol Head Neck Surg | Perioperative antibiotic choice in laryngectomy linked to complications |
| [38145982](https://pubmed.ncbi.nlm.nih.gov/38145982/) | 2024 | Cohort | Eur Arch Otorhinolaryngol | Microbiology and antibiotic selection in neck abscesses in diabetes |
| [39879424](https://pubmed.ncbi.nlm.nih.gov/39879424/) | 2025 | Guideline appraisal | CoDAS | Quality assessment of laryngitis and pharyngitis guidelines (AGREE II) |

## US Market Information

The data compiled for this report lists 10 US authorizations for single-ingredient ampicillin (ANDA records, injectable powder for solution and one powder for solution). The list may be partial. The records carry no approved-indication text.

| Authorization Number | Manufacturer | Dosage Form |
|---------|------|------|
| ANDA062719 | Fresenius Kabi USA, LLC | Injection, powder, for solution |
| ANDA062738 | Sandoz Inc | Injection, powder, for solution |
| ANDA062772 | Medical Purchasing Solutions, LLC | Injection, powder, for solution |
| ANDA090354 | Heritage Pharmaceuticals Inc. d/b/a Avet Pharmaceuticals Inc. | Powder, for solution |
| ANDA061395 | Sandoz Inc | Injection, powder, for solution |

## Safety Considerations

Package insert warnings and contraindications are not available in the data compiled for this report; please refer to the package insert.

- **Drug Interactions**: 61 interactions were recorded. Moderate-level ones include doxycycline, minocycline, tetracycline, kanamycin, balsalazide, lansoprazole, dexlansoprazole and picosulfuric acid. Clarithromycin is minor. Others, such as vancomycin, morphine, omeprazole and prednisone, are of unknown severity.
- **Conditions of concern in the drug-disease data**: kidney disease and impaired renal function, hematologic disease, peptic ulcer disease, *Clostridium difficile* colitis, infectious mononucleosis, chronic Epstein-Barr virus infection syndrome, perinatal necrotizing enterocolitis, pyoureter and acute urate nephropathy. These are not label text and need confirmation against the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but no cited study directly addresses laryngitis. The literature covers only related bacterial conditions (mainly epiglottitis), most laryngitis is viral, and ampicillin has largely been superseded for epiglottitis. Evidence is therefore at the model-prediction level (L5).

**To proceed, the following is needed:**
- Controlled clinical data on ampicillin in bacterial laryngitis or related laryngeal infections
- Definition of the bacterial subset that would be targeted, with current local resistance data
- Package insert warnings and contraindications for safety screening
- Mechanism-of-action data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

