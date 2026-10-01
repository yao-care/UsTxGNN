---
layout: default
title: Fludarabine
parent: Model Prediction Only (L5)
nav_order: 715
evidence_level: L5
indication_count: 10
---

# Fludarabine
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

# Fludarabine: From Lymphoid Malignancy Chemotherapy to Plasma Cell Myeloma

## One-Sentence Summary

Fludarabine is a purine nucleoside analog chemotherapy drug. The literature in the Evidence Pack describes its use in B-cell chronic lymphocytic leukemia, hairy cell leukemia and indolent lymphomas.
The TxGNN model predicts it may be useful for **Plasma Cell Myeloma**, with **50 clinical trials** and **20 publications** retrieved.
Almost all of that evidence has fludarabine as a conditioning or lymphodepletion component of a regimen, not as a stand-alone anti-myeloma treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the US license data. Literature describes B-cell CLL, hairy cell leukemia and indolent lymphomas |
| Predicted New Indication | Plasma cell myeloma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 (per Evidence Pack scoring; no trial isolates fludarabine as the tested variable, so this is at the optimistic end) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 (all ANDA generics; see the note under US Market Information) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in DrugBank for this record. Fludarabine is a purine nucleoside analog that inhibits DNA synthesis and is strongly lymphotoxic. Its efficacy in lymphoid malignancies is established.

In myeloma it works as a **conditioning or lymphodepleting backbone**, not as a single-agent anti-myeloma drug. The main uses are:
- Fludarabine/melphalan or fludarabine/busulfan conditioning before allogeneic transplant.
- Fludarabine/cyclophosphamide lymphodepletion before CAR-T therapy.

Preclinical work also reports anti-myeloma activity in vitro and in vivo (PMID 17976186), although a review of the field notes the drug's single-agent activity in myeloma has been controversial.

The prediction is therefore best read as a regimen-level signal. The supporting evidence does not show that fludarabine alone treats myeloma.

---

## Clinical Trial Evidence

