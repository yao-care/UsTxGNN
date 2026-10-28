---
layout: default
title: Mecamylamine
parent: Model Prediction Only (L5)
nav_order: 890
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
monitor_inn: "MECAMYLAMINE"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
description: "Mecamylamine: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Mecamylamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Mecamylamine: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Mecamylamine is an oral ganglionic blocker, originally used to treat hypertension.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9914 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, mecamylamine is a non-competitive nicotinic acetylcholine receptor (ganglionic) antagonist. By blocking autonomic ganglia it lowers sympathetic tone and blood pressure, which is why it was used in hypertension.

The new indication is also a form of severe hypertension, so the prediction is plausible on the surface. Ganglionic blockade was historically used in malignant hypertension. However, malignant renovascular hypertension is driven largely by activation of the renin-angiotensin system and renal artery stenosis, which ganglionic blockade does not address directly. The high TxGNN score most likely reflects similarity to the already-approved hypertension indication rather than independent evidence.

Other predictions for this drug are weaker still:
- **Malignant hypertensive renal disease** (score 0.9914): same rationale as above, with no trials or literature. Modern agents (RAAS inhibitors, calcium channel blockers, IV vasodilators) are better characterized.
- **Pulmonary hypertension with unclear multifactorial mechanism** (score 0.9909): no direct mechanistic link was identified, and systemic hypotension could be harmful in right-ventricle-dependent disease.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 0.9909): only indirect preclinical literature on nicotinic signalling in hypoxia (see below).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence


For the fourth prediction (pulmonary hypertension owing to lung disease and/or hypoxia), 20 publications were retrieved. All are preclinical or in vitro studies, and none evaluates mecamylamine in pulmonary hypertension. Representative examples:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9074969](https://pubmed.ncbi.nlm.nih.gov/9074969/) | 1997 | Preclinical (cat) | J Appl Physiol | Tested mecamylamine and a muscarinic blocker on carotid body chemotransduction of hypoxia |
| [16357082](https://pubmed.ncbi.nlm.nih.gov/16357082/) | 2006 | Preclinical (rat) | J Appl Physiol | After chronic hypoxia, mecamylamine no longer inhibited carotid sinus nerve activity evoked by acute hypoxia |
| [10811733](https://pubmed.ncbi.nlm.nih.gov/10811733/) | 2000 | Preclinical (rat) | J Physiol | ATP and ACh co-release mediates hypoxic signalling; nicotinic blockade (mecamylamine) only partially inhibited responses |
| [16444287](https://pubmed.ncbi.nlm.nih.gov/16444287/) | 2006 | Preclinical (rat) | Br J Pharmacol | Nicotinic receptors with alpha4 subunits induce adenosine release in the carotid body; mecamylamine among antagonists tested |
| [15649879](https://pubmed.ncbi.nlm.nih.gov/15649879/) | 2005 | Preclinical (rat) | J Appl Physiol | Effect of chronic hypoxia on cholinergic chemotransmission in the carotid body |
| [19762524](https://pubmed.ncbi.nlm.nih.gov/19762524/) | 2009 | Not classified | J Appl Physiol | Nicotinic receptors do not mediate excitatory transmission in young rat carotid body |
| [12189247](https://pubmed.ncbi.nlm.nih.gov/12189247/) | 2002 | Not classified | J Clin Invest | Mecamylamine inhibited endothelial network formation, supporting a non-neuronal nicotinic angiogenic pathway |
| [37169144](https://pubmed.ncbi.nlm.nih.gov/37169144/) | 2023 | Preclinical (in vitro) | Eur J Pharmacol | Nicotine activates HIF-1α via nicotinic receptors in lung cancer cells |
| [26361040](https://pubmed.ncbi.nlm.nih.gov/26361040/) | 2015 | Not classified | PLoS One | HIF-1α and nicotinic receptors in smoke-induced bronchopulmonary dysplasia in mice |
| [35581520](https://pubmed.ncbi.nlm.nih.gov/35581520/) | 2022 | Preclinical (rat) | Mol Neurobiol | Prenatal hypoxia affects nicotine consumption and withdrawal in adult rats |

These studies offer plausible biology for nicotinic involvement in hypoxic responses but do not support mecamylamine as a treatment for pulmonary hypertension. Several other retrieved papers (e.g., huperzine A, physostigmine, vinpocetine) are tangential and appear to be keyword matches.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA204054 (cancelled) | Vecamyl (TILDE Sciences LLC) | Tablet (oral) | Not listed in the compiled data |

## Safety Considerations

- **Drug Interactions**: 42 interactions were recorded. The 20 listed in the compiled data are all rated Moderate, including:
  - Sympathomimetics: epinephrine, ephedrine (including nasal), phenylephrine
  - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
  - Prostacyclin-pathway drugs: epoprostenol, iloprost, selexipag, treprostinil
  - Alkalinizing agents: sodium bicarbonate, sodium citrate, sodium acetate, potassium citrate, tromethamine
  - Others: amifostine, promethazine, nitrous acid
- **Autonomic adverse effects**: the analysis of the predictions notes orthostatic hypotension, constipation and urinary retention as significant concerns with ganglionic blockade.

Please refer to the package insert for warnings and contraindications, as this information was not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (Evidence Level L5), with no clinical trials or direct literature.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any clinical or mechanistic evidence specific to mecamylamine in malignant or renovascular hypertension
- Assessment of whether any demonstrated benefit would exceed that of current standard therapies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

