---
layout: default
title: Hydromorphone
parent: Model Prediction Only (L5)
nav_order: 777
evidence_level: L5
indication_count: 6
---

# Hydromorphone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Hydromorphone: From Opioid Pain Relief to Pharyngitis

## One-Sentence Summary

Hydromorphone is a mu-opioid pain medicine that is widely marketed in the US as tablets, extended-release tablets and injections. The TxGNN model predicts it may be effective for **pharyngitis**, but no trial or publication studies it for that condition. The 6 registered trials that matched the query are all about post-surgical pain (mainly after tonsillectomy) or other diseases, and there is **no directly relevant literature**.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 (no study tests hydromorphone in pharyngitis; the pipeline's automatic scoring shows L4) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

The US approved-indication text is empty for all listed licenses, so the original indication is not shown here.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. In general, hydromorphone is a mu-opioid agonist that gives central pain relief. It has no anti-infective or anti-inflammatory action against pharyngitis.

The high TxGNN score most likely reflects closeness in the knowledge graph between hydromorphone and throat or pain nodes, not a treatment effect. At most, hydromorphone might give nonspecific pain relief for a sore throat. Opioids are not a rational treatment for pharyngitis, which is usually a self-limiting infection.

The only related trial data concern pain after tonsillectomy, which is postoperative pain, not pharyngitis. The prediction should therefore be read as a low-confidence model output.

## Clinical Trial Evidence

None of these trials tests hydromorphone in pharyngitis. Only one (NCT04230681) tests hydromorphone directly, and it studies postoperative pain. The rest are incidental matches.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04230681](https://clinicaltrials.gov/study/NCT04230681) | Early Phase 1 | Completed | 189 | Hydromorphone vs fentanyl for pain control in children after tonsillectomy or adenotonsillectomy. The most relevant trial, but it addresses postoperative pain, not pharyngitis. No results provided. |
| [NCT05244226](https://clinicaltrials.gov/study/NCT05244226) | Phase 2 | Completed | 66 | Pilot comparing short-acting opioids (fentanyl/hydromorphone) with methadone for pediatric tonsillectomy pain. Hydromorphone is a comparator only. |
| [NCT06576830](https://clinicaltrials.gov/study/NCT06576830) | Phase 4 | Recruiting | 440 | Intraoperative methadone vs short-acting opioids (fentanyl/hydromorphone) for pain after pediatric tonsillectomy. |
| [NCT02996591](https://clinicaltrials.gov/study/NCT02996591) | Phase 4 | Completed | 36 | Spinal vs general anesthesia with nerve blocks for foot and ankle surgery. Unrelated to pharyngitis. |
| [NCT00189488](https://clinicaltrials.gov/study/NCT00189488) | Phase 2 | Completed | 155 | Palifermin to reduce graft-versus-host disease and oral mucositis after transplant. Different disease. |
| [NCT00109031](https://clinicaltrials.gov/study/NCT00109031) | Phase 3 | Completed | 47 | Single-dose vs 3-dose palifermin for oral mucositis after high-dose chemotherapy and irradiation. No hydromorphone efficacy signal. |

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| NDA019892 | Hydromorphone Hydrochloride (Rhodes Pharmaceuticals L.P.) | Tablet |
| NDA200403 | Hydromorphone Hydrochloride (Hospira, Inc.) | Injection, solution |
| ANDA204278 | Hydromorphone Hydrochloride (Padagis US LLC) | Tablet, extended release |
| ANDA205814 | Hydromorphone Hydrochloride (Aurolife Pharma, LLC) | Tablet |
| ANDA212133 | Hydromorphone Hydrochloride (Camber Pharmaceuticals, Inc.) | Tablet, extended release |

The oral and injectable forms above are 5 of the 20 licenses on file.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No trial or publication supports hydromorphone for pharyngitis, and the mechanism gives only nonspecific pain relief. Opioids are not a rational treatment for this usually self-limiting condition, so repurposing is not justified on current evidence.

**To proceed, the following is needed:**
- A clear rationale for why hydromorphone would treat pharyngitis, beyond symptomatic pain relief
- Mechanism of action data
- Package insert warnings and contraindications, which are still missing and block safety screening
- Any pharyngitis-specific clinical or literature evidence, which is currently absent

Among the other predicted indications for hydromorphone, **headache disorder** has the most evidence: a completed Phase 4 head-to-head RCT in acute migraine (NCT02389829) and several related publications. It is also on Hold, because the literature suggests hydromorphone serves as a comparator rather than a preferred therapy, and opioids carry dependence, medication-overuse headache and return-visit risks.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

