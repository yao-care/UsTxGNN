---
layout: default
title: Pimecrolimus
parent: High Evidence (L1-L2)
nav_order: 1045
evidence_level: L2
indication_count: 4
---

# Pimecrolimus
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **4** 
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

# Pimecrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

Pimecrolimus is a topical calcineurin inhibitor cream, marketed in the US and labeled for mild-to-moderate atopic dermatitis.
The TxGNN model predicts it may be effective for **seborrheic dermatitis**,
supported by **1 completed Phase 2 clinical trial** and **18 retrieved publications**, including several randomized comparisons and systematic reviews of RCTs.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic dermatitis (from the literature; the license records provided contain no indication text) |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 licenses (NDA and ANDA) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in DrugBank for this record. Published pharmacology, however, describes pimecrolimus as a topical calcineurin inhibitor. It blocks T-cell activation and proliferation, reduces release of IL-2, IL-4, interferon-gamma and TNF-alpha, and inhibits mast cell degranulation (PMID 16033622).

Atopic dermatitis and seborrheic dermatitis are both chronic, relapsing inflammatory skin diseases. Seborrheic dermatitis has an inflammatory component driven by the host response to *Malassezia* yeast, so a non-steroidal anti-inflammatory agent is a plausible fit. It may also help where long-term topical corticosteroid use is a concern. This link rests on general pharmacology rather than DrugBank MOA data.

The high TxGNN score is consistent with the clinical record. Several randomized studies compare pimecrolimus 1% cream with sertaconazole and ketoconazole in facial seborrheic dermatitis. Two systematic reviews of randomized trials have also been published.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Phase 2 | Completed | 113 | 4-week randomized, double-blind, active-comparator study of Elidel (pimecrolimus) in seborrheic dermatitis; exploratory effectiveness study (2007–2009) |

This is the only registered trial for this indication. It is short and exploratory, and there is no Phase 3 confirmation.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34910320](https://pubmed.ncbi.nlm.nih.gov/34910320/) | 2022 | RCT | Clin Exp Dermatol | Randomized blinded trial of pimecrolimus 1% vs sertaconazole 2% cream in facial seborrheic dermatitis |
| [22142161](https://pubmed.ncbi.nlm.nih.gov/22142161/) | 2012 | Systematic review of RCTs | Expert Rev Clin Pharmacol | Pimecrolimus 1% cream appears well tolerated and effective for seborrheic dermatitis versus corticosteroids, antimycotics, placebo or no treatment |
| [36072203](https://pubmed.ncbi.nlm.nih.gov/36072203/) | 2022 | Systematic review of RCTs | Cureus | Reviews efficacy and safety of pimecrolimus in facial seborrheic dermatitis |
| [18677657](https://pubmed.ncbi.nlm.nih.gov/18677657/) | 2009 | Open randomized comparative study | J Dermatol Treat | Pimecrolimus 1% vs ketoconazole 2% cream in seborrheic dermatitis |
| [23715821](https://pubmed.ncbi.nlm.nih.gov/23715821/) | 2013 | Comparative study | Ir J Med Sci | Sertaconazole 2% vs pimecrolimus 1% cream in seborrheic dermatitis |
| [28589618](https://pubmed.ncbi.nlm.nih.gov/28589618/) | 2018 | Comparative study | J Cosmet Dermatol | Compares different dosing regimens of pimecrolimus 1% in facial seborrheic dermatitis |
| [20000875](https://pubmed.ncbi.nlm.nih.gov/20000875/) | 2010 | Open-label study | Am J Clin Dermatol | Pimecrolimus 1% in resistant facial seborrheic dermatitis |
| [19391059](https://pubmed.ncbi.nlm.nih.gov/19391059/) | 2010 | Clinical study | J Dermatol Treat | Repetitive use of pimecrolimus in relapsing seborrheic dermatitis |
| [15700745](https://pubmed.ncbi.nlm.nih.gov/15700745/) | 2004 | Clinical study | Drugs Exp Clin Res | Pimecrolimus 1% for seborrheic dermatitis of the face and trunk; efficacy, tolerability and safety |
| [31053034](https://pubmed.ncbi.nlm.nih.gov/31053034/) | 2019 | Review | J Cutan Med Surg | Review of off-label uses of topical pimecrolimus, focused on published RCTs |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA021302 | Pimecrolimus | Cream | Oceanside Pharmaceuticals |
| ANDA209345 | Pimecrolimus | Cream | Actavis Pharma, Inc. |
| ANDA211769 | Pimecrolimus | Cream | Glenmark Pharmaceuticals Inc., USA |

The source records list six licenses in total; NDA021302 appears several times and is shown once here. The records contain no approved-indication text, and the only route of administration is topical.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 2 randomized, double-blind trial and several randomized comparisons and systematic reviews support pimecrolimus in seborrheic dermatitis, and the mechanism is plausible. Confirmatory Phase 3 evidence is missing, and the use would be off-label. Long-term use also carries the class boxed-warning concern about malignancy, and the labeled age restrictions apply.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently missing and blocking for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the labeled indication text
- A Phase 3 study or an expert review of the randomized comparator data
- A long-term safety and relapse-management plan for repeated facial use

The other predictions are:
- **Dermatitis:** atopic dermatitis is the labeled use, so this is not true repurposing.
- **Exanthem:** this is only a research question, with indirect and small trials.
- **Acrodermatitis chronica atrophicans:** hold, with no supporting evidence.

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