The Evidence Pack lists 50 trials. Below are the 10 most relevant. Many others are mixed hematologic-malignancy transplant studies.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04098393](https://clinicaltrials.gov/study/NCT04098393) | Phase 1 | Active, not recruiting | 39 | Condensed busulfan/melphalan/fludarabine plus ATG before CD34+ selected allogeneic transplant; tests whether severe side effects are equal or fewer |
| [NCT01008462](https://clinicaltrials.gov/study/NCT01008462) | Phase 2 | Completed | 16 | Autologous transplant followed by nonmyeloablative haploidentical transplant (fludarabine in conditioning) for high-risk lymphoma, myeloma or CLL |
| [NCT00054353](https://clinicaltrials.gov/study/NCT00054353) | Phase 1/2 | Completed | 16 | Reduced-intensity fludarabine + melphalan + TBI before donor stem cell transplant in multiple myeloma |
| [NCT01231412](https://clinicaltrials.gov/study/NCT01231412) | Phase 3 | Completed | 174 | Randomized comparison of post-graft immunosuppression (GVHD prevention) after nonmyeloablative conditioning; fludarabine is background, not the tested variable |
| [NCT00615589](https://clinicaltrials.gov/study/NCT00615589) | Phase 2 | Terminated | 22 | Allogeneic transplant with reduced-toxicity myeloablative conditioning in high-risk myeloma |
| [NCT00723099](https://clinicaltrials.gov/study/NCT00723099) | Phase 2 | Completed | 73 | Cord blood transplant with reduced-intensity conditioning across hematologic cancers; myeloma is one of several diseases |
| [NCT02447055](https://clinicaltrials.gov/study/NCT02447055) | Early Phase 1 | Withdrawn | 0 | Fludarabine/melphalan allo-transplant with post-transplant cyclophosphamide and tocilizumab in myeloma; no patients enrolled |
| [NCT04579523](https://clinicaltrials.gov/study/NCT04579523) | Phase 1 | Not yet recruiting | 30 | ²¹¹At-labeled anti-CD38 antibody with fludarabine before donor transplant in high-risk myeloma |
| [NCT06196255](https://clinicaltrials.gov/study/NCT06196255) | Phase 1/2 | Recruiting | 20 | Anti-FcRL5 CAR-T in relapsed/refractory myeloma after fludarabine + cyclophosphamide lymphodepletion |
| [NCT07149857](https://clinicaltrials.gov/study/NCT07149857) | Phase 2 | Recruiting | 60 | Cilta-cel with a fludarabine-free lymphodepletion regimen, or after cyclophosphamide + fludarabine; this study examines whether fludarabine can be omitted |

---

## Literature Evidence

There is no RCT in the myeloma retrieval set. The evidence is phase 1 studies, retrospective series, real-world CAR-T data and preclinical work.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38483213](https://pubmed.ncbi.nlm.nih.gov/38483213/) | 2024 | Phase 1 | Am J Clin Oncol | Bortezomib + fludarabine + melphalan, with or without total marrow irradiation, as allo-transplant conditioning in high-risk/refractory myeloma |
| [40972962](https://pubmed.ncbi.nlm.nih.gov/40972962/) | 2025 | Real-world cohort | Transplant Cell Ther | Fludarabine lymphodepletion exposure is associated with toxicities after ide-cel in relapsed/refractory myeloma |
| [37833271](https://pubmed.ncbi.nlm.nih.gov/37833271/) | 2023 | Comparative study | Blood Cancer J | Bendamustine versus fludarabine/cyclophosphamide lymphodepletion before BCMA CAR-T in myeloma |
| [37701906](https://pubmed.ncbi.nlm.nih.gov/37701906/) | 2023 | Phase 2 | Leuk Res Rep | Split-dose busulfan/fludarabine + post-transplant cyclophosphamide; only 2 myeloma patients, 1-year overall survival 50% across 6 patients |
| [17310135](https://pubmed.ncbi.nlm.nih.gov/17310135/) | 2007 | Retrospective multicenter | Bone Marrow Transplant | Feasibility of fludarabine/treosulfan conditioning before allo-SCT in 34 myeloma patients |
| [15389436](https://pubmed.ncbi.nlm.nih.gov/15389436/) | 2004 | Retrospective cohort | Biol Blood Marrow Transplant | 120 myeloma patients after melphalan/fludarabine allografts; 1-year treatment-related mortality 18%, relapse after prior autograft and chronic GVHD were the strongest adverse factors |
| [17976186](https://pubmed.ncbi.nlm.nih.gov/17976186/) | 2007 | Preclinical | Eur J Haematol | Fludarabine inhibited the RPMI8226 myeloma cell line in vitro and in vivo, with reduced Akt phosphorylation |
| [7781758](https://pubmed.ncbi.nlm.nih.gov/7781758/) | 1995 | Report | Eur J Haematol | Fludarabine in plasma cell leukemia (no abstract available) |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA090724 | Fludarabine Phosphate | Injection | Areva Pharmaceuticals |
| ANDA090724 | Fludarabine Phosphate | Injection | Lannett Company, Inc. |
| ANDA076661 | Fludarabine Phosphate | Injection, solution | Sagent Pharmaceuticals |
| ANDA078393 | Fludarabine | Injection, solution | Fresenius Kabi USA, LLC |
| ANDA078610 | Fludarabine phosphate | Injection, powder, lyophilized, for solution | Actavis Pharma, Inc. |

All products are generic injectables. Approved indication text is not included in the source data. ANDA090724 appears twice under different manufacturers, so there are 4 distinct numbers against 5 license records.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog antimetabolite) |
| Myelosuppression Risk | High (myelosuppression is flagged as a guardrail in the evidence review) |
| Emetogenicity Classification | Low (based on drug class) |
| Monitoring Items | CBC with differential, renal function (renally cleared), neurological status, infection surveillance |
| Handling Protection | Follow cytotoxic drug handling regulations |

No DrugBank toxicity data was retrieved. These entries reflect drug class and the guardrails in the evidence review. Please refer to the package insert warnings and precautions.

---

## Safety Considerations

No package insert warnings, contraindications or drug-interaction records were retrieved; the DDI query returned no results. The evidence review raises these guardrails:
- Dose adjustment is needed in renal impairment.
- Neurotoxicity risk.
- Myelosuppression.
- Prolonged immunosuppression and opportunistic infection.
- Fludarabine exposure was associated with toxicities after CAR-T therapy (PMID 40972962).
- Therapy-related MDS/AML has been reported after fludarabine combination chemotherapy (PMID 20962860).

Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Fludarabine's role in myeloma is as a conditioning or lymphodepletion component, and no study isolates its independent effect. Package insert safety data is also missing, a blocking gap that prevents safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap), plus DrugBank mechanism of action data.
- Comparative data showing what fludarabine adds within myeloma conditioning or CAR-T lymphodepletion regimens, such as fludarabine-free arms (NCT07149857 is relevant).
- A renal-dosing and neurotoxicity/infection monitoring plan for this population.

**Other predictions in the pack:** Myelodysplastic syndrome (rank 7) is better supported. Fludarabine-based conditioning is an established allogeneic transplant backbone there, with Phase 3 RCT evidence, though fludarabine is not the randomized variable. It is rated Proceed with Guardrails and merits its own evaluation. Indolent plasma cell myeloma (rank 4) and unclassified MDS (rank 8) have thin or mapping-limited evidence. Hyperthyroidism, diabetic nephropathy and the rare genetic disorders (ranks 2, 3, 5, 6, 9, 10) have no plausible mechanistic link or trial support and should be held.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

