---
layout: default
title: Ciclesonide
parent: Model Prediction Only (L5)
nav_order: 528
evidence_level: L5
indication_count: 6
monitor_inn: "CICLESONIDE"
predicted_indications: ["atopic eczema", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "bronchitis", "contact dermatitis", "asthma-related traits, susceptibility to"]
last_modified_at: 2026-10-14
description: "Ciclesonide: predicted new indication Atopic eczema (evidence level L5). Approved use: Asthma, allergic asthma, allergic rhinitis, vasomotor rhinitis"
---

# Ciclesonide
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

# Ciclesonide: From Asthma and Allergic Rhinitis to Atopic Eczema

## One-Sentence Summary

Ciclesonide is an inhaled and intranasal corticosteroid prodrug, originally used to treat asthma and allergic rhinitis.
The TxGNN model predicts it may be effective for **atopic eczema**, but **0 clinical trials** and **0 publications** currently support this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, allergic asthma, allergic rhinitis, vasomotor rhinitis (from the knowledge graph; the US label indication text is empty) |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, ciclesonide is an inhaled corticosteroid prodrug. It is converted in the body to the active metabolite des-ciclesonide, which acts as a glucocorticoid receptor agonist with anti-inflammatory activity. Its efficacy in allergic airway disease (asthma, allergic rhinitis) is established.

Atopic eczema is a chronic allergic inflammatory skin disease, and topical corticosteroids are standard therapy for it. A glucocorticoid anti-inflammatory mechanism is therefore plausible. The same rationale applies to the closely related predictions "dermatitis, atopic" (essentially the same disease, score 99.73%) and "contact dermatitis" (score 99.25%).

However, the plausibility comes from class-level pharmacology, not from ciclesonide-specific data. Ciclesonide's available forms are an inhaler and a nasal spray, not skin products, and route compatibility has not been assessed. Other predictions in the list are of limited meaning as repurposing targets:
- "2-hydroxyethyl methacrylate sensitization" is an allergic state rather than a typical treatment target.
- "Asthma-related traits, susceptibility to" is a genetic trait that mostly reflects the existing asthma indication.

## Clinical Trial Evidence

Currently no related clinical trials registered for atopic eczema.

## Literature Evidence

Currently no related literature available for atopic eczema.

For other predicted indications, the data compiled for this report contain only indirect items:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Review (guideline) | Basic & Clinical Pharmacology & Toxicology | Finnish guideline on diagnosis and pharmacotherapy of stable COPD (predicted indication: bronchitis). Indirect relevance only; no ciclesonide-specific evidence evident. |
| [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/) | 2012 | Case report | Contact Dermatitis | Systemic allergic dermatitis caused by inhaled budesonide, with cross-reactivity on patch testing to ciclesonide (predicted indication: contact dermatitis). This is a hypersensitivity signal, not evidence of benefit. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021658 (cancelled) | Alvesco | Aerosol, metered | Not available |
| NDA022004 (cancelled) | Omnaris | Spray | Not available |

Both products were marketed by Covis Pharma US, Inc. and both authorizations are cancelled.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: herpes simplex virus keratitis, adrenocortical insufficiency, Addison disease, osteoporosis, postmenopausal osteoporosis, fungal infectious disease, dermatophytosis, ocular hypertension, glaucoma, parasitic infection. These are model-derived associations and need confirmation against the package insert.
- **Drug Interactions**: 63 interactions were identified. The main ones are:
  - **Major**: cladribine.
  - **Moderate**: clarithromycin, miconazole, cobicistat, fostamatinib, abametapir (topical), fosamprenavir, atazanavir, amprenavir, ceritinib, boceprevir, conivaptan, and inhaled human insulin. Several of these are CYP3A4 inhibitors, which may raise corticosteroid exposure.
  - **Minor**: formoterol, salbutamol, arformoterol.
- **Hypersensitivity**: a case report documents cross-reactivity between budesonide and ciclesonide on patch testing, so corticosteroid contact allergy is a consideration.

Please refer to the package insert for warnings and contraindications, as this information was not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.96%), and the glucocorticoid mechanism is plausible for atopic eczema. However, there are no clinical trials or publications for this indication (evidence level L5). The US authorizations are all cancelled, label warnings are missing, and the available dosage forms (inhaler, nasal spray) are not suited to skin use.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search specific to ciclesonide in atopic dermatitis
- Assessment of route and formulation compatibility (topical delivery versus the existing inhaled and nasal forms)
- Comparison with established topical corticosteroids to judge any added value
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

