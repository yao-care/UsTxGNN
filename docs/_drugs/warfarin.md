---
layout: default
title: Warfarin
parent: Moderate Evidence (L3-L4)
nav_order: 1298
evidence_level: L4
indication_count: 7
---

# Warfarin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Warfarin: From Anticoagulation to Heparin Cofactor II Deficiency

## One-Sentence Summary

Warfarin is an oral vitamin K antagonist anticoagulant, and the data supplied lists no approved indication text.
The TxGNN model predicts it may be useful for **heparin cofactor II deficiency**, but this prediction has **0 clinical trials** and only **5 publications**, all case reports, a review or a laboratory-method paper.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the five listed below are ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, warfarin is a long-term oral anticoagulant used to prevent and treat thrombosis, and heparin cofactor II (HC II) deficiency is a hereditary thrombophilia. Mechanistically, warfarin may be applicable to the deficiency.

HC II deficiency predisposes patients to venous thrombosis, so anticoagulant therapy is a plausible management approach. This is an inference from drug class only. The retrieved literature does not confirm warfarin outcomes in HC II deficiency. The prediction therefore looks like an extension of warfarin's existing anticoagulant use, not a distinct repurposing signal.

The other six predicted indications fall into three groups:
- **Antithrombin deficiency type 2 and factor V excess:** plausible by class, but with at most one case report.
- **Thrombophilia:** the best-supported alternative, with L3 evidence and many trials and papers.
- **Rheumatoid arthritis and breast fibrocystic disease (and its synonym, benign mammary dysplasia):** no therapeutic rationale found, likely knowledge-graph artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11177584](https://pubmed.ncbi.nlm.nih.gov/11177584/) | 2001 | Review | AIDS Patient Care STDs | Review of thrombotic events and hypercoagulable abnormalities in HIV/AIDS patients, including deficiencies of natural anticoagulant proteins |
| [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) | 1990 | Case report | Kyobu Geka | A 14-year-old girl with familial HC II deficiency had a right ventricular thrombus that was surgically removed |
| [3778142](https://pubmed.ncbi.nlm.nih.gov/3778142/) | 1986 | Laboratory method | Arch Pathol Lab Med | Laboratory assay for HC II activity. Low levels were seen in liver disease, consumptive coagulopathy and preeclampsia |
| [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) | 1991 | Case report | Nihon Kyobu Shikkan Gakkai Zasshi | A woman with congenital antithrombin II (HC II) deficiency and repeated thromboses, including pulmonary infarction, had been on warfarin for 7 years. Warfarin was stopped on admission and replaced with low-dose heparin |
| [11570053](https://pubmed.ncbi.nlm.nih.gov/11570053/) | 2001 | Case report | J UOEH | A family with multiple thromboses in which known hereditary thrombophilias were ruled out. One child developed repeat DVT despite warfarin. Only indirectly relevant to HC II deficiency |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA040301 | Warfarin Sodium | Tablet | Golden State Medical Supply, Inc. |
| ANDA202202 | Warfarin Sodium | Tablet | REMEDYREPACK INC. |
| ANDA040301 | Warfarin Sodium | Tablet | Aphena Pharma Solutions - Tennessee, LLC |
| ANDA040616 | Warfarin Sodium | Tablet | PD-Rx Pharmaceuticals, Inc. |
| ANDA090935 | Warfarin Sodium | Tablet | Golden State Medical Supply, Inc. |

The only route is oral (tablet).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (99.87%), but the score is not clinical evidence. The supporting literature is five case reports, one review and one laboratory-method paper, with no trials. One case report even describes a patient switched from warfarin to heparin. The use also overlaps with warfarin's existing anticoagulant indications, so it offers little new repurposing value.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications (blocking gap for safety screening)
- Mechanism of action data (MOA) from DrugBank
- Targeted literature review of warfarin outcomes in HC II deficiency, including bleeding risk and INR management
- If a thrombosis-related direction is wanted, consider the broader **thrombophilia** prediction (rank 4, L3 evidence, many trials and reviews) instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

