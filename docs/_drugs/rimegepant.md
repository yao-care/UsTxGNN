---
layout: default
title: Rimegepant
parent: Model Prediction Only (L5)
nav_order: 1125
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Rimegepant: predicted new indication Migraine with brainstem aura (evidence level L5). Approved use: Migraine disorder"
monitor_inn: "RIMEGEPANT"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis", "heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis"]
---

# Rimegepant
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Rimegepant: From Migraine to Migraine with Brainstem Aura
{: .text-alpha }

## One-Sentence Summary

Rimegepant is an oral CGRP receptor antagonist, originally used for the acute and preventive treatment of migraine.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**, a subtype of migraine.
Currently there are **0 registered clinical trials** and **17 publications** on rimegepant in migraine generally, none of which specifically addresses brainstem aura.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine disorder; migraine with or without aura (the US license record has no indication text, so this comes from the knowledge graph) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 (see the note in the next section) |
| US Market Status | Cancelled only (the single NDA is recorded as cancelled; this should be verified) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the literature, rimegepant is a small-molecule calcitonin gene-related peptide (CGRP) receptor antagonist. It is approved for the acute treatment of migraine with or without aura and for the preventive treatment of episodic migraine in adults.

Migraine with brainstem aura is a subtype of migraine. It shares the CGRP-mediated trigeminovascular pathophysiology of the approved indication, so the prediction is biologically plausible. However, this is essentially a subtype of the original indication rather than a true repurposing. The literature retrieved covers migraine in general (reviews, Phase 3 and Phase 4 safety studies, a meta-analysis), and none of it addresses brainstem aura specifically. The evidence is therefore indirect.

The evidence level is L4 as assigned in the data compiled for this report. Strictly by the L1-L5 rules, the studies found are indirect and do not fit L1-L3 for this specific subtype.

Other predictions with scores above 99.5% (atrophoderma vermiculata, ulerythema ophryogenesis, heparin cofactor 2 deficiency, antithrombin deficiency type 2, factor 5 excess with spontaneous thrombosis) have no identifiable mechanistic link to CGRP receptor antagonism. They have no trials or literature and are likely model artifacts. They are not evaluated further here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The papers below concern rimegepant in migraine in general. None is specific to brainstem aura.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42143245](https://pubmed.ncbi.nlm.nih.gov/42143245/) | 2026 | Systematic review/meta-analysis | J Headache Pain | Efficacy and tolerability of a single 75 mg oral dose of rimegepant vs placebo for acute migraine attacks in adults |
| [41066271](https://pubmed.ncbi.nlm.nih.gov/41066271/) | 2025 | Phase 3 open-label | Cephalalgia | Long-term safety and effectiveness of rimegepant 75 mg ODT for acute migraine in Chinese adults |
| [41366286](https://pubmed.ncbi.nlm.nih.gov/41366286/) | 2025 | Phase 4 open-label | J Headache Pain | 24-week safety and tolerability of once-daily 75 mg rimegepant for episodic migraine prevention |
| [36739335](https://pubmed.ncbi.nlm.nih.gov/36739335/) | 2023 | Review | CNS Drugs | Rimegepant was more effective than placebo in pivotal Phase 3 trials for acute and preventive migraine treatment |
| [35790906](https://pubmed.ncbi.nlm.nih.gov/35790906/) | 2022 | Network meta-analysis | J Headache Pain | Relative efficacy of lasmiditan vs rimegepant and ubrogepant for acute migraine |
| [38307667](https://pubmed.ncbi.nlm.nih.gov/38307667/) | 2024 | Review | Handb Clin Neurol | Overview of second-generation gepants (ubrogepant, rimegepant) for acute migraine |
| [32270407](https://pubmed.ncbi.nlm.nih.gov/32270407/) | 2020 | Review | Drugs | First approval of rimegepant ODT as an acute migraine treatment |
| [41133671](https://pubmed.ncbi.nlm.nih.gov/41133671/) | 2026 | Phase 1 open-label | Headache | Pharmacokinetics, safety and tolerability of a single dose in children aged 6 to under 12 with migraine |
| [37904724](https://pubmed.ncbi.nlm.nih.gov/37904724/) | 2024 | Phase 1 | Clin Pharmacol Drug Dev | Pharmacokinetics, safety and tolerability of 75 mg were similar in elderly and nonelderly adults |
| [41574090](https://pubmed.ncbi.nlm.nih.gov/41574090/) | 2026 | Longitudinal imaging study | Brain Commun | Effect of rimegepant on cerebral and extracerebral arteries during migraine attacks, as a non-vasoconstrictive alternative to triptans |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212728 (cancelled) | NURTEC ODT | Orally disintegrating tablet | No indication text recorded |

---

## Safety Considerations

- **Drug Interactions**: 57 interacting drugs were identified. The examples listed are Major unless noted.
  - Major: dexamethasone, lumacaftor, apalutamide
  - Moderate: aprepitant, clarithromycin, rolapitant, sulfasalazine, cobicistat, eltrombopag, ivacaftor, chloramphenicol, erythromycin, fluconazole, ketoconazole, tacrolimus
  - Most of the interactions listed are with CYP3A4 modulators or similar agents, so co-medications should be reviewed.
- **Other literature signals**: A multinational cohort study (2026) examined glaucoma risk with CGRP inhibitors in migraine. Rimegepant has been studied in older adults, children and adolescents, but these studies do not address brainstem aura.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is plausible, but it is essentially a subtype of the approved migraine indication rather than a new use. No trial or publication addresses brainstem aura specifically, and the US NDA is recorded as cancelled, which needs verification.

**To proceed, the following is needed:**
- Verify the current US market status of NURTEC ODT (NDA212728) and the reason it is recorded as cancelled
- Obtain the FDA package insert warnings and contraindications, which are currently missing and block safety screening
- Obtain detailed mechanism of action data (for example from DrugBank)
- Find or generate evidence specific to migraine with brainstem aura, such as subgroup analyses of the existing Phase 3 trials or a dedicated study
- Review the drug-interaction profile, especially the Major interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

