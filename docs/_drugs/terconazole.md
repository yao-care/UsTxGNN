---
layout: default
title: Terconazole
parent: 僅模型預測 (L5)
nav_order: 632
evidence_level: L5
indication_count: 10
---

# Terconazole
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

# Terconazole: From Vulvovaginal Candidiasis to Trichomonal Vulvovaginitis

## One-Sentence Summary

Terconazole is a triazole antifungal agent widely used internationally for vulvovaginal candidiasis, with no currently approved product in Taiwan.
The TxGNN model assigns its top score to **trichomonal vulvovaginitis** (99.86%), though the mechanistic link is weak — trichomonal infection is caused by a protozoan, not a fungus.
Supporting evidence is limited to **1 pilot clinical trial** and **3 non-specific review publications**, none of which are designed specifically for *Trichomonas* infection.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vulvovaginal candidiasis (established international use; no Taiwan NDA) |
| Predicted New Indication | Trichomonal vulvovaginitis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, terconazole is a triazole antifungal whose primary target is CYP51 (lanosterol 14α-demethylase), a fungal cytochrome P450 enzyme essential for ergosterol biosynthesis. Blocking CYP51 depletes ergosterol and disrupts the fungal cell membrane, ultimately killing the organism. This mechanism is extensively validated across multiple clinical formulations (cream, vaginal suppository) in the treatment of vulvovaginal candidiasis.

Trichomonal vulvovaginitis is caused by *Trichomonas vaginalis*, a flagellated protozoan — not a fungus. Protozoa do not rely on ergosterol biosynthesis in the same way fungi do, and terconazole's CYP51 inhibitory activity confers no expected antiprotozoal effect. The 1983 paper included in this evidence pack (PMID 6617296) describes terconazole as a "broad-spectrum antifungal," referring to its cross-species fungal activity (yeasts, dermatophytes, mycelium-forming fungi) — not cross-kingdom activity against protozoa.

The TxGNN score of 99.86% most likely reflects anatomical co-clustering: the model learned that terconazole is used for vaginal conditions, and trichomonal vulvovaginitis occupies the same anatomical space. This is a known limitation of graph-based prediction models when phenotypic similarity overrides mechanistic distance. Standard of care for trichomonal vulvovaginitis is metronidazole, which acts through nitroreduction and has direct antiprotozoal activity. Without any preclinical evidence of terconazole activity against *T. vaginalis*, this prediction cannot be advanced to clinical evaluation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00503542](https://clinicaltrials.gov/study/NCT00503542) | Early Phase 1 | Completed | 46 | Pilot study in primary care testing two management strategies for general vaginal complaints; terconazole is one of multiple options included, not specifically evaluated for *Trichomonas* infection; no trichomonal-specific efficacy signal can be extracted |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [10546257](https://pubmed.ncbi.nlm.nih.gov/10546257/) | 1999 | Review | The Nurse Practitioner | Broad clinical overview of vaginitis management across bacterial, fungal, and protozoal subtypes; terconazole is discussed exclusively in the context of vulvovaginal candidiasis |
| [10470518](https://pubmed.ncbi.nlm.nih.gov/10470518/) | 1999 | Review | Comprehensive Therapy | Epidemiology, diagnosis, and treatment review of vulvovaginal symptoms in healthy women; covers multiple etiologies but does not attribute antiprotozoal activity to terconazole |
| [6617296](https://pubmed.ncbi.nlm.nih.gov/6617296/) | 1983 | Drug Description/Review | Chemotherapy | Original characterization of terconazole as a broad-spectrum antifungal; documents high in vitro activity against yeasts and mycelium-forming fungi; CYP51-based antifungal mechanism described; no antiprotozoal activity tested or claimed |

---

## Taiwan Market Information

Terconazole has no approved products registered in Taiwan as of the data cutoff (2026-06-22). There are 0 NDAs on record. Any future commercialization would require a full NDA submission to the Taiwan FDA (TFDA).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Trichomonal vulvovaginitis is a protozoal infection that falls entirely outside terconazole's antifungal mechanism (fungal CYP51 inhibition → ergosterol depletion), and there is no dedicated clinical or preclinical evidence to support this new use. The high TxGNN score reflects anatomical co-clustering rather than mechanistic plausibility, and the current standard treatment (metronidazole) is mechanistically unrelated to terconazole.

**To proceed, the following is needed:**
- In vitro antiprotozoal activity data: terconazole MIC testing against *Trichomonas vaginalis* strains
- Mechanistic rationale demonstrating CYP51 relevance in *T. vaginalis* biology or an alternative terconazole target in protozoa
- Clinical proof-of-concept study specifically enrolling patients with microbiologically confirmed trichomonal infection
- TFDA package insert data to complete the S1 safety screening currently blocked by missing warnings and contraindication data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

