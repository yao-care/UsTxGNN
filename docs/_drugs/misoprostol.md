---
layout: default
title: Misoprostol
parent: Model Prediction Only (L5)
nav_order: 935
evidence_level: L5
indication_count: 2
---

# Misoprostol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Misoprostol: From NSAID-Induced Gastric Ulcer Prevention to Amenorrhea

## One-Sentence Summary

Misoprostol is an oral synthetic prostaglandin E1 analog. In the US it is generally labeled for reducing the risk of NSAID-induced gastric ulcers, although the Evidence Pack does not list an approved indication.
The TxGNN model predicts it may be effective for **amenorrhea** (score 99.64%), but there are **0 registered clinical trials** and only **7 publications**, none of which studies misoprostol as a treatment for amenorrhea.
The evidence is therefore indirect, and the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Evidence Pack (general US labeling: reducing the risk of NSAID-induced gastric ulcers) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L4 (indirect literature only; no trials on amenorrhea treatment) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all generic ANDA licenses) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Misoprostol is a synthetic prostaglandin E1 analog with uterotonic and cervical-ripening effects. These properties are why it is widely used in reproductive medicine, for example for uterine evacuation.

The link to amenorrhea is indirect. The retrieved literature is about medical abortion, mainly low-dose mifepristone plus misoprostol in very early pregnancy, and about missed abortion. In these studies "amenorrhea" only describes gestational age (for example, "amenorrhea ≤35 days"), so a missed period is where misoprostol is used to bring on uterine evacuation and menstrual-like bleeding. This does not show that misoprostol treats amenorrhea itself.

The very high TxGNN score is a model output only. It may reflect knowledge-graph proximity between misoprostol and reproductive-health terms rather than a real therapeutic relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (neither ClinicalTrials.gov nor ICTRP).

---

## Literature Evidence

None of these publications tests misoprostol as a treatment for amenorrhea. The first six concern pregnancy termination or unrelated conditions. The Endometrial ablation review does not involve misoprostol.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reproductive Sciences | 744 women with ultra-early pregnancy (amenorrhea ≤35 days) compared hospital-administered with self-administered misoprostol after low-dose mifepristone for medical abortion. |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT (dose-ranging) | Reproductive Sciences | 2,500 women received mifepristone 50–150 mg followed by oral misoprostol 200 µg. The study evaluated complete abortion without surgery for ultra-early pregnancy. |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Clinical study | Human Reproduction | Low-dose mifepristone plus misoprostol before expected menstruation was evaluated for preventing unintended pregnancy. The design is not verified from the title. |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Cohort/clinical study | J Obstet Gynaecol Res | Safety and efficacy of self-administered misoprostol with low-dose mifepristone for early pregnancy termination. |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Review/clinical report | BMJ | Medical management of missed abortion and anembryonic pregnancy. No abstract available. |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | J Obstet Gynaecol Can | Endometrial ablation for abnormal uterine bleeding. Misoprostol is not the intervention. |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case report | Cureus | Acute fatty liver of pregnancy in a woman who presented with amenorrhea. Unrelated to misoprostol treatment. |

---

## US Market Information

The Evidence Pack contains no approved-indication text for these licenses, so the manufacturer is shown instead. Five of 20 licenses are listed. All are oral tablets.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA076095 | Misoprostol | Tablet | GenBioPro, Inc. |
| ANDA076095 | Misoprostol | Tablet | ANI Pharmaceuticals, Inc. |
| ANDA210201 | Misoprostol | Tablet | AvPAK |
| ANDA076095 | Misoprostol | Tablet | Cardinal Health 107, LLC |
| ANDA091667 | Misoprostol | Tablet | Novel Laboratories, Inc. |

---

## Safety Considerations

Please refer to the package insert for safety information.

One point is worth stating even though the Evidence Pack has no structured safety data. Misoprostol is contraindicated in pregnancy, which matters for any use in women of reproductive age where pregnancy has not been excluded. This is standard labeling knowledge and is also noted in the rationale text of the Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No trials exist, and the retrieved literature concerns abortion, not treatment of amenorrhea. Using misoprostol to induce uterine evacuation in early pregnancy is a different clinical purpose from treating amenorrhea. Safety data are also missing, which blocks progression past the initial screening stage.

The second predicted indication, atypical coarctation of aorta (score 99.30%), has no trials or literature. Its only rationale is theoretical (PGE1/alprostadil is given IV to keep the ductus arteriosus open). It is also on Hold.

**To proceed, the following is needed:**
- The package insert warnings and contraindications (a blocking gap for safety screening).
- Mechanism of action data (for example from the DrugBank API) to check whether a mechanistic link to amenorrhea exists.
- The original approved indications, to assess how the original use relates to the predicted one.
- Targeted literature on misoprostol for amenorrhea or menstrual induction in non-pregnant women, to test whether the model's prediction reflects a real signal.
- Confirmation that the target population and route (oral tablet) are clinically appropriate, including a pregnancy-exclusion plan.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

