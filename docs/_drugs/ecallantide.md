---
layout: default
title: Ecallantide
parent: High Evidence (L1-L2)
nav_order: 639
evidence_level: L1
indication_count: 6
---

# Ecallantide
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **6** 
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

# Ecallantide: From Acute Hereditary Angioedema Attacks to C1 Inhibitor Deficiency

## One-Sentence Summary

Ecallantide (Kalbitor) is a recombinant plasma kallikrein inhibitor marketed in the US for acute attacks of hereditary angioedema (HAE).
The TxGNN model predicts it may be effective for **C1 inhibitor deficiency**, with **6 registered clinical trials** and **20 publications** on this direction.
This is largely the drug's established indication rather than a true repurposing signal. The original-indication and mechanism fields were empty in the source data, which is a data gap.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute attacks of hereditary angioedema (inferred; the license record has no indication text) |
| Predicted New Indication | C1 inhibitor deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA125277) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ecallantide is a recombinant inhibitor of plasma kallikrein. Structured mechanism data was not available in the source record, but the pharmacology is well established. In C1 inhibitor deficiency (hereditary angioedema), the loss of C1 inhibitor removes the brake on the contact-kallikrein system. This leads to unchecked bradykinin generation, which drives the swelling attacks.

Blocking kallikrein directly addresses this pathway, so the predicted link is mechanistically sound. It is also not new: the predicted disease is essentially the condition the drug is already approved for. Support for acquired C1 inhibitor deficiency is weaker, limited to a retrospective case series and reviews.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00457015](https://clinicaltrials.gov/study/NCT00457015) | Phase 3 | Completed | 96 | EDEMA4: randomized, double-blind, placebo-controlled trial in moderate to severe acute HAE attacks |
| [NCT00262080](https://clinicaltrials.gov/study/NCT00262080) | Phase 3 | Completed | 91 | Randomized, double-blind, placebo-controlled trial (1:1) with a repeat-dosing phase in acute HAE attacks |
| [NCT00456508](https://clinicaltrials.gov/study/NCT00456508) | Phase 3 | Completed | 147 | Open-label continuation; efficacy and safety of repeated doses across attacks |
| [NCT01826916](https://clinicaltrials.gov/study/NCT01826916) | Phase 2 | Completed | 77 | EDEMA2: open-label, dose-ranging study of repeated dosing; supportive but uncontrolled |
| [NCT01059526](https://clinicaltrials.gov/study/NCT01059526) | Phase 4 / N/A | Completed | 81 | Long-term observational study of immunogenicity and hypersensitivity; relevant to safety guardrails |
| [NCT01253382](https://clinicaltrials.gov/study/NCT01253382) | Phase 2/3 | Withdrawn | 0 | Pediatric PK, safety and efficacy study; no data |
| [NCT01832896](https://clinicaltrials.gov/study/NCT01832896) | Phase 2 | Withdrawn | 0 | Single subcutaneous dose in children and adolescents with HAE; no data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21760740](https://pubmed.ncbi.nlm.nih.gov/21760740/) | 2011 | Review | Clin Cosmet Investig Dermatol | Ecallantide as a novel treatment for HAE attacks; acts on the kallikrein-kinin system to limit bradykinin release |
| [22472866](https://pubmed.ncbi.nlm.nih.gov/22472866/) | n/a | Review | Am J Health Syst Pharm | Pharmacology, pharmacokinetics, efficacy, safety, dosing and place in therapy of ecallantide |
| [23406939](https://pubmed.ncbi.nlm.nih.gov/23406939/) | 2013 | Case series | Allergy Asthma Proc | Ecallantide for acute attacks of acquired C1 inhibitor deficiency, where C1-INH replacement may fail |
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Review | J Investig Allergol Clin Immunol | Current HAE therapy, including kallikrein-kinin inhibition |
| [27503784](https://pubmed.ncbi.nlm.nih.gov/27503784/) | 2017 | Consensus guideline | Allergy | International consensus on diagnosis and management of pediatric C1-INH-HAE |
| [26512744](https://pubmed.ncbi.nlm.nih.gov/26512744/) | 2016 | Review | Expert Opin Pharmacother | Current treatment options for HAE with C1 inhibitor deficiency |
| [31690390](https://pubmed.ncbi.nlm.nih.gov/31690390/) | 2019 | Review | Allergy Asthma Proc | Overview of hereditary and acquired angioedema |
| [28687105](https://pubmed.ncbi.nlm.nih.gov/28687105/) | 2017 | Review | Immunol Allergy Clin North Am | Acquired C1 inhibitor deficiency: diagnosis and associations with autoimmunity and lymphoproliferative disorders |
| [24925394](https://pubmed.ncbi.nlm.nih.gov/24925394/) | 2014 | Review | Chem Immunol Allergy | Bradykinin-mediated diseases, including angioedema from C1 inhibitor deficiency |
| [26106828](https://pubmed.ncbi.nlm.nih.gov/26106828/) | 2015 | Guideline | Curr Opin Allergy Clin Immunol | Diagnosis and treatment of C1-INH-HAE; the Italian experience |

No randomized trial publications were among the retrieved literature; the RCT evidence comes from the registered trials above.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125277 | Kalbitor (Takeda Pharmaceuticals America, Inc.) | Injection, solution | Indication text not included in the source record |

---

## Safety Considerations

- **Key Warnings**: The package insert warnings were not in the source data. The mechanistic assessment notes a boxed warning for anaphylaxis, and the drug should be administered by a healthcare professional.
- **Immunogenicity**: The long-term observational study (NCT01059526) was designed to assess antibody formation, allergic reactions and coagulation risk.

Please refer to the package insert for the full warnings, contraindications and interactions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 randomized, placebo-controlled trials (EDEMA4 and NCT00262080) support ecallantide in acute HAE attacks, which meets L1. This is an established indication rather than a new one. Evidence for acquired C1 inhibitor deficiency is limited to lower-tier reports, and there is no evidence for prophylaxis.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, including the anaphylaxis boxed warning
- Original indication and mechanism of action recorded in the drug data
- A restriction to healthcare-professional administration, with anaphylaxis monitoring
- Further evidence before any claim in acquired C1 inhibitor deficiency
- Pediatric data, since both pediatric trials were withdrawn with no enrollment

The other five TxGNN predictions (serpinopathy with toxic serpin polymerization, Peyronie disease, pancreatitis, and esophageal varices with and without bleeding) have no trials or literature. They are L5 and should stay on **Hold**. Most appear to be knowledge-graph artifacts, and pancreatitis has only some biological plausibility.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

