---
layout: default
title: Emicizumab
parent: Model Prediction Only (L5)
nav_order: 649
evidence_level: L5
indication_count: 10
---

# Emicizumab
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

# Emicizumab: From Hemophilia to Acquired Coagulation Factor Deficiency (Acquired Hemophilia A)

## One-Sentence Summary

Emicizumab is a bispecific antibody originally used to treat hemophilia (including the symptomatic form in female carriers).
The TxGNN model's top-ranked prediction is pseudo-von Willebrand disease, but that prediction has no supporting evidence. The only prediction with substantial evidence is **acquired coagulation factor deficiency** (in practice, acquired hemophilia A), supported by **0 registered clinical trials** and **20 publications**, including 3 prospective studies.

This report therefore focuses on acquired coagulation factor deficiency, and summarizes the other predicted indications briefly at the end of the report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia; symptomatic form of hemophilia in female carriers (the US license record has no indication text) |
| Predicted New Indication | Acquired coagulation factor deficiency (evidence centers on acquired hemophilia A) |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 (see note below) |
| US Market Status | Cancelled only (1 license, cancelled) |
| Number of NDAs | 1 (BLA761083) |
| Recommended Decision | Proceed with Guardrails |

Note: No completed randomized phase 3 trial exists. The evidence comes from prospective, open-label, single-arm studies, so it is rated L2 rather than L1.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, emicizumab is a bispecific antibody that bridges activated factor IX (FIXa) and factor X (FX), mimicking the cofactor function of activated factor VIII (FVIIIa). Pharmacology data confirm binding to both targets (F9 and F10).

Acquired hemophilia A is caused by autoantibodies that neutralize the patient's own FVIII. Congenital hemophilia A is a FVIII deficiency, and emicizumab is already used in patients who have developed FVIII inhibitors. Because emicizumab does not resemble FVIII structurally, anti-FVIII antibodies do not neutralize it. This makes the mechanistic extension to acquired hemophilia A logical: the functional defect (missing FVIIIa activity) is the same, and the drug works regardless of inhibitor status.

The prediction should be read narrowly. The evidence supports acquired hemophilia A, not all acquired factor deficiencies.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered in the data compiled for this report. The prospective studies found are listed in the literature section below.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36696195](https://pubmed.ncbi.nlm.nih.gov/36696195/) | 2023 | Prospective phase III, open-label, single-arm | J Thromb Haemost | First prospective study of emicizumab prophylaxis in acquired hemophilia A (Japan) |
| [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/) | 2023 | Phase 2, open-label, single-arm (GTH-AHA-EMI) | Lancet Haematol | Emicizumab protected patients from bleeding and allowed deferral of immunosuppression during the first 12 weeks |
| [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/) | 2025 | Prospective, final analysis (AGEHA) | Thromb Haemost | Final results, including immunosuppression-ineligible patients and long-term prophylaxis |
| [38049124](https://pubmed.ncbi.nlm.nih.gov/38049124/) | 2024 | Consensus recommendations | Hamostaseologie | German working group recommendations on emicizumab in acquired hemophilia A |
| [40795229](https://pubmed.ncbi.nlm.nih.gov/40795229/) | 2025 | Cohort | Blood Adv | Two-year follow-up of GTH-AHA-EMI: sustained survival benefit with postponed immunosuppression |
| [38936699](https://pubmed.ncbi.nlm.nih.gov/38936699/) | 2024 | Comparative cohort | J Thromb Haemost | Emicizumab compared with immunosuppressive therapy for managing acquired hemophilia A |
| [39361769](https://pubmed.ncbi.nlm.nih.gov/39361769/) | 2024 | Retrospective multicenter cohort | Blood Adv | 62 US patients treated off-label with emicizumab for a median of 10 weeks |
| [37276345](https://pubmed.ncbi.nlm.nih.gov/37276345/) | 2023 | Case series | Haemophilia | Emicizumab in acquired hemophilia A; no randomized trials exist |
| [39536818](https://pubmed.ncbi.nlm.nih.gov/39536818/) | 2025 | Review | J Thromb Haemost | Management of acquired hemophilia A in the emicizumab era |
| [36795341](https://pubmed.ncbi.nlm.nih.gov/36795341/) | 2023 | Review | Blood Transfus | Pros and cons of emicizumab for preventing and treating bleeding in acquired hemophilia A |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761083 | Hemlibra (Genentech, Inc.) | Injection, solution | Not listed in the compiled data; status: cancelled |

---

## Safety Considerations

- **Drug Interactions** (5 interactions retrieved):
  - **Anti-inhibitor coagulant complex (aPCC): Major.** Concurrent use carries a risk of thrombotic microangiopathy and thrombosis.
  - Antihemophilic factor (recombinant human FVIII): Moderate.
  - Recombinant coagulation factor VIIa: Moderate.
  - Pharmacological targets: coagulation factor X and factor IX (binding partners, not safety interactions).

Please refer to the package insert for other safety information, including warnings and contraindications.

---

## Other Predicted Indications (Brief Summary)

All the following have no clinical trials, and their mechanistic rationale is weak or absent. Each is rated L5 with a Hold recommendation.

| Disease | TxGNN Score | Assessment |
|------|------|------|
| Pseudo-von Willebrand disease | 99.99% | Platelet-type disorder (GP1BA gain-of-function); not an FVIII defect |
| Primary release disorder of platelets | 99.99% | Platelet secretion defect; emicizumab does not address it |
| Glanzmann thrombasthenia | 99.98% | Integrin αIIbβ3 defect; the single paper retrieved concerns recombinant FVIIa, not emicizumab |
| Scott syndrome | 99.92% | Impaired phosphatidylserine exposure; emicizumab depends on this surface, so benefit is doubtful |
| Bleeding diathesis due to a collagen receptor defect | 99.86% | No plausible mechanistic link |
| Hemorrhagic disorder due to constitutional thrombocytopenia | 99.85% | Platelet number or function defect, not FVIII deficiency |
| Thrombotic thrombocytopenic purpura | 99.61% | Prothrombotic condition; a safety concern rather than a therapeutic rationale |
| Fetal and neonatal alloimmune thrombocytopenia | 99.52% | Platelet destruction; not addressed by emicizumab |
| "Flood factor deficiency" | 99.40% | Non-standard name, likely a data artifact; needs curation |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for acquired hemophilia A only; **Hold** for all other predicted indications)

**Rationale:**
Several prospective open-label studies (Japanese phase III, GTH-AHA-EMI, AGEHA) and real-world cohorts support emicizumab prophylaxis in acquired hemophilia A, and the mechanism fits the disease. However, no randomized phase 3 evidence exists, and the US license is recorded as cancelled.

**To proceed, the following is needed:**
- Verify the regulatory and access status of the US license (BLA761083), which is listed as cancelled
- Obtain the package insert warnings and contraindications (currently a blocking data gap) and detailed mechanism-of-action data
- Define the scope as acquired hemophilia A rather than all acquired factor deficiencies
- Establish a thrombosis and thrombotic microangiopathy risk plan, particularly avoiding concurrent aPCC
- Clarify the role of immunosuppression to eradicate the autoantibody alongside emicizumab
- Curate the ambiguous "flood factor deficiency" entry before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

