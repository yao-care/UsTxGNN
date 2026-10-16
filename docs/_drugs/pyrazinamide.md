---
layout: default
title: Pyrazinamide
parent: Model Prediction Only (L5)
nav_order: 1099
evidence_level: L5
indication_count: 10
monitor_inn: "PYRAZINAMIDE"
predicted_indications: ["infectious otitis media", "middle ear disease", "otosalpingitis", "chronic otitis media", "suppurative otitis media", "non-suppurative otitis media", "middle ear cholesterol granuloma", "allergic otitis media", "Lyme disease", "infectious otitis interna"]
last_modified_at: 2026-10-14
description: "Pyrazinamide: predicted new indication Infectious otitis media (evidence level L5). Approved use: Pulmonary tuberculosis, meningeal tuberculosis, tuberculous meningitis"
---

# Pyrazinamide
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

# Pyrazinamide: From Pulmonary Tuberculosis to Infectious Otitis Media

## One-Sentence Summary

Pyrazinamide is an antimycobacterial drug, originally used to treat tuberculosis (pulmonary and meningeal forms).
The TxGNN model predicts it may be effective for **Infectious Otitis Media**, but there are currently **0 clinical trials** and **0 publications** directly supporting this specific prediction. The only related literature (for adjacent middle ear predictions) consists of case reports of tuberculous ear infection, which are an extension of the existing TB indication rather than a new use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis, meningeal tuberculosis, tuberculous meningitis (the US license records contain no indication text) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 3 (all cancelled; listed as ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pyrazinamide is a first-line anti-tuberculosis agent. It is known to be active only against *Mycobacterium tuberculosis*, where it needs an acidic environment and the mycobacterial enzyme pyrazinamidase to become active.

This mechanism does not plausibly extend to the usual bacterial causes of otitis media (*S. pneumoniae*, *H. influenzae*, *M. catarrhalis*). The high TxGNN score most likely reflects a knowledge-graph link to **tuberculous otitis media**, a rare form of extrapulmonary TB that is already treated with standard anti-TB regimens containing pyrazinamide. The prediction is therefore best read as an extension of the existing TB indication, not as a genuinely new use.

Other predicted indications in the ear group (otosalpingitis, non-suppurative, allergic otitis media, middle ear cholesterol granuloma, infectious otitis interna) have no clinical evidence and no plausible mechanistic basis outside tuberculous involvement. Lyme disease (score 99.45%) rests only on an unvalidated hypothesis about persister bacteria; *Borrelia* is not a mycobacterium.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was retrieved for the top-ranked prediction (infectious otitis media). The table below lists the most relevant items found for closely related middle ear predictions; all are low-tier evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26785789](https://pubmed.ncbi.nlm.nih.gov/26785789/) | 2013 | Case report | Int J Mycobacteriol | Nasal and middle ear TB in a 55-year-old woman, treated with rifampicin, isoniazid and pyrazinamide for 9 months; no recurrence after 1 year |
| [15168420](https://pubmed.ncbi.nlm.nih.gov/15168420/) | 2004 | Case report | Am J Kidney Dis | Tuberculous otitis media in a renal transplant recipient after recurrent chronic otitis media treated empirically with antibiotics |
| [41783873](https://pubmed.ncbi.nlm.nih.gov/41783873/) | 2026 | Case report | Cureus | Tuberculous otitis media presenting as otorrhea; delayed diagnosis is common because of its rarity |
| [8011030](https://pubmed.ncbi.nlm.nih.gov/8011030/) | 1994 | Case series | Laryngo- rhino- otologie | 12 patients with TB first found incidentally in the head and neck, including one with middle ear involvement |
| [2527907](https://pubmed.ncbi.nlm.nih.gov/2527907/) | 1989 | Review | Infect Dis Clin North Am | General review of new uses for old antibiotics, including pyrazinamide (not specific to otitis media or Lyme disease) |
| [21439219](https://pubmed.ncbi.nlm.nih.gov/21439219/) | 2011 | Animal study | J Am Assoc Lab Anim Sci | Torticollis in TB-infected mice, including some on pyrazinamide-containing regimens; indirect relevance only |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA081319 | Pyrazinamide (Hikma Pharmaceuticals USA Inc) | Tablet | Not available (cancelled) |
| ANDA080157 | Pyrazinamide (Marlex Pharmaceuticals, Inc) | Tablet | Not available (cancelled) |
| ANDA212541 | Pyrazinamide (Macleods Pharmaceuticals Limited) | Tablet | Not available (cancelled) |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

- **Disease-level cautions (from the knowledge graph, not label text)**: Pyrazinamide is linked to contraindication or caution in liver failure and acute liver failure, liver disease, hepatitis, porphyria (including inherited porphyria and porphyrin metabolism disease), gallbladder disease, diabetes mellitus and diabetic ketoacidosis, gout, peripheral nervous system disease and peripheral neuropathy, substance abuse/dependence, and slow acetylator status. These should be verified against the official label.
- **Drug Interactions**: 56 interactions were identified in total. Those with a Moderate level are **picosulfuric acid** and **naltrexone**. Many others (for example pantoprazole, omeprazole, lansoprazole, prednisone, prednisolone, morphine, vancomycin, amphotericin B, streptomycin, metronidazole, glyburide, acetylsalicylic acid) have an unclassified severity level and need individual review.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a knowledge-graph score; there are no trials or literature for infectious otitis media itself. Pyrazinamide acts only against mycobacteria, so a benefit in common bacterial otitis media is not plausible. The related case reports concern tuberculous otitis media, which is already covered by the existing TB indication. In the US, all three licenses are cancelled, and label safety data are missing.

**To proceed, the following is needed:**
- Confirmation of whether the intended target is tuberculous otitis media (an extension of the existing indication) or non-tuberculous otitis media (no supporting mechanism)
- Mechanism of action data
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Review of the 2 moderate and the unclassified drug interactions
- Any prospective clinical data, if a non-tuberculous use is still to be pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

