---
layout: default
title: Tocilizumab
parent: Model Prediction Only (L5)
nav_order: 1238
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab: From Rheumatoid Arthritis to Ankylosing Spondylitis

## One-Sentence Summary

Tocilizumab is an anti-IL-6 receptor antibody used mainly for rheumatoid arthritis and juvenile idiopathic arthritis, according to the retrieved literature.
The TxGNN model predicts it may be effective for **ankylosing spondylitis** with a very high score (99.99%). However, the only two direct Phase 3 trials were **terminated** and are **not supportive of efficacy**.
Of the **9 retrieved trials**, only 2 test tocilizumab in this disease. The **19 publications** include no completed positive trial.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (taken from the literature; the license records supplied contain no indication text) |
| Predicted New Indication | Ankylosing spondylitis |
| TxGNN Prediction Score | 99.99% (rank 498) |
| Evidence Level | L1 by trial design (two Phase 3 RCTs), but both were terminated and non-supportive, so it does not meet the "completed" criterion |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the licenses are biologics licenses, BLA numbers) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Tocilizumab is a humanized monoclonal antibody that blocks the interleukin-6 receptor (IL-6R). IL-6 is a pro-inflammatory cytokine that has been implicated in axial inflammation in ankylosing spondylitis (AS). Detailed mechanism-of-action data from DrugBank were not supplied. The mechanistic reasoning here relies on the published literature.

Rheumatoid arthritis and AS are both chronic inflammatory rheumatic diseases in which cytokine signaling drives joint and spine inflammation. This is why the model links them. Reviews in the evidence set describe IL-6 blockade as a candidate strategy for AS patients who fail TNF inhibitors.

The clinical evidence does not support this link. Both dedicated AS Phase 3 trials were terminated after about a year, and the reason for termination is not in the supplied data. The pack's own analysis notes that, from background knowledge, the program reported a lack of efficacy, and this should be checked against the primary publication. The very high TxGNN score is therefore not corroborated by clinical data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | Terminated | 113 | Placebo-controlled RCT of tocilizumab 8 mg/kg or 4 mg/kg vs placebo in AS patients with inadequate response to TNF antagonists. Efficacy results are not in the supplied data. |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 3 (Ph II/III seamless) | Terminated | 306 | Placebo-controlled RCT of tocilizumab 8 mg/kg in NSAID-failed, TNF-naïve AS patients. Efficacy results are not in the supplied data. |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Recruiting | 10,000 | Korean biologics registry covering RA, AS and PsA. Observational, not tocilizumab-specific. |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | Recruiting | 2,500 | Cytokine and biomarker profiling cohort in systemic inflammatory diseases. No efficacy question. |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Registry of new immune-mediated inflammatory diseases after biologics. Epidemiologic only. |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Completed | 60 | Mechanistic study of tocilizumab on T follicular helper cells, apparently in RA. Indirect. |

The remaining retrieved trials concern an infliximab biosimilar observational study, perioperative immunosuppressant management, and Takayasu arteritis. They are not relevant to tocilizumab efficacy in AS.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT report (BUILDER-1/2) | Ann Rheum Dis | Assessed short-term symptomatic efficacy and safety of tocilizumab in AS. The supplied abstract does not include the results. |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Network meta-analysis | Medicine | Compares biologic regimens for AS across RCTs. Context for where tocilizumab stands against approved biologics. |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflamm Allergy Drug Targets | Discusses IL-6 antagonism in AS and the role of IL-6 in its pathogenesis. |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Review | Curr Opin Rheumatol | Reviews alternatives for AS patients refractory to TNF inhibition. |
| [21803631](https://pubmed.ncbi.nlm.nih.gov/21803631/) | 2011 | Review | Joint Bone Spine | Biologic agents for AS beyond TNFα antagonists. |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Meta-analysis | Clin Rheumatol | Serious-infection risk of biologics in AS and non-radiographic axSpA RCTs (safety context). |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Review | Semin Arthritis Rheum | Second-line biologic optimization in RA, PsA and AS. |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Case report | Front Med | Two AS patients with AA amyloidosis treated with tocilizumab. This is a complication-specific report, not evidence of efficacy against AS itself. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA125472 | Actemra | Injection, solution | Genentech, Inc. |
| BLA761420 | AVTOZMA | Injection, solution | CELLTRION USA, Inc. |
| BLA761420 | Tocilizumab-anoh | Injection, solution, concentrate | CELLTRION USA, Inc. |
| BLA761354 | TOFIDENCE | Injection | Organon LLC |
| BLA761449 | TYENNE | Injection, solution | Fresenius Kabi USA, LLC |

These are 5 of 20 licenses, all injectable. Approved-indication text is not included in the supplied records.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both Phase 3 RCTs of tocilizumab in AS were terminated and are not supportive, and no other clinical data show benefit. The high TxGNN score is not backed by clinical evidence, so repurposing for AS is not justified at present.

**To proceed, the following is needed:**
- The termination reasons and efficacy results for NCT01209689 and NCT01209702, from the primary publication (BUILDER-1/2, PMID 23765873) and the trial registry results.
- Package insert warnings and contraindications, which are currently missing and block the safety screen.
- Mechanism-of-action data from DrugBank.

**Note on other predictions:** Polyarticular juvenile idiopathic arthritis (rank 7) has the strongest evidence in this pack, including a completed Phase 3 withdrawal trial (NCT00988221, n=188). It appears to be an on-label use, so label status should be verified before treating it as repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

