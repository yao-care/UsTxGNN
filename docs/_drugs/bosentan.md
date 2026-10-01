---
layout: default
title: Bosentan
parent: Model Prediction Only (L5)
nav_order: 465
evidence_level: L5
indication_count: 9
---

# Bosentan
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

# Bosentan: From Pulmonary Arterial Hypertension to Rheumatoid Arthritis

## One-Sentence Summary

Bosentan is an oral endothelin receptor antagonist, best known for treating pulmonary arterial hypertension (PAH).
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but the support is thin: **1 registered trial** (which studies giant cell arteritis, not RA) and **15 publications**, almost none showing human RA efficacy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (approved indication text is not supplied in the US license records; inferred from the literature) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 (preclinical and mechanistic studies only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 14 US licenses (NDA and ANDA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the Evidence Pack. Bosentan is known to block endothelin receptors A and B (ETA/ETB), which regulate vasoconstriction and vascular remodelling. Its efficacy in PAH is well established.

The link to rheumatoid arthritis runs through inflammation. Endothelin-1 levels are raised in the plasma and synovial membrane of RA patients. Two mouse studies suggest that blocking endothelin reduces arthritis severity, partly via TNF-α and related mediators. One used collagen-induced arthritis (PMID 22249931), the other zymosan-induced arthritis (PMID 18515326). Rheumatic diseases also overlap with PAH clinically, since connective-tissue-disease-associated PAH is a common reason bosentan is used in rheumatology patients.

The evidence stops at animal models. No human RA efficacy data were provided, and the high TxGNN score is a graph-based prediction, not clinical evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06957002](https://clinicaltrials.gov/study/NCT06957002) | Phase 2 | Not yet recruiting | 40 | Bosentan plus glucocorticoids versus glucocorticoids alone in **giant cell arteritis** (not RA). It tests whether 3 months of bosentan improves failure-free survival at 12 months. It has no results and offers no direct RA evidence. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22249931](https://pubmed.ncbi.nlm.nih.gov/22249931/) | 2012 | Preclinical (animal model) | Inflamm Res | Bosentan ameliorated collagen-induced arthritis in mice; TNF-α drives induction of endothelin system genes |
| [18515326](https://pubmed.ncbi.nlm.nih.gov/18515326/) | 2008 | Preclinical (animal model) | J Leukoc Biol | Endothelin receptor blockade modulated inflammation in zymosan-induced arthritis (LTB4, TNF-α, CXCL-1) |
| [16766656](https://pubmed.ncbi.nlm.nih.gov/16766656/) | 2006 | Preclinical (not bosentan-specific) | PNAS | IL-15-induced joint hypernociception was inhibited by dual ETA/ETB antagonism |
| [24268012](https://pubmed.ncbi.nlm.nih.gov/24268012/) | 2014 | Review | Rheum Dis Clin North Am | PAH related to connective tissue disease: poor prognosis, more treatment options available |
| [16218473](https://pubmed.ncbi.nlm.nih.gov/16218473/) | 2005 | Review | Lupus | PAH in connective tissue diseases, including (less often) RA |
| [19487226](https://pubmed.ncbi.nlm.nih.gov/19487226/) | 2009 | Review | Rheumatology (Oxford) | Vasculopathy and PAH in SLE, Sjögren's syndrome and vasculitides |
| [21165350](https://pubmed.ncbi.nlm.nih.gov/21165350/) | 2010 | Not classified | Can Respir J | Pulmonary hypertension therapy in connective tissue disease with interstitial lung disease |
| [20054770](https://pubmed.ncbi.nlm.nih.gov/20054770/) | 2009 | Case report | Kardiol Pol | Child with Eisenmenger syndrome on bosentan who later developed juvenile RA; the RA was treated with naproxen, so this shows no bosentan effect on RA |
| [16766376](https://pubmed.ncbi.nlm.nih.gov/16766376/) | 2006 | Not classified | Scand J Rheumatol | Endothelin receptor antagonist in primary Sjögren's syndrome with PAH (no abstract available) |
| [19969421](https://pubmed.ncbi.nlm.nih.gov/19969421/) | 2010 | Preclinical (not bosentan-specific) | Pain | IL-17 mediates joint hypernociception in antigen-induced arthritis in mice |

## US Market Information

Approved indication text was not included in the US license records.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| NDA209279 | Tracleer (Actelion) | Tablet, for suspension |
| ANDA213154 | Bosentan (Lupin) | Tablet, for suspension |
| ANDA209324 | Bosentan (Sun Pharma) | Tablet, film coated |
| ANDA207760 | Bosentan (Zydus) | Tablet |
| ANDA207110 | Bosentan (Actavis) | Tablet, film coated |

All listed forms are oral. Nine further licenses are not shown.

## Safety Considerations

- **Hepatotoxicity**: liver function monitoring is a key guardrail for bosentan.
- **Teratogenicity**: contraception requirements apply.

Both points come from the candidate's rationale notes, not from the package insert. Please refer to the package insert for full warnings, contraindications and drug interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The RA prediction rests on animal-model data and a plausible endothelin-inflammation mechanism. No human RA efficacy data were provided, and the only registered trial studies giant cell arteritis. This is a research question, not a development-ready candidate.

**To proceed, the following is needed:**
- Human evidence in RA, such as a pilot or Phase 2 trial with clinical endpoints.
- Mechanism-of-action data and the package insert warnings and contraindications.
- A comparison with the same drug's other predicted indications. **Limited systemic sclerosis** (rank 3) has much stronger support (L3). It has an observational study of digital ulcers (NCT05168215) and a systematic review and meta-analysis (PMID 36974107), although one small study (PMID 19350343) found no microvascular effect. If that review pools RCTs, a narrow digital-ulcer indication could move toward Proceed with Guardrails.

*This report is for research reference only and does not constitute medical advice. Predicted repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

