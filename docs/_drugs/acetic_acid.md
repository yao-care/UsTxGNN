---
layout: default
title: Acetic Acid
parent: Model Prediction Only (L5)
nav_order: 120
evidence_level: L5
indication_count: 9
monitor_inn: "ACETIC ACID"
predicted_indications: ["post-bacterial disorder", "postinfectious vasculitis", "post-infectious syndrome", "Chagas cardiomyopathy", "infective urethral stricture", "infection-related hemolytic uremic syndrome", "drug-induced osteoporosis", "pityriasis simplex", "tinea corporis"]
last_modified_at: 2026-10-14
description: "Acetic Acid: predicted new indication Tinea corporis (evidence level L5). Approved use: Otitis externa"
---

# Acetic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Acetic Acid: From Otitis Externa to Tinea Corporis

## One-Sentence Summary

Acetic acid is a simple topical antiseptic and irrigant, originally used for ear conditions such as otitis externa.
The TxGNN model predicts several new indications. The most evidence-supported one is **Tinea Corporis** (score 99.25%), which has **0 clinical trials** and **10 publications** (mostly historical reports or in vitro studies).
The top-scoring predictions (e.g., post-bacterial disorder) have no supporting studies at all.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Otitis externa; external ear disease |
| Predicted New Indication | Tinea corporis (highest-ranked prediction by TxGNN is post-bacterial disorder, but it has no evidence, so tinea corporis is the focus here) |
| TxGNN Prediction Score | 99.25% (tinea corporis); 99.98% (post-bacterial disorder, rank 1, no evidence) |
| Evidence Level | L4 (tinea corporis); L5 for all other predictions |
| US Market Status | Cancelled only |
| Number of NDAs | 6 (all cancelled; includes ANDA and one unapproved homeopathic entry) |
| Recommended Decision | Hold (tinea corporis may be treated as a research question) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, acetic acid acts as a topical acidifier with antibacterial and antifungal properties. Its efficacy in external ear infections is thought to come from lowering local pH, which inhibits bacterial and fungal growth.

Tinea corporis is a superficial dermatophyte infection of the skin. Lowering skin pH may inhibit dermatophyte growth, so the idea is mechanistically plausible. Historical reports from 1946 to 1958 describe dilute acetic acid (with iodine) for tinea capitis and acetic acid for foot epidermophytosis, which are related dermatophyte infections. An in vitro onychomycosis model and a chemical peeling report offer indirect support. However, no modern controlled studies have been done in tinea corporis itself.

The higher-scoring predictions (post-bacterial disorder, postinfectious vasculitis, Chagas cardiomyopathy, infective urethral stricture, infection-related hemolytic uremic syndrome, drug-induced osteoporosis) have no clinical or literature evidence and no plausible mechanism. They should be regarded as computational predictions only. For post-infectious syndrome, the only publication is a review of animal models of post-infectious irritable bowel syndrome, where acetic acid is likely used as an experimental irritant, which suggests a causative rather than a therapeutic relationship.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The table covers tinea corporis, the best-supported prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20256868](https://pubmed.ncbi.nlm.nih.gov/20256868/) | 1947 | Historical case series | Urologic and Cutaneous Review | Results of treating tinea capitis with special iodine and dilute acetic acid in a larger patient series |
| [20996178](https://pubmed.ncbi.nlm.nih.gov/20996178/) | 1946 | Historical clinical report | JAMA | Tinea capitis treated with special iodine and dilute acetic acid |
| [20983383](https://pubmed.ncbi.nlm.nih.gov/20983383/) | 1946 | Historical clinical report | Archives of Dermatology and Syphilology | Treatment of tinea capitis with special iodine and dilute acetic acid |
| [13616002](https://pubmed.ncbi.nlm.nih.gov/13616002/) | 1958 | Historical clinical report | Vestnik Dermatologii i Venerologii | Treatment of foot epidermophytosis with increasing concentrations of acetic acid |
| [31049344](https://pubmed.ncbi.nlm.nih.gov/31049344/) | 2019 | Case report/series | Skin Appendage Disorders | Chemical peeling as an alternative to oral antifungals for onychomycosis in elderly and diabetic patients |
| [26857689](https://pubmed.ncbi.nlm.nih.gov/26857689/) | 2016 | In vitro study | Mycoses | Topical antifungal products compared in an in vitro onychomycosis model against *Trichophyton mentagrophytes* |
| [37256034](https://pubmed.ncbi.nlm.nih.gov/37256034/) | 2023 | Case series | Archives of Plastic Surgery | Etiology report of burns caused by Korean folk remedies; signals a safety concern with unsupervised acid-based home treatments |
| [33625606](https://pubmed.ncbi.nlm.nih.gov/33625606/) | 2021 | In vitro study (not acetic acid specific) | World J Microbiol Biotechnol | A *Lactobacillus plantarum* strain inhibited *Trichophyton rubrum* growth |
| [16233325](https://pubmed.ncbi.nlm.nih.gov/16233325/) | 2002 | In vitro study (not acetic acid specific) | J Biosci Bioeng | Fermented herb product showed antifungal activity against tinea under low-pH conditions |

Note: One additional retrieved publication (PMID 30941788, an analytical chemistry method paper on tolnaftate) is not relevant and is omitted. Several of the above (the lactic acid bacteria studies) are not specific to acetic acid and give only indirect support.

For post-infectious syndrome, the only publication is [20848144](https://pubmed.ncbi.nlm.nih.gov/20848144/) (2011, *J Gastroenterol*), a review of animal models of post-infectious IBS. It does not study acetic acid as a treatment.

## US Market Information

All six authorizations are cancelled; no product is currently marketed. The data compiled for this report contains no approved indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|------|------|
| ANDA040166 | Acetic Acid | Solution | Chartwell RX, LLC | Cancelled |
| NDA012179 | Acetic Acid | Solution | NuCare Pharmaceuticals, Inc. | Cancelled |
| ANDA040607 | Acetic Acid | Solution | A-S Medication Solutions | Cancelled |
| NDA018161 | Acetic Acid | Irrigant | B. Braun Medical Inc. | Cancelled |
| NDA018523 | Acetic Acid | Irrigant | Baxter Healthcare Corporation | Cancelled |

A sixth entry (Aceticum acidum, pellet, Boiron) has no authorization number and is also cancelled.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: inherited porphyria, porphyrin metabolism disease, porphyria, herpes simplex infectious disease, geniculate herpes zoster.
- **Practical safety signal**: a 2023 report documented burns from Korean folk remedies, which indicates a risk with unsupervised use of acid-based home treatments.
- **Drug Interactions**: No interactions were found in the queried database.

Please refer to the package insert for warnings and other safety information, as label text was not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions are supported only by model scores. Tinea corporis has the best indirect support (L4: historical reports and in vitro data, with plausible acidification-based antifungal activity), but it has no registered trials and no modern controlled studies. All US authorizations are cancelled, and label-based safety data are missing. Tinea corporis may be pursued as a research question; the other predictions should not be pursued without new evidence.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Modern controlled studies, or at least in vitro MIC data, of acetic acid against dermatophytes such as *Trichophyton rubrum*
- Formulation, concentration and skin-tolerability data, given the burn risk with acid-based remedies
- Route and formulation compatibility assessment (currently pending)
- Comparison with existing standard topical antifungals to determine whether any unmet need exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

