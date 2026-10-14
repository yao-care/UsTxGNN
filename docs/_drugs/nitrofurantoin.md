---
layout: default
title: Nitrofurantoin
parent: Model Prediction Only (L5)
nav_order: 971
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
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

# Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin is an antibacterial drug. The data compiled for this report do not list an approved indication text, but its use in urinary tract infections is evident from the literature.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but there are **0 clinical trials** and no literature showing therapeutic benefit.
The retrieved publications mostly describe harm, such as drug-induced pulmonary fibrosis and a methotrexate interaction, so this prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license data (the literature describes use in urinary tract infection) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 12 (1 NDA and 11 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, nitrofurantoin is an antibacterial agent with no recognised anti-inflammatory or immunomodulatory action relevant to rheumatoid arthritis (RA).

The high TxGNN score (0.999) is not backed by any clinical signal. The retrieved literature concerns harm rather than benefit:
- Drug-induced pulmonary fibrosis and interstitial lung disease associated with nitrofurantoin.
- A case of irreversible pulmonary fibrosis from a methotrexate–nitrofurantoin interaction in an RA patient.
- A large cohort study linking antibiotic exposure to RA flares.

The prediction is therefore best read as a statistical association in the knowledge graph, not a plausible therapeutic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort | Scientific Reports | Self-controlled case series in about 32,000 newly diagnosed RA patients examining the link between antibiotic use and RA flares |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | A 94-year-old woman on methotrexate for RA developed irreversible pulmonary fibrosis after nitrofurantoin for urinary tract infections |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Drug-induced pulmonary fibrosis; nitrofurantoin is listed as a cause, and RA is a predisposing systemic disease |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du Praticien | Drug-induced interstitial lung disease; nitrofurantoin is among the implicated antibiotics |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | Poor prognosis in RA patients hospitalised for interstitial lung fibrosis (not drug-specific) |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case report | Cureus | Autoimmune hepatitis versus drug-induced liver injury; nitrofurantoin is named as a cause to rule out |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case report | Annales de Dermatologie et de Vénéréologie | Phenylbutazone-induced sialadenitis; nitrofurantoin is mentioned as another reported cause |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case report | Revue de Pneumologie Clinique | Gold salt-induced pneumonitis with CD4 alveolitis (no direct nitrofurantoin finding) |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Other | Acta Medica Scandinavica | Short-term nitrofurantoin therapy for bacteriuria in middle-aged women (no RA finding) |

None of these publications shows a therapeutic benefit of nitrofurantoin in RA.

## US Market Information

All 12 licenses are listed as cancelled, and no approved indication text is available in the data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA016620 | Nitrofurantoin Macrocrystals (Proficient Rx LP) | Capsule | Not available |
| ANDA073652 | Nitrofurantoin (Bryant Ranch Prepack) | Capsule | Not available |
| ANDA073671 | Nitrofurantoin Macrocrystals (AvPAK) | Capsule | Not available |
| ANDA203233 | Nitrofurantoin macrocrystals (Lupin) | Capsule | Not available |
| ANDA201693 | Nitrofurantoin (Novel Laboratories) | Suspension | Not available |

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text)**: renal impairment and anuria, G6PD deficiency, interstitial lung disease and pulmonary fibrosis, peripheral neuropathy, drug-induced liver injury, hepatitis, obstructive jaundice and biliary tract disease, diabetes mellitus and diabetic ketoacidosis, optic neuritis, vitamin B12 and other B-vitamin deficiencies, *Clostridium difficile* colitis, and several metabolic disorders (cystinuria, galactosemia, glycogen storage disease).
- **Safety signals in the literature**: pulmonary fibrosis (including the methotrexate interaction in RA), drug-induced liver injury, and hemolytic anaemia with methemoglobinemia in G6PD deficiency.
- **Drug Interactions**: 100 interactions were found. Moderate-level examples include metronidazole, balsalazide, picosulfuric acid, naltrexone, rosuvastatin and simvastatin. Minor-level examples include anticholinergics (atropine, hyoscyamine, glycopyrronium, dicyclomine, scopolamine) and magnesium-containing antacids.

Please refer to the package insert for label warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no clinical trials and no literature showing benefit. The available evidence points to harm: pulmonary toxicity (particularly alongside methotrexate, a standard RA drug), liver injury, and a possible link between antibiotic exposure and RA flares. No US license is currently valid either.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, and any plausible anti-inflammatory rationale for RA
- Preclinical evidence of disease-modifying activity in RA models
- A review of the safety signals, especially the methotrexate interaction and pulmonary toxicity, before any further consideration

Other predicted indications (for example the rare genetic syndromes, gout and sclerosing cholangitis) also have no supporting evidence. For methemoglobinemia, the literature shows nitrofurantoin as a cause, so that prediction should be treated as a safety signal and not a treatment opportunity.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

