---
layout: default
title: Nitric Oxide
parent: Model Prediction Only (L5)
nav_order: 970
evidence_level: L5
indication_count: 10
monitor_inn: "NITRIC OXIDE"
predicted_indications: ["malformation syndrome with odontal and/or periodontal component", "hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "pulmonary arteriovenous malformation (disease)", "pulmonary arterial hypertension", "pulmonary arterial hypertension associated with congenital heart disease", "pulmonary arterial hypertension associated with connective tissue disease", "pulmonary arterial hypertension associated with schistosomiasis"]
---

# Nitric Oxide
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

# Nitric Oxide: From Pulmonary Hypertension to Malformation Syndrome with Odontal and/or Periodontal Component

## One-Sentence Summary

Nitric oxide (NO) is a gas, given by inhalation, that was originally used for pulmonary hypertension and related newborn circulation disorders.
The TxGNN model predicts it may be effective for **malformation syndrome with odontal and/or periodontal component**.
This prediction has **0 clinical trials** behind it. The **20 publications** retrieved are mostly laboratory studies of periodontitis, and none tests NO as a treatment for this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary hypertension; congenital alveolar capillary dysplasia; persistent fetal circulation syndrome (the licence records contain no indication text) |
| Predicted New Indication | Malformation syndrome with odontal and/or periodontal component |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| US Market Status | ✗ Cancelled only (no currently valid licences) |
| Number of NDAs | 4 (2 NDA, 2 ANDA; all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Generally, NO is a selective pulmonary vasodilator. It works through the guanylate cyclase and cGMP signalling pathway, which is the basis of its use in pulmonary hypertension.

The link to a condition with a dental or periodontal component is weak. NO also acts as an inflammatory mediator and is produced in periodontal disease. Some of the retrieved papers describe NO production by macrophages stimulated with *Porphyromonas gingivalis* vesicles. Others describe how oral bacteria produce nitrite and NO. These findings describe NO's biological role in the mouth. They do not show that giving NO treats a malformation syndrome.

The retrieved literature covers periodontitis models (gingival fibroblasts, LPS-induced inflammation, plant extracts) and not a congenital malformation syndrome. The prediction is therefore best treated as a computational hypothesis, with no direct support yet.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No randomized trials were found. The table lists the most relevant items, with reviews first.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41952916](https://pubmed.ncbi.nlm.nih.gov/41952916/) | 2026 | Narrative review | J Dent Anesth Pain Med | *P. gingivalis*, a major periodontal pathogen, and its possible role in pain modulation; not about NO treatment |
| [42795495](https://pubmed.ncbi.nlm.nih.gov/42795495/) | 2026 | Narrative review | Microorganisms | Oral and nasal microbiomes as a model linking oral and systemic health |
| [35574962](https://pubmed.ncbi.nlm.nih.gov/35574962/) | 2022 | Cohort | J Am Heart Assoc | Oral microbial nitrite generation (nitrate-nitrite-NO pathway) examined in relation to cardiometabolic risk |
| [24670812](https://pubmed.ncbi.nlm.nih.gov/24670812/) | 2014 | Metagenomic analysis | PLoS One | Nitrate-reducing oral bacteria and their implications for NO homeostasis |
| [20646228](https://pubmed.ncbi.nlm.nih.gov/20646228/) | 2011 | Cell study | Oral Dis | *P. gingivalis* vesicles induced iNOS expression and NO production in mouse macrophage cells |
| [36312752](https://pubmed.ncbi.nlm.nih.gov/36312752/) | 2022 | In vitro | PeerJ | Cystatin C antimicrobial and anti-inflammatory activity on gingival fibroblasts exposed to *P. gingivalis* |
| [28387609](https://pubmed.ncbi.nlm.nih.gov/28387609/) | 2017 | Animal study | J Periodontol | Carvacrol reduced periodontal damage in a rat ligature-induced periodontitis model |
| [16881806](https://pubmed.ncbi.nlm.nih.gov/16881806/) | 2006 | Cell study | J Periodontol | Grape seed proanthocyanidins against oxidative stress (ROS/RNS) induced by periodontopathogen LPS |
| [35455384](https://pubmed.ncbi.nlm.nih.gov/35455384/) | 2022 | Cell study | Pharmaceuticals (Basel) | *Daphne jejudoensis* extract suppressed LPS-induced inflammatory markers, including iNOS, in periodontal ligament cells |
| [27832944](https://pubmed.ncbi.nlm.nih.gov/27832944/) | 2017 | Cell study | Eur J Pharmacol | Caffeic acid phenethyl ester reduced LPS-induced inflammatory responses in gingival fibroblasts via NF-κB and PI3K/Akt |

---

## US Market Information

All four US licences are cancelled. The licence records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020845 | INOMAX (INO Therapeutics LLC) | Gas | Not specified |
| NDA202860 | GENOSYL (Vero Biotech, Inc.) | Gas | Not specified |
| ANDA207141 | Noxivent 102 (Linde Gas & Equipment Inc) | Gas | Not specified |
| ANDA203144 | Ulspira (Airgas Therapeutics, LLC) | Gas | Not specified |

---

## Safety Considerations

- **Contraindication-related conditions (from a knowledge graph, not label text)**: methemoglobinemia, sulfhemoglobinemia, heart failure.
- **Drug Interactions**: 61 interacting drugs were identified, but the severity level is recorded for only a few.
  - **Major**: nitrous acid.
  - **Moderate**: tetracaine (ophthalmic), lidocaine (topical), benzocaine (topical).
  - The remaining interactions listed (for example morphine, omeprazole, epinephrine, heparin, epoprostenol) have no severity level recorded.

Please refer to the package insert for complete warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a very high model score (99.57%). No clinical trials exist, and the literature is indirect laboratory work on periodontitis. NO is also delivered as an inhaled gas, and all four US licences are cancelled. No clear mechanism links it to a congenital malformation syndrome with a dental component.

For context, other predictions in the same analysis have more support. Pulmonary arterial hypertension, for example, has an on-label rationale, a completed Phase 2 study (NCT02734953, n=10) and several Phase 3 trials, though the Phase 3 trials were terminated or withdrawn. That indication is within the drug's original use and is not a new repurposing.

**To proceed, the following is needed:**
- Mechanism of action data for the drug
- A plausible biological rationale for NO in this specific malformation syndrome, supported by disease-specific preclinical studies
- Confirmation that an inhaled gas can reach and act on the relevant target tissue
- Full safety information from the current package insert, including methemoglobinemia monitoring and the interaction risks listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

