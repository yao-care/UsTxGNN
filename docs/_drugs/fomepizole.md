---
layout: default
title: Fomepizole
parent: Model Prediction Only (L5)
nav_order: 734
evidence_level: L5
indication_count: 1
monitor_inn: "FOMEPIZOLE"
predicted_indications: ["sclerosing cholangitis"]
last_modified_at: 2026-10-28
description: "Fomepizole: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: No approved indication text is available in the US license records (g…"
---

# Fomepizole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Fomepizole: From Ethylene Glycol/Methanol Poisoning to Sclerosing Cholangitis
{: .text-alpha }

## One-Sentence Summary

Fomepizole is an injectable alcohol dehydrogenase inhibitor, known as an antidote for ethylene glycol and methanol poisoning.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication text is available in the US license records (general pharmacology: antidote for ethylene glycol and methanol poisoning) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 0.9928 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 4 of 4) |
| Number of NDAs | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, fomepizole is a competitive inhibitor of alcohol dehydrogenase and is used as an antidote in ethylene glycol and methanol poisoning.

Sclerosing cholangitis is a chronic, cholestatic, immune-mediated biliary disease. No plausible mechanistic link between alcohol dehydrogenase inhibition and this disease can be established from the available data. One speculative route is alcohol dehydrogenase-mediated metabolism or oxidative stress in the biliary epithelium, but nothing in the data supports it, so it should not be treated as a finding.

The score is very high and has no corroboration. It may reflect TxGNN model (deep learning) artifacts and should be verified before any further work.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA078537 (Cancelled) | Fomepizole (Navinta LLC) | Injection, solution | Not specified |
| ANDA078368 (Cancelled) | Fomepizole (American Regent, Inc.) | Injection, solution | Not specified |
| ANDA216791 (Cancelled) | Fomepizole (Gland Pharma Limited) | Injection | Not specified |
| ANDA078639 (Cancelled) | Fomepizole (Mylan Institutional LLC) | Injection, solution | Not specified |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: kidney disease, pyoureter, liver disease, gallbladder disease. These come from drug-disease contraindication edges in the TxGNN knowledge graph and need verification against the package insert. Liver and gallbladder disease are especially relevant to a biliary indication.
- **Drug Interactions**: **Ethanol**, Major severity. This is expected, since fomepizole inhibits alcohol dehydrogenase, the enzyme that metabolizes ethanol.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a computational prediction score. There are no clinical trials or publications, no mechanism data, and no plausible mechanistic link to sclerosing cholangitis. The drug is marketed in the US, with 4 of 4 licenses valid.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank) and a mechanistic rationale linking alcohol dehydrogenase inhibition to biliary disease
- Verification that the prediction is not a TxGNN model (deep learning) artifact, plus a literature and trial search with broader terms
- Preclinical evidence in a cholangitis model, if the prediction survives verification
- Clarification of the original indication text and the reason for the cancelled licenses
- Route compatibility assessment (the product is injectable only)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

