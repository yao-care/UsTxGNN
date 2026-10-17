---
layout: default
title: Maraviroc
parent: Model Prediction Only (L5)
nav_order: 887
evidence_level: L5
indication_count: 10
monitor_inn: "MARAVIROC"
predicted_indications: ["multiple endocrine neoplasia", "acne (disease)", "primary cutaneous T-cell lymphoma", "pediatric systemic lupus erythematosus", "primary cutaneous T-cell non-Hodgkin lymphoma", "primary cutaneous B-cell lymphoma", "candidiasis", "complement component 4a deficiency", "cytomegalovirus infection", "HER2 positive breast carcinoma"]
last_modified_at: 2026-10-14
description: "Maraviroc: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not listed in the data compiled for this report (the drug is known as…"
---

# Maraviroc
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Maraviroc: From HIV-1 Infection to Multiple Endocrine Neoplasia

## One-Sentence Summary

Maraviroc is a CCR5 antagonist that was developed as an antiretroviral for HIV-1 infection. The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**, with a very high score but **no clinical trials and no supporting publications** at present. The prediction is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the data compiled for this report (the drug is known as an HIV-1 CCR5 antagonist) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all listed authorizations are cancelled) |
| Number of NDAs | 4 authorizations (1 NDA, 3 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Maraviroc blocks the chemokine receptor CCR5. Detailed mechanism of action data is not available in the data compiled for this report, so the statement above reflects general knowledge of the drug class. Its efficacy in its original indication rests on this CCR5 blockade, which stops HIV from entering immune cells.

For multiple endocrine neoplasia (MEN), the main disease drivers are genes such as MEN1 and RET. The data compiled for this report establishes no direct link between CCR5 signalling and these pathways. The high TxGNN score therefore reflects a computational pattern in the knowledge graph rather than a demonstrated biological rationale, and the relationship between the original and new indications remains unassessed.

Other predictions for this drug have somewhat more plausible rationales, though none has clinical support:
- **HER2-positive breast carcinoma** (score 99.22%, evidence level L4): a 2020 preclinical study (PMID 32404410) reported that autocrine CCL5 drives trastuzumab resistance through ERK pathway activation. Because CCL5 signals through CCR5, blocking CCR5 with maraviroc is a biologically plausible way to overcome resistance. This is the most mechanistically grounded candidate, but it is indirect and preclinical.
- **Primary cutaneous T-cell lymphoma** and **acne**: chemokine-mediated cell trafficking to the skin gives a speculative hypothesis, with no maraviroc-specific data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for multiple endocrine neoplasia.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022128 | SELZENTRY (A-S Medication Solutions) | Film-coated tablet | Not listed (cancelled) |
| ANDA217880 | Maraviroc (Zydus Pharmaceuticals USA Inc.) | Film-coated tablet | Not listed (cancelled) |
| ANDA217114 | Maraviroc (i3 Pharmaceuticals, LLC) | Film-coated tablet | Not listed (cancelled) |
| ANDA203347 | Maraviroc (Hetero Labs Limited) | Film-coated tablet | Not listed (cancelled) |

All four authorizations are marked as cancelled, and none is currently valid.

## Safety Considerations

- **Disease contraindication signals (knowledge graph, not label text)**: The TxGNN knowledge graph links maraviroc with contraindications in several conditions. These include:
  - Cardiovascular: coronary artery disease, myocardial infarction, myocardial ischemia, coronary thrombosis, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy
  - Liver: liver disease, drug-induced liver injury, chronic hepatitis B virus infection, hepatitis C virus infection
  - Kidney: kidney disease, chronic kidney disease, chronic renal failure syndrome, end-stage renal failure
  - Other: gallbladder disease, hemoglobinopathy, pyoureter, infectious disease
- **Drug Interactions**: 93 interactions were identified, and 20 are listed in the data compiled for this report. The major-level interaction is **clarithromycin**. The moderate-level interactions include aprepitant, dexamethasone, cimetidine, eliglustat, naltrexone, cobicistat, deferasirox, diazoxide, phentolamine, promethazine, clotrimazole, miconazole and rolapitant, among others.

Please refer to the package insert for the official warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for multiple endocrine neoplasia is very high, but there are no clinical trials or publications, and no mechanistic link to MEN pathways has been established. The drug's US authorizations are all cancelled, and the official safety information was not available.

**To proceed, the following is needed:**
- Retrieve the FDA package insert warnings and contraindications, which is a blocking gap for safety screening
- Obtain mechanism of action data from DrugBank to support the mechanistic-link analysis
- Conduct a targeted literature and trial search on CCR5/chemokine signalling in MEN
- Consider prioritising the HER2-positive breast carcinoma hypothesis (CCL5–CCR5 axis in trastuzumab resistance), which has preclinical support, for further research
- Review the cardiovascular, hepatic and renal contraindication signals before any new-indication study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

