---
layout: default
title: Terconazole
parent: Moderate Evidence (L3-L4)
nav_order: 1213
evidence_level: L4
indication_count: 10
---

# Terconazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Terconazole: From Vulvovaginal Candidiasis to Trichomonal Vulvovaginitis

## One-Sentence Summary

Terconazole is a topical triazole antifungal, marketed in the US as a vaginal cream and suppository, and used mainly for vulvovaginal candidiasis.
The TxGNN model predicts it may be effective for **trichomonal vulvovaginitis**, but this direction has only **1 clinical trial** (an early-phase pilot on non-specific vaginal complaints) and **3 publications** (reviews), none of which show efficacy against Trichomonas.
The prediction is therefore weakly supported and should be treated as a model artifact until shown otherwise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vulvovaginal candidiasis (inferred from the literature; the US licence records contain no indication text) |
| Predicted New Indication | Trichomonal vulvovaginitis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 12 (all listed entries are ANDAs, i.e. generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Terconazole is a triazole antifungal that inhibits fungal lanosterol 14-alpha-demethylase (CYP51), blocking ergosterol synthesis in the fungal cell membrane. This is why it works against Candida. Its efficacy in candidal vulvovaginitis is well documented.

Trichomonas vaginalis, however, is a protozoan, not a fungus. It is normally treated with nitroimidazoles such as metronidazole, and there is no plausible azole mechanism against it. The high graph score most likely comes from the shared "vaginitis" neighborhood in the knowledge graph. Candidal and trichomonal infections are both vaginal infections, so the graph links them, but that proximity is not evidence of pharmacological activity.

Detailed mechanism-of-action data from DrugBank is not available in the Evidence Pack. The mechanism above comes from the analysis attached to the prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00503542](https://clinicaltrials.gov/study/NCT00503542) | Early Phase 1 | Completed | 46 | Pilot comparing two ways of managing women with vaginal complaints in primary care. It is not specific to trichomoniasis and gives no efficacy evidence for terconazole against Trichomonas. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10546257](https://pubmed.ncbi.nlm.nih.gov/10546257/) | 1999 | Review | The Nurse Practitioner | Overview of bacterial, fungal and protozoal vaginitis and their treatment. General background, not terconazole-specific. |
| [10470518](https://pubmed.ncbi.nlm.nih.gov/10470518/) | 1999 | Review | Comprehensive Therapy | Epidemiology, diagnosis and therapy of vaginitis in healthy women. General background. |
| [6617296](https://pubmed.ncbi.nlm.nih.gov/6617296/) | 1983 | Review | Chemotherapy | Terconazole is highly active in vitro against yeasts and mycelium-forming fungi. It is effective topically in animal models of dermatophytosis and candidosis. No protozoal data are described. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA075953 | Terconazole | Cream | A-S Medication Solutions |
| ANDA077553 | Terconazole | Suppository | Sun Pharmaceutical Industries, Inc. |
| ANDA076043 | Terconazole | Cream | A-S Medication Solutions |
| ANDA076712 | Terconazole | Cream | A-S Medication Solutions |
| ANDA076043 | Terconazole | Cream | Sun Pharmaceutical Industries, Inc. |

The source data do not include approved-indication text for these licences.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Terconazole has no plausible activity against a protozoan, and the supporting evidence is one non-specific pilot trial plus general reviews. The high TxGNN score most likely reflects knowledge-graph proximity to other vaginitis nodes rather than a real signal.

Other predictions in the same pack have far better support, but they are essentially candidal vulvovaginitis, which is the drug's existing use. Examples are vulvitis, vulvovaginitis and vaginitis, which have Phase 3 and 4 trials and multiple RCTs. They are not true repurposing signals and should be limited to candidal etiology.

**To proceed, the following is needed:**
- Any direct evidence (in vitro or clinical) of terconazole activity against *Trichomonas vaginalis*. Without it, this indication should not be pursued.
- Package insert warnings and contraindications, to unblock safety screening.
- Confirmation of the on-label indication from the US label, since the licence records contain no indication text.
- Mechanism-of-action data from DrugBank.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

