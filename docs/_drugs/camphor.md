---
layout: default
title: Camphor
parent: 僅模型預測 (L5)
nav_order: 488
evidence_level: L5
indication_count: 10
---

# Camphor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Camphor: From Topical Counter-Irritant to Migraine Disorder

## One-Sentence Summary

Camphor (DB01744) is a naturally occurring bicyclic monoterpenoid traditionally used as a topical counter-irritant and local analgesic, found in over-the-counter products such as Tiger Balm and Vicks VapoRub.
The TxGNN model predicts it may have therapeutic potential for **migraine disorder** with a prediction score of **99.85%**,
however current supporting evidence is very limited, comprising **0 registered clinical trials** and **5 publications**—none of which directly evaluate camphor as a migraine treatment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formal approval on record; traditionally used as topical counter-irritant and local analgesic |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on published pharmacology, camphor is known to act as a partial agonist at TRPV1 (transient receptor potential vanilloid 1) and a modulator of TRPM8 channels. Both ion channels play established roles in the trigeminovascular pathway: TRPV1 activation on trigeminal nerve endings can influence CGRP (calcitonin gene-related peptide) release, a key mediator of migraine pain, while TRPM8 is implicated in the cooling/analgesic sensation that may counteract nociceptive signalling. This dual channel activity provides a plausible—if speculative—mechanistic bridge to migraine pathophysiology.

Camphor's historical use in topical preparations (Tiger Balm, menthol-camphor ointments) for headache relief provides weak indirect support. This counter-irritant tradition is consistent with a TRPV1/TRPM8 mechanism producing peripheral desensitisation of trigeminal afferents. However, this application has never been formally separated from the multi-ingredient formulation context, and systemic bioavailability of topically applied camphor has not been studied in the context of central migraine pathways.

Critically, two of the five retrieved publications (PMID 35856604, PMID 34373243) report the **opposite** signal: cluster headache temporally associated with toothpastes containing camphor essential oil, attributed to its pro-convulsant properties. Camphor is known to be a GABA-A antagonist at higher concentrations, which raises a direct mechanistic concern regarding its use in a headache-prone population. The TxGNN prediction may be driven by structural or network similarities that do not translate to clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) | 2022 | Case Series | Headache | Five cases of cluster headache attributed to toothpastes containing pro-convulsant essential oils including camphor — adverse signal, not therapeutic |
| [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/) | 2021 | Case Report | BMJ Case Reports | Two cases of cluster headache temporally related to use of toothpastes with camphor and eucalyptus essential oils — adverse signal |
| [36404301](https://pubmed.ncbi.nlm.nih.gov/36404301/) | 2022 | RCT | The Journal of Headache and Pain | Phase 3 DRAGON study of **erenumab** for chronic migraine in Asia — unrelated to camphor; included by search term overlap |
| [27058833](https://pubmed.ncbi.nlm.nih.gov/27058833/) | 2016 | Historical Review | Zeitschrift für Kinder- und Jugendpsychiatrie | Historical overview of neuropsychopharmacotherapy in the 1940s–50s; mentions multiple agents including camphor-class compounds |
| [593588](https://pubmed.ncbi.nlm.nih.gov/593588/) | 1977 | Clinical Note | Minerva Medica | Early clinical note on therapy for essential hemicrania; abstract not available for detailed assessment |

> ⚠️ **Evidence Quality Note**: Two publications report camphor as a *trigger* for cluster headache rather than a treatment. One RCT (PMID 36404301) concerns erenumab and is unrelated to camphor. Effective evidence directly supporting camphor's efficacy in migraine is absent.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Additional concern identified from literature**: Two case series/reports (PMID 35856604, PMID 34373243) document cluster headache triggered by products containing camphor essential oil. Camphor is known to lower seizure threshold via GABA-A antagonism at higher doses. In populations with migraine — who may already carry elevated neuronal excitability — camphor's pro-convulsant properties represent a potential safety concern that would need to be characterised before any clinical development could proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score, and a theoretical mechanistic basis through TRPV1/TRPM8 modulation exists, but the available literature not only fails to demonstrate efficacy—it contains adverse signals of camphor *worsening* headache disorders. Without preclinical dose-response data distinguishing analgesic from pro-convulsant effects, clinical development cannot be responsibly initiated.

**To proceed, the following is needed:**

- **Preclinical dose-response studies** in validated migraine animal models (e.g., nitroglycerin-induced trigeminovascular activation) to establish whether a therapeutic window exists between analgesic and pro-convulsant doses
- **MOA characterisation**: Confirm TRPV1/TRPM8 activity profile, CGRP modulation data, and central vs. peripheral selectivity at relevant dose ranges
- **Formulation feasibility assessment**: Determine whether a systemic or novel CNS-targeted route (intranasal?) can deliver camphor at sub-convulsant but therapeutically active concentrations
- **Safety pharmacology package**: Seizure liability studies (irwin test, pentylenetetrazol threshold model) before any human volunteer exposure
- **Signal separation from CAMPHOR questionnaire data pollution**: Confirm that the TxGNN training signal for pulmonary hypertension and related indications is not contaminating migraine pathway scores via the "CAMPHOR" abbreviation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

