---
layout: default
title: Ritonavir
parent: Model Prediction Only (L5)
nav_order: 1129
evidence_level: L5
indication_count: 3
monitor_inn: "RITONAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-28
description: "Ritonavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease / AIDS"
---

# Ritonavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Ritonavir: From HIV/AIDS to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Ritonavir is an HIV protease inhibitor and pharmacokinetic booster, originally used to treat HIV infection/AIDS and chronic hepatitis C virus infection (as part of combination regimens).
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, a veterinary indication.
Currently **0 clinical trials** and **0 publications** support this specific prediction, so this is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease / AIDS; chronic hepatitis C virus infection (the approved indication text is not available in the US license records) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 11 of 11) |
| Number of NDAs | 11 (valid: 11) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, ritonavir is an HIV-1 protease inhibitor and a CYP3A4 inhibitor used to boost other antiretrovirals. Its efficacy in HIV/AIDS is established.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV, so a protease-inhibitor mechanism is plausible in principle. However, FIV protease differs from HIV-1 protease in substrate specificity and inhibitor sensitivity, and no data were available to show that ritonavir inhibits it.

The very high TxGNN score most likely reflects network proximity to the approved HIV/AIDS indication, not independent evidence. It should be treated as a hypothesis only.

**Other predictions in the list:**
- **Simian immunodeficiency virus (SIV) infection** (score 0.9992, evidence level L4): Preclinical literature supports biological plausibility. One in vitro study (PMID 12709355) found SIVmac239 was inhibited by ritonavir (EC50 about 13 nM, compared with about 25 nM for HIV-1). SIV is an animal infection, not a human disease indication, so this mainly confirms the known anti-lentiviral mechanism rather than a new human opportunity. The recommendation for this prediction is "Research Question".
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 0.9992, L5): There is no evident mechanistic link to protease or CYP3A4 inhibition, and there are no trials or literature. This is a computational prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (feline acquired immunodeficiency syndrome). No clinical trials were found for the other two predictions either.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For reference, the literature retrieved for the related SIV prediction is preclinical only (animal or in vitro); the titles are truncated, so ritonavir's specific contribution cannot always be confirmed:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | Preclinical (in vitro) | Antimicrob Agents Chemother | SIVmac239 was inhibited by indinavir, saquinavir and ritonavir (ritonavir EC50 about 13 nM vs about 25 nM for HIV-1) |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | Preclinical (in vitro) | Antivir Ther | Susceptibility of HIV-2, SIV and SHIV to approved anti-HIV-1 drugs |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Preclinical (animal) | J Virol Methods | Oral HAART including lopinavir/ritonavir in SHIV-infected macaques and its effect on the CD8 subset |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Preclinical (animal) | PLoS Pathog | Highly intensified ART gave long-term viral suppression in a simian AIDS model |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Preclinical (animal) | J Virol | Rapid viral decay in SIV-infected macaques on quadruple antiretroviral therapy |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Preclinical (animal) | PLoS One | Combination ART plus the HDAC inhibitor SAHA in SIV-infected rhesus macaques |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Review/Preclinical | mBio | Lentiviruses persist in the brain despite effective ART |

## US Market Information

All 11 US licenses are currently valid. The approved indication text is not available in the records. The main authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022417 | Norvir (AbbVie) | Tablet, film coated | Not available |
| NDA209512 | Norvir (AbbVie) | Powder | Not available |
| NDA021906 | Kaletra (lopinavir/ritonavir, AbbVie) | Tablet, film coated | Not available |
| NDA021251 | Kaletra (lopinavir/ritonavir, AbbVie) | Solution | Not available |
| ANDA202573 | Ritonavir (Cipla USA) | Tablet | Not available |

## Safety Considerations

The package insert warnings and contraindications were not available for this report; please refer to the package insert for safety information.

- **Knowledge-graph contraindication signals** (from a drug-disease knowledge graph, not label text): long QT syndrome, torsades de pointes, sudden cardiac arrest, heart conduction disease, atrioventricular block, cardiomyopathy, myocardial ischemia, coronary artery disease, pancreatitis, liver disease, cirrhosis of liver, gallbladder disease, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, hypertriglyceridemia, familial combined hyperlipidemia, gout, hyperbilirubinemia (including Gilbert syndrome), potassium deficiency, chronic hepatitis B virus infection, and hemophilia.
- **Drug interactions** (DDInter; 100 interactions found, 20 shown in the data compiled for this report):
  - **Major**: loperamide, triamcinolone, budesonide
  - **Moderate**: acarbose, metformin, alogliptin, albiglutide, canagliflozin, chlorpropamide, hydrocortisone, dexamethasone, betamethasone, alosetron, bupropion, aprepitant, lorcaserin, metronidazole, clarithromycin
  - Ritonavir is a strong CYP3A4 inhibitor, which is consistent with the many interactions listed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (feline AIDS) is a veterinary indication with no clinical trials and no literature, so its evidence level is L5. Its score of 0.9992 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The related SIV prediction has only preclinical support (L4), and the third prediction has no identifiable mechanistic link. In addition, the drug is marketed in the US with 11 valid licenses out of 11, and the safety data are incomplete.

**To proceed, the following is needed:**
- FIV protease inhibition data for ritonavir (in vitro susceptibility and in vivo studies in cats)
- Mechanism of action data (MOA)
- FDA package insert warnings and contraindications (currently a blocking gap for safety screening)
- Clarification of the US regulatory status and the approved indication text
- Confirmation of whether a veterinary indication is within the scope of the repurposing programme (the SIV findings are best treated as a research question rather than a human indication)
- Independent target or pathway validation before pursuing the neurodevelopmental disorder prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

