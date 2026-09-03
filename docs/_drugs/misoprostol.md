---
layout: default
title: Misoprostol
parent: 僅模型預測 (L5)
nav_order: 935
evidence_level: L5
indication_count: 2
---

# Misoprostol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Misoprostol: From an Undocumented Original Indication to Amenorrhea

## One-Sentence Summary

> Misoprostol (DrugBank DB00929) is a prostaglandin E1 (PGE1) analog; its originally approved indication is not documented in this evidence pack (Blocking data gap).
> The TxGNN model predicts it may be effective for **Amenorrhea**, with a prediction score of **99.64%**,
> but **0 clinical trials** and only **7 loosely related publications** currently support this direction — none of which studies misoprostol as a treatment *for* amenorrhea.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current evidence pack (drug not marketed; 0 regulatory licenses on file) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.64% (rank 9256) |
| Evidence Level | L4 (mechanism-only; no clinical trials, and available literature does not directly test the predicted indication) |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for misoprostol is not available in this evidence pack (data gap DG002). Based on known pharmacological class, misoprostol is a synthetic prostaglandin E1 (PGE1) analog whose primary clinical effects are inducing uterine contraction, ripening the cervix, and promoting expulsion of uterine contents — actions used across obstetric and gynecologic practice (e.g., labor induction, medical abortion, missed abortion management, postpartum hemorrhage).

This creates a directional mismatch with the predicted indication. Amenorrhea is the *absence* of menstruation, while misoprostol's known pharmacology is oriented toward *inducing* uterine bleeding/expulsion. All 7 literature results returned for this pairing concern termination of pregnancy, missed/incomplete abortion, or abnormal uterine bleeding management — not treatment of amenorrhea as a condition. The more plausible explanation is that TxGNN's knowledge graph places misoprostol near disease nodes that co-occur with "amenorrhea" in a pregnancy/reproductive-health context (e.g., as an inclusion criterion — "amenorrhea ≤35 days" defining early pregnancy in several trials), rather than a genuine treatment-efficacy signal.

A second, lower-ranked candidate (Atypical Coarctation of Aorta, score 99.30%, rank 15668) has a more coherent mechanistic story: PGE1 analogs (e.g., alprostadil) are used to maintain ductus arteriosus patency in duct-dependent congenital heart disease, and misoprostol's PGE1 activity could theoretically extend to this. However, this candidate has **zero** supporting clinical trials or literature (Evidence Level L5) and is not discussed further below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT | Reproductive Sciences | Dose-ranging RCT (n=2500) of mifepristone (50–150mg) + misoprostol for termination of ultra-early pregnancy (amenorrhea ≤35 days); not a study of amenorrhea treatment |
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT/Cohort | Reproductive Sciences | RCT (n=744) of low-dose mifepristone + self-administered misoprostol for ultra-early medical abortion, comparing hospital vs. self-administration |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | J Obstet Gynaecol Can | Review of endometrial ablation for abnormal uterine bleeding management; misoprostol context not central |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Cohort | Human Reproduction | Feasibility of low-dose mifepristone + misoprostol for unintended-pregnancy prevention administered before expected menstruation |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Cohort | J Obstet Gynaecol Res | Safety/efficacy of self-administered low-dose mifepristone + misoprostol for early medical abortion |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Cohort | BMJ | Medical management of missed abortion and anembryonic pregnancy |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case report | Cureus | Case report of acute fatty liver of pregnancy presenting with amenorrhea as a symptom, not as a treatment target |

**Note:** all seven results relate misoprostol to pregnancy termination or use "amenorrhea" only as a gestational-age descriptor. None evaluates misoprostol as a therapy for amenorrhea itself.

---

## US Market Information

No regulatory licenses on file — misoprostol is currently recorded as **未上市 (not marketed)** in this jurisdiction (0 total licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(TFDA labeling warnings/contraindications and DDI data are marked as Blocking data gaps (DG001) in this evidence pack and could not be retrieved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted score is high, but the supporting evidence is mechanistically incoherent with the predicted indication — all available literature concerns pregnancy termination, not amenorrhea treatment — and no clinical trials exist for this drug-disease pair. This pattern is consistent with a spurious knowledge-graph association rather than a genuine repurposing signal, and a Blocking safety data gap (TFDA label data) prevents any safety pre-screening regardless.

**To proceed, the following is needed:**
- TFDA label data (warnings, contraindications) to clear the Blocking gap (DG001)
- Confirmed original approved indication and MOA for misoprostol (DG002)
- Clinical/pharmacological clarification of what "amenorrhea" means in the TxGNN prediction context (induction of menses vs. treatment of amenorrhea as a condition) before further evidence search
- If pursued, a targeted literature search specifically on misoprostol's use in secondary amenorrhea etiologies, distinct from its use in pregnancy-termination protocols
- No further action recommended on the secondary candidate (Atypical Coarctation of Aorta) absent any clinical or preclinical evidence (currently L5)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

