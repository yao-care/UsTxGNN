---
layout: default
title: Certolizumab Pegol
parent: Moderate Evidence (L3-L4)
nav_order: 514
evidence_level: L4
indication_count: 6
---

# Certolizumab Pegol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Certolizumab Pegol: From Crohn's Disease to Rheumatoid Vasculitis

## One-Sentence Summary

Certolizumab pegol is a PEGylated anti-TNF-α antibody fragment, originally used for Crohn's disease, rheumatoid arthritis, psoriatic arthritis and ankylosing spondylitis.
The TxGNN model predicts it may be effective for **rheumatoid vasculitis**, but the only supporting evidence is **a single case report** with **no registered clinical trials**, and several reports describe vasculitis as an *adverse reaction* to the drug.
The prediction is therefore weak, and the Hold decision rests on model-score and literature findings only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Crohn's disease (also inflammatory bowel disease, rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis) |
| Predicted New Indication | Rheumatoid vasculitis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (the single BLA is listed as cancelled) |
| Number of NDAs | 1 (BLA125160) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, certolizumab pegol is an Fc-free, PEGylated TNF-α inhibitor. Its efficacy in rheumatoid arthritis has been established, and mechanistically it may be applicable to rheumatoid vasculitis.

Rheumatoid vasculitis is a complication of rheumatoid arthritis in which TNF-α is thought to play a role, so blocking TNF is biologically plausible. One case report describes improvement of leg ulcers due to rheumatoid vasculitis after certolizumab treatment.

However, the literature is contradictory. Several case reports describe vasculitis, hypocomplementemic urticarial vasculitis, medium-vessel vasculitis and rapidly progressive glomerulonephritis as adverse reactions induced by certolizumab or other anti-TNF agents. This paradoxical signal undermines the repurposing rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34786446](https://pubmed.ncbi.nlm.nih.gov/34786446/) | 2021 | Case report | JAAD Case Reports | Certolizumab pegol treatment of leg ulcers due to rheumatoid vasculitis (the only report suggesting benefit) |
| [36597972](https://pubmed.ncbi.nlm.nih.gov/36597972/) | 2022 | Multicenter cohort | RMD Open | Long-term effectiveness and safety of certolizumab in uveitis due to immune-mediated inflammatory diseases (80 patients); indirect relevance |
| [28405087](https://pubmed.ncbi.nlm.nih.gov/28405087/) | 2017 | Case report (adverse reaction) | Proc (Bayl Univ Med Cent) | Leukocytoclastic vasculitis drug reaction to certolizumab pegol |
| [31990069](https://pubmed.ncbi.nlm.nih.gov/31990069/) | 2020 | Case report (adverse reaction) | J Clin Pharm Ther | Hypocomplementemic urticarial vasculitis during certolizumab treatment for rheumatoid arthritis |
| [32687015](https://pubmed.ncbi.nlm.nih.gov/32687015/) | 2021 | Case report (adverse reaction) | Mod Rheumatol Case Rep | Rapidly progressive glomerulonephritis after introduction of certolizumab |
| [41158918](https://pubmed.ncbi.nlm.nih.gov/41158918/) | 2025 | Case report (adverse reaction) | Cureus | Anti-TNF (certolizumab)-related medium-vessel vasculitis in a patient with seronegative RA |
| [36418084](https://pubmed.ncbi.nlm.nih.gov/36418084/) | 2022 | Pharmacovigilance analysis | RMD Open | Comparison of infection profiles of immune-modulatory drugs from product characteristic data; not specific to vasculitis |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125160 (cancelled) | Cimzia (UCB, Inc.) | Injection, solution | Not listed in the data compiled |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction screen. Examples of the interactions listed in the data:
  - **Major**: corticosteroids (hydrocortisone, prednisolone, prednisone, dexamethasone, betamethasone, budesonide, triamcinolone), deferiprone, and the radiopharmaceuticals ibritumomab tiuxetan, iobenguane (I-131) and tositumomab (I-131).
  - **Moderate**: metronidazole, tinidazole, pegvaliase, rosuvastatin, simvastatin.
  - **Minor**: zinc salts (acetate, gluconate, sulfate).
- **Vasculitis-related signal**: Case reports link certolizumab and other anti-TNF agents to drug-induced vasculitis and glomerulonephritis, which is directly relevant to this proposed indication.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the evidence consists of a single case report of benefit, set against several case reports of certolizumab-induced vasculitis. No clinical trials exist, and the mechanism of action data is incomplete. The product's only US BLA is also listed as cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data to support the mechanistic link
- Systematic evidence (cohort or controlled data) on certolizumab in rheumatoid vasculitis, with careful review of paradoxical vasculitis reactions
- Verification of current US marketing status

---

### Other Predicted Indications (Brief Notes)

| Predicted Indication | TxGNN Score | Evidence Level | Decision | Comment |
|------|------|------|------|------|
| Inflammatory spondylopathy | 99.73% | L1 | Proceed with Guardrails | Multiple completed Phase 3 RCTs in axial spondyloarthritis, non-radiographic axSpA and psoriatic arthritis. This largely overlaps existing indications, so it is closer to on-label use than true repurposing. Screen for TB and hepatitis B and monitor for infections. |
| Polyarticular juvenile rheumatoid arthritis | 99.69% | L2 | Proceed with Guardrails | One open-label Phase 3 study (n=193) plus long-term follow-up. No randomized comparison. Needs weight-based dosing, infection screening and growth monitoring. |
| Vertebral disease | 99.26% | L4 | Research Question | Too broad a term. The literature actually concerns RA and axial spondyloarthritis. It should be refined into specific diagnoses. |
| Hypermobility of coccyx | 99.75% | L5 | Hold | Model score only, with no trials or literature and no plausible TNF-mediated mechanism. |
| Kummell disease | 99.70% | L5 | Hold | Model score only. A non-inflammatory osteonecrosis with no clear mechanistic rationale. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

