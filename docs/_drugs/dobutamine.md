---
layout: default
title: Dobutamine
parent: Model Prediction Only (L5)
nav_order: 616
evidence_level: L5
indication_count: 10
monitor_inn: "DOBUTAMINE"
predicted_indications: ["alopecia", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "open-angle glaucoma", "Raynaud disease", "primary hereditary glaucoma", "headache disorder", "hypertrichosis (disease)", "migraine disorder"]
last_modified_at: 2026-10-30
description: "Dobutamine: predicted new indication Alopecia (evidence level L5). Approved use: Not available in the data compiled for this report (the drug is gener…"
---

# Dobutamine
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

## Dobutamine: From Acute Cardiac Inotropic Support to Alopecia
{: .text-alpha }

## One-Sentence Summary

Dobutamine is an intravenous beta-1 adrenergic agonist (inotrope), and the data compiled for this report contain no approved-indication text for it.
The TxGNN model predicts it may be effective for **alopecia** with a very high score, but there are **0 clinical trials** and only **1 publication**, a veterinary case report on minoxidil toxicity that does not test dobutamine for hair loss.
This prediction is best regarded as a likely model artifact rather than a genuine repurposing signal. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the drug is generally known as an inotropic agent for cardiac decompensation) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 5 of 5) |
| Number of FDA Applications | 5 (valid: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, dobutamine is a beta-1 adrenergic agonist that increases myocardial contractility and is given only by intravenous infusion.

There is no plausible mechanistic link between this action and hair follicle biology. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The only retrieved paper reports heart failure caused by minoxidil intoxication in a cat, so it concerns minoxidil cardiotoxicity and not a dobutamine benefit.

The other top predictions point the same way:
- **Alopecia areata** is autoimmune (T-cell mediated, JAK/STAT-related), and dobutamine has no known immunomodulatory action.
- **Hypotrichosis simplex of the scalp** and **congenital hypotrichosis milia** are rare genetic conditions with no connecting pathway.
- **Hypertrichosis** is excess hair growth, the opposite of the alopecia prediction, which further suggests the score reflects similarities the model learned between related diseases, not biological evidence.
- **Open-angle glaucoma** and **primary hereditary glaucoma** are not supported either. Beta-blockers lower intraocular pressure, but dobutamine is a beta-1 agonist with potentially opposing effects.
- **Raynaud disease**, **headache disorder** and **migraine** have no established dobutamine role. Headache is a known adverse effect of inotropic and vasodilatory agents rather than a treatable indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The table covers the top prediction, alopecia. No literature tests dobutamine as a treatment for hair loss.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Case report (veterinary) | Journal of Veterinary Cardiology | A young cat developed heart failure from minoxidil intoxication. Dobutamine was used only to treat hypotension. It is not evidence of benefit for alopecia. |

Literature retrieved for lower-ranked predictions is also indirect:
- **Raynaud disease:** a dobutamine stress echocardiography study of restenosis ([10916654](https://pubmed.ncbi.nlm.nih.gov/10916654/)) and an anti-RNP endothelial dysfunction study in lupus ([42373135](https://pubmed.ncbi.nlm.nih.gov/42373135/)). Neither tests dobutamine as a treatment.
- **Headache and migraine:** levosimendan reviews ([14636085](https://pubmed.ncbi.nlm.nih.gov/14636085/), [15725064](https://pubmed.ncbi.nlm.nih.gov/15725064/)), a dobutamine echocardiography safety study ([9137218](https://pubmed.ncbi.nlm.nih.gov/9137218/)) and a porcine meningeal artery study ([17103145](https://pubmed.ncbi.nlm.nih.gov/17103145/)). None shows a dobutamine benefit.

## US Market Information

All five US authorizations are valid, and no approved-indication text is available in the compiled data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA 074086 | Dobutamine (HF Acquisition Co LLC, DBA HealthFirst) | Injection, solution, concentrate | Not available (valid) |
| NDA 020255 | Dobutamine Hydrochloride (HF Acquisition Co LLC, DBA HealthFirst) | Injection | Not available (valid) |
| NDA 020201 | Dobutamine in Dextrose (Hospira, Inc.) | Injection, solution | Not available (valid) |
| ANDA 216131 | Dobutamine (Slate Run Pharmaceuticals) | Injection | Not available (valid) |
| ANDA 074277 | Dobutamine (Hikma Pharmaceuticals USA Inc.) | Injection, solution | Not available (valid) |

All products are injectable only.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease contraindication links, not label text): hypertension and hypertensive disorder, potassium deficiency, atrial fibrillation, aortic stenosis (including aortic valve disease and supravalvular aortic stenosis), myocardial infarction and coronary thrombosis, hemoglobinopathy, and hypertrophic cardiomyopathy (including the familial form).
- **Drug interactions:** 100 interactions were identified, and the 20 shown in the compiled data are all rated Moderate. Main groups:
  - Antidiabetic agents: acarbose, metformin, pioglitazone, repaglinide, chlorpropamide, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), DPP-4 inhibitors (alogliptin, linagliptin), GLP-1 agonists (albiglutide, dulaglutide, liraglutide, semaglutide) and insulins (aspart, degludec).
  - Sympathomimetic anorectics: phentermine and diethylpropion.
  - Others: cimetidine and vancomycin.

Please refer to the package insert for label warnings and contraindications, which could not be retrieved for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials and no supporting literature, and no plausible mechanism links a beta-1 agonist given by IV infusion to hair loss. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. In addition, all five US licenses are valid, and label safety data are missing.

**To proceed, the following is needed:**
- Mechanism of action data and a credible hypothesis linking dobutamine to hair follicle biology (otherwise discontinue this line)
- FDA package insert warnings and contraindications, which block safety screening
- Preclinical evidence (for example, in vitro or animal hair-growth models) before any clinical consideration
- Route-compatibility assessment, since dobutamine is available only as an IV infusion and would be impractical for a chronic condition such as alopecia
- Review of the original approved indication text, which is missing from the compiled data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

