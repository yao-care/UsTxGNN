---
layout: default
title: Enfortumab Vedotin
parent: Model Prediction Only (L5)
nav_order: 653
evidence_level: L5
indication_count: 9
---

# Enfortumab Vedotin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Enfortumab Vedotin: From Urothelial Cancer to Leprosy

## One-Sentence Summary

Enfortumab vedotin is a Nectin-4-directed antibody-drug conjugate (ADC) marketed in the US as PADCEV, and its known use is in urothelial (bladder) cancer.
The TxGNN model predicts it may be effective for **leprosy**, but the prediction rests on the model score alone, with **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urothelial (bladder) cancer. The license records in the Evidence Pack do not list an indication, so this is based on the drug's known use. |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 records, both under BLA761137 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Enfortumab vedotin is a Nectin-4-directed ADC. The antibody binds Nectin-4 on tumor cells, and the attached payload, MMAE, disrupts microtubules and kills the cell. It is a cytotoxic cancer drug and has no known antimycobacterial activity.

This prediction is therefore not well supported. Leprosy is an infection caused by *Mycobacterium leprae*, and nothing in the drug's mechanism connects it to that pathogen. The high score most likely reflects patterns in the knowledge graph rather than biology. No clinical or literature evidence backs it.

The other eight predicted indications are also L5 and show the same weakness. They are multiple endocrine neoplasia, cytomegalovirus infection, candidiasis, cerebral infarction, HIV infection, homozygous familial hypercholesterolemia, malignant catarrh and infectious bovine rhinotracheitis.
- For the infectious diseases, the cytotoxic payload and treatment-related immunosuppression would more plausibly raise infection risk than treat it.
- The only literature found for any of them is a FAERS pharmacovigilance study of ADCs in bladder cancer (PMID 41341429), retrieved for candidiasis. It is a safety analysis, not evidence of benefit.
- Malignant catarrh and infectious bovine rhinotracheitis are veterinary diseases, probably knowledge-graph artifacts, and should be excluded from human review.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Both license records are the same authorization, listed twice.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA761137 | PADCEV | Injection, powder, lyophilized, for solution | Seagen Inc. |

## Cytotoxicity

This section reflects general knowledge of the ADC class. It was not drawn from the Evidence Pack, so please confirm each item against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ADC with cytotoxic MMAE payload) |
| Myelosuppression Risk | Medium (neutropenia is a recognized concern) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver and renal function, blood glucose, skin and peripheral nerve assessment |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials, no supporting literature and no plausible mechanism linking a Nectin-4-directed cytotoxic ADC to leprosy. The drug's toxicity and immunosuppressive effects also make it a poor fit for an infectious disease.

**To proceed, the following is needed:**
- Any mechanistic or preclinical evidence linking Nectin-4 or MMAE to *M. leprae* infection
- The package insert warnings and contraindications, which were not available for this review
- A review of the knowledge-graph terms, with veterinary entries (malignant catarrh, infectious bovine rhinotracheitis) excluded
- Detailed mechanism of action data from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

