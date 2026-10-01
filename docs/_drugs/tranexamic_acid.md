---
layout: default
title: Tranexamic Acid
parent: Moderate Evidence (L3-L4)
nav_order: 1248
evidence_level: L4
indication_count: 1
---

# Tranexamic Acid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Tranexamic Acid: From Bleeding Control to Amenorrhea

## One-Sentence Summary

Tranexamic acid is an antifibrinolytic drug used to reduce bleeding, including heavy menstrual bleeding.
The TxGNN model predicts it may be effective for **amenorrhea**, but the mechanism argues against this, and no clinical trials support it.
Only **2 general review articles** on related bleeding topics are available, and neither directly tests this use.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the five listed are all ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. This assessment therefore relies on general pharmacology knowledge.

Tranexamic acid is a lysine-analogue antifibrinolytic. It blocks plasminogen from binding to fibrin, which reduces the breakdown of blood clots. It is an established therapy for heavy menstrual bleeding and abnormal uterine bleeding.

**The prediction is weak mechanistically.** Amenorrhea means the absence of menstrual periods. Tranexamic acid does not suppress ovulation or endometrial growth, so it is not expected to induce or treat amenorrhea. The very high TxGNN score (0.99) most likely reflects the drug's closeness to menstrual-disorder nodes in the knowledge graph, not a therapeutic effect.

The only plausible link is indirect. In patients with bleeding disorders or blood cancers, tranexamic acid may be one part of a bleeding-control plan alongside hormonal menses suppression. Since the drug does not itself produce amenorrhea, this remains a hypothesis without direct support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause | Evidence-based review of drug treatments for abnormal uterine bleeding. Treatments are generally effective and well tolerated. Choice depends on the cause and amount of bleeding, contraception needs, fertility, and perimenopausal status. |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Review | J Oncol Pharm Pract | Approach to preventing and suppressing menses in premenopausal women with blood cancers. Several agents exist, but data comparing them are scarce, especially in cancer patients. |

Both papers cover menstrual-bleeding management in general. Neither shows that tranexamic acid treats amenorrhea.

---

## US Market Information

The Evidence Pack lists no approved-indication text for these products. The table below shows the first 5 of 20 authorizations.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA203521 | Tranexamic Acid | Injection, solution | Heritage Pharmaceuticals Labs Inc. (Avet) |
| ANDA205035 | Tranexamic Acid | Injection, solution | HF Acquisition Co LLC, DBA HealthFirst |
| ANDA202093 | Tranexamic Acid | Tablet, film coated | Actavis Pharma, Inc. |
| ANDA218320 | Tranexamic Acid | Tablet | Advagen Pharma Limited |
| ANDA203521 | Tranexamic Acid | Injection | Northstar Rx LLC |

Both injectable and oral forms are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on model score. The drug's mechanism (reducing bleeding, not suppressing menses) does not support treating amenorrhea. No clinical trials exist, and the two available reviews do not address this use.

**To proceed, the following is needed:**
- The US package insert warnings and contraindications, which are required for any safety screening.
- Detailed mechanism of action data from DrugBank, to test the indirect-link hypothesis.
- A clear clinical rationale, such as a specific patient group (for example, bleeding disorders or blood cancers) where tranexamic acid plays a supporting role in menses management.
- Evidence from trials or studies that directly test tranexamic acid in a menses-suppression setting.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

