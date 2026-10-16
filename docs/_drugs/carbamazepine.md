---
layout: default
title: Carbamazepine
parent: Model Prediction Only (L5)
nav_order: 495
evidence_level: L5
indication_count: 10
monitor_inn: "CARBAMAZEPINE"
predicted_indications: ["trigeminal nerve neoplasm", "thinking seizures", "eating seizures", "orgasm-induced seizures", "micturation-induced seizures", "startle epilepsy", "audiogenic seizures", "reading seizures", "beta-ketothiolase deficiency", "Rett syndrome, congenital variant"]
last_modified_at: 2026-10-14
description: "Carbamazepine: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy"
---

# Carbamazepine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Carbamazepine: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Carbamazepine is a sodium channel-blocking anticonvulsant, originally used for epilepsy, bipolar disorder and trigeminal neuralgia.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but there are **0 clinical trials** and **20 publications** (all case reports or reviews on tumor-associated neuralgia, with no evidence of antitumour activity). This prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (also bipolar disorder, trigeminal neuralgia; indication text is not listed in the US license records) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all licenses recorded as cancelled) |
| Number of NDAs | 16 (2 NDAs and 14 ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Carbamazepine is a well-established antiseizure drug that is generally understood to act by blocking voltage-gated sodium channels. It is an established treatment for trigeminal neuralgia.

The high prediction score most likely reflects the anatomical overlap with trigeminal neuralgia, not any anticancer effect. The retrieved literature concerns neuralgia secondary to tumors (schwannoma, meningioma, lipoma, dermoid cyst, lymphoma, pituitary adenoma and others). In these reports carbamazepine was used for symptom control, and in several it failed or caused side effects. No evidence shows that carbamazepine acts on tumor growth. At most it offers symptomatic relief of tumor-associated facial pain, which is already within its established use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 20 retrieved publications consist of reviews, case reports and one animal study. The most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Review | Acta Clin Croat | Treatment options for trigeminal neuralgia, which can be caused by vascular compression or a tumor |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Medical and surgical options for trigeminal neuralgia |
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | Case report | Br J Neurosurg | Primary trigeminal nerve lymphoma; carbamazepine did not improve symptoms |
| [33989821](https://pubmed.ncbi.nlm.nih.gov/33989821/) | 2021 | Case report | World Neurosurg | Petroclival meningioma causing trigeminal neuralgia, resected surgically |
| [25968963](https://pubmed.ncbi.nlm.nih.gov/25968963/) | 2015 | Case report/Review | World Neurosurg | Trigeminal neuralgia caused by venous angioma |
| [25433061](https://pubmed.ncbi.nlm.nih.gov/25433061/) | 2014 | Case report | No Shinkei Geka | Cerebellopontine angle lipoma; carbamazepine pain control was inadequate because of side effects |
| [25142539](https://pubmed.ncbi.nlm.nih.gov/25142539/) | 2014 | Case report | Rinsho Shinkeigaku | Lymphoma spreading along the trigeminal nerve; initial response to carbamazepine was later lost |
| [15235745](https://pubmed.ncbi.nlm.nih.gov/15235745/) | 2004 | Case report | Arq Neuropsiquiatr | Primary melanoma of Meckel's cave; pain not relieved by carbamazepine |
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | Animal study | Exp Neurol | Carbamazepine inhibited spontaneous activity in experimental rat neuromas (a nerve injury model, not a tumor) |
| [11286444](https://pubmed.ncbi.nlm.nih.gov/11286444/) | 2001 | Survey | Br J Oral Maxillofac Surg | Practice patterns for trigeminal neuralgia management, including carbamazepine monitoring |

---

## US Market Information

All 16 US licenses are recorded as cancelled, and the records contain no approved indication text. The five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021710 | EQUETRO | Capsule, extended release | Not listed in the records |
| NDA020712 | Carbatrol | Capsule, extended release | Not listed in the records |
| ANDA075687 | Carbamazepine | Tablet, chewable | Not listed in the records |
| ANDA070541 | Carbamazepine | Tablet | Not listed in the records |
| ANDA205571 | Carbamazepine | Tablet, extended release | Not listed in the records |

---

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text)**: The knowledge graph links carbamazepine to hematological conditions (neutropenia, agranulocytosis, pancytopenia, thrombocytopenia, anemia), liver disease, kidney disease and impaired renal function, heart conduction disease and atrioventricular block, glaucoma and ocular hypertension, absence epilepsy, and inappropriate ADH syndrome, among others.
- **Drug Interactions**: 100 interactions were identified. Major-level examples include **clarithromycin** and **eliglustat**. Moderate-level examples include doxycycline, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), pioglitazone, bupropion, aprepitant, morphine, metronidazole, cimetidine, canagliflozin and vitamin D analogues.

Please also refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for trigeminal nerve neoplasm has no clinical trials, and the literature shows carbamazepine only as symptomatic therapy for tumor-associated neuralgia, not as an antitumour agent. The model score likely reflects the drug's known use in trigeminal neuralgia. Other predicted indications are mostly reflex seizure types (startle, reading, eating, audiogenic and others) that extend the existing epilepsy use. Among these, startle epilepsy has the most clinical support, with a 1984 cohort in which some patients with focal lesions responded to carbamazepine, so it is the most worthwhile follow-up question.

**To proceed, the following is needed:**
- Mechanism of action data and any preclinical evidence of antitumour activity
- FDA package insert warnings and contraindications (these were flagged as a blocking gap for safety screening)
- Confirmation of current US market status, since all records show cancelled licenses
- If pursuing reflex epilepsy indications, a targeted review of startle epilepsy as a research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

