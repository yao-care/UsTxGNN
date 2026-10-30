---
layout: default
title: Iloprost
parent: Model Prediction Only (L5)
nav_order: 790
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
monitor_inn: "ILOPROST"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "pulmonary arteriovenous malformation (disease)", "diffuse alopecia areata"]
description: "Iloprost: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Not recorded in the local data"
---

# Iloprost
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Iloprost: Hypotrichosis simplex of the scalp
{: .text-alpha }

## One-Sentence Summary

Iloprost is a prostacyclin analog originally used to treat pulmonary arterial hypertension (PAH).
with **no registered clinical trials** but **20 publications** (mostly observational studies, case series, and reviews) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

This report focuses on the highest-ranked prediction with meaningful supporting evidence (rank 3).*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, iloprost is a prostacyclin (IP receptor) analog that causes pulmonary vasodilation and inhibits platelet aggregation and vascular smooth muscle proliferation. Its efficacy in PAH is established, which is the original indication.

PAH associated with congenital heart disease (CHD-PAH) is a recognized subgroup of PAH. It shares the same pulmonary vascular pathology (vasoconstriction, remodeling, and proliferation), so the mechanistic link to the original indication is direct. Published studies have examined inhaled iloprost in children and adults with CHD-PAH, including patients with Eisenmenger syndrome.

The evidence is mostly observational or small-scale, so the extrapolation is plausible but not confirmed by randomized trials. Shunt physiology in congenital heart disease needs particular attention.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31371115](https://pubmed.ncbi.nlm.nih.gov/31371115/) | 2020 | Randomized, placebo-controlled, double-blind cross-over pilot | Int J Cardiol | Nebulised iloprost in Eisenmenger syndrome (the most severe form of CHD-PAH); single-centre pilot study |
| [28608969](https://pubmed.ncbi.nlm.nih.gov/28608969/) | 2017 | Cohort | Clin Exp Pharmacol Physiol | Effect of iloprost on endothelial-dysfunction biomarkers (NO, ET-1, ADMA, Gal-3, BNP, UA) in CHD-PAH |
| [29426959](https://pubmed.ncbi.nlm.nih.gov/29426959/) | 2018 | Cohort | Pediatr Cardiol | Safety and acute haemodynamic effects of inhaled iloprost in children with PAH and simple congenital heart defects |
| [27492657](https://pubmed.ncbi.nlm.nih.gov/27492657/) | 2017 | Cohort | J Cardiol | Effect of long-term inhaled iloprost on right ventricular function in Eisenmenger syndrome |
| [24729548](https://pubmed.ncbi.nlm.nih.gov/24729548/) | 2015 | Cohort (retrospective) | Pediatr Pulmonol | Long-term effects of inhaled iloprost in children with pulmonary hypertension |
| [36010107](https://pubmed.ncbi.nlm.nih.gov/36010107/) | 2022 | Case series | Children (Basel) | Add-on combination of sildenafil, bosentan, and iloprost in 5 patients with Eisenmenger syndrome |
| [30719004](https://pubmed.ncbi.nlm.nih.gov/30719004/) | 2018 | Prospective study | Front Pharmacol | Acute inhaled iloprost improved right ventricle function in 69 PAH patients (cardiac MRI) |
| [19436672](https://pubmed.ncbi.nlm.nih.gov/19436672/) | 2009 | Review | Vasc Health Risk Manag | Review of inhaled iloprost for PAH in children |
| [18260882](https://pubmed.ncbi.nlm.nih.gov/18260882/) | 2007 | Review | Kardiologiia | Controlled trials of prostacyclin and analogues in PAH, including PAH associated with congenital heart disease |
| [22621693](https://pubmed.ncbi.nlm.nih.gov/22621693/) | 2012 | Review | Drugs | Treatment of PAH in connective tissue disease, including discussion of associated PAH subgroups |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA217933 (cancelled) | AURLUMYN | Injection, solution | Not available |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: liver failure, chronic obstructive pulmonary disease, severe early-onset COPD, hypotensive disorder, pulmonary edema, and bronchial disease.
- **Drug Interactions**: 100 interactions were identified in total. The main moderate-level ones include:
  - Epinephrine, ephedrine, and ephedrine (nasal)
  - Acetylsalicylic acid
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
  - Inhaled rapid-acting insulin
  - Mannitol and glycerin
  - Papaverine
  - Fenfluramine, dexfenfluramine, and sibutramine

For label-based warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is the same as in the approved PAH indication, and several cohort studies, a small randomized cross-over pilot, and case series support use in CHD-PAH. However, there are no registered trials and no Phase 3 RCT evidence, so the evidence level is L3. The only US authorization is cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (MOA) from DrugBank
- Confirmation of a currently marketed US iloprost product, since the only NDA listed is cancelled
- Patient selection criteria, hemodynamic monitoring, and attention to shunt physiology
- A prospective controlled study in CHD-PAH, ideally in specialist centers

**Other predictions (not recommended at this stage):**
- Supported by long-term intravenous iloprost outcomes (PMID 27651181) and reviews.
- **PAH associated with schistosomiasis (rank 7) and HIV infection (rank 8)**: L4, Research Question. Only indirect evidence.
- **PAH associated with chronic hemolytic anemia (rank 5)**: L5, Hold. No direct evidence, and the disease drivers differ.
- **Pulmonary arteriovenous malformation (rank 4)**: L5, Hold. There is a theoretical safety concern, because vasodilators could worsen right-to-left shunting.
- **Hair disorders (ranks 1, 2, and 9)**: L5, Hold. Computational prediction only, with no plausible mechanism.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

