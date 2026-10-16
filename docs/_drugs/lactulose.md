---
layout: default
title: Lactulose
parent: Moderate Evidence (L3-L4)
nav_order: 829
evidence_level: L3
indication_count: 8
monitor_inn: "LACTULOSE"
predicted_indications: ["acute urate nephropathy", "nephrolithiasis", "obstructive jaundice", "bile duct disease", "biliary tract disease", "hyperphosphatemia (disease)", "exercise-induced malignant hyperthermia", "bile duct neoplasm"]
---

# Lactulose
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **8** 
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

# Lactulose: From Hepatic Encephalopathy to Obstructive Jaundice

## One-Sentence Summary

Lactulose is a non-absorbed disaccharide, originally used to treat hepatic encephalopathy, hepatic coma and constipation.
The TxGNN model predicts it may be useful for **obstructive jaundice** (the top-ranked prediction, acute urate nephropathy, has no supporting evidence, so the best-supported candidate is reported here), with **0 registered clinical trials** and **20 publications** currently supporting this direction, mostly older and small studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatic encephalopathy, hepatic coma, constipation (the US label text was not available) |
| Predicted New Indication | Obstructive jaundice (best-supported; the TxGNN top-ranked prediction is acute urate nephropathy) |
| TxGNN Prediction Score | 99.53% (obstructive jaundice); 99.89% (acute urate nephropathy, no evidence) |
| Evidence Level | L3 |
| US Market Status | Cancelled only (all 8 ANDAs are listed as cancelled) |
| Number of NDAs | 8 (all are ANDAs, all cancelled) |
| Recommended Decision | Hold (the indication is a research question, not ready for development) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, lactulose is a non-absorbed disaccharide that acts in the colon. It works as an osmotic laxative and traps ammonia by acidifying the gut, which is the basis for its use in hepatic encephalopathy.

Obstructive jaundice reduces the amount of bile salts reaching the gut. This impairs the intestinal barrier and promotes bacterial translocation and endotoxaemia. Endotoxaemia contributes to postoperative renal dysfunction and liver injury. Oral lactulose may bind endotoxin, lower luminal pH, alter gut flora and help restore barrier function. This gut-focused mechanism is consistent with how lactulose is already used in liver disease.

Note that the TxGNN top-ranked prediction, acute urate nephropathy (score 99.89%), has no trials or literature. Lactulose has no known effect on uric acid handling, so the score is a model output only. The same applies to nephrolithiasis and exercise-induced malignant hyperthermia, which have no data or plausible mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The most relevant publications for obstructive jaundice are shown below. Study designs are taken from titles and abstracts and have not been fully verified.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2032107](https://pubmed.ncbi.nlm.nih.gov/2032107/) | 1991 | Multicentre prospective randomized study | Br J Surg | 102 patients randomized to preoperative lactulose, sodium deoxycholate or no treatment, to prevent postoperative renal dysfunction |
| [3768644](https://pubmed.ncbi.nlm.nih.gov/3768644/) | 1986 | Experimental and clinical study | Br J Surg | In 24 surgical patients, preoperative lactulose reduced endotoxaemia versus controls |
| [12957136](https://pubmed.ncbi.nlm.nih.gov/12957136/) | 2003 | Mechanistic study (rabbit) | J Surg Res | Lactulose and endotoxaemia/bacterial translocation after bile duct ligation |
| [8944448](https://pubmed.ncbi.nlm.nih.gov/8944448/) | 1996 | Clinical and experimental study | Br J Surg | Intestinal barrier dysfunction in obstructive jaundice, reversed by internal biliary drainage |
| [23297639](https://pubmed.ncbi.nlm.nih.gov/23297639/) | 2012 | Clinical study | Zh Mikrobiol Epidemiol Immunobiol | Bile duct decompression plus lactulose and effects on gut microecology |
| [9145459](https://pubmed.ncbi.nlm.nih.gov/9145459/) | 1997 | Review | Scand J Gastroenterol Suppl | A renoprotective effect of lactulose has not been conclusively shown in clinical studies |
| [15782993](https://pubmed.ncbi.nlm.nih.gov/15782993/) | 2005 | Review | Hepatogastroenterology | Argues for hydration and lactulose before surgery to prevent renal dysfunction |
| [10576346](https://pubmed.ncbi.nlm.nih.gov/10576346/) | 1999 | Animal study (rat) | Hepatogastroenterology | Effects of lactulose, deoxycholate and glutamine on bacterial translocation |
| [12598962](https://pubmed.ncbi.nlm.nih.gov/12598962/) | 2002 | Animal study (rat) | Pediatr Surg Int | Melatonin and lactulose effects on liver and kidneys |
| [2614579](https://pubmed.ncbi.nlm.nih.gov/2614579/) | 1989 | Animal study (rat) | J Pathol | Lactulose did not prevent bile infarction or transaminase elevation (negative finding) |

The evidence is mixed: some studies show reduced endotoxaemia, but one animal study and one review report no clear protective effect. Effect sizes could not be confirmed from the available abstracts.

## US Market Information

All eight US authorizations are single-ingredient ANDAs and all are listed as cancelled. Approved indication text was not available.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA074712 | KRISTALOSE | Powder, for solution | Not available |
| ANDA209517 | Lactulose | Solution | Not available |
| ANDA076645 | Lactulose Solution | Solution | Not available |
| ANDA090502 | Enulose | Solution | Not available |
| ANDA074623 | Lactulose | Solution | Not available |

## Safety Considerations

- **Disease-related cautions (from the knowledge graph, not label text)**: Diabetes mellitus, diabetic ketoacidosis, appendicitis, galactosemia, glycogen storage disease, G6PD deficiency, cystinuria and glucose-galactose malabsorption are listed as contraindication-related conditions.
- **Drug Interactions**: 100 interactions were identified. The sample reviewed was mostly Moderate, with one Minor (sodium citrate). Moderate examples include abiraterone, tramadol, acetazolamide, hydrocortisone, salbutamol, hydrochlorothiazide, amiloride, amiodarone, arsenic trioxide, propofol and triamcinolone.

Please refer to the package insert for label warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction (acute urate nephropathy) has no evidence and no plausible mechanism. The best-supported prediction, obstructive jaundice, rests on small, dated studies with mixed results, no registered trials, and a perioperative supportive rather than disease-treating role. All US licenses are cancelled, and label safety data are missing. This is a research question rather than a development candidate.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Full-text review of the 1991 multicentre study and the 1986 clinical study to confirm design and effect sizes
- A modern, controlled trial of perioperative lactulose in obstructive jaundice with renal and infectious complication endpoints
- Clarification of why all US licenses are cancelled, and route compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

