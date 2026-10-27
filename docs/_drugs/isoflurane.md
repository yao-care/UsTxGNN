---
layout: default
title: Isoflurane
parent: Model Prediction Only (L5)
nav_order: 813
evidence_level: L5
indication_count: 7
monitor_inn: "ISOFLURANE"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "manic bipolar affective disorder", "trichotillomania", "dysthymic disorder", "nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder"]
last_modified_at: 2026-10-14
description: "Isoflurane: predicted new indication Migraine disorder (evidence level L5). Approved use: General anesthesia"
---

# Isoflurane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Isoflurane: From General Anesthesia to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Isoflurane is an inhaled volatile general anesthetic. The TxGNN model's top-ranked prediction is Prinzmetal angina, but the only prediction with meaningful supporting evidence is **Migraine Disorder** (score 99.06%). That evidence consists of **0 registered clinical trials** and **12 publications**, mostly preclinical studies plus two case reports of the same patient. This report therefore evaluates migraine disorder as the lead repurposing direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anesthesia (inferred from the drug class; the US license records contain no indication text) |
| Predicted New Indication | Migraine disorder (the highest-ranked prediction, Prinzmetal angina, has no supporting evidence) |
| TxGNN Prediction Score | 99.06% (migraine disorder); 99.67% (Prinzmetal angina, rank 1) |
| Evidence Level | L4 (preclinical and case-level evidence only) |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 5 licenses (1 NDA, 4 ANDAs), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this drug in the data compiled for this report. Isoflurane is a volatile general anesthetic. Related prediction rationales point to GABA-A receptor potentiation and NMDA receptor inhibition, but these have not been confirmed here.

The link to migraine runs through cortical spreading depression (CSD), the wave of neuronal depolarization that underlies migraine aura. A 1996 animal study (PMID 8665587) reported that inhalational anesthetics inhibit spreading depression and discussed the relevance to migraine. NMDA receptor antagonists have also been shown to suppress CSD in rats. Because isoflurane acts on both GABA-A and NMDA pathways, a suppressive effect on CSD is biologically plausible.

Clinically, two case reports (one published in both English and Portuguese) describe status migrainosus treated with general anesthesia that included isoflurane. This is thin support. Practical use would be limited to refractory, hospital-based settings. Isoflurane is not suitable as a chronic migraine preventive.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The table lists the most relevant publications. Several other retrieved papers (CGRP, nitroglycerin and trigeminal models, topiramate, cannabinoids, passive smoking) provide migraine model context but contain no isoflurane-specific data, so they are omitted.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26323741](https://pubmed.ncbi.nlm.nih.gov/26323741/) | 2015 | Case report | Braz J Anesthesiol | Status migrainosus treated with general anesthesia; propofol and isoflurane act on GABA-A receptors and were considered theoretically useful |
| [26363696](https://pubmed.ncbi.nlm.nih.gov/26363696/) | 2015 | Case report (duplicate-language publication) | Rev Bras Anestesiol | Portuguese version of the same case report |
| [8665587](https://pubmed.ncbi.nlm.nih.gov/8665587/) | 1996 | Preclinical (animal) | Cephalalgia | Inhalational anesthetics inhibit spreading depression, with relevance to migraine |
| [17267580](https://pubmed.ncbi.nlm.nih.gov/17267580/) | 2007 | Preclinical | J Pharmacol Exp Ther | NMDA receptor antagonists affect cortical spreading depression in rats (mechanistic context) |
| [27122032](https://pubmed.ncbi.nlm.nih.gov/27122032/) | 2016 | Preclinical | J Neurosci | Susceptibility of the primary sensory cortex to spreading depolarizations (model context) |
| [40764901](https://pubmed.ncbi.nlm.nih.gov/40764901/) | 2025 | Preclinical | J Headache Pain | Atogepant does not affect CSD susceptibility in rats (model context) |

## US Market Information

All five US licenses are cancelled, and no approved indication text was recorded for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA017624 | FORANE (Baxter Healthcare) | Inhalant | Not recorded (cancelled) |
| ANDA074502 | Isoflurane (Piramal Critical Care) | Liquid | Not recorded (cancelled) |
| ANDA074416 | Isoflurane (Piramal Critical Care) | Liquid | Not recorded (cancelled) |
| ANDA075225 | Isoflurane (Halocarbon Life Sciences) | Liquid | Not recorded (cancelled) |
| ANDA216527 | Isoflurane (Shandong New Time Pharmaceutical) | Liquid | Not recorded (cancelled) |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug-disease links in PrimeKG, not label text): liver disease, gallbladder disease, hypotensive disorder, malignant hyperthermia of anesthesia, exercise-induced malignant hyperthermia, Duchenne muscular dystrophy, muscular dystrophy, and Becker muscular dystrophy. Malignant hyperthermia susceptibility is the most clinically important of these.
- **Drug interactions**: 38 interactions were identified.
  - Major: **Epinephrine**.
  - Moderate: **Morphine** and **Opium**.
  - Other interactions, for which severity is not classified, include atropine, hydrocortisone, mannitol, pantoprazole, omeprazole, vancomycin, simvastatin, ondansetron, metoclopramide, dexamethasone, and aspirin.
- Use for migraine would require hospital-level monitoring, airway management, and control of occupational exposure.

Please refer to the package insert for warnings and label contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The evidence for migraine is limited to old animal studies and one case report, with no registered trials, and the drug has no currently valid US license.
- Use would be restricted to a narrow inpatient setting such as status migrainosus.
- The other predictions (Prinzmetal angina, Tourette syndrome, trichotillomania, dysthymic disorder, nephrogenic syndrome of inappropriate antidiuresis) have only model scores and no supporting evidence. The manic bipolar disorder prediction rests on a small 1993 open study in depression plus unrelated case and animal reports.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking data gap for safety screening)
- Mechanism of action data
- Direct isoflurane studies on spreading depression and migraine, and prospective data on refractory status migrainosus
- A defined hospital-based use setting and monitoring plan, including screening for malignant hyperthermia risk
- Clarification of the regulatory pathway, since all US licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

