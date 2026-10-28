---
layout: default
title: Mexiletine
parent: Model Prediction Only (L5)
nav_order: 923
evidence_level: L5
indication_count: 10
monitor_inn: "MEXILETINE"
predicted_indications: ["hypertrichosis (disease)", "nephrogenic syndrome of inappropriate antidiuresis", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "migraine disorder", "isolated genetic hair shaft abnormality", "pulmonary hypertension", "migraine with brainstem aura", "headache disorder"]
last_modified_at: 2026-10-28
description: "Mexiletine: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Mexiletine
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

## Mexiletine: Hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Mexiletine is a class IB sodium channel blocker. The data compiled for this report do not include the text of its US-approved indication, but it is widely known as an oral antiarrhythmic.
The TxGNN model predicts it may be effective for several conditions. The best-supported one is **Headache Disorder**, which has **0 registered clinical trials** and **5 publications** (mostly small, open-label studies and case series).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 (headache disorder); L5 for the top-ranked prediction |
| US Market Status | Marketed (valid licenses on record: at least 5) |
| Number of NDAs | 5 (all cancelled; these are ANDA generic applications) |
| Recommended Decision | Hold (headache disorder may be advanced as a research question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, mexiletine is a class IB sodium channel blocker (related to lidocaine). It is used for ventricular arrhythmias and, in practice, for neuropathic pain and myotonia.

Sodium channel blockade may dampen the hyperexcitability of trigeminal and central pain pathways. Small studies report benefit of mexiletine or intravenous lidocaine in trigeminal autonomic cephalalgias, SUNCT/SUNA, refractory chronic daily headache and vascular headaches. The link to **migraine** itself is more indirect, because the evidence comes from related but different headache subtypes.

- **Hypertrichosis, Ambras-type hypertrichosis, hair shaft abnormality:** structural or genetic hair disorders with no link to sodium channel blockade.
- **Nephrogenic syndrome of inappropriate antidiuresis:** caused by gain-of-function variants in the vasopressin V2 receptor.
- **Developmental malformation syndromes (odontal/periodontal, Dandy-Walker):** structural defects not expected to respond to a sodium channel blocker.
- **Pulmonary hypertension:** only indirect preclinical support, from a study of lidocaine (not mexiletine) as a TMEM16A chloride channel blocker.
- **Migraine with brainstem aura:** a theoretical link through neuronal hyperexcitability only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Publications for the best-supported predictions (headache disorder and migraine):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33361408](https://pubmed.ncbi.nlm.nih.gov/33361408/) | 2021 | Prospective open-label study with single-arm meta-analysis | J Neurol Neurosurg Psychiatry | Medical treatment of SUNCT and SUNA, conditions where evidence-based recommendations are lacking |
| [20425204](https://pubmed.ncbi.nlm.nih.gov/20425204/) | 2010 | Clinical case series / review | Curr Pain Headache Rep | IV lidocaine and mexiletine (class 1B sodium channel blockers) used in trigeminal autonomic cephalalgias |
| [18793209](https://pubmed.ncbi.nlm.nih.gov/18793209/) | 2008 | Case series (9 cases) | Headache | Mexiletine used in a refractory chronic daily headache population |
| [6938859](https://pubmed.ncbi.nlm.nih.gov/6938859/) | 1981 | Early clinical report | N Z Med J | Early report on mexiletine in vascular headaches |
| [40197813](https://pubmed.ncbi.nlm.nih.gov/40197813/) | 2025 | Cochrane review | Cochrane Database Syst Rev | Drug treatment for myotonia; only indirect relevance to headache |

The following publications relate to other predictions and offer only indirect support:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41518899](https://pubmed.ncbi.nlm.nih.gov/41518899/) | 2026 | Preclinical study (lidocaine, not mexiletine) | J Pharmacol Exp Ther | Lidocaine blocks the TMEM16A chloride channel, proposed for pulmonary arterial hypertension |
| [1724233](https://pubmed.ncbi.nlm.nih.gov/1724233/) | 1991 | Clinical study | Int J Cardiol | Disopyramide and mexiletine in 29 patients with ventricular arrhythmias; does not address pulmonary hypertension |

---

## US Market Information

The approved indication text is not available in the compiled data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA214089 | Mexiletine Hydrochloride (Bryant Ranch Prepack) | Capsule | Not available |
| ANDA074450 | Mexiletine Hydrochloride (ANI Pharmaceuticals) | Capsule | Not available |
| ANDA214352 | Mexiletine Hydrochloride (Ingenus Pharmaceuticals) | Capsule | Not available |
| ANDA074377 | Mexiletine Hydrochloride (Teva Pharmaceuticals USA) | Capsule | Not available |
| ANDA216463 | Mexiletine Hydrochloride (Camber Pharmaceuticals) | Capsule | Not available |

---

## Safety Considerations

- **Contraindications (from the TxGNN knowledge graph, not label text):** epilepsy, liver disease, gallbladder disease, hypotensive disorder, myocardial infarction, coronary thrombosis, hemoglobinopathy, atrioventricular block, sick sinus syndrome, familial sick sinus syndrome. These should be verified against the package insert.
- **Drug Interactions:** 100 interactions were identified in total. The 20 retrieved include:
  - **Major:** bupropion.
  - **Moderate:** alosetron, morphine, lorcaserin, potassium citrate, picosulfuric acid, polyethylene glycol (3350 with electrolytes), eliglustat, obeticholic acid, sodium sulfate, glycerol phenylbutyrate, rolapitant.
  - **Minor:** ascorbic acid.
  - **Unknown severity:** omeprazole, sucralfate, vancomycin, nizatidine, simvastatin, potassium chloride, prednisolone.
- **Other considerations:** The literature notes proarrhythmic risk, CNS and GI adverse effects, and a large DDI burden, all of which need careful assessment. Please refer to the package insert for full warnings.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Most predictions, including the top-ranked hypertrichosis, have no clinical or literature support and no plausible mechanism (L5).
- Headache disorder and migraine have only small, uncontrolled, mostly older studies (L3), with no registered trials. They are suitable as a research question, but not for a Go decision.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking gap).
- Mechanism of action data from DrugBank.
- Approved indication text, to confirm the original indication.
- A systematic review of mexiletine in trigeminal autonomic cephalalgias and chronic headache, followed by a controlled trial design if the signal holds.
- A cardiac safety plan (proarrhythmia, conduction block) and a DDI management plan for headache populations.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

