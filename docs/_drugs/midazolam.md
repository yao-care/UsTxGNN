---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 925
evidence_level: L5
indication_count: 1
---

# Midazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Midazolam: From Procedural Sedation to Insomnia

## One-Sentence Summary

> Midazolam is a short-acting benzodiazepine originally approved for procedural sedation and anesthesia induction.
> The TxGNN model predicts it may be effective for **Insomnia**,
> with **32 clinical trials** and **11 publications** currently identified in the evidence pack, though most reflect procedural/ICU sedation contexts rather than chronic insomnia treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Procedural sedation / anesthesia induction (per literature; drug is not TFDA-licensed in Taiwan) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| US Market Status | Not Marketed (Taiwan) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The structured `original_moa` field is a data gap, but the model's repurposing rationale provides mechanistic detail: midazolam is a short-acting benzodiazepine and positive allosteric modulator of the GABA-A receptor, producing sedative/hypnotic effects that are a class-effect of benzodiazepines rather than a mechanism unique to this drug. Its approved use is procedural sedation and anesthesia induction, with a short half-life (~1.5–2.5 hours) — a pharmacokinetic profile designed for brief procedural use, not chronic nightly dosing for insomnia.

Despite this mismatch in intended use duration, there is a real historical basis for the prediction: oral midazolam was studied as a hypnotic in the 1980s–1990s (dose-finding and comparative trials against flurazepam and other sedative-hypnotics), showing it can effectively induce and maintain sleep. The GABA-A mechanism that underlies its sedative action in anesthesia is the same mechanism that would underlie any hypnotic effect in insomnia, which is why TxGNN's prediction is mechanistically plausible.

However, the bulk of contemporary clinical trial activity involving midazolam is centered on ICU/procedural sedation, postoperative delirium, and comparisons against dexmedetomidine — not on chronic insomnia as a treatment target. This creates a gap between the historical proof-of-concept and current clinical development activity, which should temper the strength of this signal.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | NA | Recruiting | 280 | Preoperative oral midazolam in patients with sleep disturbance/anxiety undergoing colorectal cancer surgery; notes "midazolam oral solution is safe and effective for short-term hypnosis" |
| [NCT07336095](https://clinicaltrials.gov/study/NCT07336095) | Phase 3 | Not yet recruiting | 195 | Oral melatonin vs. oral midazolam as premedication in children; midazolam used as the sedative/hypnotic comparator |
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | Completed | 111 | Compares postoperative sleep quality of dexmedetomidine vs. midazolam sedation in TURP surgery |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | N/A | Terminated | 5 | Compares dexmedetomidine vs. midazolam on sleep quality/quantity (24h polysomnography) and delirium in ICU patients |
| [NCT04082767](https://clinicaltrials.gov/study/NCT04082767) | Phase 3 | Unknown | 120 | Sedation efficacy of dexmedetomidine vs. midazolam in critically ill ventilated children |
| [NCT04149626](https://clinicaltrials.gov/study/NCT04149626) | Phase 2 | Unknown | 60 | Compares dexmedetomidine, midazolam, and remifentanil for sedation in regional anesthesia |
| [NCT00744380](https://clinicaltrials.gov/study/NCT00744380) | NA | Completed | 23 | Dexmedetomidine vs. midazolam for facilitating extubation in ICU patients on benzodiazepine sedation |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | Terminated | 6 | Polysomnographic comparison of α2 agonist vs. GABA agonist (e.g., midazolam-class) sedation on sleep stages |
| [NCT05466279](https://clinicaltrials.gov/study/NCT05466279) | NA | Completed | 131 | Remazolam vs. propofol+midazolam general anesthesia comparison |
| [NCT06498869](https://clinicaltrials.gov/study/NCT06498869) | NA | Completed | 178 | Effect of ketamine on sleep quality (PSQI) in colonoscopy patients sedated with midazolam-based protocol |

*Note: most trials in the evidence pack involve midazolam in ICU/procedural sedation settings rather than a direct chronic-insomnia treatment design; several other retrieved trials were graded low relevance (e.g., NCT04399343, NCT01343095, NCT06493396) and are omitted here.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | British Journal of Clinical Pharmacology | Midazolam 15mg vs. Vesparax in insomnia secondary to neuromuscular disease; midazolam effective hypnotic, better tolerated, no hangover effect |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT | Journal of Clinical Psychopharmacology | 14-day multicenter RCT of flurazepam vs. midazolam in chronic insomniacs, examining sleep, performance, and plasma levels |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | RCT | Arzneimittel-Forschung | Dose-finding study of oral midazolam (10–30mg) in 75 patients with mild-moderate insomnia secondary to musculoskeletal/nerve disorders and allergies |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | RCT | Journal of Clinical Psychopharmacology | Executive summary of the 14-day multicenter flurazepam vs. midazolam study in chronic insomniacs |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | RCT | Journal of Clinical Medicine | Evaluates lemborexant (not midazolam) for insomnia to prevent delirium in high-risk sedation patients; notes benzodiazepines may worsen delirium |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Review | Orvosi Hetilap | General review of insomnia pathogenesis and cerebral hypoperfusion; not midazolam-specific |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Review | Acta Psychiatrica Scandinavica Supplementum | Review of hypnotic drug classes including benzodiazepines for insomnia management |
| [22729271](https://pubmed.ncbi.nlm.nih.gov/22729271/) | 2013 | Preclinical | Psychopharmacology | Zolpidem (not midazolam) effects on sedation, anxiety, and memory in an animal model |
| [21396773](https://pubmed.ncbi.nlm.nih.gov/21396773/) | 2011 | Preclinical | Pain | Mouse model of neuropathic pain-related sleep disturbance and GABAergic transmission; not midazolam-specific |
| [36912148](https://pubmed.ncbi.nlm.nih.gov/36912148/) | 2024 | Review | American Journal of Hospice & Palliative Care | End-of-life symptom management case discussion; low direct relevance to insomnia indication |

## Taiwan Market Information

Midazolam currently has no marketing authorization on record in Taiwan (0 licenses; market status: not marketed). No dosage form or approved indication data is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TFDA label/warning data needed for safety review (S1) is a blocking gap, midazolam has no marketing authorization in Taiwan, and while there is a plausible historical mechanistic basis (1980s–1990s RCTs of oral midazolam for insomnia), current clinical trial activity does not directly target chronic insomnia — most active trials use midazolam in procedural/ICU sedation contexts, and a durable therapeutic use would need to address dependency/abuse risk from repeated benzodiazepine dosing.

**To proceed, the following is needed:**
- TFDA/manufacturer label data on warnings, contraindications, and DDI (currently blocking)
- Confirmed structured MOA and original indication data from DrugBank
- Assessment of an appropriate oral formulation and dosing regimen for chronic (vs. procedural) use
- Safety monitoring plan addressing benzodiazepine dependency, tolerance, and elderly/fall-risk concerns (e.g., Beers Criteria)
- Pathway assessment for Taiwan market entry, given the drug currently holds no local license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

