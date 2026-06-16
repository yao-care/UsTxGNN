---
layout: default
title: Cortisone
parent: 僅模型預測 (L5)
nav_order: 550
evidence_level: L5
indication_count: 9
---

# Cortisone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Cortisone: From Adrenocortical Insufficiency to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Cortisone is an endogenous glucocorticoid hormone historically used as replacement therapy for adrenocortical insufficiency (Addison's disease), although no current US market approvals are on record for this specific compound.
The TxGNN model predicts it may be effective for **Primary Cutaneous T-Cell Lymphoma (CTCL)**,
with **1 clinical trial** and **10 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No US approvals on record (historically used for adrenocortical insufficiency) |
| Predicted New Indication | Primary Cutaneous T-Cell Lymphoma |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L3 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on established pharmacology, cortisone is a natural glucocorticoid secreted by the adrenal cortex and converted to its active form — cortisol (hydrocortisone) — in the liver via the enzyme 11β-hydroxysteroid dehydrogenase type 1 (11β-HSD1). As a glucocorticoid, it exerts potent immunosuppressive and anti-inflammatory effects primarily through inhibition of NF-κB signaling and downstream suppression of pro-inflammatory cytokines (TNF-α, IL-1β, IL-6).

Primary Cutaneous T-Cell Lymphoma (CTCL) — particularly mycosis fungoides and Sézary syndrome — is characterized by clonal proliferation of malignant T-lymphocytes within the skin. Cortisone's capacity to directly induce lymphocyte apoptosis and suppress T-cell proliferation provides a theoretical mechanistic basis for activity in CTCL, a disease driven by aberrant T-cell survival.

Historical evidence partially supports this rationale: case reports from the early 1950s (PMID 14884116, PMID 14896727) documented temporary clinical remissions in mycosis fungoides patients treated with cortisone or combined ACTH/cortisone regimens. However, the same era also recorded fatal ulceronecrotic complications in similar patients receiving cortisone derivatives (PMID 13612293, PMID 13573074) — a significant safety signal that was never resolved. In modern practice, more potent and better-characterized glucocorticoids (prednisolone, dexamethasone) have fully replaced cortisone in all lymphoma regimens, substantially limiting cortisone's potential as a standalone repurposing candidate for CTCL.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04799275](https://clinicaltrials.gov/study/NCT04799275) | Phase 2/3 | Suspended | 422 | R-MiniCHOP ± oral azacitidine (CC-486) in patients ≥75 years with newly diagnosed diffuse large B-cell lymphoma and related high-grade B-cell lymphomas. The regimen contains prednisone (a more potent glucocorticoid) rather than cortisone; the trial is not CTCL-specific and is currently suspended. |

