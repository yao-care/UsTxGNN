---
layout: default
title: Nystatin
parent: 僅模型預測 (L5)
nav_order: 978
evidence_level: L5
indication_count: 10
---

# Nystatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Nystatin: From Antifungal Therapy (Established Use) to Predicted Vulvovaginitis Indication

## One-Sentence Summary

> Nystatin is a polyene antifungal that disrupts fungal cell membranes by binding ergosterol; detailed original-indication and regulatory history are not available in the current dataset, and the drug is currently **not marketed in Taiwan**.
> The TxGNN model predicts continued/expanded efficacy for **Vulvovaginitis** (Candida-driven vaginal inflammation), with a **99.92% prediction score**, **0 registered clinical trials**, and **20 supporting publications** (mostly reviews, one cohort study).
> Notably, the underlying rationale indicates this is likely an **already-established antifungal indication** captured by the knowledge graph rather than a genuinely novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in dataset — no license or original-indication records found |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Licenses (NDAs) | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug profile (`original_moa: [Data Gap]`). However, the prediction rationale supplied with this evidence pack describes Nystatin as a **polyene antifungal** that binds ergosterol in fungal cell membranes, disrupting membrane permeability and causing fungal cell death.

Vulvovaginitis is predominantly caused by *Candida albicans* (85–90% of cases per the cited literature). Nystatin's core antifungal mechanism maps directly onto this pathophysiology — there is no need to invoke an indirect or repurposed pathway, since topical/local antifungal treatment of candidal vulvovaginitis is a direct application of the drug's known mode of action.

Importantly, the evidence pack itself flags a key caveat: **this appears to be an already-established/traditional indication rather than a novel discovery**. The high TxGNN score likely reflects pre-existing, well-documented drug–disease associations already embedded in the knowledge graph, not a new hypothesis requiring independent validation. This should be factored into any decision-making — the "prediction" largely confirms known clinical practice.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16047929](https://pubmed.ncbi.nlm.nih.gov/16047929/) | 2005 | Cohort | Ceska gynekologie | Evaluated combined vaginal nystatin + nifuratel therapy for mixed/miscellaneous vulvovaginitis |
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Clinical/In vitro | Mycoses | Correlated fluconazole/nystatin in vitro susceptibility with clinical outcomes in 283 patients with complicated VVC |
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | Update on managing fluconazole-resistant VVC; nystatin discussed as an alternative antifungal option |
| [30359236](https://pubmed.ncbi.nlm.nih.gov/30359236/) | 2018 | Mechanistic (animal) | BMC Microbiology | Nystatin enhanced mucosal immune response and protected vaginal epithelial ultrastructure in a rat VVC model |
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Review | BMJ Clinical Evidence | Overview of vulvovaginal candidiasis as second most common cause of vaginitis |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Women's Health | Reviews boric acid and alternative therapies for recurrent VVC amid rising azole resistance |
| [21718579](https://pubmed.ncbi.nlm.nih.gov/21718579/) | 2010 | Review | BMJ Clinical Evidence | Epidemiology and management overview of vulvovaginal candidiasis |
| [12228137](https://pubmed.ncbi.nlm.nih.gov/12228137/) | 2002 | Review | BMJ | Clinical review of vulvovaginal candidiasis diagnosis and treatment |
| [11363911](https://pubmed.ncbi.nlm.nih.gov/11363911/) | 1996 | Review | J Int Assoc Physicians AIDS Care | General review of candidiasis management |
| [4919155](https://pubmed.ncbi.nlm.nih.gov/4919155/) | 1970 | Review | Med Clin North Am | Early foundational review of nystatin pharmacology and clinical use |

---

## US Market Information

Currently no market authorization data available — Nystatin has 0 registered licenses and is not marketed in Taiwan under the current dataset.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack; TFDA label/warning data acquisition is flagged as a **Blocking** data gap — see Next Steps.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is strong and direct (Nystatin's known antifungal action against *Candida* directly explains efficacy in vulvovaginitis), and is supported by 20 publications including one cohort study — but there are **no registered clinical trials** for this specific indication, and the evidence pack itself suggests this may simply reflect an already-established clinical use rather than a new discovery requiring validation.

**To proceed, the following is needed:**
- Obtain TFDA label warnings/contraindications (Blocking gap, DG001) before any S1 safety assessment
- Obtain confirmed mechanism of action from DrugBank (High-priority gap, DG002)
- Clarify Taiwan market/licensing status and available dosage forms/routes (currently 0 licenses, "not marketed") to assess feasibility of pursuing this indication locally
- Confirm whether related lower-confidence candidates in the same disease cluster (e.g., vulvitis, rank 8, evidence level L3; postmenopausal atrophic vaginitis, rank 6, evidence level L5 — likely a false positive due to lexical overlap with "vaginitis") should be deprioritized or excluded from further review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

