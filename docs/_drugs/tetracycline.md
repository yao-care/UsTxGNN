---
layout: default
title: Tetracycline
parent: 僅模型預測 (L5)
nav_order: 638
evidence_level: L5
indication_count: 4
---

# Tetracycline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Tetracycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Tetracycline is a broad-spectrum antibiotic of the tetracycline class, historically used to treat a wide range of bacterial infections including chlamydial, respiratory, and skin infections.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis (PEK)**,
with **0 clinical trials** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (broad-spectrum tetracycline-class antibiotic) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L4 |
| US Market Status | Not Marketed (no NDA on record) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on established pharmacological knowledge, Tetracycline is a member of the tetracycline antibiotic class. It exerts antibacterial activity by inhibiting the 30S ribosomal subunit, blocking bacterial protein synthesis. Notably, the tetracycline class also demonstrates anti-inflammatory effects through inhibition of matrix metalloproteinases (MMPs), an effect that is independent of its antimicrobial action.

Punctate epithelial keratoconjunctivitis (PEK) is a condition characterized by multiple focal corneal epithelial defects. One well-recognized infectious cause is *Chlamydia trachomatis*, the pathogen responsible for trachoma and chlamydial follicular conjunctivitis — organisms against which Tetracycline has direct, established antibacterial activity. Furthermore, MMP inhibition may reduce corneal stromal inflammation and limit progressive epithelial damage, providing a secondary anti-inflammatory rationale for use in PEK.

However, the mechanistic link must be interpreted with caution. The sole available literature describes PEK as a *sequela* that persisted after chlamydial conjunctivitis was treated with oral tetracycline — not a study designed to evaluate Tetracycline as a treatment for PEK itself. The prediction is biologically plausible but lacks interventional clinical evidence at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case Series | *Cornea* | Two patients with chlamydial follicular conjunctivitis were treated with oral tetracycline or doxycycline, achieving resolution of follicles; both subsequently developed recurrent bilateral punctate epithelial keratitis with grayish corneal lesions and anterior stromal edema, suggesting PEK can persist as a post-infectious sequela even after treatment |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The single available publication (a 1992 case series) describes PEK as a residual complication *after* tetracycline treatment of chlamydial conjunctivitis — it does not constitute evidence that Tetracycline treats PEK. With no clinical trials registered and only a mechanism-level inference connecting the drug to this indication, the evidence base is insufficient to support further development at this time.

**To proceed, the following is needed:**

- **MOA verification**: Obtain full mechanism of action data from DrugBank (DrugBank ID: DB00759) to confirm MMP-inhibitory and anti-chlamydial pharmacodynamic properties
- **Safety profile**: Review the package insert to document key warnings, contraindications, and ocular-use safety data before any ophthalmic indication work begins
- **Route compatibility assessment**: Evaluate whether topical ophthalmic formulations of tetracycline (eye drops or ointment) are available or feasible, as systemic oral dosing for a corneal epithelial condition raises bioavailability concerns
- **Targeted literature search**: Commission a focused search for prospective or interventional studies on tetracycline (or doxycycline as a class proxy) directly treating PEK, particularly in trachoma-endemic regions where chlamydial PEK is clinically relevant
- **Class extrapolation decision**: Determine whether evidence from doxycycline (a next-generation tetracycline with superior bioavailability and safety profile) can serve as a valid proxy for Tetracycline in this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

