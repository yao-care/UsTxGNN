---
layout: default
title: Dofetilide
parent: Moderate Evidence (L3-L4)
nav_order: 619
evidence_level: L4
indication_count: 10
monitor_inn: "DOFETILIDE"
predicted_indications: ["stroke disorder", "obsolete susceptibility to ischemic stroke", "ABri amyloidosis", "sick sinus syndrome 2, autosomal dominant", "Wildervanck syndrome", "sarcoglycanopathy", "duodenal obstruction", "brain stem infarction", "macrocephaly, dysmorphic facies, and psychomotor retardation", "cerebrovascular disorder"]
---

# Dofetilide
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

# Dofetilide: From Atrial Fibrillation to Stroke Disorder

## One-Sentence Summary

Dofetilide is an antiarrhythmic drug originally used to treat atrial fibrillation.
The TxGNN model predicts it may be effective for **stroke disorder**, but there are currently **0 registered clinical trials** and **7 publications** (all about atrial fibrillation management, none testing stroke as an outcome), so the evidence is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation |
| Predicted New Indication | Stroke disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 9 authorizations (1 NDA and 8 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, dofetilide is a selective blocker of the IKr potassium current (Kv11.1/hERG) and is used for rhythm control in atrial fibrillation.

The link between the two conditions is indirect. Stroke is a downstream complication of atrial fibrillation, so maintaining sinus rhythm might lower the risk of clot formation and embolism. However, the retrieved literature covers rhythm management and comparisons of antiarrhythmic drugs. None of it shows that dofetilide prevents stroke. Rhythm control also does not replace anticoagulation.

The very high TxGNN score most likely reflects how closely atrial fibrillation and stroke sit in the knowledge graph, not a new mechanism of action.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26233885](https://pubmed.ncbi.nlm.nih.gov/26233885/) | 2016 | Systematic review / Meta-analysis | Journal of Cardiology | Comparative effectiveness of antiarrhythmic drugs for rhythm control of atrial fibrillation; little comparative data exists to guide drug choice |
| [32538135](https://pubmed.ncbi.nlm.nih.gov/32538135/) | 2020 | Cohort | Circulation: Arrhythmia and Electrophysiology | Dofetilide in AF patients with LVEF ≤35%; assessed LVEF improvement, safety and outcomes |
| [21955243](https://pubmed.ncbi.nlm.nih.gov/21955243/) | 2012 | Cohort | Journal of Cardiovascular Electrophysiology | Dofetilide reduced ventricular arrhythmias and ICD therapies in patients with implanted defibrillators |
| [11174354](https://pubmed.ncbi.nlm.nih.gov/11174354/) | 2001 | Review | American Heart Journal | Pharmacologic strategies for AF, which carries a risk of embolic complications |
| [11445058](https://pubmed.ncbi.nlm.nih.gov/11445058/) | 2001 | Review | Current Treatment Options in Cardiovascular Medicine | Treatment of atrial flutter |
| [20638626](https://pubmed.ncbi.nlm.nih.gov/20638626/) | 2010 | Review | Gender Medicine | Gender differences in atrial fibrillation |
| [32435191](https://pubmed.ncbi.nlm.nih.gov/32435191/) | 2020 | Preclinical (animal) | Frontiers in Pharmacology | KCa2 and Kv11.1 channel inhibition in pigs with left ventricular dysfunction |

None of these studies uses stroke as an endpoint.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020931 | Tikosyn (Pfizer) | Capsule | Not listed (cancelled) |
| ANDA210466 | Dofetilide (Sun Pharmaceutical) | Capsule | Not listed (cancelled) |
| ANDA207058 | Dofetilide (Dr. Reddy's) | Capsule | Not listed (cancelled) |
| ANDA213220 | Dofetilide (Novadoz) | Capsule | Not listed (cancelled) |
| ANDA210740 | Dofetilide (Aurobindo) | Capsule | Not listed (cancelled) |

Four more ANDAs (Accord, Bionpharma, Sigmapharm, Exelan) are also cancelled. All 9 authorizations are in cancelled status.

## Safety Considerations

- **Disease-level cautions from the knowledge graph** (these come from knowledge-graph contraindication links, not from label text): long QT syndrome, familial long QT syndrome, torsades de pointes, kidney disease, liver disease, gallbladder disease, potassium deficiency, pyoureter and anorexia nervosa.
- **Known class concern**: Dofetilide's most concerning adverse effect is QT prolongation with polymorphic ventricular tachycardia (reported in the literature).
- **Case report**: One report (PMID 30700466) describes facial paralysis after cardioversion in a dofetilide-treated patient, initially mistaken for stroke. This is a safety signal or diagnostic confounder, not evidence of benefit.
- **Drug Interactions**: The interaction query returned 100 entries; the first 20 reviewed include many **Major** ones:
  - Hydrocortisone
  - Cimetidine
  - Clarithromycin
  - Cisapride
  - Dolasetron
  - Eliglustat
  - Amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms)
  - Picosulfuric acid
  - Polyethylene glycol (3350 with electrolytes)
  - Moderate interactions include famotidine, metformin, loperamide, aprepitant, bisacodyl, castor oil and clotrimazole. Dexamethasone is Minor.

Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The stroke prediction rests on knowledge-graph proximity to atrial fibrillation. No trials exist, the literature contains no stroke-outcome data, and the drug carries a serious proarrhythmic risk. All US authorizations are also cancelled. The other nine predicted indications are either unsupported by any evidence (L5) or biologically implausible, so none is a better candidate.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a current blocking gap)
- Mechanism of action data to support a mechanistic-link analysis
- Evidence that dofetilide-based rhythm control reduces stroke or cerebrovascular events beyond anticoagulation
- A review of whether the cancelled US market status limits practical development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

