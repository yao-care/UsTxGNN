---
layout: default
title: Pyrazinamide
parent: Model Prediction Only (L5)
nav_order: 1099
evidence_level: L5
indication_count: 10
---

# Pyrazinamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Pyrazinamide: From Tuberculosis to Infectious Otitis Media

## One-Sentence Summary

Pyrazinamide is a first-line oral antimycobacterial drug used in multidrug tuberculosis regimens.
The TxGNN model predicts it may be effective for **infectious otitis media** (score 99.96%),
but **0 clinical trials** and **0 publications** currently support this specific prediction, so it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (the approved indication text is blank in the supplied US license records) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 (all listed as ANDA generic approvals) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pyrazinamide is part of standard multidrug anti-tuberculosis therapy. Its efficacy in tuberculosis is established, but the supplied data do not show a mechanistic link to common ear infections.

The prediction is weak on mechanism. Pyrazinamide has no activity against the usual bacterial causes of otitis media. The only plausible connection is the rare tuberculous subset of middle ear infection, where anti-TB drugs are the treatment. That is the drug's existing anti-TB activity applied to an ear site, not a new mechanism. It does not justify use in infectious otitis media in general. The high score likely reflects a knowledge-graph neighborhood effect.

Other predictions for this drug have more supporting literature, though still weak:

- **Middle ear disease (rank 2, 99.92%)**: 7 retrieved publications, mostly case reports and small series of tuberculous otitis media treated with regimens that include pyrazinamide. Evidence level L4.
- **Chronic otitis media (rank 4)** and **suppurative otitis media (rank 5)**: the same type of tuberculous otitis media case reports. Evidence level L4.
- **Lyme disease (rank 9)**: no supportive evidence. The one retrieved trial tests doxycycline in pulmonary TB and does not involve pyrazinamide.

All of this evidence applies only to culture- or PCR-confirmed tuberculous etiology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA081319 | pyrazinamide (Hikma Pharmaceuticals USA Inc) | Tablet | Not listed in source data |
| ANDA080157 | PYRAZINAMIDE (Marlex Pharmaceuticals, Inc) | Tablet | Not listed in source data |
| ANDA080157 | Pyrazinamide (American Health Packaging) | Tablet | Not listed in source data |
| ANDA212541 | Pyrazinamide (Macleods Pharmaceuticals Limited) | Tablet | Not listed in source data |
| ANDA080157 | Pyrazinamide (Novitium Pharma LLC) | Tablet | Not listed in source data |

Only the oral tablet form is on the market.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for infectious otitis media rests on a model score alone (L5), with no trials or literature. Pyrazinamide has no plausible activity against common bacterial otitis media. The only credible signal is tuberculous otitis media, which is already treated with standard anti-TB regimens and is better handled as a separate, narrower research question.

**To proceed, the following is needed:**
- The package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (MOA)
- The approved indication text for the US licenses, to confirm the label context
- If pursued, a narrower question limited to culture- or PCR-confirmed tuberculous otitis media, supported by a systematic review of the existing case reports
- Confirmation that the prediction is not a knowledge-graph artifact for the non-tuberculous, allergic, and non-infectious ear conditions (non-suppurative otitis media, allergic otitis media, cholesterol granuloma)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

