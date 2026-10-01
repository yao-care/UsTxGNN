---
layout: default
title: Omadacycline
parent: Moderate Evidence (L3-L4)
nav_order: 991
evidence_level: L4
indication_count: 10
---

# Omadacycline
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

# Omadacycline: From Bacterial Infections (Community-Acquired Bacterial Pneumonia) to Mycoplasma pneumoniae Pneumonia

## One-Sentence Summary

Omadacycline is a tetracycline-class antibiotic marketed in the US as NUZYRA. The literature describes it as approved for adult community-acquired bacterial pneumonia (CABP), and its Phase 3 programs also cover skin infections.
The TxGNN model predicts it may be effective for **Mycoplasma pneumoniae pneumonia**, but there are **0 registered clinical trials** and only **10 publications** (mostly case reports) for this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adult community-acquired bacterial pneumonia (per literature; the license records contain no indication text) |
| Predicted New Indication | Mycoplasma pneumoniae pneumonia |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Omadacycline is an aminomethylcycline, a tetracycline derivative. It binds the 30S ribosomal subunit and is designed to evade common tetracycline efflux and ribosomal-protection resistance. This mechanism description comes from the analysis in the Evidence Pack, not from a curated DrugBank mechanism field.

Mycoplasma pneumoniae has no cell wall, so cell-wall-targeting antibiotics such as beta-lactams do not work against it. It is susceptible to tetracyclines, and omadacycline shows good in vitro activity against atypical pathogens.

The original indication, bacterial pneumonia, and the predicted one are both lower respiratory tract infections. Omadacycline may be useful in macrolide-resistant *M. pneumoniae*, which the case reports suggest. So far this rests on individual cases, not controlled data.

## Clinical Trial Evidence

Currently no related clinical trials registered for Mycoplasma pneumoniae pneumonia.

For indirect context only, omadacycline has completed Phase 3 trials in adult CABP against moxifloxacin ([NCT02531438](https://clinicaltrials.gov/study/NCT02531438), n=774; [NCT04779242](https://clinicaltrials.gov/study/NCT04779242), n=670). These do not test the predicted indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37728376](https://pubmed.ncbi.nlm.nih.gov/37728376/) | 2023 | PK study | Expert Opin Drug Metab Toxicol | Pharmacokinetic evaluation of an oral-only omadacycline regimen for CABP. It notes activity against atypical bacteria and MRSA. |
| [33512346](https://pubmed.ncbi.nlm.nih.gov/33512346/) | 2021 | Review | Med Lett Drugs Ther | Overview of antibacterial drugs for community-acquired pneumonia. No abstract available. |
| [31169800](https://pubmed.ncbi.nlm.nih.gov/31169800/) | 2019 | Review | Med Lett Drugs Ther | Review of omadacycline (Nuzyra) as a new tetracycline antibiotic. No abstract available. |
| [31599865](https://pubmed.ncbi.nlm.nih.gov/31599865/) | 2019 | Review | Med Lett Drugs Ther | Review of lefamulin, a different drug, for CABP. Comparative context only. |
| [37842004](https://pubmed.ncbi.nlm.nih.gov/37842004/) | 2023 | Case report | Front Cell Infect Microbiol | Adolescent with macrolide-unresponsive *M. pneumoniae* pneumonia treated with omadacycline. It notes pediatric safety and efficacy are not established. |
| [39867285](https://pubmed.ncbi.nlm.nih.gov/39867285/) | 2025 | Case report | Infect Drug Resist | Compassionate use in a pre-schooler with Down syndrome and critically ill macrolide-resistant *M. pneumoniae* atypical pneumonia, identified by targeted NGS. |
| [41356655](https://pubmed.ncbi.nlm.nih.gov/41356655/) | 2025 | Case report | Clin Case Rep | 4-year-old with multiple antimicrobial allergies and mixed CAP treated with omadacycline. |
| [41710381](https://pubmed.ncbi.nlm.nih.gov/41710381/) | 2026 | Case report | Infect Drug Resist | Safety signal: an 18-year-old with *M. pneumoniae* pneumonia developed anticardiolipin antibody positivity, raised D-dimer and a hypercoagulable state after IV omadacycline. |
| [39224609](https://pubmed.ncbi.nlm.nih.gov/39224609/) | 2024 | Case report | Front Med | Severe *M. pneumoniae* pneumonia with anti-IgLON5 encephalitis in a teenager. Disease context; the abstract does not describe omadacycline use. |
| [39789442](https://pubmed.ncbi.nlm.nih.gov/39789442/) | 2025 | Case report | BMC Infect Dis | Co-infection with Dabie bandavirus and *M. pneumoniae*. Disease context; the abstract does not describe omadacycline use. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA209816 | NUZYRA | Tablet, film coated (oral) | Paratek Pharmaceuticals, Inc. |
| NDA209817 | NUZYRA | Injection, powder, lyophilized, for solution (injectable) | Paratek Pharmaceuticals, Inc. |

Both oral and injectable forms exist, which allows IV-to-oral step-down.

## Safety Considerations

- **Pediatric use**: The case reports state that safety and efficacy in patients under 18 years have not been established. Most published *M. pneumoniae* cases involve children or adolescents, so this is a key concern.
- **Immune and coagulation signal**: One 2026 case report links omadacycline to new anticardiolipin antibody positivity and a hypercoagulable state. It is a single case and needs monitoring in any further use.

Please refer to the package insert for full warnings, contraindications, and drug interaction information. No drug-interaction records were found in the source data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and the case reports are encouraging, especially for macrolide-resistant strains. However, there are no registered trials for this indication, the evidence is case-level only, and the population in the reports is largely pediatric, where safety is unestablished. Package insert safety data are also missing, so the candidate cannot yet pass safety screening.

The other nine predictions (for example drug-induced osteoporosis, ophthalmic herpes zoster, and infection-related hemolytic uremic syndrome) are Hold with L5 evidence. Most have no credible mechanism, and antibiotics may be harmful in infection-related HUS. Orbital cellulitis is plausible in principle but has no clinical data.

**To proceed, the following is needed:**
- Obtain and parse the US package insert for warnings, contraindications, and approved indication text.
- Supplement curated mechanism of action data from DrugBank.
- Systematically review omadacycline against *M. pneumoniae*, including macrolide-resistant strains, in adults.
- Develop a controlled trial design (for example versus doxycycline or a fluoroquinolone) in adults.
- Assess pediatric safety, including the anticardiolipin and hypercoagulability signal, before any use in children.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

