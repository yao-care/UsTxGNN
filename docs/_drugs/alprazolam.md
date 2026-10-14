---
layout: default
title: Alprazolam
parent: Moderate Evidence (L3-L4)
nav_order: 268
evidence_level: L4
indication_count: 3
---

# Alprazolam
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Alprazolam: From Anxiety Disorder to Insomnia

## One-Sentence Summary

Alprazolam is a benzodiazepine originally used to treat anxiety disorders and mixed anxiety and depressive disorder.
The TxGNN model predicts it may be effective for **insomnia**, but there are **no registered clinical trials** and only **indirect literature** (no dedicated insomnia RCT of alprazolam) behind this prediction.
Two lower-ranked predictions were also generated: agoraphobia, which has more supporting literature but largely overlaps the existing anxiety/panic use, and benign paroxysmal torticollis of infancy, which has no evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorder (the supplied U.S. license records do not include indication text) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 7 license records (all cancelled; 2 are NDAs and 5 are ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general benzodiazepine pharmacology, alprazolam enhances GABA-A receptor signaling, which produces sedative-hypnotic and anxiolytic effects. This is a plausible basis for treating insomnia, particularly insomnia that occurs together with anxiety.

Anxiety and insomnia often coexist, and the same sedative effect that relieves anxiety could help sleep. However, this link rests on general class pharmacology rather than on supplied data. The very high TxGNN score is a computational prediction only.

The supplied literature does not include a dedicated insomnia trial of alprazolam. It consists mostly of panic disorder reviews, benzodiazepine utilization studies, and pharmacokinetic reviews. The one study that used alprazolam in insomnia combined it with acupuncture-based therapy, so the drug effect cannot be isolated. Benzodiazepine hypnotics also carry known risks (dependence, falls, cognitive impairment).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The table lists the most relevant publications for insomnia. Because none is a dedicated alprazolam insomnia trial, they are indirect support at best.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | Retrospective observational study | Medicine | 116 patients with coronary heart disease and insomnia; alprazolam was the control treatment against Du Meridian moxibustion plus ear acupuncture. The drug's own effect cannot be isolated. |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharmaceutica | Tranquilizers in elderly patients with chronic diseases, assessed by dose, outcomes, and adverse effects. |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | Pharmacokinetics of anxiolytic drugs. |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Predictive modeling | Value Health Reg Issues | Benzodiazepine use trends and economic burden; long-term use is linked to memory loss, dependence, and falls. |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | Preclinical (mouse) | Aging | Repeated alprazolam administration caused mitochondrial dysfunction and impaired hippocampus-dependent memory. |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Prescription pattern study | Sleep Medicine | Characteristics of prescriptions for insomnia in a managed-care population. |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Cross-sectional | Medicine | Insomnia among COVID-19 survivors; not specific to alprazolam. |
| [35493764](https://pubmed.ncbi.nlm.nih.gov/35493764/) | 2022 | Cohort | JHEP Reports | Zolpidem deprescribing reduced falls and fractures in cirrhosis; not an alprazolam study. |

---

## US Market Information

All seven license records are cancelled, and the supplied data contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA074342 | Alprazolam (Bryant Ranch Prepack) | Tablet | Not available |
| ANDA203346 | Alprazolam (NuCare Pharmaceuticals) | Tablet | Not available |
| NDA018276 | Alprazolam (Mylan) | Tablet | Not available |
| ANDA090871 | Alprazolam (Bryant Ranch Prepack) | Extended-release tablet | Not available |
| NDA021434 | Xanax (Viatris Specialty) | Extended-release tablet | Not available |

Two further cancelled records (ANDA200739, Natco, tablet; ANDA078088, Endo, orally disintegrating tablet) are not listed.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** the TxGNN knowledge graph links alprazolam to contraindications in kidney disease, liver disease, gallbladder disease, open-angle and angle-closure glaucoma, obesity, obstructive sleep apnea and other sleep apnea syndromes, congenital central hypoventilation syndrome, and substance-related disorder or abuse/dependence. These need verification against the official label.
- **Drug interactions:** 100 interactions were found. The sample reviewed includes:
  - **Major:** morphine and liposomal morphine (additive central nervous system and respiratory depression).
  - **Moderate:** aprepitant, bupropion, cimetidine, clarithromycin, clotrimazole, dronabinol, eliglustat, glycerol phenylbutyrate, metoclopramide, and miconazole.
  - **Minor:** several antacids (aluminum hydroxide, calcium carbonate, magnesium salts, magaldrate) and corticosteroids (betamethasone, dexamethasone).
- **Literature-reported risks:** dependence, withdrawal and rebound symptoms, falls, cognitive and memory impairment, and behavioral toxicity.

Please refer to the package insert for official warnings and contraindications, which were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction is supported only by a computational score and indirect literature, with no registered trials and no dedicated alprazolam insomnia study. The known risks of benzodiazepine hypnotic use and the fact that all U.S. licenses are cancelled further limit practical feasibility.

**Other predictions:**
- **Agoraphobia (score 99.56%, evidence level L2):** the literature is more substantial, including a Cochrane network meta-analysis of panic disorder treatments and several alprazolam studies in panic disorder with agoraphobia. However, this largely overlaps alprazolam's existing anxiety and panic use rather than being a truly new indication, and current guidelines generally favor SSRIs/SNRIs and CBT over long-term benzodiazepines. It is best treated as a research question.
- **Benign paroxysmal torticollis of infancy (score 99.61%, evidence level L5):** there is no trial, no literature, and no mechanistic support, and benzodiazepine use in infants raises safety concerns. Hold.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Randomized controlled evidence of alprazolam specifically in insomnia, including comparison with established hypnotics
- A benefit-risk assessment covering dependence, falls, and cognitive effects, especially in older patients
- Clarification of the regulatory and commercial path, since no valid U.S. license is currently on record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

