---
layout: default
title: Omadacycline
parent: Model Prediction Only (L5)
nav_order: 991
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
monitor_inn: "OMADACYCLINE"
predicted_indications: ["drug-induced osteoporosis", "orbital cellulitis", "post-infectious syndrome", "postinfectious vasculitis", "post-bacterial disorder", "ophthalmic herpes zoster", "otitis externa", "infective urethral stricture", "infection-related hemolytic uremic syndrome"]
description: "Omadacycline: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Omadacycline
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

## Omadacycline: Drug-induced osteoporosis
{: .text-alpha }

## One-Sentence Summary

Omadacycline is a tetracycline-class antibiotic (aminomethylcycline) originally used to treat bacterial pneumonia and skin infections.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 0.9956 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of NDAs | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Omadacycline is an aminomethylcycline tetracycline. It binds the 30S ribosomal subunit and inhibits bacterial protein synthesis. It is approved for community-acquired bacterial pneumonia and has in vitro activity against atypical pathogens, including *Mycoplasma pneumoniae*.

Macrolide resistance in *M. pneumoniae* is mainly driven by 23S rRNA mutations (such as A2063G). Because omadacycline acts on a different ribosomal target, this resistance mechanism does not affect it. That makes it a plausible second-line option for macrolide-unresponsive cases.

This prediction is closely related to the original pneumonia indication. It is better viewed as an extension within the same disease area than as a distant repurposing. Detailed mechanism-of-action data from DrugBank were not available for this report, so the mechanistic description above relies on the known tetracycline-class pharmacology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42559097](https://pubmed.ncbi.nlm.nih.gov/42559097/) | 2026 | Retrospective cohort | Front Cell Infect Microbiol | IV omadacycline as second-line therapy for macrolide-unresponsive M. pneumoniae pneumonia in children aged 8-16 years; efficacy and short-term safety evaluated |
| [42370222](https://pubmed.ncbi.nlm.nih.gov/42370222/) | 2026 | Clinical study | Infect Drug Resist | Real-world experience with IV omadacycline in patients with M. pneumoniae harboring the 23S rRNA A2063G mutation |
| [37728376](https://pubmed.ncbi.nlm.nih.gov/37728376/) | 2023 | Pharmacokinetic evaluation | Expert Opin Drug Metab Toxicol | Oral-only dosing regimen of omadacycline in community-acquired bacterial pneumonia; active against atypical bacteria and MRSA |
| [37842004](https://pubmed.ncbi.nlm.nih.gov/37842004/) | 2023 | Case report | Front Cell Infect Microbiol | Omadacycline used in an adolescent with macrolide-unresponsive M. pneumoniae pneumonia |
| [39867285](https://pubmed.ncbi.nlm.nih.gov/39867285/) | 2025 | Case report | Infect Drug Resist | Compassionate use in a preschool child with Down syndrome and critical macrolide-resistant M. pneumoniae pneumonia |
| [41356655](https://pubmed.ncbi.nlm.nih.gov/41356655/) | 2025 | Case report | Clin Case Rep | Treatment of community-acquired pneumonia in a 4-year-old with multiple antimicrobial allergies |
| [41710381](https://pubmed.ncbi.nlm.nih.gov/41710381/) | 2026 | Case report and review | Infect Drug Resist | Anticardiolipin antibody positivity and hypercoagulable state after omadacycline in an 18-year-old with M. pneumoniae pneumonia (safety signal) |
| [31169800](https://pubmed.ncbi.nlm.nih.gov/31169800/) | 2019 | Review | Med Lett Drugs Ther | Drug profile of omadacycline (Nuzyra) as a new tetracycline antibiotic |
| [33512346](https://pubmed.ncbi.nlm.nih.gov/33512346/) | 2021 | Review | Med Lett Drugs Ther | Antibacterial drugs for community-acquired pneumonia |
| [42853493](https://pubmed.ncbi.nlm.nih.gov/42853493/) | 2026 | Review | Infection | Recent advances in M. pneumoniae infection from pathogenesis to clinical management |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA209816 | NUZYRA | Tablet, film coated | Not specified (status: valid) |
| NDA209817 | NUZYRA | Injection, powder, lyophilized, for solution | Not specified (status: valid) |

## Safety Considerations

- **Drug Interactions**: 44 interactions were identified in total. The ones listed here are all rated Moderate and involve polyvalent cations and antacids, which commonly reduce absorption of tetracycline-class drugs. Examples include calcium salts (phosphate, acetate, carbonate, chloride, citrate, gluconate, lactate), magnesium salts (oxide, carbonate, chloride, citrate, gluconate), zinc sulfate, aluminum hydroxide, iron, kaolin, attapulgite and magaldrate.
- **Case-report safety signal**: One report describes new anticardiolipin antibody positivity and a hypercoagulable state (raised D-dimer) after starting IV omadacycline, along with gastrointestinal symptoms and rash.
- **Pediatric use**: Safety and efficacy in patients under 18 have not been established. Most of the Mycoplasma evidence comes from children and adolescents, so this gap matters.

Please refer to the package insert for warnings and contraindications, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale is strong and the TxGNN score is very high. However, the supporting evidence is limited to retrospective studies, a pharmacokinetic evaluation, case reports and reviews, with no registered clinical trials. Both US NDAs are cancelled, and label warnings and contraindications were not available, so safety screening cannot yet proceed. The other nine predicted indications (for example drug-induced osteoporosis, orbital cellulitis and ophthalmic herpes zoster) have no clinical evidence and are also on Hold. Infection-related hemolytic uremic syndrome carries a specific safety concern, because antibiotics may increase toxin release.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Full-text review of the two 2026 clinical studies (PMIDs 42559097 and 42370222) to confirm design, sample size and outcomes
- Clarification of the cancelled NDA status and its commercial availability
- A prospective controlled trial in macrolide-resistant *M. pneumoniae* pneumonia, with pediatric safety monitoring
- Review of the anticardiolipin and hypercoagulability signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

