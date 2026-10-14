---
layout: default
title: Ozanimod
parent: Moderate Evidence (L3-L4)
nav_order: 1006
evidence_level: L4
indication_count: 1
---

# Ozanimod
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Ozanimod: From Multiple Sclerosis to Progressive Relapsing Multiple Sclerosis

## One-Sentence Summary

Ozanimod is an oral sphingosine 1-phosphate (S1P) receptor modulator, originally used to treat relapsing forms of multiple sclerosis.
The TxGNN model predicts it may be effective for **Progressive Relapsing Multiple Sclerosis**,
but there are currently **0 registered clinical trials** and **18 publications** (mostly reviews and network meta-analyses on MS therapy in general, not direct evidence for this indication), so this remains a computational prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple sclerosis |
| Predicted New Indication | Progressive relapsing multiple sclerosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (the single NDA is cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, ozanimod is an S1P receptor modulator selective for S1P1 and S1P5. S1P1 agonism causes the receptor to be internalized on lymphocytes, which traps them in lymph nodes and reduces the infiltration of autoreactive lymphocytes into the central nervous system (CNS). This is plausibly relevant to the inflammatory component of progressive relapsing MS.

S1P5 is expressed on oligodendrocytes and other CNS cells, and ozanimod is lipophilic and can cross the blood-brain barrier. A direct effect on neurodegeneration or remyelination is therefore theoretically possible, but it has not been demonstrated.

The approved MS indication covers relapsing forms (clinically isolated syndrome, relapsing-remitting disease, and active secondary progressive disease). This overlaps with, but is not identical to, the progressive relapsing phenotype, which is an older classification now generally subsumed under primary progressive MS with active disease. The high TxGNN score is consistent with ozanimod's established use in relapsing MS but is a computational prediction, not clinical evidence. No data support efficacy in progressive disease without relapses or MRI activity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications below is a trial of ozanimod in progressive relapsing MS. They provide context on S1P modulators and MS treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39254048](https://pubmed.ncbi.nlm.nih.gov/39254048/) | 2024 | Network meta-analysis | Cochrane Database Syst Rev | Compares immunomodulators and immunosuppressants in progressive MS; relative benefits and safety remain unclear due to a lack of direct comparison trials |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Network meta-analysis | Cochrane Database Syst Rev | Update on immunomodulators and immunosuppressants for relapsing-remitting MS; relative benefit between therapies remains unclear |
| [32385738](https://pubmed.ncbi.nlm.nih.gov/32385738/) | 2020 | Review (drug approval summary) | Drugs | US FDA approved ozanimod in March 2020 for relapsing forms of MS in adults |
| [33287177](https://pubmed.ncbi.nlm.nih.gov/33287177/) | 2020 | Review | Neurology International | Review of ozanimod disease background, efficacy and side effects in relapsing MS |
| [33797705](https://pubmed.ncbi.nlm.nih.gov/33797705/) | 2021 | Review | CNS Drugs | S1P receptor modulators for MS, starting from fingolimod as the first-in-class agent |
| [31598138](https://pubmed.ncbi.nlm.nih.gov/31598138/) | 2019 | Review | Ther Adv Neurol Disord | Latest therapeutic developments and future directions in progressive MS |
| [36946625](https://pubmed.ncbi.nlm.nih.gov/36946625/) | 2023 | Review (study type not classified) | Expert Opin Pharmacother | Update on S1P receptor modulators (fingolimod, siponimod, ozanimod, ponesimod) in relapsing MS |
| [38162670](https://pubmed.ncbi.nlm.nih.gov/38162670/) | 2023 | Review | Front Immunol | CNS-bioavailable disease-modifying therapies; many therapies have limited efficacy in progressive disease |
| [28812220](https://pubmed.ncbi.nlm.nih.gov/28812220/) | 2017 | Review | Neurotherapeutics | S1P receptor modulators act by sequestering lymphocytes in lymph nodes |
| [37638037](https://pubmed.ncbi.nlm.nih.gov/37638037/) | 2023 | Preclinical study | Front Immunol | S1PR-1/5 modulator RP-101074 showed beneficial effects in a CNS degeneration model (a different compound) |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA209899 (cancelled) | ZEPOSIA (Celgene Corporation) | Capsule | Not listed in the data compiled for this report |

## Safety Considerations

- **Contraindication-related conditions in the knowledge graph** (not label text): obstructive sleep apnea and other sleep apnea syndromes, stroke and cerebrovascular disorders, cerebral infarction, transient ischemic attack, vertebrobasilar insufficiency, myocardial infarction and coronary thrombosis, congestive heart failure, sick sinus syndrome (including familial form), atrioventricular block, sinoatrial block, and hemoglobinopathy. Many of these are cardiac conduction or cardiovascular conditions, consistent with the heart-rate and conduction effects of S1P modulators.
- **Drug Interactions**: 100 interactions were identified. Major-level examples include isometheptene, famotidine, hydrocortisone, triamcinolone, betamethasone, budesonide, bupropion, morphine, lorcaserin, clarithromycin, diethylpropion, dolasetron, palonosetron and phentermine. Moderate-level examples include ranitidine, cimetidine, epinephrine, loperamide, picosulfuric acid and polyethylene glycol with electrolytes.

Please refer to the package insert for the official warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score and mechanistic plausibility (evidence level L4, research-question stage). There are no registered trials, and the supplied literature contains no direct evidence in progressive disease. The existing US NDA is also cancelled, and the package insert safety data are missing.

**To proceed, the following is needed:**
- Official package insert warnings and contraindications (a blocking gap for safety screening)
- Verified mechanism of action data from DrugBank
- Evidence of efficacy in progressive MS without relapses or MRI activity, for example from subgroup analyses of existing trials or a dedicated trial
- Clarification of the phenotype definition (progressive relapsing MS versus active primary progressive MS)
- Clarification of the cancelled US NDA status and current availability of the product
- Review of the cardiovascular and conduction-related safety signals for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

