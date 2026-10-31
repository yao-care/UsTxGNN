---
layout: default
title: Prilocaine
parent: Model Prediction Only (L5)
nav_order: 1081
evidence_level: L5
indication_count: 10
monitor_inn: "PRILOCAINE"
predicted_indications: ["papillary conjunctivitis", "manic bipolar affective disorder", "bronchitis", "migraine disorder", "neuralgia", "migraine with brainstem aura", "atopic eczema", "allergic asthma", "rhinitis", "rosacea conjunctivitis"]
last_modified_at: 2026-10-31
description: "Prilocaine: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Prilocaine
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

## Prilocaine: Papillary conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Prilocaine is an amide local anesthetic. Its only US authorization on record is a dental injectable.
The TxGNN model predicts it may be effective for **Neuralgia** (the most evidence-supported of 10 predictions), with **2 clinical trials** and **14 publications** currently supporting this direction.
The evidence is early-stage: small, uncontrolled studies, mostly of the lidocaine/prilocaine combination (EMLA), and no Phase 3 RCT.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Prilocaine is an amide local anesthetic, and this class generally blocks voltage-gated sodium channels in nerve fibres. This is background knowledge, not something confirmed by the compiled data.

Neuralgia, especially postherpetic neuralgia (PHN), is a neuropathic pain condition driven by hyperexcitable peripheral nociceptors. Blocking sodium channels in these fibres is mechanistically coherent. Prilocaine is usually given topically as the lidocaine 2.5%/prilocaine 2.5% eutectic mixture (EMLA). Reports from 1989 to 1996 describe this cream in PHN, including a pharmacokinetic study.

The original indications (premature ejaculation, psychologic dyspareunia) also relate to reducing sensory input from local tissue. This is a loose conceptual link to neuralgia, and the data do not formally assess it. The evidence cannot separate prilocaine's contribution from lidocaine's, because nearly all studies use the combination.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00916942](https://clinicaltrials.gov/study/NCT00916942) | Phase 2 | Completed | 20 | Open-label study of lidocaine 2.5%/prilocaine 2.5% cream as pre-treatment before the capsaicin 8% patch (NGX-4010) in PHN. It assessed tolerability only, with no hypothesis testing. |
| [NCT06899438](https://clinicaltrials.gov/study/NCT06899438) | N/A | Completed | 38 | Botulinum toxin type A vs prilocaine in myofascial pain syndrome. Prilocaine was a comparator intervention, and the relevance to neuralgia is indirect. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2493878](https://pubmed.ncbi.nlm.nih.gov/2493878/) | 1989 | Clinical study | BMJ | Lignocaine-prilocaine cream in postherpetic neuralgia (no abstract available) |
| [2616182](https://pubmed.ncbi.nlm.nih.gov/2616182/) | 1989 | Clinical study with PK | Pain | 12 patients with refractory PHN. 5% EMLA cream significantly improved mean pain scores 6 h after application. Pharmacokinetics were also assessed. |
| [8695081](https://pubmed.ncbi.nlm.nih.gov/8695081/) | 1996 | Case report | J Clin Anesth | Successful EMLA treatment of PHN resistant to other therapies |
| [22182397](https://pubmed.ncbi.nlm.nih.gov/22182397/) | 2011 | Clinical study | BMC Anesthesiol | Tolerability of the capsaicin 8% patch after lidocaine/prilocaine pre-treatment in PHN |
| [41777672](https://pubmed.ncbi.nlm.nih.gov/41777672/) | 2026 | Retrospective cohort | Front Aging Neurosci | EMLA alone vs paravertebral block plus EMLA to improve tolerability of capsaicin patch application in thoracic PHN |
| [1430539](https://pubmed.ncbi.nlm.nih.gov/1430539/) | 1992 | Review | J Dermatol Surg Oncol | EMLA (2.5% lidocaine and 2.5% prilocaine) gives effective, safe analgesia on normal and diseased skin. PHN is listed among other indications. |
| [23314014](https://pubmed.ncbi.nlm.nih.gov/23314014/) | 2013 | Review | Curr Opin Support Palliat Care | Evidence-based approach to persistent wound-related pain |
| [10342425](https://pubmed.ncbi.nlm.nih.gov/10342425/) | 1999 | Experimental | Pain | In 9 healthy subjects, EMLA pre-treatment failed to reduce the pain induced by 1% topical capsaicin |
| [18379178](https://pubmed.ncbi.nlm.nih.gov/18379178/) | 2008 | Formulation study | Yakugaku Zasshi | In-house lidocaine-tetracaine cream compared with a lidocaine-prilocaine eutectic cream for conditions such as PHN |
| [7897165](https://pubmed.ncbi.nlm.nih.gov/7897165/) | 1995 | Case report | J Allergy Clin Immunol | EMLA cream-induced allergic contact dermatitis, with prilocaine as an immunogen |

Of the 14 publications listed in the data, 10 are shown here. The 4 omitted are indirect (a PHN prognostic cohort, a healthy-volunteer sensory study, a nerve-block injury series, and a capsaicin patch case report).

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA079235 (cancelled) | Citanest Plain (Dentsply Pharmaceutical Inc.) | Injection, solution | No indication text available |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these are graph relationships, not label text): hypertension and other cardiovascular disease (coronary artery disease, myocardial infarction, heart conduction disease, atrioventricular block, sudden cardiac arrest), epilepsy, kidney disease, liver disease, diabetes and diabetic ketoacidosis, hemoglobinopathy, respiratory failure, angle-closure glaucoma, myasthenia gravis and other neuromuscular junction disease, butyrylcholinesterase deficiency, and hyperthyroidism (Graves disease, thyrotoxicosis).
- **Drug interactions:** 22 interactions were recorded. The list shows 20 entries, 17 of them Major. The main ones are:
  - Agents associated with methemoglobinemia risk: amyl nitrite, nitrous acid, nitric oxide, dapsone (oral and topical), primaquine, tafenoquine, chloroquine, quinine, rasburicase, sulfasalazine, silver nitrate and silver sulfadiazine.
  - Other local anesthetics: lidocaine (including topical), benzocaine (topical) and cinchocaine (topical).
  - Metoclopramide (Major).
  - Moderate and minor: liposomal morphine (Moderate) and hyaluronidase (Minor).
- **Safety signals in the literature:** methemoglobinemia and seizures after EMLA in a child with atopic dermatitis, increased systemic absorption through compromised skin, allergic contact dermatitis, and purpura.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Neuralgia is the best-supported prediction (L3), but the evidence consists of small, early, uncontrolled studies of the lidocaine/prilocaine combination, and the open trial only tested pre-treatment tolerability. The other nine predictions have either no evidence (L5) or only indirect or safety-oriented evidence (L4).

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- Controlled trials of prilocaine-containing products in PHN or other neuralgias, ideally separating prilocaine's contribution from lidocaine's
- A route and formulation compatibility assessment (the original authorization is an injectable, while the supporting evidence is for topical cream)
- A safety plan covering methemoglobinemia risk, interacting drugs, and use on compromised skin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