> No clinical trials directly testing cortisone in primary cutaneous T-cell lymphoma were identified. The trial above uses a corticosteroid-containing regimen for a related lymphoma subtype and has only indirect relevance to cortisone repurposing.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [11917454](https://pubmed.ncbi.nlm.nih.gov/11917454/) | 2001 | Review | Dermatology Nursing | Overview of Sézary syndrome as the leukemic form of CTCL; documents aggressive clinical course, poor prognosis, and the psychological burden on patients — contextualizing the unmet need in this population. |
| [6234331](https://pubmed.ncbi.nlm.nih.gov/6234331/) | 1984 | Review | J Am Acad Dermatol | 18 patients with pre-Sézary syndrome followed over ~5 years; none progressed to frank lymphoproliferative disease; notable IgE elevation and positive patch testing. Establishes the clinical spectrum of early-stage CTCL. |
| [14884116](https://pubmed.ncbi.nlm.nih.gov/14884116/) | 1951 | Case Series | Svenska Läkartidningen | Combined ACTH and cortisone therapy in mycosis fungoides; one of the earliest reports of glucocorticoid use in CTCL, documenting initial clinical responses. |
| [14896727](https://pubmed.ncbi.nlm.nih.gov/14896727/) | 1951 | Case Series | Dermatologica | Cortisone administered to two cases of mycosis fungoides; documents observable clinical effects, representing early proof-of-concept for glucocorticoid activity in CTCL. |
| [13612293](https://pubmed.ncbi.nlm.nih.gov/13612293/) | 1958 | Case Series | Lyon Médical | Two cases of mycosis fungoides treated with delta-cortisone; reports fatal ulceronecrotic processes likely connected to medication — a critical safety signal for glucocorticoid use in CTCL. |
| [13573074](https://pubmed.ncbi.nlm.nih.gov/13573074/) | 1958 | Case Series | Bull Soc Fr Dermatol Syphiligr | Two cases of mycosis fungoides treated with prednisone (cortisone analog); documents fatal ulcero-necrotic processes as a probable drug effect, reinforcing the immunosuppression-related harm pattern. |
| [13536705](https://pubmed.ncbi.nlm.nih.gov/13536705/) | 1957 | Case Report | Bull Soc Fr Dermatol Syphiligr | Two cases of bronchial epithelioma arising in patients with mycosis fungoides during cortisone treatment; raises concerns about secondary malignancy risk from cortisone-induced immunosuppression. |
| [14169182](https://pubmed.ncbi.nlm.nih.gov/14169182/) | 1964 | Historical Review | J Med Chir Prat | Historical review of mycosis fungoides covering diagnostic and treatment approaches; contextualizes early cortisone therapy within the pre-modern-chemotherapy era. |
| [4241287](https://pubmed.ncbi.nlm.nih.gov/4241287/) | 1969 | Narrative Review | Münch Med Wochenschr | Review of climatotherapy and systemic approaches in dermatoses; discusses treatment of mycosis fungoides and related dermatological conditions including corticosteroid use. |
| [5161189](https://pubmed.ncbi.nlm.nih.gov/5161189/) | 1971 | Case Report | Bull Soc Fr Dermatol Syphiligr | Atypical case of mycosis fungoides with pleuropulmonary origin and sclerodermiform skin manifestations; treated with nitrogen mustard, illustrating the shift toward cytotoxic alternatives over cortisone. |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Historical safety signal from literature**: Case series from 1957–1958 (PMID 13612293, PMID 13573074) documented fatal ulceronecrotic complications in mycosis fungoides patients receiving cortisone or prednisone, and a separate report (PMID 13536705) raised concerns about secondary malignancy during cortisone treatment. These findings suggest that cortisone's immunosuppressive mechanism may be harmful in CTCL rather than therapeutic. Formal pharmacovigilance review and current safety data (package insert) are required before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All available evidence for cortisone in primary cutaneous T-cell lymphoma derives from 1950s case series documenting temporary remissions in mycosis fungoides, accompanied by serious — including fatal — safety signals. No modern clinical trials, prospective studies, or controlled data directly address cortisone in CTCL, and every contemporary lymphoma regimen that incorporates a glucocorticoid uses more potent alternatives (prednisolone, dexamethasone) that have superseded cortisone entirely.

**To proceed, the following is needed:**
- Obtain full DrugBank MOA data to formally document the mechanistic basis for lymphocytotoxic activity
- Review current package insert and TFDA/FDA safety records to establish up-to-date contraindications and warnings
- Conduct a comparative analysis of cortisone vs. prednisolone/dexamethasone in CTCL to determine whether cortisone offers any distinct pharmacological advantage (e.g., differential tissue distribution, unique metabolite profile)
- Commission modern preclinical studies in validated CTCL cell lines and animal models using contemporary dosing protocols
- If preclinical results are promising, initiate a systematic review of whether re-examining cortisone within a combination regimen context (similar to how prednisone is used in CHOP) is scientifically justified
- Ensure any further development plan includes a formal risk management strategy for the documented immunosuppression-related harm signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

